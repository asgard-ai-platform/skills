# Example: 台灣保健食品品牌 — 降低 Meta Ads CPA、提升整體 ROAS

## Scenario

**Vitazen 台灣**（中型保健食品電商，月營業額約 NT$1,800,000）的行銷主管 Christine 找上 Asgard，提出以下問題：

> 「我們每個月在 Meta 和 Google 各投約 NT$120,000，總共 NT$240,000 廣告費。上個月 ROAS 只有 2.1x，公司要求要到 3x。我知道哪些廣告『看起來不錯』，但 CPA 卻一直降不下來。我不知道問題在哪裡。」

她提供的數據（2026 年 3 月）：

| 平台 | 月預算 | 花費 | 轉換數 | CPA | 營收 | ROAS |
|------|--------|------|--------|-----|------|------|
| Google Search | NT$80,000 | NT$78,500 | 41 | NT$1,915 | NT$193,000 | 2.46x |
| Meta (FB/IG) | NT$120,000 | NT$118,200 | 38 | NT$3,111 | NT$152,000 | 1.29x |
| **合計** | NT$200,000 | NT$196,700 | 79 | NT$2,490 | NT$345,000 | 1.75x |

> 補充說明：平均客單價 NT$4,350。目標 CPA ≤ NT$1,450，目標 ROAS ≥ 3x。

---

## Analysis

### Phase 1: Audit Current Performance

**Google Search — 初步健診**

Christine 分享 Search Terms Report，發現：
- Top spend 關鍵字：「維生素 C」「葉黃素推薦」「膠原蛋白哪個好」
- 「維生素 C」貢獻 32% 花費，但轉換率只有 0.8%（品類詞，非品牌意圖）
- 「葉黃素推薦」CPA NT$890，表現最佳
- 搜尋詞中出現大量「免費」「副作用」「評測」等資訊型查詢，但都導入購買頁

Quality Score 平均 5/10，主因：廣告文案強調「免運」但 landing page 首屏沒有呈現。

**Meta Ads — 初步健診**

- 主力受眾：台灣女性 25-55 歲，興趣「健康」「美容保養」（冷受眾）
- 廣告組合（Ad Sets）：4 個，每組預算 NT$30,000
- 唯一使用的素材：同一張產品棚拍靜態圖，已上線 9 週
- 頻率（Frequency）：6.2（同一人平均看到 6.2 次）→ 嚴重 creative fatigue
- 無 retargeting 受眾，無 Lookalike

**核心診斷**：

| 問題 | 平台 | 嚴重程度 |
|------|------|----------|
| Creative fatigue（素材 9 週未換） | Meta | 🔴 高 |
| 冷受眾無分層，缺 retargeting | Meta | 🔴 高 |
| 品類詞吃掉預算但不轉換 | Google | 🟡 中 |
| 廣告承諾與 landing page 不一致 | Google | 🟡 中 |
| 無跨平台 UTM 追蹤，ROAS 各算各的 | 全部 | 🟡 中 |

---

### Phase 2: Quick Wins（Week 1–2）

**Google Search**

1. **加負面關鍵字**：排除「免費」「副作用」「評測」「PTT」「dcard」等資訊型詞，預計省下約 NT$12,000/月浪費花費
2. **降低「維生素 C」出價 50%**：從廣泛匹配改為精確匹配，避免雜訊流量
3. **修正 landing page**：首屏加入「全館滿 NT$1,500 免運費」banner，與廣告文案呼應 → 預期 Quality Score 回升至 7

**Meta Ads**

1. **立即暫停頻率 > 5 的廣告組合**：停止對疲勞受眾繼續曝光
2. **上線 2 支新素材**：顧客使用情境短影片（15 秒）、UGC 風格靜態圖，取代棚拍
3. **新增 Retargeting 廣告組合**：對「過去 30 天瀏覽產品頁但未購買」受眾投放，預算 NT$20,000/月

---

### Phase 3: Structural Improvements（Week 3–4）

