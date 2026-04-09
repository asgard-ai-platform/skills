# Content Analytics — 內容績效分析參考

## 核心指標體系

### 指標層級：由淺到深

```
Layer 1 — 曝光 (Reach)
  └── Impressions、Reach、Follower Growth

Layer 2 — 互動 (Engagement)
  └── Likes、Comments、Shares、Saves、Clicks

Layer 3 — 行動 (Action)
  └── Link Clicks、Profile Visits、DMs、Website Traffic

Layer 4 — 轉換 (Conversion)
  └── Email Sign-ups、Purchases、Lead Forms
```

**原則**：Layer 1-2 是 Vanity Metrics（虛榮指標）。Layer 3-4 才是業務指標。每月回顧時，Layer 3-4 的數字比 Layer 1-2 更重要。

---

## 必追蹤的六個指標與公式

### 1. Engagement Rate (互動率)

```
ER = (Likes + Comments + Shares + Saves) / Reach × 100%
```

**計算範例**：
- 一篇 IG 貼文：Reach = 2,400、Likes = 180、Comments = 24、Shares = 12、Saves = 60
- ER = (180 + 24 + 12 + 60) / 2,400 × 100% = 276 / 2,400 × 100% = **11.5%**

**行業基準（2024）**：

| 平台 | 低於平均 | 正常 | 優秀 |
|------|---------|------|------|
| Instagram | < 1% | 1–3% | > 5% |
| Facebook | < 0.5% | 0.5–1% | > 2% |
| LinkedIn | < 1% | 2–4% | > 5% |
| X (Twitter) | < 0.5% | 0.5–1% | > 2% |

> 注意：Reach-based ER 和 Follower-based ER 是不同公式。平台原生報表常用 Follower-based（分母為粉絲數而非觸及數）。跨平台比較時必須統一公式。

---

### 2. Save Rate (儲存率) — 內容價值指標

```
Save Rate = Saves / Reach × 100%
```

Saves 是最能代表「內容是否有實用價值」的訊號。使用者儲存貼文代表「這個我之後用得到」。

**基準**：Save Rate > 2% 代表內容有強烈實用性。

**實作**：每月找出 Save Rate 最高的前 3 篇，分析它們的共同特徵（格式？主題？Pillar？），下個月加重製作。

---

### 3. Share Rate (分享率) — 病毒性指標

```
Share Rate = Shares / Reach × 100%
```

Shares 代表「我的朋友也需要看到這個」。是自然觸及的引擎。

**基準**：Share Rate > 1% 是優秀的自然擴散訊號。

---

### 4. Click-Through Rate (連結點擊率)

```
CTR = Link Clicks / Impressions × 100%
```

**計算範例**：
- LinkedIn 文章：Impressions = 5,200、Link Clicks = 94
- CTR = 94 / 5,200 × 100% = **1.8%**

**行業基準**：

| 平台 | 平均 CTR |
|------|---------|
| Instagram (bio link) | 0.5–1% |
| Facebook 貼文 | 1–3% |
| LinkedIn 貼文 | 1–2% |
| Email newsletter | 2–5% |

---

### 5. Follower Growth Rate (粉絲成長率)

```
Growth Rate = (新增粉絲 - 流失粉絲) / 月初粉絲數 × 100%
```

**計算範例**：
- 月初：12,400 粉絲
- 本月新增：380、流失：90
- Net new = 290
- Growth Rate = 290 / 12,400 × 100% = **2.3%**

**基準**：月成長率 > 2% 是健康的有機成長。< 0.5% 需要重新審視策略。

---

### 6. Content ROI (內容投報率) — 進階指標

```
Content ROI = (Social-attributed Revenue - Content Production Cost) / Content Production Cost × 100%
```

若無法直接追蹤 Revenue，用「轉換事件數 × 平均訂單價值」估算 Social-attributed Revenue。

需在 GA4 或後端設定 UTM 參數才能追蹤。

---

## Monthly Performance Review — 標準流程

