# RFM Implementation: Python & SQL

This document covers concrete implementation in Python (pandas) and SQL. All examples use the same synthetic dataset so you can cross-check outputs.

---

## Synthetic Dataset (Reference)

All worked examples below use this 10-customer slice. In practice you will have thousands of rows.

| customer_id | order_id | order_date | order_amount |
|-------------|----------|------------|--------------|
| C001 | O101 | 2025-11-15 | 320.00 |
| C001 | O102 | 2026-01-03 | 150.00 |
| C001 | O103 | 2026-03-20 | 210.00 |
| C002 | O201 | 2025-09-01 | 890.00 |
| C002 | O202 | 2025-09-28 | 430.00 |
| C003 | O301 | 2026-03-30 | 55.00 |
| C004 | O401 | 2025-03-10 | 1200.00 |
| C004 | O402 | 2025-04-22 | 980.00 |
| C005 | O501 | 2026-04-01 | 75.00 |
| C005 | O502 | 2026-04-05 | 90.00 |
| C006 | O601 | 2024-12-01 | 300.00 |
| C007 | O701 | 2026-03-01 | 500.00 |
| C007 | O702 | 2026-03-15 | 500.00 |
| C007 | O703 | 2026-04-01 | 500.00 |
| C008 | O801 | 2026-02-14 | 88.00 |
| C009 | O901 | 2025-06-01 | 2100.00 |
| C010 | O1001 | 2026-01-10 | 420.00 |
| C010 | O1002 | 2026-02-20 | 380.00 |

**Analysis reference date**: `2026-04-09` (today)
**Analysis window**: 2025-04-09 → 2026-04-09 (12 months)

---

## Step 1: Aggregate Raw Metrics

Before scoring, compute R/F/M values per customer.

### Python

```python
import pandas as pd
from datetime import date

ANALYSIS_DATE = date(2026, 4, 9)
WINDOW_START = date(2025, 4, 9)

# Load transactions — adjust to your actual source
df = pd.read_csv("transactions.csv", parse_dates=["order_date"])

# Filter to analysis window
df = df[df["order_date"].dt.date >= WINDOW_START]

# Aggregate
rfm_raw = (
    df.groupby("customer_id")
    .agg(
        last_order_date=("order_date", "max"),
        frequency=("order_id", "nunique"),   # distinct orders, not rows
        monetary=("order_amount", "sum"),
    )
    .reset_index()
)

rfm_raw["recency"] = (
    pd.Timestamp(ANALYSIS_DATE) - rfm_raw["last_order_date"]
).dt.days

rfm_raw = rfm_raw[["customer_id", "recency", "frequency", "monetary"]]
```

### SQL

```sql
-- PostgreSQL / BigQuery syntax
-- Adjust DATE '2026-04-09' to your dialect (e.g., CURRENT_DATE)

WITH base AS (
    SELECT
        customer_id,
        MAX(order_date)                               AS last_order_date,
        COUNT(DISTINCT order_id)                      AS frequency,
        SUM(order_amount)                             AS monetary
    FROM orders
    WHERE order_date >= DATE '2025-04-09'
      AND order_date <  DATE '2026-04-10'   -- exclusive upper bound
    GROUP BY customer_id
)
SELECT
    customer_id,
    DATE '2026-04-09' - last_order_date     AS recency,   -- days as integer
    frequency,
    monetary
FROM base;
```

**Worked output** (customers active in the window):

| customer_id | recency | frequency | monetary |
|-------------|---------|-----------|----------|
| C001 | 20 | 3 | 680.00 |
| C002 | 193 | 2 | 1320.00 |
| C003 | 10 | 1 | 55.00 |
| C005 | 4 | 2 | 165.00 |
| C007 | 8 | 3 | 1500.00 |
| C008 | 54 | 1 | 88.00 |
| C009 | 312 | 1 | 2100.00 |
| C010 | 48 | 2 | 800.00 |

> C004 (last order 2025-04-22) is inside the window; C006 (2024-12-01) is outside.

---

## Step 2: Quintile Scoring

### Formula

For dimensions where **higher = better** (F, M):

```
score = quintile rank (1 = lowest 20%, 5 = top 20%)
```

For **Recency**, lower days = more recent = better, so the rank is inverted:

```
R_score = 6 - quintile_rank(recency)
```

### Python

