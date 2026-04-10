# Example: 台灣戶外裝備平台搜尋排名重建

## Scenario

**公司：** OutdoorHub TW（台灣中型戶外運動電商，月搜尋量約 180 萬次）
**時間：** 2026 年 Q1

工程師 Jenny 找上你：

> 「我們的搜尋現在只用 BM25，搜『登山背包 40L』排第一的是一個庫存剩 2 件、評價只有 12 則、三年沒更新的老商品。明明有幾個新品 CTR 和加購率都比它高，卻排在第 8、9 頁。老闆說這季要做 learning-to-rank，但我不確定從哪裡開始，手上有 90 天的點擊與購買 log。」

現有資料：
- 點擊 log：90 天，約 2.2M 筆曝光紀錄
- 轉換 log：同期，約 68K 筆訂單
- 商品總數：約 42,000 SKU
- 現有欄位：BM25 分、品牌、類別、價格、評分、評論數、庫存狀態、上架日期

---

## Analysis

### Phase 1：Input Validation — 確認前置條件

**30 天最低門檻檢查：**

| 指標 | 門檻 | 現狀 | 通過？ |
|------|------|------|--------|
| 點擊 log 天數 | ≥ 30 天 | 90 天 | ✅ |
| 曝光筆數 | ≥ 100K | 2.2M | ✅ |
| 轉換筆數 | ≥ 5K | 68K | ✅ |
| 特徵覆蓋率 | ≥ 80% SKU 有完整特徵 | 評論數缺失率 22% | ⚠️ 需填補 |

**評論數缺失的處理：** 缺失值以同類別中位數填補（登山背包類 = 34 則），並新增 `has_reviews` 布林特徵，讓模型自行學習缺失的影響。

**Gate 通過：** 資料量足夠進入 LTR pipeline。

---

### Phase 2：Core Algorithm

#### Step 1 — Rule-Based Baseline（先上線，作為 A/B 對照組）

手動調校權重，快速取代純 BM25：

```
score_baseline = 0.40 × bm25_norm
              + 0.25 × ctr_30d_norm
              + 0.20 × rating_norm
              + 0.10 × review_count_norm
              + 0.05 × recency_norm
```

- `bm25_norm`：BM25 分 min-max 正規化至 [0, 1]
- `ctr_30d_norm`：過去 30 天在該 query 下的點擊率，平滑處理（貝葉斯平均，先驗 = 類別均值）
- `recency_norm`：上架 < 90 天得 1.0，> 365 天得 0.2，線性內插

**庫存規則（hard filter，不進入分數）：**
- 庫存 = 0：直接移除
- 庫存 ≤ 3：降 3 名

---

#### Step 2 — LTR 訓練資料建構

從 90 天曝光/點擊 log 建立 (query, product, label) 三元組：

| 事件類型 | 標籤值 | 備註 |
|----------|--------|------|
| 購買 | 3 | 最強正訊號 |
| 加入購物車 | 2 | 中等正訊號 |
| 點擊 | 1 | 弱正訊號 |
| 曝光但未點擊 | 0 | 負訊號 |

**Position Debiasing（這是最常被跳過的關鍵步驟）：**

BM25 舊排名下，位置 1 的商品天然獲得更多點擊，與商品品質無關。不處理的話，模型只會學到「舊模型排第一的東西應該繼續排第一」——也就是 Jenny 描述的問題根源。

```python
# Inverse Propensity Weighting
# propensity[k] = 估計在位置 k 被點擊的機率（與內容無關）
# 從 pair-wise AB 實驗或 result randomization 估計
sample_weight = 1.0 / propensity[position]
```

OutdoorHub 沒有 randomization 實驗的歷史資料。替代方案：用 **examination propensity model**（假設 propensity ∝ 1/log(1+position)）作為近似估計，並在下一季跑 10% 流量的結果隨機化實驗取得真實估計值。

---

#### Step 3 — 特徵工程（每個 query-product pair）

