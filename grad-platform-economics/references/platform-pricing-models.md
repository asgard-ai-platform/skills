# Platform Pricing Models (Rochet-Tirole Formalization)

## Core Setup

A two-sided platform connects side 1 (e.g., buyers) and side 2 (e.g., sellers). The platform charges per-interaction prices $p_1$ and $p_2$ to each side, where the total price level is:

$$P = p_1 + p_2$$

The platform's problem is not just to maximize $P$, but to **allocate** $P$ across sides to maximize interaction volume (and hence total value created).

Notation used throughout:

| Symbol | Meaning |
|--------|---------|
| $p_i$ | Per-interaction price charged to side $i$ |
| $c_i$ | Marginal cost of serving one user on side $i$ |
| $n_i$ | Number of users on side $i$ |
| $\alpha_{ij}$ | Cross-side network effect: benefit side $i$ gets from each additional user on side $j$ |
| $\sigma_i$ | Price elasticity of demand for side $i$ |
| $b_i$ | Benefit side $i$ gets from each interaction (willingness to pay per interaction) |

---

## The Rochet-Tirole Pricing Rule

**Source**: Rochet & Tirole (2003, 2006), Armstrong (2006).

Under symmetric Hotelling competition between two platforms, the equilibrium price to side $i$ satisfies:

$$p_i - c_i = \frac{1}{2\sigma_i} - \alpha_{ij} n_j$$

But the key insight is not the equilibrium itself — it is the **price structure** result:

> **Only the total price level $P = p_1 + p_2$ determines efficiency. But the allocation of $P$ between sides determines participation.**

This means a monopoly platform maximizing profit solves:

$$\max_{p_1, p_2} \; (p_1 - c_1) \cdot n_1(p_1, n_2) + (p_2 - c_2) \cdot n_2(p_2, n_1)$$

subject to both sides choosing to participate. The first-order conditions yield the **modified Lerner rule** for platforms:

$$\frac{p_i - c_i}{p_i} = \frac{1}{\sigma_i} - \frac{\alpha_{ij} \cdot n_j}{p_i \cdot \sigma_i}$$

