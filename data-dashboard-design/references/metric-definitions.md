# Metric Definitions

SQL-based canonical definitions for the KPI hierarchy in `data-dashboard-design`. Each metric includes: business question, formula, SQL template, worked example, and common mistakes.

---

## Why Canonical Definitions Matter

If Marketing calculates "conversion rate" as `signups / visits` and Product calculates it as `paid_users / signups`, every cross-team dashboard conversation becomes a terminology debate. Canonical definitions are the single source of truth — defined once, referenced everywhere.

**Rule**: Every metric on a dashboard must have a corresponding entry in this file or an equivalent data catalog. If it can't be defined precisely, it can't be measured reliably.

---

## North Star Metrics

### Monthly Recurring Revenue (MRR)

**Business question**: How much predictable revenue do we have this month?

**Formula**:
```
MRR = Σ (active_subscriptions × monthly_price_at_billing_period)
```

**SQL**:
```sql
SELECT
  DATE_TRUNC('month', billing_date) AS month,
  SUM(
    CASE
      WHEN billing_interval = 'monthly' THEN amount_usd
      WHEN billing_interval = 'annual'  THEN amount_usd / 12.0
      WHEN billing_interval = 'quarterly' THEN amount_usd / 3.0
    END
  ) AS mrr_usd
FROM subscriptions
WHERE status = 'active'
  AND billing_date BETWEEN :start_date AND :end_date
GROUP BY 1
ORDER BY 1;
```

**Worked example**:
- 100 monthly subscribers @ $29 = $2,900
- 24 annual subscribers @ $240/yr = $240/12 × 24 = $480
- MRR = $3,380

**Variants**:
| Variant | Definition |
|---------|-----------|
| New MRR | MRR from customers acquired this month |
| Expansion MRR | MRR from upgrades/upsells this month |
| Churned MRR | MRR lost from cancellations this month |
| Net New MRR | New MRR + Expansion MRR − Churned MRR |

---

### Daily Active Users (DAU)

**Business question**: How many distinct users performed a meaningful action today?

**Formula**:
```
DAU = COUNT(DISTINCT user_id) WHERE event_date = :date AND action IN (meaningful_actions)
```

**Critical decision**: Define "active". Page view ≠ active. Pick 1-3 actions that signal genuine value delivery.

| Product Type | Reasonable "Active" Definition |
|-------------|-------------------------------|
| Social app | Posted, commented, or liked |
| SaaS tool | Opened a document, ran a query, or created an item |
| E-commerce | Searched, added to cart, or purchased |
| Content platform | Played video > 30 seconds or read > 50% of article |

**SQL**:
```sql
SELECT
  event_date,
  COUNT(DISTINCT user_id) AS dau
FROM user_events
WHERE event_date = :date
  AND event_type IN ('post_created', 'comment_added', 'item_liked')
GROUP BY 1;
```

**Pitfall**: Do not include bot/internal traffic. Add `AND user_type = 'real'` or exclude known internal IP ranges at the source table level, not in every metric query.

---

## L1 Business KPIs

### Customer Acquisition Cost (CAC)

**Business question**: How much does it cost to acquire one paying customer?

**Formula**:
```
CAC = Total Sales & Marketing Spend / New Customers Acquired
      (measured over the same time period)
```

**SQL**:
```sql
WITH spend AS (
  SELECT
    DATE_TRUNC('month', spend_date) AS month,
    SUM(amount_usd) AS total_spend
  FROM marketing_spend
  WHERE spend_date BETWEEN :start_date AND :end_date
  GROUP BY 1
),
new_customers AS (
  SELECT
    DATE_TRUNC('month', first_paid_at) AS month,
    COUNT(DISTINCT user_id) AS acquired
  FROM users
  WHERE first_paid_at BETWEEN :start_date AND :end_date
  GROUP BY 1
)
SELECT
  s.month,
  s.total_spend,
  nc.acquired,
  ROUND(s.total_spend / NULLIF(nc.acquired, 0), 2) AS cac_usd
FROM spend s
JOIN new_customers nc USING (month)
ORDER BY 1;
```

