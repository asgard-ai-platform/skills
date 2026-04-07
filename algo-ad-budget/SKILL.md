---
name: "algo-ad-budget"
description: "Optimize advertising budget allocation across campaigns using marginal returns analysis. Use this skill when the user needs to distribute budget across multiple campaigns, optimize spend pacing, or maximize overall ROAS under budget constraints — even if they say 'how to split my ad budget', 'campaign budget optimization', or 'diminishing returns on ad spend'."
metadata:
  category: "WP-37 廣告演算法"
  tags: ["advertising", "budget-optimization", "allocation", "marginal-returns"]
---

# Ad Budget Allocation Optimization

## Overview

Budget allocation distributes a total advertising budget across campaigns to maximize overall returns. Uses the equal marginal returns principle: allocate until the marginal CPA (or marginal ROAS) is equalized across all campaigns. Handles diminishing returns and budget constraints.

## When to Use

**Trigger conditions:**
- Distributing a fixed budget across multiple campaigns or channels
- Identifying diminishing returns and optimal spend levels per campaign
- Rebalancing budget after performance changes

**When NOT to use:**
- When optimizing bids within a single campaign (use bidding strategy)
- When there's only one campaign (nothing to allocate across)

## Algorithm

```
IRON LAW: Equal Marginal Returns Principle
Optimal allocation makes the MARGINAL return of the last dollar
equal across ALL campaigns. If Campaign A's marginal CPA is $5
and Campaign B's is $15, shift budget from B to A until they equalize.
Total budget constraint: Σ budget_i = total_budget.
```

### Phase 1: Input Validation
Collect per-campaign: historical spend, conversions, revenue at multiple spend levels. Need at least 3 data points per campaign to fit response curve.
**Gate:** Sufficient historical data to estimate response curves.

### Phase 2: Core Algorithm
1. Fit response curve per campaign: conversions = f(spend). Common models: log curve, power curve, or S-curve
2. Compute marginal return curve: f'(spend) for each campaign
3. Allocate: use Lagrangian optimization or iterative greedy — assign next marginal dollar to campaign with highest marginal return
4. Apply constraints: minimum spend floors, maximum caps, channel-specific rules

### Phase 3: Verification
Check: total allocation = total budget, no campaign below floor or above cap, marginal returns approximately equal at boundaries.
**Gate:** Allocation sums to budget, constraints satisfied.

### Phase 4: Output
Return allocation table with expected performance projections.

## Output Format

```json
{
  "allocation": [{"campaign": "Search-Brand", "budget": 50000, "expected_conversions": 200, "expected_cpa": 250}],
  "total": {"budget": 200000, "expected_conversions": 650, "blended_cpa": 308},
  "metadata": {"optimization_method": "lagrangian", "response_model": "log_curve"}
}
```

## Examples

### Sample I/O
**Input:** Budget: $100K, Campaigns: Search ($50K, 100 conv), Social ($30K, 60 conv), Display ($20K, 20 conv)
**Expected:** Shift budget from Display (high marginal CPA) to Search (low marginal CPA). e.g., Search $60K, Social $30K, Display $10K.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| One campaign dominates | Most budget to winner | But maintain minimum floor for others |
| All campaigns saturated | Reduce total spend | Spending more won't help |
| New campaign, no data | Use minimum test budget | Need data before optimizing |

## Gotchas

- **Response curve extrapolation**: Don't optimize beyond observed spend ranges. The curve may change shape at higher spend levels.
- **Attribution overlap**: Users may see ads across campaigns. Last-click attribution double-counts, inflating high-funnel campaign CPA. Use multi-touch attribution.
- **Diminishing returns assumption**: Not all campaigns follow smooth diminishing returns. Some have step functions (e.g., reaching a new audience segment at a spend threshold).
- **Time dynamics**: Response curves shift seasonally and competitively. Refit curves monthly or use rolling windows.
- **Minimum viable spend**: Each campaign needs enough budget to exit the learning phase. Spreading too thin means no campaign gets sufficient data.

## References

- For response curve fitting methods, see `references/response-curves.md`
- For multi-touch attribution integration, see `references/attribution-integration.md`
