# Example: 電商品牌新品上市後的社群情緒監測

## Scenario

**背景：** TrendKit（台灣中型運動用品電商）於 2026-03-15 推出新款無線耳機「TrendKit AirFlow Pro」，上市後一週內收到大量社群反應。行銷團隊從 Twitter/X 和 Dcard 爬取了 450 則留言，想在週一晨會前量化情緒分佈，判斷是否需要緊急公關應對。

**使用者問題：** 「這些留言整體是正面還是負面？有沒有哪個議題特別拉低評分？」

**原始資料樣本（450 則中的代表性摘錄）：**

```
[1]  "AirFlow Pro 音質真的超棒！戴一整天耳朵不痛 👍👍"
[2]  "連線一直斷，退貨!!!"
[3]  "還可以啦，沒特別驚艷"
[4]  "AMAZING sound quality for the price 😍"
[5]  "Oh great, another earphone that dies in 3 hours 🙄"
[6]  "不難用但不值這個價"
[7]  "降噪功能完全沒用 垃圾"
[8]  "配戴感超舒服！通勤必備"
[9]  "充電盒做工太差，塑膠感很重"
[10] "性價比算高啦，推薦給預算有限的人"
```

---

## Analysis

### Phase 1: Input Validation

- 共 450 則文字，混合繁體中文與英文。
- **注意：VADER 為英文設計**。中文留言需前處理：將常見中文情緒詞翻譯或標記後再送入 VADER，或分流處理（中文用 SnowNLP，英文用 VADER）。
- 本案採**分流策略**：英文或含英文關鍵字的留言走 VADER；純中文留言走 SnowNLP，最後合併結果。
- 過濾空白留言：0 則。Gate ✓

---

### Phase 2: Core Algorithm（VADER 對英文/混合留言）

以上 10 則為例，標記語言後處理：

| # | 語言判定 | 工具 | compound | label |
|---|---------|------|----------|-------|
| 1 | 中文為主 | SnowNLP | +0.72 | positive |
| 2 | 中文 | SnowNLP | −0.61 | negative |
| 3 | 中文 | SnowNLP | +0.08 | neutral |
| 4 | 英文 | VADER | +0.87 | positive |
| 5 | 英文 | VADER | +0.34 | **positive** ⚠️ |
| 6 | 中文 | SnowNLP | −0.22 | negative |
| 7 | 中文 | SnowNLP | −0.78 | negative |
| 8 | 中文 | SnowNLP | +0.65 | positive |
| 9 | 中文 | SnowNLP | −0.31 | negative |
| 10 | 中文 | SnowNLP | +0.41 | positive |

**留言 [5] Sarcasm 陷阱：**
> "Oh great, another earphone that dies in 3 hours 🙄"

VADER 看到 "great" → compound = +0.34，判為正面。但語意明顯負面（諷刺）。VADER 無法偵測反諷，此類留言需人工抽樣複查。

---

### Phase 3: Verification（全量 450 則）

**人工 spot-check（隨機抽 20 則）：**
- 18 則分類與人工判斷一致
- 2 則誤判（均為英文諷刺句，結構為 "great/perfect + 負面結果"）
- 準確率 90%，超過 80% 門檻 → Gate ✓

**議題分群（關鍵詞 TF-IDF 後人工標記）：**

| 議題 | 留言數 | 平均 compound |
|------|--------|--------------|
| 音質 / 降噪 | 112 | +0.58 |
| 配戴舒適度 | 89 | +0.61 |
| 藍牙連線穩定 | 74 | **−0.52** |
| 電池續航 | 68 | **−0.41** |
| 充電盒做工 | 43 | −0.28 |
| 性價比 | 64 | +0.33 |

---

### Phase 4: Output

```json
{
  "results_sample": [
    {"text": "AMAZING sound quality for the price 😍", "compound": 0.87, "pos": 0.65, "neu": 0.35, "neg": 0.0, "label": "positive"},
    {"text": "Oh great, another earphone that dies in 3 hours 🙄", "compound": 0.34, "pos": 0.28, "neu": 0.72, "neg": 0.0, "label": "positive"},
    {"text": "連線一直斷，退貨!!!", "compound": -0.61, "pos": 0.0, "neu": 0.22, "neg": 0.78, "label": "negative"}
  ],
  "metadata": {
    "texts_analyzed": 450,
    "date_range": "2026-03-15 to 2026-03-21",
    "distribution": {
      "positive": 0.48,
      "neutral": 0.22,
      "negative": 0.30
    },
    "overall_compound_mean": 0.14,
    "sarcasm_suspected": 11,
    "language_split": {"chinese_snowNLP": 318, "english_vader": 132}
  }
}
```

---

## Result

**整體情緒：偏正面，但有明確痛點**

- 48% 正面、22% 中立、30% 負面；整體 compound 均值 +0.14，屬於「溫和正面」。
- **音質與配戴舒適**是口碑亮點（compound 均值 > +0.58）。
- **藍牙連線穩定性**是最大拉力（compound −0.52），74 則負評集中於「斷線」、「延遲」，建議工程團隊優先查韌體版本。
- **電池續航**為次要痛點（compound −0.41），68 則提及「3 小時就沒電」，與官方宣稱 8 小時出入明顯，需公關釐清。
- 發現 11 則疑似諷刺留言被誤判為正面，已標記供公關人員人工複查。

**建議行動：**
1. 本週發布韌體更新說明，主動回應藍牙斷線問題。
2. 公關稿澄清電池續航測試條件（音量、降噪開啟與否）。
3. 每日跑一次情緒監測，追蹤韌體更新後負評比例是否下降。
