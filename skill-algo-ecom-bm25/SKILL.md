---
name: "skill-algo-ecom-bm25"
description: "Implement BM25 ranking function for e-commerce product search relevance scoring. Use this skill when the user needs to build a text-based product search engine, improve search result relevance, or replace basic TF-IDF with a more robust ranking function — even if they say 'product search ranking', 'search relevance', or 'BM25 implementation'."
metadata:
  category: "WP-43 電商搜尋演算法"
  tags: ["ecommerce", "bm25", "search", "information-retrieval"]
---

# BM25 Ranking Function

## Overview

BM25 (Best Matching 25) is an improved TF-IDF ranking function that adds term frequency saturation and document length normalization. Score = Σ IDF(t) × (TF(t,d) × (k₁+1)) / (TF(t,d) + k₁ × (1 - b + b × |d|/avgdl)). Standard parameters: k₁=1.2, b=0.75. The backbone of most text search engines (Elasticsearch, Solr).

## When to Use

**Trigger conditions:**
- Building product search with text-based relevance ranking
- Replacing basic TF-IDF with better document length normalization
- Tuning search relevance in Elasticsearch/Solr

**When NOT to use:**
- When semantic similarity matters more than keyword matching (use embeddings)
- For single-field exact matching (simpler methods suffice)

## Algorithm

```
IRON LAW: BM25 Has Two Critical Parameters — k₁ and b
k₁ controls term frequency saturation: higher k₁ = more weight to
repeated terms. k₁=0 ignores TF entirely (boolean).
b controls document length normalization: b=1 fully normalizes by
length, b=0 ignores length. Default k₁=1.2, b=0.75 works for most
cases but MUST be tuned for your specific corpus.
```

### Phase 1: Input Validation
Build inverted index: term → list of (document, term frequency). Compute: document lengths, average document length, document frequency per term.
**Gate:** Index built, statistics computed, corpus non-empty.

### Phase 2: Core Algorithm
For query Q with terms t₁...tₙ against document d:
1. For each query term tᵢ: compute IDF(tᵢ) = log((N - DF(tᵢ) + 0.5) / (DF(tᵢ) + 0.5) + 1)
2. Compute TF component: (TF(tᵢ,d) × (k₁+1)) / (TF(tᵢ,d) + k₁ × (1 - b + b × |d|/avgdl))
3. Score(d, Q) = Σᵢ IDF(tᵢ) × TF_component(tᵢ, d)
4. Rank documents by score descending

### Phase 3: Verification
Spot-check: query "red shoes" should rank documents containing both "red" and "shoes" higher than documents with only one term. Shorter product titles with both terms should rank above long descriptions with sparse mentions.
**Gate:** Relevance spot-check passes on 10+ test queries.

### Phase 4: Output
Return ranked results with scores.

## Output Format

```json
{
  "results": [{"doc_id": "SKU-123", "score": 12.5, "title": "Red Running Shoes"}],
  "metadata": {"query": "red shoes", "hits": 85, "k1": 1.2, "b": 0.75, "avg_doc_length": 45}
}
```

## Examples

### Sample I/O
**Input:** Query "wireless earbuds", corpus of 1000 product listings
**Expected:** Products with "wireless earbuds" in title rank highest; "wireless headphones" ranks lower (no "earbuds" term).

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Single-word query | IDF-dominated ranking | Only one term's IDF differentiates |
| Very common term ("the") | Near-zero IDF, low impact | IDF suppresses common terms |
| Document with 100 repetitions | Saturated TF, not 100x score | k₁ caps the benefit of repetition |

## Gotchas

- **Multi-field scoring**: E-commerce products have title, description, brand, category. Weight fields differently: title match > description match. Use field-boosted BM25.
- **Synonyms and stemming**: BM25 is keyword-exact. "earphones" won't match "earbuds." Add synonym expansion and stemming in the query pipeline.
- **Parameter tuning**: Default k₁=1.2, b=0.75 is reasonable but not optimal. Tune on relevance judgments specific to your catalog.
- **Numeric attributes**: BM25 doesn't handle numeric filtering (price range, ratings). Use it for text relevance, then combine with numeric filters.
- **Zero-result queries**: When BM25 returns nothing, fall back to fuzzy matching or semantic search rather than showing empty results.

## References

- For BM25F multi-field extension, see `references/bm25f.md`
- For parameter tuning methodology, see `references/parameter-tuning.md`