```
文字匹配類：
  - bm25_score（BM25 原始分）
  - title_exact_match（query term 是否完整出現在標題）
  - brand_match（query 是否提到品牌名）

行為訊號類：
  - ctr_7d, ctr_30d, ctr_90d（三個時間窗口）
  - add_to_cart_rate_30d
  - conversion_rate_30d（含貝葉斯平滑）

商品品質類：
  - avg_rating
  - review_count（log 轉換）
  - has_reviews

商業訊號類：
  - price_rank_in_category（類別內價格分位數）
  - inventory_level（分箱：0/1-5/6-20/20+）
  - days_since_listed（新品加成）
```

---

#### Step 4 — LambdaMART 訓練

```python
import lightgbm as lgb

params = {
    "objective": "lambdarank",
    "metric": "ndcg",
    "ndcg_eval_at": [5, 10],
    "num_leaves": 63,
    "learning_rate": 0.05,
    "n_estimators": 500,
    "min_child_samples": 20,   # 防止低曝光 query 過擬合
}

model = lgb.LGBMRanker(**params)
model.fit(
    X_train, y_train,
    group=train_query_sizes,
    sample_weight=ipw_weights,   # position debiasing
    eval_set=[(X_val, y_val)],
    eval_group=[val_query_sizes],
)
```

訓練集：前 75 天；驗證集：後 15 天（依時間切割，避免資料洩漏）

---

#### Step 5 — 商業 Boost 混合

```
final_score = 0.85 × ltr_score_norm + 0.15 × business_boost
```

`business_boost` 組成：
- 毛利率 > 35%：+0.05
- 品牌廣告合約（sponsored）：+0.10，並在結果頁標示「贊助」
- 當季新品（< 30 天）：+0.03

> **注意：** Sponsored 結果必須與 organic 明確隔離標示，避免用戶信任損耗。

---

### Phase 3：Verification

**Offline 評估（驗證集 15 天）：**

| 指標 | BM25 Baseline | Rule-Based | LambdaMART |
|------|---------------|------------|------------|
| NDCG@5 | 0.51 | 0.61 | 0.71 |
| NDCG@10 | 0.48 | 0.58 | 0.68 |
| MRR | 0.44 | 0.55 | 0.64 |

LambdaMART 相對 BM25 提升 NDCG@10 +41.7%，通過 Gate。

**計畫 A/B Test（上線後 2 週）：**
- 對照組：BM25（30% 流量）
- 實驗組 A：Rule-Based（30% 流量）
- 實驗組 B：LambdaMART（40% 流量）
- 主要指標：每次搜尋的 GMV（revenue per search）
- 次要指標：CTR@5、轉換率、搜尋後跳出率

---

## Result

### 排名輸出範例

查詢：`"登山背包 40L"`

```json
{
  "results": [
    {
      "product_id": "P00841",
      "rank": 1,
      "final_score": 0.89,
      "components": {
        "relevance": 0.82,
        "popularity": 0.91,
        "quality": 0.88
      }
    },
    {
      "product_id": "P02203",
      "rank": 2,
      "final_score": 0.84,
      "components": {
        "relevance": 0.90,
        "popularity": 0.74,
        "quality": 0.85
      }
    },
    {
      "product_id": "P00117",
      "rank": 3,
      "final_score": 0.79,
      "components": {
        "relevance": 0.78,
        "popularity": 0.80,
        "quality": 0.81
      }
    }
  ],
  "metadata": {
    "query": "登山背包 40L",
    "model": "lambdamart",
    "ndcg_at_10": 0.68,
    "total_candidates": 312,
    "out_of_stock_removed": 18
  }
}
```

舊的 BM25 第一名（P00553，庫存 2 件、12 則評論）已降至第 19 名；原先被埋在第 8 頁的 P00841（CTR 0.14、加購率 0.08）升至第 1 名。

### 給 Jenny 的後續行動清單

1. **立即：** 部署 Rule-Based 取代純 BM25，預計 1 天上線
2. **2 週內：** 完成 LambdaMART 訓練，啟動 A/B test
3. **下一季：** 跑 10% 流量的結果隨機化實驗，取得真實 propensity 估計值以改善 debiasing
4. **長期：** 考慮依類別拆模型（登山裝備 vs. 服飾 vs. 露營炊具的排名邏輯差異顯著）
