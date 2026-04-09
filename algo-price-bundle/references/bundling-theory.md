# Bundling Theory (Adams & Yellen 1976)

## Core Insight

Adams & Yellen (1976) proved that bundling increases profit when consumer valuations across products are **negatively correlated**: customers who strongly value product A tend to weakly value product B, and vice versa. The bundle price captures consumers who would otherwise be priced out of one of the individual products.

The mechanism is not price discrimination in the traditional sense — it is **surplus extraction through averaging**: the bundle price sits between the two extreme valuations, pulling in both customer types.

---

## Formal Setup

Two products A and B. Two customer segments, each with N customers.

| Segment | WTP for A | WTP for B | WTP for Bundle |
|---------|-----------|-----------|----------------|
| α       | $v_A^α$  | $v_B^α$  | $v_A^α + v_B^α$ |
| β       | $v_A^β$  | $v_B^β$  | $v_A^β + v_B^β$ |

**Assumption**: additive valuations (bundle WTP = sum of individual WTPs). This is the standard Adams-Yellen assumption and holds when products are independent in utility.

**Negative correlation condition**:

```
v_A^α > v_A^β   AND   v_B^α < v_B^β
```

Segment α pays more for A, less for B. Segment β is the reverse.

---

## The Three Regimes (Adams-Yellen Taxonomy)

Given prices $(p_A, p_B, p_{AB})$, each consumer buys whichever option maximizes their surplus, subject to surplus ≥ 0.

A consumer chooses:
- **Bundle** if $(v_A + v_B - p_{AB}) \geq \max(v_A - p_A,\ v_B - p_B,\ 0)$
- **A only** if $(v_A - p_A) \geq \max(v_A + v_B - p_{AB},\ v_B - p_B,\ 0)$
- **B only** if $(v_B - p_B) \geq \max(v_A + v_B - p_{AB},\ v_A - p_A,\ 0)$
- **Nothing** otherwise

### Regime 1: Individual Pricing (no bundle offered)

Maximize:

```
π_ind = p_A · Q_A(p_A) + p_B · Q_B(p_B)
```

Each product is priced independently. Optimal: set $p_A$ at the highest WTP that still sells to at least one segment.

### Regime 2: Pure Bundling (bundle only, no individual sales)

```
π_pure = p_{AB} · (N_α + N_β)   if p_{AB} ≤ min(v_A^α + v_B^α, v_A^β + v_B^β)
```

The binding constraint is the lower-valuing segment. You set $p_{AB}$ just at or below $\min(\Sigma v^α, \Sigma v^β)$.

### Regime 3: Mixed Bundling (bundle + individual sales)

The most general regime. Allows the high-WTP segment for A to buy A individually at a premium, while the low-WTP segment for A still buys the bundle.

**Adams-Yellen theorem**: Mixed bundling weakly dominates both pure bundling and individual pricing. This means:

```
π_mixed ≥ π_pure ≥ 0   AND   π_mixed ≥ π_ind
```

The intuition: pure bundling and individual pricing are just special cases of mixed bundling with additional constraints (either $p_A = p_B = ∞$ or $p_{AB} = ∞$).

---

## Worked Numerical Example

**Setup**: 100 customers per segment. Zero marginal cost (digital goods).

| Segment | WTP_A | WTP_B | Count |
|---------|-------|-------|-------|
| α       | $80   | $30   | 100   |
| β       | $30   | $70   | 100   |

### Step 1 — Individual Pricing

For product A:
- Price at $80: only α buys → revenue = $80 × 100 = **$8,000**
- Price at $30: both buy → revenue = $30 × 200 = **$6,000**
- Optimal: $p_A = $80, revenue = $8,000

For product B:
- Price at $70: only β buys → revenue = $70 × 100 = **$7,000**
- Price at $30: both buy → revenue = $30 × 200 = **$6,000**
- Optimal: $p_B = $70, revenue = $7,000

**Total individual revenue = $15,000**

### Step 2 — Pure Bundling

Bundle valuations:
- α: $80 + $30 = $110
- β: $30 + $70 = $100

Set $p_{AB} = $100 (binding on β):
- Both segments buy → revenue = $100 × 200 = **$20,000**

Set $p_{AB} = $110 (only α buys):
- Revenue = $110 × 100 = **$11,000**

**Optimal pure bundle: $p_{AB} = $100, revenue = $20,000**

### Step 3 — Mixed Bundling

Now allow individual sales alongside the bundle. Can we do better than $20,000?

Try: $p_A = $80$, $p_B = $70$, $p_{AB} = $100$.