### Step 1：收集數據（第 1-2 天）

從各平台原生分析工具匯出：

```
每篇貼文需要的欄位：
- 貼文日期
- 平台
- Content Pillar
- 格式（Carousel / Reel / 靜態圖 / 文字）
- Reach
- Impressions
- Likes / Comments / Shares / Saves
- Link Clicks
- Follower 變化（發文日當天）
```

匯出工具：Instagram Insights、Facebook Business Suite、LinkedIn Analytics、X Analytics

---

### Step 2：計算彙總指標（第 2 天）

使用試算表，計算當月整體：

| 指標 | 計算方式 | 本月 | 上月 | 變化 |
|------|---------|------|------|------|
| 總發文數 | COUNT | 24 | 22 | +2 |
| 平均 ER | AVG(所有貼文 ER) | 4.2% | 3.8% | +0.4pp |
| 平均 Save Rate | AVG(所有貼文 Save Rate) | 1.8% | 1.2% | +0.6pp |
| 粉絲淨增 | 月底 - 月初 | +340 | +210 | +62% |
| 社群導流 | GA4 / UTM | 1,840 | 1,520 | +21% |

---

### Step 3：按 Pillar 分析（第 3 天）

將貼文依 Content Pillar 分組，計算各 Pillar 的平均 ER 和 Save Rate：

```
Pillar 分析範例：

Educational (40%): 平均 ER 6.1%、平均 Save Rate 3.2% ← 最強
Engagement  (20%): 平均 ER 8.4%、平均 Save Rate 0.3% ← ER 高但無實用價值
Promotional (20%): 平均 ER 1.8%、平均 Save Rate 0.1% ← 最低，但必要
Brand Story (10%): 平均 ER 5.2%、平均 Save Rate 0.8%
Curated     (10%): 平均 ER 2.9%、平均 Save Rate 1.1%
```

**結論邏輯**：
- Educational 的 Save Rate 最高 → 下個月維持或增加比例
- Engagement 的 ER 高但 Save Rate 低 → 帶來互動但不帶來忠誠受眾，不要過度增加
- Promotional 的 ER 最低 → 正常現象，但若低於 0.5% 需重新審視文案

---

### Step 4：找出 Top 3 / Bottom 3（第 3 天）

**排序維度**：依 ER 由高到低，找出 Top 3 和 Bottom 3。

**分析 Top 3 的共同特徵**，填寫以下表格：

| 特徵維度 | Top 3 共同點 | Bottom 3 共同點 |
|---------|------------|----------------|
| 格式 | Carousel | 靜態單圖 |
| Pillar | Educational | Promotional |
| 發文時間 | 週二 12:00 / 週四 18:00 | 週一 08:00 |
| 主題類型 | How-to / 懶人包 | 純廣告訊息 |
| 有無 CTA | 有，放第 1 張 | 無或放最後 |

這份表格直接成為下個月的製作指引。

---

### Step 5：製作 Monthly Insight 報告

```markdown
## {Month} 內容績效摘要

### 數字
- 發文：{N} 篇 / {N} 個平台
- 平均 ER：{%}（上月：{%}）
- 粉絲淨增：+{N}（成長率 {%}）
- 社群導流：{N} 次（上月：{N}）

### 本月最強貼文
1. [{貼文描述}] — ER {%}、Saves {N}
   → 為什麼表現好：{1句}

### 本月最弱貼文
1. [{貼文描述}] — ER {%}
   → 原因假設：{1句}

### 下個月調整
- 增加：{具體改變}
- 減少：{具體改變}
- 測試：{要測試的假設}
```

---

## 格式效益對照表

基於各平台普遍觀察到的格式表現差異（並非普遍定律，須以自身數據驗證）：

