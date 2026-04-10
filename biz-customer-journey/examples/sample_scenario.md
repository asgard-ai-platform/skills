QMD 工具被拒絕了，但這裡我只需要寫入本地檔案。根據 git status 確認 `biz-customer-journey/examples/` 目錄存在，直接寫入：

```markdown
# Example: SaaS 訂閱制平台的客戶旅程優化

## Scenario

**公司背景：** CloudForm，台灣本土 B2B SaaS，提供中小企業報帳與發票管理工具。月費方案 NT$990/月，目前有 3,200 名付費用戶。

**產品經理 Vivian 的問題：**
> 「我們的 Trial → Paid 轉換率只有 8%，業界平均是 20-25%。我知道我們在某個環節大量流失，但不確定是哪裡。能不能幫我把整個流程拉出來看？」

Vivian 提供了以下數據：
- 每月新增 Trial 用戶：約 500 人
- Trial 期：14 天
- Trial → Paid 轉換：8%（約 40 人）
- 付費後 3 個月留存率：72%
- NPS：+18（偏低）
- 支援信箱最常見主旨：「發票格式不對」、「匯出 PDF 失敗」、「不知道怎麼加員工帳號」

---

## Analysis

### Step 1: 定義 Persona

**Persona：Annie，45 歲，家族企業財務主管**
- 負責 10-50 人規模的製造業或貿易公司帳務
- 目標：減少月底報帳手工作業，讓會計師月結更順
- 痛點：不熟悉 SaaS，怕導入麻煩、怕資料搞丟
- 習慣：Google 搜尋、問同業推薦、Line 群組討論

> ⚠️ 注意：CloudForm 另有 IT 採購型 Persona（科技新創財務長），旅程完全不同——這份地圖只對應 Annie。

---

### Step 2: 各階段觸點、行動、情緒、痛點

**數據來源：** Hotjar 錄影回放 × 50 sessions、支援信箱 3 個月 ticket 分析、Trial 離場問卷（n=180）。

| Stage | 觸點 | 行動 | 情緒 | 痛點 | 機會 |
|-------|------|------|------|------|------|
| **Awareness** | Google 搜尋「電子發票管理系統」；Line 群同業推薦 | 點前三名搜尋結果；截圖傳給老闆 | 😊 有希望 | SEO 排名第 4，競品佔 1-3；廣告文案含「API 串接」嚇跑 Annie | 廣告文案改為「不需 IT，10 分鐘上線」；優化 Line 分享文案 |
| **Consideration** | 官網首頁；功能頁；定價頁；YouTube | 看功能比較表；找「適合我這種公司嗎」的線索 | 😐 猶豫 | 功能頁充滿技術術語；定價頁沒有「適合幾人公司」的引導；找不到中文教學影片 | 加互動問卷「找適合你的方案」；定價頁加「5-50 人公司最常選這方案」社群證明 |
| **Decision** | Trial 註冊頁；信用卡綁定流程 | 填表；猶豫要不要綁卡 | 😤 卡住 | Trial 需先綁信用卡（**最大摩擦點**）：62% 離場問卷標記「還沒準備好綁卡」；頁面未說明「試用期不扣費」 | 改為免信用卡 Trial；綁卡頁加顯眼說明「14 天到期前不收費，可隨時取消」 |
| **Usage（Trial）** | Onboarding Email；產品 UI；發票建立流程 | 試建第一張發票；嘗試加員工帳號；匯出 PDF | 😤 → 😐 | D+0 收到一封 email 後 6 天無任何引導；「加員工帳號」入口埋在設定第三層；PDF 匯出對 Chrome 有相容 bug | 設計 D+1/D+3/D+7 行為觸發 email；把「加員工」捷徑移至首頁；優先修 PDF bug |
| **Usage（付費後）** | 月結報表；會計師共享連結；客服信箱 | 月底跑月結；寄給外部會計師 | 😊 順暢 | 會計師「唯讀共享連結」功能幾乎無人知道（Support ticket 第 2 高頻）；月結報表格式與事務所 Excel 不符 | 月底前 D-3 推播「月結 Checklist」；功能發現改善 |
| **Advocacy** | Line 群；Google 評論；同業口碑 | （多數沉默） | 😐 普通 | NPS +18，體驗「還好」而非「超好」；無推薦誘因；轉介機制藏在深頁 | 推出「推薦一家送一個月」；NPS 9-10 分用戶 24 小時內自動觸發推薦邀請 |

---

### Step 3: 找出關鍵時刻（Moments of Truth）

1. **Trial 信用卡綁定（Decision 階段）**
   - 62% 流失集中在此（離場問卷數據）
   - 競品 KIPO、EZflow 均已提供免卡 Trial
   - 移除此摩擦是最高 ROI 的單一改動

2. **D+3 發出第一張發票（Usage Trial 初期）**
   - Hotjar 數據：D+3 前完成第一張發票者，Trial → Paid 轉換率 31%；未完成者僅 2%
   - 這是 **Activation Moment**，整個 Onboarding 應以「推動 Annie 在 D+3 前發出第一張發票」為核心目標

3. **第一次月底月結順利完成（Usage 付費後）**
   - 3 個月留存率 72% 的流失集中在第一個月底
   - 月結是「產品價值兌現時刻」——跑不順就直接 Churn

---

### Step 4: 優先改善排序

| 優先序 | Stage | 改善項目 | 預期影響 | 執行難度 |
|--------|-------|----------|----------|----------|
| P1 | Decision | 移除 Trial 信用卡綁定要求 | Trial 啟動量預估 +40%（競品參考） | 中（工程 + 帳務流程） |
| P2 | Usage Trial | 修 PDF 匯出 Chrome bug | 減少 30% 相關 ticket；直接影響 Activation | 低（已知 bug，工程評估 2 週） |
| P3 | Usage Trial | D+1/D+3/D+7 行為觸發 Onboarding Email（目標：推動發出第一張發票） | Activation Rate 預估 +15pp | 低（行銷自動化，2 週上線） |
| P4 | Usage 付費 | 月底 D-3「月結 Checklist」推播 + 會計師共享連結功能發現 | 3 個月留存率目標 72% → 80% | 低（in-app 通知 + Email） |
| P5 | Advocacy | 推薦計畫 + NPS 高分自動觸發邀請 | 有機獲客成本降低 | 中 |

---

## Result

```markdown
# Customer Journey Map: CloudForm — B2B 報帳 SaaS