```python
def quintile_score(series: pd.Series, ascending: bool = True) -> pd.Series:
    """
    ascending=True  → higher values get higher scores (used for F, M)
    ascending=False → lower values get higher scores (used for R)
    """
    labels = [1, 2, 3, 4, 5] if ascending else [5, 4, 3, 2, 1]
    return pd.qcut(series, q=5, labels=labels, duplicates="drop").astype(int)

rfm_raw["R"] = quintile_score(rfm_raw["recency"], ascending=False)
rfm_raw["F"] = quintile_score(rfm_raw["frequency"], ascending=True)
rfm_raw["M"] = quintile_score(rfm_raw["monetary"], ascending=True)

rfm_raw["rfm_score"] = (
    rfm_raw["R"].astype(str)
    + rfm_raw["F"].astype(str)
    + rfm_raw["M"].astype(str)
)
```

### SQL (NTILE)

```sql
WITH metrics AS (
    -- ... (output of Step 1 query)
),
scored AS (
    SELECT
        customer_id,
        recency,
        frequency,
        monetary,
        -- Recency: low days = high score, so rank ascending then invert
        6 - NTILE(5) OVER (ORDER BY recency ASC)      AS r_score,
        NTILE(5)     OVER (ORDER BY frequency ASC)     AS f_score,
        NTILE(5)     OVER (ORDER BY monetary ASC)      AS m_score
    FROM metrics
)
SELECT
    customer_id,
    recency, frequency, monetary,
    r_score, f_score, m_score,
    CONCAT(r_score::text, f_score::text, m_score::text) AS rfm_score
FROM scored;
```

**Note on `duplicates="drop"` in pandas**: When many customers share the same value (e.g., frequency=1 for 60% of customers), `pd.qcut` raises an error if bin edges are non-unique. `duplicates="drop"` merges duplicate edges, meaning some "quintiles" may cover more than 20% of customers. This is acceptable; the alternative is custom breakpoints (see §4 below).

**Worked scores** for the 8-customer example:

| customer_id | recency | frequency | monetary | R | F | M | rfm_score |
|-------------|---------|-----------|----------|---|---|---|-----------|
| C005 | 4 | 2 | 165.00 | 5 | 3 | 2 | 532 |
| C007 | 8 | 3 | 1500.00 | 5 | 5 | 5 | 555 |
| C003 | 10 | 1 | 55.00 | 4 | 1 | 1 | 411 |
| C001 | 20 | 3 | 680.00 | 4 | 5 | 3 | 453 |
| C010 | 48 | 2 | 800.00 | 3 | 3 | 4 | 334 |
| C008 | 54 | 1 | 88.00 | 3 | 1 | 1 | 311 |
| C002 | 193 | 2 | 1320.00 | 2 | 3 | 4 | 234 |
| C009 | 312 | 1 | 2100.00 | 1 | 1 | 5 | 115 |

---

## Step 3: Segment Assignment

Map RFM scores to named segments using rule-based logic. Rules are evaluated **in order**; the first match wins.

### Segment Rules

```python
def assign_segment(r: int, f: int, m: int) -> str:
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    if r >= 4 and f >= 4:
        return "Loyal"
    if r >= 4 and f >= 2:
        return "Potential Loyalists"
    if r == 5 and f == 1:
        return "New Customers"
    if r >= 2 and f >= 3 and m >= 3:
        return "At Risk"
    if r <= 2 and f <= 2 and m <= 2:
        return "Hibernating"
    return "Others"

rfm_raw["segment"] = rfm_raw.apply(
    lambda row: assign_segment(row["R"], row["F"], row["M"]), axis=1
)
```

### SQL Equivalent

```sql
SELECT
    *,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN 'Champions'
        WHEN r_score >= 4 AND f_score >= 4                  THEN 'Loyal'
        WHEN r_score >= 4 AND f_score >= 2                  THEN 'Potential Loyalists'
        WHEN r_score =  5 AND f_score =  1                  THEN 'New Customers'
        WHEN r_score >= 2 AND f_score >= 3 AND m_score >= 3 THEN 'At Risk'
        WHEN r_score <= 2 AND f_score <= 2 AND m_score <= 2 THEN 'Hibernating'
        ELSE 'Others'
    END AS segment
FROM scored;
```

**Worked segment assignments**:

| customer_id | rfm_score | segment |
|-------------|-----------|---------|
| C007 | 555 | Champions |
| C001 | 453 | Loyal |
| C005 | 532 | Potential Loyalists |
| C003 | 411 | Potential Loyalists |
| C010 | 334 | Others |
| C008 | 311 | Others |
| C002 | 234 | At Risk |
| C009 | 115 | Hibernating |

---

## Step 4: Custom Breakpoints (When Quintiles Fail)

Quintiles assume a roughly uniform distribution. Two common failure modes:

**Failure mode A — Frequency spike at 1**: If 70% of customers bought exactly once, quintile ranks 1–4 all correspond to F=1. Everyone looks equal.

