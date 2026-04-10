# Example: SaaS 人資平台評估現有商業模式

## Scenario

**公司**：Workpio（台灣，成立 2022 年）  
**產品**：雲端人資管理 SaaS，主要功能：出勤管理、薪資計算、電子簽核  
**現況**：

- 客戶 320 家，全部為台灣 50–500 人規模中小企業
- ARR NT$18M，月流失率 2.8%（行業平均 1.5%）
- 主要收費：每月每帳號 NT$299，平均每客戶 40 帳號 → 月收 NT$11,960
- 團隊 15 人，其中 9 人工程師、3 人業務、3 人客服
- 月燒錢 NT$2.1M，runway 約 8 個月

**CEO 的問題**：「我們留不住客戶，高流失率快把我們逼死了。我想知道現在的商業模式哪裡出了問題，以及是否應該轉型成市集模式（讓顧問、會計師在平台接案）。」

---

## Analysis

### Step 1：填寫現有商業模式的九個積木

先把 current state 寫清楚，再討論轉型。

| 積木 | 現況描述 |
|------|----------|
| **Customer Segments** | 台灣中小企業（50–500 人），HR 人員 1–3 名，IT 能力有限，自行採購決策 |
| **Value Propositions** | 取代 Excel 薪資表＋出勤打卡機；勞基法自動合規計算；電子化簽核減少紙本 |
| **Channels** | Google Ads（40%）、業務電話開發（35%）、口碑介紹（25%）；14 天免費試用→付費轉換 |
| **Customer Relationships** | 自助文件＋Email 工單；無專屬客成；新客導入全靠 YouTube 教學影片 |
| **Revenue Streams** | 月費訂閱 NT$299/帳號；最低消費 20 帳號；一次性導入費 NT$5,000（常被免除以促成交易） |
| **Key Resources** | AWS 雲端基礎設施；勞基法法規資料庫；9 人工程團隊；客戶出勤與薪資資料 |
| **Key Activities** | 產品開發與維護；勞基法更新同步；業務開發；客服工單處理 |
| **Key Partnerships** | AWS（IaaS）；財政部電子發票串接；無其他實質夥伴 |
| **Cost Structure** | 人力 NT$1.6M（76%）；行銷 NT$250K（12%）；AWS NT$120K（6%）；其他 NT$130K；共 NT$2.1M/月 |

---

### Step 2：一致性檢查

| 連結 | 一致？ | 說明 |
|------|--------|------|
| Value Prop ↔ Segments | ✓ | 中小企業確實痛在 Excel 薪資與打卡機，NPS +42 確認價值主張匹配 |
| Channels ↔ Segments | ⚠️ | Google Ads 能觸及，但 HR 採購決策者依賴同業推薦，口碑僅 25% 偏低 |
| Revenue ↔ Cost | ✗ | 月收 NT$1.5M，月燒 NT$2.1M，**每月虧損 NT$600K**，不可持續 |
| Customer Relationships ↔ Churn | ✗ | **月流失 2.8% 根源在此**：無客成、無導入支援，客戶自生自滅 |
| Key Activities ↔ Value Prop | ⚠️ | 工單量 60% 是「使用困難」而非「法規問題」，代表導入失敗而非產品缺陷 |

**核心診斷**：問題不在市場或產品方向，而在 **Customer Relationships 完全空洞** — 客戶導入失敗 → 感受不到價值 → 第 3–6 個月流失。

---

### Step 3：最高風險假設

| 積木 | 假設 | 風險等級 |
|------|------|----------|
| Customer Relationships | 「客戶看 YouTube 就會自己上手」 | 🔴 已被 2.8% 流失率否定 |
| Revenue Streams | 「導入費免除能促成更多交易」 | 🔴 消除了客戶認真導入的動機 |
| Key Partnerships | 「只靠自有通路就夠了」 | 🟡 缺乏會計師/顧問轉介，CAC 居高不下 |
| Value Propositions | 「合規計算是主要價值」 | 🟢 客戶調查確認，風險低 |

---

