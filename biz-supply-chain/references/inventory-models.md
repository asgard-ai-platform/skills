# Inventory Models Reference

Inventory sits at the intersection of **Plan** and **Source** in the SCOR model. Too much = cash tied up, obsolescence risk, high holding cost. Too little = stockouts, backorders, lost sales, and the downstream delivery failures that surface as customer complaints. These models give you the math to find the right amount.

---

## The Four Questions Every Model Answers

| Question | Model / Method |
|---|---|
| How much to order at once? | EOQ (Economic Order Quantity) |
| When to trigger a reorder? | ROP (Reorder Point) + Safety Stock |
| How much buffer to hold against uncertainty? | Safety Stock calculation |
| Which items deserve the most attention? | ABC / ABC-XYZ classification |

---

## 1. EOQ — Economic Order Quantity

EOQ minimizes total inventory cost by balancing ordering cost against holding cost.

### Formula

```
EOQ = √(2DS / H)

D = Annual demand (units/year)
S = Cost per order (setup/ordering cost, in $)
H = Annual holding cost per unit ($ per unit per year)
    H is often expressed as (unit cost × holding rate), e.g., $50 × 25% = $12.50/yr
```

### Worked Example

A Taiwanese electronics brand sells 12,000 units/year of a main PCB component.

- `D = 12,000` units/year
- `S = NT$800` per purchase order (admin, inspection, receiving labor)
- Unit cost = NT$500; holding rate = 25%/year
- `H = 500 × 0.25 = NT$125` per unit per year

```
EOQ = √(2 × 12,000 × 800 / 125)
    = √(19,200,000 / 125)
    = √153,600
    ≈ 392 units per order
```

**Number of orders per year** = 12,000 / 392 ≈ 31 orders
**Average cycle inventory** = 392 / 2 = 196 units

### Total Cost Check

```
Total cost = (D/Q) × S + (Q/2) × H
           = (12,000/392) × 800 + (392/2) × 125
           = 30.6 × 800  +  196 × 125
           = 24,490  +  24,500
           ≈ NT$48,990 / year
```

The symmetry (ordering cost ≈ holding cost) is a sanity check: at EOQ, these two costs are always equal.

### EOQ Assumptions and Where They Break

| Assumption | Reality Check |
|---|---|
| Demand is constant and known | Promotions, seasonality break this — see ABC-XYZ |
| Lead time is fixed and known | Supplier variability breaks this — add safety stock |
| No quantity discounts | If supplier offers tiered pricing, run EOQ at each tier and compare total cost |
| Infinite shelf life | Perishables require time-sensitive variants (e.g., newsvendor model) |
| Single item, single location | Multi-echelon inventory requires more complex models |

**Practical rule**: EOQ gives you the right *order of magnitude*. Don't treat the output as a precise target — round to the nearest pallet or MOQ, then recalculate total cost.

---

## 2. Reorder Point (ROP)

EOQ tells you *how much* to order. ROP tells you *when* to order.

### Formula

```
ROP = d̄ × L + SS

d̄ = Average daily demand (units/day)
L  = Lead time (days)
SS = Safety stock (units) — see Section 3
```

### Worked Example (continuing from above)

- `D = 12,000` units/year → `d̄ = 12,000 / 250 = 48` units/day (250 working days)
- Supplier lead time from Shenzhen: `L = 14` days
- Safety stock (calculated below): `SS = 180` units

```
ROP = 48 × 14 + 180
    = 672 + 180
    = 852 units
```

**Interpretation**: When on-hand inventory drops to 852 units, place the next order. It will arrive in ~14 days, just as stock approaches safety stock level.

---

## 3. Safety Stock

Safety stock is the buffer against two sources of variability: **demand uncertainty** and **lead time uncertainty**.

### Method A: Service Level Approach (Most Common)

```
SS = z × σ_demand × √L

z           = z-score for target service level
σ_demand    = Standard deviation of daily demand (units/day)
L           = Lead time (days)
```

**Service Level → z-score table:**

| Target Service Level | z-score |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |

Service level here = probability of *not* stocking out during a replenishment cycle.

### Method A Worked Example

Same PCB component:
- Target service level: 95% → `z = 1.65`
- Historical daily demand std dev: `σ_demand = 12` units/day
- Lead time: `L = 14` days

```
SS = 1.65 × 12 × √14
   = 1.65 × 12 × 3.742
   = 74.1 ≈ 75 units
```

This is safety stock against **demand variability only** (assumes lead time is constant).

### Method B: Combined Demand + Lead Time Variability

When the supplier's lead time is also variable (the Shenzhen supplier in the SKILL.md example):

```
SS = z × √(L × σ_d² + d̄² × σ_L²)

σ_d = Std dev of daily demand
σ_L = Std dev of lead time (days)
d̄   = Average daily demand
L   = Average lead time
```

### Method B Worked Example

- `z = 1.65` (95% service level)
- `d̄ = 48` units/day, `σ_d = 12` units/day
- `L = 14` days, `σ_L = 3` days (supplier on-time rate is inconsistent)

```
SS = 1.65 × √(14 × 12² + 48² × 3²)
   = 1.65 × √(14 × 144 + 2304 × 9)
   = 1.65 × √(2,016 + 20,736)
   = 1.65 × √22,752
   = 1.65 × 150.8
   = 248.8 ≈ 249 units
```

