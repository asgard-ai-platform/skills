# Retention SQL Query Templates

SQL 是建構 Retention Matrix 最直接的工具。本文提供可直接複用的查詢模板，以 PostgreSQL 語法為主，附 BigQuery 差異說明。

---

## 前置假設：事件表結構

所有查詢假設你有一張事件表，schema 如下：

```sql
-- 事件表（activity log）
CREATE TABLE events (
    user_id     BIGINT,
    event_type  VARCHAR(64),   -- 'signup', 'purchase', 'login', etc.
    created_at  TIMESTAMP
);
```

若你的資料庫是 SaaS 訂閱模式（有 subscription 表），見最後一節。

---

## Step 1：定義 Cohort（取得每位用戶的 cohort 日期）

最常見的 cohort 定義是「首次事件日期」，通常取月份粒度：

```sql
-- cohort_month = 用戶第一次發生指定事件的月份
CREATE TEMP TABLE user_cohorts AS
SELECT
    user_id,
    DATE_TRUNC('month', MIN(created_at))::DATE AS cohort_month
FROM events
WHERE event_type = 'signup'   -- 換成你的 cohort 起點事件
GROUP BY user_id;
```

> **注意**：`event_type = 'signup'` 是 cohort 起點，不是「活躍」的定義。這兩個定義必須分開。

---

## Step 2：定義活躍事件（每位用戶每月是否活躍）

```sql
-- 每位用戶每個月，是否有發生「核心價值」事件
CREATE TEMP TABLE user_activity AS
SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', created_at)::DATE AS activity_month
FROM events
WHERE event_type IN ('purchase', 'create_document', 'send_message')
  -- 替換成你產品的「核心價值動作」，不要用 login
;
```

---

## Step 3：計算每個 cohort 在每個月份的 period offset

```sql
-- 對每個用戶，計算每次活躍距離 cohort_month 的月數差
CREATE TEMP TABLE cohort_activity AS
SELECT
    c.user_id,
    c.cohort_month,
    a.activity_month,
    -- 月份差 = period offset（M0, M1, M2...）
    (DATE_PART('year', a.activity_month) - DATE_PART('year', c.cohort_month)) * 12
    + DATE_PART('month', a.activity_month) - DATE_PART('month', c.cohort_month)
    AS period_offset
FROM user_cohorts c
JOIN user_activity a USING (user_id)
WHERE a.activity_month >= c.cohort_month;   -- 不可能在 cohort 之前活躍
```

---

## Step 4：建立 Retention Matrix

```sql
-- 最終 Retention Matrix：每個 cohort × period_offset 的留存率
WITH cohort_sizes AS (
    SELECT
        cohort_month,
        COUNT(DISTINCT user_id) AS cohort_size
    FROM user_cohorts
    GROUP BY cohort_month
),
retention_counts AS (
    SELECT
        cohort_month,
        period_offset,
        COUNT(DISTINCT user_id) AS retained_users
    FROM cohort_activity
    GROUP BY cohort_month, period_offset
)
SELECT
    r.cohort_month,
    r.period_offset,
    s.cohort_size,
    r.retained_users,
    ROUND(r.retained_users * 100.0 / s.cohort_size, 1) AS retention_pct
FROM retention_counts r
JOIN cohort_sizes s USING (cohort_month)
ORDER BY r.cohort_month, r.period_offset;
```

**範例輸出：**

| cohort_month | period_offset | cohort_size | retained_users | retention_pct |
|---|---|---|---|---|
| 2024-01-01 | 0 | 1200 | 1200 | 100.0 |
| 2024-01-01 | 1 | 1200 | 780 | 65.0 |
| 2024-01-01 | 2 | 1200 | 576 | 48.0 |
| 2024-02-01 | 0 | 950 | 950 | 100.0 |
| 2024-02-01 | 1 | 950 | 570 | 60.0 |

---

## Step 5：轉為寬表（Pivot）方便視覺化

標準 SQL 沒有原生 PIVOT，用條件聚合模擬：

