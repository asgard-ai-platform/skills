---
name: "fin-m-and-a"
description: "M&A integration playbook covering eight modules: strategic rationale, target screening, due diligence (financial/legal/commercial), valuation with valuation bridge, synergy analysis, deal structuring (stock vs. asset, cash vs. equity, earn-out), SPA key clauses, and post-merger integration (PMI). Use for deal evaluation, valuation disputes, structure design, earn-out design, synergy breakdown, integration risk, or hostile takeover defense. Triggers: 『併購』『收購』『M&A』『盡職調查』『DD』『估值橋』『綜效』『earn-out』『換股比例』『PMI』『買殼』『借殼上市』『敵意併購』『交易結構』. For Taiwan EMBA 財管組 case studies and term reports (台大／政大／陽交). Complements Asgard `biz-dcf` and `fin-modeling` (valuation tools) plus `biz-corporate-governance` (governance layer) by providing the transaction-layer framework."
metadata:
  category: "WP-08 商學院—財務"
  tags: ["m-and-a", "mergers-acquisitions", "due-diligence", "valuation-bridge", "synergy", "earn-out", "pmi", "deal-structure", "emba"]
  audience: "台灣 EMBA 財管組學員、投行／PE 從業者、企業發展主管、創辦人／大股東"
---

# 併購交易整合 Playbook（M&A Integration Playbook）

## 定位

**為什麼 EMBA 要學 M&A Playbook**

M&A 是商學教育中最「跨領域」的主題：需要策略、財務、會計、稅務、法律、組織行為整合。多數 EMBA 學員（或其公司）在以下情境會遇到：
- 成長瓶頸需外部併購
- 被大型集團收購談判
- 投資 PE 基金後的併購決策
- 接班過程的家族股權重組
- IPO 前的策略性併購
- 國際擴張的跨境併購

**本 skill 的定位**：不是單純估值工具（DCF、可比公司法），而是**整個交易生命週期的導航**。估值只是其中一個模組。

**與相近 Asgard skill 的邊界**
- `biz-dcf` — 估值技術（DCF 建模）
- `fin-modeling` — 財務建模工具
- `biz-financial-ratios` — 比率分析
- `biz-value-chain` — 策略工具
- `biz-corporate-governance`（本 repo）— 治理結構
- **本 skill** — 併購交易的整體 playbook，協調上述工具並加入 DD、交易結構、PMI、合約層

## 何時使用

**觸發條件**
- 任何併購案從「要不要做」到「怎麼做」的決策
- 估值報告爭議調解
- 交易結構設計（含跨國）
- SPA（Share Purchase Agreement）條款談判準備
- PMI 規劃與執行
- 敵意收購防禦／公開收購應對
- EMBA 財管組個案、企業併購模擬

**不適用**
- 單純 DCF 估值 → Asgard `biz-dcf`
- 純財務建模 → Asgard `fin-modeling`
- 投資組合理論 → Asgard `grad-fama-french`
- 單一上市公司財報分析 → Asgard `data-financial-analysis`

## IRON LAW — M&A 三條鐵律

```
IRON LAW 1：70% 併購案毀滅股東價值
多個學術研究（KPMG、BCG、McKinsey 長期追蹤）顯示：
買方股東 1 年後累積異常報酬為負的比例約 60–70%。
不是「為什麼要併購」，而是「為什麼不做時勢會更好」。
沒通過這個挑戰的併購案應放棄。
```

```
IRON LAW 2：綜效（Synergy）永遠被高估
成本綜效（裁員、共採）達成率約 70%；
營收綜效（交叉銷售、整合市場）達成率 < 30%。
任何營收綜效在估值模型中都該打 0.3 係數。
「保守估計綜效」是所有併購報告的底線。
```

```
IRON LAW 3：整合（PMI）在 Day 1 之前就要規劃
60% 的併購失敗可追溯到 PMI 規劃不足。
交易結束才開始想怎麼整合 = 已經輸一半。
DD 階段必須產出初版 100-day plan，簽約前完成詳版。
```

