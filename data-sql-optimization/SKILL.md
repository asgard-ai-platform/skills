---
name: "data-sql-optimization"
description: "Optimize SQL query performance using EXPLAIN analysis, indexing strategies, and common anti-pattern fixes. Use this skill when the user needs to speed up slow queries, design indexes, fix N+1 problems, or optimize database performance — even if they say 'this query is slow', 'optimize our database', 'which indexes do we need', or 'our dashboard takes 30 seconds to load'."
metadata:
  category: "WP-04 數據分析"
  tags: ["data-analysis", "sql", "database", "performance"]
---

# SQL Query Optimization

## Framework

```
IRON LAW: Measure Before Optimizing

NEVER guess which query is slow or why. Use EXPLAIN (EXPLAIN ANALYZE in
PostgreSQL) to see the actual execution plan. The database's plan often
differs from what you expect — a query you think is efficient may do
a full table scan, and a complex-looking query may use an index perfectly.

Measure → identify bottleneck → fix → measure again.
```

### EXPLAIN Output Reading

Key metrics in EXPLAIN ANALYZE (PostgreSQL):
| Metric | What It Means | Red Flag |
|--------|-------------|----------|
| **Seq Scan** | Full table scan | On large tables (>100K rows) |
| **Index Scan** | Using an index | Expected for filtered queries |
| **Nested Loop** | Join method (row-by-row) | On large tables without index |
| **Hash Join** | Join method (hash table) | Normal for larger tables |
| **Sort** | Sorting results | Without index support on large sets |
| **Actual Time** | Milliseconds for this step | Compare to identify bottleneck |
| **Rows** | Actual rows processed vs estimated | Large mismatch = stale statistics |

### Indexing Strategy

| When to Index | Index Type | Example |
|--------------|-----------|---------|
| WHERE clause column | B-Tree (default) | `CREATE INDEX idx_user_email ON users(email)` |
| JOIN column | B-Tree | `CREATE INDEX idx_order_user ON orders(user_id)` |
| Composite filter | Composite index | `CREATE INDEX idx_order_status_date ON orders(status, created_at)` |
| Text search | GIN / Full-text | `CREATE INDEX idx_product_name_gin ON products USING gin(name gin_trgm_ops)` |
| Range queries | B-Tree | Columns used with `BETWEEN`, `>`, `<` |

**Composite index column order matters**: Put the most selective (highest cardinality) column first. `INDEX(status, date)` is good if you always filter by status. `INDEX(date, status)` is better if you always filter by date range first.

### Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| `SELECT *` | Reads all columns, prevents index-only scans | Select only needed columns |
| Subquery in WHERE | Re-executes for each row | Rewrite as JOIN or CTE |
| `OR` in WHERE | Prevents index use | Rewrite as UNION or separate queries |
| Function on indexed column | `WHERE YEAR(date) = 2024` bypasses index | `WHERE date >= '2024-01-01' AND date < '2025-01-01'` |
| N+1 queries | 1 query for list + N queries for details | JOIN or batch query with `IN` |
| Missing pagination | Fetching all rows when only showing 20 | `LIMIT` + `OFFSET` or keyset pagination |
| Implicit type conversion | `WHERE id = '123'` (string vs int) | Use correct type: `WHERE id = 123` |

### Optimization Workflow

1. **Identify slow queries**: Database slow query log (pg_stat_statements, MySQL slow log)
2. **Run EXPLAIN ANALYZE** on the slowest
3. **Find the bottleneck**: Seq Scan on large table? Missing index? Expensive sort?
4. **Apply fix**: Add index, rewrite query, or restructure schema
5. **Verify**: Run EXPLAIN ANALYZE again — confirm improvement
6. **Monitor**: Check that fix didn't degrade other queries

### Partitioning (Large Tables)

When tables exceed millions of rows:
| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **Range partition** | Split by date range (monthly, yearly) | Time-series data, logs |
| **Hash partition** | Distribute by hash of a column | Even distribution, high-throughput |
| **List partition** | Split by specific values | Multi-tenant, status-based |

## Output Format

```markdown
# Query Optimization: {Context}

## Slow Query
```sql
{the original slow query}
```
- Execution time: {current ms}
- Rows scanned: {N}
- Problem: {what EXPLAIN revealed}

## Fix Applied
{What was changed — new index, query rewrite, etc.}

## Result
- Execution time: {original ms} → {optimized ms} ({X% improvement})
- Rows scanned: {original N} → {optimized N}
```

## Gotchas

- **Indexes have write cost**: Every INSERT/UPDATE must update all indexes. Over-indexing slows writes. Index what you query, not everything.
- **Statistics can be stale**: If EXPLAIN estimates are way off from actuals, run `ANALYZE` (PostgreSQL) or `ANALYZE TABLE` (MySQL) to update statistics.
- **Query cache hides problems**: A query may appear fast because it's cached. Test with cache cleared or cold start.
- **ORM-generated queries**: ORMs (Django, SQLAlchemy, ActiveRecord) generate SQL that may not be optimal. Always inspect the actual SQL for performance-critical paths.
- **Connection pooling**: Sometimes the bottleneck isn't the query but connection overhead. Use connection pooling (PgBouncer, ProxySQL) for high-concurrency applications.

## References

- For PostgreSQL-specific optimization, see `references/pg-optimization.md`
- For CTE vs temp table performance comparison, see `references/cte-vs-temp.md`
