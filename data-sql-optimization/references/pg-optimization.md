# PostgreSQL-Specific Optimization

## Reading EXPLAIN ANALYZE Output

Every optimization starts here. Run with all options:

```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) 
SELECT ...;
```

`BUFFERS` shows cache hits vs disk reads — often the real bottleneck.

### Node-by-Node Breakdown

```
Seq Scan on orders  (cost=0.00..18340.00 rows=850000 width=72)
                     (actual time=0.043..312.451 rows=850000 loops=1)
  Buffers: shared hit=3340 read=5000
```

| Field | Meaning | Watch For |
|-------|---------|-----------|
| `cost=A..B` | Planner estimate: startup cost .. total cost | A/B are in arbitrary planner units |
| `actual time=A..B` | Real ms: first row .. last row | `B` is what matters for latency |
| `rows=N` (estimate vs actual) | Planner guessed N, actually got M | Ratio > 10× means stale statistics |
| `loops=N` | Node executed N times | Nested loop with large N is expensive: multiply `actual time` by `loops` |
| `shared hit=N` | Pages served from `shared_buffers` (RAM) | High hit = good |
| `shared read=N` | Pages read from OS/disk | High read = I/O bottleneck |

**The most important calculation**: actual total time × loops = real cost of a node.

```
Nested Loop  (actual time=0.02..0.15 loops=50000)
```
This node actually cost `0.15ms × 50000 = 7500ms`. A single-node bottleneck.

### Identifying the Bottleneck Node

In a large plan, find the worst node:

1. Look for the node with the largest `actual time` on the right side
2. Look for `Seq Scan` on tables with `rows=` in the millions
3. Look for `loops=` that multiplies small times into large totals
4. Look for `Sort` nodes that exceed `work_mem` (they spill to disk)

Spill indicator:
```
Sort  (actual time=1234.5..1456.7 rows=500000 loops=1)
  Sort Key: created_at
  Sort Method: external merge  Disk: 48256kB   ← spilled to disk
```
Fix: increase `work_mem` for this session, or add an index to eliminate the sort.

---

## pg_stat_statements — Find Slow Queries First

Before opening EXPLAIN, identify which queries to investigate.

### Setup

```sql
-- postgresql.conf (requires restart)
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.track = all

-- Then in your database:
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

### Query: Top 10 by Total Time

```sql
SELECT
    round(total_exec_time::numeric, 2)          AS total_ms,
    calls,
    round(mean_exec_time::numeric, 2)           AS mean_ms,
    round(stddev_exec_time::numeric, 2)         AS stddev_ms,
    round((total_exec_time / sum(total_exec_time) OVER ()) * 100, 2) AS pct_total,
    left(query, 120)                            AS query_snippet
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

**Interpretation**:
- High `total_ms` + low `calls` = one expensive query, optimize the query itself
- High `total_ms` + high `calls` + low `mean_ms` = N+1 or chatty pattern, fix the caller
- High `stddev_ms` = inconsistent performance, likely plan instability or cache misses

### Reset After Deploying a Fix

```sql
SELECT pg_stat_statements_reset();
```

Wait for traffic to accumulate (15–30 minutes in production), then re-query to confirm improvement.

---

## Index Types: When to Use Each

### B-Tree (Default)

```sql
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

Handles: `=`, `<`, `<=`, `>`, `>=`, `BETWEEN`, `IN`, `IS NULL`, `ORDER BY`.

Does NOT help: `LIKE '%suffix%'`, full-text search, array containment.

### Partial Index

Index only the rows you actually query. Smaller, faster, less write overhead.

```sql
-- Only index pending orders, not the millions of completed ones
CREATE INDEX idx_orders_pending 
ON orders(created_at) 
WHERE status = 'pending';
```

Query must include the `WHERE` predicate for the planner to use this index:

```sql
-- Uses idx_orders_pending
SELECT * FROM orders WHERE status = 'pending' AND created_at > now() - interval '7 days';

-- Does NOT use it (no status filter)
SELECT * FROM orders WHERE created_at > now() - interval '7 days';
```

**Decision rule**: if a column has a skewed distribution (e.g., 95% `completed`, 5% `pending`) and you only query the minority value, use a partial index.

### Covering Index (INCLUDE)

PostgreSQL 11+. Avoids a second heap fetch by storing extra columns in the index leaf.

```sql
-- Without INCLUDE: index scan finds user_id rows, then heap-fetches status + total
CREATE INDEX idx_orders_user ON orders(user_id);

