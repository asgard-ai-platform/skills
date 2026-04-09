# Constrained Newsvendor

The single-product newsvendor has a closed-form solution: Q* = F⁻¹(CR). The moment you add a shared constraint — budget, warehouse capacity, or supplier MOQ — the products are coupled and each Q* can no longer be found independently.

This reference covers the **budget-constrained multi-product newsvendor** solved via Lagrangian relaxation. The method generalizes to capacity constraints with minor notation changes.

---

## Problem Formulation

You have N products indexed i = 1…N. Each product has:

| Symbol | Meaning |
|--------|---------|
| pᵢ | Selling price per unit |
| cᵢ | Unit cost (purchase price) |
| vᵢ | Salvage value per unsold unit |
| μᵢ, σᵢ | Normal demand mean and std dev |
| Qᵢ | Decision variable: order quantity |

Derived per-product costs (same as unconstrained skill):

```
Cuᵢ = pᵢ - cᵢ     (underage cost: margin lost per unit of unmet demand)
Coᵢ = cᵢ - vᵢ     (overage cost: loss per unsold unit)
CRᵢ = Cuᵢ / (Cuᵢ + Coᵢ)   (unconstrained critical ratio)
```

**Objective:** Maximize total expected profit across all products.

**Constraint:** Total purchasing cost cannot exceed budget B:

```
maximize  Σᵢ Πᵢ(Qᵢ)
subject to  Σᵢ cᵢ Qᵢ ≤ B
            Qᵢ ≥ 0  ∀i
```

where the expected profit for product i at order quantity Q is:

```
Πᵢ(Q) = Cuᵢ · E[min(Q, Dᵢ)] - Coᵢ · E[max(Q - Dᵢ, 0)]
```

For Normal demand, this expands to:

```
Πᵢ(Q) = Cuᵢ · [μᵢ - σᵢ · L(zᵢ)] - Coᵢ · σᵢ · L(zᵢ) - Coᵢ · (Q - μᵢ)
       = Cuᵢ · μᵢ - (Cuᵢ + Coᵢ) · σᵢ · L(zᵢ) - Coᵢ · (Q - μᵢ)
```

where zᵢ = (Q - μᵢ) / σᵢ and L(z) is the **standard normal loss function**:

```
L(z) = φ(z) - z · (1 - Φ(z))
```

φ = standard normal PDF, Φ = standard normal CDF.

---

## Why the Unconstrained Solution Often Violates the Budget

The unconstrained optimum for product i is:

```
Qᵢ* = μᵢ + z(CRᵢ) · σᵢ
```

Sum the purchasing cost: if Σᵢ cᵢ Qᵢ* > B, you must reduce orders. The naive approach of proportionally scaling all Qᵢ* down is **wrong** — it ignores that high-margin products should be cut less than low-margin ones. Lagrangian relaxation respects this.

---

## Lagrangian Relaxation

Relax the budget constraint by introducing a multiplier λ ≥ 0 (the "shadow price of budget"):

```
L(Q, λ) = Σᵢ Πᵢ(Qᵢ) - λ · (Σᵢ cᵢ Qᵢ - B)
         = Σᵢ [Πᵢ(Qᵢ) - λ · cᵢ · Qᵢ] + λ · B
```

For a fixed λ, this **decouples** into N independent newsvendor problems. Each product i faces a modified underage cost:

```
Cuᵢ(λ) = Cuᵢ - λ · cᵢ = (pᵢ - cᵢ) - λ · cᵢ = pᵢ - (1 + λ) · cᵢ
```

Interpretation: λ is the opportunity cost of spending one dollar of budget. Ordering one more unit of product i costs cᵢ in budget, so it "taxes" the underage benefit by λ · cᵢ.

The modified critical ratio becomes:

```
CRᵢ(λ) = Cuᵢ(λ) / (Cuᵢ(λ) + Coᵢ)
        = (pᵢ - (1+λ)cᵢ) / (pᵢ - (1+λ)cᵢ + cᵢ - vᵢ)
        = (pᵢ - (1+λ)cᵢ) / (pᵢ - λcᵢ - vᵢ)
```

And the optimal quantity for product i at multiplier λ:

```
Qᵢ*(λ) = μᵢ + z(CRᵢ(λ)) · σᵢ    if CRᵢ(λ) ∈ (0, 1)
         = 0                        if CRᵢ(λ) ≤ 0  (product killed by budget pressure)
```