**Worked example**:
- October spend: $45,000
- New paying customers in October: 150
- CAC = $45,000 / 150 = **$300**

**Interpretation**: CAC is meaningless without LTV. The ratio LTV:CAC should be ≥ 3:1 for a healthy SaaS business.

---

### Customer Lifetime Value (LTV)

**Formula (simple)**:
```
LTV = ARPU × Average Customer Lifetime
    = ARPU / Churn Rate
```

**Formula (cohort-based, more accurate)**:
```
LTV = Σ (revenue_in_month_n × retention_rate_at_month_n) for n = 1..N
```

**SQL (simple estimate)**:
```sql
WITH monthly_arpu AS (
  SELECT
    AVG(mrr_per_user) AS arpu_usd
  FROM (
    SELECT user_id, SUM(amount_usd) AS mrr_per_user
    FROM subscriptions
    WHERE status = 'active'
      AND billing_date >= DATE_TRUNC('month', CURRENT_DATE)
    GROUP BY user_id
  ) sub
),
monthly_churn AS (
  SELECT
    churned_count * 1.0 / start_count AS monthly_churn_rate
  FROM (
    SELECT
      COUNT(*) FILTER (WHERE status = 'active'   AND snapshot_date = :month_start) AS start_count,
      COUNT(*) FILTER (WHERE status = 'churned'  AND churned_at BETWEEN :month_start AND :month_end) AS churned_count
    FROM user_snapshots
  ) sub
)
SELECT
  arpu_usd,
  monthly_churn_rate,
  ROUND(arpu_usd / NULLIF(monthly_churn_rate, 0), 2) AS ltv_usd,
  ROUND((arpu_usd / NULLIF(monthly_churn_rate, 0)) /
        (SELECT cac_usd FROM cac_latest), 2) AS ltv_cac_ratio
FROM monthly_arpu, monthly_churn;
```

**Worked example**:
- ARPU: $50/month
- Monthly churn: 2.5%
- LTV = $50 / 0.025 = **$2,000**
- If CAC = $300, then LTV:CAC = 6.7x (healthy)

---

### Churn Rate

**Formula**:
```
Monthly Churn Rate = Churned Customers in Month / Customers at Start of Month
```

**Two schools of thought**:

| Method | Formula | When to Use |
|--------|---------|-------------|
| Logo churn | Churned accounts / Starting accounts | When all accounts matter equally |
| Revenue churn | Churned MRR / Starting MRR | When large and small accounts differ significantly |

**SQL (logo churn)**:
```sql
SELECT
  month,
  churned_count,
  start_count,
  ROUND(churned_count * 100.0 / NULLIF(start_count, 0), 2) AS churn_rate_pct
FROM (
  SELECT
    DATE_TRUNC('month', event_date) AS month,
    COUNT(*) FILTER (WHERE event_type = 'subscription_cancelled') AS churned_count,
    COUNT(DISTINCT user_id) FILTER (WHERE status = 'active' AT :month_start)   AS start_count
  FROM subscription_events
  GROUP BY 1
) sub
ORDER BY month;
```

**Pitfall**: Customers who pause ≠ customers who churn. Decide upfront which status transitions count as churn and encode it in the source table definition.

---

### Retention Rate (Cohort)

**Formula**:
```
Retention(cohort, month_n) = Users_active_in_month_n / Users_in_cohort
```

**SQL (cohort retention matrix)**:
```sql
WITH cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', created_at) AS cohort_month
  FROM users
  WHERE created_at >= :start_date
),
activity AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', event_date) AS activity_month
  FROM user_events
)
SELECT
  c.cohort_month,
  DATEDIFF('month', c.cohort_month, a.activity_month) AS months_since_signup,
  COUNT(DISTINCT a.user_id) AS retained_users,
  COUNT(DISTINCT c.user_id) AS cohort_size,
  ROUND(COUNT(DISTINCT a.user_id) * 100.0 / COUNT(DISTINCT c.user_id), 1) AS retention_pct
FROM cohorts c
LEFT JOIN activity a ON c.user_id = a.user_id
  AND a.activity_month >= c.cohort_month
GROUP BY 1, 2
ORDER BY 1, 2;
```

