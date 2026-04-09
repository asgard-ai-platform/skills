# Example: 家居品牌從手動 CPC 轉換至 Target CPA

## Scenario

**公司：** 居家生活電商 HomePlus（台灣本地品牌，年營收約 NT$8,000 萬）

**廣告帳戶狀況（2026 年 3 月）：**
- 平台：Google Ads，搜尋廣告為主
- 預算：NT$150,000 / 月
- 目前策略：手動 CPC，平均出價 NT$12–35（依關鍵字分組）
- 月轉換數：112 筆（追蹤事件：完成結帳）
- 目前平均 CPA：NT$580
- 目標 CPA：NT$500（行銷主管設定的 KPI）
- 轉換追蹤：Google Ads Tag + GA4 匯入，已驗證無重複計算

**使用者問題：**
> 我們手動出價很費時，帳戶有 112 筆月轉換，想改用自動出價。Target CPA 設多少合適？什麼時候可以切？切完要觀察哪些指標？

---

## Analysis

### Phase 1：Input Validation

| 檢核項目 | 數值 | 判斷 |
|----------|------|------|
| 月轉換數 | 112 筆 | ✅ 超過 50 筆門檻，可用 Target CPA |
| 轉換追蹤準確性 | Google Tag + GA4 驗證通過 | ✅ 資料品質可信 |
| 有無收益資料 | 有（結帳金額），但各 SKU 差異大 | Target ROAS 可考慮，但先以 CPA 穩定基線 |
| 業務目標 | 降低 CPA（580→500）+ 維持量 | 效率優先 → Target CPA 適合 |
| 月預算 | NT$150,000 | CPA 目標 NT$500 → 理論最大量：300 筆；目前量 112 筆，預算非瓶頸 |

**Gate 通過：** 轉換資料充足、追蹤正確、策略選擇明確。

---

### Phase 2：Core Algorithm 應用

**策略選擇：Target CPA**

依 Iron Law 數據門檻：
- 112 conv/month >> 50 門檻 → Target CPA 可用
- 有收益資料 → 未來可升級 Target ROAS，但目前 SKU 均價差異（NT$800–NT$4,500）會讓 ROAS 目標難以設定，先以 CPA 控制效率

**Target CPA 初始值設定：**

不應直接設目標值 NT$500（過於激進），應從當前表現開始緩步收斂：

```
初始 Target CPA = 當前 CPA × 1.0 ~ 1.1
              = NT$580 × 1.05
              = NT$609（建議設 NT$600）
```

原因：演算法在學習期需要足夠的拍賣空間找到轉換，若目標設得比現況低 14%，學習期曝光量會大幅萎縮，難以蒐集足夠訊號。

**收斂計畫（3 個月）：**

| 時段 | Target CPA | 預期操作 |
|------|------------|----------|
| 第 1–2 週（學習期） | NT$600 | 禁止調整，僅監控 |
| 第 3–4 週 | NT$575 | 學習期結束後，若 CPA < NT$600 則降 |
| 第 5–8 週 | NT$530 | 穩定後再收斂 |
| 第 9–12 週 | NT$500 | 達成 KPI 目標 |

**出價邏輯（Target CPA 運作方式）：**

每次拍賣，演算法根據以下訊號預測轉換機率（P_conv）：
- 使用者裝置、時段、地點
- 搜尋意圖（查詢語意）
- 受眾屬性（再行銷清單、相似受眾）
- 歷史互動行為

出價公式：
```
bid = Target CPA × P_conv
    = NT$600 × P_conv

高意圖用戶（P_conv = 0.08）→ bid = NT$48
低意圖用戶（P_conv = 0.01）→ bid = NT$6
```

目標：跨所有拍賣平均 CPA 趨近 NT$600。

---

### Phase 3：Verification 指標

學習期（前 14 天）監控清單：

| 指標 | 基準值 | 警戒線 | 行動 |
|------|--------|--------|------|
| 日轉換數 | ~3.7 筆/天 | < 1 筆/天連續 5 天 | 檢查預算是否限制、CPA 是否過緊 |
| 曝光份額 | （切換前記錄） | 下降 > 40% | Target CPA 可能過低，暫緩調降 |
| 實際 CPA | NT$580 | > NT$800 | 學習期波動允許，超過才介入 |
| 轉換追蹤正常 | 每日有數據 | 連續 2 天 0 轉換 | 立即查 Tag 是否失效 |

**Gate：** 第 14 天後，若實際 CPA 落在 NT$480–720（目標 ±20%），視為學習期通過。

---

### Gotchas 應對（本案適用）

1. **學習期波動**：告知行銷主管第 1–2 週 CPA 可能飆至 NT$800+，這是正常現象，不要在此期間更動目標值。

2. **轉換延遲**：HomePlus 分析顯示，消費者平均在點擊後 1.8 天完成購買。Google Ads 轉換窗口應設為 **30 天**（非預設 7 天），確保演算法拿到完整訊號。

3. **預算非瓶頸**：目前 112 筆 × NT$580 = NT$64,960 實際花費，遠低於 NT$150,000 預算。Target CPA 不會因預算充裕就放量——它只在找得到符合 CPA 目標的拍賣時才出價。勿期待切換後花費自動倍增。

4. **季節性衝擊**：6 月父親節、雙 11 前後，競價環境劇變。需提前在 Google Ads 設定**季節性調整（Seasonality Adjustment）**，避免演算法誤判。

---

## Result

```json
{
  "recommendation": {
    "strategy": "target_cpa",
    "target": 600,
    "currency": "TWD",
    "confidence": "high",
    "rationale": "112 conv/month exceeds 50-conversion threshold; start at NT$600 (current CPA x1.05) to preserve learning signal, then step down to NT$500 over 12 weeks"
  },
  "expected_performance": {
    "cpa_range": [480, 720],
    "volume_change": "-5% to +20%",
    "note": "Volume may dip during 14-day learning period before recovering"
  },
  "convergence_plan": {
    "week_1_2": {"target_cpa": 600, "action": "freeze — learning period"},
    "week_3_4": {"target_cpa": 575, "action": "reduce if actual CPA < 600"},
    "week_5_8": {"target_cpa": 530, "action": "reduce if stable"},
    "week_9_12": {"target_cpa": 500, "action": "KPI target reached"}
  },
  "metadata": {
    "monthly_conversions": 112,
    "current_cpa": 580,
    "learning_period_days": 14,
    "conversion_window_recommended_days": 30,
    "budget_monthly_twd": 150000,
    "budget_is_binding": false
  }
}
```

**切換時機建議：** 避開促銷檔期（如雙 11、節慶），選在流量平穩的週二或週三上午切換，以確保學習期資料不被異常流量污染。
