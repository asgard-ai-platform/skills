# Revenue Management Models (Airline / Hotel)

Revenue management (RM) is the discipline of allocating limited, perishable capacity to maximize total revenue. The canonical setting: a fixed number of seats or rooms, multiple fare classes, and a booking horizon that ends at departure/check-in. This document covers the mathematical core you need to implement or reason about these systems.

---

## Core Setup

| Symbol | Meaning |
|--------|---------|
| `C` | Total capacity (seats, rooms) |
| `n` | Number of fare classes, indexed `1..n`, sorted low-to-high fare |
| `f_i` | Fare (revenue per unit) for class `i`, so `f_1 < f_2 < ... < f_n` |
| `D_i` | Random demand for class `i` over the booking horizon |
| `x_i` | Number of units to accept from class `i` (decision variable) |
| `b` | Bid price — the shadow price of one unit of capacity |

RM assumes bookings arrive sequentially, low fares first (discount bookers commit early, premium bookers late). This is the **nested booking** assumption: if you close class 2, you implicitly close all cheaper classes.

---

## Littlewood's Rule (Two-Class Case)

The foundation of all RM. With two fare classes (`f_L < f_H`):

**Accept a low-fare request if and only if:**

```
f_L ≥ f_H × P(D_H > remaining capacity)
```

In words: accept the cheap booking only if its revenue exceeds the expected revenue you would have earned from a future high-fare booking that gets displaced.

### Worked Example

- 100 seats remaining, 60 days until departure
- Low fare: $200, High fare: $500
- Historical high-fare demand: Normal(μ=40, σ=15)

At 100 seats remaining, `P(D_H > 100) ≈ 0` — accept all low-fare bookings.

At 45 seats remaining:
```
P(D_H > 45) = P(Z > (45-40)/15) = P(Z > 0.33) ≈ 0.37

Threshold: 500 × 0.37 = $185 < $200 (low fare)
→ Accept the low-fare booking
```

At 35 seats remaining:
```
P(D_H > 35) = P(Z > (35-40)/15) = P(Z > -0.33) ≈ 0.63

Threshold: 500 × 0.63 = $315 > $200 (low fare)
→ Reject the low-fare booking (protect seats for high-fare)
```

The **protection level** for high-fare class is the capacity `y` where:

```
f_L = f_H × P(D_H > y)
→ P(D_H > y) = f_L / f_H = 200/500 = 0.40
→ y = F_H^{-1}(1 - 0.40) = F_H^{-1}(0.60)
→ y = μ + 0.25σ = 40 + 0.25×15 = 43.75 → protect 44 seats
```

**Booking limit** for low fare = `C - y = 100 - 44 = 56 seats`.

---

## EMSR-b (Expected Marginal Seat Revenue — Version b)

Extension to `n` fare classes. The most widely used heuristic in practice.

### Algorithm

For each fare class `i` (from highest to lowest), compute the **protection level** against all higher classes combined:

1. Aggregate all classes above `i` into a single composite demand:
   - Combined mean: `μ_agg = Σ μ_j` for `j > i`
   - Combined variance: `σ²_agg = Σ σ²_j` for `j > i`
   - Approximate as Normal: `D_agg ~ N(μ_agg, σ_agg)`
   - Weighted average fare: `f_agg = (Σ f_j × μ_j) / Σ μ_j` for `j > i`

2. Apply Littlewood's Rule on the aggregate:
   ```
   P(D_agg > y_i) = f_i / f_agg
   y_i = F_agg^{-1}(1 - f_i/f_agg)
   ```

3. Booking limit for class `i`: `BL_i = C - y_{i-1}` (nested)

### Worked Example (3 Classes)

- Capacity: 100
- Class 3 (low): fare=$150, demand~N(50,20)
- Class 2 (mid): fare=$300, demand~N(30,15)
- Class 1 (high): fare=$600, demand~N(20,10)

**Step 1: Protect against class 1 alone (for class 2 booking limit)**

```
f_agg = $600, μ_agg = 20, σ_agg = 10
P(D1 > y2) = 300/600 = 0.50
y2 = F^{-1}(0.50) at N(20,10) = 20 (median = mean for Normal)
```

