# DX 成熟度模型與營運模式重構筆記

## 成熟度模型的目的

- **診斷**：了解目前在哪
- **對齊**：跨部門共通語言
- **規劃**：識別 gap、設定目標
- **溝通**：對投資人、董事會說明進度

## 主要成熟度框架

### Gartner DX 成熟度（2020）
1. **Digital Survivors**（數位求生）：基礎 IT
2. **Digital Seekers**（數位探索）：局部數位化
3. **Digital Strivers**（數位努力）：策略性採納
4. **Digital Leaders**（數位領導）：全面轉型
5. **Digital Disruptors**（數位顛覆者）：重塑產業

### MIT Sloan & Deloitte（2015）
- 基於 DNA 視角
- **數位原生（Native）** vs. **數位成熟（Mature）** vs. **數位發展中（Developing）**
- 重視領導力與文化、非僅技術

### McKinsey 7S × DX
- Strategy、Structure、Systems、Shared Values、Skills、Style、Staff
- 每一 S 的 DX 指標

### IDC DX MaturityScape
- 5 個階段：
  - Ad Hoc
  - Opportunistic
  - Repeatable
  - Managed
  - Optimized
- 涵蓋策略、組織、資訊、客戶、營運五個維度

### 本 skill 使用的整合模型

**五級 × 六支柱**（見 SKILL.md）

## 各支柱的成熟度標誌

### 策略支柱

| 等級 | 指標 |
|---|---|
| L1 | 無數位策略、IT 預算為主 |
| L2 | 數位議題進入策略討論 |
| L3 | 明確數位戰略、與業務戰略對齊 |
| L4 | 數位為核心策略、新商模探索 |
| L5 | 產業重塑、生態系主導 |

### CX 支柱

| 等級 | 指標 |
|---|---|
| L1 | 單通路、無數位接觸 |
| L2 | 多通路、但各自獨立 |
| L3 | 全通路、資料整合 |
| L4 | 個人化、AI 推薦 |
| L5 | 預測性服務、生態互動 |

### 流程支柱

| 等級 | 指標 |
|---|---|
| L1 | 紙本、Excel、電話 |
| L2 | 核心流程有系統（ERP 等） |
| L3 | 端到端流程整合、跨部門 |
| L4 | 流程自動化（RPA、AI） |
| L5 | 自我最佳化、預測性流程 |

### 資料支柱

| 等級 | 指標 |
|---|---|
| L1 | 資料分散、品質差 |
| L2 | 部門資料倉儲、BI 報表 |
| L3 | 統一資料平台、自助分析 |
| L4 | AI / ML 嵌入決策 |
| L5 | 資料產品化、對外共享 |

### 技術支柱

| 等級 | 指標 |
|---|---|
| L1 | 老舊系統、地端為主 |
| L2 | 部分雲端、現代化 ERP |
| L3 | 雲端為主、API 架構 |
| L4 | 微服務、平台化 |
| L5 | 邊緣計算、生態 API |

### 組織支柱

| 等級 | 指標 |
|---|---|
| L1 | 傳統科層、功能分離 |
| L2 | 跨部門專案 |
| L3 | 矩陣組織、數位單位 |
| L4 | 敏捷團隊、Product Team |
| L5 | 全組織敏捷、生態協作 |

## 營運模式（Operating Model）核心

### 定義

**Operating Model = 組織如何運作以交付策略的藍圖**。
包括：
- **People**：組織結構、人才、能力、文化
- **Process**：流程、決策、績效
- **Technology**：系統、資料、架構
- **Partnerships**：合作夥伴、生態系

### 傳統 vs. 數位營運模式

| 面向 | 傳統 | 數位 |
|---|---|---|
| 組織 | 部門分層 | 跨功能團隊 |
| 決策 | 向上審批 | 授權前線 |
| 績效 | 年度 KPI | 即時 OKR |
| 客戶 | 銷售完即結束 | 持續互動 |
| 產品 | 推出即凍結 | 持續迭代 |
| 資料 | IT 管理 | 業務擁有 |
| 技術 | 專案式購買 | 平台與 API |
| 速度 | 季度 / 年 | 週 / 月 |

### TOM（Target Operating Model）設計

**TOM 的六個常見維度**：
1. 組織架構
2. 人才與能力
3. 流程
4. 決策權與治理
5. 技術架構
6. 資料與指標

**TOM 設計流程**：
1. 願景（Vision）
2. 主要決策點（Decision Rights）
3. 關鍵能力（Capabilities）
4. 組織結構（Structure）
5. 流程設計（Processes）
6. 技術藍圖（Technology）
7. 實施路徑（Roadmap）

## 敏捷組織

### Spotify Model 細節

**Squad**
- 6–12 人、跨功能
- 自主產品 / 功能
- 產品經理（PO）帶領

**Tribe**
- 3–10 個 Squad 組成
- 相關產品領域
- Tribe Lead 協調

**Chapter**
- 同職能橫向組織（例：所有 Squad 的後端工程師）
- Chapter Lead 為職涯發展導師

**Guild**
- 跨 Tribe 興趣社群
- 自願參與

### Spotify Model 的批評（含 Spotify 自己的反思）
- 實際 Spotify 並非完全如此
- 未解決跨 Tribe 依賴
- 純複製會失敗

### 其他敏捷模型

**SAFe（Scaled Agile Framework）**
- 大型企業敏捷
- Portfolio、Program、Team 三層
- 更結構化