**Reading the output**:
```
cohort_month | months_since | retained | cohort_size | retention_pct
2025-01      | 0            | 500      | 500         | 100.0
2025-01      | 1            | 350      | 500         | 70.0
2025-01      | 2            | 280      | 500         | 56.0
2025-01      | 3            | 260      | 500         | 52.0   ← flattening = good
```

A flattening curve means you have a retained core. A line that keeps falling to near zero means the product has a fundamental engagement problem no dashboard can fix.

---

## L2 Driving Metrics

### Conversion Rate

**Business question**: What fraction of users complete the target action?

**Formula**:
```
Conversion Rate = Users who completed action / Users who started funnel step
```

**The funnel matters more than the single number**. Always define conversion rate with explicit start and end events:

| Name | Start Event | End Event |
|------|------------|----------|
| Visit-to-signup | Page view (landing) | Account created |
| Signup-to-paid | Account created | First payment |
| Trial-to-paid | Trial started | Subscription activated |
| Cart-to-purchase | Item added to cart | Order completed |

**SQL (funnel step conversion)**:
```sql
WITH funnel AS (
  SELECT
    session_id,
    MAX(CASE WHEN event_type = 'landing_page_view'  THEN 1 ELSE 0 END) AS step_1,
    MAX(CASE WHEN event_type = 'signup_form_viewed' THEN 1 ELSE 0 END) AS step_2,
    MAX(CASE WHEN event_type = 'account_created'    THEN 1 ELSE 0 END) AS step_3,
    MAX(CASE WHEN event_type = 'first_payment'      THEN 1 ELSE 0 END) AS step_4
  FROM events
  WHERE event_date BETWEEN :start_date AND :end_date
  GROUP BY session_id
)
SELECT
  SUM(step_1) AS visitors,
  SUM(step_2) AS saw_form,
  SUM(step_3) AS signed_up,
  SUM(step_4) AS paid,
  ROUND(SUM(step_2) * 100.0 / NULLIF(SUM(step_1), 0), 2) AS step1_to_2_pct,
  ROUND(SUM(step_3) * 100.0 / NULLIF(SUM(step_2), 0), 2) AS step2_to_3_pct,
  ROUND(SUM(step_4) * 100.0 / NULLIF(SUM(step_3), 0), 2) AS step3_to_4_pct,
  ROUND(SUM(step_4) * 100.0 / NULLIF(SUM(step_1), 0), 2) AS overall_pct
FROM funnel;
```

---

### Return on Ad Spend (ROAS)

**Formula**:
```
ROAS = Revenue attributable to ads / Ad spend
```

A ROAS of 4x means every $1 spent on ads returned $4 in revenue.

**Attribution model choice changes this number significantly**:

| Model | Definition | Bias |
|-------|-----------|------|
| Last click | 100% credit to last ad touchpoint | Overvalues retargeting |
| First click | 100% credit to first touchpoint | Overvalues awareness |
| Linear | Equal credit across all touchpoints | Dilutes high-impact channels |
| Data-driven | ML-assigned credit per touchpoint | Requires volume (>1,000 conversions/month) |

**SQL (last-click ROAS)**:
```sql
SELECT
  c.channel,
  SUM(s.revenue_usd)   AS attributed_revenue,
  SUM(sp.spend_usd)    AS ad_spend,
  ROUND(SUM(s.revenue_usd) / NULLIF(SUM(sp.spend_usd), 0), 2) AS roas
FROM conversions c
JOIN orders s ON c.order_id = s.order_id
JOIN ad_spend sp ON c.channel = sp.channel
  AND DATE_TRUNC('month', c.converted_at) = DATE_TRUNC('month', sp.spend_date)
WHERE c.converted_at BETWEEN :start_date AND :end_date
GROUP BY 1
ORDER BY roas DESC;
```

**Pitfall**: ROAS ignores margin. A 3x ROAS on a 20% margin product is unprofitable. Use **MER** (Marketing Efficiency Ratio = Total Revenue / Total Marketing Spend) for a blended view that is harder to game by channel.

---

### Average Revenue Per User (ARPU)

