# Dimensional Modeling for Data Warehouses

Dimensional modeling is the standard design technique for analytical databases (data warehouses). It optimizes for query performance and human understandability, not write efficiency. Use it when building the **Transform → Load → Serve** layers of an ELT pipeline.

---

## Core Concepts

### Fact Tables

A **fact table** stores measurable, numeric events — one row per event.

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | INT (PK) | Surrogate or natural key |
| `date_key` | INT (FK) | Reference to date dimension |
| `customer_key` | INT (FK) | Reference to customer dimension |
| `product_key` | INT (FK) | Reference to product dimension |
| `quantity` | INT | Additive measure |
| `revenue` | DECIMAL | Additive measure |
| `discount_amount` | DECIMAL | Additive measure |

**Three types of measures:**

| Type | Example | Can SUM across all dimensions? |
|------|---------|-------------------------------|
| **Additive** | revenue, quantity | Yes |
| **Semi-additive** | account balance, inventory | Across some dimensions (not time) |
| **Non-additive** | ratio, percentage, margin% | No — must recompute from base facts |

> **IRON LAW**: Never store non-additive measures as fact columns. Store the numerator and denominator separately, compute the ratio in the query layer. Storing `margin_pct` directly will give wrong answers when aggregated.

### Dimension Tables

A **dimension table** stores the descriptive attributes of a business entity.

```sql
-- Example: customer dimension
CREATE TABLE dim_customer (
  customer_key    INT PRIMARY KEY,       -- surrogate key
  customer_id     VARCHAR(50),           -- natural/source key
  full_name       VARCHAR(200),
  email           VARCHAR(200),
  city            VARCHAR(100),
  country         VARCHAR(100),
  signup_date     DATE,
  customer_tier   VARCHAR(50),           -- 'free', 'pro', 'enterprise'
  -- SCD fields (see below)
  valid_from      DATE NOT NULL,
  valid_to        DATE,                  -- NULL = current record
  is_current      BOOLEAN NOT NULL
);
```

Key rules:
- Always use a **surrogate key** (system-generated INT) as the dimension PK, not the source system's natural key
- Natural keys from source systems change, get reused, or leak across environments
- Dimension tables are wide — 20-100 columns is normal

---

## Star Schema vs Snowflake Schema

### Star Schema (Recommended Default)

```
                    dim_date
                       |
dim_customer ── fact_orders ── dim_product
                       |
                   dim_store
```

- Every dimension joins **directly** to the fact table
- No joins between dimension tables
- Optimized for query performance (fewer joins)
- Denormalized: duplicate strings in dimension tables (e.g., `country_name` repeated per customer)

### Snowflake Schema

```
dim_country ── dim_customer ── fact_orders ── dim_product ── dim_category
```

- Dimensions are normalized (sub-dimensions link to parent dimensions)
- Less storage, more joins
- Harder to query, harder to explain to analysts
- Use only when dimension tables are genuinely huge (>50M rows) and storage cost matters

**Decision rule:**

```
if (dimension_rows < 10M AND analyst queries the warehouse directly):
    use star schema
else if (storage is extremely constrained OR dimension is shared across many fact tables):
    consider snowflake
```

In practice: **always start with star schema.** Snowflaking is an optimization, not a default.

---

## Slowly Changing Dimensions (SCD)

When a customer changes city or tier, do you overwrite the old value? Your answer determines which SCD type to use.

### SCD Type 1 — Overwrite

No history preserved. Old value is gone.

```sql
UPDATE dim_customer
SET city = 'Taipei', customer_tier = 'pro'
WHERE customer_id = 'C-1042';
```

**Use when**: The old value is genuinely wrong (data correction), or history doesn't matter for analysis.

**Warning**: Historical fact rows now point to changed dimension values. A sale in 2023 will show the customer as "pro" even if they were "free" at the time.

### SCD Type 2 — Add New Row (Recommended for most cases)

History preserved by adding a new dimension row with new surrogate key.

```sql
-- Step 1: expire the old record
UPDATE dim_customer
SET valid_to = '2026-03-15', is_current = FALSE
WHERE customer_id = 'C-1042' AND is_current = TRUE;

-- Step 2: insert new record with new surrogate key
INSERT INTO dim_customer (
  customer_key, customer_id, full_name, city, customer_tier,
  valid_from, valid_to, is_current
) VALUES (
  9999, 'C-1042', 'Alice Chen', 'Taipei', 'pro',
  '2026-03-16', NULL, TRUE
);
```

Historical fact rows keep their old `customer_key` → old dimension row → correct historical attribute. New fact rows get the new `customer_key` → new dimension row.

**Use when**: You need "what was the customer's tier at the time of purchase?"

**Surrogate key assignment** for SCD Type 2: use a sequence/identity column in the warehouse, never derive from source key.