-- With INCLUDE: index scan returns all three columns, no heap fetch needed
CREATE INDEX idx_orders_user_covering 
ON orders(user_id) 
INCLUDE (status, total_amount);
```

EXPLAIN will show `Index Only Scan` instead of `Index Scan` — the former never touches the heap.

Use when: a query filters on column A and selects only columns A + B + C (narrow projections).

### GIN — Arrays and Full-Text

```sql
-- Array containment
CREATE INDEX idx_products_tags ON products USING gin(tags);
SELECT * FROM products WHERE tags @> ARRAY['organic', 'vegan'];

-- Full-text search
CREATE INDEX idx_articles_tsv ON articles USING gin(to_tsvector('english', body));
SELECT * FROM articles WHERE to_tsvector('english', body) @@ plainto_tsquery('english', 'database optimization');

-- Trigram similarity (requires pg_trgm extension)
CREATE EXTENSION pg_trgm;
CREATE INDEX idx_products_name_trgm ON products USING gin(name gin_trgm_ops);
SELECT * FROM products WHERE name ILIKE '%organic%';  -- now uses index
```

GIN indexes are large and slow to build. Trade-off: fast reads, slow writes.

### BRIN — Time-Series Large Tables

Block Range INdex. Stores min/max value per physical block group. Tiny index (kilobytes vs gigabytes for B-Tree), but only works when data is physically correlated with the indexed column.

```sql
-- Events table inserted in timestamp order — BRIN works perfectly
CREATE INDEX idx_events_created_brin ON events USING brin(created_at);
```

BRIN is useless if rows are inserted out of order for the indexed column. Check with:

```sql
SELECT correlation FROM pg_stats 
WHERE tablename = 'events' AND attname = 'created_at';
-- correlation close to 1.0 or -1.0 = BRIN will work
-- correlation close to 0 = BRIN useless, use B-Tree
```

---

## Composite Index Column Order

**Rule**: filter columns before sort/range columns; highest-cardinality filter first.

Given query:
```sql
SELECT * FROM orders 
WHERE status = 'pending'       -- low cardinality: 3 values
  AND user_id = 42             -- high cardinality: millions of users
ORDER BY created_at DESC;
```

| Index | Selectivity | Verdict |
|-------|------------|---------|
| `(status, user_id, created_at)` | Filters status first (3 values), then user_id | Poor — status is too broad |
| `(user_id, status, created_at)` | Filters user_id first (highly selective), then status, then sorted | Good |
| `(user_id, created_at)` | Filters user_id, range scan on date | OK if status selectivity is low |

The planner can use a composite index for a prefix of columns, but not a suffix. `INDEX(a, b, c)` supports queries on `(a)`, `(a, b)`, `(a, b, c)` — but not `(b)` or `(c)` alone.

---

## Configuration Parameters That Affect Query Plans

These can be set per-session without a restart:

```sql
SET work_mem = '256MB';      -- affects sorts and hash joins for THIS query
SET enable_seqscan = off;    -- force planner away from seq scan (diagnostic only)
```

### work_mem

Controls memory for sort operations and hash tables **per operation per query**. A query with 3 sort nodes can use `3 × work_mem`.

```sql
-- Check current value
SHOW work_mem;

-- Set for a single expensive report query
SET work_mem = '512MB';
SELECT ... ORDER BY ... ;
RESET work_mem;
```

Signs `work_mem` is too low:
- EXPLAIN shows `Sort Method: external merge  Disk: NNkB`
- EXPLAIN shows `Hash Batches: N` where N > 1 (hash join spilled)

### random_page_cost

Default is `4.0` (assumes HDD). On SSDs or cloud block storage, set lower:

```sql
-- postgresql.conf or per-database
ALTER DATABASE mydb SET random_page_cost = 1.1;
```

With a high `random_page_cost`, the planner prefers sequential scans over index scans on larger tables. Lowering it makes the planner more willing to use indexes.

### effective_cache_size

Not actual memory allocation — just a hint to the planner about how much data the OS page cache can hold. Affects cost estimates for index scans.

```sql
-- Typical: set to ~75% of total RAM
ALTER SYSTEM SET effective_cache_size = '24GB';
```

---

## Statistics and the Planner

Stale statistics cause bad plans. The symptom: `rows=` estimate is far from `actual rows=`.

```sql
-- Update statistics for one table immediately
ANALYZE orders;