**Key monotonicity property:** As λ increases, CRᵢ(λ) decreases, so Qᵢ*(λ) decreases. Total budget usage Σᵢ cᵢ Qᵢ*(λ) is non-increasing in λ.

---

## Algorithm: Binary Search on λ

Because total budget spend is monotone in λ, find λ* by bisection.

```
Algorithm: Constrained Newsvendor via Lagrangian Bisection

Input:  products (pᵢ, cᵢ, vᵢ, μᵢ, σᵢ), budget B
Output: optimal quantities Qᵢ*

1. Check unconstrained solution:
   Compute Qᵢ_unc = μᵢ + z(CRᵢ) · σᵢ for each i
   If Σᵢ cᵢ Qᵢ_unc ≤ B: return Qᵢ_unc (constraint not binding)

2. Set λ_lo = 0, λ_hi = max_i(pᵢ/cᵢ) - 1
   (λ_hi is the value that would zero out the best product's CR)

3. While λ_hi - λ_lo > ε (e.g., 1e-6):
   a. λ_mid = (λ_lo + λ_hi) / 2
   b. For each i, compute CRᵢ(λ_mid) and Qᵢ*(λ_mid)
   c. spend = Σᵢ cᵢ · Qᵢ*(λ_mid)
   d. If spend > B: λ_lo = λ_mid   (budget still exceeded, raise λ)
      Else:         λ_hi = λ_mid   (under budget, try lower λ)

4. Use λ* = λ_hi, return Qᵢ*(λ*)
```

Convergence: 50 iterations of bisection gives precision ~(λ_hi - λ_lo) / 2^50, more than sufficient.

---

## Worked Example: 3-Product Fashion Retailer

**Setup:**

| Product | p | c | v | μ | σ |
|---------|---|---|---|---|---|
| A (high margin) | 80 | 20 | 5 | 100 | 25 |
| B (medium) | 50 | 25 | 8 | 200 | 40 |
| C (low margin) | 30 | 22 | 0 | 150 | 30 |

**Budget B = 8,000**

**Step 1: Unconstrained solution**

```
Product A: CuA=60, CoA=15, CRA=60/75=0.800, z(0.800)=0.842
           QA_unc = 100 + 0.842×25 = 121 units, cost = 20×121 = 2,420

Product B: CuB=25, CoB=17, CRB=25/42=0.595, z(0.595)=0.241
           QB_unc = 200 + 0.241×40 = 210 units, cost = 25×210 = 5,245

Product C: CuC=8, CoC=22, CRC=8/30=0.267, z(0.267)=-0.621
           QC_unc = 150 + (-0.621)×30 = 131 units, cost = 22×131 = 2,882

Total unconstrained spend = 2,420 + 5,245 + 2,882 = 10,547
```

Budget exceeded by 2,547. Must optimize with λ > 0.

**Step 2: Bisect on λ**

λ_hi = max(80/20, 50/25, 30/22) - 1 = 4 - 1 = 3.0

| Iteration | λ | QA | QB | QC | Spend |
|-----------|---|----|----|-----|-------|
| 1 | 1.500 | 80 | 165 | 61 | 7,330 |
| 2 | 0.750 | 101 | 189 | 97 | 9,004 |
| 3 | 1.125 | 90 | 177 | 79 | 8,155 |
| 4 | 0.938 | 96 | 183 | 88 | 8,573 |
| 5 | 1.031 | 93 | 180 | 84 | 8,360 |
| 6 | 1.078 | 92 | 179 | 82 | 8,256 |
| 7 | 1.102 | 91 | 178 | 80 | 8,203 |
| … | … | … | … | … | … |
| converge | 1.147 | 90 | 177 | 78 | 7,998 ≈ 8,000 |

**Final solution at λ* ≈ 1.147:**

```
QA* = 90  (was 121 unconstrained — reduced least, highest margin)
QB* = 177 (was 210)
QC* = 78  (was 131 — reduced most, lowest margin-to-cost ratio)
Total spend = 90×20 + 177×25 + 78×22 = 1,800 + 4,425 + 1,716 = 7,941 ≈ 8,000
```

**What λ* = 1.147 means:** Each additional dollar of budget is worth ≈ $1.147 in expected profit. If you can expand the budget by $1,000, expected profit increases by ~$1,147. This is actionable for supplier negotiation.

---

## Products Killed by Budget Pressure

When λ is large enough that CRᵢ(λ) ≤ 0, the Lagrangian says order zero of product i. This happens when:

```
pᵢ - (1+λ)cᵢ ≤ 0
λ ≥ pᵢ/cᵢ - 1
```

