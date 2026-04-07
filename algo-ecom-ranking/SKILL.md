---
name: "algo-ecom-ranking"
description: "Design multi-objective e-commerce product ranking combining relevance, conversion, and business metrics. Use this skill when the user needs to build a product ranking system beyond text relevance, balance relevance with commercial objectives, or implement learning-to-rank — even if they say 'product sorting', 'search result ranking', or 'how to rank products'."
metadata:
  category: "WP-43 電商搜尋演算法"
  tags: ["ecommerce", "ranking", "learning-to-rank", "multi-objective"]
---

# E-Commerce Product Ranking

## Overview

E-commerce ranking combines text relevance (BM25) with commercial signals (CTR, conversion rate, revenue, margin) into a unified ranking score. Uses learning-to-rank (LTR) models trained on click and conversion data to optimize for business-relevant outcomes.

## When to Use

**Trigger conditions:**
- Building a product search/browse ranking beyond pure text relevance
- Incorporating business metrics (margin, inventory) into ranking
- Implementing a learning-to-rank pipeline

**When NOT to use:**
- For pure text search relevance only (use BM25)
- When no click/conversion data exists (start with rule-based ranking)

## Algorithm

```
IRON LAW: Relevance Is Necessary But NOT Sufficient for E-Commerce Ranking
A result that is textually relevant but has zero sales history, no
reviews, and is out of stock serves no one. E-commerce ranking must
balance: relevance (does it match the query?), quality (is it a good
product?), and commercial value (does it generate revenue?).
```

### Phase 1: Input Validation
Collect features per product-query pair: text relevance score (BM25), historical CTR, conversion rate, average rating, review count, price competitiveness, inventory level, margin.
**Gate:** Minimum features available, click data from 30+ days.

### Phase 2: Core Algorithm
**Rule-based baseline:** Score = w₁×relevance + w₂×popularity + w₃×rating + w₄×recency. Manually tune weights.

**LTR approach:**
1. Generate training data from click logs (clicked = positive, skipped = negative, with position debiasing)
2. Features: text match, behavioral (CTR, add-to-cart rate), product quality (rating, reviews), freshness, price
3. Train: LambdaMART or gradient-boosted ranking model optimizing NDCG
4. Blend: final_score = α × LTR_score + (1-α) × business_boost

### Phase 3: Verification
Evaluate offline: NDCG@10, MRR. A/B test online: revenue per search, click-through rate, conversion rate.
**Gate:** NDCG improves over baseline, A/B test positive on primary metric.

### Phase 4: Output
Return ranked product list with score decomposition.

## Output Format

```json
{
  "results": [{"product_id": "P123", "rank": 1, "final_score": 0.92, "components": {"relevance": 0.85, "popularity": 0.95, "quality": 0.90}}],
  "metadata": {"query": "wireless earbuds", "model": "lambdamart", "ndcg_at_10": 0.72}
}
```

## Examples

### Sample I/O
**Input:** Query "laptop", 500 matching products
**Expected:** Top results balance text match + high conversion + good ratings, not just keyword relevance.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| New product, no history | Rely on text relevance + category avg | Cold start — no behavioral signal |
| Out of stock item | Demote or remove | Showing unavailable products frustrates users |
| Sponsored product | Blend ad rank with organic | Separate sponsored from organic clearly |

## Gotchas

- **Position bias in training data**: Higher-ranked items get more clicks regardless of quality. Debias training data using inverse propensity weighting or randomization experiments.
- **Popularity bias**: Without diversity controls, popular items dominate rankings. New or niche products get no exposure. Add exploration bonus.
- **Revenue optimization ≠ user satisfaction**: Ranking by margin pushes expensive products up. Users lose trust if results feel commercially manipulated.
- **Feature freshness**: Click signals change daily. Retrain or update features frequently. Stale features degrade ranking quality.
- **Category-specific models**: A single ranking model may not work across all categories. Electronics ranking differs from fashion ranking.

## References

- For LambdaMART implementation, see `references/lambdamart.md`
- For position debiasing techniques, see `references/position-debiasing.md`
