# EOQ with Quantity Discounts

When a supplier offers price breaks at certain order quantities, the standard EOQ formula is no longer sufficient. A lower unit price reduces holding cost H (since H = unit cost × holding rate), which shifts the optimal order quantity. You must compare total annual cost — including purchase cost — across all feasible price tiers.

---

## Two Discount Structures

### All-Units Discount

The discount applies to **every unit** in the order once the quantity threshold is crossed.

| Order Quantity | Unit Price |
|----------------|------------|
| 0–499          | $10.00     |
| 500–999        | $9.50      |
| 1000+          | $9.00      |

If you order 500 units, **all 500** cost $9.50 each.

### Incremental (Marginal) Discount

The discount applies only to units **within each tier**, like a progressive tax.

| Units | Unit Price |
|-------|------------|
| First 499  | $10.00 |
| Units 500–999 | $9.50 |
| Units 1000+ | $9.00 |

If you order 600 units: 499 × $10.00 + 101 × $9.50 = $5,949.50 (avg ≈ $9.92/unit).

**Incremental discounts are rare in practice.** Most supplier contracts use all-units discounts. This document focuses on all-units; a brief note on incremental appears at the end.

---

## Total Annual Cost with Purchase Cost

Standard EOQ only minimizes ordering + holding cost. With discounts, you must also include **annual purchase cost** because the unit price differs by tier:

```
TC(Q, P) = D×P  +  (D/Q)×S  +  (Q/2)×H(P)
           ────     ────────     ─────────────
         purchase   ordering      holding
```

Where:
- `D` = annual demand (units/year)
- `P` = unit price for the applicable tier
- `S` = fixed cost per order
- `H(P)` = holding cost per unit per year = `P × h` (h = holding rate, e.g. 0.25)
- `Q` = order quantity

Since H depends on P, each price tier has its own EOQ.

---

## All-Units Discount: Step-by-Step Procedure

**Setup variables:** D, S, h (holding rate as decimal, e.g. 0.25), and a price schedule with n tiers.

### Step 1 — Compute EOQ for Each Tier

For each price tier i with unit price Pᵢ:

```
Hᵢ = Pᵢ × h
EOQᵢ = √(2 × D × S / Hᵢ)
```

### Step 2 — Check Feasibility

Each EOQᵢ must fall within the quantity range [Qᵢ_min, Qᵢ_max) that qualifies for price Pᵢ.

- If EOQᵢ < Qᵢ_min: **round up to Qᵢ_min** (you must order at least that much to get this price)
- If EOQᵢ > Qᵢ_max: this tier's EOQ is **infeasible** — drop it from consideration
- If Qᵢ_min ≤ EOQᵢ < Qᵢ_max: EOQᵢ is **feasible as-is**

### Step 3 — Compute Total Annual Cost for Each Candidate

For each feasible candidate quantity Qᵢ (after rounding):

```
TC(Qᵢ) = D × Pᵢ  +  (D / Qᵢ) × S  +  (Qᵢ / 2) × Hᵢ
```

### Step 4 — Select the Minimum

Pick the candidate Qᵢ with the lowest TC(Qᵢ).

---

## Worked Example

**Inputs:**
- D = 10,000 units/year
- S = $200/order
- h = 0.25 (25% of unit cost per year)

**Price schedule (all-units):**

| Tier | Min Qty | Unit Price Pᵢ |
|------|---------|--------------|
| 1    | 0       | $10.00       |
| 2    | 500     | $9.50        |
| 3    | 1,000   | $9.00        |

---

### Step 1: EOQ per Tier

**Tier 1** (P = $10.00, H = 10.00 × 0.25 = $2.50):
```
EOQ₁ = √(2 × 10000 × 200 / 2.50)
      = √(4,000,000 / 2.50)
      = √1,600,000
      = 1,265 units
```

**Tier 2** (P = $9.50, H = $2.375):
```
EOQ₂ = √(2 × 10000 × 200 / 2.375)
      = √(4,000,000 / 2.375)
      = √1,684,211
      = 1,298 units
```

