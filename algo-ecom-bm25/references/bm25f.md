# BM25F — Multi-Field BM25 for E-Commerce Product Search

BM25F (Best Matching 25 with Fields) extends vanilla BM25 to handle documents with multiple named fields — title, description, brand, category — by computing a **weighted pseudo-TF** across fields before applying IDF and saturation. The key distinction from naively summing per-field BM25 scores: normalization happens **per field**, but saturation is applied **once** to the combined signal. This ordering matters and is non-negotiable.

---

## The Formula

For query term `t` and document `d` with fields `F = {title, desc, brand, category, …}`:

```
pseudoTF(t, d) = Σ_f  w_f × tf(t, d, f) / (1 - b_f + b_f × |d_f| / avgdl_f)

TF_component(t, d) = pseudoTF(t, d) × (k₁ + 1) / (pseudoTF(t, d) + k₁)

Score(d, Q) = Σ_t  IDF(t) × TF_component(t, d)
```

Where:
| Symbol | Meaning |
|--------|---------|
| `w_f` | Boost weight for field `f` (tunable, not in standard BM25) |
| `tf(t, d, f)` | Raw term frequency of `t` in field `f` of document `d` |
| `b_f` | Length normalization strength for field `f` (0 = off, 1 = full) |
| `|d_f|` | Token count of field `f` in document `d` (after stop-word removal) |
| `avgdl_f` | Average length of field `f` across the corpus |
| `k₁` | Shared saturation parameter (use same value as parent BM25: 1.2) |
| `IDF(t)` | Global IDF computed over whole-document term presence (same Lucene-style formula as parent skill) |

**IDF uses corpus-level DF, not per-field DF.** A term is considered to appear in a document if it appears in any field.

---

## Why Not Sum Per-Field BM25 Scores?

Naive approach (wrong):

```
Score_naive = w_title × BM25(q, d.title) + w_desc × BM25(q, d.desc) + …
```

Problem: each field independently applies saturation. A term appearing once in title and once in description gets **two applications** of the `k₁` cap — as if the term were rare in each field independently. The combined signal undershoots.

BM25F approach (correct): pool the weighted, length-normalized TF from all fields first, then saturate once. A term appearing in both title and description benefits from both signals before the cap is applied.

---

## Worked Example

**Query:** "wireless earbuds"  
**Corpus:** 3 product documents, k₁ = 1.2

**Corpus statistics (post stop-word removal):**

| Field | avgdl |
|-------|-------|
| title | 4.0 tokens |
| description | 12.0 tokens |

**Document field weights and b values (reasonable e-commerce defaults):**

| Field | `w_f` | `b_f` |
|-------|-------|-------|
| title | 3.0 | 0.75 |
| description | 1.0 | 0.75 |

**Documents:**

| Doc | title | desc |
|-----|-------|------|
| A | "wireless earbuds" (2 tokens) | "compact wireless audio earbuds with mic" (6 tokens) |
| B | "sport wireless headphones earbuds style" (5 tokens) | "wireless design" (2 tokens) |
| C | "noise cancelling headphones" (3 tokens) | "wireless audio for sport use at gym" (8 tokens) |

**Global DF (N=3):**

| Term | DF | IDF = log((3 - DF + 0.5)/(DF + 0.5) + 1) |
|------|----|-------------------------------------------|
| wireless | 3 | log((0.5)/(3.5) + 1) = log(1.143) = 0.134 |
| earbuds | 2 | log((1.5)/(2.5) + 1) = log(1.600) = 0.470 |

**Step 1: Compute pseudoTF for "wireless" in Doc A**

```
title:   tf=1, |d|=2, avgdl=4.0, b=0.75, w=3.0
  → 3.0 × 1 / (1 - 0.75 + 0.75 × 2/4.0)
  → 3.0 × 1 / (0.25 + 0.375)
  → 3.0 × 1 / 0.625 = 4.800

desc:    tf=1, |d|=6, avgdl=12.0, b=0.75, w=1.0
  → 1.0 × 1 / (1 - 0.75 + 0.75 × 6/12.0)
  → 1.0 × 1 / (0.25 + 0.375)
  → 1.0 × 1 / 0.625 = 1.600

pseudoTF("wireless", A) = 4.800 + 1.600 = 6.400
```

**Step 2: Apply saturation**

```
TF_component = 6.400 × (1.2 + 1) / (6.400 + 1.2)
             = 6.400 × 2.2 / 7.600
             = 1.853
```

**Step 3: Weight by IDF**

```
IDF("wireless") × TF_component = 0.134 × 1.853 = 0.248
```

**Step 4: Repeat for "earbuds" in Doc A**

