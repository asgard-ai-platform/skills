---
name: "ops-digital-transformation"
description: "Digital-transformation execution playbook: maturity assessment, transformation roadmap, Operating Model redesign, PMO and transformation governance, data/AI platform deployment, process digitization, organizational agility, digital talent, and change management. Use for DX roadmap design, transformation governance (CDO/PMO/Steering Committee), data/AI/cloud platform planning, ERP or core-system upgrade, traditional-industry digitization, or DX organizational resistance. Triggers: 『DX 從哪開始』『數位長』『資料平台』『AI 落地』『傳產數位化』『ERP 要不要換』『轉型辦公室』『員工不配合數位化』『Operating Model』『敏捷轉型』『PMO』. For Taiwan EMBA info-management/DX/strategy/operations/change courses. Focuses on execution; theory layer: use Asgard `grad-digital-transformation`, `grad-sociotechnical`, `grad-tam-utaut`."
metadata:
  category: "WP-09 商學院—管理"
  tags: ["digital-transformation", "dx", "operating-model", "data-platform", "ai-deployment", "pmo", "change-management", "emba"]
  audience: "台灣 EMBA 在職學員、CEO、CDO、CIO、事業主管"
---

# 數位轉型執行工具箱（Digital Transformation Playbook）

## 定位

「數位轉型」在企業中最常見的失敗模式：
- **做了很多專案、沒有轉型**
- **買了很多系統、員工不用**
- **喊了三年口號、數字沒動**
- **成立 DX 辦公室、事業部不甩**

本 skill 的核心主張：**DX 是「營運模式重設」（Operating Model Reset），不是「IT 系統升級」**。

### 三個常見誤解澄清
- **不是**：把既有流程電子化（那是數位化，Digitization）
- **不是**：上雲、導 AI、換 ERP（那是技術專案）
- **是**：用數位能力重塑商業邏輯、組織結構、人才、客戶體驗的一體性變革

**與相近 Asgard skill 的邊界**：
- `grad-digital-transformation` — DX 學理（定義、類型、成熟度研究）
- `grad-sociotechnical` — 社會技術系統理論
- `grad-tam-utaut` — 科技接受模型（個人層）
- `data-*` skills — 資料分析工具
- **本 skill** — DX 的**執行治理與營運模式設計**

## 何時使用

**觸發條件**
- 執行長委託 DX 藍圖設計
- 成熟度評估與標竿對照
- 轉型辦公室（DX Office / PMO）組建
- 資料平台 / AI 平台規劃
- 核心系統（ERP、CRM、MES、HRIS）升級決策
- 傳統產業的數位化轉型
- 客戶體驗數位化
- DX 組織阻抗的診斷
- EMBA 資管、營運、策略、組織變革課程個案

**不適用**
- 單一 IT 專案規劃 → 需特定技術文件
- AI 模型設計 → 需技術團隊
- DX 學理文獻 review → Asgard `grad-digital-transformation`
- 資料分析方法 → Asgard `data-*` skills
- 創新新事業 → 本 repo `biz-innovation-management`

## IRON LAW — 數位轉型的三條鐵律

```
IRON LAW 1：DX 是營運模式，不是技術專案
買系統、導工具 = Digitization，不是 Transformation。
真正的 DX 改變：
（1）價值主張（你賣什麼、怎麼賣、誰買）
（2）營運模式（流程、組織、能力）
（3）收入模式（訂閱、平台、數據）
沒改變以上三者的「DX」是花錢裝潢。
```

```
IRON LAW 2：CEO 不親自帶 = DX 必死
DX 涉及跨部門整合、資源重分配、文化變革、短期 EPS 犧牲。
這些決定只有 CEO 能做。
把 DX 交給 CIO / CDO 獨立推動 =
「給一個人一把掃把、要他清空一座山」。
CEO 至少每月親自主持一次 DX 指導委員會。
```

