# 台灣行銷／銷售技術堆疊（MarTech／SalesTech）地景

## 技術分類與代表供應商

### 1. 電商平台（Commerce Platform）

**B2C 零售**
- **91APP**（台灣）：一條龍電商 + App + 線下整合，中型品牌首選
- **Shopline**（香港／台灣）：SaaS 電商，進入門檻低
- **Cyberbiz**（台灣）：中小品牌常見
- **Shopify**（國際）：跨境品牌、海外市場
- **WooCommerce**（開源）：自建彈性高、技術門檻中等

**大型／跨境**
- **Magento / Adobe Commerce**：大型多站點
- **SAP Commerce Cloud**：企業級整合
- **Salesforce Commerce Cloud**：大型 B2C 品牌

### 2. CRM 系統

**B2B 銷售導向**
- **Salesforce**（國際領導者）：大型企業、生態豐富、顧問生態完整
- **HubSpot**：中小企業入門友善、整合行銷
- **Microsoft Dynamics 365**：與 Office／ERP 整合
- **Zoho CRM**：性價比高、中小企業

**台灣本地**
- **鼎新電腦 CRM**：傳產、製造業熟悉
- **關貿網路 CRM**：中大型企業
- 多數台灣 SME 仍用 Excel + Email + LINE 組合

### 3. 會員／忠誠平台

**台灣原生**
- **91APP OMO**：零售整合
- **台灣大哥大 OP 會員**：跨業聯盟
- **全聯 PX Pay**：自家體系
- **Open Point**（統一超）：跨業聯盟

**國際**
- **Yotpo Loyalty**：電商會員
- **Annex Cloud**：大型零售
- **Salesforce Loyalty Management**：企業級

### 4. 行銷自動化（Marketing Automation）

**入門級**
- **Mailchimp**：小規模 EDM 為主
- **Omnichat**（台灣）：LINE + FB Messenger 自動化
- **Freemind**（台灣）：AI 驅動的行銷自動化

**中階**
- **Braze**：行動 App 為主
- **Iterable**：跨通路 orchestration
- **HubSpot Marketing Hub**：整合 CRM

**企業級**
- **Salesforce Marketing Cloud**：完整 Journey Orchestration
- **Adobe Journey Optimizer**：Adobe 生態整合
- **Oracle Eloqua**：B2B 強

### 5. CDP（Customer Data Platform）

**國際**
- **Segment**（Twilio）：開發者友善
- **Tealium**：企業級資料整合
- **mParticle**：行動優先
- **Adobe Real-Time CDP**：Adobe 生態
- **Salesforce Data Cloud**：Salesforce 生態

**台灣／亞太**
- **Vpon**（台灣）：旅遊、零售
- **Pichu**（台灣）：中小企業
- **Appier BotBonnie**：亞洲為主
- **ET（玩美移動子公司）**：美妝垂直

**自建 vs. 採購決策**
- 自建：資料主權高、客製彈性大、技術門檻高、至少 NT$ 2,000 萬起
- 採購：快速上線、年費 300–800 萬、客製彈性受限

### 6. 分析與 BI

**免費／低價**
- **Google Analytics 4**：網站分析基礎
- **Google Data Studio / Looker Studio**：視覺化免費
- **Metabase**（開源）：儀表板

**企業級**
- **Tableau**（Salesforce）：視覺化領先
- **Microsoft Power BI**：整合 Microsoft 生態
- **Looker**（Google Cloud）：資料建模完整
- **Qlik Sense**：自助式分析

### 7. 廣告技術（AdTech）

**Ads 平台**
- Google Ads、Meta Ads、LINE Ads Platform、TikTok Ads、蝦皮廣告

**追蹤與歸因**
- **AppsFlyer**：行動歸因
- **Adjust**：類似 AppsFlyer
- **Google Campaign Manager**：跨通路廣告

### 8. 客服／Chat

**即時通訊**
- **LINE 官方帳號**：台灣第一大通路
- **LINE Shopping**：交易整合

**客服系統**
- **Zendesk**：國際標準
- **Freshdesk**：性價比高
- **Intercom**：SaaS 客服

**Chatbot**
- **Omnichat**、**BotBonnie**（Appier）、**ChatBot.com**

## 台灣企業 MarTech 堆疊典型組合

