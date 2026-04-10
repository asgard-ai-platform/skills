# Example: SaaS 新創電商 SaaS 的執行長儀表板重設計

## Scenario

**公司**：Cartify（B2B 電商 SaaS，月訂閱制，200 家中小企業客戶）
**提問者**：Head of Data，Amy Chen

> 我們現在的 Looker 儀表板有 47 個圖表，每次開週會高層都說「找不到重點」。
> CEO 只想知道公司有沒有在成長，但他得翻好幾頁才能看到 MRR。
> 另外 CS 團隊也一直說報表跑得很慢。能幫我重新設計嗎？

**現況痛點**：
- 1 張儀表板服務 CEO、CS、工程三個受眾
- 47 個圖表，無層級，無排序邏輯
- 載入時間 > 30 秒（底層跑全量 JOIN）
- 沒有 last updated 時間戳記

---

## Analysis

### Step 1：拆分受眾，One Dashboard One Audience

目前是一張儀表板服務所有人 → 違反 Iron Law。重新切成三張：

| 儀表板 | 受眾 | 核心問題 | 刷新頻率 |
|--------|------|----------|----------|
| **Growth Overview** | CEO、董事會 | 我們在成長嗎？健康嗎？ | 每週 |
| **CS Operations** | CS Lead、客戶成功 | 哪些客戶有流失風險？ | 每日 |
| **System Health** | 工程、SRE | 服務穩定嗎？ETL 正常嗎？ | 即時 |

本次聚焦：**CEO 的 Growth Overview**

---

### Step 2：建立 KPI Hierarchy

Cartify 的 North Star：**Net MRR Growth**（月淨新增訂閱收入）

```
              [Net MRR Growth]
             /                \
    [New MRR]              [Churned MRR]
    /        \              /           \
[New Logos] [Expansion]  [Churn Rate] [Contraction MRR]
    |
[Trial → Paid CVR]
```

**L1 KPIs（本月快照）**
- Net MRR Growth：+$18,400（目標 +$20,000）
- Churn Rate：2.1%（警戒線 3%）
- Net Revenue Retention（NRR）：108%

**L2 Driving Metrics**
- New Logos：14 家（上月 11 家）
- Trial → Paid CVR：22%（業界均值 ~18%）
- Expansion MRR：+$4,200（upsell 貢獻）
- Churned MRR：-$6,800（3 家客戶未續約）

---

### Step 3：選擇正確圖表類型

| 指標 | 選用圖表 | 原因 |
|------|----------|------|
| Net MRR Growth 本月 | **Scorecard + vs 目標** | 一秒掌握，不需要讀圖 |
| MRR 12 個月走勢 | **Line chart**（堆疊：New/Expansion/Churned） | 趨勢 + 組成同時呈現 |
| Churn Rate | **Gauge**（紅色警戒 >3%） | 立刻看出是否超標 |
| NRR | **Bullet chart**（vs 100% 基準線） | 直覺呈現是否 expansion-led |
| New Logos by 行業 | **Horizontal bar chart** | 行業名稱較長，橫向易讀 |
| Trial CVR 漏斗 | **Funnel chart**（Trial → Active → Paid） | 顯示流失點 |

**不選 pie chart**：New Logos 有 6 個行業分類，角度差異小，改用橫條圖。

---

### Step 4：版面佈局（Above the Fold 原則）

```
┌─────────────────┬──────────────────┬──────────────┐
│  Net MRR Growth │   Churn Rate     │     NRR      │
│  +$18,400       │   2.1% 🟢        │   108%       │
│  (目標 $20,000) │   Gauge          │   Bullet     │
├─────────────────┴──────────────────┴──────────────┤
│         MRR 走勢（12 個月）Line Chart              │
│         New ■  Expansion ■  Churned ■             │
├───────────────────┬────────────────────────────────┤
│ New Logos         │ Trial → Paid Funnel            │
│ by Industry       │ 450 Trial → 310 Active → 99   │
│ Horizontal Bar    │ Paid (CVR 22%)                 │
└───────────────────┴────────────────────────────────┘
  Last updated: 2024-03-11 06:00 UTC  (ETL: ✅ Normal)
```

**總計 7 個元件**，符合執行層儀表板 5–8 個上限。

---

### Step 5：效能問題處理

CS 抱怨的慢查詢根因：所有圖表共用一個 47-table JOIN 的 view。

建議：
- 將 MRR metrics 預計算為 `daily_mrr_snapshot` materialized table（每日凌晨 05:00 跑）
- CEO 儀表板只查 snapshot，不碰原始事件表
- 預期載入從 30s → < 3s

---

## Result

```markdown
# Dashboard Specification: Growth Overview — Cartify

## Purpose & Audience
- Audience: CEO、Co-founders、董事會觀察者
- Key question: 公司 MRR 是否健康成長？流失是否受控？
- Refresh: 每日凌晨更新（ETL 05:00 UTC），週會前已備妥

## KPI Hierarchy
- North Star: Net MRR Growth（月）
- L1 KPIs: Churn Rate, Net Revenue Retention (NRR), New Logos
- L2 Driving Metrics: Trial→Paid CVR, Expansion MRR, Churned MRR by reason

## Layout
| Position | Component | Chart Type | Metric |
|----------|-----------|-----------|--------|
| Top-left | North Star | Scorecard + vs target | Net MRR Growth $18,400 / $20,000 |
| Top-mid | Health signal | Gauge | Churn Rate 2.1%（警戒 3%）|
| Top-right | Expansion signal | Bullet chart | NRR 108% vs 100% |
| Mid-full | Trend | Stacked line | MRR 12-month: New/Expansion/Churned |
| Bottom-left | Acquisition mix | Horizontal bar | New Logos by industry |
| Bottom-right | Conversion | Funnel | Trial → Active → Paid |
| Footer | Data freshness | Text | Last updated + ETL status |

## Filters
- Date range（預設：當月 vs 上月）
- 客戶規模（SMB / Mid-market）

## Alerts
| Metric | Threshold | Alert To |
|--------|-----------|---------|
| Churn Rate | > 3% | CEO, CS Lead（Slack #alerts-growth）|
| Net MRR Growth | < $15,000（月中預測） | CEO, CFO |
| ETL failure | 06:30 仍未更新 | Data Engineer on-call |
```

**遷移建議**：
1. 現有 47 圖表儀表板標記為 `[DEPRECATED - 2024-04-01]`，給 CS 和工程各自的新儀表板 2 週準備期
2. CEO 版本先以 Looker 現有工具重建，無需換工具
3. 3 個月後依使用頻率決定是否遷移至 Metabase（成本較低，查詢速度相近）