```
IRON LAW 3：成熟度不能跳級
L1（手工） → L2（流程數位化） → L3（資料驅動）
→ L4（智慧決策） → L5（生態平台）
跳級常見錯誤：L1 企業直接買 AI 平台
→ 無資料基礎、使用率 < 10%、2 年後被砍。
應先做地基（L2 流程數位化 + 資料治理），再上智慧層。
```

## Rationalization Table — 當 Claude 想「本案例外」時，先自問

| 可能想 | 但 Iron Law 仍適用，因為 |
|---|---|
| 「公司剛導完 ERP，這算 DX 完成了」 | 導 ERP = Digitization，不是 Transformation；須評估商業模式、組織、文化是否同步改變 |
| 「CEO 授權 CDO 全權處理，自己專注本業」 | DX 涉及跨部門資源搶食、短期 EPS 犧牲，只有 CEO 能拍板；報告須標註「CEO 未親帶為重大風險」 |
| 「公司資金充裕，直接跳到 AI／L4」 | 無 L2–L3 資料基礎，L4 智慧決策建在沙上；建議「先補基礎階段」或明示高失敗率 |

## DX 的核心框架：六大支柱

```
┌─────────────────────────────────────────────┐
│ 支柱 1：策略與價值主張                         │
│   為誰創造什麼價值？如何獲利？                  │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ 支柱 2：客戶體驗（CX）                         │
│   接觸點、旅程、個人化、全通路                  │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ 支柱 3：營運流程                              │
│   核心流程的數位化、自動化、智慧化              │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ 支柱 4：資料與 AI                             │
│   資料治理、分析能力、AI 落地                  │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ 支柱 5：技術架構                              │
│   雲端、API、微服務、資安、資料平台             │
└─────────────────────────────────────────────┘
┌─────────────────────────────────────────────┐
│ 支柱 6：組織與人才                            │
│   敏捷組織、數位人才、文化、領導               │
└─────────────────────────────────────────────┘
```

## DX 成熟度模型

### 五級成熟度

| 等級 | 特徵 | 典型工具 |
|---|---|---|
| L1：手工 | 紙本、Excel、無系統 | 無 |
| L2：流程數位化 | 核心流程已有 IT 系統（ERP、CRM） | ERP、CRM、HRIS |
| L3：資料驅動 | 資料整合、BI 儀表板、資料驅動決策 | Data Warehouse、BI 工具 |
| L4：智慧決策 | AI / ML 模型嵌入決策、自動化 | ML 平台、RPA、個人化 |
| L5：生態平台 | API 開放、平台化、生態系經營 | Open API、平台經濟 |

### 各支柱獨立評估

**實務上**，各支柱可能在不同等級：
- 一家零售企業可能：**CX L3**（全通路）、**流程 L2**（ERP 到位）、**資料 L2**（數據孤島）、**技術 L2**（老舊架構）、**組織 L1**（傳統科層）

### 成熟度診斷工具

**支柱 × 等級**雙軸圖：
- 現況（Current）：實線
- 目標（Target）：虛線
- 差距識別：最需要補強的支柱

## DX 藍圖設計方法

### Step 1：Why（為何要 DX）

**策略動因**
- 市場被顛覆（新創、電商、平台）
- 客戶需求變化（數位原生世代）
- 成本結構不可持續
- 人才招募困難（留不住年輕人）
- 監管 / 合規升級
- 永續 / ESG 要求

**不可接受的 Why**
- 「大家都在做 DX」
- 「董事長參觀了某家公司」
- 「顧問說我們要做」

### Step 2：What（轉型方向）

**典型 DX 類型**
1. **流程效率型**：自動化、降成本
2. **客戶體驗型**：全通路、個人化
3. **新商業模式型**：訂閱、平台、數據產品
4. **產業重塑型**：價值鏈重組

多數企業是**組合型**，但需明確主軸。

### Step 3：How（執行路徑）

**三階段典型路徑**

**Phase 1（0–12 個月）：基礎建設**
- 核心系統升級 / 到位（ERP、CRM）
- 資料治理啟動（資料目錄、品質、安全）
- 雲端遷移部分（混合雲）
- 轉型辦公室成立

