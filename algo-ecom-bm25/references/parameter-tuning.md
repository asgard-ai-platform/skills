# BM25 Parameter Tuning

Two parameters govern BM25 behavior: **k₁** (TF saturation) and **b** (length normalization). Default values (k₁=1.2, b=0.75) are reasonable starting points but are not optimal for all corpora. This document gives you a concrete procedure to tune them against your own catalog.

---

## What Each Parameter Controls

### k₁ — Term Frequency Saturation

The TF component of BM25:

```
TF_component = TF(t,d) × (k₁ + 1) / (TF(t,d) + k₁ × L_norm)
```

where `L_norm = 1 - b + b × |d| / avgdl`.

As TF → ∞, TF_component → (k₁ + 1). That ceiling is the saturation cap.

| k₁ value | Behavior |
|----------|----------|
| 0        | Ignores TF entirely — boolean: term present or not |
| 0.5–1.0  | Quick saturation; 3–4 occurrences ≈ diminishing returns |
| 1.2      | Default; reasonable for mixed short/long text |
| 2.0–3.0  | Slower saturation; rewards documents with many occurrences |
| ∞        | Degenerates to raw TF (unbounded) |

**Practical example.** With k₁=1.2 and L_norm=1.0:

| TF | TF_component |
|----|-------------|
| 1  | 1×2.2 / (1+1.2) = 1.00 |
| 2  | 2×2.2 / (2+1.2) = 1.375 |
| 5  | 5×2.2 / (5+1.2) = 1.774 |
| 10 | 10×2.2 / (10+1.2) = 1.964 |
| 50 | 50×2.2 / (50+1.2) = 2.148 |