### Step 4：市集轉型模式評估（多邊平台比較）

CEO 想加入「顧問與會計師接案市集」——Uber 有司機與乘客兩側，此市集有企業與顧問兩側，需各自填寫 BMC：

| 積木 | 現有 SaaS（企業側） | 市集新增（顧問側） |
|------|-------------------|------------------|
| **Customer Segments** | 中小企業 HR | 獨立薪資顧問、會計師事務所 |
| **Value Propositions** | 自動化省時合規 | 顧問：穩定接案來源；企業：「軟體＋人」一站式服務 |
| **Revenue Streams** | 月費訂閱 | ＋媒合抽成 8–15%；顧問端月費 NT$499 |
| **Key Activities** | 產品開發、法規更新 | ＋顧問資格審核、評價系統、糾紛處理 |
| **Cost Structure** | 人力為主 | ＋信任機制建置（背景查核、保險、客訴處理） |

**市集冷啟動問題**：顧問少 → 企業不來；企業少 → 顧問不留。建立雙側臨界規模通常需要 12–18 個月，Workpio 剩餘 runway 僅 8 個月，**時序不允許**。

---

## Result

### Business Model Canvas：Workpio

| 積木 | 描述 |
|------|------|
| **Customer Segments** | 台灣中小企業（50–500 人），HR 人員主導採購 |
| **Value Propositions** | 勞基法自動合規薪資計算；取代紙本打卡與 Excel；電子簽核流程 |
| **Channels** | Google Ads、業務電話、口碑介紹；14 天試用轉換漏斗 |
| **Customer Relationships** | 純自助（文件＋YouTube＋Email 工單）— **根本問題所在** |
| **Revenue Streams** | NT$299/帳號/月，最低 20 帳號；ARR NT$18M；導入費常被免除 |
| **Key Resources** | 工程團隊、勞基法資料庫、客戶薪資與出勤資料 |
| **Key Activities** | 產品開發、法規更新同步、業務開發、客服工單 |
| **Key Partnerships** | AWS、財政部電子發票（夥伴生態薄弱） |
| **Cost Structure** | 人力 76%、行銷 12%、基礎設施 6%；月燒 NT$2.1M |

### 一致性檢查

| 連結 | 一致？ | 說明 |
|------|--------|------|
| Value Prop ↔ Segments | ✓ | 痛點對齊，NPS +42 確認 |
| Channels ↔ Segments | ⚠️ | 需補強通路夥伴（會計師、顧問轉介） |
| Revenue ↔ Cost | ✗ | 月虧 NT$600K，需提升 ARPU 或降低 CAC |
| Customer Relationships ↔ Churn | ✗ | 無客成 → 2.8% 流失，是存活威脅 |

### 最高風險假設

1. **Customer Relationships**：假設客戶自助導入可行 → 2.8% 流失已否定，立即修正
2. **Revenue Streams**：導入費被免除 → 失去 onboarding 動機，變相補貼不認真導入的客戶
3. **Key Partnerships**：無通路夥伴 → 高 CAC 且口碑來源稀薄

### 建議：先穩後轉

**不建議現在做市集轉型**（runway 8 個月，冷啟動需 12–18 個月，時序不符）。

優先修復流失問題（90 天計畫）：

| 動作 | 修改積木 | 預期影響 |
|------|----------|----------|
| 前 30 天指定客成，電話導入 | Customer Relationships | 流失降至 1.5%，每月多留 ~NT$400K |
| 恢復導入費 NT$8,000（含 4 小時上線輔導） | Revenue Streams | 提升 ARPU＋確保客戶認真導入 |
| 與 3 家薪資顧問事務所談轉介佣金（首年 20%） | Key Partnerships | 降低 CAC，增加口碑來源 |

待流失率降至 1.5% 以下、runway 延伸至 18 個月後，再用完整 BMC 評估市集轉型可行性。

---

以上是完整的 `sample_scenario.md` 內容。請確認是否要我直接將這份檔案寫入 `ops-business-model-canvas/examples/sample_scenario.md`？