**Meta 受眾分層架構重建**

```
冷受眾 (Cold)    — NT$60,000   興趣受眾 + 1% Lookalike（以過去購買名單為種子）
暖受眾 (Warm)    — NT$20,000   過去 60 天網站訪客、IG 互動用戶
熱受眾 (Hot)     — NT$20,000   加購未結帳、產品頁訪客 30 天
既有客戶 (Loyal) — NT$10,000   過去購買名單，推薦補貨 / 新品
```

**Google 帳戶結構調整**

- 新增「品牌詞」獨立 Campaign：`Vitazen` 關鍵字，獨立預算 NT$8,000，防止競爭對手截流
- 「葉黃素推薦」「葉黃素功效」等高意圖關鍵字獨立 Ad Group，放大預算至 NT$25,000
- Bidding 由 Manual CPC 切換為 **Target CPA NT$1,200**（現有 41 次轉換，剛好達到門檻，可開始用智慧出價）

---

### Phase 4: Scaling Roadmap（Month 2+）

若 Week 3-4 後 CPA 確認達標：
- Google 預算 +20%：NT$80,000 → NT$96,000
- Meta Lookalike 受眾擴展至 2%、3%
- 評估加入 LINE LAP：Vitazen 主力客群為 35-55 歲女性，LINE 觸及率高於 Facebook 同族群

---

## Result

# Ad Optimization Report: Vitazen Taiwan — 2026-03

## Performance Summary（現況 vs. 目標）

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Spend | NT$196,700/month | NT$200,000 | — |
| CPA | NT$2,490 | NT$1,450 | 🔴 |
| ROAS | 1.75x | 3.0x | 🔴 |
| CVR (Meta) | 0.9% | 2.5% | 🔴 |
| CVR (Google) | 1.8% | 3.0% | 🟡 |

## Top Performing

| Campaign/Ad | CPA | ROAS | Action |
|------------|-----|------|--------|
| Google — 葉黃素高意圖 Ad Group | NT$890 | 4.9x | Scale +20%，獨立 Campaign |
| Google — 品牌詞（新增） | NT$420（預估） | 10x+ | 設定 NT$8,000 保護預算 |

## Underperforming

| Campaign/Ad | CPA | Issue | Action |
|------------|-----|-------|--------|
| Meta — 冷受眾靜態棚拍（9 週） | NT$3,890 | Creative fatigue，頻率 6.2 | 立即暫停 |
| Google — 「維生素 C」廣泛匹配 | NT$4,200 | 品類意圖，非購買意圖 | 改精確匹配，降價 50% |
| Meta — 無 retargeting 受眾 | 無資料 | 結構缺失 | 新增 Hot 受眾 NT$20,000 |

## Optimization Plan

| Priority | Action | Expected Impact | Timeline |
|----------|--------|----------------|----------|
| 1 | Meta 上線新素材（短影片 + UGC） | CPA -40%，回到 NT$1,900 | Week 1 |
| 2 | Google 加負面關鍵字，省浪費花費 | 省 NT$12,000/月 | Week 1 |
| 3 | Meta 新增 Retargeting 受眾分層 | CVR +120%（熱受眾） | Week 2 |
| 4 | Google 切換 Target CPA NT$1,200 | CPA -25% | Week 3 |
| 5 | 葉黃素 Campaign 預算 +20% | 轉換數 +8 | Week 4 |
| 6 | LINE LAP 評估測試（35-55 女性） | 新平台觸及 | Month 2 |

**預估 Month 2 成果**（若優化順利執行）：
- CPA：NT$2,490 → NT$1,380（-45%）
- ROAS：1.75x → 3.2x（達標）
- 月轉換數：79 → 145（+84%）

> ⚠️ **注意**：Google 切換 Target CPA 後，需給予 2-3 週學習期（learning phase），期間轉換量可能短暫下降 15-20%，不要在學習期內再次調整出價或預算，否則重置學習。
