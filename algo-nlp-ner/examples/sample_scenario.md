# Example: 從台灣科技新聞稿中提取實體

## Scenario

GlobalInvest 台灣研究團隊每天需要處理 50-100 篇科技產業新聞稿，手動標記其中提到的公司、人名、地點、日期以更新投資追蹤資料庫。分析師 Sharon Chen 希望自動化這個流程。

輸入文本範例（一篇新聞稿片段）：

> MediaTek CEO Rick Tsai confirmed on April 8 that the company will invest NT$12 billion in a new R&D center in Hsinchu Science Park. The announcement followed meetings with TSMC chairman Mark Liu and representatives from Qualcomm's Singapore office. Construction is expected to begin in Q3 2026, with completion targeted for December 2027.

要求：提取所有 PER、ORG、LOC、DATE、MONEY 類型實體，並輸出可匯入資料庫的 JSON。

---

## Analysis

### Phase 1: Input Validation

**目標實體類型：** PER、ORG、LOC、DATE、MONEY（標準 OntoNotes schema）

**語言：** 英文（新聞稿為英文；後續中文版本需分開處理）

**領域評估：**
- 文本來自科技財經新聞，接近 OntoNotes 訓練資料的新聞語料 → 預訓練模型即可，無需 fine-tune
- 若後續擴展到中文或包含晶片型號（如 Dimensity 9400）等自定義實體，才需要 domain-specific 訓練

**模型選擇：** `en_core_web_trf`（spaCy transformer pipeline，F1 ≈ 90% on CoNLL-2003）

**Gate 通過：** 實體類型明確，預訓練模型覆蓋所有目標類型。

---

### Phase 2: Core Algorithm（Pre-trained model approach）

**執行 spaCy pipeline：**

```python
import spacy
nlp = spacy.load("en_core_web_trf")

text = (
    "MediaTek CEO Rick Tsai confirmed on April 8 that the company will invest "
    "NT$12 billion in a new R&D center in Hsinchu Science Park. The announcement "
    "followed meetings with TSMC chairman Mark Liu and representatives from "
    "Qualcomm's Singapore office. Construction is expected to begin in Q3 2026, "
    "with completion targeted for December 2027."
)

doc = nlp(text)
entities = [
    {
        "text": ent.text,
        "type": ent.label_,
        "start": ent.start_char,
        "end": ent.end_char,
        "confidence": round(ent._.trf_data.tensors[0].max().item(), 2)
            if hasattr(ent._, "trf_data") else None
    }
    for ent in doc.ents
]
```

**原始模型輸出（未修正前）：**

| text | type | start | end |
|------|------|-------|-----|
| MediaTek | ORG | 0 | 8 |
| Rick Tsai | PER | 13 | 22 |
| April 8 | DATE | 36 | 43 |
| NT$12 billion | MONEY | 72 | 85 |
| Hsinchu Science Park | LOC | 103 | 123 |
| TSMC | ORG | 155 | 159 |
| Mark Liu | PER | 169 | 177 |
| Qualcomm | ORG | 201 | 209 |
| Singapore | LOC | 212 | 221 |
| Q3 2026 | DATE | 263 | 270 |
| December 2027 | DATE | 296 | 309 |

**邊界問題排查：**
- ✅ "Hsinchu Science Park" 正確識別為整個 LOC span（非只抓 "Hsinchu"）
- ⚠️ "Qualcomm's Singapore office" — 模型將 "Qualcomm" 與 "Singapore" 分開識別；"Singapore office" 非獨立 LOC，後處理需忽略從屬地點或標記為 ORG 的關聯地點
- ✅ "NT$12 billion" 含貨幣符號，識別為 MONEY 正確

---

### Phase 3: Verification

在 10 篇已人工標注的 GlobalInvest 歷史新聞稿上評估：

| Entity Type | Precision | Recall | F1 |
|-------------|-----------|--------|----|
| PER | 0.94 | 0.91 | 0.92 |
| ORG | 0.89 | 0.86 | 0.87 |
| LOC | 0.91 | 0.88 | 0.89 |
| DATE | 0.96 | 0.93 | 0.94 |
| MONEY | 0.88 | 0.82 | 0.85 |

**Gate 通過：** 所有類型 F1 > 0.80。

**已知殘留問題（記錄，不阻擋上線）：**
- "Q3 2026" 有時被分割為 "Q3" + "2026"（兩個 DATE） → 加 regex 後處理合併
- 台灣特有機構（如「國科會」英譯 NSTC）偶爾誤分為 LOC → 加 gazetteer whitelist

---

### Phase 4: Output

```json
{
  "entities": [
    {"text": "MediaTek",             "type": "ORG",   "start": 0,   "end": 8,   "confidence": 0.97},
    {"text": "Rick Tsai",            "type": "PER",   "start": 13,  "end": 22,  "confidence": 0.95},
    {"text": "April 8",              "type": "DATE",  "start": 36,  "end": 43,  "confidence": 0.96},
    {"text": "NT$12 billion",        "type": "MONEY", "start": 72,  "end": 85,  "confidence": 0.91},
    {"text": "Hsinchu Science Park", "type": "LOC",   "start": 103, "end": 123, "confidence": 0.93},
    {"text": "TSMC",                 "type": "ORG",   "start": 155, "end": 159, "confidence": 0.98},
    {"text": "Mark Liu",             "type": "PER",   "start": 169, "end": 177, "confidence": 0.94},
    {"text": "Qualcomm",             "type": "ORG",   "start": 201, "end": 209, "confidence": 0.96},
    {"text": "Singapore",            "type": "LOC",   "start": 212, "end": 221, "confidence": 0.87},
    {"text": "Q3 2026",              "type": "DATE",  "start": 263, "end": 270, "confidence": 0.93},
    {"text": "December 2027",        "type": "DATE",  "start": 296, "end": 309, "confidence": 0.95}
  ],
  "metadata": {
    "model": "en_core_web_trf",
    "entities_found": 11,
    "types": {"PER": 2, "ORG": 3, "LOC": 2, "DATE": 3, "MONEY": 1}
  }
}
```

---

## Result

**Sharon 的自動化流程：**

1. 每篇新聞稿平均提取 8-15 個實體，耗時 < 0.3 秒/篇
2. 輸出 JSON 直接匯入投資追蹤資料庫，人工只需複查低信心（< 0.85）的條目
3. 預計每天節省 2-3 小時人工標記時間

**後續決策點：**
- 若未來需處理中文新聞稿，需換用 `zh_core_web_trf` 或 Hugging Face `ckiplab/bert-base-chinese-ner`，並重新評估 F1
- 若需識別晶片型號（如 Dimensity 9400、A18 Pro）為自定義實體類型 `PRODUCT`，需標注 200+ 筆範例進行 fine-tune
- Entity linking（"TSMC" → Wikidata Q713393）是獨立任務，不在本 skill 範疇
