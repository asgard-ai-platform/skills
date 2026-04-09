# dbt Project Structure & ELT Transform Layer

dbt (data build tool) handles the **T** in ELT: SQL-based transformations that run inside the warehouse after raw data is already loaded. This guide covers project layout, model layering, quality checks, and incremental patterns that align with the parent skill's Iron Law.

---

## Project Layout

```
my_project/
├── dbt_project.yml          ← project config, model materializations
├── profiles.yml             ← connection credentials (NOT in version control)
├── models/
│   ├── staging/             ← 1:1 with source tables; minimal transforms
│   │   ├── _sources.yml     ← source declarations + freshness checks
│   │   ├── _staging.yml     ← column docs + dbt tests
│   │   ├── stg_orders.sql
│   │   └── stg_customers.sql
│   ├── intermediate/        ← joins, business logic; not exposed to BI
│   │   └── int_orders_with_customers.sql
│   └── marts/               ← final, BI-ready tables by domain
│       ├── finance/
│       │   └── fct_revenue_daily.sql
│       └── marketing/
│           └── dim_customers.sql
├── tests/                   ← custom singular tests (SQL files)
│   └── assert_revenue_non_negative.sql
├── macros/                  ← reusable Jinja macros
│   └── generate_schema_name.sql
└── seeds/                   ← small static CSVs (lookup tables)
    └── country_codes.csv
```

### Layer Contracts

| Layer | Purpose | Materialization | Allowed to reference |
|-------|---------|----------------|----------------------|
| `staging` | Clean raw → typed columns, rename snake_case | `view` | `sources` only |
| `intermediate` | Business joins, derived metrics | `view` or ephemeral | `staging` only |
| `marts` | Final domain tables for BI/APIs | `table` or `incremental` | `staging`, `intermediate` |

**Rule**: downstream layers must only reference upstream layers. A mart must never reference another mart. A staging model must never reference another staging model.

---

## Source Declarations and Freshness Checks

`models/staging/_sources.yml` declares raw tables loaded by Fivetran/Airbyte:

```yaml
version: 2

sources:
  - name: raw_ecommerce
    database: my_warehouse
    schema: raw
    freshness:
      warn_after: {count: 6, period: hour}
      error_after: {count: 24, period: hour}
    loaded_at_field: _fivetran_synced   # timestamp column to check freshness

    tables:
      - name: orders
        description: "Raw orders from Shopify via Fivetran"
        columns:
          - name: id
            tests:
              - unique
              - not_null
          - name: created_at
            tests:
              - not_null
          - name: total_price
            tests:
              - not_null

      - name: customers
        columns:
          - name: id
            tests:
              - unique
              - not_null
```

Run freshness check separately (in CI or before dbt run):

```bash
dbt source freshness
```

This directly implements the **Freshness** quality check from the parent skill's quality framework.

---

## Staging Model Pattern

Every staging model follows the same template. Rename, cast, and nothing else.

```sql
-- models/staging/stg_orders.sql
with source as (
    select * from {{ source('raw_ecommerce', 'orders') }}
),

renamed as (
    select
        id                                          as order_id,
        customer_id,
        cast(created_at as timestamp)               as created_at,
        cast(total_price as numeric)                as total_price_usd,
        lower(trim(status))                         as status,
        _fivetran_synced                            as _loaded_at
    from source
    where _fivetran_deleted is false   -- soft-delete filter
)

select * from renamed
```

**What belongs in staging**:
- Column renames (camelCase → snake_case)
- Type casts
- Deduplication of the raw layer
- Filtering deleted records

**What does NOT belong in staging**:
- Joins to other tables
- Business metric calculations
- Aggregations

---

## Incremental Models (Backfill-Safe)

From the parent skill's Gotchas: *"When a pipeline fails for 3 days, can you rerun for those days without duplicating data?"* Incremental models solve this.

```sql
-- models/marts/finance/fct_revenue_daily.sql
{{
    config(
        materialized='incremental',
        unique_key='date_day || \'-\' || source_currency',
        on_schema_change='sync_all_columns'
    )
}}

with orders as (
    select * from {{ ref('stg_orders') }}
    where status = 'completed'

    {% if is_incremental() %}
        -- Only process new rows since last run
        -- Leave a 3-hour buffer for late-arriving data
        and created_at >= (
            select dateadd(hour, -3, max(date_day))
            from {{ this }}
        )
    {% endif %}
),

daily as (
    select
        date_trunc('day', created_at)   as date_day,
        'USD'                           as source_currency,
        count(*)                        as order_count,
        sum(total_price_usd)            as revenue_usd
    from orders
    group by 1, 2
)

select * from daily
```

### Incremental Strategy Decision Table

| Scenario | Strategy | Config |
|----------|----------|--------|
| Append-only events (logs, clicks) | `append` | `materialized='incremental'`, no `unique_key` |
| Mutable records (orders that update) | `merge` | `unique_key='order_id'` |
| Large tables, date-partitioned | `insert_overwrite` | `partition_by` (BigQuery only) |
| Small tables (< 1M rows) | `table` | Skip incremental entirely |

**The 3-hour buffer** in the example above handles late-arriving data: rows that were created yesterday but only appeared in the source system today. Always tune this buffer based on source system SLA, not instinct.

---

## Schema Tests (Built-in Quality Checks)

`models/staging/_staging.yml` wires dbt's built-in tests to the quality framework:

