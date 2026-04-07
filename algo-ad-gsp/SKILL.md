---
name: "algo-ad-gsp"
description: "Implement Generalized Second Price auction for ad slot allocation and pricing. Use this skill when the user needs to understand search ad auctions, compute ad positions and costs-per-click, or analyze bidding dynamics — even if they say 'how does Google Ads auction work', 'ad rank calculation', or 'second price auction for ads'."
metadata:
  category: "WP-37 廣告演算法"
  tags: ["advertising", "auction", "gsp", "ad-pricing"]
---

# Generalized Second Price Auction

## Overview

GSP allocates K ad slots to N bidders, assigning the highest bidder the top slot, second-highest the second slot, etc. Each winner pays the bid of the advertiser ONE POSITION BELOW them (per-slot second price). Used by Google Ads and Bing Ads. Runs in O(N log N) for sorting bids.

## When to Use

**Trigger conditions:**
- Understanding search engine ad auction mechanics
- Computing ad position and cost-per-click from bid and quality data
- Analyzing bidding strategy in sponsored search

**When NOT to use:**
- When you need incentive-compatible truthful bidding (use VCG mechanism)
- When analyzing display/programmatic ad auctions (typically use first-price)

## Algorithm

```
IRON LAW: GSP Is NOT Incentive-Compatible
Unlike Vickrey (single-item second-price) auctions, truthful bidding
is NOT a dominant strategy in GSP. Bidders may strategically shade
bids below their true value. The equilibrium depends on competitor bids.
Ad Rank = Bid × Quality Score (Google's variant adds format/extensions).
```

### Phase 1: Input Validation
Collect: bids, quality scores (or ad rank scores) for all competing advertisers. Define available slot positions and their click-through rate multipliers.
**Gate:** All bids positive, quality scores in valid range.

### Phase 2: Core Algorithm
1. Compute Ad Rank for each advertiser: AdRank_i = Bid_i × QualityScore_i
2. Sort advertisers by Ad Rank descending
3. Assign top-K to slots 1 through K
4. Compute payment: CPC_i = AdRank_{i+1} / QualityScore_i (price to maintain position)
5. Last slot winner pays the minimum bid threshold

### Phase 3: Verification
Check: all payments ≤ bids, positions ordered by Ad Rank, no advertiser pays more than their bid.
**Gate:** Payment ≤ bid for all winners, positions consistent.

### Phase 4: Output
Return slot assignments with positions, CPCs, and estimated clicks.

## Output Format

```json
{
  "slots": [{"advertiser": "A", "position": 1, "ad_rank": 8.5, "cpc": 2.10, "est_clicks": 100}],
  "metadata": {"total_bidders": 15, "slots_available": 4, "auction_type": "gsp"}
}
```

## Examples

### Sample I/O
**Input:** Bidders: A(bid=3, QS=8), B(bid=4, QS=5), C(bid=2, QS=9). Slots: 2.
**Expected:** Ranks: A=24, C=18, B=20. Order: A(1st), B(2nd). CPC_A = 20/8 = 2.50, CPC_B = 18/5 = 3.60.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Tie in Ad Rank | Platform tiebreaker (historical CTR, etc.) | GSP needs strict ordering |
| One bidder | Wins slot 1, pays minimum CPC | No competition → floor price |
| Bid below threshold | Not eligible | Minimum bid requirement enforced |

## Gotchas

- **Quality Score is opaque**: Google's QS includes expected CTR, ad relevance, and landing page experience. The exact formula is proprietary.
- **Strategic bid shading**: Since GSP isn't truthful, sophisticated advertisers shade bids. This means observed bids don't reflect true willingness to pay.
- **Position ≠ value**: Higher position gets more clicks but at higher CPC. The most profitable position may be #2 or #3, not #1.
- **Budget constraints**: GSP doesn't account for daily budgets. Budget-constrained advertisers must pace bids throughout the day.
- **Broad match expansion**: The auction includes query-expanded matches, which may have different conversion rates than exact matches.

## References

- For Nash equilibrium analysis of GSP, see `references/gsp-equilibrium.md`
- For comparison with VCG mechanism, see `references/gsp-vs-vcg.md`