```sql
-- PostgreSQL：手動 pivot（最多顯示 M0–M6）
SELECT
    cohort_month,
    cohort_size,
    ROUND(MAX(CASE WHEN period_offset = 0 THEN retention_pct END), 1) AS m0,
    ROUND(MAX(CASE WHEN period_offset = 1 THEN retention_pct END), 1) AS m1,
    ROUND(MAX(CASE WHEN period_offset = 2 THEN retention_pct END), 1) AS m2,
    ROUND(MAX(CASE WHEN period_offset = 3 THEN retention_pct END), 1) AS m3,
    ROUND(MAX(CASE WHEN period_offset = 4 THEN retention_pct END), 1) AS m4,
    ROUND(MAX(CASE WHEN period_offset = 5 THEN retention_pct END), 1) AS m5,
    ROUND(MAX(CASE WHEN period_offset = 6 THEN retention_pct END), 1) AS m6
FROM (
    -- 把 Step 4 的查詢貼在這裡，或建成 VIEW
    SELECT
        r.cohort_month,
        r.period_offset,
        s.cohort_size,
        r.retained_users,
        r.retained_users * 100.0 / s.cohort_size AS retention_pct
    FROM retention_counts r
    JOIN cohort_sizes s USING (cohort_month)
) t
GROUP BY cohort_month, cohort_size
ORDER BY cohort_month;
```

**BigQuery 差異**：BigQuery 支援原生 `PIVOT`，但行數必須是靜態的，動態 pivot 仍需 CASE WHEN 或 `EXECUTE IMMEDIATE`。

---

## 常見變體

### 變體 A：N-day Retention（日粒度，適合 App / 遊戲）

```sql
-- 改用天數差取代月份差
CREATE TEMP TABLE user_cohorts_daily AS
SELECT
    user_id,
    MIN(created_at)::DATE AS cohort_day
FROM events
WHERE event_type = 'signup'
GROUP BY user_id;

CREATE TEMP TABLE cohort_activity_daily AS
SELECT
    c.user_id,
    c.cohort_day,
    a.activity_day,
    (a.activity_day - c.cohort_day) AS day_offset
FROM user_cohorts_daily c
JOIN (
    SELECT DISTINCT user_id, created_at::DATE AS activity_day
    FROM events
    WHERE event_type = 'open_app'
) a USING (user_id)
WHERE a.activity_day >= c.cohort_day;

-- 查 D1 / D7 / D30 Retention
SELECT
    cohort_day,
    COUNT(DISTINCT user_id)                                        AS cohort_size,
    COUNT(DISTINCT CASE WHEN day_offset = 1 THEN user_id END) * 100.0
        / COUNT(DISTINCT user_id)                                  AS d1_retention,
    COUNT(DISTINCT CASE WHEN day_offset = 7 THEN user_id END) * 100.0
        / COUNT(DISTINCT user_id)                                  AS d7_retention,
    COUNT(DISTINCT CASE WHEN day_offset = 30 THEN user_id END) * 100.0
        / COUNT(DISTINCT user_id)                                  AS d30_retention
FROM user_cohorts_daily c
LEFT JOIN cohort_activity_daily a USING (user_id, cohort_day)
GROUP BY cohort_day
ORDER BY cohort_day;
```

> `LEFT JOIN` 確保即使在某天沒有活躍用戶，cohort 列仍然出現（retention = 0）。

### 變體 B：Bounded Retention（「前 N 天內」曾活躍即算）

```sql
-- 前 7 天內（Day 0–6）只要出現一次就算留存
SELECT
    cohort_day,
    COUNT(DISTINCT user_id)                                        AS cohort_size,
    COUNT(DISTINCT CASE WHEN day_offset BETWEEN 1 AND 7
                        THEN user_id END) * 100.0
        / COUNT(DISTINCT user_id)                                  AS d7_bounded_retention
FROM user_cohorts_daily c
LEFT JOIN cohort_activity_daily a USING (user_id, cohort_day)
GROUP BY cohort_day;
```

### 變體 C：Revenue Cohort（每月每 cohort 的 ARPU）