## Rationalization Table — 當 Claude 想「本案例外」時，先自問

| 可能想 | 但 Iron Law 仍適用，因為 |
|---|---|
| 「這案子戰略合理、估值便宜，推薦進行」 | 仍要挑戰「不做時勢會不會更好」；若答案是「差不多」，傾向放棄而非推進 |
| 「承諾綜效是財務部認真估算的 X 億，應全額納入估值」 | 營收綜效達成率 < 30%，必須打 0.3 係數；成本綜效 × 0.7；財務綜效 × 0.5 |
| 「DD 完成後再規劃 PMI」 | 60% 併購失敗源於 PMI 晚；PMI 初版必須在 DD 階段就啟動、簽約前完成詳版 |

## 八大交易模組

```
┌───────────────────────────────────────┐
│ 模組 8：整合（PMI）                    │
│   100-day plan、文化融合、人才保留    │
├───────────────────────────────────────┤
│ 模組 7：合約條款（SPA）                │
│   關鍵條款、Reps & Warranties         │
├───────────────────────────────────────┤
│ 模組 6：交易結構                       │
│   股權 vs. 資產、支付工具、稅務       │
├───────────────────────────────────────┤
│ 模組 5：綜效分析                       │
│   營收／成本／稅務／財務四類          │
├───────────────────────────────────────┤
│ 模組 4：估值與估值橋                   │
│   EV-to-Equity、三種方法交叉驗證       │
├───────────────────────────────────────┤
│ 模組 3：盡職調查（DD）                 │
│   財稅／法律／商業三大類              │
├───────────────────────────────────────┤
│ 模組 2：目標篩選                       │
│   策略契合度、市場地位、可併性        │
├───────────────────────────────────────┤
│ 模組 1：戰略動機                       │
│   Why M&A vs. Organic vs. JV          │
└───────────────────────────────────────┘
```

## 模組 1：戰略動機分析

併購是成長路徑三選一（Build／Partner／Buy）；選擇 M&A 必須有明確動機（規模、範疇、市場進入、關鍵資產、垂直整合、財務套利其中之一），並通過 IRON LAW 1 的「不做時勢會不會更好」挑戰。Build／Partner／Buy 對照與六大動機詳解是商管常識，Claude 可直接調用；本 skill 聚焦下列紅旗識別。

### 動機紅旗（非顯然、最易被學員忽略）

- **純粹 CEO ego**：大老闆想成為大老闆 — 需由獨董／財顧挑戰
- **追隨潮流**：同業併購、我也要 — 需檢視自身策略獨立依據
- **隱藏問題**：核心業務衰退、靠併購掩蓋 — 需先診斷本業
- **會計操縱**：靠併購美化 EPS — 需檢視合併效果是否來自真實價值
- **估值便宜的錯覺**：賣方低估必有原因，DD 前別急著擁抱「便宜」
- **時機壓力**：董事會年度預算 / IPO 前業績要求 — 壓力下決策易跳過 IRON LAW

## 模組 2：目標篩選

### 策略契合度檢核

```
目標公司
  ↓ 初篩 (> 100 家)
產業契合、規模適配、地理可控
  ↓ 中篩 (10–20 家)
財務健康、成長性、競爭地位
  ↓ 深篩 (3–5 家)
文化相容、管理層品質、可併性
  ↓ 正式接觸 (1–2 家)
詳細分析、投資邏輯書
```

### 可併性（Acquirability）評估

- 股權結構：是否有單一控制股東？
- 管理層態度：友善或敵對？
- 法規障礙：反壟斷、外資限制？
- 勞資關係：工會強弱、退休金負債？
- 競業禁止：是否有技術出口管制？

### 進入談判前必答四問

1. 這個目標的內在價值（Standalone Value）？
2. 我們能創造的綜效價值（Synergy Value）？
3. 我們願意支付的最高價（Walk-away Price）？
4. 失敗的替代方案（BATNA）？

