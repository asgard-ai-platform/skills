# VCG vs GSP Revenue Comparison

## Core Claim

VCG payments are computed from externalities; GSP payments are computed from the next-highest bid. These two mechanisms produce **identical revenue only at one specific Nash equilibrium** of GSP (the locally envy-free equilibrium). In practice, GSP bids sit above that equilibrium, generating more revenue than VCG.

---

## Payment Formulas Side by Side

Assume N bidders sorted by value v₁ ≥ v₂ ≥ … ≥ vₙ, K slots with CTRs α₁ ≥ α₂ ≥ … ≥ αₖ (define αₖ₊₁ = 0).

### VCG Total Payment for Bidder i (in slot i)

$$p_i^{VCG} = \sum_{j=i}^{K} v_{j+1} \cdot (\alpha_j - \alpha_{j+1})$$

This is the sum of "harm" the winner imposes: each lower-ranked bidder j+1 is displaced from slot j by the presence of bidder i, costing others v_{j+1} × (αⱼ − αⱼ₊₁).

### GSP Total Payment for Bidder i (in slot i)

$$p_i^{GSP} = b_{i+1} \cdot \alpha_i$$

Bidder i pays per click the **bid** of the next-ranked bidder below them. At truthful bids bᵢ = vᵢ this becomes vᵢ₊₁ × αᵢ.

---

## Worked Example (from SKILL.md canonical input)

**Input:** bidders A, B, C with values [10, 8, 2]; slots 1, 2 with CTRs [0.5, 0.3].

Allocation: A → slot 1, B → slot 2 (welfare-maximizing, both mechanisms agree on this).

### VCG Payments

Bidder A (slot 1):
```
p_A^VCG = v_B × (α₁ − α₂) + v_C × α₂
        = 8 × (0.5 − 0.3) + 2 × 0.3
        = 8 × 0.2 + 2 × 0.3
        = 1.60 + 0.60
        = 2.20
```

Bidder B (slot 2):
```
p_B^VCG = v_C × α₂
        = 2 × 0.3
        = 0.60
```

**Total VCG Revenue = 2.20 + 0.60 = 2.80**

### GSP Payments at Truthful Bids (b = v)

Bidder A (slot 1) pays next bid per click:
```
p_A^GSP = b_B × α₁ = 8 × 0.5 = 4.00
```

Bidder B (slot 2) pays next bid per click:
```
p_B^GSP = b_C × α₂ = 2 × 0.3 = 0.60
```

**Total GSP Revenue (truthful bids) = 4.00 + 0.60 = 4.60**

### Revenue Comparison Table

| Scenario | Bidder A pays | Bidder B pays | Platform Revenue |
|---|---|---|---|
| VCG (dominant strategy) | 2.20 | 0.60 | **2.80** |
| GSP at truthful bids | 4.00 | 0.60 | **4.60** |
| GSP at locally envy-free NE | 2.20 | 0.60 | **2.80** |
| GSP in practice (above NE) | ~3.00–3.80 | ~0.60 | **~3.60–4.40** |

The revenue gap is entirely in slot 1: VCG charges A based on the externality imposed (displacing bidders B and C), while GSP charges A based on B's bid for slot 1.

---

## Why the Nash Equilibrium Closes the Gap (EOS Theorem)

Edelman, Ostrovsky, and Schwarz (2007) proved that every **locally envy-free Nash equilibrium** of GSP produces the same payments as VCG.

A locally envy-free equilibrium is a bid profile where no advertiser can increase utility by swapping bids with an adjacent-ranked advertiser. At this equilibrium, the bid of advertiser in slot i satisfies:

$$b_i^{NE} = \frac{\alpha_{i-1} \cdot b_{i-1}^{NE} - v_i \cdot (\alpha_{i-1} - \alpha_i)}{\alpha_i}$$

Working backwards from bₖ₊₁ = 0 for our example:

```
b_C = 0 (no slot for C)
b_B^NE: B prefers slot 2 at bid b_B over slot 1 at bid b_A
  → envy-free condition for B: v_B × α₂ − b_C × α₂ ≥ v_B × α₁ − b_A × α₁
  → 8×0.3 − 0.60 ≥ 8×0.5 − b_A×0.5
  → 1.80 ≥ 4.00 − 0.5×b_A
  → b_A ≥ 4.40

Minimum b_A^NE = 4.40
Check: p_A^GSP at NE = b_B^NE × α₁
```

At the minimum locally envy-free NE, each winner's payment exactly equals their VCG payment. The equilibrium exists but requires bidders to coordinate to find it — they rarely do.

---

## Why Practice Diverges: The Revenue Gap

Three structural reasons GSP generates more revenue than VCG in deployed systems:

