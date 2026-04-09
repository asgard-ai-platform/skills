# BM25 vs TF-IDF: Formula Comparison and Migration Guide

BM25 (Best Match 25) is the de facto successor to TF-IDF in information retrieval. It fixes two structural weaknesses in classic TF-IDF: **unbounded term frequency saturation** and **no document length normalization**. This document gives you the formulas, a side-by-side worked example, and a decision table for choosing between them.

---

## The Core Problem with Classic TF-IDF

Classic TF-IDF (log-normalized variant) computes:

```
TF(t, d)        = log(1 + count(t, d))
IDF(t)          = log(N / DF(t))
Score(t, d)     = TF(t, d) × IDF(t)
```

Two issues:

**1. TF grows without bound.** A term appearing 100× in a document scores much higher than one appearing 10×, even though the marginal informativeness of each additional occurrence drops sharply. A document about "machine learning" that mentions "learning" 200 times isn't 20× more relevant than one mentioning it 10 times.

**2. Long documents are unfairly penalized or rewarded.** A 5,000-word document will accumulate higher raw TF counts than a 500-word document purely because of length, not relevance density.

BM25 addresses both with two parameters: **k1** (TF saturation) and **b** (length normalization).

---

## BM25 Formula

The BM25 score for a query Q with terms t₁…tₙ against document d:

```
BM25(Q, d) = Σ IDF(tᵢ) × [ f(tᵢ, d) × (k1 + 1) ]
                             ─────────────────────────────────────────
                             [ f(tᵢ, d) + k1 × (1 - b + b × |d|/avgdl) ]
```

Where:
- `f(tᵢ, d)` = raw term frequency of tᵢ in d (NOT log-normalized — BM25 does its own saturation)
- `|d|` = length of document d in tokens
- `avgdl` = average document length across the corpus
- `k1` ∈ [1.2, 2.0] — TF saturation parameter (default: 1.5)
- `b` ∈ [0, 1] — length normalization parameter (default: 0.75)

**IDF variant used in BM25 (Robertson-Spärck Jones):**

```
IDF(t) = log( (N - DF(t) + 0.5) / (DF(t) + 0.5) + 1 )
```

This differs from classic TF-IDF's `log(N / DF(t))`. The `+0.5` smoothing prevents division-by-zero and slightly dampens IDF for very rare terms.

---

## Parameter Semantics

### k1: TF Saturation Ceiling

As `f(t, d) → ∞`, the BM25 TF component approaches `(k1 + 1)`, never exceeding it:

```
lim_{f→∞}  f × (k1 + 1) / (f + k1) = k1 + 1
```

| k1 value | Effect |
|----------|--------|
| 0 | Pure IDF — TF completely ignored (boolean retrieval) |
| 1.2 | Strong saturation — 3rd occurrence ≈ 75% value of 1st |
| 2.0 | Moderate saturation — term frequency still matters more |
| ∞ | Approaches classic TF (no saturation) |

### b: Length Normalization

| b value | Effect |
|---------|--------|
| 0 | No length normalization — long documents have raw TF advantage |
| 0.75 | Default — moderate normalization |
| 1.0 | Full normalization — scores purely by term density |

**Practical defaults:** k1=1.5, b=0.75 work well for most English web corpora. For short documents (tweets, product titles), reduce b toward 0.3.

---

## Worked Example

**Corpus (3 documents):**

| Doc | Content | Token count |
|-----|---------|-------------|
| d1 | "machine learning machine learning machine" | 5 |
| d2 | "machine learning deep learning neural networks" | 6 |
| d3 | "neural networks classification" | 3 |

```
avgdl = (5 + 6 + 3) / 3 = 4.67
N = 3
```

**Query:** "machine learning"

**Step 1: Compute DF and IDF**

| Term | DF | TF-IDF IDF = log(3/DF) | BM25 IDF = log((N-DF+0.5)/(DF+0.5)+1) |
|------|----|-----------------------|---------------------------------------|
| machine | 2 | log(3/2) = 0.405 | log((3-2+0.5)/(2+0.5)+1) = log(1.6) = 0.470 |
| learning | 2 | log(3/2) = 0.405 | log((1.5/2.5)+1) = log(1.6) = 0.470 |

**Step 2: TF-IDF scores (log-normalized TF)**