```
title:  tf=1, |d|=2, b=0.75, w=3.0 → 3.0/0.625 = 4.800
desc:   tf=1, |d|=6, b=0.75, w=1.0 → 1.0/0.625 = 1.600

pseudoTF("earbuds", A) = 6.400
TF_component = 1.853
IDF("earbuds") × 1.853 = 0.470 × 1.853 = 0.871
```

**Score(A) = 0.248 + 0.871 = 1.119**

**Doc B — "wireless":**

```
title:  tf=1, |d|=5, w=3.0 → 3.0 / (0.25 + 0.75×5/4.0) = 3.0/1.188 = 2.525
desc:   tf=1, |d|=2, w=1.0 → 1.0 / (0.25 + 0.75×2/12.0) = 1.0/0.375 = 2.667

pseudoTF("wireless", B) = 5.192
TF_component = 5.192 × 2.2 / 6.392 = 1.788
IDF term = 0.134 × 1.788 = 0.239
```

**Doc B — "earbuds":**

```
title:  tf=1, |d|=5, w=3.0 → 2.525
desc:   tf=0 → 0

pseudoTF("earbuds", B) = 2.525
TF_component = 2.525 × 2.2 / 3.725 = 1.491
IDF term = 0.470 × 1.491 = 0.701
```

**Score(B) = 0.239 + 0.701 = 0.940**

**Doc C — "wireless":**

```
title:  tf=0 → 0
desc:   tf=1, |d|=8, w=1.0 → 1.0 / (0.25 + 0.75×8/12.0) = 1.0/0.750 = 1.333

pseudoTF("wireless", C) = 1.333
TF_component = 1.333 × 2.2 / 2.533 = 1.158
IDF term = 0.134 × 1.158 = 0.155
```

**Doc C — "earbuds":** tf=0 everywhere → 0

**Score(C) = 0.155 + 0 = 0.155**

**Final ranking:** A (1.119) > B (0.940) > C (0.155) ✓

Doc A wins because both query terms appear in both fields, and its shorter title gets a length-normalization bonus.

---

## Field Parameter Defaults for E-Commerce

These starting values work for most product catalogs. Tune on actual relevance judgments.

| Field | `w_f` | `b_f` | Rationale |
|-------|-------|-------|-----------|
| title | 3.0 | 0.75 | Primary signal; length normalization matters |
| brand | 2.0 | 0.1 | Very short field; length normalization mostly off |
| category | 1.5 | 0.1 | Short, controlled vocabulary |
| description | 1.0 | 0.75 | Baseline; length normalization matters |
| tags/keywords | 1.2 | 0.3 | Semi-structured; partial normalization |

**b_f guidance:**
- Short, controlled fields (brand, category, tags): `b_f` near 0 (0.1–0.2). Length variation is noise, not signal.
- Free-text fields (title, description): `b_f` = 0.75, same as standard BM25. A 200-word description is genuinely different from a 20-word one.

**w_f guidance:**
- Title weight should be 2–5× description weight. Exact ratio depends on how well-written your descriptions are.
- If brand queries are common (users searching "Sony headphones"), raise `w_brand` to 2.5–3.0.
- If your titles are short and keyword-stuffed, reduce title weight; description becomes more reliable.

---

## Implementation

```python
import math
from collections import defaultdict

def tokenize(text: str, stop_words: set) -> list[str]:
    return [w for w in text.lower().split() if w.isalpha() and w not in stop_words]

class BM25F:
    def __init__(self, field_weights: dict, field_b: dict, k1: float = 1.2):
        """
        field_weights: {"title": 3.0, "description": 1.0, ...}
        field_b:       {"title": 0.75, "description": 0.75, ...}
        """
        self.field_weights = field_weights
        self.field_b = field_b
        self.k1 = k1
        self.fields = list(field_weights.keys())
        self.stop_words = {
            "the","a","an","and","or","but","of","in","on","at","to",
            "for","with","by","from","as","is","are","was","were","be","been","being"
        }

    def build_index(self, documents: list[dict]):
        """documents: [{"id": "SKU-1", "title": "...", "description": "...", ...}]"""
        self.docs = documents
        self.N = len(documents)

        # Per-field token counts and avgdl
        self.field_lengths = defaultdict(list)   # field -> [length per doc]
        self.tf = []                              # tf[doc_idx][field][term] = count
        self.df = defaultdict(int)               # term -> doc count (any field)

        for doc in documents:
            doc_tf = {}
            seen_terms = set()
            for field in self.fields:
                tokens = tokenize(doc.get(field, ""), self.stop_words)
                self.field_lengths[field].append(len(tokens))
                counts = defaultdict(int)
                for token in tokens:
                    counts[token] += 1
                    seen_terms.add(token)
                doc_tf[field] = counts
            self.tf.append(doc_tf)
            for term in seen_terms:
                self.df[term] += 1

        self.avgdl = {
            field: sum(lengths) / len(lengths) if lengths else 1
            for field, lengths in self.field_lengths.items()
        }

    def idf(self, term: str) -> float:
        df = self.df.get(term, 0)
        return math.log((self.N - df + 0.5) / (df + 0.5) + 1)

    def pseudo_tf(self, term: str, doc_idx: int) -> float:
        total = 0.0
        doc_tf = self.tf[doc_idx]
        for field in self.fields:
            tf_val = doc_tf[field].get(term, 0)
            if tf_val == 0:
                continue
            dl = self.field_lengths[field][doc_idx]
            avgdl = self.avgdl[field]
            b = self.field_b[field]
            w = self.field_weights[field]
            total += w * tf_val / (1 - b + b * dl / avgdl)
        return total

    def score(self, query: str, doc_idx: int) -> float:
        terms = tokenize(query, self.stop_words)
        total = 0.0
        for term in terms:
            ptf = self.pseudo_tf(term, doc_idx)
            if ptf == 0:
                continue
            tf_component = ptf * (self.k1 + 1) / (ptf + self.k1)
            total += self.idf(term) * tf_component
        return total

    def search(self, query: str, top_k: int = 10) -> list[dict]:
        scores = [
            (self.score(query, i), self.docs[i])
            for i in range(self.N)
        ]
        scores.sort(key=lambda x: x[0], reverse=True)
        return [
            {"doc_id": doc["id"], "score": round(s, 4), "title": doc.get("title", "")}
            for s, doc in scores[:top_k]
            if s > 0
        ]
```