**Formula**:
```
ARPU = Total Revenue in Period / Active Users in Period
```

**SQL**:
```sql
SELECT
  DATE_TRUNC('month', p.payment_date) AS month,
  SUM(p.amount_usd) AS total_revenue,
  COUNT(DISTINCT u.user_id) AS active_users,
  ROUND(SUM(p.amount_usd) / NULLIF(COUNT(DISTINCT u.user_id), 0), 2) AS arpu_usd
FROM payments p
JOIN (
  SELECT DISTINCT user_id, DATE_TRUNC('month', event_date) AS month
  FROM user_events
) u ON DATE_TRUNC('month', p.payment_date) = u.month
WHERE p.payment_date BETWEEN :start_date AND :end_date
GROUP BY 1
ORDER BY 1;
```

**Segment ARPU separately**: A blended ARPU of $40 can hide a free tier dragging down a premium tier worth $200. Always show ARPU by plan tier or segment.

---

## L3 Diagnostic Metrics

These metrics rarely live on executive dashboards. They explain *why* L1/L2 metrics moved.

### Funnel Drop-off Rate

```
Drop-off Rate at Step N = 1 − (Users at Step N+1 / Users at Step N)
```

Use this to prioritize where to invest in funnel optimization. A 60% drop from signup form → account created is a bigger lever than a 5% drop from account created → first login.

### Feature Adoption Rate

```
Feature Adoption = Users who used feature X / Total active users
```

```sql
SELECT
  DATE_TRUNC('week', event_date) AS week,
  COUNT(DISTINCT user_id) FILTER (WHERE event_type = 'feature_x_used') AS adopted,
  COUNT(DISTINCT user_id) AS total_active,
  ROUND(
    COUNT(DISTINCT user_id) FILTER (WHERE event_type = 'feature_x_used') * 100.0
    / NULLIF(COUNT(DISTINCT user_id), 0), 1
  ) AS adoption_pct
FROM user_events
WHERE event_date BETWEEN :start_date AND :end_date
GROUP BY 1
ORDER BY 1;
```

### Time to First Value (TTFV)

**Definition**: Minutes/hours from account creation to the first "aha moment" event.

```
TTFV = timestamp(first_value_event) − timestamp(account_created)
```

```sql
SELECT
  PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY ttfv_minutes) AS p50_minutes,
  PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY ttfv_minutes) AS p90_minutes,
  AVG(ttfv_minutes) AS mean_minutes
FROM (
  SELECT
    u.user_id,
    DATEDIFF('minute', u.created_at, MIN(e.event_timestamp)) AS ttfv_minutes
  FROM users u
  JOIN user_events e ON u.user_id = e.user_id
    AND e.event_type = 'first_value_event'
  WHERE u.created_at >= :start_date
  GROUP BY u.user_id, u.created_at
) sub;
```

Use **p50 and p90**, not mean. A small number of users taking 10 hours can inflate the mean and hide that most users reach value in 5 minutes.

---

## Metric Quality Checklist

Before adding a metric to a dashboard, verify:

| Check | Question |
|-------|---------|
| **Actionable** | If this number changes, what would we do differently? |
| **Owned** | Which team is responsible for moving this number? |
| **Defined** | Is there an exact SQL definition in this file or the data catalog? |
| **Timely** | Is the data pipeline refresh rate fast enough for the dashboard audience? |
| **Trustworthy** | Is the "last updated" timestamp visible on the dashboard? |
| **Comparable** | Is there a prior period, target, or benchmark for context? |

A metric that fails more than one of these checks should not be on a production dashboard.

---

## Naming Conventions for SQL Definitions

Use this pattern consistently in your data warehouse views:

```
dm_{domain}_{metric_name}_{granularity}

Examples:
  dm_revenue_mrr_monthly
  dm_acquisition_cac_monthly
  dm_engagement_dau_daily
  dm_retention_cohort_monthly
```

Each view should include:
- `as_of_date` — when the row was last computed
- `period_start`, `period_end` — the measurement window
- The metric value column, named `{metric_name}_{unit}` (e.g., `mrr_usd`, `cac_usd`, `dau_count`)