| Doc | TF(machine) | TF(learning) | TF-IDF score |
|-----|-------------|--------------|--------------|
| d1 | log(1+3)=1.386 | log(1+2)=1.099 | 1.386×0.405 + 1.099×0.405 = **1.006** |
| d2 | log(1+1)=0.693 | log(1+2)=1.099 | 0.693×0.405 + 1.099×0.405 = **0.727** |
| d3 | 0 | 0 | **0** |

**Step 3: BM25 scores (k1=1.5, b=0.75)**

Length normalization factor for each doc:
```
norm(d1) = 1 - 0.75 + 0.75 × (5/4.67) = 1 - 0.75 + 0.803 = 1.053
norm(d2) = 1 - 0.75 + 0.75 × (6/4.67) = 1 - 0.75 + 0.964 = 1.214
norm(d3) = 1 - 0.75 + 0.75 × (3/4.67) = 1 - 0.75 + 0.482 = 0.732
```

BM25 TF component for term t in doc d:
```
BM25_TF(t, d) = f(t,d) × (k1 + 1) / (f(t,d) + k1 × norm(d))
```

**d1 (length=5):**
```
BM25_TF(machine, d1) = 3 × 2.5 / (3 + 1.5 × 1.053) = 7.5 / 4.580 = 1.637
BM25_TF(learning, d1) = 2 × 2.5 / (2 + 1.5 × 1.053) = 5.0 / 3.580 = 1.397
Score(d1) = 0.470 × 1.637 + 0.470 × 1.397 = 0.769 + 0.657 = 1.426
```

**d2 (length=6):**
```
BM25_TF(machine, d2) = 1 × 2.5 / (1 + 1.5 × 1.214) = 2.5 / 2.821 = 0.886
BM25_TF(learning, d2) = 2 × 2.5 / (2 + 1.5 × 1.214) = 5.0 / 3.821 = 1.309
Score(d2) = 0.470 × 0.886 + 0.470 × 1.309 = 0.416 + 0.615 = 1.031
```

**d3:** Score = 0

**Ranking comparison:**

| Rank | TF-IDF | BM25 |
|------|--------|------|
| 1st | d1 (1.006) | d1 (1.426) |
| 2nd | d2 (0.727) | d2 (1.031) |

Both agree here, but notice **the gap is larger in BM25**. d1 has "machine" 3×, and BM25 gives it more credit — but with saturation so "machine ×10" would not dominate infinitely. TF-IDF's log normalization also compresses differences but in a less theoretically motivated way.

---

## Where Rankings Actually Diverge

Classic TF-IDF and BM25 often agree on rank order for short, similar-length documents. **Divergence appears when:**

### Case 1: Very long documents with high raw TF

A 10,000-token document mentioning "python" 50 times vs. a 200-token document mentioning it 5 times:

```
TF-IDF: log(1+50) ≈ 3.93  vs  log(1+5) ≈ 1.79  → long doc wins by 2.2×
BM25 (b=0.75): long doc is penalized by length → scores converge
```

BM25 correctly demotes the verbose document if its term density is similar.

### Case 2: Very high TF in a single document

A document that repeats a keyword 200 times (keyword stuffing):

```
TF-IDF: log(201) ≈ 5.3
BM25 (k1=1.5): saturates near (k1+1)=2.5 regardless of count
```

BM25 is naturally resistant to term-spam. TF-IDF is not.

### Case 3: Short snippets in a corpus of long articles

With b=0.75, BM25 slightly penalizes documents shorter than `avgdl`. For a corpus where `avgdl=1000` and a snippet has length 50, the length factor is `1 - 0.75 + 0.75×(50/1000) = 0.288` — which actually *boosts* short documents relative to long ones (denominator is smaller). Short docs with exact term matches rank highly. This can be desirable (FAQ answers) or noisy (boilerplate headers).

---

## Python Implementation

Minimal BM25 scorer, stdlib only, compatible with the TF-IDF script conventions in this skill:

```python
import math
from collections import Counter

def tokenize(text: str) -> list[str]:
    return text.lower().split()

def build_bm25_index(corpus: list[str], k1: float = 1.5, b: float = 0.75) -> dict:
    tokenized = [tokenize(doc) for doc in corpus]
    N = len(tokenized)
    avgdl = sum(len(d) for d in tokenized) / N

    # Document frequency
    df = Counter()
    for doc_tokens in tokenized:
        for term in set(doc_tokens):
            df[term] += 1

    # IDF (Robertson-Spärck Jones)
    idf = {
        term: math.log((N - df[term] + 0.5) / (df[term] + 0.5) + 1)
        for term in df
    }

    return {
        "tokenized": tokenized,
        "idf": idf,
        "avgdl": avgdl,
        "k1": k1,
        "b": b,
        "N": N,
    }

def score_query(index: dict, query: str) -> list[tuple[int, float]]:
    k1, b, avgdl = index["k1"], index["b"], index["avgdl"]
    query_terms = tokenize(query)
    scores = []

    for i, doc_tokens in enumerate(index["tokenized"]):
        tf = Counter(doc_tokens)
        dl = len(doc_tokens)
        norm = 1 - b + b * (dl / avgdl)
        score = 0.0
        for term in query_terms:
            if term not in index["idf"]:
                continue
            f = tf.get(term, 0)
            bm25_tf = f * (k1 + 1) / (f + k1 * norm)
            score += index["idf"][term] * bm25_tf
        scores.append((i, score))

    return sorted(scores, key=lambda x: -x[1])
```

Usage:
```python
corpus = ["machine learning machine learning machine",
          "machine learning deep learning neural networks",
          "neural networks classification"]

index = build_bm25_index(corpus)
results = score_query(index, "machine learning")
# → [(0, 1.426), (1, 1.031), (2, 0.0)]
```

---

## Decision Table: TF-IDF vs BM25

| Condition | Use TF-IDF | Use BM25 |
|-----------|-----------|---------|
| Documents have similar lengths | ✓ acceptable | ✓ also fine |
| Mixed-length corpus (articles + snippets) | ✗ length bias | ✓ b param normalizes |
| Corpus has spam/repetitive text | ✗ exploitable | ✓ saturates naturally |
| Need interpretable scores for debugging | ✓ simpler math | ✓ still interpretable |
| Need to implement from scratch, no deps | ✓ simpler | ✓ 20 extra lines |
| scikit-learn pipeline integration | ✓ `TfidfVectorizer` | ✗ no native support |
| Production search (Elasticsearch, Solr) | ✗ not default | ✓ default scoring function |
| Very small corpus (< 50 docs) | ✓ differences negligible | ✓ differences negligible |

**Rule of thumb:** If you have a homogeneous corpus where documents are roughly the same length (e.g., all product descriptions, all news headlines), TF-IDF and BM25 produce nearly identical rankings. Switch to BM25 when document length varies by more than 5×.

---

## IDF Formula Differences and Their Effect

Three IDF variants appear in practice:

```
Classic:          log(N / DF(t))                           # → 0 for universal terms
TF-IDF smoothed:  log(N / (DF(t) + 1)) + 1               # sklearn default
BM25 (RSJ):       log((N - DF(t) + 0.5) / (DF(t) + 0.5) + 1)
```

The RSJ variant has a useful property: **it can go negative** when `DF(t) > N/2` (a term appearing in more than half the corpus). This effectively *penalizes* extremely common terms beyond just zeroing them out. In classic TF-IDF, such terms just approach zero from above.

For query terms not seen in the corpus (OOV):
- Classic IDF: division by zero — must guard with `DF+1` smoothing
- BM25 RSJ: `log((N+0.5)/0.5+1) = log(2N+2)` — automatically handles it

This is the smoothing fix mentioned in the parent skill's Gotchas section (`IDF = log(N/(DF+1))+1`).

---

## BM25 Variants

**BM25+** adds a floor δ to the TF component to prevent zero scores for matching terms:

```
BM25+_TF(t, d) = f(t,d) × (k1+1) / (f(t,d) + k1×norm) + δ
```

Typical δ=1.0. Prevents a document with a single query-term match from scoring identically to one with no matches. Rarely needed unless you observe many tied-zero results.

**BM25F** (Field-weighted BM25) applies separate weights and length normalization per field (title, body, anchor text). Used in Elasticsearch's `multi_match` with `type: best_fields`. Not covered here — see Elasticsearch BM25F documentation.

---

## Migration Checklist: TF-IDF → BM25

1. **Replace log-normalized TF** with raw `f(t, d)` — BM25 does its own saturation
2. **Replace IDF formula** with RSJ variant above
3. **Add length normalization** — compute `avgdl` from corpus at index time
4. **Choose k1 and b** — start with (1.5, 0.75), tune on a held-out relevance set
5. **Drop L2 normalization** — BM25 scores are not designed for cosine similarity; if you need vector similarity, use embeddings instead
6. **Rebuild all stored scores** — IDF is corpus-dependent; adding documents requires recomputing `avgdl` and all IDF values, same as TF-IDF