## 模組 3：盡職調查（Due Diligence）

DD 分三大類：**財稅 DD**（收入品質、EBITDA 正常化、營運資金、稅務暴露）、**法律 DD**（章程、重大合約、訴訟、IP、勞動、環安衛、合規）、**商業／營運 DD**（市場地位、客戶集中度、供應鏈、IT、管理團隊、文化）。DD 必須產出紅旗清單、Deal Breaker 識別、EBITDA 正常化表與 SPA 條款建議。

**最常見 Deal Breaker**：前三大客戶佔比 > 50%、重大合約含 CoC 條款、未揭露跨境稅務爭議、EBITDA 調整項失真 > 10%。

→ 完整 DD 清單（含財稅／法律／商業三大類詳細查核項目）、紅旗辨識邏輯、DD 產出文件模板：`references/dd-checklist.md`

## 模組 4：估值與估值橋

估值必須三法交叉驗證：**內在價值法**（DCF，見 Asgard `biz-dcf`）、**相對估值法**（可比公司、可比交易倍數）、**過去交易法**（目標公司過往股權交易）。任何單一方法結果都需另兩法驗證。

**估值橋（Valuation Bridge）——EMBA 最常考題**：
```
Standalone Value（獨立經營價值）
  + 控制權溢價（Control Premium, 20–40%）
  + 綜效分享（買方通常拿多數）
  − DD 調整（瑕疵折減）
  − 營運資金／退休金／訴訟／稅務調整
  = Transaction Value（交易對價）
```

**致命陷阱**：Terminal Value > 80% EV（幻覺）、Control Premium 重複計算（已在可比交易倍數中）、綜效全算給買方（賣方必爭）。

→ 三法交叉驗證詳解、EV-to-Equity 完整橋、WACC 計算、Terminal Value 警訊、控制權溢價處理：`references/valuation-bridge.md`

## 模組 5：綜效分析

四類綜效的達成率差異極大，估值時**必須**按類別打係數：
- **成本綜效**（人員／採購／製造／IT 整合）：達成率 60–70%
- **營收綜效**（交叉銷售、新市場、定價力）：達成率 **< 30%**，估值折現要重
- **稅務綜效**（NOL 抵減、Interest Tax Shield）：需專業稅顧確認
- **財務綜效**（WACC 降低、多元化）：學術爭議，市場常打折

**EMBA 報告通用底線**：公開承諾綜效達成率約 55–70%，估值時先估毛綜效再乘 0.6–0.7 係數。成本綜效 6–18 月實現，營收綜效 24–60 月才到位。

→ 四類綜效拆解、實現率係數、時程表、Implementation Cost 估算、綜效追蹤儀表板：`references/synergy-analysis.md`

## 模組 6：交易結構設計

### 股權交易 vs. 資產交易

| 維度 | 股權 Stock Purchase | 資產 Asset Purchase |
|---|---|---|
| 法律主體 | 買下整家公司 | 買下特定資產 |
| 既有負債 | 全部承繼 | 選擇性承繼 |
| 既有合約 | 自動承繼（含重大不利條款） | 需重新簽訂或 assignment |
| 稅務 | 目標公司成本基礎不變 | 可重新估價、折舊攤提 |
| 結構複雜度 | 低 | 高（資產清單） |
| 員工 | 自動轉移 | 需重新聘僱 |
| 適用 | 完整業務收購 | 特定資產、出清部門 |

### 支付工具組合

**現金（Cash）**
- 賣方確定性高
- 買方現金壓力
- 稅務：賣方即課稅

**換股（Stock）**
- 賣方共擔風險
- 買方免動現金
- 稅務：部分可遞延
- 股價波動風險

**混合（Cash + Stock）**
- 最常見
- 比例依雙方議價而定

**遞延工具**
- 賣方票據（Seller's Note）
- Earn-out（參考下節）
- 盈餘保留（Escrow / Holdback）