### 組合 A：中小電商（年營收 < 3 億）
```
電商平台：Shopline / Cyberbiz
會員系統：平台內建
EDM：Mailchimp / 平台內建
LINE：LINE 官方帳號 + Omnichat
分析：GA4 + Shopline / Cyberbiz 後台
成本：年 50–150 萬
```

### 組合 B：中型品牌（3–30 億）
```
電商平台：91APP（含 App）
會員系統：91APP OMO
CRM：HubSpot / 關貿
行銷自動化：91APP Marketing / Omnichat
分析：GA4 + Looker Studio / Power BI
LINE：多通路 LINE CRM 整合
成本：年 300–800 萬
```

### 組合 C：大型零售／金融（> 30 億）
```
電商平台：Salesforce Commerce Cloud / 自建
CRM：Salesforce Sales Cloud
行銷自動化：Salesforce Marketing Cloud / Braze
CDP：Segment / Tealium / 自建
會員：自建或 Salesforce Loyalty
資料倉儲：BigQuery / Snowflake
分析：Tableau / Looker
成本：年 3,000 萬以上
```

### 組合 D：B2B 製造／科技
```
CRM：Salesforce / Microsoft Dynamics
行銷自動化：HubSpot / Pardot
ABM 工具：Demandbase / 6sense（少數）
分析：Power BI / Tableau
LinkedIn Sales Navigator
成本：年 500–2,000 萬
```

## 選型決策樹

```
Q1：年度行銷技術預算？
  < 100 萬 → 組合 A（中小）
  100–500 萬 → 組合 B（中型）
  500–3,000 萬 → 組合 B+ 升級組件
  > 3,000 萬 → 組合 C（大型）

Q2：是 B2B 還是 B2C？
  B2B → Salesforce 或 HubSpot 為中心
  B2C → 電商平台 + 會員系統為中心
  混合 → 雙軌（兩套系統少交集）

Q3：有沒有 App？
  有 → Braze 等行動優先工具優先
  無 → 網頁 + EDM + LINE 為主

Q4：資料分散度？
  1–2 系統 → 不需 CDP
  3–5 系統 → 考慮 CDP
  > 5 系統 → 強烈需要 CDP

Q5：團隊技術能力？
  低 → SaaS 為主、避免自建
  中 → SaaS + 部分自建
  高 → 可混合，甚至完全自建
```

## 採購常見陷阱

### 陷阱 1：功能迷信
**症狀**：被供應商 demo 的所有功能驚艷，全勾選
**後果**：80% 功能未用，年費高昂
**解方**：先列出自己的 3–5 個核心需求，再選

### 陷阱 2：顧問費黑洞
**症狀**：年費 500 萬的系統，顧問費 1,500 萬
**後果**：實施期 12–18 個月，超支超時
**解方**：先問清導入與持續顧問費用比例

### 陷阱 3：組織不配套
**症狀**：買了工具但沒人負責使用
**後果**：變成 IT 部門管的閒置資產
**解方**：採購前先設定使用者與 KPI 責任人

### 陷阱 4：資料未清洗
**症狀**：系統上線後資料垃圾進垃圾出（GIGO）
**後果**：所有分析都不可信
**解方**：採購前先做資料品質盤點

### 陷阱 5：供應商鎖定
**症狀**：一個生態綁死（如 Salesforce 全家桶）
**後果**：年年漲價、換平台成本極高
**解方**：保留多廠策略，至少關鍵資料可遷移

## 法遵與資安

**台灣特別注意**
- PDPA 個資法：同意機制、資料保留、被遺忘權
- 資料跨境：使用 AWS / Google Cloud 海外區域需評估
- GDPR：若有歐洲客戶需合規
- 金管會規定：金融業資料處理有特殊要求

**常用工具**
- **OneTrust**：同意管理（Consent）
- **TrustArc**：隱私治理
- **內建 Consent**：多數 MarTech SaaS 已內建基礎功能

## 未來趨勢（2025–2027）

1. **AI 全面嵌入**：每個工具都有 AI 功能（Salesforce Einstein、HubSpot AI）
2. **Cookie 淘汰後**：第一方資料更加重要、CDP 地位上升
3. **LINE 整合深化**：台灣特有，LINE Service 整合各 CRM
4. **垂直化 SaaS**：產業特化工具增加（如美妝、保險、B2B 特定垂直）
5. **低程式碼（Low-code）**：行銷團隊可自行設定，降低 IT 依賴
6. **Retail Media Network**：零售品牌自建廣告媒體
