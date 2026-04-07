---
name: "algo-ecom-search"
description: "Optimize e-commerce search relevance across the full pipeline from query understanding to result presentation. Use this skill when the user needs to improve search quality, implement query processing features, or diagnose search relevance issues — even if they say 'search results are bad', 'improve product search', or 'search relevance optimization'."
metadata:
  category: "WP-43 電商搜尋演算法"
  tags: ["ecommerce", "search", "relevance", "query-understanding"]
---

# E-Commerce Search Relevance

## Overview

E-commerce search is a pipeline: query understanding → retrieval → ranking → presentation. Each stage affects relevance. Optimization requires diagnosing WHICH stage fails, not just tuning one component. Zero-result rate, click-through rate, and add-to-cart rate are key metrics.

## When to Use

**Trigger conditions:**
- Diagnosing why search results don't meet user expectations
- Implementing query processing features (spell check, synonyms, intent detection)
- Reducing zero-result searches and improving conversion

**When NOT to use:**
- For ranking algorithm design only (use e-commerce ranking skill)
- For text relevance scoring only (use BM25)

## Algorithm

```
IRON LAW: Search Quality Is Determined by the WEAKEST Pipeline Stage
Query understanding, retrieval, ranking, and presentation are sequential.
Perfect ranking cannot fix bad retrieval (missing products). Perfect
retrieval cannot fix bad query understanding (wrong intent). Diagnose
which stage fails FIRST before optimizing.
```

### Phase 1: Input Validation
Audit current search: sample 100 queries by volume. For each, evaluate: query understanding (correct intent?), retrieval (relevant products in candidate set?), ranking (best products at top?), presentation (useful display?).
**Gate:** Weakness localized to specific pipeline stage(s).

### Phase 2: Core Algorithm
**Query understanding:** 1. Spell correction (edit distance, n-gram). 2. Synonym expansion (earbuds↔earphones). 3. Intent classification (product search vs brand search vs category browse). 4. Query rewriting (attribute extraction: "red shoes size 10" → color:red, category:shoes, size:10).

**Retrieval optimization:** 1. Multi-field search (title, description, brand, category, SKU). 2. Boosting strategies (title match > description match). 3. Filter vs boost (hard constraints: category, availability vs soft signals: popularity).

**Result quality:** 1. Zero-result fallback (relax query, suggest alternatives). 2. Faceted navigation (filters by price, brand, rating). 3. Did-you-mean suggestions.

### Phase 3: Verification
Measure: zero-result rate (<5% target), CTR on first page (>30% target), NDCG on judged queries.
**Gate:** Key metrics improve over baseline.

### Phase 4: Output
Return search audit with prioritized improvements.

## Output Format

```json
{
  "audit": {"zero_result_rate": 0.08, "avg_ctr": 0.25, "top_failing_queries": ["earbuds wireless", "gift ideas"]},
  "recommendations": [{"stage": "query_understanding", "issue": "no_synonym_expansion", "impact": "high", "fix": "Add earbuds↔earphones synonym"}],
  "metadata": {"queries_sampled": 100, "period": "2025-Q1"}
}
```

## Examples

### Sample I/O
**Input:** "wireles earbud" (misspelled) returns 0 results
**Expected:** Spell correction → "wireless earbuds" → relevant products displayed. Recommendation: implement spell correction.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Category-only query ("shoes") | Browse intent, show popular | Not a specific product search |
| Brand misspelling | Fuzzy brand matching | "Nikee" → "Nike" |
| Long-tail query ("blue cotton v-neck t-shirt men XL") | Attribute parsing needed | Multiple structured attributes in free text |

## Gotchas

- **Synonym maintenance**: Synonym lists need ongoing curation. "AirPods" is a brand, not a synonym for "earbuds." Wrong synonyms hurt precision.
- **Over-recall**: Aggressive synonym expansion and fuzzy matching return too many irrelevant results. Balance recall (find everything) with precision (only relevant).
- **Language-specific challenges**: Chinese search needs word segmentation. "皮鞋" (leather shoes) should not match "拖鞋" (slippers) despite shared "鞋".
- **Search analytics are essential**: Without tracking query-level CTR, zero-result queries, and conversion rates, you're optimizing blind.
- **A/B testing search is hard**: Search changes affect all queries. Some improve, some regress. Measure aggregate metrics AND stratify by query type.

## References

- For query understanding pipeline architecture, see `references/query-pipeline.md`
- For search relevance evaluation methodology, see `references/relevance-evaluation.md`