Notice TF=50 gives only 2× the score of TF=1. If your domain rewards documents that repeat a term many times (e.g., a buyer's guide with 30 mentions of "wireless"), raise k₁. If keyword stuffing is a concern, keep it low.

### b — Document Length Normalization

The length penalty factor:

```
L_norm = 1 - b + b × (|d| / avgdl)
```

| b value | Behavior |
|---------|----------|
| 0       | No length normalization; long and short docs compared raw |
| 0.75    | Default; partial normalization |
| 1.0     | Full normalization; every doc treated as if avgdl length |

For a document twice the average length (`|d| / avgdl = 2`):

| b    | L_norm |
|------|--------|
| 0    | 1.00   |
| 0.25 | 1.25   |
| 0.5  | 1.50   |
| 0.75 | 1.75   |
| 1.0  | 2.00   |

Higher L_norm means the TF component is smaller (more penalized for length). A long document with TF=5 and b=1.0 will score lower than a short document with the same TF.

**E-commerce implication:** Product titles are short and dense; descriptions are long. If b is too high, title matches and description matches get equalized, hurting precision. If b is too low, a 500-word description with one mention of "wireless" can outrank a title "Wireless Earbuds."

---

## Decision Framework: Which Parameter to Tune First

```
Step 1: Fix b, grid-search k₁ (b has more impact on e-commerce corpora)
Step 2: With best k₁, grid-search b
Step 3: Verify on held-out queries
```

Do not grid-search both simultaneously on small datasets — the interaction effects are real but you won't have enough signal.

---

## Offline Tuning Procedure

### Prerequisites

You need a **relevance judgment set** (also called a qrel file):

```
query_id  doc_id   relevance_grade
q001      SKU-045  2               # highly relevant
q001      SKU-102  1               # somewhat relevant
q001      SKU-889  0               # not relevant
q002      SKU-017  2
...
```

A minimum viable set: **30 queries × 10 judged documents each = 300 judgments**. If you have less, your tuning will overfit. If you have none, use the heuristic defaults section below instead.

Relevance grades: 0 = irrelevant, 1 = partial, 2 = relevant. Use integer grades; fractional grades require more complex metrics.

### Metric: NDCG@10

Normalized Discounted Cumulative Gain at rank 10. This is the industry standard for search quality.

```
DCG@k = Σᵢ₌₁ᵏ  (2^rel_i - 1) / log₂(i + 1)

NDCG@k = DCG@k / IDCG@k
```

where IDCG@k is DCG@k when results are sorted in perfect relevance order.

**Worked example** for one query with grades [2, 1, 0, 2, 1] at ranks 1–5:

```
DCG@5 = (2²-1)/log₂(2) + (2¹-1)/log₂(3) + (2⁰-1)/log₂(4) + (2²-1)/log₂(5) + (2¹-1)/log₂(6)
      = 3/1 + 1/1.585 + 0/2 + 3/2.322 + 1/2.585
      = 3.0 + 0.631 + 0 + 1.292 + 0.387
      = 5.310

Perfect order = [2, 2, 1, 1, 0] → IDCG@5 = 3/1 + 3/1.585 + 1/2 + 1/2.322 + 0
             = 3.0 + 1.893 + 0.5 + 0.431 + 0 = 5.824

NDCG@5 = 5.310 / 5.824 = 0.912
```

Average NDCG@10 across all queries is your tuning objective. Higher = better.

If relevance judgments only have binary grades (0/1), use **MAP@10** (Mean Average Precision) instead — it degrades more gracefully on binary labels.

### Grid Search

Recommended search space for e-commerce:

```python
k1_values = [0.5, 0.75, 1.0, 1.2, 1.5, 2.0]
b_values  = [0.0, 0.25, 0.5, 0.75, 1.0]
```

That's 30 combinations — tractable. For each (k₁, b) pair:

1. Re-index corpus with that pair (or re-score if you cache the index)
2. Run all queries in your judgment set
3. Compute NDCG@10 per query, average across queries
4. Record result

```python
results = {}
for k1 in k1_values:
    for b in b_values:
        scores = []
        for query_id, query_text in queries.items():
            ranked = bm25_rank(corpus, query_text, k1=k1, b=b)
            ndcg = compute_ndcg(ranked, judgments[query_id], k=10)
            scores.append(ndcg)
        results[(k1, b)] = sum(scores) / len(scores)

best_params = max(results, key=results.get)
```

The bundled `scripts/bm25.py` exposes `--k1` and `--b` flags, so you can loop it from the shell if preferred:

```bash
python scripts/bm25.py --input '{"query":"...","corpus":[...]}' --k1 1.5 --b 0.5
```

### Validation Split

Split your judgment queries 80/20: use 80% for grid search, hold out 20% for final validation. Report the held-out NDCG@10. If held-out NDCG is more than 2 percentage points below in-sample, you are overfitting — your judgment set is too small.

---

## Heuristic Defaults When You Have No Relevance Judgments

If you cannot collect relevance judgments before launch, use these corpus-driven heuristics:

### Step 1: Measure your corpus characteristics

```python
doc_lengths = [len(tokenize(doc)) for doc in corpus]
avgdl = sum(doc_lengths) / len(doc_lengths)
cv = stdev(doc_lengths) / avgdl   # coefficient of variation
```

### Step 2: Choose b from length variance

| CV of document lengths | Recommended b |
|------------------------|---------------|
| < 0.5 (uniform length) | 0.25–0.5 |
| 0.5–1.0 (moderate variance) | 0.75 (default) |
| > 1.0 (high variance: titles mixed with long descriptions) | 0.9–1.0 |

E-commerce catalogs with both 3-word product titles and 500-word descriptions typically have CV > 1.0. Consider b=0.9.

### Step 3: Choose k₁ from query length

| Typical query length (tokens) | Recommended k₁ |
|-------------------------------|----------------|
| 1–2 words (head queries) | 0.5–1.0 |
| 2–4 words (standard) | 1.2 (default) |
| 4+ words (long-tail, conversational) | 1.5–2.0 |

Most e-commerce queries are 2–3 words. k₁=1.2 is appropriate.

### Step 4: Record your reasoning

Document why you chose specific values. When you collect relevance data later, you'll want to know the baseline.

---

## Corpus-Specific Observations for E-Commerce

These observations come from published IR literature and should be verified against your own data.

**Short-title catalogs** (fashion, electronics accessories):
- Average title length: 6–12 tokens post-stop-word removal
- Recommended: lower b (0.5–0.6) because penalizing "long" titles (15 words) is not meaningful when all titles are short
- k₁ doesn't matter much when TF > 2 is impossible in a 10-word title

**Long-description corpora** (technical/industrial parts, books):
- Average doc length after stop-word removal: 80–200+ tokens
- Recommended: higher b (0.8–1.0) to prevent long descriptions from dominating
- k₁=1.5–2.0 lets repeated technical terms (part numbers, material codes) influence ranking

**Mixed title+description in one field**:
- High CV (> 1.2 typically); use b close to 1.0
- Or, better: use BM25F (see `references/bm25f.md`) which keeps fields separate

---

## Interaction Between k₁ and b

The two parameters are not fully independent. When b is high (strong length penalty), documents are effectively normalized to the same length. In that regime, k₁ matters less because TF differences are already dampened by the length normalization.

Conversely, when b=0, raw document lengths affect scoring, and k₁ controls how aggressively you reward frequency. High k₁ + low b can amplify noise from long documents.

**Stable region for most corpora:** k₁ ∈ [0.8, 2.0] × b ∈ [0.5, 0.9]. Stay in this box unless your data strongly pulls you out.

---

## Common Tuning Mistakes

**Tuning on the training split and reporting training NDCG.** Always report held-out scores. Training NDCG is meaningless for parameter selection.

**Using too few queries.** With fewer than 20 queries, NDCG differences of < 3 percentage points are noise. Don't read into small differences.

**Tuning k₁ and b on different datasets.** Both must be tuned and validated on the same query distribution, or the interaction between them is not captured.

**Forgetting to re-apply stop-word removal when recomputing avgdl.** If you change your tokenizer (e.g., add a stop word), avgdl changes, which shifts all b-normalization. Reindex from scratch.

**Treating tuned parameters as permanent.** Catalog composition changes — seasonal additions, category expansions — shift avgdl and term distributions. Re-tune quarterly or when catalog size changes by > 20%.

---

## Quick Reference

```
Default: k₁=1.2, b=0.75

k₁ higher → rewards term repetition more
k₁ lower  → diminishing returns kick in faster (near-boolean at k₁=0)

b higher   → penalizes long documents more (levels the playing field)
b lower    → raw TF wins; long documents with many mentions score high

Tune order: fix b=0.75, grid k₁ first; then fix best k₁, grid b.
Metric: NDCG@10 (binary judgments → MAP@10)
Minimum judgment set: 30 queries × 10 docs
```