```yaml
version: 2

models:
  - name: stg_orders
    columns:
      - name: order_id
        tests:
          - unique          # Uniqueness check
          - not_null        # Null check
      - name: status
        tests:
          - accepted_values: # Range / domain check
              values: ['pending', 'completed', 'cancelled', 'refunded']
      - name: total_price_usd
        tests:
          - not_null
          - dbt_utils.expression_is_true:  # Custom range check
              expression: ">= 0"

  - name: fct_revenue_daily
    columns:
      - name: date_day
        tests:
          - unique
          - not_null
      - name: revenue_usd
        tests:
          - dbt_utils.expression_is_true:
              expression: ">= 0"
```

### Mapping to Parent Skill Quality Checks

| Parent Skill Check | dbt Implementation |
|-------------------|--------------------|
| Row count | `dbt_utils.recency` or custom singular test |
| Null check | `not_null` schema test |
| Schema validation | `on_schema_change='fail'` in incremental config |
| Freshness | `dbt source freshness` + `loaded_at_field` |
| Uniqueness | `unique` schema test |
| Range check | `accepted_values` or `expression_is_true` |
| Referential integrity | `relationships` schema test (see below) |

Referential integrity example:

```yaml
- name: order_id
  tests:
    - relationships:
        to: ref('stg_orders')
        field: order_id
```

---

## Custom Singular Test (Row Count Check)

Built-in tests cover column-level checks. Row count requires a singular test:

```sql
-- tests/assert_orders_row_count_not_dropped.sql
-- Fails if today's order count is less than 50% of yesterday's count
-- Catches pipeline failures, source outages, accidental filters

with today as (
    select count(*) as cnt
    from {{ ref('stg_orders') }}
    where date_trunc('day', created_at) = current_date
),

yesterday as (
    select count(*) as cnt
    from {{ ref('stg_orders') }}
    where date_trunc('day', created_at) = current_date - 1
)

select
    today.cnt as today_count,
    yesterday.cnt as yesterday_count,
    today.cnt * 1.0 / nullif(yesterday.cnt, 0) as ratio
from today, yesterday
where today.cnt < yesterday.cnt * 0.5   -- Alert if < 50% of yesterday
```

A singular test **passes when it returns 0 rows**. If this query returns rows, dbt marks the test as failed.

---

## `dbt_project.yml` Materialization Defaults

```yaml
name: my_project
version: '1.0.0'
config-version: 2

profile: my_warehouse

model-paths: ["models"]
test-paths: ["tests"]
seed-paths: ["seeds"]
macro-paths: ["macros"]

models:
  my_project:
    staging:
      +materialized: view
      +schema: staging
    intermediate:
      +materialized: view
      +schema: intermediate
    marts:
      +materialized: table
      +schema: marts
      finance:
        fct_revenue_daily:
          +materialized: incremental
```

Setting defaults at the folder level means individual models don't need `{{ config(...) }}` blocks unless overriding. This prevents the common mistake of forgetting to set materialization on a mart and accidentally running it as a view.

---

## Running dbt in a Pipeline

dbt slots into the orchestrator (Airflow/Prefect) after the load step:

```
[Fivetran sync complete] → [dbt source freshness] → [dbt run] → [dbt test] → [notify]
```

### Recommended dbt run commands

```bash
# Full refresh (use sparingly — expensive on large tables)
dbt run --full-refresh

# Production: run all models then test all
dbt run && dbt test

# Run only downstream of a changed model (CI optimization)
dbt run --select stg_orders+   # stg_orders and everything downstream

# Run only failed tests
dbt test --select result:fail --store-failures

# Source freshness check (run before dbt run)
dbt source freshness --select source:raw_ecommerce
```

### CI/CD Checks (minimum viable)

```bash
# On every PR:
dbt compile                   # catches Jinja/SQL syntax errors
dbt run --select state:modified+  # only changed models + downstream
dbt test --select state:modified+ # test those models
```

`state:modified+` requires a production manifest artifact (`manifest.json`) to diff against. Store it in S3/GCS after each production run.

---

## Schema Drift Defense

From the parent skill Gotchas: *"Source systems change schemas without warning."*

In `dbt_project.yml`, set the default for incremental models:

```yaml
models:
  my_project:
    marts:
      +on_schema_change: "sync_all_columns"
```

Options:

| `on_schema_change` | Behavior | Use when |
|-------------------|----------|----------|
| `ignore` | Silently skip new columns | Never (hides drift) |
| `fail` | Hard error on schema change | Strict compliance environments |
| `append_new_columns` | Add new columns, keep old | Most production setups |
| `sync_all_columns` | Add new, remove dropped columns | Recommended default |

Additionally, add a staging test that alerts on unexpected columns:

```yaml
# models/staging/_staging.yml
- name: stg_orders
  config:
    on_schema_change: fail   # override project default for critical models
```

---

## Common Mistakes

**Materializing staging as a table**: Staging models should be views. Materializing them as tables wastes warehouse compute and storage — they're just renamed raw tables.

**Putting business logic in staging**: Staging is a cleaning step, not a calculation step. Metric definitions belong in intermediate or marts, where they can be reused and tested independently.

**Using `{{ this }}` in a non-incremental model**: `{{ this }}` references the model's own table and only works when `materialized='incremental'`. Using it in a table model causes a cryptic error.

**Forgetting `--full-refresh` after changing incremental logic**: If you change the WHERE clause or aggregation in an incremental model, old rows retain the old logic. Run `dbt run --full-refresh --select model_name` to rebuild from scratch.

**Running `dbt test` without `dbt run` first**: On first setup or after schema changes, models may not exist. Always run `dbt run` before `dbt test` in CI.

**Not storing `manifest.json`**: Without a production manifest artifact, `state:modified+` in CI cannot work. After every successful production run, upload `target/manifest.json` to object storage.