Adding lead time variability more than **tripled** the required safety stock (75 → 249 units). This is why fixing the Shenzhen supplier's reliability (SCOR Source metric: Supplier On-Time Rate) directly reduces inventory cost — it's not just about delivery predictability, it cuts the safety stock requirement.

**Revised Inventory Days** with Method B:
- Cycle stock: 392 / 2 = 196 units
- Safety stock: 249 units
- Average total inventory: 196 + 249 = 445 units
- At 48 units/day → **9.3 days of inventory**

---

## 4. ABC Classification

Not all SKUs deserve the same inventory model and attention. ABC classifies by revenue or cost contribution.

### Classification Rules

| Class | % of SKUs | % of Revenue/Value | Treatment |
|---|---|---|---|
| A | ~20% | ~80% | Tight control, frequent review, sophisticated models |
| B | ~30% | ~15% | Moderate control, periodic review |
| C | ~50% | ~5% | Loose control, simplify, min-max policies |

### How to Run the Classification

```
1. List all SKUs with annual usage value = (annual units sold × unit cost)
2. Sort descending by annual usage value
3. Calculate cumulative % of total value
4. Assign A / B / C cutoffs (80% / 95% / 100% cumulative value)
```

### ABC-XYZ Extension

Add a second dimension for **demand variability** (XYZ):

| Class | Coefficient of Variation (CV = σ/μ) | Meaning |
|---|---|---|
| X | CV < 0.5 | Stable, predictable demand |
| Y | 0.5 ≤ CV < 1.0 | Seasonal or moderate variability |
| Z | CV ≥ 1.0 | Highly irregular, lumpy demand |

**CV formula:**
```
CV = (Standard Deviation of demand) / (Mean demand)
     measured over rolling 12 months, same time bucket (weekly or monthly)
```

### ABC-XYZ Decision Matrix

| Class | Inventory Approach |
|---|---|
| AX | EOQ + ROP with tight safety stock; review weekly |
| AY | Safety stock + S&OP integration; review weekly |
| AZ | Make-to-order if possible; no bulk inventory; escalate to Plan team |
| BX | Standard ROP; review monthly |
| BY | Min-max policy; review monthly |
| BZ | Min-max with buffer; consider consolidating with suppliers |
| CX | Min-max with large lot (reduce ordering cost); review quarterly |
| CY | Periodic review; consider consignment from supplier |
| CZ | Eliminate SKU or special-order only; high risk of obsolescence |

**AZ items are the supply chain manager's biggest headache**: high value AND unpredictable. Do not apply EOQ here — it assumes stable demand and will systematically under- or over-stock.

---

## 5. Inventory Days (DSI) and Target-Setting

The SKILL.md SCOR dashboard uses **Inventory Days** as the Plan process metric.

```
Inventory Days (DSI) = Inventory / (COGS / 365)

or equivalently:

DSI = Average Inventory (units) / Average Daily Demand (units/day)
```

### Industry Benchmarks

| Industry | Typical DSI Target |
|---|---|
| FMCG / Grocery | 15–30 days |
| Consumer Electronics | 30–60 days |
| Automotive Parts | 20–45 days |
| Apparel (fast fashion) | 30–60 days |
| Industrial B2B | 45–90 days |
| Pharmaceuticals | 60–120 days |

**Warning**: Low DSI is not always good. If DSI drops below lead time + safety stock coverage, stockouts are guaranteed. Calculate the floor:

```
Minimum viable DSI = Lead Time (days) + Safety Stock Days
                   = L + (SS / d̄)
```

Using the example above: `14 + (249 / 48) = 14 + 5.2 ≈ 20 days minimum`.
Pushing DSI below 20 days for this item would cause stockouts even with 95% service level target.

---

## 6. Choosing the Right Model — Decision Tree

```
Is demand stable and continuous?
├── YES → Use EOQ + ROP
│         ├── Is lead time variable?  → Use Method B safety stock
│         └── Is lead time fixed?     → Use Method A safety stock
│
└── NO → Is it lumpy / project-based?
          ├── YES → Make-to-order; no standing inventory
          └── NO (seasonal) → Use time-phased MRP or newsvendor model
                              (outside scope of this reference)
```

**Additional forcing conditions:**
- Supplier requires MOQ > EOQ → Order at MOQ, recalculate cost
- Product has shelf life < lead time → Cannot pre-stock; redesign supply chain
- Demand CV > 1.0 (Z class) → Standard EOQ/ROP will fail; escalate

---

## 7. Interaction with SCOR Metrics

| Safety Stock Driver | SCOR Process | Metric to Improve |
|---|---|---|
| High `σ_demand` | Plan | Forecast Accuracy |
| High `σ_L` (supplier variability) | Source | Supplier On-Time Rate |
| Long `L` (average lead time) | Source | Supplier Lead Time |
| High `z` required (high service target) | Deliver | Perfect Order Rate target |
| High unit cost → high `H` | Source | Unit Cost / Make-vs-Buy |

The Iron Law applies directly here: **reducing safety stock requires fixing the upstream root cause** (forecast accuracy or supplier reliability), not just adjusting the inventory model parameters.