The second term on the right is the crucial correction: **subsidize side $i$ more when the cross-side effect $\alpha_{ij}$ is large** (side $i$'s presence creates high value for side $j$).

---

## Simplified Decision Rule

In practice, derive the subsidy side using this two-factor test:

### Factor 1: Relative Price Elasticity

Whichever side is MORE price-elastic should pay LESS.

$$\text{Subsidy side} \Leftarrow \text{higher } \sigma_i$$

Intuition: elastic side walks away easily; losing them collapses cross-side value.

### Factor 2: Cross-Side Effect Asymmetry

Whichever side generates STRONGER cross-side effects for the other side gets subsidized.

$$\text{Subsidy side} \Leftarrow \text{higher } \alpha_{ij}$$

Intuition: subsidizing side $i$ is an investment — each additional user on side $i$ raises side $j$'s willingness to pay by $\alpha_{ij}$, increasing what you can extract from side $j$.

### Combined Decision Table

| $\sigma_1$ vs $\sigma_2$ | $\alpha_{12}$ vs $\alpha_{21}$ | Subsidy side |
|--------------------------|-------------------------------|--------------|
| $\sigma_1 > \sigma_2$ | $\alpha_{12} > \alpha_{21}$ | Side 1 clearly |
| $\sigma_1 > \sigma_2$ | $\alpha_{12} < \alpha_{21}$ | Ambiguous — compute |
| $\sigma_1 < \sigma_2$ | $\alpha_{12} > \alpha_{21}$ | Ambiguous — compute |
| $\sigma_1 < \sigma_2$ | $\alpha_{12} < \alpha_{21}$ | Side 2 clearly |

When ambiguous, go to the numerical example in the next section.

---

## Worked Example: Ride-Hailing Platform

### Setup

A ride-hailing platform is deciding how to split a total interaction price of **$3.00** between riders (side 1) and drivers (side 2). Estimated parameters:

| Parameter | Riders (Side 1) | Drivers (Side 2) |
|-----------|----------------|-----------------|
| Marginal cost $c_i$ | $0.20 | $0.50 |
| Price elasticity $\sigma_i$ | 1.8 | 0.9 |
| Cross-side benefit $\alpha_{ij}$ | $0.30 per driver | $0.15 per rider |
| Current user count $n_i$ | 50,000 | 8,000 |

### Step 1: Compute Cross-Side Subsidy Value

For riders (side 1): what does each additional rider generate for drivers?

$$\alpha_{21} \cdot n_1 = \$0.15 \times 50{,}000 = \$7{,}500 \text{ in aggregate driver value}$$

For drivers (side 2): what does each additional driver generate for riders?

$$\alpha_{12} \cdot n_2 = \$0.30 \times 8{,}000 = \$2{,}400 \text{ in aggregate rider value}$$

Riders generate more aggregate cross-side value ($7,500 > $2,400), but on a **per-user** basis, each additional driver is worth more to riders ($0.30) than each additional rider is worth to drivers ($0.15).

### Step 2: Apply Modified Lerner Rule

Rearranging the first-order condition for each side:

$$p_i^* = \frac{c_i + \alpha_{ij} \cdot n_j}{1 - \frac{1}{\sigma_i}}$$

For riders ($i = 1$):

$$p_1^* = \frac{0.20 + (0.30 \times 8{,}000) / N}{1 - \frac{1}{1.8}}$$

Here we normalize $\alpha_{ij}$ to per-interaction terms. If we express cross-side benefit as **per interaction** rather than per user count, say $\alpha_{12} = \$0.30$ per interaction:

$$p_1^* = \frac{0.20 + 0.30}{1 - 0.556} = \frac{0.50}{0.444} = \$1.13$$

For drivers ($i = 2$):

$$p_2^* = \frac{0.50 + 0.15}{1 - \frac{1}{0.9}} = \frac{0.65}{1 - 1.11} = \frac{0.65}{-0.11}$$

Negative price — drivers should be **subsidized** (negative $p_2$). This is the classic result: inelastic sides with small cross-side effects are not necessarily the money side.

### Step 3: Re-check with Budget Constraint

If the platform needs $P = p_1 + p_2 = \$3.00$ total to cover costs and margin:

Given the ratio signal from elasticities:

$$\frac{p_1}{p_2} \approx \frac{\sigma_2}{\sigma_1} = \frac{0.9}{1.8} = 0.5$$

So riders should pay roughly **half** of what drivers pay, IF elasticity were the only factor. But drivers have much lower elasticity (0.9 < 1.8), so they *can* bear more. However, the cross-side effect $\alpha_{12} = \$0.30$ favors subsidizing drivers, who generate high value for riders.

**Resolution**: Charge riders more, subsidize (or charge minimally) drivers:

- $p_1 = \$2.50$ (riders pay most of the freight)
- $p_2 = \$0.50$ (drivers pay a small listing/access fee)

This matches observed ride-hailing pricing: riders pay; drivers pay nothing or a small commission on transactions only.

---

## The Seesaw Property

**Core result** (Armstrong 2006): In a competitive market with two platforms, reducing $p_1$ by $\Delta$ and raising $p_2$ by $\Delta$ (keeping $P$ constant) increases side-1 participation and decreases side-2 participation. The net effect on platform profit depends entirely on cross-side effects.

$$\frac{\partial \pi}{\partial p_1} = n_1 + (p_1 - c_1)\frac{\partial n_1}{\partial p_1} + (p_2 - c_2)\frac{\partial n_2}{\partial n_1}\frac{\partial n_1}{\partial p_1}$$

The last term is the **externality correction**: lowering $p_1$ attracts more side-1 users, which raises side-2 participation, which raises side-2 revenue. A platform that ignores this term sets prices too high on the subsidy side.

**Practical implication**: If you raise the price on the subsidy side and see disproportionate drop in the money side's activity — you've crossed the seesaw pivot. The subsidy side was underpriced.

---

## Transaction Fee vs. Membership Fee

Rochet & Tirole distinguish two pricing instruments:

| Instrument | Structure | When to use |
|------------|-----------|-------------|
| **Membership fee** | Fixed cost to join the platform | When value is derived from access (B2B SaaS platforms, credit card network membership) |
| **Transaction fee** | Per-interaction charge | When value scales with usage (marketplaces, payment networks) |
| **Mixed** | Fixed fee + per-transaction | When fixed costs are high AND volume variance is high |

**Key result**: Transaction fees are more efficient when users have heterogeneous usage intensity. Membership fees extract more surplus when all users have similar intensity.

### Decision Formula

Let $\bar{q}$ = average transactions per user, $\sigma_q$ = standard deviation of transactions per user.

If $\sigma_q / \bar{q} > 0.5$ (high variance): prefer **transaction fees**.

If $\sigma_q / \bar{q} < 0.2$ (low variance): prefer **membership fees**.

In between: use mixed pricing.

---

## Zero-Price Side: When to Make One Side Free

Setting $p_i = 0$ (not just subsidized but free) is optimal when:

$$\alpha_{ij} \cdot n_j \geq c_i + \text{margin required from side } i$$

In words: the indirect revenue generated by side $i$'s presence (via attracting side $j$, who pays) exceeds the cost of serving side $i$.

**Adobe test**: Adobe Reader is free because:
- $c_i$ (marginal cost of Reader download) ≈ $0
- $\alpha_{ij}$ (each Reader user increases Acrobat Pro demand) is high
- Acrobat Pro margin covers Reader's distribution cost

**Failure mode**: Setting $p_i = 0$ when $\alpha_{ij}$ is low. Platform absorbs cost of a side that doesn't generate cross-side pull. Example: free restaurant listings on a platform where diners don't respond to restaurant count.

---

## Multi-Homing Correction

Standard Rochet-Tirole assumes single-homing. When users multi-home (use multiple platforms), adjust:

$$p_i^{\text{multi-home}} = p_i^{\text{single-home}} - \frac{\alpha_{ij} \cdot (1 - \lambda_i)}{1}$$

Where $\lambda_i \in [0,1]$ is the **exclusivity rate** of side $i$ (fraction of side $i$ users who use only this platform).

When $\lambda_i \to 0$ (full multi-homing on side $i$): the platform cannot extract much from side $i$ because users face near-zero switching cost. The subsidy on side $i$ also generates less lock-in value.

**Practical implication**: If drivers freely multi-home between Uber and Lyft, Uber cannot rely on driver-side network effects as a moat. The subsidy to drivers generates less durable advantage. Price accordingly — lower subsidy, invest in supply-side exclusivity incentives instead.

---

## Common Pricing Mistakes and Diagnostics

### Mistake 1: Charging Both Sides Equally

**Symptom**: Neither side grows. Interaction rate stagnates despite users on both sides.

**Diagnosis**: Equal pricing ignores elasticity asymmetry. One side is over-charged relative to the cross-side value it generates.

**Fix**: Run a price split test. Halve the price on one side for 30 days. If interactions per user on the OTHER side increase, the halved side was the correct subsidy side.

### Mistake 2: Raising Price on Money Side to Fund Subsidy

**Symptom**: Money side churns faster than subsidy side grows.

**Diagnosis**: Platform crossed the seesaw pivot. The money side's willingness to pay is driven by the subsidy side's participation. Reducing subsidy-side quality (via money-side price hike) is self-defeating.

**Fix**: Find revenue from outside the interaction (e.g., data licensing, premium features, SaaS add-ons) rather than the per-interaction price.

### Mistake 3: Free Side With No Conversion Path

**Symptom**: Free side is large but money side is small and stagnant.

**Diagnosis**: Free side is being treated as the subsidy side, but there is no mechanism converting free-side growth into money-side value. The $\alpha_{ij}$ was assumed but not verified.

**Fix**: Measure cross-side lift directly: does a 10% increase in free-side users correlate with higher money-side activity within 60 days? If not, the free side is a cost center, not a subsidy.

---

## Summary: Pricing Decision Checklist

```
1. Measure σ₁ and σ₂ (price elasticity, both sides)
   → Higher σ = subsidy candidate

2. Estimate α₁₂ and α₂₁ (cross-side benefits per interaction)
   → Higher α = subsidy candidate (generates more pull for the other side)

3. Check multi-homing rate λᵢ on each side
   → Low λ = subsidy generates less lock-in; reduce subsidy accordingly

4. Choose pricing instrument (membership vs. transaction)
   → σ_q / q̄ > 0.5 → transaction fees
   → σ_q / q̄ < 0.2 → membership fees

5. Evaluate zero-price threshold
   → Set pᵢ = 0 only if αᵢⱼ · nⱼ ≥ cᵢ + required margin

6. Monitor: interactions per user per period (NOT registered users)
   → Per IRON LAW: value = interactions, not headcount
```