-- Check per-column statistics
SELECT attname, n_distinct, correlation, most_common_vals, most_common_freqs
FROM pg_stats
WHERE tablename = 'orders';
```

### Increasing Statistics Target

PostgreSQL samples 300 rows per column by default (`default_statistics_target = 100`). For columns with complex distributions (e.g., `user_id` with 10M distinct values):

```sql
ALTER TABLE orders ALTER COLUMN user_id SET STATISTICS 500;
ANALYZE orders;
```

Higher `STATISTICS` means better estimates but slower `ANALYZE`. Start with 500 for columns that drive major join or filter decisions.

### Extended Statistics (PostgreSQL 10+)

The planner assumes column independence. For correlated columns, create extended statistics:

```sql
-- city and zip_code are correlated: knowing city tells you zip
CREATE STATISTICS stat_city_zip ON city, zip_code FROM addresses;
ANALYZE addresses;
```

Without this, a query filtering on both `city` AND `zip_code` will have an over-estimated row count (planner multiplies selectivities independently), leading to a bad join order.

---

## VACUUM and Table Bloat

PostgreSQL's MVCC means dead tuples accumulate. Bloat causes larger table scans.

### Check Table Bloat

```sql
SELECT
    relname,
    pg_size_pretty(pg_total_relation_size(oid))   AS total_size,
    n_dead_tup,
    n_live_tup,
    round(n_dead_tup::numeric / nullif(n_live_tup + n_dead_tup, 0) * 100, 1) AS dead_pct,
    last_autovacuum,
    last_autoanalyze
FROM pg_stat_user_tables
WHERE n_live_tup > 10000
ORDER BY n_dead_tup DESC
LIMIT 20;
```

`dead_pct > 20%` on a large table is a problem. Manual vacuum:

```sql
VACUUM (ANALYZE, VERBOSE) orders;
```

`VACUUM FULL` reclaims disk space but takes an exclusive lock. Use only during maintenance windows:

```sql
-- Takes ACCESS EXCLUSIVE lock — blocks all reads and writes
VACUUM FULL orders;
```

Prefer `pg_repack` extension for online table compaction without the lock.

### Autovacuum Tuning for High-Churn Tables

Default autovacuum triggers at `20% dead tuples`. For a 100M-row table, that's 20M dead tuples before vacuum runs.

```sql
-- Lower threshold for high-churn tables
ALTER TABLE orders SET (
    autovacuum_vacuum_scale_factor = 0.01,   -- 1% instead of 20%
    autovacuum_vacuum_threshold = 1000        -- minimum 1000 dead tuples
);
```

---

## Diagnosing Index Bloat

Indexes also bloat over time. Check:

```sql
SELECT
    schemaname,
    tablename,
    indexname,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
JOIN pg_indexes USING (schemaname, tablename, indexname)
ORDER BY pg_relation_size(indexrelid) DESC
LIMIT 20;
```

Indexes with `idx_scan = 0` (or very low) after sufficient traffic are unused — drop them:

```sql
DROP INDEX CONCURRENTLY idx_orders_old_column;
```

`CONCURRENTLY` drops the index without locking the table.

---

## Lock Contention

Sometimes "slow query" is actually "query waiting for a lock."

```sql
-- See all waiting queries
SELECT
    pid,
    now() - pg_stat_activity.query_start AS duration,
    query,
    state,
    wait_event_type,
    wait_event
FROM pg_stat_activity
WHERE wait_event IS NOT NULL
  AND state = 'active'
ORDER BY duration DESC;

-- See what's blocking what
SELECT
    blocked.pid           AS blocked_pid,
    blocked.query         AS blocked_query,
    blocking.pid          AS blocking_pid,
    blocking.query        AS blocking_query
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocking
    ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
WHERE cardinality(pg_blocking_pids(blocked.pid)) > 0;
```

Common causes: long-running transactions, DDL migrations (`ALTER TABLE` takes `AccessExclusiveLock`), bulk updates without batching.

Fix for DDL: use `ALTER TABLE ... SET DEFAULT` instead of `ALTER COLUMN TYPE` where possible, or use tools like `pg_repack` that operate without full locks.

---

## Quick Decision Matrix

| Symptom | First Check | Likely Fix |
|---------|------------|-----------|
| Query is slow, always | `EXPLAIN ANALYZE` | Missing index, bad join order |
| Query is sometimes slow | `pg_stat_activity` wait events | Lock contention or plan instability |
| Query was fast, now slow | `pg_stats` row estimates | Stale stats — run `ANALYZE` |
| Seq scan on big table | Index exists but not used | `random_page_cost`, partial index condition mismatch, or statistics too low |
| Hash join spill to disk | `Sort Method: external merge` | Increase `work_mem` |
| `SELECT *` query on wide table | EXPLAIN `width=` value | Use covering index + column projection |
| Table growing indefinitely | `pg_stat_user_tables` dead tuples | Autovacuum misconfigured, long transactions blocking vacuum |
| New index not used | Check `pg_stats.correlation` | BRIN on non-correlated column; or planner prefers seq scan due to high `random_page_cost` |
