---
name: "algo-rank-wilson"
description: "Calculate Wilson Score confidence intervals for ranking items by positive proportion with sample size correction. Use this skill when the user needs to rank products by ratings, sort content by approval rate, or build a 'best rated' list that accounts for sample size — even if they say 'rank by star rating', 'best rated with few reviews', or 'confidence-adjusted rating'."
metadata:
  category: "WP-44 排名演算法"
  tags: ["ranking", "wilson-score", "confidence-interval", "rating"]
---

# Wilson Score Ranking

## Overview

Wilson Score interval provides a lower confidence bound on the true proportion of positive ratings. Unlike simple averages, it penalizes items with few ratings, preventing a 5/5 review item (1 review) from outranking a 4.8/5 item (1000 reviews). Computes in O(1) per item.

## When to Use

**Trigger conditions:**
- Ranking items by user ratings when review counts vary widely
- Building "top rated" or "best of" lists that are fair to well-reviewed items
- Sorting binary feedback (upvote/downvote) with confidence

**When NOT to use:**
- For continuous scores (use Bayesian average instead)
- When comparing items with similar sample sizes (simple average suffices)

## Algorithm

```
IRON LAW: Never Rank by Simple Average When Sample Sizes Differ
A 5.0 average from 1 review is NOT better than 4.8 from 1000 reviews.
Wilson Score lower bound accounts for sample uncertainty:
Items with few ratings get a LOWER bound, properly reflecting our
uncertainty about their true quality.
```

### Phase 1: Input Validation
Collect per item: number of positive ratings (p), total ratings (n). For star ratings, convert to binary (e.g., 4-5 stars = positive).
**Gate:** n > 0 for all items, confidence level chosen (typically 95%, z=1.96).

### Phase 2: Core Algorithm
1. Compute observed proportion: p̂ = positive / total
2. Wilson lower bound: (p̂ + z²/2n - z × √(p̂(1-p̂)/n + z²/4n²)) / (1 + z²/n)
3. Rank by Wilson lower bound descending (conservative estimate of true quality)

### Phase 3: Verification
Check: items with many positive reviews rank above items with few reviews and same proportion. Items with very few reviews are appropriately penalized.
**Gate:** Ranking intuitively correct on manual inspection.

### Phase 4: Output
Return ranked items with scores and confidence intervals.

## Output Format

```json
{
  "rankings": [{"item": "Product_A", "wilson_lower": 0.89, "positive": 950, "total": 1000, "proportion": 0.95}],
  "metadata": {"confidence": 0.95, "z": 1.96, "items_ranked": 500}
}
```

## Examples

### Sample I/O
**Input:** Item A: 1 positive / 1 total (100%). Item B: 950 positive / 1000 total (95%).
**Expected:** B ranks higher. Wilson lower: A ≈ 0.05, B ≈ 0.94. The single review gives almost no confidence.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| 0 reviews | Cannot rank | n=0, undefined. Exclude or assign minimum |
| 0 positive, 100 total | Very low score | Genuinely bad item, high confidence |
| 1M positive, 1M total | Lower bound ≈ 1.0 | Massive sample, high confidence in 100% |

## Gotchas

- **Binary conversion**: For 5-star ratings, the positive/negative threshold matters. 4+ stars as positive? 3+ stars? Different thresholds produce different rankings.
- **Not for continuous data**: Wilson Score is for proportions (binary outcomes). For continuous ratings, use Bayesian average with a prior.
- **Cold start**: New items with zero reviews can't be ranked. Use a minimum review threshold or Bayesian smoothing.
- **Confidence level choice**: Higher confidence (99%) penalizes small samples more aggressively. 95% is standard but tune for your use case.
- **Sorting by lower bound is conservative**: This approach favors well-known items. For discovery/exploration, consider also boosting items with high upper bounds (potential hidden gems).

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/wilson_score.py` | Compute Wilson score interval and rank items | `python scripts/wilson_score.py --help` |

Run `python scripts/wilson_score.py --verify` to execute built-in sanity tests.

## References

- For Bayesian average alternative, see `references/bayesian-average.md`
- For Reddit's ranking algorithm (Wilson-based), see `references/reddit-ranking.md`
