# Example: 電商平台冷啟動與個人化混合推薦

## Scenario

**公司背景：** ShopNest，台灣中型跨品類電商，SKU 約 120,000 件，月活躍用戶 800,000。

**問題陳述：**
> 「我們目前純用協同過濾（CF），但新用戶佔每日新增的 40%，這群人推薦品質很差，轉換率只有回訪用戶的 1/5。我們想加入商品內容特徵來改善冷啟動，但不確定怎麼組合、權重怎麼設。」

**可用資料：**
- 互動歷史：點擊、加購、購買，共 3,200 萬筆（回訪用戶均值 18 筆 / 人）
- 商品特徵：品類、品牌、價格區間、材質標籤、商品描述 embedding（全部 120K SKU 完整覆蓋）
- 上下文：裝置類型（mobile / desktop）、時段

## Analysis

### Phase 1：Input Validation — 資料能力映射

| 資料源 | 可用方法 | 覆蓋範圍 |
|--------|----------|----------|
| 互動歷史（≥ 5 筆）| CF（矩陣分解 ALS）| 約 60% 用戶 |
| 互動歷史（< 5 筆）| CF 不可靠 | 約 40% 用戶（新 / 低活）|
| 商品特徵 embedding | Content-Based（cosine 相似）| 100% 商品 |
| 上下文訊號 | 規則 / 過濾輔助 | 100% session |

**互補性確認：** CF 覆蓋高活用戶但冷啟動失效；Content-Based 對任何用戶都能推（只要有瀏覽記錄 ≥ 1 件），兩者短板不重疊。**Gate 通過。**

**架構決策：** 選 **Switching Hybrid**（非加權）。

原因：
- 新用戶 CF embedding 品質差，強行加權會污染結果
- 商品特徵完整，Content-Based 可獨立撐起冷啟動
- 工程複雜度低，可先快速上線驗證

---

### Phase 2：Core Algorithm — Switching 邏輯設計

**切換閾值（cross-validation 決定）：**

```
if user_interactions >= 10:
    method = "CF"          # ALS 因子穩定，precision@10 = 0.31
elif 2 <= user_interactions < 10:
    method = "content"     # 以最近瀏覽 N 件做 seed，cosine top-K
else:  # 新用戶 / 0-1 筆互動
    method = "popularity"  # 品類熱銷榜，依裝置過濾（mobile 偏低價）
```

**Content-Based 細節（2-9 筆互動用戶）：**

```python
# seed = 用戶最近 3 筆互動商品
seed_embeddings = [item_emb[i] for i in last_3_items]
user_profile = np.mean(seed_embeddings, axis=0)  # 簡單均值

# 候選集：同品類下 cosine 相似度 top-50
candidates = cosine_top_k(user_profile, item_embeddings, k=50)

# 排除已互動商品，取前 10
recommendations = [c for c in candidates if c not in user_history][:10]
```

**CF 細節（≥ 10 筆互動用戶）：**

ALS rank-128，implicit feedback 加權（購買 × 5、加購 × 2、點擊 × 1），每日增量更新。

---

### Phase 3：Verification — A/B 測試設計

**測試分組（流量 20%，為期 14 天）：**

| 組別 | 方法 | 流量佔比 |
|------|------|----------|
| Control | 純 CF（現行） | 50% |
| Treatment | Switching Hybrid | 50% |

**分層分析（依用戶互動數）：**

| 用戶段 | Control NDCG@10 | Treatment NDCG@10 | 提升 |
|--------|-----------------|-------------------|------|
| 0-1 筆 | 0.04（熱銷榜退化）| 0.04（同，尚無 seed）| — |
| 2-9 筆 | 0.11 | 0.19 | **+73%** |
| ≥ 10 筆 | 0.31 | 0.30 | -3%（誤差內）|

**覆蓋率與多樣性：**

| 指標 | Control | Treatment |
|------|---------|-----------|
| Catalog coverage | 23% | 41% |
| Intra-list diversity（avg）| 0.38 | 0.52 |
| 新用戶 7 日留存 | 22% | 29% |

**Gate 判定：** Hybrid 在主力目標（新用戶 NDCG）大幅提升，回訪用戶持平。通過。

---

### Phase 4：Source Attribution

每筆推薦記錄來源，供 explainability 與 debug：

## Result

```json
{
  "user_id": "u_cold_20240315",
  "user_interactions": 3,
  "recommendations": [
    {
      "item_id": "sku_089231",
      "score": 0.87,
      "sources": {
        "content": 0.87,
        "cf": null
      },
      "method": "content",
      "reason": "與您瀏覽的 [登山背包] 相似度高（品類 + 材質標籤）"
    },
    {
      "item_id": "sku_045902",
      "score": 0.82,
      "sources": {
        "content": 0.82,
        "cf": null
      },
      "method": "content",
      "reason": "同品牌、相近價格區間"
    }
  ],
  "metadata": {
    "architecture": "switching",
    "active_method": "content",
    "switch_threshold": 10,
    "user_segment": "cold_start",
    "coverage": 0.41,
    "diversity": 0.52
  }
}
```

**落地建議：**

1. **不要現在做加權混合**：回訪用戶 CF 表現穩定，加入 CB 加權沒有顯著收益（A/B 已驗證），增加的維護複雜度不划算。
2. **0-1 筆互動用戶是下一個攻克目標**：考慮引入 onboarding 問卷（品類偏好 3 選 1）作為 cold seed，讓 Content-Based 更早接手。
3. **閾值 10 筆需定期校準**：隨季節性購物行為變化，每季重跑交叉驗證確認切換點。
4. **監控 content 方法的 item 多樣性**：若 seed 商品過度集中單一品類，均值 embedding 會強化馬太效應，需加入品類去重邏輯。
