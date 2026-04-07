---
name: "tech-data-pipeline"
description: "Design data pipelines covering ETL vs ELT architectures, data source integration, scheduling, quality checks, and warehouse design. Use this skill when the user needs to move data between systems, build a data warehouse, automate data processing, or improve data reliability — even if they say 'move data from X to Y', 'build an ETL pipeline', 'our data is a mess', or 'set up a data warehouse'."
metadata:
  category: "WP-11 通用技術"
  tags: ["technology", "data-pipeline", "etl", "data-engineering"]
---

# Data Pipeline Design

## Framework

```
IRON LAW: Data Quality Checks at Every Stage

A pipeline that moves bad data fast is worse than no pipeline — it
corrupts downstream analytics and decisions. Every pipeline stage
(extract, transform, load) must have data quality checks:
row counts, null checks, schema validation, freshness checks.

"Garbage in, garbage out" is not a warning — it's a guarantee.
```

### ETL vs ELT

| Aspect | ETL (Extract, Transform, Load) | ELT (Extract, Load, Transform) |
|--------|-------------------------------|-------------------------------|
| Transform where? | Before loading (in pipeline) | After loading (in warehouse) |
| Best for | Structured data, compliance-heavy | Cloud warehouses (BigQuery, Snowflake) |
| Flexibility | Less (transform logic is fixed) | More (transform in SQL after loading) |
| Cost | Compute in pipeline | Compute in warehouse |
| Trend | Legacy/on-prem | Modern/cloud-native |

### Pipeline Architecture

```
[Sources] → [Extract] → [Stage] → [Transform] → [Load] → [Serve]
   ↑                                                          ↓
   |              [Quality Checks at every stage]        [Dashboard]
   |              [Monitoring & Alerting]                [API]
   └──────────────── [Orchestrator (Airflow/Prefect)] ──────┘
```

### Data Source Types

| Source | Extraction Method | Challenges |
|--------|-----------------|-----------|
| **Database** | CDC (Change Data Capture), bulk query, replication | Schema changes, performance impact on source |
| **API** | REST/GraphQL polling, webhooks | Rate limits, pagination, auth token refresh |
| **Files** | S3/GCS pickup, SFTP, email attachment | Format inconsistency, encoding issues |
| **Streaming** | Kafka, Kinesis, Pub/Sub | Ordering, exactly-once processing |
| **SaaS tools** | Pre-built connectors (Fivetran, Airbyte) | API changes, data model complexity |

### Orchestration Tools

| Tool | Type | Best For | Complexity |
|------|------|----------|-----------|
| **Airflow** | Python DAGs | Complex pipelines, team of engineers | High |
| **Prefect** | Python, modern API | Simpler than Airflow, good DX | Medium |
| **dbt** | SQL transforms only | Transform layer in ELT | Low-Medium |
| **Cron** | Simple scheduling | Single script, low complexity | Low |
| **Fivetran/Airbyte** | Managed connectors | Extract + Load (no transform) | Low |

### Data Quality Framework

| Check | What It Validates | When |
|-------|-----------------|------|
| **Row count** | Expected number of rows (within ±10% of prior run) | After extract, after load |
| **Null check** | Critical columns have no unexpected nulls | After extract |
| **Schema validation** | Column names, types match expected | After extract |
| **Freshness** | Data is recent (not stale) | After load |
| **Uniqueness** | No duplicate primary keys | After load |
| **Range check** | Values within expected bounds | After transform |
| **Referential integrity** | Foreign keys match parent tables | After load |

### Pipeline Design Steps

1. **Map sources and destinations**: What data, from where, to where?
2. **Define freshness requirements**: Real-time? Hourly? Daily?
3. **Choose architecture**: ETL or ELT based on tools and team
4. **Build incrementally**: Start with one source, one destination, one schedule
5. **Add quality checks**: At minimum: row count + null check + freshness
6. **Set up monitoring**: Alert on failure, quality check violations, latency
7. **Document**: Data dictionary, pipeline diagram, SLAs

## Output Format

```markdown
# Data Pipeline Design: {Project}

## Sources & Destinations
| Source | Type | Destination | Freshness | Volume |
|--------|------|-----------|-----------|--------|
| {source} | DB/API/File | {dest} | {daily/hourly} | {rows/day} |

## Architecture
- Pattern: ETL / ELT
- Orchestrator: {tool}
- Transform: {tool/SQL}
- Quality: {tool/custom checks}

## Pipeline Diagram
{Source} → {Extract} → {Stage} → {Transform} → {Load} → {Serve}

## Quality Checks
| Stage | Check | Threshold | Alert |
|-------|-------|-----------|-------|
| Extract | Row count | ±10% of prior | Slack alert |
| Load | Freshness | < 6 hours old | PagerDuty |

## Schedule
| Pipeline | Frequency | Start Time | SLA |
|----------|-----------|-----------|-----|
| {name} | {daily/hourly} | {time} | Data ready by {time} |
```

## Gotchas

- **Idempotency is essential**: A pipeline that runs twice should produce the same result as running once. Use upsert (not insert) and date-partitioned loads.
- **Schema drift**: Source systems change schemas without warning. Build schema detection and alerting.
- **Backfill capability**: When a pipeline fails for 3 days, can you rerun for those days without duplicating data? Design for this from day 1.
- **Don't build what you can buy**: Fivetran/Airbyte handle 200+ source connectors. Writing a custom Salesforce extractor is rarely worth the engineering time.
- **Data warehouse vs data lake**: Warehouse (BigQuery, Snowflake) = structured, SQL-queryable. Lake (S3, GCS) = raw, any format. Most modern stacks use both (lakehouse pattern).

## References

- For dbt project structure, see `references/dbt-guide.md`
- For data warehouse modeling (star schema), see `references/dimensional-modeling.md`
