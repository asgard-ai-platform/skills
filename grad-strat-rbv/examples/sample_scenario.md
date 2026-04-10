`grad-strat-rbv/examples/sample_scenario.md` 尚不存在，直接建立：

```markdown
# Example: 台灣 SaaS 公司評估 AI 自動化定價引擎的競爭優勢

## Scenario

**用戶問題（2026 年 1 月）：**

> 我們是一家台灣的 B2B SaaS 公司（化名 Vega Analytics），提供供應鏈可視化平台，主要客戶是台灣與東南亞的中大型製造商。最近 VC 問我們：「你們的競爭優勢可以撐多久？中國對手兩年後會不會追上？」我們的核心差異化是一套 AI 自動化定價引擎，整合了我們過去六年在台灣製造業累積的 12,000 家供應商交易資料。我需要一個有理論依據的答案。

**已知背景資訊：**

- 成立：2019 年，台北
- 員工：180 人，其中 40 位 ML 工程師
- ARR：USD 8.2M（2025 年底），YoY 成長 64%
- 主要資源：AI 定價引擎、供應商交易資料庫、客戶成功團隊、台灣製造業人脈網絡
- 競爭者：中國 SaaS 對手（Chainova、LogiSense）、國際玩家（SAP Ariba、Coupa）

---

## Analysis

### Step 1：資源盤點

先將 Vega Analytics 的資源分為三類：

| # | 資源 | 類型 |
|---|------|------|
| R1 | AI 自動化定價引擎（模型 + 演算法） | 無形資源 |
| R2 | 12,000 家供應商六年交易資料庫 | 無形資源 |
| R3 | 40 人 ML 工程師團隊（平均 4.2 年在職） | 人力資本 |
| R4 | 台灣製造業高層人脈（C-suite 關係） | 無形資源 |
| R5 | 客戶成功流程（實施方法論） | 無形資源 |
| R6 | 品牌與 ISO 27001 資安認證 | 無形資源 |

---

### Step 2：VRIO 逐一檢驗

#### R1 — AI 定價引擎

- **Value (V)：YES** — 客戶平均採購成本下降 11%，直接中和「不確定原物料波動」的威脅。EBITDA 影響可量化。
- **Rarity (R)：YES** — SAP Ariba 有通用定價模組，但針對台灣製造業供應鏈的本地化演算法，目前僅 Vega 具備。Chainova 的版本針對中國內需市場校準，在台精度差。
- **Imitability (I)：PARTIAL** — 演算法本身可被反向工程（18–24 個月），但引擎的準確度依賴 R2（資料）。若無 R2，複製引擎價值大幅縮水。**單獨為 Temporary Advantage；與 R2 結合則升為 I=YES（資料護城河 + 因果模糊性）。**
- **Organization (O)：YES** — 有 ML Ops 團隊維護模型漂移，有 A/B 測試流程，有 CPO 主導 roadmap。

**結論：V+R+I（因 R2 互補）+O → 持續性競爭優勢**

---

#### R2 — 12,000 家供應商交易資料庫

- **V：YES** — 唯有足夠的歷史交易量，定價模型才能處理台灣特有的「多層次轉包」結構（三角貿易、VMI 模式）。
- **R：YES** — Chainova 進台灣市場不足三年，資料量估計不超過 2,000 家；SAP 的資料分散在全球節點，台灣本地化不足。
- **I：YES** — 典型路徑依賴（unique historical conditions）：六年持續授權協議換取資料訪問權；社會複雜性（客戶信任 Vega 才願意共享敏感交易資料）；新進者若從零開始需 4–5 年才能達到同等體量。
- **O：YES** — 有資料治理委員會、客戶資料共享 NDA 框架、即時資料管道（Kafka + dbt）。

**結論：V+R+I+O → 持續性競爭優勢（最強護城河）**

---

#### R3 — ML 工程師團隊

- **V：YES** — 高留存率（年離職率 8%，業界平均 22%）確保模型迭代速度。
- **R：PARTIAL** — 台灣 ML 人才市場競爭激烈（TSMC、MediaTek 也在搶），Vega 非唯一雇主。
- **I：NO** — 工程師可被挖角；薪資 + 股票可複製。
- **O：YES** — 技術棧文件完整、知識轉移流程成熟。

**結論：V+Partial R+N+O → Competitive Parity（可能升為 Temporary Advantage 若強化 R）**

---

#### R4 — 台灣製造業高層人脈

- **V：YES** — 高管引薦縮短銷售週期（平均 94 天 vs 業界 160 天），有助於進入封閉型採購決策圈。
- **R：YES** — 六年田野累積，非金錢可直接購買。
- **I：YES** — 社會複雜性（關係需時間建立信任，新進者難以在短期複製）；Chainova 為外資背景，在台灣本地高管圈信任度低。
- **O：PARTIAL** — 人脈高度集中在共同創辦人身上（2 位），若離職有斷鏈風險；尚未系統化移轉至業務團隊 CRM。

**結論：V+R+I+Partial O → Unrealized Advantage（組織支撐不足）**

---

#### R5 — 客戶成功方法論

- **V：YES** — 平均實施週期 6 週（業界 14 週），降低客戶切換成本。
- **R：NO** — 方法論文件可被分析師報告或客戶口述間接重建。
- **I：NO**
- **O：YES**

**結論：V+N+N+O → Competitive Parity**

---

#### R6 — 品牌 + ISO 27001

- **V：YES** — 對製造業客戶（多為上市公司）的合規要求有直接加分。
- **R：NO** — ISO 27001 為可取得認證；品牌知名度在 SME 以外尚未建立。
- **I：NO**
- **O：YES**

**結論：V+N+N+O → Competitive Parity**

---

### Step 3：資源分類彙總

| 資源 | V | R | I | O | 競爭涵義 |
|------|---|---|---|---|---------|
| R2 供應商交易資料庫 | Y | Y | Y | Y | **持續性競爭優勢** |
| R1 AI 定價引擎（與 R2 結合） | Y | Y | Y | Y | **持續性競爭優勢** |
| R4 高層人脈 | Y | Y | Y | Partial | **未實現優勢**（組織缺口） |
| R3 ML 工程師團隊 | Y | Partial | N | Y | Competitive Parity（趨向 Temporary） |
| R5 客戶成功方法論 | Y | N | N | Y | Competitive Parity |
| R6 品牌 + 認證 | Y | N | N | Y | Competitive Parity |

---

## Result

## RBV / VRIO Analysis: Vega Analytics — AI 定價引擎競爭優勢評估

### Resource Inventory

| Resource | Type | V | R | I | O | Implication |
|----------|------|---|---|---|---|-------------|
| 供應商交易資料庫（12K 家，6 年） | Intangible | Y | Y | Y | Y | Sustained Advantage |
| AI 自動化定價引擎（依托 R2） | Intangible | Y | Y | Y | Y | Sustained Advantage |
| 台灣製造業高層人脈 | Intangible | Y | Y | Y | Partial | Unrealized Advantage |
| ML 工程師團隊 | Human Capital | Y | Partial | N | Y | Competitive Parity |
| 客戶成功方法論 | Intangible | Y | N | N | Y | Competitive Parity |
| 品牌 + ISO 27001 | Intangible | Y | N | N | Y | Competitive Parity |

### Key Findings

- **持續性優勢資源（2 個）：** 資料庫（R2）與 AI 引擎（R1）形成互補護城河。R2 的路徑依賴性（6 年授權協議 + 社會信任）是最難被中國對手複製的機制。Chainova 若 2026 年進場，估計需 4–5 年才能達到同等資料體量，且台灣客戶信任壁壘難以用資本加速突破。
- **未實現優勢（1 個）：** 高層人脈（R4）具備全部三項 VRI 條件，但 O 不足——關係集中在共同創辦人，未系統化進入 CRM 與業務傳承流程。一旦創辦人離開，優勢大幅縮水。
- **同等資源（3 個）：** ML 人才、方法論、品牌雖創造價值，但競爭對手可複製，不構成差異化護城河。

### Strategic Recommendations

1. **保護並加深 R1+R2 護城河**：優先擴大資料授權協議簽約數（目標 2027 年達 20,000 家供應商），強化因果模糊性。考慮申請演算法專利（雖不完美，但增加訴訟成本作為嚇阻）。
2. **修復 R4 的 O 缺口**：啟動「人脈制度化」專案——將創辦人關係系統性轉移至 CRM，指派客戶關係副理接棒，12 個月內完成 Top 50 客戶的關係交接，將 R4 從「未實現優勢」升格為「持續性優勢」。
3. **對 VC 的直接答覆**：中國對手（Chainova）在資料與信任兩個維度均存在結構性落差，非資本密集可快速弭平。兩年內被追上的風險低，但前提是 Vega 必須持續加深 R2 的資料護城河，並修補 R4 的組織漏洞。
```