**Tier 3** (P = $9.00, H = $2.25):
```
EOQ₃ = √(2 × 10000 × 200 / 2.25)
      = √(4,000,000 / 2.25)
      = √1,777,778
      = 1,333 units
```

---

### Step 2: Feasibility Check

| Tier | Qty Range   | EOQᵢ  | Feasible? | Candidate Qᵢ |
|------|-------------|-------|-----------|--------------|
| 1    | [0, 499]    | 1,265 | No — above range | Drop |
| 2    | [500, 999]  | 1,298 | No — above range | Drop |
| 3    | [1,000, ∞)  | 1,333 | Yes — in range   | **1,333** |

Only Tier 3 produces a feasible EOQ. But we must also check the **minimum quantity threshold of each lower tier** — specifically, the boundary quantities 500 and 1,000. For all-units discounts, a standard procedure is to also evaluate the minimum quantity of any tier whose EOQ was rounded up or was infeasible.

Re-evaluate with candidate quantities: {500 (Tier 2 min), 1,000 (Tier 3 min), 1,333 (Tier 3 EOQ)}.

Wait — Tier 1's EOQ (1,265) falls outside Tier 1's range, and Tier 2's EOQ (1,298) falls outside Tier 2's range. In both cases the computed EOQ exceeds the tier's upper bound, which means ordering *less* than EOQ is forced if you want that price — you'd be on the wrong side of the cost curve. These are truly infeasible.

However, always include the **lowest quantity that qualifies for each non-dropped tier** as a candidate, in case a discount is so large it outweighs the suboptimal ordering cost:

Candidates: 500 (Tier 2 at its min), 1,000 (Tier 3 at its min), 1,333 (Tier 3 EOQ).

---

### Step 3: Total Annual Cost for Each Candidate

**Q = 500 (Tier 2, P = $9.50, H = $2.375):**
```
TC = 10000×9.50  +  (10000/500)×200  +  (500/2)×2.375
   = 95,000  +  4,000  +  593.75
   = $99,593.75
```

**Q = 1,000 (Tier 3, P = $9.00, H = $2.25):**
```
TC = 10000×9.00  +  (10000/1000)×200  +  (1000/2)×2.25
   = 90,000  +  2,000  +  1,125
   = $93,125.00
```

**Q = 1,333 (Tier 3, P = $9.00, H = $2.25):**
```
TC = 10000×9.00  +  (10000/1333)×200  +  (1333/2)×2.25
   = 90,000  +  1,500  +  1,499.63
   = $92,999.63
```

---

### Step 4: Decision

| Candidate Q | Price  | TC           |
|-------------|--------|--------------|
| 500         | $9.50  | $99,593.75   |
| 1,000       | $9.00  | $93,125.00   |
| **1,333**   | $9.00  | **$92,999.63** ← minimum |

**Optimal: order 1,333 units per order.**

The saving vs. no-discount EOQ at $10.00 is meaningful: standard EOQ at $10 (1,265 units) yields TC = $90,000 + $1,581 + $1,581 = $93,162, but only if you could actually buy at $10/unit with Q=1,265 — which falls in Tier 3 range, so you'd get $9.00 anyway. The discount saves $90,000 → already baked in.

---

## Python Implementation