### SCD Type 3 — Add Column

Keeps one level of history via an additional column.

```sql
ALTER TABLE dim_customer ADD COLUMN prev_customer_tier VARCHAR(50);

UPDATE dim_customer
SET prev_customer_tier = customer_tier, customer_tier = 'pro'
WHERE customer_id = 'C-1042';
```

**Use when**: You only need "current" and "previous" value, nothing older.

**Rarely used** — most real-world requirements end up needing SCD Type 2.

### SCD Type Summary

| Type | History | Storage | Complexity | Use case |
|------|---------|---------|-----------|----------|
| Type 1 | None | Low | Low | Corrections, non-historical |
| Type 2 | Full | High | Medium | Most dimensions with changing attributes |
| Type 3 | One level | Medium | Medium | "Current vs previous" only |

---

## Date Dimension

Every warehouse needs a pre-populated date dimension. Do not use the raw `DATE` column from fact tables for date-based filtering — use a `dim_date` table.

```sql
CREATE TABLE dim_date (
  date_key        INT PRIMARY KEY,        -- YYYYMMDD integer, e.g. 20260409
  full_date       DATE NOT NULL,
  year            INT,
  quarter         INT,                    -- 1-4
  month           INT,                    -- 1-12
  month_name      VARCHAR(20),
  week_of_year    INT,
  day_of_week     INT,                    -- 1=Monday, 7=Sunday
  day_name        VARCHAR(20),
  is_weekend      BOOLEAN,
  is_holiday      BOOLEAN,
  fiscal_year     INT,                    -- if fiscal calendar differs
  fiscal_quarter  INT
);
```

**Generate 10 years of dates** (Python snippet):

```python
import csv
from datetime import date, timedelta

start = date(2020, 1, 1)
end = date(2030, 12, 31)
rows = []
d = start
while d <= end:
    rows.append({
        "date_key": int(d.strftime("%Y%m%d")),
        "full_date": d.isoformat(),
        "year": d.year,
        "quarter": (d.month - 1) // 3 + 1,
        "month": d.month,
        "month_name": d.strftime("%B"),
        "week_of_year": d.isocalendar()[1],
        "day_of_week": d.isoweekday(),   # 1=Mon
        "day_name": d.strftime("%A"),
        "is_weekend": d.isoweekday() >= 6,
    })
    d += timedelta(days=1)

with open("dim_date.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
```

**Why integer date key?** `20260409` is smaller than a DATE or VARCHAR, partitions cleanly, and is human-readable in query results without casting.

---

## Fact Table Grain

**Grain** = the level of detail of one row in the fact table. Defining grain precisely is the most important design decision.

### Step-by-step grain definition

1. Name the business process (e.g., "online order placement")
2. Ask: "What is the most atomic event we need to track?"
3. Write it as one sentence: *"One row per order line item"*

| Grain | Example row | What you can measure |
|-------|------------|---------------------|
| One row per order | order #1001 | Order-level revenue, order count |
| One row per order line | order #1001, product SKU-A | Line-level revenue, units per product |
| One row per daily product summary | 2026-04-09, SKU-A | Daily aggregates only (no per-order queries) |

**Finer grain = more flexibility but larger table.** Start at the most atomic grain your source provides; you can always aggregate up, you cannot disaggregate down.

### Common grain mistakes

- **Mixed grains in one fact table**: some rows are at order level, some at line level. This causes double-counting. One fact table = one grain.
- **Pre-aggregated grain**: loading daily summaries when you need hourly analysis. Design around the lowest grain you'll ever need.

---

## Worked Example: E-commerce Warehouse

### Business process: online orders

**Grain**: one row per order line item

```sql
-- Fact table
CREATE TABLE fact_order_lines (
  order_line_key   BIGINT PRIMARY KEY,
  order_id         VARCHAR(50),
  date_key         INT REFERENCES dim_date(date_key),
  customer_key     INT REFERENCES dim_customer(customer_key),
  product_key      INT REFERENCES dim_product(product_key),
  channel_key      INT REFERENCES dim_channel(channel_key),

  -- Additive measures
  quantity         INT NOT NULL,
  unit_price       DECIMAL(12,4) NOT NULL,
  discount_amount  DECIMAL(12,4) NOT NULL DEFAULT 0,
  revenue          DECIMAL(12,4) NOT NULL,    -- quantity * unit_price - discount
  cost             DECIMAL(12,4),

  -- Audit
  loaded_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Margin query** — note: computed at query time, not stored:

```sql
SELECT
  p.category,
  SUM(f.revenue)                                AS total_revenue,
  SUM(f.cost)                                   AS total_cost,
  SUM(f.revenue - f.cost) / SUM(f.revenue)      AS margin_pct   -- recomputed
