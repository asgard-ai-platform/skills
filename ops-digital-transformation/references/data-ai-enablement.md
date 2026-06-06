# 資料與 AI 落地實務筆記

## 資料成熟度（Data Maturity）

### 五級路徑

**L1：分散、混亂**
- 資料在 Excel、紙本、各系統
- 無品質
- 無共通定義

**L2：部門型**
- 部門資料倉儲
- 固定報表
- 品質待改善

**L3：整合型**
- 企業資料平台（EDW / Data Lake）
- 自助分析
- 資料治理

**L4：智慧型**
- AI / ML 嵌入流程
- 即時 / 預測分析
- 資料驅動決策文化

**L5：產品型**
- 資料本身為產品
- 對外 API
- 生態協作

## 資料治理（Data Governance）

### 核心要素

**1. 資料擁有者（Data Owner）**
- 每個資料域有負責業務主管
- 非 IT 人員（但與 IT 協作）

**2. 資料品質（Data Quality）**
- 六維度：正確性、完整性、一致性、及時性、獨特性、有效性
- 定期評估、改善計畫

**3. 資料目錄（Data Catalog）**
- 所有資料資產清單
- 含 metadata、使用者、權限

**4. 資料標準**
- 主資料（Master Data）定義
- 編碼規則
- 欄位格式

**5. 資料安全與隱私**
- 存取控制
- 加密
- 個資法合規
- 資料脫敏

### 資料治理組織

**Chief Data Officer（CDO / CDA）**
- 組織層級
- 直屬 CEO 或 CIO

**Data Governance Council**
- 業務高管 + CDO + CIO
- 月度
- 決策：政策、優先順序

**Data Stewards**
- 各業務部門
- 資料品質責任
- 日常治理

## 資料平台架構

### 傳統 vs. 現代

**傳統 Data Warehouse**
- ETL（Extract, Transform, Load）
- 結構化資料
- 固定 Schema

**現代 Data Lake / Lakehouse**
- ELT（Extract, Load, Transform）
- 結構化 + 半結構化 + 非結構化
- Schema-on-Read

**Lakehouse 架構（2020+）**
- 結合 Data Lake 與 Warehouse 優點
- 代表：Databricks Delta Lake、Snowflake

### 常見技術組合

**公有雲**
- AWS：S3 + Glue + Redshift + EMR
- Azure：Data Lake Storage + Synapse + Fabric
- GCP：GCS + BigQuery + Dataflow

**地端 / 混合**
- Hadoop / Spark
- Snowflake（跨雲）
- Databricks（跨雲）

**台灣企業常見選擇**
- 大型上市：Snowflake、Databricks、AWS / Azure 企業方案
- 中型：單一雲、託管服務
- 小型：SaaS BI（Tableau、Power BI、Looker）

### 資料平台組件

- 資料擷取（ingestion）：Kafka、Airflow
- 儲存（storage）：S3、ADLS、GCS
- 計算（compute）：Spark、Snowflake、BigQuery
- 治理：Collibra、Alation
- BI：Tableau、Power BI、Looker
- ML 平台：Databricks、SageMaker、Vertex AI

## AI 落地的實務路徑

### 五步方法

**Step 1：業務問題定義**
- 不是「我們要做 AI」、而是「哪個業務問題值得 AI 解決」
- 5 個篩選條件：
  1. 問題明確
  2. 有大量歷史資料
  3. 決策可量化
  4. 投資回報可估
  5. 組織能接納 AI 結果

**Step 2：資料就緒度評估**
- 資料量是否足夠？
- 資料品質？
- 標註（Labeled）資料？

**Step 3：模型開發**
- PoC（Proof of Concept）
- MVP
- 內部評估

**Step 4：部署與整合**
- ML Ops（模型部署）
- 整合到業務流程
- 使用者介面

**Step 5：持續優化**
- 模型再訓練
- 使用者回饋
- 指標追蹤

### AI 應用常見情境

**預測**
- 銷售預測
- 需求預測
- 離職預測
- 違約預測

**推薦**
- 個人化產品推薦
- 內容推薦
- 下一步最佳行動（NBA）

**分類**
- 客戶分層
- 詐欺偵測
- 情感分析

**視覺 AI**
- 品質檢測
- 顧客計數
- 設施監控

**NLP**
- 聊天機器人
- 合約審查
- 客服自動化

**生成式 AI（2023+）**
- 內容生成
- 程式碼
- 客服
- 摘要

## 生成式 AI 的企業應用

### 應用場景

**生產力**
- 文件撰寫、摘要
- 會議記錄
- 程式碼生成

**客戶互動**
- 智能客服
- 個人化行銷文案
- 產品文件

**知識管理**
- 內部 Q&A 系統
- 文件搜尋
- 訓練資料生成

**決策支援**
- 報告分析
- 風險評估
- 情境模擬

### 導入挑戰

**1. 資訊安全**
- 公司資料是否傳到外部？
- 資料外洩風險

**2. 正確性**
- 幻覺（Hallucination）
- 需驗證流程