**Step 2: Protect against classes 1+2 combined (for class 3 booking limit)**

```
μ_agg = 20 + 30 = 50
σ_agg = √(10² + 15²) = √325 ≈ 18.0
f_agg = (600×20 + 300×30) / (20+30) = (12000+9000)/50 = 420

P(D_agg > y3) = 150/420 ≈ 0.357
y3 = F^{-1}(1 - 0.357) = F^{-1}(0.643) at N(50, 18)
   = 50 + 0.368×18 ≈ 56.6 → protect 57 seats
```

**Resulting booking limits (nested):**

| Class | Fare | Protection Level | Booking Limit |
|-------|------|-----------------|---------------|
| 1 (high) | $600 | — | 100 (always open) |
| 2 (mid) | $300 | y₂ = 20 | 100 - 20 = 80 |
| 3 (low) | $150 | y₃ = 57 | 100 - 57 = 43 |

Meaning: accept at most 43 low-fare bookings, 80 mid-or-higher bookings, and all 100 high-fare bookings.

---

## Bid Price Control

An alternative to booking limits. Compute a **bid price** `b` — the opportunity cost of one unit of capacity — and accept any fare request where `f_i ≥ b`.

The bid price equals the shadow price of the capacity constraint in the linear program:

```
maximize   Σ f_i × x_i
subject to Σ x_i ≤ C
           0 ≤ x_i ≤ E[D_i]  for all i
```

At optimality, `b = f_k` where class `k` is the marginal accepted class.

### Dynamic Bid Price (Over the Booking Horizon)

In a multi-period setting, the bid price changes as remaining capacity and time change. Define:

```
V(c, t) = expected revenue from c remaining units with t periods left
b(c, t) = V(c, t) - V(c-1, t)  ← opportunity cost of one unit
```

Accept request with fare `f` if `f ≥ b(c, t)`.

**DP Recursion:**

```
V(c, t) = V(c, t-1) + Σ_i λ_i(t) × max(0, f_i - b(c, t-1))
```

Where `λ_i(t)` is the arrival rate of class `i` at time `t`. This is exact but computationally expensive for large `C` — approximate with LP relaxation or simulation.

---

## Overbooking

Hotels and airlines routinely sell more than capacity because some bookings cancel or no-show. The optimal overbooking level balances:

- **Spoilage cost**: empty seat at departure (lost revenue ≈ `f_avg`)
- **Denied service cost**: bumping a confirmed booking (penalty `d`, reputation damage)

**Optimal authorization level** `C*`:

```
P(show-ups > C) = f_avg / (f_avg + d)
```

This is again Littlewood's Rule applied to the no-show problem.

### Worked Example

- 100 rooms, average rate = $120/night
- Denied service penalty (walk cost + reputation) = $360/booking
- Historical show-up rate: 90% of bookings show up, ~N with σ=8

```
P(show-ups > C*) = 120 / (120 + 360) = 0.25

If bookings_sold = B, show-ups ~ N(0.9B, 8)
P(0.9B + Z×8 > 100) = 0.25
0.9B + 0.674×8 = 100
0.9B = 94.6
B ≈ 105
```

Authorize selling up to **105 bookings** for 100 rooms.

---

## Demand Forecasting for RM

RM model quality is bounded by forecast quality. Two required forecasts:

### 1. Unconstrained Demand (De-truncation)

When you close a booking class early, you only observe demand up to the closing point — not true demand. Naive averaging understates demand.

**EM-based de-truncation (simplified):**

For observations where demand was censored at booking limit `L`:
```
E[D | D ≥ L] = μ + σ × φ((L-μ)/σ) / (1 - Φ((L-μ)/σ))
```
Where `φ` is the Normal PDF and `Φ` is the CDF. Use this to back-estimate true `μ`.

### 2. Booking Pace (Pickup Forecasting)

Forecast total bookings at departure from current bookings-on-hand:

```
Final demand = current bookings + expected pickup
Pickup(t) = historical average pickup in remaining t periods × seasonality factor
```