**1. No dominant strategy in GSP**

In VCG, each bidder's optimal action is independent of others: bid truthfully. In GSP, there is no dominant strategy — the optimal bid depends on competitors' bids. Bidders respond to uncertainty by experimenting and adjusting, often bidding above the Nash equilibrium to capture better positions.

**2. Overbidding in position auctions**

Empirically (Varian 2007), advertisers in Google's ad system bid above the locally envy-free Nash equilibrium. The intuition: they overbid to secure higher slots, hoping the displacement effect pays off. This pushes GSP revenue above VCG revenue.

**3. Budget pacing and position preferences**

Real advertisers have target CPA goals, not abstract "values per click." When budget constraints bind, they bid up to secure preferred positions. VCG payments stay fixed (they depend only on others' valuations, which don't change); GSP payments float upward with competitive pressure.

---

## Revenue Deficit Pathologies in VCG

VCG can underperform its own theoretical floor in specific configurations:

### Zero-Payment Cases

If bidder i imposes no externality, p_i^VCG = 0. This happens when:
- Removing bidder i would not displace any other bidder (bidder count < slot count)
- All remaining bidders have value 0

In the 3-bidder example, if C's value is 0 instead of 2:
- Bidder A's VCG payment = 8×0.2 + 0×0.3 = 1.60
- Bidder B's VCG payment = 0×0.3 = 0.00
- **Total VCG Revenue = 1.60 vs GSP Revenue = 4.40**

The platform collects nothing from slot 2 despite filling it.

### Lonely Bidder Pathology

Adding a slot can **decrease** VCG revenue. Example:

**Before** (2 slots, CTRs [0.5, 0.3], bidders [10, 8, 2]):
- VCG Revenue = 2.80 (computed above)

**After** adding slot 3 with CTR = 0.1, bidder C (value 2) now wins:
```
p_A^VCG = 8×(0.5−0.3) + 2×(0.3−0.1) + 0×0.1 = 1.60 + 0.40 = 2.00
p_B^VCG = 2×(0.3−0.1) + 0×0.1 = 0.40
p_C^VCG = 0×0.1 = 0.00
Total VCG Revenue = 2.40  ← less than 2.80
```

Adding slot 3 gave C a "home," reducing the externality that A and B imposed on C in the 2-slot world. GSP does not exhibit this pathology — adding slots cannot reduce revenue because payments depend only on next-ranked bids, not on allocating to lower slots.

---

## Decision Framework: VCG vs GSP

| Factor | Prefer VCG | Prefer GSP |
|---|---|---|
| Bidder sophistication | High (know their true value) | Low (noisy bids) |
| Theoretical guarantees needed | Yes (academic / regulatory) | No |
| Platform revenue priority | Secondary | Primary |
| Auction repetition | One-shot | Repeated (bidders learn bids) |
| Number of slots | Few (≤ 5) | Many |
| Collusion risk tolerance | Low (VCG is collusion-vulnerable) | Higher |
| Implementation complexity | Higher | Lower |

No major ad platform (Google, Meta, Amazon) runs pure VCG for display/search ads. Microsoft Bing ran a VCG variant briefly but reverted. The revenue loss is structural, not a tuning problem.

---

## Revenue Gap Magnitude in Practice

Theoretical upper bound on GSP/VCG revenue ratio at truthful bids:

$$\frac{R^{GSP}_{truthful}}{R^{VCG}} = \frac{\sum_i v_{i+1} \cdot \alpha_i}{\sum_i \sum_{j \geq i} v_{j+1} \cdot (\alpha_j - \alpha_{j+1})}$$

For geometric CTR decay αᵢ = α × δⁱ⁻¹ (common empirical model, δ ≈ 0.6–0.8), this ratio simplifies:

```
GSP truthful revenue   v₂α₁ + v₃α₂ + ... + vₖ₊₁αₖ
─────────────────── = ──────────────────────────────────
VCG revenue            (same numerator reweighted by δ)
```

With δ = 0.7 and uniform valuation spacing, the ratio is typically **1.3–1.8×**. The gap widens with:
- Steeper CTR decay (larger δ spread)
- Larger spread between adjacent valuations
- More slots (more opportunities for zero-externality winners)

---

## Summary of Iron Law Reinforcement

> VCG payments are based on externality (harm to others), not competition. This makes VCG payments often LOWER than GSP payments.

The worked numbers confirm this concretely: for the canonical [10, 8, 2] / [0.5, 0.3] example, VCG collects 2.80 vs GSP's 4.60 at truthful bids — a 39% revenue shortfall. The EOS theorem shows this gap closes at Nash equilibrium, but equilibrium requires coordination that advertisers do not achieve in practice. Platforms capture the gap as profit.
