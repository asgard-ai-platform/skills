---
name: "algo-price-van-westendorp"
description: "Conduct Van Westendorp Price Sensitivity Meter analysis to identify acceptable price ranges. Use this skill when the user needs to determine price boundaries for a new product, find the optimal and indifference price points, or survey-based pricing research — even if they say 'what should we charge', 'price sensitivity survey', or 'acceptable price range'."
metadata:
  category: "WP-39 定價演算法"
  tags: ["pricing", "van-westendorp", "survey", "price-sensitivity"]
---

# Van Westendorp Price Sensitivity Meter

## Overview

Van Westendorp PSM uses four price perception questions to identify an acceptable price range through intersection analysis. Produces: Point of Marginal Cheapness (PMC), Point of Marginal Expensiveness (PME), Indifference Price Point (IPP), and Optimal Price Point (OPP). Requires survey data from 100+ respondents.

## When to Use

**Trigger conditions:**
- Setting initial price for a new product or service
- Identifying the acceptable price range from consumer perception
- Quick pricing research without complex experimental design

**When NOT to use:**
- When you need to measure attribute trade-offs (use conjoint analysis)
- When you need demand curve estimation (use price elasticity)

## Algorithm

```
IRON LAW: Van Westendorp Identifies an ACCEPTABLE Range, Not Optimal Price
It doesn't account for competition, costs, or willingness to pay at
scale. It tells you WHERE prices are perceived as reasonable, not
what maximizes revenue. Use as input to pricing strategy, not as the
final answer.
```

### Phase 1: Input Validation
Survey 100+ target customers with four questions at various price points:
1. Too cheap (quality suspect)?  2. A bargain (great deal)?  3. Getting expensive (but would consider)?  4. Too expensive (would not buy)?
**Gate:** 100+ responses, all four curves plottable.

### Phase 2: Core Algorithm
1. For each price point, compute cumulative percentages for each question
2. Plot four curves: "too cheap" (descending), "cheap/bargain" (descending), "expensive" (ascending), "too expensive" (ascending)
3. Find intersections:
   - OPP = intersection of "too cheap" and "too expensive" (optimal price point)
   - IPP = intersection of "cheap" and "expensive" (indifference price point)
   - PMC = intersection of "too cheap" and "expensive" (marginal cheapness)
   - PME = intersection of "cheap" and "too expensive" (marginal expensiveness)
4. Acceptable range = [PMC, PME]

### Phase 3: Verification
Check: PMC < OPP < IPP < PME (expected ordering). All intersections exist within surveyed range.
**Gate:** Four-point ordering is logical, range is commercially viable.

### Phase 4: Output
Return price points and acceptable range.

## Output Format

```json
{
  "price_points": {"opp": 299, "ipp": 349, "pmc": 199, "pme": 449},
  "acceptable_range": {"min": 199, "max": 449},
  "metadata": {"respondents": 250, "currency": "TWD", "product": "..."}
}
```

## Examples

### Sample I/O
**Input:** 200 survey responses for a SaaS product, price range tested: $5-$50/month
**Expected:** PMC=$12, OPP=$18, IPP=$22, PME=$35. Acceptable range: $12-$35.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Curves don't intersect | Extend surveyed range | Price points tested were too narrow |
| IPP < OPP | Unusual but possible | Check data quality, may indicate confused respondents |
| Very wide range | Low price sensitivity | Product category has high tolerance |

## Gotchas

- **Hypothetical bias**: People say they'd pay more than they actually would. Van Westendorp systematically overestimates willingness to pay.
- **No competitive context**: Respondents answer in isolation. Real purchase decisions consider alternatives. Supplement with competitive analysis.
- **Sample representativeness**: Results are only valid for the surveyed population. B2B vs B2C, early adopters vs mainstream — all give different ranges.
- **Newton-Miller-Smith extension**: Add purchase intent questions at OPP and IPP for more actionable revenue estimates. Standard Van Westendorp alone lacks this.
- **Product must be understood**: Respondents need to understand what they're pricing. For novel products, include a clear concept description.

## References

- For Newton-Miller-Smith purchase intent extension, see `references/nms-extension.md`
- For survey design best practices, see `references/survey-design.md`