```python
import math
from typing import List, Tuple

def eoq_all_units_discount(
    D: float,
    S: float,
    h: float,
    price_schedule: List[Tuple[float, float]],  # (min_qty, unit_price), sorted by min_qty
) -> dict:
    """
    EOQ with all-units quantity discounts.

    price_schedule: list of (min_qty, unit_price) tuples, ascending by min_qty.
    Example: [(0, 10.0), (500, 9.50), (1000, 9.0)]

    Returns: dict with optimal_q, unit_price, total_cost, and all candidates.
    """
    candidates = []

    for i, (q_min, P) in enumerate(price_schedule):
        H = P * h

        # Upper bound of this tier
        q_max = price_schedule[i + 1][0] if i + 1 < len(price_schedule) else float('inf')

        # EOQ for this tier's holding cost
        eoq_i = math.sqrt(2 * D * S / H)

        # Feasibility: EOQ must be within [q_min, q_max)
        if eoq_i >= q_max:
            # EOQ is above this tier's range — infeasible as an EOQ candidate
            # Still evaluate q_min as a candidate for discount benefit
            q_candidate = q_min
        elif eoq_i < q_min:
            # EOQ is below min threshold — round up to q_min
            q_candidate = q_min
        else:
            q_candidate = eoq_i

        # Total cost at candidate quantity with this tier's price
        TC = D * P + (D / q_candidate) * S + (q_candidate / 2) * H
        candidates.append({
            "tier": i,
            "q_candidate": round(q_candidate, 2),
            "unit_price": P,
            "total_cost": round(TC, 2),
        })

    best = min(candidates, key=lambda x: x["total_cost"])
    return {
        "optimal_q": best["q_candidate"],
        "unit_price": best["unit_price"],
        "total_cost": best["total_cost"],
        "all_candidates": candidates,
    }


# Verify with worked example
if __name__ == "__main__":
    result = eoq_all_units_discount(
        D=10000,
        S=200,
        h=0.25,
        price_schedule=[(0, 10.0), (500, 9.50), (1000, 9.0)],
    )
    print(result)
    assert abs(result["optimal_q"] - 1333) < 2, f"Expected ~1333, got {result['optimal_q']}"
    assert result["unit_price"] == 9.0
    assert result["total_cost"] < 93000
    print("All assertions passed.")
```

---

## Decision Heuristic (When Not to Bother Computing)

Before running the full procedure, these rules of thumb help:

| Condition | Likely outcome |
|-----------|----------------|
| Discount < 1% of unit price | Discount savings rarely outweigh increased holding cost; standard EOQ is fine |
| Required minimum order > 2× standard EOQ | Deep inventory build-up; likely not worth it unless discount > 5% |
| Holding rate h > 40% (perishables, fashion) | High holding cost amplifies the penalty for ordering too much; discount must be large |
| Lead time > 90 days | Reorder timing risk dominates; solve lead time problem first |

These are rough screens, not substitutes for the full calculation.

---

## Incremental Discount: Brief Note

With incremental discounts, there is no clean per-tier EOQ formula because the effective unit cost varies with Q. The approach:

1. Express total purchase cost as a piecewise linear function of Q.
2. Write TC(Q) as a piecewise function; differentiate each piece and solve.
3. Check feasibility of each critical point within its tier's range.
4. Compare all feasible critical points.

In practice, incremental discounts almost never appear in supplier contracts. If you encounter one, confirm with the supplier — it is more likely an all-units discount described ambiguously.

---

## Interaction with Safety Stock

EOQ with discounts changes Q but does not change the **reorder point** formula:

```
ROP = d × L + SS
```

Where `d` = average daily demand, `L` = lead time in days, `SS` = safety stock.

However, a larger Q means **fewer orders per year**, which means each stockout event has higher cost consequence (you wait longer for the next replenishment). If the optimal discount-adjusted Q is significantly larger than the base EOQ, review whether your safety stock is still adequate for the longer order cycle.

Order cycle length at discount-optimal Q:

```
T = Q* / D   (in years)
```

If T increases substantially, recalculate safety stock using the longer review period.

---

## Common Errors

**Forgetting to include annual purchase cost in TC.** Standard EOQ drops `D×P` because it's constant regardless of Q. With discounts, P varies by tier, so `D×P` is no longer constant — it must be in the comparison.

**Evaluating EOQ at the wrong holding cost.** H = unit cost × holding rate. When unit cost drops (discount tier), H drops too, shifting EOQ upward. Using the undiscounted H for a lower-priced tier underestimates the discount-adjusted EOQ.

**Accepting the first feasible solution.** Always evaluate all candidate quantities. The minimum-quantity threshold of a deeper discount tier may produce a lower TC than the natural EOQ of a shallower tier.

**Applying EOQ with quantity discounts to perishable or fashion goods.** The flat-cost-curve property of EOQ assumes unlimited shelf life. For perishables, the cost of holding excess inventory is non-linear (spoilage accelerates), and discount-chasing can cause write-offs that dwarf the savings.
