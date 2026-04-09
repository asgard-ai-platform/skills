# EOQ Model — Economic Order Quantity

EOQ answers one question: **given a fixed annual demand and known costs, what order size minimizes total inventory cost?**

It is most useful for A-class items with relatively stable demand. For C-class items with erratic demand, a simple min/max rule is usually sufficient.

---

## Core Formula

```
EOQ = √( 2 × D × S / H )

Where:
- D  = Annual demand (units/year)
- S  = Ordering cost per order (固定費用，每次下單的成本, e.g., admin, shipping setup)
- H  = Annual holding cost per unit (= unit cost × carrying cost %)
```

**Total Annual Cost at EOQ:**

```
TAC = (D / Q) × S  +  (Q / 2) × H

     └─ ordering cost ─┘  └─ holding cost ─┘

At Q = EOQ, ordering cost = holding cost (they balance exactly).
```

---

## Worked Example

**Scenario**: An e-commerce shop sells a phone case (SKU: PC-001).

| Input | Value |
|-------|-------|
| Annual demand (D) | 1,200 units/year |
| Unit cost | NT$150 |
| Carrying cost rate | 25%/year |
| Holding cost per unit (H) | NT$150 × 25% = **NT$37.5/year** |
| Ordering cost per order (S) | NT$600 (admin + shipping setup) |

**Step 1: Compute EOQ**

```
EOQ = √( 2 × 1,200 × 600 / 37.5 )
    = √( 1,440,000 / 37.5 )
    = √( 38,400 )
    = 196 units  ≈ 200 units (round to a practical lot size)
```

**Step 2: Orders per year**

```
Orders/year = D / EOQ = 1,200 / 200 = 6 orders/year
              → roughly one order every 2 months
```

**Step 3: Verify total cost**

```
Ordering cost = (1,200 / 200) × 600 = NT$3,600/year
Holding cost  = (200 / 2) × 37.5   = NT$3,750/year
TAC           = NT$7,350/year
```

At EOQ the two halves are nearly equal — this is the mathematical minimum.

**Comparison: What if they ordered 500 units at a time?**

```
Ordering cost = (1,200 / 500) × 600 = NT$1,440/year
Holding cost  = (500 / 2) × 37.5   = NT$9,375/year
TAC           = NT$10,815/year  (+47% vs EOQ)
```

Over-ordering roughly doubles holding cost while under-saving ordering cost.

---

## Sensitivity: EOQ Is Robust to Estimate Errors

EOQ's biggest practical strength is **flatness near the optimum**. The total cost curve is shallow — a 50% error in your inputs moves total cost by far less than 50%.

| If your EOQ estimate is off by... | TAC increases by... |
|-----------------------------------|---------------------|
| 10% | ~0.5% |
| 25% | ~3% |
| 50% | ~11% |
| 100% (order 2× EOQ) | ~25% |

**Implication**: don't spend days perfecting your S and H estimates. A rough EOQ beats gut instinct ordering by a wide margin.

---

## Connecting EOQ to Reorder Point

EOQ tells you **how much** to order. The reorder point (from SKILL.md) tells you **when** to order.

```
Reorder Point = (Avg Daily Demand × Lead Time) + Safety Stock

Order Cycle   = EOQ / Avg Daily Demand  (days between orders)
```

**Continuing the example** (lead time = 14 days, σ_d = 5 units, service level 95%):

```
Avg daily demand  = 1,200 / 365 ≈ 3.3 units/day
Safety stock      = 1.65 × 5 × √14 ≈ 31 units
Reorder Point     = 3.3 × 14 + 31  ≈ 77 units
```

So the operating rule for PC-001 is:
- When stock drops to **77 units**, place an order for **200 units**.

---

## When EOQ Assumptions Break Down

EOQ requires four assumptions. When they fail, the model needs adjustment or replacement.

| Assumption | When it breaks | What to do |
|------------|---------------|------------|
| Demand is constant and known | Seasonal products, trend items | Use seasonal forecast; recalculate EOQ per season |
| Unit cost is fixed (no volume discounts) | Supplier offers tiered pricing | Use EOQ with quantity discount model (see below) |
| Entire order arrives at once | Long production runs, partial shipments | Use Production Order Quantity variant |
| Ordering cost is fixed | Digital/EDI orders where S ≈ 0 | EOQ → very small batches; use JIT or replenishment triggers instead |

---