**3. 合規**
- 著作權
- 個資法
- 產業法規

**4. 成本**
- API 成本
- 模型訓練成本
- 內部化（自建）成本

**5. 人才**
- Prompt Engineering
- LLM Ops
- AI 應用架構

### 企業導入策略

**Layer 1：工具採用（Tools）**
- ChatGPT Enterprise、Microsoft Copilot、Google Gemini for Workspace
- 全體員工普及

**Layer 2：應用整合（Integration）**
- 與既有系統整合（CRM、知識庫）
- Prompt + Context 設計

**Layer 3：客製化（Customization）**
- RAG（Retrieval Augmented Generation）
- 微調（Fine-tuning）
- Agent 設計

**Layer 4：自建模型（Build）**
- 專業領域 LLM
- 主權資料
- 大型企業、高資本投入

## AI 治理

### AI 倫理原則
- 公平（無偏誤）
- 透明（可解釋）
- 當責（有負責人）
- 隱私
- 穩健（安全）

### 偏誤（Bias）處理
- 資料偏誤
- 演算法偏誤
- 部署偏誤

**工具**：
- Fairness 套件（IBM AIF360、Google What-If）
- 定期 Audit

### 可解釋性（Explainability）
- SHAP、LIME
- 依場景選擇（醫療、金融需高度可解釋）

### 企業 AI 倫理委員會
- 跨部門組成
- 政策與指引
- 高風險 AI 案例審議

### AI 決策責任
- 半自動（人在迴圈）
- 全自動
- 不同情境不同原則

## 資料與 AI 的 KPI

### 資料層
- 資料品質分數
- 資料涵蓋率（完整度）
- 自助分析使用者數
- 資料 API 呼叫量

### AI 層
- 模型數量（部署中）
- 模型準確率（對照業務指標）
- AI 相關營收 / 成本節省
- 使用者接受度

### 治理層
- 資料治理會議頻率
- Data Steward 涵蓋率
- AI 倫理審議案件數

## 資料 × AI 在台灣企業的常見失敗

### 失敗 1：沒有 CDO、資料治理不存在
- 各部門資料孤島
- AI 專案必然失敗

### 失敗 2：PoC 陷阱
- Pilot 成功、Scale 失敗
- 未考慮規模化條件

### 失敗 3：使用者不信任
- 模型準確率高、業務不用
- 未納入業務設計過程

### 失敗 4：資料隱私無意識
- 個資法違反
- 生成式 AI 外洩

### 失敗 5：人才流失
- 培養的人才被挖走
- 無保留機制

## 台灣企業的實務建議

### 中小企業（< 10 億營收）
- SaaS 優先（Tableau、Power BI、Google Analytics）
- 雲端平台初階（AWS、Azure）
- 外部顧問 + 少量內部人才
- 不做自建 ML 平台

### 中型企業（10–100 億）
- 資料平台建置（Snowflake、Databricks SaaS）
- 1–2 位 CDO / 資料長
- 10–30 人資料團隊
- 2–5 個 AI 用例

### 大型企業（100 億+）
- 自建 Lakehouse
- 完整治理組織
- 50+ 人資料與 AI 團隊
- 10+ AI 應用

## 延伸閱讀

- Davenport, T., & Ronanki, R. (2018). Artificial intelligence for the real world. *HBR*.
- Agrawal, A., Gans, J., & Goldfarb, A. (2018). *Prediction Machines*.
- DalleMule, L., & Davenport, T. (2017). What's your data strategy? *HBR*.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*.
- Wing, J. M. (2021). Trustworthy AI. *Communications of the ACM*.
- NIST AI Risk Management Framework (2023)
- EU AI Act (2024)
- 金管會 AI 金融應用指引

---

## AI 落地的 5 大陷阱

### 陷阱 1：技術先行
- 買了 AI 平台、不知道用來做什麼
- **修正**：從業務問題倒推

### 陷阱 2：資料不足 / 不乾淨
- AI 模型準確率低
- **修正**：先做資料基礎建設

### 陷阱 3：Pilot 陷阱
- 試點成功、但放大失敗
- **修正**：Pilot 設計時考慮 scale 條件

### 陷阱 4：組織阻抗
- 使用者不信任 AI 建議
- **修正**：共創、透明化、小勝利

### 陷阱 5：ROI 難證明
- AI 投資回報不明
- **修正**：明確衡量指標、階段性展示價值

## AI 治理

- **AI 倫理委員會**
- **偏誤審查**（Bias Audit）
- **可解釋性**（Explainability）
- **資料隱私**（符合個資法）
- **AI 決策責任歸屬**

## AI 成熟度 vs. 風險配比

| 成熟度 | 可容忍風險 | 建議做法 |
|---|---|---|
| 低 | 僅輔助人類 | 人工最終把關 |
| 中 | 半自動化 | 抽樣審核、爭議可退回人工 |
| 高 | 全自動化 | 嚴格 KPI 追蹤、異常預警 |
