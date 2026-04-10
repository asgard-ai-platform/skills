以下是 `meta-structured-problem/examples/sample_scenario.md` 的完整內容：

````markdown
# Example: SaaS 公司 ARR 成長停滯診斷

## Scenario

**用戶問題：**
「我是 Futurepath（一間台灣 B2B SaaS，做 HR 人力資源管理系統）的 CEO。我們去年 ARR 成長率從 80% 跌到 22%，這個月的 MRR 幾乎零成長。我知道哪裡出了問題，但說不清楚，也不知道從哪裡開始解決。幫我理清楚。」

**背景數據（用戶提供）：**
- ARR：NT$48M（2025 年底）
- 客戶數：320 家中小企業
- 平均 ACV：NT$150K
- 月 churn rate：從 1.2% 漲至 2.8%（過去 6 個月）
- 新客戶簽約：Q4 2025 掉了 40%
- 主要競爭者：Workday（大企業）、本土新創 HRex（2024 年 3 月進市場）

---

## Analysis

### Step 1 — 定義問題

**可測量的問題陳述：**
Futurepath 的 MRR 成長在 2025 Q3 後接近停滯——新簽約下滑 40% + churn 從 1.2% 升至 2.8%，使淨新增 MRR ≈ 0。需要找出根本原因並在 90 天內提出可行方案。

---

### Step 2 — Issue Tree（MECE 分解）

```
ARR 成長停滯
├── A. 新客戶獲取下降？（流入端）
│   ├── A1. 市場需求本身萎縮？
│   │    └── 台灣 SMB HR SaaS 整體市場放緩？
│   ├── A2. 我們的獲客漏斗出問題？
│   │    ├── A2a. 行銷漏斗：Lead 數量下降？
│   │    └── A2b. 銷售漏斗：Lead→Close 轉換率下降？
│   └── A3. 競爭者搶走我們的 Prospect？
│        └── HRex 新進市場，以低價切入？
└── B. 現有客戶流失加速？（留存端）
    ├── B1. 產品問題：功能落後競爭者？
    ├── B2. 服務問題：客戶成功/支援品質惡化？
    └── B3. 價格問題：客戶因成本壓縮而流失？
```

**MECE 檢查：**
- 互斥性 ✓（流入端 vs 留存端不重疊）
- 完整性 ✓（SMB SaaS ARR 變化 = 新客×ACV − 流失×ACV；所有可能路徑皆覆蓋）

---

### Step 3 — 優先排序（80/20）

| 分支 | 優先度 | 理由 |
|------|--------|------|
| B（churn 上升） | 🔴 最高 | Churn 從 1.2%→2.8% 代表每月多流失約 NT$800K MRR，比新簽約下滑影響更直接 |
| A3（HRex 競爭） | 🟠 高 | 時間點吻合（HRex 2024 Q1 進場，Q3 開始有感）|
| A2b（銷售轉換） | 🟡 中 | Lead 數未知，轉換率下滑可能反映定位問題 |
| A1（市場萎縮） | 🟢 低 | 台灣數位轉型仍成長，市場萎縮可能性低 |

---

### Step 4 — 假設

> **主假設：** ARR 停滯的主因是 HRex 以「免費基本版 + 低價升級」策略同時侵蝕 Futurepath 的新客獲取（A3）和現有客戶留存（B），而非內部執行問題。

**次假設：** 流失的客戶集中在 ACV < NT$100K 的小型客戶，這些客戶對價格最敏感，而非因為功能不滿意。

---

### Step 5 — 收集證據

| 分支 | 子假設 | 數據 | 結論 |
|------|--------|------|------|
| B — Churn 原因 | HRex 是主要流失原因 | Exit survey：68% 流失客戶提及「轉用其他系統」，其中 52% 點名 HRex | ✅ 確認 |
| B — Churn 分佈 | 流失集中在小型客戶 | 分析：員工 < 50 人的客戶 churn 4.1%；50-200 人的 1.4% | ✅ 確認 |
| A3 — 競爭侵蝕 | HRex 搶走 Prospect | 銷售 CRM：Q4 有 23 個 lost deals 記錄 HRex 為原因，佔總 lost 的 58% | ✅ 確認 |
| B1 — 產品落後 | 功能差距導致流失 | 功能對比：Futurepath 在考勤/薪資功能持平；HRex 在行動 App UI 較優 | ⚠️ 部分 |
| B2 — 服務品質 | CS 反應時間惡化 | Ticket 回應時間從 4hr → 11hr（CS 團隊未隨客戶數擴編） | ⚠️ 次要因素 |
| B3 — 純價格 | 客戶因預算砍掉 SaaS | 僅 12% 流失客戶提及「預算削減」 | ❌ 不是主因 |