**Failure mode B — Monetary long tail**: If 5% of customers account for 80% of revenue, quintile cuts don't separate the elite tier.

### Fix: Business-Defined Breakpoints

Replace `pd.qcut` with `pd.cut` and set explicit bin edges:

```python
# Example: e-commerce site where most customers buy 1-3x per year
FREQ_BINS  = [0, 1, 2, 4, 8, float("inf")]   # edges
FREQ_LABELS = [1, 2, 3, 4, 5]

MON_BINS   = [0, 50, 200, 500, 1000, float("inf")]
MON_LABELS = [1, 2, 3, 4, 5]

# Recency in days — invert: recent=5, old=1
REC_BINS   = [0, 30, 90, 180, 365, float("inf")]
REC_LABELS = [5, 4, 3, 2, 1]   # note reversed

rfm_raw["R"] = pd.cut(rfm_raw["recency"],   bins=REC_BINS, labels=REC_LABELS).astype(int)
rfm_raw["F"] = pd.cut(rfm_raw["frequency"], bins=FREQ_BINS, labels=FREQ_LABELS).astype(int)
rfm_raw["M"] = pd.cut(rfm_raw["monetary"],  bins=MON_BINS,  labels=MON_LABELS).astype(int)
```

**How to choose bin edges**: Pull the percentile distribution first, then set edges at natural business thresholds:

```python
print(rfm_raw["monetary"].describe(percentiles=[.2, .4, .6, .8, .9, .95]))
```

Set edges where you see a meaningful behavioral gap (e.g., $200 separating one-time small buyers from repeat mid-spenders), not just at equal-count splits.

---

## Step 5: Segment Summary Report

```python
summary = (
    rfm_raw.groupby("segment")
    .agg(
        count=("customer_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        avg_monetary=("monetary", "mean"),
        total_revenue=("monetary", "sum"),
    )
    .round(1)
    .reset_index()
)

total_rev = summary["total_revenue"].sum()
summary["revenue_pct"] = (summary["total_revenue"] / total_rev * 100).round(1)
summary = summary.sort_values("total_revenue", ascending=False)
print(summary.to_markdown(index=False))
```

SQL equivalent:

```sql
SELECT
    segment,
    COUNT(*)                             AS customer_count,
    ROUND(AVG(recency), 1)               AS avg_recency_days,
    ROUND(AVG(frequency), 1)             AS avg_frequency,
    ROUND(AVG(monetary), 2)              AS avg_monetary,
    ROUND(SUM(monetary), 2)              AS total_revenue,
    ROUND(
        100.0 * SUM(monetary) / SUM(SUM(monetary)) OVER (), 1
    )                                    AS revenue_pct
FROM rfm_final          -- the view/CTE with segment assigned
GROUP BY segment
ORDER BY total_revenue DESC;
```

---

## Data Cleaning Checklist

These must happen **before** aggregation in Step 1.

| Issue | How to handle |
|-------|---------------|
| Refunded orders | Remove rows where `status IN ('refunded', 'cancelled')`, or subtract refund amount from `order_amount` |
| Partial refunds | Use `net_amount = order_amount - refund_amount`; exclude row if `net_amount <= 0` |
| Test / internal orders | Filter `customer_email NOT LIKE '%@yourcompany.com%'` and `is_test = false` |
| Duplicate order IDs | Deduplicate on `order_id` before aggregating (use `DISTINCT order_id` in `COUNT`) |
| Multi-currency | Convert all amounts to a single currency before summing |
| B2B accounts / resellers | Separate B2B into its own RFM run; their F/M baselines differ from B2C |

---

## Subscription Business: Drop M, Use RF

If your product is a fixed-price subscription (e.g., SaaS, box subscription), every paying customer has nearly identical M within a tier. M adds no discriminating signal. Run a 2-dimension RF model instead:

```python
# No monetary column. Score R and F only.
rfm_raw["R"] = quintile_score(rfm_raw["recency"], ascending=False)
rfm_raw["F"] = quintile_score(rfm_raw["frequency"], ascending=True)
rfm_raw["rf_score"] = rfm_raw["R"].astype(str) + rfm_raw["F"].astype(str)
```

Segment definitions simplify to:

| Segment | R | F |
|---------|---|---|
| Champions | 4-5 | 4-5 |
| Loyal | 4-5 | 3 |
| At Risk | 1-3 | 4-5 |
| Dormant | 1-2 | 1-2 |
| New | 5 | 1 |

For subscriptions, M can be replaced by **plan tier** (Free / Pro / Enterprise) as a fourth dimension if meaningful differentiation exists.

