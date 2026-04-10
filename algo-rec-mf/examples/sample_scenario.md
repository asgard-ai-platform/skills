# Example: 串流音樂平台的個人化推薦

## Scenario

**公司：** Cadence Music（台灣獨立音樂串流平台）
**時間：** 2026 年 Q1

Cadence 的數據工程師 Vivian 來詢問：

> 「我們有 12 萬名活躍用戶和 8 萬首曲目。用戶可以對歌曲評分（1–5 星），但矩陣填充率只有約 0.8%。現在用的是 user-based 協同過濾，但當用戶量超過 10 萬後，pairwise 相似度計算慢到不可用——每次推薦要 4 秒。想換成 matrix factorization，請問怎麼做？」

---

## Analysis

### Phase 1：Input Validation

**互動矩陣規模：**
- m = 120,000 users，n = 80,000 items
- 觀測評分數：120,000 × 80,000 × 0.8% = **76,800,000 筆**
- 平均每用戶 640 筆評分，每首曲目 960 筆評分

**密度檢查：**
```
fill_rate = 0.008 (0.8%)
```
> 0.1% threshold → **通過 Gate 1**。但密度屬於「低端可接受」區間，需要謹慎選擇 k。

**分割策略（時序切割，避免 data leakage）：**
- Train：用戶最後 20% 評分之前的所有資料（~61.4M 筆）
- Validation：用戶最後 20% 中的 10%（~7.7M 筆）
- Test：用戶最後 20% 中的 10%（~7.7M 筆）

---

### Phase 2：Core Algorithm — ALS

**選擇 ALS 而非 SGD 的原因：**
- 資料量 76M 筆，ALS 支援平行化；Cadence 有 Spark 叢集
- ALS 對 implicit feedback 擴展更直接（未來準備切 plays→ratings）

**超參數搜尋（grid search on validation RMSE）：**

| k  | λ     | iterations | val_RMSE |
|----|-------|------------|----------|
| 20 | 0.01  | 20         | 1.02     |
| 50 | 0.01  | 20         | 0.89     |
| 50 | 0.1   | 20         | 0.91     |
| 100| 0.01  | 20         | 0.87     |
| 100| 0.01  | 50         | 0.84     |
| 200| 0.01  | 50         | 0.86     |

**決策：k=100, λ=0.01, iterations=50**

> k=200 反而略高，出現輕微 overfitting（正如 Iron Law 所警示：k 過高會對 noise 過擬合）。k=100 是 bias-variance 甜點。

**初始化：** 用 truncated SVD（前 100 個奇異值）做 warm-start，比隨機初始化快 30% 收斂。

**ALS 核心更新（pseudocode）：**
```python
for iteration in range(50):
    # 固定 V，更新 U
    for i in range(m):
        V_i = V[rated_by_user_i]       # shape: (n_i, k)
        R_i = R[i, rated_by_user_i]    # shape: (n_i,)
        U[i] = solve(V_i.T @ V_i + λ*I, V_i.T @ R_i)

    # 固定 U，更新 V
    for j in range(n):
        U_j = U[users_rated_item_j]    # shape: (m_j, k)
        R_j = R[users_rated_item_j, j] # shape: (m_j,)
        V[j] = solve(U_j.T @ U_j + λ*I, U_j.T @ R_j)
```

注意：Vivian 特別問到是否要加 bias。**答案是要加：**
```
r̂ᵢⱼ = μ + bᵢ + bⱼ + uᵢ · vⱼ
```
Cadence 的用戶評分行為差異很大（有些用戶普遍打高分），加 bias 後 val_RMSE 從 0.84 降到 **0.79**。

---

### Phase 3：Verification

**Baseline 比較：**

| 模型              | val_RMSE | 推薦延遲     |
|-------------------|----------|------------|
| Global mean (μ)   | 1.18     | < 1ms      |
| User mean         | 1.03     | < 1ms      |
| User-based CF     | 0.96     | 4,200ms    |
| **MF k=100 + bias** | **0.79** | **12ms** |

val_RMSE 比 user-based CF 再降 0.17，且延遲從 4.2 秒降至 **12 毫秒**（350× 加速）。

**Gate 2 通過：** val_RMSE 顯著低於所有 baseline。

**潛在因子可解釋性驗證（抽樣前 3 個 latent factors）：**
- Factor 1：流行度偏好（高負載 = 台語流行、低負載 = 前衛爵士）
- Factor 2：年代偏好（高負載 = 2000 年代以前、低負載 = 2020 年後）
- Factor 3：節奏偏好（高負載 = 慢板、低負載 = 快板電子）

---

### Phase 4：Output

用戶 `u_A8823`（28 歲，聽了大量獨立民謠）的 Top-5 推薦：

```json
{
  "recommendations": [
    {
      "user_id": "u_A8823",
      "items": [
        {"item_id": "track_7741", "title": "落雨聲", "predicted_rating": 4.61},
        {"item_id": "track_2290", "title": "候鳥", "predicted_rating": 4.55},
        {"item_id": "track_8812", "title": "走鋼索的人", "predicted_rating": 4.48},
        {"item_id": "track_0334", "title": "給十年後的你", "predicted_rating": 4.44},
        {"item_id": "track_5501", "title": "海平面以上", "predicted_rating": 4.39}
      ]
    }
  ],
  "metadata": {
    "rank_k": 100,
    "regularization": 0.01,
    "bias_terms": true,
    "iterations": 50,
    "train_rmse": 0.71,
    "val_rmse": 0.79,
    "inference_latency_ms": 12
  }
}
```

---

## Result

**部署建議：**

1. **離線訓練排程：** 每日凌晨 2:00 用前 90 天資料重新訓練（ALS 全量訓練約 45 分鐘）
2. **因子向量快取：** U（120K × 100）≈ 96 MB、V（80K × 100）≈ 64 MB，直接載入 Redis
3. **新用戶冷啟動：** 新用戶沒有 U 因子，暫用 popularity fallback；等累積 ≥ 10 筆評分後觸發 user-only ALS 更新

**Vivian 的原始痛點全數解決：**
- 推薦延遲：4,200ms → **12ms**
- 模型品質：val_RMSE 0.96 → **0.79**
- 可擴展性：O(n²) 相似度計算 → O(k × nnz × iter)，百萬用戶規模可行

**注意事項（Gotchas 對應）：**
- Cadence 未來若要用播放次數（implicit）取代評分，需切換為 **Hu et al. (2008) 加權 MF**，不能直接套用現有 RMSE 目標函數
- 新上架曲目（cold-start items）無法被 MF 推薦，建議用內容特徵（曲風、BPM）做 item embedding 橋接
