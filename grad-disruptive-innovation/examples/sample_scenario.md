# Example: FlowERP vs. SAP Business One — SME ERP 市場破壞評估

## Scenario

一家私募股權公司（PE firm）正評估是否投資 FlowERP——一家 2021 年成立的台灣 SaaS 新創，提供雲端帳務與營運管理軟體，定價 TWD 2,500/月（約 USD 80）。FlowERP 目前擁有 12,000 家付費客戶，清一色是員工人數 20 人以下、年營收低於 TWD 5,000 萬的微型企業。

SAP Business One 在台灣的授權代理商對此不以為意：「FlowERP 沒有多公司合併報表、沒有進階製造模組、API 整合也很陽春。真正的企業客戶不會考慮它。」

PE firm 的問題：**FlowERP 是破壞性威脅還是利基玩家？SAP 應該擔心嗎？**

---

## Analysis

### Step 1: Map Performance Trajectories

**SAP Business One 的效能軌跡**

| 功能維度 | 2018 | 2022 | 2025 (預測) |
|---|---|---|---|
| 多公司合併 | ✓ 基本 | ✓ 完整 | ✓ AI 輔助 |
| 製造 MRP | ✓ | ✓ 進階 | ✓ IoT 整合 |
| 導入成本（TWD） | 80 萬 | 120 萬 | 150 萬 |
| 月維護費（TWD） | 8,000 | 12,000 | 15,000 |

**台灣 SME 客戶需求閾值分析**

訪談 200 家年營收 5,000 萬以下企業，結果：
- 89% 表示「只需要基本進銷存 + 電子發票 + 現金流報表」
- 只有 6% 實際使用多公司合併功能（即使他們付費擁有）
- 68% 認為 SAP B1 「功能太多，我們用不到三成」

**結論：明顯的效能過射（Performance Overshoot）**

SAP B1 持續沿著「更複雜、更整合」的軌跡升級，但 TWD 5,000 萬以下的微型企業需求早在 2020 年前就已被滿足——甚至超過。這條曲線的上方就是 FlowERP 的進入空間。

---

### Step 2: Identify the Foothold

**FlowERP 的落腳點分類：低端切入（Low-End Foothold）**

FlowERP 明確鎖定 SAP B1 的「過度服務」群：

| | SAP Business One | FlowERP |
|---|---|---|
| 目標客群 | 50–500 人企業 | <20 人微型企業 |
| 導入門檻 | TWD 80–150 萬（一次性）| TWD 0（免費試用） |
| 月費 | TWD 12,000–15,000 | TWD 2,500 |
| 上線時間 | 3–6 個月 | 當日自助開通 |
| 核心功能 | MRP、多公司、EDI | 進銷存、電子發票、Line 通知 |

FlowERP 的核心優勢不是功能更強，而是**夠用 + 極低摩擦**。微型企業老闆自己設定、自己操作，不需要 SI 顧問介入。

這不是新市場切入（非消費者），因為這些微型企業過去有在用 SAP B1 的廉價替代品（鼎新、91APP 帳務模組）。FlowERP 是從更低端切入，以更好的 UX 和雲端架構取代本地端老舊軟體。

---

### Step 3: Assess Disruption Potential

**條件一：效能過射是否存在？**

✅ **是**。SAP B1 在「台灣微型 SME」這個區間明顯過度服務。89% 的受訪者不使用付費功能中的 70%。FlowERP 的「缺陷」（無 MRP、無多公司）在這個族群根本不是缺陷。

**條件二：FlowERP 有上行遷移路徑嗎？**

✅ **是，且已在進行中。**

- 2023 Q3：推出「FlowERP Pro」，新增庫存批號追蹤（目標：20–50 人製造業）
- 2024 Q1：推出多使用者權限管理（目標：連鎖店型態）
- 2025 路線圖：簡易多公司帳務（兩個法人以內）

每一步都向上侵蝕 SAP B1 的低端客戶。每年約有 800 家 FlowERP 客戶因成長而「畢業」到需要更複雜功能——FlowERP 正在攔截這批本來會轉向 SAP B1 的客戶。

**條件三：SAP 有不對稱動機嗎？**

✅ **強烈成立。**