**LeSS（Large-Scale Scrum）**
- 簡化版大規模敏捷
- 保持 Scrum 本質

**Disciplined Agile**
- IBM 推動
- 選擇式敏捷（Choose Your WoW）

**台灣企業建議**：
- 數位產品團隊：Squad / Scrum
- 傳統業務：看板（Kanban）先導入
- 避免全公司強推

## 客戶體驗重設計

### 客戶旅程映射（Customer Journey Mapping）

**步驟**：
1. Persona 設計
2. 關鍵旅程識別
3. 每階段的接觸點
4. 每接觸點的痛點 / 機會
5. 數位化建議
6. 優先順序

### Service Design Thinking
- 同理 → 定義 → 發想 → 原型 → 測試
- 適用服務業、B2C

### 全通路（Omnichannel）設計
- 目標：客戶在任何通路都有連貫體驗
- 技術要件：統一客戶 ID、整合資料、API 串接
- 組織要件：一位 Customer Owner、非分通路部門

## 資料驅動決策的阻抗

### 阻抗源

**1. HIPPO（Highest Paid Person's Opinion）**
- 老闆說了算
- 資料只是「佐證」
- 破解：董事會承諾「資料優先」

**2. 資料不可信**
- 不同部門數字對不起來
- 破解：資料治理、單一真相來源

**3. 工具不友善**
- BI 工具需訓練
- 破解：自助分析、UX 優化

**4. 既得利益者**
- 數據透明 = 被管
- 破解：漸進、共創

## 數位人才戰略

### 數位人才類型

**技術人才**
- 軟體工程師
- 資料工程師
- 資料科學家
- DevOps / SRE
- 資安工程師

**產品人才**
- 產品經理
- UX / UI 設計師
- 用戶研究員

**業務 × 數位人才**
- 數位行銷
- 數位銷售
- 業務分析師

**管理人才**
- CDO / CIO / CDA
- 敏捷教練
- DX 專案經理

### 人才策略矩陣

| 人才類型 | Build（自養） | Buy（挖角） | Borrow（外包 / 顧問） |
|---|---|---|---|
| 核心戰略 | 高 | 中 | 低 |
| 業界稀缺 | 中 | 高 | 中 |
| 短期需求 | 低 | 中 | 高 |

### 台灣數位人才市場

**熱缺領域（2026）**
- 資料工程師
- AI / ML 工程師
- 資安
- 雲端架構
- 產品經理

**薪資行情（參考）**
- 資料工程師：80 萬 – 180 萬
- 資料科學家：120 萬 – 300 萬
- 產品經理：100 萬 – 250 萬
- 雲端架構：150 萬 – 350 萬
- CDO：350 萬 – 800 萬 +

## DX 典型失敗模式

### 失敗模式 1：技術驅動（Tech-First）
- 先買工具、再找用途
- 結果：使用率低、被砍
- **修正**：業務問題驅動

### 失敗模式 2：CIO 獨行
- CEO 不介入、CIO 孤軍
- 結果：事業部抵制
- **修正**：CEO 親主、跨部門治理

### 失敗模式 3：Big Bang
- 所有系統一次切換
- 結果：業務中斷、員工崩潰
- **修正**：漸進、試點、擴散

### 失敗模式 4：速成 KPI
- 3 個月看到成果
- 結果：表面數字、無實質
- **修正**：短期 Quick Wins + 長期里程碑

### 失敗模式 5：忽略文化
- 系統改、文化不改
- 結果：老路回歸
- **修正**：變革管理並行

### 失敗模式 6：外包過度
- 全交給顧問 / 廠商
- 結果：無內部能力、鎖定風險
- **修正**：核心能力內部化

## 延伸閱讀

- Kane, G. C., Palmer, D., Phillips, A. N., Kiron, D., & Buckley, N. (2015). *Strategy, not technology, drives digital transformation*. MIT Sloan.
- Westerman, G., Bonnet, D., & McAfee, A. (2014). *Leading Digital*.
- Ross, J. W., Beath, C. M., & Mocker, M. (2019). *Designed for Digital*.
- Rogers, D. L. (2016). *The Digital Transformation Playbook*.
- Bonnet, D., & Westerman, G. (2021). *The New Elements of Digital Transformation*. MIT Sloan.
- Gothelf, J., & Seiden, J. (2016). *Lean UX* (2nd ed.).
- Kniberg, H., & Ivarsson, A. (2012). *Scaling Agile @ Spotify*.

---

## DX KPI 五層架構

### 策略層
- 數位收入占比
- 新商業模式營收
- 客戶生命週期價值（LTV）
- 市佔率變化

### 營運層
- 自動化率（自動 vs. 手動流程比例）
- 訂單處理時間
- 客戶滿意度（NPS）
- 員工生產力

### 技術層
- 系統可用性（SLA）
- 資料品質指標
- AI 模型準確率
- 資安事件數

### 組織層
- 數位人才比例
- 員工數位素養
- 敏捷團隊佔比
- 離職率（特別是數位人才）

### 轉型治理層
- 轉型專案 on-time、on-budget 比例
- Steering Committee CEO 出席率
- 跨部門協作滿意度

## KPI 設計原則
- 五層必須平衡，不可獨尊策略層或技術層
- 每層建議 3–5 個指標，超過 15 個 KPI 難以管理
- 與 DX 成熟度對齊：L1–L2 重營運與技術層、L3 強化策略與組織、L4–L5 強化治理
- 年度檢視並剔除過時指標