**Phase 2（12–30 個月）：流程與體驗**
- 核心流程數位化 / 自動化
- 客戶旅程重設計
- 資料平台整合
- AI 應用試點

**Phase 3（30–60 個月）：智慧化與平台化**
- AI 嵌入核心決策
- 新商業模式試行
- API 開放、生態合作
- 組織全面敏捷

## DX 治理結構

### 三層治理

**Steering Committee（指導委員會，董事會 / CEO 層級）**
- CEO 主席
- 獨立董事、CFO、COO、CDO / CIO
- 季度會議
- 決議：策略、大額投資、資源重配置

**Digital Transformation Office（DX 辦公室 / PMO）**
- CDO / 轉型長主持
- 跨部門專案經理
- 月度會議
- 決議：專案進度、跨部門協調、問題升級

**事業部 / 職能 DX 小組**
- 各事業部 DX 大使
- 雙週 / 月度會議
- 落地執行

### 新設職位

**CDO（Chief Digital Officer）**
- 外部或內部招聘
- 具業務 + 技術綜合背景
- 直屬 CEO
- 有預算權、有人事權

**CDA（Chief Data Analytics / Chief Data Officer）**
- 資料治理
- AI 應用
- 獨立或兼於 CDO 之下

**CIO / CTO**
- 技術架構
- 基礎設施

### 常見治理失靈

- **CDO 是 CIO 的換包裝**：仍只做 IT 採購、無業務轉型
- **PMO 無權力**：只追進度、無決策權
- **Steering Committee 淪為報告會**：CEO 缺席、決議被推翻

## 營運模式（Operating Model）重構

DX 不是單純技術專案，真正的轉型必須同時重構營運模式的六大維度：**組織架構、人才、流程、資料、技術、文化與管理方式**。敏捷組織（Spotify 模型：Squad / Tribe / Chapter / Guild）適合數位團隊但不適合製造產線；台灣企業常見錯誤是直接照搬，建議「**部分敏捷**」：核心數位團隊採敏捷、其他維持傳統。

→ 完整六大維度、敏捷組織結構、切換前提、常見誤用：`references/operating-model.md`

## 資料與 AI 落地

### 資料成熟度路徑

**Phase 1：資料盤點**
- 資料目錄（Data Catalog）
- 資料擁有者（Data Owner）指派
- 資料品質評估

**Phase 2：資料平台**
- Data Warehouse / Data Lake
- ETL / ELT 流程
- 資料安全與隱私

**Phase 3：資料產品化**
- 標準化資料 API
- 自助分析工具
- 跨部門資料共享

**Phase 4：AI 應用**
- 預測模型
- 個人化推薦
- 自動化決策

### AI 落地與治理

**5 大陷阱**：技術先行、資料不足／不乾淨、Pilot 陷阱（試點成功但放大失敗）、組織阻抗、ROI 難證明。**治理要素**：AI 倫理委員會、偏誤審查（Bias Audit）、可解釋性（Explainability）、資料隱私（個資法）、AI 決策責任歸屬。

→ 完整陷阱破解、AI 治理機制、成熟度 vs. 風險配比：`references/data-ai-enablement.md`

## 核心系統升級決策

### ERP 升級的「沉沒成本陷阱」

**症狀**：
- 現有 ERP 用了 15 年、客製化嚴重
- 升級需 30–50 億、3–5 年
- 風險：升級期間業務受影響
- 延遲：年年討論、年年不升級

**決策架構**：
- **維持**：系統仍可用、業務穩定、變革風險高
- **升級同款**：新版本、降低風險
- **換系統**：重新檢視業務流程、更大變革

**建議**：
- 5–7 年週期評估
- 避免「客製化過深」鎖死
- 新系統導入時「業務流程重設計」先於系統配置

### Legacy 系統處置

**Strangler Fig 模式**
- 新功能在新系統、舊功能漸進搬遷
- 避免「big bang」切換風險

**API Wrapper**
- 舊系統包一層 API
- 新功能呼叫 API、不直接碰舊系統

**漸進退役（Sunset）**
- 設定時間表、分批關閉

