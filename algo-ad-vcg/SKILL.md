---
name: "algo-ad-vcg"
description: "Implement VCG mechanism for incentive-compatible ad slot allocation with truthful bidding. Use this skill when the user needs to design a truthful auction mechanism, compute externality-based payments, or understand why platforms may prefer GSP over VCG — even if they say 'truthful auction design', 'VCG payments', or 'incentive-compatible mechanism'."
metadata:
  category: "WP-37 廣告演算法"
  tags: ["advertising", "auction", "vcg", "mechanism-design"]
---

# VCG Mechanism (Vickrey-Clarke-Groves)

## Overview

VCG allocates slots to maximize total social welfare and charges each winner the externality they impose on others. Truthful bidding is a dominant strategy. Runs in O(N log N + K × N) where N=bidders, K=slots.

## When to Use

**Trigger conditions:**
- Designing an incentive-compatible (truthful) multi-slot auction
- Computing welfare-maximizing allocations with externality pricing
- Academic analysis comparing VCG to GSP auctions

**When NOT to use:**
- When revenue maximization matters more than truthfulness (GSP often generates more revenue)
- For single-item auctions (standard Vickrey suffices)

## Algorithm

```
IRON LAW: VCG Guarantees Truthful Bidding BUT May Not Maximize Revenue
VCG payments are based on externality (harm to others), not competition.
This makes VCG payments often LOWER than GSP payments. Platforms
choose GSP because it typically generates higher revenue despite
strategic bidding. Truthfulness has a revenue cost.
```

### Phase 1: Input Validation
Collect true valuations per click for each advertiser and CTR for each slot position. Valuations must be non-negative.
**Gate:** All valuations non-negative, slot CTRs decreasing by position.

### Phase 2: Core Algorithm
1. Compute welfare-maximizing allocation: assign advertisers to slots to maximize Σ(value_i × CTR_slot_i)
2. For each winner i in slot s: compute total welfare WITHOUT advertiser i (re-optimize remaining bidders)
3. VCG payment_i = (welfare of others without i) - (welfare of others with i present)
4. This equals: Σ over lower positions j of (value_{j+1} × (CTR_j - CTR_{j+1}))

### Phase 3: Verification
Check: all payments ≤ valuations (individual rationality), truthful bidding is dominant strategy, allocation maximizes welfare.
**Gate:** IR satisfied, welfare is optimal.

### Phase 4: Output
Return allocation with VCG payments and welfare metrics.

## Output Format

```json
{
  "allocation": [{"advertiser": "A", "slot": 1, "vcg_payment_per_click": 1.80, "total_welfare_contribution": 500}],
  "metadata": {"total_welfare": 1500, "total_revenue": 420, "mechanism": "vcg"}
}
```

## Examples

### Sample I/O
**Input:** 3 bidders values [10, 8, 2], 2 slots CTRs [0.5, 0.3]
**Expected:** Allocation: Bidder1→Slot1, Bidder2→Slot2. VCG payments: Bidder1 = 8×(0.5-0.3)+2×0.3 = 2.20, Bidder2 = 2×0.3 = 0.60.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| All same valuation | All pay 0 | No externality imposed — no marginal harm |
| One bidder, one slot | Pays 0 | No other bidder harmed |
| Bidders < slots | All win, all pay 0 | No competition = no externality |

## Gotchas

- **Revenue deficit**: VCG often generates less revenue than GSP. In some cases, winners pay nothing (zero externality).
- **Computational complexity**: For general combinatorial auctions, VCG requires solving NP-hard welfare maximization. For position auctions, it's polynomial.
- **Collusion vulnerability**: VCG can be manipulated by colluding bidders who coordinate to reduce each other's externalities.
- **Non-monotonicity**: Adding a slot can sometimes DECREASE revenue (known as the "lonely bidder" pathology).
- **Practical rarity**: Almost no major ad platform uses pure VCG. It's theoretically elegant but commercially suboptimal.

## References

- For VCG vs GSP revenue comparison, see `references/revenue-comparison.md`
- For combinatorial VCG extensions, see `references/combinatorial-vcg.md`
