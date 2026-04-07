---
name: "algo-rank-bayesian"
description: "Apply Bayesian averaging to rank items by combining observed ratings with prior expectations. Use this skill when the user needs to rank items with varying review counts, build a 'top rated' list that handles low-sample items fairly, or implement IMDB-style weighted rating — even if they say 'weighted average rating', 'IMDB formula', or 'ranking with prior'."
metadata:
  category: "WP-44 排名演算法"
  tags: ["ranking", "bayesian-average", "rating", "prior"]
---

# Bayesian Average Rating

## Overview

Bayesian average combines an item's observed average rating with a prior (global average), weighted by review count. Formula: BR = (C × m + Σrᵢ) / (C + n) where m=global mean, C=confidence parameter, n=item reviews, Σrᵢ=sum of item ratings. Items with few reviews are pulled toward the global mean.

## When to Use

**Trigger conditions:**
- Ranking items by continuous ratings (1-5 stars) with varying review counts
- IMDB-style "Top 250" lists that balance quality and popularity
- Any rating aggregation where new items shouldn't dominate with few high ratings

**When NOT to use:**
- For binary (upvote/downvote) data (use Wilson Score instead)
- When all items have similar review counts (simple average is sufficient)

## Algorithm

```
IRON LAW: The Prior Protects Against Small-Sample Extremes
Without a prior, a single 5-star review makes an item "the best."
The Bayesian average adds C "phantom votes" at the global mean m,
shrinking small-sample items toward average. C controls shrinkage
strength: higher C = more conservative (more phantom votes).
Typical C = median review count across all items.
```

### Phase 1: Input Validation
Compute: global mean rating (m) across all items, choose C (phantom vote count). Collect per item: review count (n), average rating, or sum of ratings.
**Gate:** m computed, C selected, item data available.

### Phase 2: Core Algorithm
1. Global mean: m = Σ(all ratings) / Σ(all review counts)
2. Bayesian average per item: BR = (C × m + n × avg_rating) / (C + n)
3. Rank items by BR descending
4. For items with n >> C, BR ≈ avg_rating (data dominates). For n << C, BR ≈ m (prior dominates).

### Phase 3: Verification
Check: items with very few reviews should be near global mean. Items with many reviews should be near their actual average. Ranking is intuitive.
**Gate:** Shrinkage behavior confirmed, top items have both high ratings AND sufficient reviews.

### Phase 4: Output
Return ranked items with Bayesian scores.

## Output Format

```json
{
  "rankings": [{"item": "Movie_A", "bayesian_avg": 8.7, "raw_avg": 9.1, "reviews": 5000, "shrinkage": 0.04}],
  "metadata": {"global_mean": 6.8, "confidence_C": 500, "items_ranked": 10000}
}
```

## Examples

### Sample I/O
**Input:** m=7.0, C=100. Item A: avg=9.5, n=5. Item B: avg=8.5, n=500.
**Expected:** BR_A = (100×7 + 5×9.5)/(105) = 7.12. BR_B = (100×7 + 500×8.5)/(600) = 8.25. B ranks higher.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| n=0 | BR = m (global mean) | No data, fully prior-driven |
| n=100000 | BR ≈ raw average | Massive sample overwhelms prior |
| All items same n | Equivalent to simple average ranking | Uniform shrinkage, ordering preserved |

## Gotchas

- **C selection is subjective**: Common choices: median review count, minimum reviews for "reliable" rating (IMDB uses top 25,000 voters with min votes). No universally correct value.
- **Rating scale matters**: A 4.0 on a 5-point scale means something different than 4.0 on a 10-point scale. Normalize or use the same scale.
- **Category-specific priors**: A 4.0 average in "horror movies" might be exceptional, while 4.0 in "Studio Ghibli" might be below average. Consider category-level priors.
- **Temporal bias**: Old items accumulate reviews. Unless you weight recent reviews more, established items permanently dominate "top" lists.
- **Review gaming**: Bayesian average doesn't prevent review manipulation — it only mitigates small-sample extremes. Pair with fraud detection.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/bayesian_avg.py` | Rank items using Bayesian average to handle small-sample extremes | `python scripts/bayesian_avg.py --help` |

Run `python scripts/bayesian_avg.py --verify` to execute built-in sanity tests.

## References

- For IMDB weighted rating formula, see `references/imdb-formula.md`
- For multi-dimensional Bayesian rating, see `references/multi-dimensional.md`