FROM fact_order_lines f
JOIN dim_product p USING (product_key)
JOIN dim_date d USING (date_key)
WHERE d.year = 2026 AND d.quarter = 1
GROUP BY p.category;
```

### Product dimension (Type 2)

```sql
CREATE TABLE dim_product (
  product_key      INT PRIMARY KEY,
  product_id       VARCHAR(50),          -- source system ID
  product_name     VARCHAR(200),
  sku              VARCHAR(100),
  category         VARCHAR(100),
  subcategory      VARCHAR(100),
  brand            VARCHAR(100),
  unit_cost        DECIMAL(12,4),
  list_price       DECIMAL(12,4),
  is_active        BOOLEAN,
  -- SCD Type 2
  valid_from       DATE NOT NULL,
  valid_to         DATE,
  is_current       BOOLEAN NOT NULL
);
```

---

## dbt Implementation Pattern

In a dbt project, dimensional models follow a layered naming convention:

```
models/
├── staging/        # stg_*  — raw source cleaned, 1:1 with source tables
├── intermediate/   # int_*  — joins and business logic (optional)
└── marts/
    ├── dim_*.sql   # dimension tables
    └── fct_*.sql   # fact tables
```

### Surrogate key generation in dbt

```sql
-- models/marts/dim_customer.sql
WITH source AS (
    SELECT * FROM {{ ref('stg_customers') }}
),
renamed AS (
    SELECT
        {{ dbt_utils.generate_surrogate_key(['customer_id', 'valid_from']) }}
            AS customer_key,
        customer_id,
        full_name,
        email,
        city,
        customer_tier,
        valid_from,
        valid_to,
        is_current
    FROM source
)
SELECT * FROM renamed
```

### Incremental fact table in dbt

```sql
-- models/marts/fct_order_lines.sql
{{ config(materialized='incremental', unique_key='order_line_key') }}

WITH source AS (
    SELECT * FROM {{ ref('stg_order_lines') }}
    {% if is_incremental() %}
    WHERE loaded_at > (SELECT MAX(loaded_at) FROM {{ this }})
    {% endif %}
)
SELECT
    order_line_key,
    order_id,
    {{ dbt_utils.get_surrogate_key(['customer_id']) }}   AS customer_key,
    {{ dbt_utils.get_surrogate_key(['product_id']) }}    AS product_key,
    CAST(TO_CHAR(order_date, 'YYYYMMDD') AS INT)         AS date_key,
    quantity,
    unit_price,
    discount_amount,
    quantity * unit_price - discount_amount              AS revenue
FROM source
```

---

## Quality Checks Specific to Dimensional Models

Reinforcing the IRON LAW — checks must exist at every stage:

| Check | SQL Pattern | When |
|-------|------------|------|
| Orphan fact rows | `SELECT COUNT(*) FROM fct WHERE dim_key NOT IN (SELECT key FROM dim)` | After load |
| SCD Type 2 overlap | `SELECT customer_id, COUNT(*) FROM dim WHERE is_current=TRUE GROUP BY 1 HAVING COUNT(*)>1` | After dim load |
| Fact grain uniqueness | `SELECT order_line_key, COUNT(*) FROM fct GROUP BY 1 HAVING COUNT(*)>1` | After load |
| Date key coverage | `SELECT COUNT(*) FROM fct WHERE date_key NOT IN (SELECT date_key FROM dim_date)` | After load |
| Revenue non-negative | `SELECT COUNT(*) FROM fct WHERE revenue < 0` | After transform |

In dbt, use `dbt test` with `not_null`, `unique`, `relationships`, and `accepted_values` tests declared in `schema.yml`.

---

## Common Mistakes

**1. Storing derived metrics as fact columns**
Storing `margin_pct = revenue / cost` directly. When you SUM across rows, `SUM(margin_pct)` is meaningless. Store `revenue` and `cost`, compute ratio in queries.

**2. Using natural keys as dimension PKs**
Source IDs get reused, change format, or collide across environments. Always generate surrogate keys in the warehouse layer.

**3. Ignoring SCD until production**
Retrofitting SCD Type 2 onto an existing warehouse requires rebuilding history. Decide at design time whether history matters. If unsure, use Type 2 — it's easier to downgrade to Type 1 than to upgrade.

**4. One giant fact table**
Mixing multiple business processes (orders + returns + inventory) at different grains into one fact table. Separate fact tables, one per grain.

**5. Late-arriving facts**
An order placed on Apr 8 but loaded on Apr 9 gets `date_key = 20260409`. Use `order_date` as the date key, not `loaded_at`. Separate the business event date from the pipeline processing date.

**6. Missing date dimension records**
If your date dimension only goes to 2025-12-31 and a fact row has `date_key = 20260101`, the JOIN returns NULL and the row disappears from reports silently. Pre-populate the date dimension 5+ years ahead.