A simple multiplicative model:
```python
def forecast_final_demand(bookings_on_hand, days_to_departure, pickup_curve):
    """
    pickup_curve: dict {days_before: avg_historical_pickup_from_that_day}
    """
    expected_pickup = pickup_curve.get(days_to_departure, 0)
    return bookings_on_hand + expected_pickup
```

---

## Fare Class Structure Decisions

Before running any RM algorithm, the fare class structure must be defined.

| Structure | Description | When to Use |
|-----------|-------------|-------------|
| **Nested (closed)** | Higher class can sell into lower class capacity | Standard; simpler to implement |
| **Partitioned** | Each class has fixed seat block, no sharing | Rare; wastes capacity |
| **Nested (open)** | Lower class can upgrade to higher class | Hotels with room type upgrades |

**Nested booking** is nearly universal. All EMSR-b calculations assume nested structure.

---

## Competitive RM: When to Deviate from Pure Optimization

Classical RM models ignore competitors. In practice:

**Don't auto-match competitor price drops if:**
1. Your product has verifiable differentiation (location, brand, amenities)
2. The competitor's drop appears temporary or promotional
3. Your occupancy/load is already above 80%

**Do respond to competitor prices when:**
1. Your booking pace is significantly below historical average for this period
2. You have excess inventory with little time remaining
3. The gap exceeds typical customer price sensitivity threshold (usually >15-20%)

The IRON LAW applies here: competitive response should be based on **current** demand signals, not automated price mirroring. A rule like "always match competitors" creates race-to-the-bottom dynamics (see SKILL.md Gotchas).

---

## Reference Implementation: EMSR-b

```python
from scipy import stats

def emsr_b(capacity, fare_classes):
    """
    fare_classes: list of dicts sorted HIGH to LOW fare
      [{"fare": 600, "mean": 20, "std": 10}, ...]
    Returns: booking limits (nested), indexed same as fare_classes
    """
    n = len(fare_classes)
    protection_levels = []

    for i in range(1, n):  # protect against classes 0..i-1
        higher = fare_classes[:i]

        # Aggregate demand for higher classes
        mu_agg = sum(c["mean"] for c in higher)
        var_agg = sum(c["std"]**2 for c in higher)
        sigma_agg = var_agg ** 0.5
        f_agg = sum(c["fare"] * c["mean"] for c in higher) / mu_agg

        # Current class fare
        f_i = fare_classes[i]["fare"]
        ratio = f_i / f_agg

        if ratio >= 1.0:
            # This class fare >= weighted average of higher classes: protect 0
            protection_levels.append(0)
        else:
            # P(D_agg > y) = ratio → y = inverse CDF at (1 - ratio)
            dist = stats.norm(loc=mu_agg, scale=sigma_agg)
            y = dist.ppf(1 - ratio)
            protection_levels.append(max(0, int(y + 0.5)))  # round up

    # Booking limits (nested): BL[i] = capacity - protection_level[i-1]
    booking_limits = [capacity]  # highest class always open
    for y in protection_levels:
        booking_limits.append(max(0, capacity - y))

    return booking_limits


# Example usage:
classes = [
    {"fare": 600, "mean": 20, "std": 10},
    {"fare": 300, "mean": 30, "std": 15},
    {"fare": 150, "mean": 50, "std": 20},
]
limits = emsr_b(100, classes)
# limits[0]=100 (high fare), limits[1]=80 (mid), limits[2]=43 (low)
```

---

## Known Limitations

**EMSR-b limitations:**
- Assumes independent demands across fare classes (correlated demand requires simulation)
- Normal approximation fails for small-demand classes (use Poisson for low-volume)
- Static: computed once, not updated mid-horizon (use re-optimization on each booking)

**Bid price limitations:**
- Single bid price ignores class-specific demand elasticity
- LP relaxation of DP overestimates revenue by ~2-5% in practice

**General RM limitations:**
- All models assume the demand distribution is known. Bootstrap from at least 2 years of historical data per departure day-of-week × season cell.
- Models break under structural demand shifts (COVID, new competitor entry, venue change). Monitor booking pace vs. forecast daily; trigger manual override when divergence exceeds 25%.