Check each segment's choice:
- α: Buy A at $80 (surplus $0), Buy B at $70 → surplus = $30-$70 = -$40 (no), Bundle surplus = $110-$100 = $10. **α buys A individually** (surplus $0 vs $10 for bundle — bundle wins if ≥ individual surplus).

Wait — α's A-only surplus = $80 - $80 = $0. Bundle surplus = $110 - $100 = $10. So α prefers **bundle**.

- β: A-only surplus = $30-$80 = -$50 (no). B-only surplus = $70-$70 = $0. Bundle surplus = $100-$100 = $0. β is **indifferent** between B-only and bundle; conventionally assign to bundle.

Revenue = $100 × 200 = **$20,000**. No gain yet.

Try: $p_A = $75$, $p_B = $65$, $p_{AB} = $100$.

- α: A-only surplus = $80-$75 = $5. Bundle surplus = $110-$100 = $10. α prefers **bundle**.
- β: B-only surplus = $70-$65 = $5. Bundle surplus = $100-$100 = $0. β prefers **B only**.

Revenue = $100 × 100 (bundle, α) + $65 × 100 (B only, β) = $10,000 + $6,500 = **$16,500**. Worse.

Try: $p_A = $80$, $p_B = $70$, $p_{AB} = $95$.

- α: A-only surplus = $0. Bundle surplus = $110-$95 = $15. **Bundle**.
- β: B-only surplus = $0. Bundle surplus = $100-$95 = $5. **Bundle** (weakly).

Revenue = $95 × 200 = **$19,000**. Worse than $100 bundle.

Try: $p_A = $60$, $p_B = $70$, $p_{AB} = $100$.

- α: A-only surplus = $80-$60 = $20. Bundle surplus = $110-$100 = $10. **A only**.
- β: B-only surplus = $70-$70 = $0. Bundle surplus = $100-$100 = $0. Indifferent; **bundle** (tie-break).

Revenue = $60 × 100 + $100 × 100 = $6,000 + $10,000 = **$16,000**. Worse.

In this 2×2 example, pure bundling at $100 is already optimal. Mixed bundling equals but does not exceed it. This illustrates the theorem — mixed bundling **weakly** dominates; in some cases equality holds.

**To see strict dominance, add a third segment:**

| Segment | WTP_A | WTP_B | Count |
|---------|-------|-------|-------|
| α       | $80   | $30   | 100   |
| β       | $30   | $70   | 100   |
| γ       | $80   | $70   | 100   |

Pure bundle at $100: all three buy → $100 × 300 = **$30,000**

Mixed bundle: $p_A = $80$, $p_B = $70$, $p_{AB} = $100$.

- α: A-only surplus = $0. Bundle surplus = $10. **Bundle**.
- β: B-only surplus = $0. Bundle surplus = $0. **Bundle** (tie).
- γ: A-only surplus = $0. B-only surplus = $0. Bundle surplus = $50. **Bundle**.

Revenue = **$30,000**. Equal.

Try: $p_A = $80$, $p_B = $70$, $p_{AB} = $130$.

- α: Bundle surplus = $110-$130 = -$20 (no). A-only surplus = $0. **A only**.
- β: Bundle surplus = $100-$130 = -$30 (no). B-only surplus = $0. **B only**.
- γ: Bundle surplus = $150-$130 = $20 > A-only $0, B-only $0. **Bundle**.

Revenue = $80×100 + $70×100 + $130×100 = $8,000 + $7,000 + $13,000 = **$28,000**. Worse.

Try: $p_A = $80$, $p_B = $70$, $p_{AB} = $109$.

- γ: Bundle surplus = $150-$109 = $41 > A-only $0. **Bundle**.
- α: Bundle surplus = $110-$109 = $1 > A-only $0. **Bundle**.
- β: Bundle surplus = $100-$109 = -$9. B-only surplus = $0. **B only**.

Revenue = $109×200 + $70×100 = $21,800 + $7,000 = **$28,800**. Worse than $30,000.

In this 3-segment case, pure bundling at $100 still wins. The classic strict-dominance examples require continuous or wider valuation distributions.

---

## The Negative Correlation Condition — Diagnostic Test

Before running the optimization, verify the correlation condition. With segment data:

```python
import statistics

wtp_a = [80, 30, 50]   # WTP for A per segment
wtp_b = [30, 70, 50]   # WTP for B per segment

def correlation(x, y):
    n = len(x)
    mx, my = sum(x)/n, sum(y)/n
    num = sum((x[i]-mx)*(y[i]-my) for i in range(n))
    denom = (sum((x[i]-mx)**2 for i in range(n)) *
             sum((y[i]-my)**2 for i in range(n))) ** 0.5
    return num / denom if denom else 0

r = correlation(wtp_a, wtp_b)
print(f"Valuation correlation: {r:.2f}")
# r < -0.3  → bundling likely beneficial
# -0.3 ≤ r ≤ 0.1 → mixed bundling, test both
# r > 0.1   → individual pricing likely better
```