---

## Complete Python Reference Implementation

```python
"""
rfm_score.py  — minimal, dependency-free RFM scorer
Input : CSV with columns: customer_id, order_id, order_date, order_amount
Output: CSV with columns: customer_id, recency, frequency, monetary, R, F, M, rfm_score, segment
"""

import argparse
import sys
from datetime import date, timedelta

import pandas as pd


ANALYSIS_DATE = date.today()
WINDOW_MONTHS = 12

SEGMENT_RULES = [
    ("Champions",          lambda r, f, m: r >= 4 and f >= 4 and m >= 4),
    ("Loyal",              lambda r, f, m: r >= 4 and f >= 4),
    ("Potential Loyalists",lambda r, f, m: r >= 4 and f >= 2),
    ("New Customers",      lambda r, f, m: r == 5 and f == 1),
    ("At Risk",            lambda r, f, m: r >= 2 and f >= 3 and m >= 3),
    ("Hibernating",        lambda r, f, m: r <= 2 and f <= 2 and m <= 2),
    ("Others",             lambda r, f, m: True),
]


def quintile_score(series: pd.Series, ascending: bool) -> pd.Series:
    labels = [1, 2, 3, 4, 5] if ascending else [5, 4, 3, 2, 1]
    return pd.qcut(series.rank(method="first"), q=5, labels=labels).astype(int)


def assign_segment(r: int, f: int, m: int) -> str:
    for name, rule in SEGMENT_RULES:
        if rule(r, f, m):
            return name
    return "Others"


def compute(df: pd.DataFrame, analysis_date: date, window_months: int) -> pd.DataFrame:
    window_start = analysis_date - timedelta(days=window_months * 30)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df[df["order_date"].dt.date >= window_start].copy()

    agg = (
        df.groupby("customer_id")
        .agg(
            last_order_date=("order_date", "max"),
            frequency=("order_id", "nunique"),
            monetary=("order_amount", "sum"),
        )
        .reset_index()
    )
    agg["recency"] = (pd.Timestamp(analysis_date) - agg["last_order_date"]).dt.days

    agg["R"] = quintile_score(agg["recency"], ascending=False)
    agg["F"] = quintile_score(agg["frequency"], ascending=True)
    agg["M"] = quintile_score(agg["monetary"], ascending=True)
    agg["rfm_score"] = agg["R"].astype(str) + agg["F"].astype(str) + agg["M"].astype(str)
    agg["segment"] = agg.apply(lambda row: assign_segment(row["R"], row["F"], row["M"]), axis=1)

    return agg[["customer_id", "recency", "frequency", "monetary", "R", "F", "M", "rfm_score", "segment"]]


def verify():
    rows = [
        ("C001", "O1", "2026-03-20", 200),
        ("C001", "O2", "2026-04-01", 100),
        ("C002", "O3", "2025-06-01", 500),
        ("C003", "O4", "2026-04-07", 50),
    ]
    df = pd.DataFrame(rows, columns=["customer_id", "order_id", "order_date", "order_amount"])
    result = compute(df, date(2026, 4, 9), 12)

    c1 = result[result["customer_id"] == "C001"].iloc[0]
    assert c1["recency"] == 8,      f"Expected C001 recency=8, got {c1['recency']}"
    assert c1["frequency"] == 2,    f"Expected C001 frequency=2, got {c1['frequency']}"
    assert c1["monetary"] == 300.0, f"Expected C001 monetary=300, got {c1['monetary']}"

    c3 = result[result["customer_id"] == "C003"].iloc[0]
    assert c3["recency"] == 2,      f"Expected C003 recency=2, got {c3['recency']}"

    # C003 has R=5 (most recent), F=1 (least frequent) → New Customers
    assert c3["segment"] == "New Customers", f"Expected New Customers, got {c3['segment']}"

    print("All verify() assertions passed.")


def main():
    parser = argparse.ArgumentParser(description="RFM scorer")
    parser.add_argument("--input", help="Path to transactions CSV")
    parser.add_argument("--output", default="rfm_output.csv", help="Output path")
    parser.add_argument("--verify", action="store_true", help="Run built-in sanity tests")
    args = parser.parse_args()

    if args.verify:
        verify()
        sys.exit(0)

    if not args.input:
        parser.print_help()
        sys.exit(1)

    df = pd.read_csv(args.input)
    result = compute(df, ANALYSIS_DATE, WINDOW_MONTHS)
    result.to_csv(args.output, index=False)
    print(f"Wrote {len(result)} customers to {args.output}")


if __name__ == "__main__":
    main()
```
