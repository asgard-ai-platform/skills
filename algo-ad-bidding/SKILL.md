---
name: "algo-ad-bidding"
description: "Implement and select ad bidding strategies from manual CPC to automated target-CPA and target-ROAS. Use this skill when the user needs to choose a bidding strategy, set up automated bidding, or optimize bid parameters — even if they say 'what bidding strategy should I use', 'target CPA setup', or 'smart bidding configuration'."
metadata:
  category: "WP-37 廣告演算法"
  tags: ["advertising", "bidding-strategy", "automated-bidding", "optimization"]
---

# Ad Bidding Strategies

## Overview

Bidding strategies determine how much an advertiser pays per auction. Range from manual CPC (full control) to automated strategies (Target CPA, Target ROAS, Maximize Conversions) that use ML to optimize bids in real-time based on contextual signals.

## When to Use

**Trigger conditions:**
- Choosing between manual and automated bidding strategies
- Setting up or troubleshooting Target CPA / Target ROAS campaigns
- Analyzing bid strategy performance and making adjustments

**When NOT to use:**
- When designing the auction mechanism itself (use GSP/VCG)
- When building a CTR prediction model (use CTR prediction skill)

## Algorithm

```
IRON LAW: Automated Bidding Requires SUFFICIENT Conversion Data
Below ~30 conversions/month, the algorithm lacks signal and performs
WORSE than manual bidding. Strategy selection depends on data volume:
- < 30 conv/month: Manual CPC or Maximize Clicks
- 30-50 conv/month: Maximize Conversions
- 50+ conv/month: Target CPA
- 50+ conv/month + revenue data: Target ROAS
```

### Phase 1: Input Validation
Assess: monthly conversion volume, conversion tracking accuracy, campaign budget, business goal (volume vs efficiency vs revenue).
**Gate:** Conversion tracking verified, sufficient data for chosen strategy.

### Phase 2: Core Algorithm
**Manual CPC:** Set bid per keyword. Adjust based on: device, time, location, audience performance data.

**Target CPA:** 1. Set target cost-per-acquisition. 2. Algorithm predicts conversion probability per auction using contextual signals. 3. Bids up for high-probability conversions, down for low. 4. Aims to average at target CPA over time.

**Target ROAS:** Same as CPA but optimizes for return on ad spend = conversion_value / cost.

### Phase 3: Verification
Monitor: actual CPA vs target, conversion volume stability, impression share changes, budget utilization.
**Gate:** Actual CPA within 20% of target after learning period (2-4 weeks).

### Phase 4: Output
Return strategy recommendation with expected performance ranges.

## Output Format

```json
{
  "recommendation": {"strategy": "target_cpa", "target": 500, "currency": "TWD", "confidence": "high"},
  "expected_performance": {"cpa_range": [400, 600], "volume_change": "-10% to +15%"},
  "metadata": {"monthly_conversions": 85, "current_cpa": 550, "learning_period_days": 14}
}
```

## Examples

### Sample I/O
**Input:** E-commerce campaign, 120 conversions/month, current CPA=NT$450, goal: maintain CPA, increase volume
**Expected:** Target CPA at NT$450. Expected: volume +10-20% as algorithm finds efficient auctions.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| 10 conversions/month | Manual CPC | Insufficient data for automation |
| Target CPA too aggressive | Volume drops to near zero | Algorithm can't find profitable auctions |
| Conversion tracking broken | All strategies fail | Garbage data → garbage optimization |

## Gotchas

- **Learning period volatility**: First 2 weeks after switching strategies show unstable performance. Don't change targets during this period.
- **Conversion delay**: If conversions take days to attribute (e.g., B2B), the algorithm optimizes on stale data. Use conversion modeling or extend the attribution window.
- **Budget as a constraint**: Target CPA won't spend if it can't hit the target. Setting an aggressive CPA with a large budget doesn't increase spend — it just saves money.
- **Micro-conversions**: If training on a proxy conversion (add to cart) instead of final purchase, the algorithm optimizes for the proxy. Ensure the tracked conversion aligns with business value.
- **Seasonality shocks**: Automated bidding learns from recent data. Black Friday, holidays, or competitive events can throw it off. Use seasonality adjustments.

## References

- For bid strategy migration playbook, see `references/migration-playbook.md`
- For learning period best practices, see `references/learning-period.md`