- SAP B1 台灣一張授權平均 ARR：TWD 144,000
- FlowERP 一個客戶平均 ARR：TWD 30,000
- 即使 SAP 開發「Lite 版」，每個 FlowERP 客戶的利潤只有現有客戶的 20%
- SAP 的代理商（SI）靠導入服務費為生，主動推低端產品等同自砍收入
- SAP 總部的資源分配優先順序：S/4HANA 雲端遷移 >> 台灣微型 SME

**SAP 為何理性地選擇不回應：** 回應意味著以 TWD 30,000 ARR 的客戶替換 TWD 144,000 ARR 的客戶，且還會惹怒現有 SI 渠道夥伴。這是教科書級的不對稱動機。

---

### Step 4: Recommend Response Strategy

**針對 SAP（現有業者）**

SAP 不太可能在內部直接回應——動機不對稱太強。但若不作為，FlowERP 的上行路徑將在 3–5 年內侵蝕 SAP B1 在台灣 50 人以下企業市場的 30–40% 份額。

建議選項（按可行性排序）：
1. **收購 FlowERP**（最可行）：以 5–8x ARR 估值（TWD 3.6–5.8 億）收購，隔離為獨立品牌運作，避免渠道衝突
2. **授權代理商推 SAP B1 Starter**：降低入門版定價至 TWD 3,500/月，但需補貼 SI，執行難度高
3. **放任不管**（目前選擇）：代價是逐步失去下一代成長型企業——這批客戶五年後會成為 SAP B1 的自然客群，但屆時已被 FlowERP 鎖住

**針對 FlowERP（破壞者）**

核心建議：**繼續潛伏，不要提前正面宣戰。**

- 繼續以「不跟 SAP 比較」的行銷語言，避免觸發 SAP 的防禦反應
- 2025 年優先補強「連鎖店多門市」功能，攻向 SAP B1 最薄弱的 20–50 人零售業
- 不急於推出 MRP——MRP 會讓 SAP 把你當競爭對手看待，且需要大量客製，違背低摩擦原則
- 建立電子發票 + 政府申報的深度整合（台灣本地護城河），讓 SAP 的外商背景成為劣勢

---

## Result

```markdown
# Disruption Assessment: ERP 市場 — FlowERP vs. SAP Business One（台灣 SME 區間）

## Performance Trajectory Analysis
- Incumbent performance vector: SAP B1 持續沿「多公司、MRP、EDI、AI 洞察」軸升級，導入成本年增 8–12%
- Customer need threshold: 年營收 <5,000 萬企業只需「進銷存 + 電子發票 + 現金流報表」，此需求在 2019 年前已被充分滿足
- Overshoot zone: 20 人以下微型企業——89% 不使用已付費功能的 70%，客戶實際付出的價值遠高於使用量

## Entrant Classification
- Type: **低端切入（Low-End Foothold）**
- Target segment: <20 人、年營收 <5,000 萬台幣的微型企業（台灣約 78 萬家）
- Core advantage: 導入零摩擦（當日開通）+ 月費為 SAP B1 的 1/5 + 台灣本地電子發票深度整合

## Disruption Potential: **HIGH**
1. Performance overshoot: ✅ 是——89% 受訪者表示 SAP B1 功能超過需求；現有功能使用率 <30%
2. Upmarket path: ✅ 是——FlowERP 每季推出功能，已開始攔截 20–50 人成長型企業；2025 路線圖覆蓋簡易多公司場景
3. Asymmetric motivation: ✅ 強——SAP B1 ARR 是 FlowERP 的 4.8x；SI 渠道利益衝突；SAP 總部資源集中在 S/4HANA 遷移

## Strategic Recommendations
- For incumbent (SAP): 收購是唯一兼顧財務回報與渠道保護的選項；若不收購，應在 2026 年前建立獨立低端品牌，否則將在台灣 SME 市場失去下一個世代的客戶
- For entrant (FlowERP): 繼續低調潛行；2025 年聚焦連鎖零售與服務業（20–50 人）；深化電子發票、健保、勞保申報整合以建立本地護城河；避免過早宣稱「取代 SAP」觸發反擊
```

**PE firm 投資建議**：FlowERP 符合 Christensen 框架的全部三個破壞條件，且已展示可重複的上行路徑。風險在於上行速度——若 FlowERP 在進入 50 人以上市場前資金耗盡，破壞過程會中斷。建議盡職調查重點放在：客戶留存率（NRR）是否超過 110%，以及「畢業客戶」（成長至 20 人以上）的流失率。