**Usage:**

```python
bm25f = BM25F(
    field_weights={"title": 3.0, "brand": 2.0, "category": 1.5, "description": 1.0},
    field_b={"title": 0.75, "brand": 0.1, "category": 0.1, "description": 0.75},
    k1=1.2,
)
bm25f.build_index(products)
results = bm25f.search("wireless earbuds", top_k=20)
```

---

## Gotchas Specific to BM25F

**1. Averaging avgdl across documents with missing fields**

If 30% of your products have no description, `avgdl_description` will be pulled down by zero-length documents. This inflates the length normalization for documents that do have descriptions. Fix: compute `avgdl_f` only over documents where the field is non-empty, and treat missing fields as tf=0 (not as length=0).

```python
# Correct: exclude empty fields from avgdl
non_empty = [l for l in lengths if l > 0]
avgdl = sum(non_empty) / len(non_empty) if non_empty else 1
```

**2. Field weight is NOT a score multiplier**

`w_f` multiplies the **length-normalized TF** before saturation, not the final score. A title weight of 3.0 does not mean title contributes 3× as much to the final score — saturation compresses the effective difference. To reason about relative field contribution, simulate it: compute pseudoTF with only one field active and observe the saturation output.

**3. k₁ is shared — you cannot tune it per field**

BM25F uses a single `k₁` for the combined saturation step. If you need different saturation behavior per field, you must pre-saturate each field and then combine — but that's a different algorithm (field-independent BM25 sum), not BM25F.

**4. Stop-word removal must be consistent across all fields**

The same stop list applied in the parent skill must be applied identically to every field. Inconsistency causes length miscalculation (see parent SKILL.md warning on stop-word removal affecting `|d|` and `avgdl`). This is especially important for short fields like brand where removing one word changes length by 50%.

**5. Title keyword stuffing breaks `w_f` intent**

If merchants stuff titles ("wireless earbuds bluetooth earbuds true wireless earbuds"), a high title weight amplifies noise. Detect and cap title length (e.g., titles > 20 tokens may be stuffed); consider applying a more aggressive `b_title` (0.85–0.95) to penalize bloated titles.

---

## Parameter Tuning Decision Table

| Observation | Likely Cause | Adjustment |
|-------------|--------------|------------|
| Brand queries return wrong-brand products | `w_brand` too low or `b_brand` too high | Raise `w_brand` to 2.5–3.0; lower `b_brand` to 0.05 |
| Long-description products outrank concise titles | `w_title` too low relative to `w_desc` | Raise `w_title` or lower `w_desc` |
| Common words in category dominate scores | IDF not suppressing category terms | Check DF; if category has few unique terms, lower `w_category` |
| Exact title match loses to description-heavy doc | `b_title` too high (penalizing short exact titles) | Lower `b_title` to 0.5–0.6 |
| Repeated terms in description inflate scores | `k₁` too high | Lower `k₁` to 0.9–1.0 |

Minimum viable tuning loop:
1. Collect 50–100 queries with human relevance judgments (NDCG@10)
2. Grid search: `w_title` ∈ {2.0, 3.0, 4.0}, `w_brand` ∈ {1.5, 2.0, 2.5}, `b_title` ∈ {0.5, 0.75, 0.9}
3. Hold `k₁` at 1.2 and `b_desc` at 0.75 until field weights are stable
4. Only tune `k₁` last — it interacts with all fields simultaneously
