# GSP Nash Equilibrium Analysis

GSP has **infinitely many Nash equilibria**. This document derives the locally envy-free (LEF) equilibrium — the refinement used in practice — and shows how to compute equilibrium bids from true values.

## The Core Problem

In Vickrey (single-item) auctions, truth-telling is a dominant strategy. In GSP it is not. Consider a bidder who wins slot 1 by bidding truthfully. They might prefer to shade their bid downward, drop to slot 2, and pay less per click — if the click-rate reduction is worth the cost savings.

This means equilibrium requires solving a system of inequalities, not just ranking bids.

## Notation

| Symbol | Meaning |
|--------|---------|
| N | number of bidders |
| K | number of ad slots (K ≤ N) |
| v_i | true value per click for advertiser i |
| b_i | equilibrium bid of advertiser i |
| α_k | click-through rate multiplier of slot k |
| p_i | price per click paid by advertiser in slot i |

Assume values and slots are labeled so that v_1 > v_2 > … > v_N and α_1 > α_2 > … > α_K > α_{K+1} = 0.

In equilibrium, advertiser i wins slot i and pays p_i = b_{i+1} (the bid of the person just below).

## Locally Envy-Free (LEF) Condition

A bid vector is a **Locally Envy-Free equilibrium** (Edelman, Ostrovsky, Schwarz 2007; Varian 2007) if no advertiser prefers to swap positions with an **adjacent** neighbor.

**No upward envy** (i does not want slot i−1):

```
(v_i − p_i) · α_i ≥ (v_i − p_{i-1}) · α_{i-1}
```

**No downward envy** (i does not want slot i+1):

```
(v_i − p_i) · α_i ≥ (v_i − p_{i+1}) · α_{i+1}
```

These two together, applied to every adjacent pair, define the LEF equilibrium. Note that only adjacent swaps are checked — transitivity handles non-adjacent ones.

## Worked Example: 3 Bidders, 2 Slots

### Setup

| Advertiser | True value v_i ($/click) |
|------------|--------------------------|
| A | 10 |
| B | 7 |
| C | 3 |

| Slot | Click rate α_k |
|------|----------------|
| 1 (top) | 100 clicks/day |
| 2 | 40 clicks/day |
| (floor) | 0 |

Minimum bid threshold: $0.01/click. Advertiser C's value is $3/click but they do not win a slot in this example (only 2 slots for 3 bidders).

### Step 1: Compute VCG Payments (Lower Bound on LEF Equilibrium)

VCG payment for slot i is the externality imposed on others:

```
VCG_i = Σ_{k=i}^{K} (α_k − α_{k+1}) · v_{k+1}
```

**VCG payment for slot 1 (advertiser A):**
```
VCG_1 = (α_1 − α_2) · v_B + (α_2 − α_3) · v_C
       = (100 − 40) · 7  +  (40 − 0) · 3
       = 60 · 7 + 40 · 3
       = 420 + 120
       = 540  →  CPC = 540 / 100 = $5.40
```

**VCG payment for slot 2 (advertiser B):**
```
VCG_2 = (α_2 − α_3) · v_C
       = (40 − 0) · 3
       = 120  →  CPC = 120 / 40 = $3.00
```

VCG payments are the **minimum** that can sustain an LEF equilibrium.

### Step 2: Verify LEF Conditions at VCG Payments

Let p_A = 5.40, p_B = 3.00.

**A does not want to drop to slot 2:**
```
(10 − 5.40) · 100 ≥ (10 − 3.00) · 40
460 ≥ 280  ✓
```

**B does not want to move up to slot 1:**
```
(7 − 3.00) · 40 ≥ (7 − 5.40) · 100
160 ≥ 160  ✓  (exactly indifferent — this is VCG's boundary)
```

**B does not want to exit (slot 3 = 0 clicks):**
```
(7 − 3.00) · 40 ≥ (7 − 0.01) · 0
160 ≥ 0  ✓
```

VCG payments satisfy LEF. Advertiser B is exactly indifferent between slot 1 and slot 2 at VCG prices — this is the characteristic VCG boundary.

### Step 3: Upper Bound of the Equilibrium Range

The **maximum** LEF-compatible payment for slot i is bounded by the next-higher type's indifference condition. For A:

```
(v_A − p_A^max) · α_1 = (v_A − p_B) · α_2
(10 − p_A^max) · 100 = (10 − 3.00) · 40
10 − p_A^max = 2.80
p_A^max = 7.20
```

So A's CPC in any LEF equilibrium is in **[$5.40, $7.20]**.

For B, the upper bound comes from C's indifference (C would enter at exactly v_C = $3.00):

```
p_B^max = v_C = 3.00
```

B's CPC is pinned at **$3.00** — no wiggle room because C is right below the cutoff.

