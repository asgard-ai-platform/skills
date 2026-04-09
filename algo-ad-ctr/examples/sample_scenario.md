# Example: 電商平台廣告排名模型 CTR 校準失準修復

## Scenario

**公司：** ShopWave（B2C 電商平台，月活 800 萬用戶）
**時間：** 2026 年 Q1

ShopWave 的廣告工程師 Iris 發現廣告收益在過去三週持續下滑 12%。排查後懷疑是 CTR 預測模型出了問題：模型預測的 pCTR 系統性偏高，導致高出價廣告的 Expected Value（EV = Bid × pCTR）被高估，劣質廣告擠掉了優質廣告。

Iris 的問題：
> 「我的 GBDT 模型 AUC 還有 0.79，看起來不錯，但廣告主在抱怨 ROI 變差。Platt scaling 有做，但我不確定校準是否真的有效。怎麼驗證？」

已有資料：
- 過去 30 天 2,000 萬筆 impression log（含 click label）
- 模型版本：GBDT，上次重訓時間為 45 天前
- 模型輸出：每筆 impression 的 pCTR（0~1 浮點數）
- 實際整體 CTR：1.8%

---

## Analysis

### Phase 1：輸入驗證

| 檢查項目 | 狀態 |
|---------|------|
| 樣本量（需 100K+） | ✅ 2,000 萬筆 |
| Click label 完整性 | ✅ 無缺漏 |
| 資料洩漏風險 | ⚠️ 待確認 feature leakage |
| 模型新鮮度 | ❌ 45 天前訓練，距今過長 |

**發現 1：** GBDT 模型已 45 天未重訓。ShopWave 的廣告組合在農曆新年促銷後出現大幅輪替，新廣告的 ad category 分布已與訓練資料不同。

**發現 2：** Feature audit 時發現 `ad_historical_ctr_7d`（該廣告過去 7 天 CTR）在訓練與推論時都使用同一時間窗口計算，**訓練集沒有嚴格 time-based split**，存在 feature leakage。

---

### Phase 2：校準診斷

將 2,000 萬筆 impression 依 pCTR 分成 10 個十分位桶（decile），比較每桶的 predicted CTR vs. actual CTR：

| Decile | Predicted pCTR (avg) | Actual CTR | Ratio (pred/actual) |
|--------|---------------------|------------|---------------------|
| 1（最低）| 0.003 | 0.004 | 0.75 |
| 2 | 0.007 | 0.008 | 0.88 |
| 3 | 0.012 | 0.013 | 0.92 |
| 4 | 0.018 | 0.017 | 1.06 |
| 5 | 0.025 | 0.021 | 1.19 |
| 6 | 0.034 | 0.026 | 1.31 |
| 7 | 0.048 | 0.033 | 1.45 |
| 8 | 0.071 | 0.046 | 1.54 |
| 9 | 0.110 | 0.067 | 1.64 |
| 10（最高）| 0.198 | 0.108 | 1.83 |

**結論：** 校準嚴重失準，且越高分段越嚴重。低分廣告略微低估，高分廣告被高估近 2 倍。這正是高出價廣告的 EV 被系統性高估的根源。

> **IRON LAW 違反確認：** AUC = 0.79（排序能力正常），但 ECE（Expected Calibration Error）高達 0.031，遠超可接受閾值 0.01。Platt scaling 雖有執行，但是在 45 天前的資料上擬合，已過期失效。

---

### Phase 3：修復方案

**修復一：立即重訓 Platt scaling**

用最近 7 天的 holdout set（佔最近 14 天資料的後半段）重新擬合 Platt scaling 參數：

```
原始 Platt: σ(A·f(x) + B)，A=0.91, B=-0.02（45 天前）
重新擬合後: A=0.74, B=-0.08
```

重新校準後的 decile 對比：

| Decile | Predicted pCTR (recalibrated) | Actual CTR | Ratio |
|--------|------------------------------|------------|-------|
| 10（最高）| 0.112 | 0.108 | 1.04 |
| 7 | 0.035 | 0.033 | 1.06 |
| 3 | 0.013 | 0.013 | 1.00 |

ECE 降至 0.006，符合標準。

**修復二：修正 feature leakage**

`ad_historical_ctr_7d` 改為在訓練時使用 `[t-14, t-7]` 窗口（相對於當筆 impression 時間戳），確保不包含未來資訊。預計 AUC 會從 0.79 微降至 0.76，但校準品質更可靠。

**修復三：建立每日重訓 pipeline**

模型新鮮度 SLA：不超過 7 天。

---

### Phase 4：修復後驗證

對 2026-03-28 的 100 萬筆 impression 做回測：

**修復前 EV 計算（問題版本）：**
```
廣告 A: Bid=50元, pCTR=0.11 → EV=5.5  ← 贏得競標（pCTR 高估）
廣告 B: Bid=80元, pCTR=0.06 → EV=4.8
```

**修復後 EV 計算：**
```
廣告 A: Bid=50元, pCTR=0.058 → EV=2.9
廣告 B: Bid=80元, pCTR=0.059 → EV=4.7  ← 廣告 B 應贏（實際 CTR 相近，出價更高）
```

廣告主 ROI 模擬：修復後廣告 B 類型（高出價、中等 CTR）的展示量預期回升 23%。

---

## Result

```json
{
  "prediction": {
    "ctr": 0.058,
    "confidence_interval": [0.051, 0.065]
  },
  "top_features": [
    {"feature": "query_ad_match",      "importance": 0.34},
    {"feature": "ad_historical_ctr_7d","importance": 0.28},
    {"feature": "position_1",          "importance": 0.19},
    {"feature": "user_is_mobile",      "importance": 0.11},
    {"feature": "ad_category_match",   "importance": 0.08}
  ],
  "metadata": {
    "model": "gbdt",
    "auc": 0.76,
    "log_loss": 0.19,
    "calibration_error": 0.006
  }
}
```

**行動清單（Iris 的 next steps）：**

1. **立即（今天）：** 用最近 7 天 holdout 重新擬合 Platt scaling，hotfix 部署
2. **本週：** 修正 `ad_historical_ctr_7d` 的 time-based split，重新全量訓練 GBDT
3. **下週：** 建立每日重訓 + ECE 監控 dashboard，ECE > 0.01 自動告警
4. **持續：** 加入 position bias 修正（IPW 或 DLA），避免 position 1 廣告的 CTR 被高估

> **核心教訓：** AUC 高不代表校準正確。在 EV-based 競標系統中，校準誤差直接等於出價誤差，會改變競標結果。每次 CTR 模型更新後，Platt scaling 也必須一起更新。