| 格式 | 適合目標 | 通常 ER | Save Rate | 製作成本 |
|------|---------|---------|-----------|---------|
| Carousel (輪播) | 教育、懶人包 | 高 | 高 | 中 |
| Reel / Short Video | 觸及新受眾 | 中-高 | 低 | 高 |
| 靜態單圖 | 品牌形象、節日 | 中 | 低 | 低 |
| 文字貼文 | LinkedIn 思想領導 | 高（LinkedIn） | 低 | 低 |
| Story / 限時動態 | 即時互動、投票 | 高互動 | 不適用 | 低 |
| UGC 轉發 | 社群建立 | 中 | 低 | 極低 |

**使用方法**：若 Save Rate 是本月主要 KPI，優先排 Carousel；若目標是觸及新受眾，優先排 Reel。

---

## A/B 測試框架

單一變數測試，每次只改一個元素：

### 可測試的變數

| 變數 | 測試方法 | 衡量指標 |
|------|---------|---------|
| 發文時間 | 同類型貼文，Week A 發 12:00，Week B 發 18:00 | Reach、ER |
| 第一張圖的 Hook | 同主題，測試「數字型」vs「問題型」封面 | Carousel 完讀率 |
| CTA 位置 | 文末 CTA vs 文中 CTA | Link Clicks |
| Caption 長度 | 短文案（< 100 字）vs 長文案（> 300 字） | ER、Comments |
| Hashtag 數量 | 5 個 vs 15 個 vs 30 個 | Reach |

### 測試週期

- 最少跑 **4 組同類型貼文**才有足夠樣本
- 控制外部因素：避免在促銷期、節假日前後比較
- 記錄在試算表，持續累積歷史數據

---

## 常見分析陷阱

**Impressions vs Reach 混用**
- Impressions = 貼文被看到的總次數（同一人可重複）
- Reach = 看過貼文的不重複人數
- 計算 ER 應用 Reach 作分母，用 Impressions 會低估互動率

**Follower ER vs Reach ER**
- Follower-based ER = Engagements / Followers → 適合比較帳號整體表現
- Reach-based ER = Engagements / Reach → 適合評估單篇貼文品質
- 兩個數字都有用，但不能混著比較

**用總數而非率**
- 「本月總 Likes 3,200」沒有意義，除非帳號規模固定
- 永遠用比率（ER%、Save Rate%）才能跨月比較

**只看平台原生數據**
- 各平台的 "Reach" 定義略有不同
- 跨平台比較時，用統一的 UTM + GA4 追蹤才可靠

**月底才看數據**
- 應每週 check 一次，能即時發現異常（某篇貼文 ER 特別高 → 立刻追問為什麼、可否複製）
- 月底回顧是彙整，不是第一次看數據

---

## UTM 參數標準格式

社群導流必須加 UTM 才能在 GA4 追蹤：

```
utm_source   = 平台名稱（instagram / facebook / linkedin / x）
utm_medium   = social
utm_campaign = 活動名稱或月份（2024-april / summer-sale）
utm_content  = 貼文識別碼（post-001 / carousel-tips-seo）
```

**範例 URL**：
```
https://example.com/blog/seo-tips
?utm_source=instagram
&utm_medium=social
&utm_campaign=2024-april
&utm_content=carousel-seo-tips-0408
```

在試算表的貼文記錄中加入 UTM URL 欄位，方便後續在 GA4 篩選。

---

## 季度趨勢分析

每季做一次深度回顧，比較三個月的 Pillar 表現：

```
範例：Q1 Pillar ER 趨勢

           Jan    Feb    Mar
Educational  5.2%   6.1%   7.3%  ← 持續成長，策略有效
Promotional  1.4%   1.6%   1.2%  ← 波動，需調整文案
Engagement   7.8%   6.2%   8.1%  ← 不穩定，依賴時事/話題
Brand Story  3.9%   4.4%   5.0%  ← 穩定成長
Curated      2.1%   2.3%   2.2%  ← 平穩，維持現狀
```

季度回顧的輸出：調整下一季的 Content Pillar 比例。若 Educational 持續強，考慮從 40% 提升到 50%，對應壓縮表現較差的 Pillar。