```sql
-- 用 orders 表取代 events，計算 MRR per cohort
WITH user_cohorts AS (
    SELECT user_id, DATE_TRUNC('month', first_order_date)::DATE AS cohort_month
    FROM customers
),
monthly_revenue AS (
    SELECT
        user_id,
        DATE_TRUNC('month', order_date)::DATE AS revenue_month,
        SUM(amount) AS revenue
    FROM orders
    GROUP BY user_id, revenue_month
),
cohort_revenue AS (
    SELECT
        c.cohort_month,
        (DATE_PART('year', r.revenue_month) - DATE_PART('year', c.cohort_month)) * 12
            + DATE_PART('month', r.revenue_month) - DATE_PART('month', c.cohort_month)
            AS period_offset,
        COUNT(DISTINCT c.user_id)  AS cohort_size,
        SUM(r.revenue)             AS total_revenue
    FROM user_cohorts c
    JOIN monthly_revenue r USING (user_id)
    WHERE r.revenue_month >= c.cohort_month
    GROUP BY c.cohort_month, period_offset
)
SELECT
    cohort_month,
    period_offset,
    cohort_size,
    ROUND(total_revenue / cohort_size, 2) AS arpu
FROM cohort_revenue
ORDER BY cohort_month, period_offset;
```

---

## 訂閱模式（Subscription Table）

若資料庫有訂閱表，活躍定義改為「訂閱仍在有效期內」：

```sql
-- subscriptions 表：user_id, start_date, end_date（NULL = 仍活躍）
CREATE TEMP TABLE user_cohorts AS
SELECT
    user_id,
    DATE_TRUNC('month', MIN(start_date))::DATE AS cohort_month
FROM subscriptions
GROUP BY user_id;

-- 用 generate_series 展開每個 cohort 的每個未來月份
WITH months AS (
    SELECT generate_series(
        '2024-01-01'::DATE,
        '2025-12-01'::DATE,
        INTERVAL '1 month'
    )::DATE AS month
),
cohort_x_month AS (
    SELECT c.user_id, c.cohort_month, m.month AS check_month
    FROM user_cohorts c
    CROSS JOIN months m
    WHERE m.month >= c.cohort_month
),
active_check AS (
    SELECT
        cm.user_id,
        cm.cohort_month,
        cm.check_month,
        CASE WHEN EXISTS (
            SELECT 1 FROM subscriptions s
            WHERE s.user_id = cm.user_id
              AND s.start_date <= cm.check_month
              AND (s.end_date IS NULL OR s.end_date >= cm.check_month + INTERVAL '1 month' - INTERVAL '1 day')
        ) THEN 1 ELSE 0 END AS is_active
    FROM cohort_x_month cm
)
SELECT
    cohort_month,
    (DATE_PART('year', check_month) - DATE_PART('year', cohort_month)) * 12
        + DATE_PART('month', check_month) - DATE_PART('month', cohort_month)
        AS period_offset,
    ROUND(AVG(is_active) * 100, 1) AS retention_pct
FROM active_check
GROUP BY cohort_month, period_offset
ORDER BY cohort_month, period_offset;
```

---

## 常見錯誤及修正

| 錯誤 | 症狀 | 修正 |
|------|------|------|
| M0 retention < 100% | cohort_month 和 activity 定義用不同事件 | 確保 cohort 起點事件 ⊆ 活躍事件；或讓 M0 直接等於 cohort_size |
| 重複計算用戶 | `COUNT(user_id)` 而非 `COUNT(DISTINCT user_id)` | 一律用 `COUNT(DISTINCT user_id)` |
| 最近幾個 cohort retention 偏低 | 資料還沒到齊（truncation bias） | 在 UI 或報表中標記「資料不完整」的 cohort；常見做法是只顯示距今 ≥ 3 個月的 cohort |
| cohort 跨時區不一致 | `created_at` 沒有統一轉換時區就截斷 | `DATE_TRUNC('month', created_at AT TIME ZONE 'Asia/Taipei')` |
| 分母包含當月新用戶 | Survivorship bias — 新用戶 M0 = 100% 拉高平均 | 永遠按 cohort 計算，不要計算跨 cohort 的平均 retention |

---

## BigQuery 版本差異

```sql
-- BigQuery：DATE_DIFF 取代手動月份計算
DATE_DIFF(activity_month, cohort_month, MONTH) AS period_offset

-- BigQuery：DATE_TRUNC 語法相同，但轉型不同
DATE_TRUNC(created_at, MONTH) AS cohort_month   -- 不需要 ::DATE

-- BigQuery：generate_series 改用 UNNEST + GENERATE_ARRAY
UNNEST(GENERATE_DATE_ARRAY('2024-01-01', '2025-12-01', INTERVAL 1 MONTH)) AS month
```
