直接建立檔案：

```markdown
# Example: Taiwan HR SaaS — Q2 2026 OKR Planning

## Scenario

CloudHR 是一家台灣 B2B HR SaaS 新創，提供中小企業薪資與人事管理系統，目前 45 人、Series A 後期。

CEO 帶著這個問題來：

> 「我們 Q1 新簽了 38 家客戶，但流失了 14 家，NPS 只有 22，業務和產品各做各的。董事會要我們 Q2 把重心轉到留存，但我不知道怎麼把這個轉成所有人都看得懂的目標。以前用 KPI，每個部門有自己的指標，沒人在乎別人的。」

現有 KPI（參考用，不直接沿用）：
- 業務：每月新簽合約數
- 產品：功能發布頻率  
- 客服：工單平均回應時間

---

## Analysis

### Step 1 — 識別策略轉向，確立公司層級方向

CEO 的問題核心是方向問題，不是工具問題。從「獲客優先」轉為「留存優先」，必須先在公司層級確立，再讓各團隊翻譯成自己的 OKR。

**公司 Q2 策略重心**：提升現有客戶留存與擴展收入，使每位客戶的 LTV 成長。

---

### Step 2 — 設定公司 OKR

**O1：讓 CloudHR 成為台灣 SMB 老闆捨不得換掉的 HR 系統**

| KR | Baseline（Q1 末） | Target（Q2 末） | 類型 |
|----|------------------|----------------|------|
| KR1：月流失率（Churn Rate） | 4.2% | ≤ 2.0% | lagging |
| KR2：NPS | 22 | 40 | lagging |
| KR3：Net Revenue Retention（NRR） | 88% | 100% | lagging |
| KR4：新客戶完成 onboarding 流程比例 | 41% | 75% | **leading** |

KR4 是 leading indicator：onboarding 完整度通常領先 90 天後的留存率，讓團隊有辦法在季中修正，而不是等 Q2 末才發現流失。

**O2：讓全公司對「哪些客戶有風險」有共同視野**

| KR | Baseline | Target |
|----|----------|--------|
| KR1：Customer Health Score 儀表板上線並每週全員同步 | 無 | Q2W4 上線 |
| KR2：高風險客戶（Health Score < 50）主動觸達覆蓋率 | 0% | 100%（每月 ≥ 1 次） |
| KR3：建立 CSM 預測準確率基線 | 無紀錄 | Q2 末建立，供 Q3 優化 |

---

### Step 3 — 團隊 OKR 級聯（Cascade）

公司 OKR 確定後，各團隊將公司目標翻譯成自己領域的貢獻，而非複製貼上。

#### 產品團隊（支援公司 O1、O2）

**O1：讓新客戶在 7 天內感受到 CloudHR 的核心價值**

| KR | Baseline | Target |
|----|----------|--------|
| KR1：新客戶 time-to-first-value（完成第一次薪資跑帳） | 平均 11 天 | ≤ 5 天 |
| KR2：Onboarding wizard 完成率 | 41% | 75% |
| KR3：Onboarding 期間客戶主動發起工單數 | 6.3 張/客戶 | ≤ 3 張/客戶 |

**O2：提供全公司可自助查詢的客戶健康度工具**

| KR | Target |
|----|--------|
| KR1：Health Score 模型定義完成，CS 驗收通過 | Q2W3 |
| KR2：儀表板整合至內部工具，CS + 業務均可自助查詢 | Q2W5 |

#### 業務團隊（支援公司 O1）

**O1：讓客戶的成功成為我們最好的業務工具**

| KR | Baseline | Target |
|----|----------|--------|
| KR1：現有客戶升級方案（upsell）產生的 ARR | NT$0 | NT$800,000 |
| KR2：客戶轉介紹（referral）帶來的新簽合約數 | 2 家/季 | 8 家/季 |
| KR3：高風險客戶挽留成功率 | 無紀錄 | 建立基線 |

> 業務 Q2 刻意不設新簽合約數目標——若同時追新客戶，業務會優先衝新簽而忽略 upsell 與挽留，與公司策略轉向背道而馳。

---

### Step 4 — 陷阱確認

| 陷阱 | CloudHR 的具體情境 | 處理方式 |
|------|-------------------|---------|
| OKR 變成 to-do list | 「上線 Health Score 儀表板」是任務，不是 KR | 改為：儀表板上線後，高風險客戶觸達覆蓋率達 100% |
| 目標不夠有野心 | NPS 22→40 夠 stretch 嗎？ | 台灣 B2B SaaS 平均 NPS 約 28–32，40 是顯著 stretch |
| OKR 綁薪酬 | 原有 KPI 制有業務獎金 | 明確宣示：Q2 OKR 評分與獎金分離，不做掛鉤 |
| 先做團隊 OKR 再補公司 OKR | 以前各部門各自為政 | 本次強制先確認公司 O1/O2，各隊再提貢獻方案 |

---

## Result

```markdown
# OKR Plan: CloudHR — Q2 2026（2026-04-01 ～ 2026-06-30）

## Company Objectives

### O1：讓 CloudHR 成為台灣 SMB 老闆捨不得換掉的 HR 系統
- KR1：月流失率 — 4.2% → ≤ 2.0%
- KR2：NPS — 22 → 40
- KR3：Net Revenue Retention — 88% → 100%
- KR4：新客戶 onboarding 完成率 — 41% → 75%（leading indicator）

### O2：讓全公司對「哪些客戶有風險」有共同視野
- KR1：Customer Health Score 儀表板 Q2W4 上線，每週全員同步
- KR2：高風險客戶主動觸達覆蓋率 — 0% → 100%（每月 ≥ 1 次）
- KR3：建立 CSM 預測準確率基線（Q3 優化依據）

## Team OKRs

### 產品團隊

#### O1：讓新客戶在 7 天內感受到 CloudHR 的核心價值（支援公司 O1）
- KR1：time-to-first-value — 11 天 → ≤ 5 天
- KR2：onboarding wizard 完成率 — 41% → 75%
- KR3：onboarding 期支援工單數 — 6.3 張 → ≤ 3 張/客戶

#### O2：提供全公司可自助查詢的客戶健康度工具（支援公司 O2）
- KR1：Health Score 模型定義完成，CS 驗收通過 — Q2W3
- KR2：儀表板整合完成，CS + 業務自助可查 — Q2W5

### 業務團隊

#### O1：讓客戶的成功成為我們最好的業務工具（支援公司 O1）
- KR1：現有客戶 upsell ARR — NT$0 → NT$800,000
- KR2：客戶轉介紹新簽合約數 — 2 家 → 8 家/季
- KR3：高風險客戶挽留成功率基線（Q2 末建立）

## Check-in Template（每週五）

| KR | Target | Current (W6) | Confidence | Blocker |
|----|--------|-------------|-----------|---------|
| 月流失率 | ≤ 2.0% | 3.1% | 🟡 | 3 家高風險客戶待訪談 |
| NPS | 40 | 28 | 🟡 | Q2W8 發問卷 |
| onboarding 完成率 | 75% | 52% | 🟢 | — |
| upsell ARR | NT$800K | NT$180K | 🔴 | Health Score 儀表板尚未上線 |

🟢 按計畫 ／ 🟡 輕微落後，可追回 ／ 🔴 需要介入
```

**Q2 評分預期**

- **0.7–0.8**：理想。目標有足夠 stretch，執行有力。
- **0.9–1.0**：檢視下季目標是否夠有野心。
- **< 0.5**：召開 retrospective，區分執行問題與目標設定問題。
```

這是完整的範例內容，以下直接建立檔案：

```

OK，我直接建立檔案，不再贅述：
