# CTE vs Temporary Table: Performance Decision Guide

## When It Matters

Both CTEs and temporary tables solve the same problem: breaking a complex query into named, reusable intermediate results. The performance difference is real but context-dependent. Wrong choice on a large table can mean 10x slower execution; right choice on a small table makes no measurable difference.

## How Each Works Internally

### CTE (Common Table Expression)

```sql
WITH monthly_sales AS (
    SELECT user_id, SUM(amount) AS total
    FROM orders
    WHERE created_at >= '2024-01-01'
    GROUP BY user_id
)
SELECT u.name, ms.total
FROM users u
JOIN monthly_sales ms ON u.id = ms.user_id
WHERE ms.total > 1000;
```

**PostgreSQL (≥ 12 by default)**: The optimizer treats the CTE as an *inlined subquery* — it can push predicates into the CTE and use indexes inside it. The CTE is **not** materialized unless the optimizer decides it's beneficial or you add `MATERIALIZED`.

**PostgreSQL (< 12) and MySQL**: CTEs are **always materialized** — the result set is computed once and stored as an anonymous temporary structure. Predicates from the outer query cannot be pushed inside.

**SQL Server**: Optimizer may or may not materialize; it's treated as a view-like rewrite with no guarantee.

### Temporary Table

```sql
CREATE TEMPORARY TABLE monthly_sales AS
SELECT user_id, SUM(amount) AS total
FROM orders
WHERE created_at >= '2024-01-01'
GROUP BY user_id;

CREATE INDEX idx_ms_user ON monthly_sales(user_id);

SELECT u.name, ms.total
FROM users u
JOIN monthly_sales ms ON u.id = ms.user_id
WHERE ms.total > 1000;
```

The result is written to disk (or memory buffer), persists for the session, and — critically — **you can add indexes to it**. The optimizer treats it like any real table with up-to-date statistics.

---

## Performance Decision Table

| Condition | Use CTE | Use Temp Table |
|-----------|---------|----------------|
| Result used once | ✓ | — |
| Result used 2+ times in same query | Depends on engine | ✓ |
| Result set < ~10K rows | ✓ | — |
| Result set > ~100K rows | — | ✓ |
| Need index on intermediate result | — | ✓ |
| Multiple joins on intermediate result | — | ✓ |
| PostgreSQL ≥ 12, optimizer can inline | ✓ | — |
| PostgreSQL < 12 (always materializes) | Functionally = temp table | ✓ (explicit control) |
| Inside a function / loop | — | ✓ |
| Ad-hoc / exploratory query | ✓ | — |
| Production scheduled job | Verify with EXPLAIN | ✓ (predictable) |

---

## The Materialization Problem

This is the core issue. Consider a CTE referenced twice:

```sql
WITH expensive_cte AS (
    SELECT * FROM orders
    WHERE status = 'completed'  -- 500K rows
)
SELECT COUNT(*) FROM expensive_cte
UNION ALL
SELECT SUM(amount) FROM expensive_cte;
```

**PostgreSQL < 12**: `expensive_cte` executes **twice** — once per reference. Total rows scanned: 1M.

**PostgreSQL ≥ 12**: The optimizer may or may not inline. If inlined, still executes twice. If auto-materialized, executes once.

**Force materialization** in PostgreSQL ≥ 12:

```sql
WITH expensive_cte AS MATERIALIZED (
    SELECT * FROM orders WHERE status = 'completed'
)
SELECT COUNT(*) FROM expensive_cte
UNION ALL
SELECT SUM(amount) FROM expensive_cte;
```

Now it executes once. But you still can't add indexes.

**Temp table equivalent** (explicit, portable, indexable):

```sql
CREATE TEMPORARY TABLE completed_orders AS
SELECT * FROM orders WHERE status = 'completed';

SELECT COUNT(*) FROM completed_orders
UNION ALL
SELECT SUM(amount) FROM completed_orders;

DROP TABLE completed_orders;
```

---

## Worked Example: When Temp Table Wins

**Scenario**: Dashboard query joining three large tables, two intermediate aggregations reused multiple times.

### Slow version with CTEs