### Earn-out 設計

**定義**：部分對價繫於目標公司未來績效

**結構要素**
- 期間（通常 2–3 年）
- 指標（EBITDA、Revenue、Milestone）
- 計算公式與門檻
- 上限（Cap）與下限（Floor）
- 爭議解決機制

**Earn-out 陷阱**
- 會計操縱（賣方追短期）
- 整合衝突（賣方希望獨立運作）
- 指標失真（綜效如何分攤）
- 訴訟高發（40% earn-out 有爭議）

**適用情境**
- 買賣雙方估值差距大
- 關鍵創辦人需留任
- 新事業或新產品估值不確定

### 稅務結構（台灣常見）

**併購法相關**
- 併購法（2002 年，多次修訂）提供稅務優惠
- 合併、收購、分割可享股東課稅遞延
- 虧損抵減限制
- 需配合經濟部核准

**跨境併購**
- 台灣控股公司 vs. 境外控股
- 稅務條約運用
- 資金路徑設計
- 需配合會計師跨境架構

## 模組 7：合約關鍵條款（SPA）

SPA 九大核心章節：**標的定義、對價、交割條件（Conditions Precedent）、陳述與保證（R&W）、特別保證、賠償機制、競業禁止、爭議解決、終止條款**。

**賠償機制三要素**（談判重心）：
- **Basket（門檻）**：Tipping vs. Deductible
- **Cap（上限）**：一般 R&W 10–25%，稅務／環安衛可能無上限
- **Survival Period（時效）**：一般 R&W 18–24 月、稅務依法定時效、基本 R&W 永久

**近年趨勢**：R&W Insurance 已是大型交易標配，保費約交易金額 2–4%，能大幅降低買賣雙方摩擦。

→ SPA 各章節樣本條款、R&W 類別與樣本語言、Working Capital 調整、Basket／Cap／Survival 設計、R&W Insurance：`references/spa-key-clauses.md`

## 模組 8：整合（PMI, Post-Merger Integration）

PMI 以 **Day 1 / Day 100 / Day 365** 為節奏：Day 1 聚焦關鍵溝通與組織架構生效；Day 100 完成組織整合、Key People 保留、第一波成本綜效；Day 365 綜效達成率檢討與文化融合。**IRON LAW 3** 要求 DD 階段就啟動 100-day plan 初版，簽約前完成詳版。

**PMI 七大支柱**：治理（IMO）、組織設計、人才保留、文化融合、流程與系統、客戶與品牌、綜效追蹤。

**最常見失敗模式**：文化忽視、Key People 12 月內流失 > 30%、整合速度失調（過快破壞價值、過慢綜效落空）、IMO 無決策權變協調會議。

→ Day 1 / Day 30 / Day 100 / Day 365 完整行動清單、IMO 組織設計、七大支柱各自 playbook、文化融合方法：`references/pmi-playbook.md`

## Output Format

```markdown
# M&A 交易分析：{案件名稱／買方 vs. 賣方}

## 一、戰略動機
- Why M&A（相對於 Build / JV）
- 六大動機對應
- 動機紅旗檢核

## 二、目標評估
- 策略契合度
- 可併性（Acquirability）
- 四個關鍵問題回答

## 三、DD 發現
- 財稅發現（紅旗與調整）
- 法律發現
- 商業／營運發現
- Deal Breaker 識別

## 四、估值分析
- 三種方法交叉驗證
- EV to Equity 橋
- Valuation Bridge（Standalone → Transaction）
- 敏感度分析

## 五、綜效拆解
- 四類綜效各估算（保守、基本、樂觀）
- 實現率與時程
- 實施成本

## 六、交易結構建議
- 股權 vs. 資產
- 支付工具組合
- Earn-out（若適用）
- 稅務考量

## 七、SPA 關鍵條款
- R&W 重點
- 賠償機制（Basket / Cap / Survival）
- 特別保證
- 競業禁止

## 八、PMI 規劃
- Day 1 / Day 100 / 365 重點
- 關鍵人才
- 文化融合
- 綜效追蹤儀表板

## 九、風險與限制
- 執行風險
- 整合風險
- 法遵風險
- 分析資料侷限
```

