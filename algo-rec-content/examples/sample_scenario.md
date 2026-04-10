# Example: 串流平台新上架影片推薦

## Scenario

**公司：** StreamNest（台灣中型 OTT 平台）  
**背景：** 本週新上架 12 部影片，這些影片剛進資料庫，完全沒有觀看記錄或評分。傳統協同過濾無法處理這類新項目冷啟動問題。  
**需求：** 針對用戶 `user_7821`（有 30 部觀看歷史）產生個人化推薦清單，優先從新上架影片中挑選適合的片目。

---

## Analysis

### Phase 1：建立 Feature Vectors

每部影片以以下特徵表示：

| Feature | 類型 | 範例值 |
|---------|------|--------|
| `genre` | one-hot (12 類) | `[1,0,0,1,0,0,0,0,0,0,0,0]` (action, thriller) |
| `language` | one-hot (5 類) | `[0,1,0,0,0]` (zh-TW) |
| `duration_bucket` | one-hot (3 類) | `[0,1,0]` (90–120 min) |
| `director_score` | 數值 [0,1] | `0.78`（平台歷史完播率） |
| `title_tfidf` | TF-IDF (50 dims) | （稀疏向量） |

新上架影片 `movie_2991`（《暗流》，2026 年台灣驚悚片）：

```
genre:       [0,0,0,0,0,0,0,0,1,1,0,0]  # mystery, thriller
language:    [0,1,0,0,0]                  # zh-TW
duration:    [0,1,0]                      # 105 min
director:    0.83
tfidf_top5:  偵探(0.41), 謀殺(0.38), 懸疑(0.35), 台北(0.29), 警察(0.22)
```

**Gate 通過：** 12 部新片均完成特徵提取，feature dimension = 70。

---

### Phase 2：建立 User Profile（user_7821）

從 30 部觀看歷史取加權重心。權重策略：

- 近 90 天：weight × 1.5（時間衰減）
- 完播（>85%）：weight × 1.3
- 評分 ≥ 4 星：weight × 1.2

**觀看歷史摘要（前 10 部高權重）：**

| 影片 | 類型 | 完播 | 評分 | 最終權重 |
|------|------|------|------|----------|
| 《無聲計劃》 | mystery, thriller | ✓ | 5★ | 2.34 |
| 《暗夜搜查官》 | thriller, crime | ✓ | 4★ | 2.08 |
| 《失蹤的鄰居》 | mystery, drama | ✓ | 4★ | 1.95 |
| 《終局》 | action, thriller | — | 3★ | 1.00 |
| 《台北謎案》 | mystery | ✓ | 5★ | 2.34 |
| … | … | … | … | … |

**User Profile Vector（加權平均後前 5 個顯著維度）：**

```
genre_mystery:    0.71
genre_thriller:   0.68
language_zh-TW:   0.84
director_score:   0.75
tfidf_偵探:       0.39
```

---

### Phase 3：計算 Cosine Similarity

對 12 部新片分別計算 user profile 與 item vector 的 cosine similarity：

$$\text{sim}(u, i) = \frac{\vec{u} \cdot \vec{i}}{|\vec{u}||\vec{i}|}$$

| 影片 | 主要類型 | Cosine Score |
|------|----------|:------------:|
| 《暗流》(movie_2991) | mystery, thriller | **0.87** |
| 《獵影》(movie_2994) | thriller, crime | **0.81** |
| 《霧中城》(movie_2988) | drama, romance | 0.34 |
| 《爆裂球場》(movie_2997) | sports, comedy | 0.18 |
| 《星際漫遊》(movie_2983) | sci-fi | 0.22 |
| … | … | … |

**Top 3 新片推薦：** movie_2991 (0.87)、movie_2994 (0.81)、movie_2995 (0.76)

**多樣性注入：** user_7821 有 2 部紀錄片觀看記錄（輕微偏好），強制加入 movie_2986（紀錄片，score 0.51）作為第 4 位探索型推薦，避免 filter bubble 純化。

**Gate 通過：** Top-4 推薦的類型分布與用戶歷史主類型（mystery 71%、thriller 68%）一致；加入 1 部探索項目。

---

## Result

```json
{
  "user_id": "user_7821",
  "recommendations": [
    {
      "item_id": "movie_2991",
      "title": "暗流",
      "score": 0.87,
      "matching_features": ["genre:mystery", "genre:thriller", "language:zh-TW", "tfidf:偵探", "director_score:0.83"]
    },
    {
      "item_id": "movie_2994",
      "title": "獵影",
      "score": 0.81,
      "matching_features": ["genre:thriller", "genre:crime", "language:zh-TW"]
    },
    {
      "item_id": "movie_2995",
      "title": "第七個嫌疑人",
      "score": 0.76,
      "matching_features": ["genre:mystery", "language:zh-TW", "tfidf:謀殺"]
    },
    {
      "item_id": "movie_2986",
      "title": "山海之間（紀錄片）",
      "score": 0.51,
      "matching_features": ["genre:documentary", "language:zh-TW"],
      "note": "diversity_injection"
    }
  ],
  "metadata": {
    "method": "content-based",
    "features_used": 70,
    "profile_items": 30,
    "profile_dominant_genre": "mystery (0.71)",
    "temporal_decay_applied": true,
    "new_item_cold_start": true,
    "diversity_injected": 1
  }
}
```

**結論：**  
《暗流》以 0.87 高分奪冠，完全符合 user_7821 偏好 mystery + thriller + 台灣製作的輪廓。因為使用 content-based，新上架影片無需任何歷史觀看數據即可參與排名，解決了新片冷啟動問題。推薦引擎同時注入一部探索型紀錄片，緩解長期 filter bubble 風險。