```sql
WITH order_totals AS (               -- 2M orders → 800K users
    SELECT user_id,
           COUNT(*)        AS order_count,
           SUM(amount)     AS lifetime_value
    FROM orders
    GROUP BY user_id
),
recent_orders AS (                   -- 2M orders → 400K users
    SELECT user_id,
           MAX(created_at) AS last_order_date
    FROM orders
    WHERE created_at >= NOW() - INTERVAL '90 days'
    GROUP BY user_id
)
SELECT u.id, u.email,
       ot.order_count, ot.lifetime_value,
       ro.last_order_date,
       CASE WHEN ro.user_id IS NOT NULL THEN 'active' ELSE 'lapsed' END AS segment
FROM users u
LEFT JOIN order_totals ot ON u.id = ot.user_id
LEFT JOIN recent_orders ro ON u.id = ro.user_id
WHERE ot.lifetime_value > 500
ORDER BY ot.lifetime_value DESC;
```

**EXPLAIN ANALYZE result** (PostgreSQL 11):

```
Hash Join  (cost=85234.00..142891.00 rows=23000 width=72)
  ->  Seq Scan on users
  ->  Hash
        ->  CTE Scan on order_totals         ← full scan, no index
              ->  HashAggregate (800K rows)
                    ->  Seq Scan on orders   ← 2M rows
        ->  CTE Scan on recent_orders        ← full scan, no index
              ->  HashAggregate (400K rows)
                    ->  Seq Scan on orders   ← 2M rows again
Execution Time: 18,400 ms
```

### Fast version with temp tables

```sql
CREATE TEMPORARY TABLE order_totals AS
SELECT user_id,
       COUNT(*)    AS order_count,
       SUM(amount) AS lifetime_value
FROM orders
GROUP BY user_id;

CREATE INDEX idx_ot_user ON order_totals(user_id);
CREATE INDEX idx_ot_ltv  ON order_totals(lifetime_value);

CREATE TEMPORARY TABLE recent_orders AS
SELECT user_id, MAX(created_at) AS last_order_date
FROM orders
WHERE created_at >= NOW() - INTERVAL '90 days'
GROUP BY user_id;

CREATE INDEX idx_ro_user ON recent_orders(user_id);

SELECT u.id, u.email,
       ot.order_count, ot.lifetime_value,
       ro.last_order_date,
       CASE WHEN ro.user_id IS NOT NULL THEN 'active' ELSE 'lapsed' END AS segment
FROM users u
LEFT JOIN order_totals ot ON u.id = ot.user_id
LEFT JOIN recent_orders ro ON u.id = ro.user_id
WHERE ot.lifetime_value > 500
ORDER BY ot.lifetime_value DESC;

DROP TABLE order_totals, recent_orders;
```

**EXPLAIN ANALYZE result**:

```
Hash Join  (cost=4231.00..9870.00 rows=23000 width=72)
  ->  Seq Scan on users
  ->  Hash
        ->  Index Scan on order_totals       ← uses idx_ot_ltv for WHERE filter
        ->  Hash
              ->  Seq Scan on recent_orders  ← small table (400K), hash fits in memory
Build temp tables: 3,200 ms
Main query: 890 ms
Total: 4,090 ms  ← 4.5× faster
```

The speedup comes from:
1. `orders` scanned once (not twice)
2. `WHERE lifetime_value > 500` uses an index on the temp table, reducing the users hash from 800K to ~23K rows
3. The optimizer has accurate statistics on both temp tables

---

## Recursive CTEs: No Temp Table Equivalent

Recursive CTEs are the one case where CTEs have a capability temp tables cannot replicate cleanly:

```sql
-- Walk an org chart hierarchy
WITH RECURSIVE org_tree AS (
    -- Anchor
    SELECT id, name, manager_id, 0 AS depth
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive step
    SELECT e.id, e.name, e.manager_id, ot.depth + 1
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY depth, name;
```

You cannot replicate this with a single temp table creation; you'd need a stored procedure with a loop. Use recursive CTEs for tree traversal — performance is usually acceptable because the dataset is bounded by the hierarchy depth.

---