## Persona
- Name: Annie
- Profile: 45 歲，製造業/貿易業財務主管，10-50 人公司帳務負責人
- Goal: 減少月底手工報帳作業，讓月結更順暢

## Journey Map

| Stage | Touchpoints | Actions | Emotion | Pain Points | Opportunities |
|-------|------------|---------|---------|-------------|---------------|
| Awareness | Google 搜尋、Line 群推薦 | 點搜尋結果、截圖給老闆 | 😊 有希望 | 廣告文案含技術術語，排名第 4 | 文案改「10 分鐘上線，不需 IT」 |
| Consideration | 官網、定價頁、YouTube | 看功能表、找適用方案 | 😐 猶豫 | 找不到「適合幾人公司」的引導 | 互動問卷引導選方案 |
| Decision | Trial 註冊、信用卡綁定 | 填表、猶豫綁卡 | 😤 卡住 | 需先綁卡（62% 在此流失） | 改為免卡 Trial（P1） |
| Usage Trial | Onboarding Email、產品 UI | 建第一張發票、加員工、匯出 PDF | 😤 → 😐 | D+1~D+6 無引導；PDF Chrome bug | 行為觸發 Email 序列；修 bug（P2/P3） |
| Usage 付費 | 月結報表、共享連結、客服 | 月底跑月結、寄會計師 | 😊 順暢 | 不知道共享連結；月結格式不符 Excel | D-3 月結 Checklist 推播（P4） |
| Advocacy | Line 群、Google 評論 | （多數沉默） | 😐 普通 | 無推薦誘因，NPS 僅 +18 | 推薦計畫 + NPS 自動觸發（P5） |

## Moments of Truth
1. **Trial 信用卡綁定** — 62% 流失在此，是 Trial 啟動的最大單一阻力
2. **D+3 發出第一張發票** — Activation Moment：完成者轉換率 31%，未完成者僅 2%
3. **第一次月底月結順利完成** — 產品價值兌現時刻，決定 Month 1 留存

## Priority Improvements
1. Decision → 移除 Trial 信用卡要求 — Impact: 高, Effort: 中
2. Usage Trial → 修 PDF Chrome 相容 bug — Impact: 高, Effort: 低
3. Usage Trial → D+1/D+3/D+7 行為觸發 Onboarding Email — Impact: 高, Effort: 低
4. Usage 付費 → 月底 D-3 月結 Checklist + 功能發現改善 — Impact: 中, Effort: 低
5. Advocacy → 推薦計畫上線 — Impact: 中, Effort: 中
```

**給 Vivian 的結論：**

Trial → Paid 8% 問題分三層：

| 層次 | 問題 | 解法 | 優先序 |
|------|------|------|--------|
| **進不來** | 信用卡摩擦，Trial 啟動率低 | 免卡 Trial | P1 |
| **活不起來** | D+3 前未完成 Activation | 行為 Email + 修 bug | P2/P3 |
| **第一個月結卡住** | 月底流失 | 月結 Checklist | P4 |

P1 + P2 + P3 合計工時約 6 週，預估可將 Trial → Paid 轉換率從 8% 提升至 **15-18%**，相當於每月新增 35-50 名付費用戶（月增收約 NT$34,000-49,000）。
```
