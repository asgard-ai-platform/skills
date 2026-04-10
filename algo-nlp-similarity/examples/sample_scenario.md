# Example: 客服 FAQ 自動比對去重

## Scenario

**公司：** 91App（台灣 SaaS 電商平台）  
**時間：** 2026 年 Q1  
**背景：** 客服知識庫累積了 3 年的 FAQ，現有 847 筆問答。行銷部門要上線新的 AI 客服機器人，但工程師發現資料庫裡有大量重複或近似的問題（例如「怎麼退款」「退貨流程是什麼」「我要申請退費」），會導致機器人給出不一致的答案。  
**需求：**
1. 找出近似重複的 FAQ（語意相似度 ≥ 0.85），準備合併
2. 當使用者提問時，從 FAQ 庫找出最相關的前 3 筆

---

## Analysis

### Phase 1：Input Validation

**資料狀況：**
- 847 筆 FAQ，每筆平均 12 個字（繁體中文短句）
- 文字極短 → TF-IDF 向量稀疏，Jaccard 不可靠
- 需要的是「語意」相同（退款 ≈ 退貨退費），不是字面相同

**方法選擇：**

| 需求 | 方法 | 原因 |
|------|------|------|
| 近似重複偵測 | Semantic cosine（句子嵌入） | 短文本字詞差異大，需語意捕捉 |
| 即時查詢比對 | Semantic cosine + FAISS | 847 筆可接受暴力搜尋，但 FAISS 留作擴充 |

**Iron Law 應用：** 先用 Jaccard 做快速驗證——  
「怎麼退款」vs「退貨流程是什麼」：Jaccard = 0/7 = **0.00**（無共用詞）  
但這兩筆語意幾乎相同，確認必須走語意路線。

**Gate ✅** 文字已清洗（去除標點），方法選定為 sentence-transformers。

---

### Phase 2：Core Algorithm

**模型選擇：** `paraphrase-multilingual-MiniLM-L12-v2`  
（支援繁體中文，比 all-MiniLM-L6-v2 更適合非英文場景）

**Step 2a：批次編碼 847 筆 FAQ 問題**

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
questions = [faq["question"] for faq in faq_db]   # 847 筆
embeddings = model.encode(questions, normalize_embeddings=True)
# shape: (847, 384)
```

**Step 2b：計算 all-pairs cosine 相似度（N=847，pairs=358,381）**

```python
similarity_matrix = np.dot(embeddings, embeddings.T)
# 因為已 L2 normalize，dot product = cosine similarity
```

**Step 2c：找出高相似度對（threshold = 0.85）**

前 10 組近似重複範例：

| FAQ ID A | 問題 A | FAQ ID B | 問題 B | Semantic Score |
|----------|--------|----------|--------|---------------|
| Q0042 | 怎麼申請退款？ | Q0318 | 我要退費怎麼辦 | 0.94 |
| Q0042 | 怎麼申請退款？ | Q0521 | 退款流程是什麼 | 0.91 |
| Q0107 | 訂單出貨了嗎 | Q0209 | 如何查詢出貨狀態 | 0.88 |
| Q0155 | 忘記密碼怎麼辦 | Q0612 | 密碼重設步驟 | 0.87 |
| Q0200 | 可以修改收件地址嗎 | Q0401 | 訂單地址怎麼改 | 0.86 |

共找出 **73 組**相似度 ≥ 0.85 的近似重複對，涵蓋 **124 筆**（約 15% 的 FAQ）。

**Step 2d：即時查詢比對（使用者提問 → Top-3 FAQ）**

使用者輸入：「我的包裹還沒到，要怎麼查」

```python
query = "我的包裹還沒到，要怎麼查"
query_emb = model.encode([query], normalize_embeddings=True)
scores = np.dot(query_emb, embeddings.T)[0]
top3_idx = np.argsort(scores)[::-1][:3]
```

結果：

| Rank | FAQ ID | 問題 | Score |
|------|--------|------|-------|
| 1 | Q0107 | 訂單出貨了嗎 | 0.87 |
| 2 | Q0209 | 如何查詢出貨狀態 | 0.85 |
| 3 | Q0388 | 包裹延誤怎麼辦 | 0.79 |

---

### Phase 3：Verification

**Spot-check 高分對（應真正相似）：**
- Q0042「怎麼申請退款？」& Q0318「我要退費怎麼辦」→ Score 0.94 ✅ 確實同義
- Q0107「訂單出貨了嗎」& Q0209「如何查詢出貨狀態」→ Score 0.88 ✅ 確實相關

**Spot-check 低分對（應真正不同）：**
- Q0042「怎麼申請退款？」& Q0155「忘記密碼怎麼辦」→ Score 0.21 ✅ 確實不同

**Threshold 校準：**  
人工抽查 20 組 score 介於 0.80–0.85 的配對：
- 12 組確實是「語意相近但不同問題」（例：退款 vs 換貨）
- 8 組偏重複  
→ 決定**去重閾值維持 0.85**，0.80–0.85 之間的對列為「人工審核」佇列

**Gate ✅** 相似度分佈與人工判斷一致，閾值校準完成。

---

## Result

### Output（JSON 格式，符合 SKILL.md）

```json
{
  "similarities": [
    {
      "text_a": "Q0042: 怎麼申請退款？",
      "text_b": "Q0318: 我要退費怎麼辦",
      "score": 0.94,
      "method": "semantic_cosine"
    },
    {
      "text_a": "Q0042: 怎麼申請退款？",
      "text_b": "Q0521: 退款流程是什麼",
      "score": 0.91,
      "method": "semantic_cosine"
    }
  ],
  "metadata": {
    "method": "sentence-transformers",
    "model": "paraphrase-multilingual-MiniLM-L12-v2",
    "pairs_computed": 358381,
    "duplicates_found": 73,
    "threshold": 0.85,
    "manual_review_queue": 31
  }
}
```

### 行動建議

| 優先級 | 行動 | 數量 |
|--------|------|------|
| 立即合併 | Score ≥ 0.85 的重複對 | 73 組 → 精簡 49 筆 FAQ |
| 人工審核 | Score 0.80–0.85 的邊界對 | 31 組 |
| 保留 | Score < 0.80 | 672 筆（確認為獨立問題） |

合併後 FAQ 庫從 847 筆降至約 **798 筆**，重複內容消除，機器人回覆一致性預計顯著提升。

### 注意事項（Gotchas 應用）

- **閾值不能套用其他場景**：本次 0.85 是為「去重」校準的。若日後要做「推薦相關問題」，合理閾值可能降至 0.65。
- **繁中模型選擇關鍵**：若誤用 all-MiniLM-L6-v2（英文優化），「退款」與「退費」的相似度只有 0.61，低於閾值，會漏掉真正的重複。
- **規模警示**：目前 847 筆 O(N²) 可接受（358K pairs），若 FAQ 擴充至 5 萬筆以上，需改用 FAISS IndexFlatIP 做近似搜尋。
