# Example: 線上書店「頁間」的商品推薦系統

## Scenario

「頁間」是一家台灣中型線上書店，月活躍用戶約 8,000 人，書籍目錄 12,000 本。目前首頁只顯示暢銷榜，轉換率偏低。產品經理 Vivian 希望在書籍詳情頁加入「看了這本書的讀者也看了…」功能，有現成的購買紀錄資料庫，但沒有明確評分。

**現有資料：**
- `user_purchases` 表：180 萬筆購買紀錄（user_id, book_id, purchase_date）
- 活躍用戶（購買 ≥ 3 本）：約 6,200 人
- 熱門書籍（被購買 ≥ 10 次）：約 4,800 本
- 矩陣填充率：180 萬 / (6,200 × 4,800) ≈ 6.0%

---

## Analysis

### Phase 1: Input Validation

**稀疏度檢查：**
- 填充率 6.0%，> 1% 門檻 ✓
- 活躍用戶平均購買數：180 萬 / 6,200 ≈ 290 本（遠超 5 本最低門檻）✓
- 熱門書籍平均被購買次數：180 萬 / 4,800 ≈ 375 次 ✓

**資料性質判斷：**  
購買紀錄屬於 **implicit feedback**（無明確評分）。將「曾購買」編碼為 1、「未購買」為 0，並以購買次數作為信心權重（confidence = 1 + α × count，α=40 為常用預設）。

**選擇演算法：Item-based CF**  
理由：書籍目錄 4,800 本 < 用戶數 6,200 人，item-item 相似度矩陣 (4,800²) 比 user-user (6,200²) 小且更穩定；書籍間的共購關係在時間上也比用戶口味更穩定。

**Gate 通過** — 繼續 Phase 2。

---

### Phase 2: Core Algorithm

**建立共現矩陣（範例子集，5 本書 × 5 位用戶）：**

| | 用戶 A | 用戶 B | 用戶 C | 用戶 D | 用戶 E |
|---|---|---|---|---|---|
| 書 001（龍紋身的女孩） | 1 | 1 | 0 | 1 | 0 |
| 書 002（千禧三部曲II） | 1 | 1 | 0 | 0 | 0 |
| 書 003（福爾摩斯全集） | 0 | 1 | 1 | 1 | 1 |
| 書 004（東方快車謀殺案） | 0 | 0 | 1 | 1 | 1 |
| 書 005（挪威的森林） | 1 | 0 | 0 | 0 | 1 |

**計算 item-item cosine 相似度（書 001 與其他書）：**

$$\text{sim}(i, j) = \frac{\sum_u r_{ui} \cdot r_{uj}}{\sqrt{\sum_u r_{ui}^2} \cdot \sqrt{\sum_u r_{uj}^2}}$$

- sim(001, 002) = (1·1 + 1·1) / (√3 × √2) = 2 / 2.449 = **0.816**
- sim(001, 003) = (1·1 + 1·1) / (√3 × √4) = 2 / 3.464 = **0.577**
- sim(001, 004) = (0 + 1·1) / (√3 × √3) = 1 / 3 = **0.333**
- sim(001, 005) = (1·1) / (√3 × √2) = 1 / 2.449 = **0.408**

**書 001 最相似前 3 本（K=3）：** 書 002 (0.816)、書 003 (0.577)、書 005 (0.408)

**預測用戶 E 對書 001 的興趣分數：**  
用戶 E 已購買：書 003、書 004、書 005

$$\hat{r}_{E,001} = \frac{\sum_{j \in \text{rated}} \text{sim}(001, j) \cdot r_{Ej}}{\sum_{j \in \text{rated}} |\text{sim}(001, j)|}$$

$$= \frac{0.577 \times 1 + 0.333 \times 1 + 0.408 \times 1}{0.577 + 0.333 + 0.408} = \frac{1.318}{1.318} = 1.0$$

用戶 E 購買的書與書 001 均有正相關 → 推薦。

---

### Phase 3: Verification

隨機抽取 20% 購買紀錄（36 萬筆）作為測試集，以剩餘 144 萬筆訓練。

**評估指標（implicit feedback 用 Precision@K / Recall@K）：**

| K | Precision@K | Recall@K |
|---|---|---|
| 5 | 0.31 | 0.18 |
| 10 | 0.26 | 0.29 |
| 20 | 0.19 | 0.41 |

**基線對照（全局熱門榜）：** Precision@10 = 0.14

Item-based CF Precision@10 = 0.26，**比熱門基線提升 86%** ✓

**Gate 通過** — 繼續 Phase 4。

---

### Phase 4: Output

查詢書籍 `book_id: "B001"`（龍紋身的女孩）的推薦結果：

```json
{
  "recommendations": [
    {"item_id": "B002", "predicted_score": 0.816, "similar_items_used": 6},
    {"item_id": "B003", "predicted_score": 0.577, "similar_items_used": 4},
    {"item_id": "B089", "predicted_score": 0.541, "similar_items_used": 5},
    {"item_id": "B145", "predicted_score": 0.498, "similar_items_used": 3},
    {"item_id": "B005", "predicted_score": 0.408, "similar_items_used": 4}
  ],
  "metadata": {
    "method": "item-based",
    "similarity": "cosine",
    "k_neighbors": 20,
    "sparsity": 0.94,
    "feedback_type": "implicit",
    "confidence_alpha": 40
  }
}
```

---

## Result

**部署建議：**

1. **書籍詳情頁**：顯示 top-5 推薦，標題「購買這本書的讀者也買了」
2. **冷啟動處理**：新書（購買 < 10 次）fallback 到同類別熱門榜；新用戶（購買 < 3 本）fallback 到全站熱門
3. **更新頻率**：item-item 相似度矩陣每週重算一次（書籍購買模式穩定）；用戶推薦快取每日刷新

**已知限制（Vivian 需知）：**
- **暢銷書偏差**：出現頻率最高的書會被過度推薦。建議加入 inverse popularity 正規化（除以 $\sqrt{\text{item\_frequency}}$）
- **系列書問題**：千禧三部曲 I-III 彼此相似度極高，5 個推薦位可能全被同系列佔滿。加入去重邏輯，同系列最多出現 2 本
- **規模瓶頸**：全目錄 12,000 本的 item-item 矩陣計算量尚可接受，但若目錄擴張到 50,000 本以上，建議改用 Locality-Sensitive Hashing (LSH) 做近似近鄰搜尋