## PostgreSQL-Specific: `MATERIALIZED` vs `NOT MATERIALIZED`

Available in PostgreSQL 12+. Use these hints when the optimizer makes the wrong call.

```sql
-- Force materialization: result used 3+ times, expensive to recompute
WITH heavy_agg AS MATERIALIZED (
    SELECT region, SUM(revenue) AS total
    FROM sales
    GROUP BY region
)
SELECT * FROM heavy_agg WHERE total > 1000000
UNION ALL
SELECT * FROM heavy_agg WHERE total < 10000;

-- Prevent materialization: CTE used once, outer predicate should be pushed in
WITH filtered AS NOT MATERIALIZED (
    SELECT * FROM products WHERE category = 'electronics'
)
SELECT * FROM filtered WHERE price < 100;
-- Equivalent to: SELECT * FROM products WHERE category='electronics' AND price < 100
-- Allows index on (category, price) to be used
```

**Rule of thumb**:
- `MATERIALIZED` when CTE is referenced **≥ 2 times** and the computation is expensive
- `NOT MATERIALIZED` when you want the outer WHERE pushed into the CTE for index use
- Omit both and let optimizer decide when you're unsure (verify with EXPLAIN)

---

## Statistics: Why Temp Tables Are More Predictable

CTEs (when materialized) produce an anonymous result that the optimizer estimates using default statistics — often wildly wrong. Temp tables get real statistics after creation:

```sql
CREATE TEMPORARY TABLE my_temp AS
SELECT ...;

ANALYZE my_temp;  -- optional but useful for very large temp tables
                  -- PostgreSQL auto-analyzes small temp tables
```

After `ANALYZE`, the optimizer knows the row count, null fraction, and column distribution of `my_temp` exactly, leading to better join strategy choices (Nested Loop vs Hash Join vs Merge Join).

If you see bad join strategy on a CTE-based query (e.g., Nested Loop on 500K rows), switching to a temp table and letting the optimizer use real stats often fixes it without any other changes.

---

## MySQL / MariaDB Notes

MySQL (< 8.0) does not support CTEs at all. MySQL 8.0+ adds CTE support, but the optimizer always materializes CTEs — there is no `MATERIALIZED` / `NOT MATERIALIZED` hint.

For MySQL, the decision is simpler:

- Small intermediate results (< ~10K rows): CTE is fine
- Large intermediate results, reused: use temp table with explicit index

```sql
-- MySQL temp table with index
CREATE TEMPORARY TABLE order_totals (
    user_id    INT NOT NULL,
    total      DECIMAL(12,2),
    order_count INT,
    PRIMARY KEY (user_id),
    INDEX idx_total (total)
) AS
SELECT user_id, SUM(amount), COUNT(*)
FROM orders
GROUP BY user_id;
```

Note: MySQL requires declaring the temp table schema separately from `AS SELECT` if you want to add a PRIMARY KEY or INDEX at creation time.

---

## Decision Flowchart

```
Is the intermediate result used only once?
├── YES → CTE (simpler, no cleanup needed)
└── NO  → Is the result set large (>50K rows)?
          ├── NO  → CTE with MATERIALIZED (PostgreSQL 12+) or just CTE
          └── YES → Do you need to filter/join on the intermediate result?
                    ├── NO  → CTE with MATERIALIZED
                    └── YES → Temp table + index
                               (optimizer gets real stats, join uses index)
```

---

## Cleanup Discipline

Temp tables are session-scoped: they vanish when the session ends. In connection-pooled applications (PgBouncer, ProxySQL), **sessions are reused** — a temp table created in request A may still exist in request B if the same connection is reused.

Always drop explicitly:

```sql
DROP TABLE IF EXISTS order_totals;
DROP TABLE IF EXISTS recent_orders;
```

Or use `CREATE TEMPORARY TABLE IF NOT EXISTS` combined with `TRUNCATE` at the start of each use:

```sql
-- Safe pattern for pooled connections
TRUNCATE TABLE IF EXISTS order_totals;
INSERT INTO order_totals SELECT ...;
```

CTEs have no cleanup burden — another reason to prefer them for simple, one-off queries.