## EOQ with Quantity Discounts

When suppliers offer price breaks, compare **total cost including purchase cost** at each price tier.

**Procedure:**

1. Calculate EOQ at each unit price.
2. Check if the computed EOQ is feasible (≥ the minimum quantity for that tier).
3. If feasible: compute TAC = purchase cost + ordering cost + holding cost.
4. If not feasible: use the minimum quantity for that tier, compute TAC.
5. Pick the tier with the lowest TAC.

**Example extension** — Supplier offers:

| Order Qty | Unit Price |
|-----------|-----------|
| 1–299 | NT$150 |
| 300–599 | NT$140 |
| 600+ | NT$130 |

Compute TAC for each tier (D = 1,200, S = 600, carrying rate = 25%):

**Tier 1 (NT$150, H = 37.5):**
- EOQ = 200 (feasible: 200 < 300 ✓)
- TAC = 1,200 × 150 + 3,600 + 3,750 = **NT$187,350**

**Tier 2 (NT$140, H = 35):**
- EOQ = √(2 × 1,200 × 600 / 35) = 202 → not feasible (need 300+), use Q = 300
- TAC = 1,200 × 140 + (1,200/300)×600 + (300/2)×35 = 168,000 + 2,400 + 5,250 = **NT$175,650**

**Tier 3 (NT$130, H = 32.5):**
- EOQ = 210 → not feasible (need 600+), use Q = 600
- TAC = 1,200 × 130 + (1,200/600)×600 + (600/2)×32.5 = 156,000 + 1,200 + 9,750 = **NT$166,950** ← lowest

**Decision**: Order 600 units at a time despite holding more inventory — the price discount outweighs the extra holding cost.

---

## Python Snippet

```python
import math

def eoq(D: float, S: float, H: float) -> float:
    """
    D: annual demand (units)
    S: ordering cost per order (currency)
    H: annual holding cost per unit (currency)
    Returns: EOQ (units)
    """
    return math.sqrt(2 * D * S / H)

def total_annual_cost(D: float, S: float, H: float, Q: float,
                      unit_cost: float = 0.0) -> float:
    """Includes optional purchase cost."""
    return (D / Q) * S + (Q / 2) * H + D * unit_cost

def reorder_point(avg_daily_demand: float, lead_time: float,
                  safety_stock: float) -> float:
    return avg_daily_demand * lead_time + safety_stock


# --- Example ---
D, S, unit_cost, carrying_rate = 1200, 600, 150, 0.25
H = unit_cost * carrying_rate

q = eoq(D, S, H)
print(f"EOQ: {q:.0f} units")
print(f"Orders/year: {D/q:.1f}")
print(f"TAC: {total_annual_cost(D, S, H, q, unit_cost):,.0f}")
```

Output:
```
EOQ: 196 units
Orders/year: 6.1
TAC: 187,350
```

---

## ABC Class Application

Per the parent skill's Iron Law, not all SKUs deserve EOQ analysis.

| Class | EOQ Worth Computing? | Recommended Approach |
|-------|---------------------|---------------------|
| **A** | Yes — compute precisely, review quarterly | Full EOQ + safety stock + reorder point |
| **B** | Optional — use EOQ or round to practical lot | EOQ with simplified safety stock |
| **C** | Usually no | Min/max levels; fixed reorder quantities |

For a 500-SKU catalogue: roughly 100 A-items justify rigorous EOQ. The remaining 400 B/C items can use simplified rules. This matches the Pareto principle in SKILL.md.

---

## Common Mistakes

- **Using retail price instead of COGS for H**: H must be based on the cost you have tied up, not the selling price.
- **Forgetting capital cost in H**: Carrying cost % should include the opportunity cost of capital (typically 10-15% of the 20-30% total). Underestimating H overstates EOQ and leads to over-ordering.
- **Applying EOQ to seasonal items without adjustment**: A coat with demand concentrated in Oct-Feb will have very different optimal order quantities in each season than an annual EOQ implies. Segment by season or use a rolling 90-day demand window.
- **Treating EOQ as the only input to order quantity**: Supplier minimums, shelf capacity, expiry dates, and container fill rates are hard constraints that override the EOQ optimum. Use EOQ as a starting point and adjust upward to the nearest feasible quantity.
- **Recalculating too infrequently**: If demand or costs shift significantly, the EOQ shifts too. Recalculate A-item EOQs quarterly or when a major demand change occurs.