## Examples

### 正確應用
**情境**：台灣上市電子公司（買方）擬併購一家東南亞製造廠（賣方，家族經營、年營收 30 億）。

**分析**：
- 戰略：規模 + 地理擴張（避開中國關稅），Organic 時間成本 3–5 年
- 目標評估：賣方家族願意退場，但要求部分留任，可併性高
- DD 紅旗：EBITDA 正常化後下修 15%、環安衛有潛在爭議、主要客戶合約含 CoC 條款
- 估值：EV/EBITDA 法（8x 調整後 EBITDA）、DCF（WACC 10.5%、TV 70% 偏高警示）、中值 NT$ 24 億
- 綜效：成本綜效 2 億／年（15–24 月實現）、營收綜效打 0.3 係數僅 0.3 億／年
- 交易結構：80% 現金 + 20% 換股、Earn-out 2 年（EBITDA 達標）、保留創辦人 3 年
- SPA：R&W 標準包、環安衛特別保證、Cap 交易金額 15%、R&W 保險配套
- PMI：Day 1 保留賣方 CEO、Day 100 整合採購與財務、文化並行 24 個月不強制同化

**正確之處**：八大模組完整、綜效保守、PMI 有時程，符合 IRON LAW。

### 錯誤應用
- 只做 DCF 估值報告 → 只用一種方法，忽略相對估值與交易法
- 把承諾綜效 100% 放入估值 → 違反 IRON LAW 2
- 忽略 PMI 規劃 → 違反 IRON LAW 3
- 交易結構「全現金」不考量稅務 → 賣方稅負可能殺死交易
- R&W 陽春（無特別保證）→ DD 發現未在合約反映
- Earn-out 指標設為「淨利」→ 易被會計操縱爭議

## Gotchas

- **估值中位數不等於交易價**：中位數只是參考，競購壓力會推高，DD 發現會壓低，買方應預設 walk-away price
- **綜效對外公開需謹慎**：上市買方對外承諾的綜效金額將被市場追蹤，保守 + 附條件說明
- **台灣併購法優惠需配合主管機關**：經濟部、公平會、金管會的審查時程可能 3–6 個月，影響交易時程
- **跨境併購的外匯管制**：台灣對外投資金額有報備／核准門檻，中國投資有經濟部投審會規範
- **Earn-out 爭議率高**：約 40% 有爭議，合約條款需極明確、會計方法需預先約定
- **Key Man 條款雙面刃**：綁定創辦人留任可能形成人質條款，若創辦人不快樂，整合會失敗
- **PMI 文化融合沒有捷徑**：強制快速同化 = 人才流失、慢條斯理 = 綜效落空，必須雙軌並行
- **敵意收購的政治成本**：台灣市場對敵意收購接受度低，需考量政府、媒體、員工、客戶多方反應

## References

- 三大 DD 完整清單與紅旗辨識 → `references/dd-checklist.md`
- 估值橋詳解與交叉驗證 → `references/valuation-bridge.md`
- 綜效拆解與實現時程 → `references/synergy-analysis.md`
- SPA 條款模板（R&W、Indemnification、Earn-out）→ `references/spa-key-clauses.md`
- PMI 100-day plan 模板 → `references/pmi-playbook.md`
- 台灣併購法規與稅務框架 → `references/tw-ma-regulation.md`
- EMBA 併購課程脈絡與學術誠信提醒 → `references/emba-ma-courses.md`
- 延伸：Asgard `biz-dcf`（DCF 估值）、`fin-modeling`（財務建模）、`biz-financial-ratios`、`grad-fama-french`（CAPM 延伸）、`law-contract`（合約法）、本 repo `biz-corporate-governance`（治理）、`biz-sme-management`（家族企業）