**Threshold guidance** (empirical, not theoretical):

| Correlation r | Prediction |
|---------------|------------|
| r < −0.3      | Pure or mixed bundling wins |
| −0.3 ≤ r ≤ 0 | Mixed bundling may help; test |
| r > 0         | Individual pricing likely optimal |

These thresholds assume roughly symmetric valuation distributions. For skewed distributions, compute all three regime revenues directly.

---

## Welfare Implications (Why Bundling Can Be Controversial)

Adams & Yellen also showed that bundling is not always welfare-improving:

- **Seller surplus increases** (that's the point)
- **Consumer surplus may decrease**: customers who valued only one product now pay a bundle price that includes an unwanted product
- **Allocative efficiency**: bundling can cause some consumers to buy products they value at zero (welfare-neutral) or even reduce total welfare if the bundle forces suboptimal combinations

This is why antitrust authorities scrutinize **tying arrangements** — a firm with market power in product A that bundles it with B can foreclose competition in B. The legal test is whether the bundle is a genuine discount or a forced purchase.

**Safe harbor heuristic**: if $p_{AB} < p_A + p_B$, it reads as a consumer-friendly discount. If $p_A$ or $p_B$ are unavailable (pure bundling) for products with independent demand, regulatory risk rises.

---

## Extension: Continuous Valuation Distributions

With a continuous joint distribution $f(v_A, v_B)$, the firm solves:

```
max_{p_A, p_B, p_{AB}} ∫∫ R(v_A, v_B, p_A, p_B, p_{AB}) · f(v_A, v_B) dv_A dv_B
```

where $R(\cdot)$ is the revenue contribution of each consumer given optimal purchase decision.

**Uniform distribution benchmark**: if $(v_A, v_B) \sim \text{Uniform}([0,1]^2)$ independently:

- Individual pricing optimum: $p_A = p_B = 0.5$, revenue per consumer = $0.5 × 0.5 + 0.5 × 0.5 = 0.5$
- Pure bundle at $p_{AB} = 2/3$: consumers with $v_A + v_B \geq 2/3$ buy. Revenue $\approx 0.556$ per consumer (≈11% gain)
- Mixed bundling: small additional gain over pure bundling in the uniform case

The uniform case is positively correlated (independent), yet bundling still helps because of the **variance reduction effect**: the sum $v_A + v_B$ has lower relative variance than either component, so the seller can charge a higher fraction of mean surplus.

**Variance reduction formula** (for i.i.d. products):

```
Var(v_A + v_B) = Var(v_A) + Var(v_B) + 2·Cov(v_A, v_B)
```

Bundling effectively prices the sum. If Cov < 0, variance of the sum drops, enabling a tighter price. Lower variance → fewer consumers excluded at the optimal price → higher revenue.

---

## Decision Framework: Which Regime to Implement

```
1. Compute valuation correlation r across segments
   │
   ├── r < -0.3
   │     → Test pure bundling first (simpler, fewer SKUs)
   │     → If high-WTP single-product segment exists, add mixed
   │
   ├── -0.3 ≤ r ≤ 0.1
   │     → Run all three revenue calculations
   │     → Choose mixed bundling (weakly dominates, low downside)
   │
   └── r > 0.1
         → Individual pricing baseline
         → Bundling adds complexity without revenue gain
         → Consider only if bundle has lower marginal cost (e.g., shipping)

2. Check marginal cost
   └── If MC_A + MC_B > p_{AB} → bundling destroys margin
       Fix: raise p_{AB} or unbundle

3. Check segment count
   └── 2-3 segments → exact optimization tractable
       4+ segments → use grid search or linear programming
```

---

## Key Parameters the Model Does Not Capture

The Adams-Yellen model assumes:
1. **Additive valuations** — no complementarity or substitutability between products
2. **Complete information** — seller knows the valuation distribution
3. **Single purchase** — consumers buy once, no repeat purchase dynamics
4. **No resale** — consumers cannot arbitrage bundles

When these fail:
- **Complements** ($v_{AB} > v_A + v_B$): bundle price can exceed sum of individual prices; consumers still buy because complementarity adds value
- **Substitutes** ($v_{AB} < v_A + v_B$): bundling less effective; consumers prefer one product at a lower price
- **Uncertainty**: if the firm does not know the distribution, use revealed-preference data from A/B tests on bundle vs. individual pricing before committing
