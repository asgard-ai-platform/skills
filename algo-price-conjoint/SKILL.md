---
name: "algo-price-conjoint"
description: "Run conjoint analysis to measure how product attributes drive consumer preferences and willingness to pay. Use this skill when the user needs to quantify feature value trade-offs, estimate willingness to pay for specific features, or optimize product configuration — even if they say 'which features do customers value most', 'willingness to pay for feature X', or 'product attribute trade-offs'."
metadata:
  category: "WP-39 定價演算法"
  tags: ["pricing", "conjoint-analysis", "market-research", "preference"]
---

# Conjoint Analysis

## Overview

Conjoint analysis estimates the relative value consumers place on product attributes by analyzing their choices among hypothetical product profiles. Choice-Based Conjoint (CBC) is the most common variant. Produces part-worth utilities per attribute level and derived willingness-to-pay estimates.

## When to Use

**Trigger conditions:**
- Determining which features drive purchase decisions and how much they're worth
- Estimating willingness to pay for specific product features
- Optimizing product configuration for a target segment

**When NOT to use:**
- When you only need an acceptable price range (use Van Westendorp — simpler)
- When attributes can't be varied independently (natural constraints)

## Algorithm

```
IRON LAW: Conjoint Results Are Valid ONLY for Tested Attribute Levels
Extrapolating beyond tested ranges is unreliable. If you tested
prices $10-$50, you cannot predict preference at $100. The utility
function is only defined within the experimental design space.
```

### Phase 1: Input Validation
Define: attributes (3-7), levels per attribute (2-5 each), design type (full factorial if small, fractional/D-optimal if large). Survey 200+ respondents minimum.
**Gate:** Attributes independent, levels realistic, sample size sufficient.

### Phase 2: Core Algorithm
1. Generate choice sets using experimental design (D-optimal or balanced overlap)
2. Present respondents with sets of 3-4 product profiles, ask to choose preferred
3. Estimate part-worth utilities using multinomial logit (MNL) or hierarchical Bayes (HB)
4. Compute: attribute importance = range of part-worths within attribute / sum of all ranges
5. Derive WTP: utility-to-price conversion using the price attribute coefficient

### Phase 3: Verification
Check: holdout task prediction accuracy (hit rate > 60%), signs of part-worths are logical (higher price → lower utility).
**Gate:** Holdout hit rate acceptable, utilities directionally correct.

### Phase 4: Output
Return part-worth utilities, attribute importance, and WTP estimates.

## Output Format

```json
{
  "attribute_importance": [{"attribute": "price", "importance_pct": 35}, {"attribute": "brand", "importance_pct": 28}],
  "part_worths": {"price": {"$10": 2.1, "$30": 0.5, "$50": -1.8}},
  "wtp": {"feature_x": 12.50, "brand_premium": 8.00},
  "metadata": {"respondents": 300, "model": "hierarchical_bayes", "holdout_hit_rate": 0.72}
}
```

## Examples

### Sample I/O
**Input:** Laptop with attributes: Brand(Apple/Dell/Lenovo), RAM(8/16/32GB), Price($800/$1200/$1600)
**Expected:** Apple has highest brand utility, 32GB RAM preferred, price negative utility. WTP for Apple brand premium ≈ $200.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All attributes equally important | No clear driver | Product is commodity-like |
| Price dominates (>60%) | Highly price-sensitive market | Features don't differentiate enough |
| One level never chosen | Extreme negative utility | That level is a deal-breaker |

## Gotchas

- **Hypothetical bias**: Respondents making hypothetical choices may not reflect real purchase behavior. Incentive-compatible designs (real choices) are better but expensive.
- **Number of attributes**: More than 6-7 attributes overwhelms respondents, leading to simplification strategies (ignore some attributes). Keep designs manageable.
- **Interaction effects**: Standard analysis assumes attributes are independent. If brand affects price sensitivity (brand×price interaction), you need interaction terms.
- **Segment heterogeneity**: Average part-worths mask segments with opposite preferences. Use latent class or HB models to uncover segments.
- **Design efficiency**: Poor experimental designs (unbalanced, correlated attributes) produce imprecise estimates. Use proper design software.

## References

- For experimental design generation, see `references/experimental-design.md`
- For hierarchical Bayes estimation, see `references/hb-estimation.md`