**假設修正：** 主假設確認，次假設確認。加入次要發現：CS 服務品質惡化加速了本已因競爭壓力搖擺的小型客戶離開。

---

### Step 6 — 合成

三個彼此強化的問題：
1. **HRex 以低價 + 行動端 UX 直接打 Futurepath 的甜蜜區（50 人以下 SMB）**
2. **小型客戶黏性本就最低，CS 服務惡化成為流失觸發點**
3. **Futurepath 沒有針對性的「防禦產品」或定價策略應對新進者**

---

## Result

# Structured Analysis: Futurepath ARR 成長停滯

## Problem Statement
Futurepath 的月淨新增 MRR 自 2025 Q3 起趨近於零：churn rate 從 1.2% 升至 2.8%（主因 HRex 競爭），新客簽約 Q4 下滑 40%，若不干預，2026 年 ARR 將負成長。

## Issue Tree
（詳見 Analysis Step 2 完整分解）

## Hypothesis
HRex 以免費基本版策略同時侵蝕新客獲取與小型現有客戶留存；CS 服務品質下滑為加速器。

## Evidence
| 分支 | 子假設 | 證據 | 結論 |
|------|--------|------|------|
| Churn 原因 | HRex 主導流失 | 68% 流失客戶提及換系統，52% 點名 HRex | ✅ 確認 |
| Churn 分佈 | 集中小型客戶 | < 50 人 churn 4.1% vs 50-200 人 1.4% | ✅ 確認 |
| 競爭侵蝕 | HRex 搶 Prospect | Q4 lost deals 58% 因 HRex | ✅ 確認 |
| 服務品質 | CS 反應惡化 | Ticket 回應 4hr → 11hr | ⚠️ 次因 |
| 純價格 | 預算削減 | 僅 12% 流失客戶提及 | ❌ 否認 |

## Synthesis（Pyramid Structure）
**Recommendation：** 推出「Futurepath Lite」免費方案鎖定 < 30 人企業，同時在 60 天內將 CS 回應時間壓回 4 小時以下——這兩個動作可在 Q2 內將 churn 壓回 1.5% 以下，並重建新客漏斗防線。

**Supporting Arguments：**
1. **競爭防禦優先於功能追趕**：HRex 的真正武器是「免費進場」而非功能。若 Futurepath 花 6 個月追趕行動 App UI，HRex 早已完成客戶遷移。免費方案能在客戶決策點攔截競爭者。
2. **小型客戶（< 50 人）是出血點，也是升級引擎**：此族群 churn 4.1%，但佔新簽約的 55%；穩住這一層才有 Land & Expand 升級路徑，是 ARR 長期成長的基礎。
3. **CS 是立即可修復的止血點**：增聘 2 名 CS 專員（成本 NT$1.2M/年）可攔截每月約 NT$2M 因服務不滿而流失的 MRR，ROI 明確且無需產品開發週期。

## Next Steps
1. **Week 1-2**：增聘 2 名 CS，設定 60 天目標：回應時間 ≤ 4hr
2. **Week 2-4**：設計「Futurepath Lite」方案邊界（功能上限、升級觸發條件）
3. **Month 2**：Lite 方案上線，同步聯繫 Q4 lost deals pipeline 重新接觸
4. **Month 3**：檢視 churn 數據；若 < 50 人族群 churn 未降至 2% 以下，啟動定價包重組
````

請將以上內容存為 `meta-structured-problem/examples/sample_scenario.md`。

這個範例的設計重點：
- **Futurepath** 是虛構但具體的台灣 B2B SaaS，有真實數字（NT$48M ARR、churn 1.2%→2.8%、Q4 -40%）
- Issue Tree 在「流入端 vs 留存端」兩層都做了完整 MECE 分解，並附驗核說明
- 假設→證據→修正的迴圈示範了「假設驅動 ≠ 確認偏誤」的 Gotcha
- Result 區段完全對應 SKILL.md 的 Output Format 模板（Problem Statement / Issue Tree / Hypothesis / Evidence / Synthesis / Next Steps）
