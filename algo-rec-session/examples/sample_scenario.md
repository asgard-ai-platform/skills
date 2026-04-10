# Example: 運動用品電商匿名瀏覽者的即時 Next-Item 推薦

## Scenario

**公司：** SportZone Taiwan（運動用品電商）  
**情境：** 一位未登入的訪客在手機上瀏覽了約 8 分鐘，點了幾個跑步相關頁面。前端工程師需要在使用者停留在商品頁時，於右側欄即時顯示「你可能也會看」推薦模組。

**使用者問法：**
> 我有一個 anonymous session，sequence 是 `[category_running, product_brooks_ghost, product_asics_gel_kayano, product_socks_dryfit]`，用 Markov 算出來的 next item 是什麼？目前 transition matrix 從過去 30 天的 session log 訓練出來。

---

## Analysis

### Phase 1：Input Validation

原始 session（session_id: `anon_5f3a1c`）：

| 順序 | 事件 | timestamp |
|------|------|-----------|
| 1 | `category_running` | 14:02:11 |
| 2 | `product_brooks_ghost` | 14:03:45 |
| 3 | `product_asics_gel_kayano` | 14:05:22 |
| 4 | `product_socks_dryfit` | 14:09:58 |

- Session 長度 = 4（≥ 3，通過 gate）
- 間距最大 4 分 36 秒，遠低於 30 分鐘 timeout，屬同一 session
- 無重複商品，意圖連貫：跑步類別 → 高端跑鞋 → 功能性配件

**Iron Law 警示：** 前兩次點擊（`category_running` → `product_brooks_ghost`）已確立 session 意圖為「高端跑鞋購買評估」，後續 `socks_dryfit` 是配件，不代表意圖轉移——應以跑鞋序列為主信號。

---

### Phase 2：Core Algorithm（Markov Order-2）

從 30 天 session log（共 142,000 sessions）建出的 2-階 transition matrix，取最後兩個 item 作為條件：

**查詢 key：** `(product_asics_gel_kayano, product_socks_dryfit)`

從 transition matrix 撈出以此 bigram 結尾的後繼 item 分佈：

| next_item | count | P(next \| bigram) |
|-----------|-------|-------------------|
| `product_nike_zoom_vomero` | 412 | 0.31 |
| `product_insole_superfeet` | 287 | 0.22 |
| `product_asics_gel_nimbus` | 201 | 0.15 |
| `product_running_shorts` | 178 | 0.13 |
| `product_brooks_adrenaline` | 134 | 0.10 |
| (其他) | 122 | 0.09 |

**Position bias 修正：** 歷史資料中 `product_nike_zoom_vomero` 長期排在搜尋結果第 1 位，原始 count 高估。套用 IPS（Inverse Propensity Score）修正後 P 從 0.31 → 0.26。

**修正後最終排序：**

| next_item | 修正後 score |
|-----------|-------------|
| `product_insole_superfeet` | 0.24 |
| `product_nike_zoom_vomero` | 0.26 → 修正 0.22 |
| `product_asics_gel_nimbus` | 0.15 |
| `product_brooks_adrenaline` | 0.11 |
| `product_running_shorts` | 0.10 |

> 注意：`product_insole_superfeet`（鞋墊）排名上升，符合「高端跑鞋 + 跑步配件」的 session 模式——購買高端跑鞋的使用者常同時評估鞋墊。

---

### Phase 3：Verification

以相同 30 天 log 的最後 7 天做 leave-one-out 評估（隱藏各 session 最後一個 item）：

| Metric | 本模型（Order-2 Markov + IPS） | Baseline（Popularity） |
|--------|-------------------------------|----------------------|
| Hit@10 | 0.38 | 0.21 |
| Hit@20 | 0.49 | 0.31 |
| MRR@20 | 0.19 | 0.08 |

Hit@20 = 0.49，顯著高於 random baseline（約 0.05）及 popularity baseline，通過 gate。

---

## Result

```json
{
  "predictions": [
    {
      "item_id": "product_insole_superfeet",
      "score": 0.24,
      "based_on": "last_2_clicks"
    },
    {
      "item_id": "product_nike_zoom_vomero",
      "score": 0.22,
      "based_on": "last_2_clicks"
    },
    {
      "item_id": "product_asics_gel_nimbus",
      "score": 0.15,
      "based_on": "last_2_clicks"
    },
    {
      "item_id": "product_brooks_adrenaline",
      "score": 0.11,
      "based_on": "last_2_clicks"
    },
    {
      "item_id": "product_running_shorts",
      "score": 0.10,
      "based_on": "last_2_clicks"
    }
  ],
  "session": {
    "length": 4,
    "items_viewed": [
      "category_running",
      "product_brooks_ghost",
      "product_asics_gel_kayano",
      "product_socks_dryfit"
    ]
  },
  "metadata": {
    "method": "markov_order2",
    "position_bias_correction": "IPS",
    "hit_rate_at_20": 0.49,
    "mrr_at_20": 0.19,
    "training_window_days": 30,
    "session_timeout_min": 30
  }
}
```

**前端呈現建議：** 顯示前 3 筆（`insole_superfeet`、`nike_zoom_vomero`、`asics_gel_nimbus`）；若 `asics_gel_kayano` 已在畫面上，自動去重，補入第 4 名。Cold-start 保護：若任何推薦 item 在過去 7 天上架為新品（零 session 紀錄），以同類別熱銷品替換。
