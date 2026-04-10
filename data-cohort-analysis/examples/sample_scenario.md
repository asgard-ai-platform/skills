# Example: SaaS 專案管理工具用戶留存下滑調查

## Scenario

**公司**: Taskflow — 一款面向中小企業的 SaaS 專案管理工具，月費制
**問題**: 產品 VP 注意到過去兩季整體月留存率從 72% 降到 67%，懷疑是新用戶品質下滑，但行銷團隊說獲客來源沒變。

> "我們的整體留存在掉，但行銷說 channel mix 沒變。能幫我拆開看看到底哪裡出問題嗎？我需要一張留存表。"

可用資料：PostgreSQL，有 `users` 表（signup_date、plan_type）和 `events` 表（user_id、event_type、event_date）。核心動作定義為 `project_created` 或 `task_assigned`（產品的 core value delivery）。

---

## Analysis

### Phase 1: 定義 Cohort 與活躍

- **Cohort**: 以 `signup_month` 為基準（acquisition cohort）
- **Active**: 當月有至少一次 `project_created` 或 `task_assigned` 事件（排除純登入）
- **時間粒度**: 月（SaaS 訂閱產品適用）
- **分析範圍**: 2024-07 ～ 2025-01 共 7 個月隊列

> 注意：特意排除純登入事件。Taskflow 的 core value 是協作，不是瀏覽。

### Phase 2: 建立留存矩陣

從 PostgreSQL 跑出原始留存矩陣：

```sql
WITH cohorts AS (
  SELECT
    user_id,
    DATE_TRUNC('month', signup_date) AS cohort_month
  FROM users
),
activity AS (
  SELECT DISTINCT
    user_id,
    DATE_TRUNC('month', event_date) AS active_month
  FROM events
  WHERE event_type IN ('project_created', 'task_assigned')
),
retention AS (
  SELECT
    c.cohort_month,
    DATEDIFF('month', c.cohort_month, a.active_month) AS period,
    COUNT(DISTINCT a.user_id) AS active_users
  FROM cohorts c
  JOIN activity a ON c.user_id = a.user_id
  GROUP BY 1, 2
),
cohort_sizes AS (
  SELECT cohort_month, COUNT(*) AS cohort_size FROM cohorts GROUP BY 1
)
SELECT
  r.cohort_month,
  r.period,
  ROUND(100.0 * r.active_users / cs.cohort_size, 1) AS retention_pct
FROM retention r
JOIN cohort_sizes cs ON r.cohort_month = cs.cohort_month
ORDER BY 1, 2;
```

### Phase 3: 識別模式

## Retention Matrix

| Cohort | Size | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|--------|------|-----|-----|-----|-----|-----|-----|-----|
| 2024-07 | 1,240 | 100% | 74% | 62% | 58% | 55% | 54% | 53% |
| 2024-08 | 1,180 | 100% | 73% | 61% | 57% | 54% | 53% | — |
| 2024-09 | 1,310 | 100% | 72% | 60% | 55% | 53% | — | — |
| 2024-10 | 1,420 | 100% | 68% | 54% | 49% | — | — | — |
| 2024-11 | 1,650 | 100% | 63% | 50% | — | — | — | — |
| 2024-12 | 1,890 | 100% | 58% | — | — | — | — | — |
| 2025-01 | 2,100 | 100% | — | — | — | — | — | — |

> 熱圖觀察：2024-10 之後明顯變暗，M1 留存從 72-74% 跌至 58-68%。

**三個關鍵發現：**

1. **留存曲線形狀（正面）**: 2024-07 ～ 09 隊列在 M4 之後趨於平緩（53-55%），代表有穩定核心用戶群，產品本身並無根本問題。

2. **隊列趨勢惡化（警報）**: M1 留存從 Jul 隊列的 74% 連續下滑到 Dec 隊列的 58%，差距 16pp。這是系統性問題，不是隨機波動。

3. **關鍵斷崖點**: M0 → M1 是最大流失點，且惡化集中在 2024-10 之後開始的隊列。

### Phase 4: 連結行動

**問題定位**：2024-10 是什麼改變了？

對照產品變更日誌：
- **2024-09-15**: 新版 onboarding wizard 上線（原 5 步驟壓縮為 2 步驟）
- **2024-10-01**: 行銷擴大 Google Ads 預算 40%，帶入更多 SMB 長尾關鍵字流量

兩個假說：
- **假說 A**: 新 onboarding 太簡化，用戶沒有真正完成 setup，第一個月就放棄
- **假說 B**: 新流量來源用戶 intent 較低，天生留存就差

交叉驗證：將 2024-10 隊列按 `onboarding_completed` 事件切分：

| 子群 | 用戶數 | M1 留存 |
|------|--------|---------|
| 完成新 onboarding | 680 | 74% |
| 未完成 onboarding | 740 | 44% |

> **結論**: 假說 A 成立。新 onboarding 完成率從 78% 跌至 48%（因步驟刪減，用戶未建立第一個 project 就離開）。完成 onboarding 的用戶 M1 留存與舊隊列相當。

### Phase 5: LTV 試算

以 ARPU = $45/月，比較 Jul 隊列 vs Dec 隊列的 12 個月 LTV：

| 期間 | Jul 隊列留存 | Dec 隊列留存（預估） |
|------|------------|-----------------|
| M1 | 74% | 58% |
| M3 | 58% | 42%（估） |
| M6 | 53% | 36%（估） |
| M12 | 50%（估） | 33%（估） |

- **Jul 隊列 LTV（12M）≈ $45 × (1+0.74+0.62+0.58+0.55+0.54+0.53×6) ≈ $252**
- **Dec 隊列 LTV（12M）≈ $45 × (1+0.58+0.50+0.42+0.36+0.33×8) ≈ $196**

Dec 隊列每位用戶 LTV 較 Jul 隊列少約 **$56（-22%）**，以 Dec 隊列 1,890 人計算，預期損失 LTV 約 **$105,840**。

---

## Result

# Cohort Analysis: Taskflow 用戶留存調查

## Cohort Definition
- Cohort: 用戶 signup_month（acquisition cohort）
- Activity: 當月有 `project_created` 或 `task_assigned`（排除純登入）
- Period: Monthly

## Retention Matrix
（見上方 Phase 3 表格）

## Key Findings
1. **留存曲線形狀健康**：老隊列（Jul-Sep）M4 後趨平於 53-55%，產品核心無問題
2. **新隊列系統性惡化**：M1 留存從 74% 跌至 58%，惡化起點為 2024-10 隊列
3. **關鍵斷崖點**：M0 → M1，且可追溯至 onboarding 完成率下滑（78% → 48%）

## Cohort Comparison
| Metric | Jul 2024 隊列 | Dec 2024 隊列 | Delta |
|--------|-------------|-------------|-------|
| M1 留存 | 74% | 58% | −16pp |
| M3 留存 | 58% | 42%（預估） | −16pp |
| 12M LTV | $252 | $196 | −22% |

## Recommendations
1. **立即**: 還原或修復 onboarding wizard — 確保用戶在 Day 7 前完成「建立第一個 project」，此為留存 leading indicator
2. **本週**: 對 2024-10 之後隊列中「未完成 onboarding」的用戶發送 re-engagement email，附操作引導影片
3. **下季**: A/B 測試新版 onboarding 變體，以 M1 留存率（而非 onboarding 完成率）為主要指標，避免假陽性
4. **監控**: 建立每週隊列留存 dashboard，以 M1 留存為早期預警指標（而非等到整體留存數字才反應）