## 客戶體驗（CX）數位化

### 客戶旅程重設計

**典型步驟**
1. **Awareness**（認知）
2. **Consideration**（考慮）
3. **Purchase**（購買）
4. **Onboarding**（入門）
5. **Service**（服務）
6. **Loyalty**（忠誠）

**每一階段的數位接觸點**：
- 網站 / App / Social Media
- 聊天機器人
- 會員平台
- 客服系統
- 社群 / 論壇

### 全通路（Omnichannel）vs. 多通路（Multichannel）

- **多通路**：各通路獨立（網、店、App 無連動）
- **全通路**：客戶體驗連貫（線上結帳、店取、App 退貨）

### CDP（Customer Data Platform）
- 整合客戶資料（360 度視圖）
- 個人化推薦
- 行銷自動化

## 變革管理（Change Management）

Kotter 八步 + ADKAR 個人變革模型為主流框架。台灣企業 DX 阻抗常見於：**既得利益者、中階主管、資深員工、客戶**四類。處理工具：Champion 制度、Quick Wins、反對者納入設計階段、不配合後果顯性化。

→ 完整 Kotter 八步、ADKAR、阻抗源診斷與處理工具：`references/agile-change.md`

## DX KPI

五層 KPI 架構：**策略層**（數位收入占比、新商模營收、LTV、市佔率）、**營運層**（自動化率、訂單處理時間、NPS）、**技術層**（SLA、資料品質、AI 準確率、資安事件）、**組織層**（數位人才比例、員工素養、敏捷團隊佔比）、**轉型治理層**（on-time/on-budget、CEO 出席率）。五層必須平衡，每層 3–5 個指標為佳。

→ 完整 KPI 清單、設計原則、與成熟度對齊：`references/dx-maturity.md`

## 台灣企業 DX 特殊挑戰

五大結構性挑戰：**代工文化下的客戶驅動、家族企業的 DX 決策、中小企業資源有限、勞動力結構、資訊安全意識**。每項挑戰均有對應的破解策略（客戶共創升級、二代獨立新事業、SaaS 優先 + 政府補助、分層訓練、資安納入治理）。

→ 完整挑戰分析與破解方案：`references/tw-dx-context.md`

## 分析流程

> 根據個案性質跳過不適用步驟；以下為完整候選路徑，非必跑清單。

```
Step 1：Why 診斷
  - 策略動因
  - 外部威脅
  - 內部需求
  - 不可接受的 Why 篩掉

Step 2：成熟度盤點
  - 六大支柱現況
  - 與標竿對照
  - gap 分析

Step 3：What 定義
  - 主軸（效率、體驗、新模式、重塑）
  - 3 年目標
  - 成功指標

Step 4：How 藍圖
  - Phase 1（基礎）、2（流程）、3（智慧）
  - 各支柱具體行動
  - 里程碑

Step 5：治理設計
  - Steering Committee
  - DX 辦公室
  - 新職位（CDO 等）
  - KPI 與 PMO

Step 6：組織與人才
  - 營運模式重構
  - 人才招募與再培訓
  - 文化變革

Step 7：投資與財務
  - CAPEX / OPEX
  - 3 年回報預估
  - 風險資本

Step 8：風險與限制
  - 執行風險
  - 組織阻抗
  - 技術不確定性
```

## Output Format

```markdown
# 數位轉型藍圖：{公司／個案}

## 一、轉型動因（Why）
- 策略動因
- 外部威脅 / 內部需求
- 不做的代價

## 二、成熟度盤點
### 六大支柱現況
| 支柱 | 現況等級 | 目標等級 | gap |
### 標竿對照

## 三、轉型主軸（What）
- 主軸類型
- 3 年目標
- 成功指標

## 四、轉型藍圖（How）
### Phase 1（0–12 個月）
### Phase 2（12–30 個月）
### Phase 3（30–60 個月）

## 五、治理設計
- Steering Committee
- DX 辦公室
- 新設職位
- KPI 與 PMO

## 六、營運模式重構
- 組織
- 流程
- 人才
- 資料與技術
- 文化

## 七、財務影響
- 投資需求
- 3–5 年 ROI 預估
- 風險資本

## 八、風險與限制
- 執行風險
- 組織阻抗
- 技術不確定性
- 關鍵假設
```