### Step 4: Equilibrium Bid Recovery

Given equilibrium prices p_1, p_2, the bids that implement them are:

- b_B = p_A (B's bid sets A's price)
- b_C = p_B (C's bid sets B's price)
- b_A = any value such that A wins slot 1

For the VCG payments: b_B = 5.40, b_C = 3.00. A bids anything above b_B = 5.40 (say 10.00, their true value).

**Bid shading summary:**
- A: bids truthfully (10.00) — top position has no one above to shade against
- B: shades from 7.00 down to 5.40 to implement VCG prices

## The Full Equilibrium Range in Tabular Form

For this example, all LEF equilibria have payments in:

| Advertiser | Slot | Min CPC (VCG) | Max CPC |
|------------|------|--------------|---------|
| A | 1 | $5.40 | $7.20 |
| B | 2 | $3.00 | $3.00 |

The auctioneer's revenue ranges from:
- **Minimum** (VCG): 100 × 5.40 + 40 × 3.00 = $660/day
- **Maximum**: 100 × 7.20 + 40 × 3.00 = $840/day

## General Formula for Equilibrium Bounds

For K slots and N ≥ K bidders, the LEF equilibrium payment for slot i satisfies:

**Lower bound (VCG):**
```
p_i^min = (1 / α_i) · Σ_{k=i}^{K} (α_k − α_{k+1}) · v_{k+1}
```

**Upper bound:**
```
p_i^max = v_i − (α_{i+1} / α_i) · (v_i − p_{i+1})
```

Applied recursively top-down, starting from p_K^max = v_{K+1} (the first excluded bidder's value).

## Bid Shading in Practice

An advertiser who knows competitor bids can compute their optimal shade:

```python
def optimal_shade(v_i, alpha_i, alpha_next, p_next):
    """
    Compute max bid to remain in slot i given prices.
    v_i:       true value per click
    alpha_i:   clicks in current slot
    alpha_next: clicks in next slot down
    p_next:    CPC of next slot down (= bid of person two below you)
    Returns: bid that makes you exactly indifferent between slot i and slot i+1
    """
    # Solve: (v_i - p_next) * alpha_i = (v_i - b_shade) * alpha_next
    # b_shade is what your competitor bids to set your price
    # But you control your own bid to stay in slot i
    # Indifference condition: stay in slot i vs drop to i+1
    # (v_i - b_{i+1}) * alpha_i = (v_i - p_{i+1}) * alpha_{i+1}
    surplus_below = (v_i - p_next) * alpha_next
    p_shade = v_i - surplus_below / alpha_i
    return p_shade
```

**Example:** B wants to know their equilibrium bid.
```
optimal_shade(v_i=7, alpha_i=100, alpha_next=40, p_next=3.00)
= 7 - (7-3)*40/100
= 7 - 1.60
= 5.40
```

B should bid $5.40, not $7.00. This is exactly the VCG payment boundary.

## Revenue Comparison: GSP vs VCG

| Metric | GSP (min LEF) | GSP (max LEF) | VCG |
|--------|--------------|--------------|-----|
| Total revenue | $660 | $840 | $660 |
| Incentive-compatible | No | No | Yes |
| Truthful bidding | No | No | Yes |
| Revenue ≥ VCG | Always | Always | Baseline |

GSP revenue always weakly exceeds VCG revenue because the equilibrium set includes VCG as a lower bound and can go higher. However, under repeated bidding with learning, markets tend to converge toward the VCG outcome (advertisers learn to shade optimally).

## IRON LAW Reinforcement

The parent skill's Iron Law holds here: no LEF equilibrium has truthful bidding as a dominant strategy. The worked example shows B's equilibrium bid is $5.40, not $7.00. Claiming "GSP = second-price = truthful" is wrong. The correct statement is:

> In a **single-item** second-price auction, truth-telling is dominant. In GSP with multiple slots, it is not — the equilibrium depends on competitor bids and click-rate ratios.

## When Equilibrium Analysis Matters

| Scenario | Implication |
|----------|-------------|
| Competitor bids are stable | Use shade formula to compute profitable bid |
| Competitor bids fluctuate | LEF equilibrium may not be reached; bid closer to true value |
| Only 1 slot available | Reduces to Vickrey; truth-telling is dominant |
| All α_k equal | Position doesn't matter; again reduces to simpler problem |
| You are the only bidder | Pay floor price regardless; equilibrium analysis irrelevant |

## References

- Edelman, B., Ostrovsky, M., & Schwarz, M. (2007). "Internet Advertising and the Generalized Second-Price Auction." *American Economic Review*, 97(1), 242–259.
- Varian, H. R. (2007). "Position Auctions." *International Journal of Industrial Organization*, 25(6), 1163–1178.
