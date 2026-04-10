# Example: 法說會財報新聞自動摘要 Pipeline

## Scenario

TechInsight Media 是一家財經媒體公司，每季需要處理 200+ 篇法說會報導，記者平均每篇需花 15 分鐘閱讀並手寫 TLDR 給編輯。主編 Amy 希望建立自動摘要系統，初期先針對科技股法說會新聞（平均 1,800 字），產出 150-200 字的中文摘要，供編輯快速審核後發布。

Amy 的問題：「要用 extractive 還是 abstractive？摘要品質怎麼評估？」

---

## Analysis

### Phase 1: Input Validation

| 項目 | 值 |
|------|-----|
| 輸入長度 | 平均 1,800 字（~2,400 tokens，在 T5/BART 限制內） |
| 目標摘要長度 | 150-200 字，壓縮比 ~0.10 |
| 文件類型 | 單篇新聞，財經領域，結構化（inverted pyramid） |
| 語言 | 繁體中文 |
| 使用場景 | 編輯審核後發布 → 高準確性需求 |

**Gate 通過：** 輸入長度在模型限制內，目標明確，domain 已知。

---

### Phase 2: Core Algorithm 選擇

**決策：先跑 Extractive（TextRank），作為 baseline 和安全網。**

財經報導屬於高風險 domain（IRON LAW：Abstractive 可能幻覺出不存在的數字），用 extractive 作為主力，abstractive 作為輔助產出供對照。

#### Extractive — TextRank 實作

範例輸入（節錄，聯發科 Q4 法說會報導，2025-01-16）：

```
聯發科技（2454）昨日召開法人說明會，公告第四季合併營收為新台幣 1,423 億元，
季增 8.2%，年增 21.4%，創歷史新高。毛利率為 49.3%，優於市場預期的 48.8%。

執行長蔡力行表示，AI 邊緣運算晶片需求強勁，尤其 Dimensity 9400 系列出貨量
超預期，預估 2025 年上半年 AI 手機滲透率將達 35%，帶動旗艦晶片平均單價上漲
約 12%。

第一季營收展望為 1,380 億至 1,470 億元（中間值季減 2.7%），毛利率指引 48%-50%，
符合季節性淡季規律。法人關注的庫存方面，管理層表示客戶庫存已回到健康水位，
去庫存壓力完全解除...
[全文共 1,847 字，23 段]
```

**Step 1 — 斷句：** 切出 47 句。

**Step 2 — 建 similarity graph：**
- 使用 TF-IDF 向量 + cosine similarity
- 剔除 similarity < 0.1 的邊（稀疏化）

**Step 3 — PageRank（damping=0.85，迭代至收斂）：**

| Rank | 句子（節錄） | Score |
|------|-------------|-------|
| 1 | Q4 合併營收 1,423 億，年增 21.4%，創歷史新高 | 0.087 |
| 2 | 毛利率 49.3%，優於預期 48.8% | 0.074 |
| 3 | Dimensity 9400 出貨超預期，AI 手機滲透率 2025H1 達 35% | 0.068 |
| 4 | Q1 營收展望 1,380-1,470 億，符合季節性淡季 | 0.063 |
| 5 | 客戶庫存回健康水位，去庫存壓力解除 | 0.059 |

**Step 4 — 選 top-5，按原文位置重排輸出。**

---

#### Abstractive — mT5-base（中文 fine-tuned）對照

同一篇文章送入 `csebuetnlp/mT5_multilingual_XLSum`（已支援繁中）：

- 參數：`max_length=200, num_beams=4, no_repeat_ngram_size=3`
- 輸出：流暢但出現「毛利率達 50.1%」（原文為 49.3%） → **數字幻覺，觸發 IRON LAW**

---

### Phase 3: Verification

對 20 篇已有記者手寫摘要的文章進行 ROUGE 評估：

| 方法 | ROUGE-1 | ROUGE-2 | ROUGE-L |
|------|---------|---------|---------|
| TextRank (extractive) | 0.48 | 0.31 | 0.44 |
| mT5 abstractive | 0.52 | 0.34 | 0.47 |
| First-2-sentences baseline | 0.39 | 0.22 | 0.36 |

**觀察：**
- Abstractive ROUGE 略高，但 20 篇中有 6 篇出現數字錯誤（30%）
- TextRank 無幻覺風險，ROUGE 差距小（< 0.04），可接受
- 「取前兩句」baseline 在財經 inverted pyramid 結構下已不差，但遺漏 guidance 和庫存資訊

**決策：** 採 extractive TextRank 作為生產版本；abstractive 僅作為內部參考欄。

---

## Result

### 系統輸出（聯發科 Q4 法說會）

```json
{
  "summary": "聯發科第四季合併營收 1,423 億元，季增 8.2%、年增 21.4%，創歷史新高，毛利率 49.3% 優於市場預期。AI 手機需求帶動 Dimensity 9400 系列出貨超預期，預估 2025 年上半年 AI 手機滲透率達 35%，旗艦晶片單價上漲約 12%。首季展望為 1,380 至 1,470 億元，符合季節性淡季規律，客戶庫存已回健康水位。",
  "method": "extractive_textrank",
  "metadata": {
    "input_words": 1847,
    "summary_words": 83,
    "compression_ratio": 0.045,
    "sentences_selected": 5,
    "rouge_1_benchmark": 0.48,
    "hallucination_risk": "low"
  }
}
```

> **注意：** 壓縮比 0.045 低於目標 0.10，因財經文章關鍵資訊密度高，5 句已足夠。

### 給 Amy 的建議

1. **生產環境用 extractive**：財經數字不容幻覺，TextRank 無此風險
2. **不要只看 ROUGE**：mT5 ROUGE 更高，但 30% 數字錯誤對媒體是致命問題
3. **位置偏差反而有利**：財經報導 inverted pyramid 結構與 TextRank 排序高度吻合
4. **多文件場景另案處理**：若未來需跨多篇法說會比較，需加入去重複邏輯