## Examples

### 正確應用
**情境**：台灣中型零售連鎖（食品、年營收 35 億、門市 180 家）面臨純線上零售與大型平台夾擊，2024–2025 營收衰退 5%。

**診斷**：
- 成熟度：CX L2（App 有但使用率低）、流程 L2（POS、ERP 到位但無數據整合）、資料 L1（數據孤島）、技術 L2（地端系統）、組織 L1（傳統科層）、策略 L1（無清楚數位戰略）
- Why：被大型平台蠶食年輕客群、會員活躍度下滑
- 主軸：客戶體驗型 + 新模式（會員經濟、B2B 採購平台）

**藍圖**：
- Phase 1：ERP/CRM 升級、資料平台啟動、CDO 招募
- Phase 2：全通路 CX（App 重設計、店取、訂閱）、會員分層、AI 個人化
- Phase 3：B2B 平台（小型餐飲 / 辦公室）、資料產品（廠商洞察）
- 治理：CEO 主持季度 Steering、DX 辦公室 12 人
- 投資：3 年 12 億（系統 5 億 + 人才 3 億 + 行銷 4 億）
- ROI：第 3 年起由數位營收（10% → 25%）補回衰退

### 錯誤應用
- 「導 AI 解決問題」→ 沒定義問題、沒資料基礎
- 「上雲端」當終極目標 → 雲是手段不是目的
- 把 DX 交給 CIO 獨立推 → CEO 缺席、必敗
- 企業 L1 就做 L4（AI 決策）→ 跳級、失敗

## Gotchas

- **「Digitization vs. Digitalization vs. Transformation」混淆**：
  - Digitization = 紙本變電子（L1→L2）
  - Digitalization = 流程數位化（L2→L3）
  - Transformation = 商業模式與營運模式改變（L3 以上）
  - 很多「DX 專案」其實只是 Digitization
- **CIO 升 CDO 的「換包裝」陷阱**：若 CDO 仍只做 IT 採購、沒有業務整合權力，轉型失敗必然
- **大爆炸（Big Bang）式系統切換的災難**：ERP 一次切換常造成業務中斷。修正：Strangler Fig 漸進
- **資料治理的「重要但不急」迷思**：資料治理耗時不討喜、但沒做完 AI 都是空談。CEO 需親自拍板推進
- **人才戰略的「挖角 vs. 培養」**：只挖角不培養 → 舊員工反感；只培養不挖角 → 速度不夠。需雙軌並行
- **敏捷的「紙上敏捷」陷阱**：換說法、開 standup 會議、用 Jira → 不是敏捷。真敏捷需授權、減層級、失敗容忍
- **DX 與 ESG 的整合機會**：IoT 能源管理、供應鏈碳追蹤、AI 減碳路徑 → 把 DX 與 ESG 一起規劃，資源與治理共享
- **「參觀某公司後的 DX 狂熱」**：董事長 / CEO 參訪矽谷 / 日本後要求立刻模仿。需 CDO 結構化消化、不照抄

## References

- DX 成熟度模型、營運模式重構 → 見 `references/dx-maturity.md`
- 資料與 AI 落地實務 → 見 `references/data-ai-enablement.md`
- 敏捷組織與變革管理 → 見 `references/agile-change.md`
- 台灣企業 DX 實務與在地挑戰 → 見 `references/tw-dx-context.md`
- 各校 EMBA 資管 / DX 課程取向 → 見 `references/emba-dx-courses.md`
- 延伸：Asgard `grad-digital-transformation`（DX 學理）、`grad-sociotechnical`（社會技術系統）、`grad-tam-utaut`（科技接受模型）、`data-*`（資料分析）；本 repo `biz-innovation-management`、`biz-net-zero-transition`、`ops-org-behavior`
