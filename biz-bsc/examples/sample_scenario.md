以下是 `biz-bsc/examples/sample_scenario.md` 的內容：

```markdown
# Example: 台灣 B2B SaaS 公司的平衡計分卡建置

## Scenario

**公司：** Flowmix（台灣新創，B2B 工作流程自動化 SaaS）
**規模：** 45 人，ARR 約 NT$28M，主要客戶為中型製造業與物流業
**提問者：** 共同創辦人兼 COO

> 「我們現在有一堆 KPI，但感覺各部門在各跑各的。業務在衝新客數、產品在衝功能上線速度、客服在衝工單關閉率。到了季末大家數字都達標，但 ARR 沒長、NRR 在掉。我想用 BSC 把這些指標串起來，但不知道從哪裡下手。」

背景補充：
- 策略方向：「以產品黏著度驅動成長」（Product-Led Growth）
- 近 2 季 NRR 從 108% 掉到 97%，主因是中型客戶在試用期後的轉換率偏低
- 產品 bug 回報率高，工程團隊缺乏數據工具，改版靠直覺
- 員工滿意度調查顯示：工程師覺得「不知道用戶在用哪些功能」

---

## Analysis

### Step 1：確認策略句

根據 COO 描述，策略句定為：

> **「以產品體驗黏著度驅動 ARR 成長，核心是降低試用轉換流失。」**

這不是「廣撒網拉新客」策略，而是「讓現有與新進客戶留下來、用深、往上賣」策略。因此 BSC 的重心應放在 **Customer 與 Internal Process** 兩個視角，L&G 的核心投資是產品分析能力。

---

### Step 2：各視角目標定義

#### Financial（落後指標）
COO 說 ARR 沒長、NRR 在掉。財務目標鎖定：
- 提高 NRR（現有客戶擴張 > 流失）
- 提高 ARR（在 NRR 回穩後才有健康成長基礎）

#### Customer（財務的領先指標）
NRR 掉的直接原因是試用轉換率低。客戶視角目標：
- 提高試用轉正率
- 提高核心功能採用深度（Feature Adoption）

#### Internal Process（客戶體驗的領先指標）
產品 bug 多、靠直覺改版 → 流程目標：
- 縮短 bug 修復週期
- 建立數據驅動的功能優先排序機制

#### Learning & Growth（所有視角的根基）
工程師沒有數據工具、不知道用戶在用哪些功能 → 能力目標：
- 建立產品分析能力（Amplitude）
- 導入使用者旅程追蹤

---

### Step 3：策略地圖（因果鏈）

```
[L&G]      工程 & 產品團隊完成產品分析工具培訓
               ↓
[Internal]  以用戶行為數據驅動功能排序；Bug P1 修復週期縮短
               ↓
[Customer]  試用期核心功能採用率提升；試用轉正率提高
               ↓
[Financial] NRR 回升至 108%+；ARR 成長 30% YoY
```

**邏輯驗證：**
- 若工程師看不到用戶行為（L&G缺口），就無法修對的 bug、排對的功能（Internal缺口）
- 若功能體驗差、bug 多（Internal缺口），試用客戶就不會轉正（Customer缺口）
- 若轉正率低、現有客戶流失（Customer缺口），NRR 與 ARR 就不會成長（Financial缺口）

---

### Step 4：逐目標填入指標、目標值、行動方案

注意：每個目標必須有**指標（Measure）+ 目標值（Target）+ 行動（Initiative）**三件套，缺一不可。

---

## Result

# Balanced Scorecard：Flowmix

## Strategy Statement
以產品體驗黏著度驅動 ARR 成長，核心是降低試用期客戶流失、提高功能採用深度。

## Strategy Map

```
[L&G] 產品分析能力培訓 → 用戶旅程追蹤上線
    ↓
[Internal] Bug P1 修復週期縮短 → 功能排序數據化
    ↓
[Customer] 試用期核心功能採用率提升 → 試用轉正率提高
    ↓
[Financial] NRR 回升 → ARR 年成長 30%
```

## Scorecard

### Financial Perspective

| 目標 | 指標 | 目標值 | 行動方案 |
|------|------|--------|---------|
| 提高客戶擴張收益 | Net Revenue Retention (NRR) | ≥ 108%（Q3 2026 前） | 客戶成功計畫 + 功能體驗改善 |
| 提高年度經常性收益 | Annual Recurring Revenue (ARR) | NT$36M（2026 年底） | 以 NRR 回穩為前提，再啟動新客拓展 |

### Customer Perspective

| 目標 | 指標 | 目標值 | 行動方案 |
|------|------|--------|---------|
| 提高試用轉正率 | Trial-to-Paid Conversion Rate | 從 31% 提升至 48%（Q3 2026） | 試用期第 7/14/21 天自動 check-in + onboarding flow 優化 |
| 提高核心功能採用深度 | Core Feature Adoption Rate（啟用 3+ 核心功能的帳戶比例） | 從 40% 提升至 65%（Q3 2026） | In-app 功能引導 + 使用者旅程重新設計 |

### Internal Process Perspective

| 目標 | 指標 | 目標值 | 行動方案 |
|------|------|--------|---------|
| 縮短關鍵 Bug 修復週期 | P1 Bug Mean Time to Resolution (MTTR) | 從 6 天縮短至 2 天（Q2 2026） | 導入 bug triage SLA + on-call 輪值制度 |
| 數據驅動功能排序 | % 功能 roadmap 項目有用戶行為數據佐證 | 從 15% 提升至 80%（Q2 2026） | 每兩週 product analytics review 會議制度化 |

### Learning & Growth Perspective

| 目標 | 指標 | 目標值 | 行動方案 |
|------|------|--------|---------|
| 建立產品分析能力 | 工程 + 產品人員完成 Amplitude 培訓比例 | 100%（Q1 2026 底） | 4 週內部 bootcamp + 外部顧問 2 次工作坊 |
| 建立完整用戶旅程追蹤 | 關鍵事件（Events）埋點完成率 | 核心 30 個事件 100% 覆蓋（Q1 2026 底） | 由資深工程師主導 tracking plan，納入 sprint definition of done |

## Causal Chain Validation

**L&G → Internal：**
工程與產品團隊完成 Amplitude 培訓、埋點覆蓋核心事件後，才能看到用戶在哪一步流失、哪些功能沒被採用。沒有這個基礎，功能排序就是靠感覺，bug 修復也不知道影響範圍。

**Internal → Customer：**
P1 bug 從 6 天修到 2 天，直接降低試用期客戶因體驗問題放棄的比例。功能排序數據化後，roadmap 優先修用戶真正卡關的地方，核心功能採用率才能提升。

**Customer → Financial：**
試用轉正率從 31% 到 48%，直接增加新增 MRR。核心功能採用率從 40% 到 65%，代表客戶黏著度提升，流失率下降，NRR 從 97% 回升至 108%+ 的基礎才成立。ARR 成長 30% 是這條因果鏈全部打通後的結果，而非起點。

---

> **執行優先順序建議：** 先打通 L&G（Q1），再修 Internal（Q2），Customer 指標在 Q2-Q3 才會反應。不要因為 Financial 指標 Q1 沒動就砍 L&G 投資——那正是因果鏈的設計，落後指標本來就最後才動。
```

請將上述內容寫入 `biz-bsc/examples/sample_scenario.md`。