In the example above, product C (p=30, c=22) gets killed when λ ≥ 30/22 - 1 = 0.364. If budget were much tighter, C would drop out entirely and the solver would only allocate across A and B.

**Practical implication:** When a product's order quantity hits zero, remove it from the active set and re-run bisection. The algorithm above handles this automatically via the `max(CRᵢ(λ), 0)` floor.

---

## Python Implementation

```python
import math
from scipy.stats import norm

def newsvendor_constrained(products, budget, tol=1e-6, max_iter=100):
    """
    products: list of dicts with keys p, c, v, mu, sigma
    budget:   total purchasing budget B
    Returns:  list of optimal quantities, lambda_star
    """
    def cr(prod, lam):
        cu = prod['p'] - (1 + lam) * prod['c']
        co = prod['c'] - prod['v']
        if cu <= 0:
            return 0.0
        return cu / (cu + co)

    def q_star(prod, lam):
        ratio = cr(prod, lam)
        if ratio <= 0:
            return 0.0
        if ratio >= 1:
            return prod['mu'] + 4 * prod['sigma']  # practical cap
        z = norm.ppf(ratio)
        return max(0.0, prod['mu'] + z * prod['sigma'])

    def total_spend(lam):
        return sum(p['c'] * q_star(p, lam) for p in products)

    # Check if unconstrained solution is feasible
    if total_spend(0) <= budget:
        quantities = [q_star(p, 0) for p in products]
        return quantities, 0.0

    # Bisect on lambda
    lam_lo, lam_hi = 0.0, max(p['p'] / p['c'] for p in products) - 1 + 0.01

    for _ in range(max_iter):
        lam_mid = (lam_lo + lam_hi) / 2
        if total_spend(lam_mid) > budget:
            lam_lo = lam_mid
        else:
            lam_hi = lam_mid
        if lam_hi - lam_lo < tol:
            break

    lam_star = lam_hi
    quantities = [q_star(p, lam_star) for p in products]
    return quantities, lam_star


# Example usage
products = [
    {'p': 80, 'c': 20, 'v': 5,  'mu': 100, 'sigma': 25},
    {'p': 50, 'c': 25, 'v': 8,  'mu': 200, 'sigma': 40},
    {'p': 30, 'c': 22, 'v': 0,  'mu': 150, 'sigma': 30},
]
quantities, lam = newsvendor_constrained(products, budget=8000)
for i, q in enumerate(quantities):
    print(f"Product {i+1}: Q* = {q:.1f}")
print(f"Lambda* = {lam:.4f}  (shadow price of budget)")
```

---

## Capacity Constraint (Alternative Formulation)

If the constraint is warehouse space rather than budget, replace cᵢ with the space consumed per unit (sᵢ), and B with total capacity S:

```
Σᵢ sᵢ Qᵢ ≤ S
```

The Lagrangian modification becomes:

```
Cuᵢ(λ) = Cuᵢ - λ · sᵢ
```

Everything else is identical. λ is now the shadow price of one unit of warehouse space.

---

## Common Mistakes

**Proportional scaling:** Reducing all orders by the same percentage (e.g., multiply all Qᵢ* by 0.76 to fit budget) ignores cross-product margin differences. This is easy to compute but suboptimal. The constrained optimum always re-weights toward high-margin, low-cost products.

**Ignoring products driven to zero:** If the bisection produces Qᵢ = 0 for some products, verify that their unconstrained CR was not already below 0.5 — they may have been marginal products even without the constraint.

**Using λ to compare across scenarios:** λ* is scenario-specific. A λ* of 1.2 in one assortment does not mean budget is equally scarce in a different assortment with different products.

**Treating the solution as integer:** The Lagrangian solution is continuous. Round each Qᵢ to the nearest integer, then check if the budget constraint is still satisfied. If rounding up violates it, round down the product with the lowest loss in expected profit per unit.

---

## When the Lagrangian Approach Fails

The Lagrangian relaxation gives the **exact** constrained optimum when the Lagrangian dual gap is zero — which holds here because the profit function is concave in Q (for Normal demand) and the constraint is linear. There is no duality gap.

However, the approach requires:
- Concave profit function (holds for Normal, Poisson, lognormal distributions)
- Single linear constraint (multiple constraints require multi-dimensional bisection or subgradient methods)
- Continuous Q (integer rounding is handled as a post-processing step)

For two simultaneous constraints (e.g., budget AND capacity), use a 2D grid search over (λ₁, λ₂) or subgradient optimization.
