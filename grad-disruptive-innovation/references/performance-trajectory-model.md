# Performance Trajectory Model

Christensen's disruption mechanism hinges on a geometric argument: incumbent performance improves along a trajectory that **eventually exceeds what any customer tier can absorb**. This document formalizes that argument with equations, worked numbers, and a diagnostic procedure.

---

## Core Claim (Geometric Form)

Let:

- `P_inc(t)` = incumbent performance at time `t` (measured on the primary attribute that matters to customers)
- `N_high(t)` = performance needed by the most demanding customer tier
- `N_low(t)` = performance needed by the least demanding (overserved) tier

Christensen's empirical observation is:

```
dP_inc/dt  >  dN_high/dt  >>  dN_low/dt
```

Incumbents improve faster than even high-end needs evolve. Low-end needs evolve slowest of all. This means every performance trajectory eventually crosses above both need lines — first crossing `N_low`, creating the overserved zone where disruption can enter.

**Disruption becomes viable when:**

```
P_inc(t*) ≥ N_low(t*)   AND   P_ent(t*) ≥ N_low(t*)
```

where `P_ent` is the entrant's performance and `t*` is the foothold date.

---

## S-Curve vs. Linear Approximation

Performance often follows an S-curve (logistic), but for disruption analysis a **log-linear approximation** over a 5–15 year window is usually sufficient:

```
P(t) = P₀ · e^(r · t)
```

where:
- `P₀` = baseline performance at `t = 0`
- `r` = annual growth rate of performance (the slope in log-space)

Customer need thresholds also drift upward but at a much slower `r_need`:

```
N(t) = N₀ · e^(r_need · t)
```

Typical empirical values (from Christensen's disk-drive data):

| Trajectory | Annual growth rate |
|---|---|
| Incumbent performance | 35–50% |
| High-end customer needs | 20–30% |
| Low-end customer needs | 5–15% |
| Entrant (disruptive) performance | 15–25% (initially) |

The key ratio to compute is the **overshoot gap**:

```
Gap(t) = P_inc(t) − N_low(t)
```

Once `Gap(t) > 0`, low-end customers are being over-served.

---

## Two-Trajectory Diagram: Construction Procedure

### Step 1: Define the Performance Dimension

Choose **one primary attribute** — the one incumbents compete on. Examples:

| Industry | Primary dimension |
|---|---|
| Hard disk drives | Storage capacity (MB) |
| Steel | Structural grade (yield strength) |
| Airlines | On-time performance + route breadth |
| Accounting software | Feature count / compliance coverage |

Do not composite multiple dimensions yet. Disruption is almost always about entrants winning on a **different** dimension (price, simplicity, accessibility) while being inferior on the incumbent's primary dimension.

### Step 2: Gather Historical Data Points

Collect 5–10 data points for:
1. Incumbent's primary attribute over time
2. What the low-end customer tier actually needed (reveal this from defection patterns, customer interviews, or pricing data)
3. Entrant's primary attribute at entry and at 3–5 year intervals

Plot on a **semi-log scale** (log y-axis, linear x-axis). Parallel straight lines = constant exponential growth rates.

### Step 3: Fit Growth Rates

Using two data points `(t₁, P₁)` and `(t₂, P₂)`:

```
r = ln(P₂ / P₁) / (t₂ − t₁)
```

### Step 4: Project Forward

Extrapolate both the incumbent trajectory and the need threshold. Mark:
- `t_overshoot`: when `P_inc` first exceeds `N_low`
- `t_intersect`: when `P_ent` reaches `N_low` (entrant can satisfy low-end)
- `t_crossover`: when `P_ent` trajectory reaches the **mainstream** need level

The **disruption window** opens at `max(t_overshoot, t_intersect)` and incumbents lose the mainstream around `t_crossover`.

---

## Worked Example: 3.5-inch vs. 5.25-inch Disk Drives (1980s)

This is Christensen's canonical case. Numbers are approximate but directionally accurate.

### Setup

- **Incumbent primary dimension**: storage capacity (MB) in 5.25" drives
- **New entrant**: 3.5" drives (introduced ~1980 for portable computers)

### Historical Data

| Year | 5.25" capacity (MB) | 3.5" capacity (MB) | Desktop need (MB) | Laptop need (MB) |
|---|---|---|---|---|
| 1980 | 10 | 2 | 5 | — (no segment) |
| 1983 | 20 | 5 | 8 | 2 |
| 1986 | 50 | 15 | 12 | 6 |
| 1989 | 150 | 60 | 20 | 15 |
| 1992 | 400 | 200 | 40 | 40 |

### Compute Growth Rates (1980–1989)

**5.25" incumbent:**
```
r_inc = ln(150 / 10) / 9 = ln(15) / 9 ≈ 2.708 / 9 ≈ 0.301 (30% per year)
```

**3.5" entrant:**
```
r_ent = ln(60 / 2) / 9 = ln(30) / 9 ≈ 3.401 / 9 ≈ 0.378 (38% per year)
```

**Desktop customer need:**
```
r_need_desktop = ln(20 / 5) / 9 = ln(4) / 9 ≈ 1.386 / 9 ≈ 0.154 (15% per year)
```

### Overshoot Computation

At 1980, `P_inc(0) = 10`, `N_desktop(0) = 5`. Overshoot gap:

```
Gap(0) = 10 − 5 = 5 MB  (already overserving desktops in 1980)
```

The 5.25" drive was already over-serving the mainstream desktop market at launch of the 3.5". This is why the 3.5"'s inferior 2 MB was sufficient for the new laptop segment.

### Crossover Forecast

When does 3.5" reach desktop-need parity?

```
P_ent(t) = 2 · e^(0.378 · t) = N_desktop(t) = 5 · e^(0.154 · t)

2 · e^(0.378t) = 5 · e^(0.154t)
e^(0.224t) = 2.5
0.224t = ln(2.5) ≈ 0.916
t ≈ 4.1 years from 1980  →  ~1984
```

By 1984 the 3.5" drive had enough capacity to serve desktop mainstream needs. This matches historical record: 3.5" drives dominated desktop sales by the mid-1980s.

---

## Asymmetric Slope Diagnostic

The model produces a simple test for **whether disruption is structurally possible**:

```
Disruption structurally possible  iff  r_inc > r_need_low
```

If incumbents improve slower than even the low-end customer's rising needs, there is no overshoot — incumbents are not over-serving anyone, and a cheaper-but-worse entrant has no foothold.

Conversely, if `r_ent < r_need_mainstream`, the entrant can never reach the mainstream — it stays trapped in the low end. This is a **failed disruption** (common in industries where entrant improvement rates stall).

| Condition | Interpretation |
|---|---|
| `r_inc > r_need_low` AND `r_ent ≥ r_need_mainstream` | Full disruption path exists |
| `r_inc > r_need_low` AND `r_ent < r_need_mainstream` | Entrant footholds but cannot fully displace |
| `r_inc ≤ r_need_low` | No overshoot; disruption from below not viable |
| `r_ent ≥ r_inc` AND entrant starts high | Sustaining competition, NOT disruption |

---

## Multi-Tier Extension

When a market has more than two customer tiers (low / medium / high), extend the model:

```
N_k(t) = N_k0 · e^(r_k · t)    for k = 1, …, K  (ordered low to high)
```

The incumbent over-serves tier `k` starting at:

```
t_k* = ln(N_k0 / P_inc0) / (r_inc − r_k)    [valid when r_inc > r_k]
```

Compute `t_k*` for each tier in sequence. The lowest tier is disrupted first, then successive tiers fall as the entrant's trajectory improves.

**Example with three tiers (hypothetical SaaS accounting software):**

| Tier | `N_k0` (features) | `r_k` (annual) | `t_k*` (years from entry) |
|---|---|---|---|
| SMB (low-end) | 20 | 5% | 1.8 |
| Mid-market | 60 | 12% | 5.2 |
| Enterprise | 200 | 18% | 11.7 |

An entrant with `P_ent0 = 15` features and `r_ent = 30%` per year:
- Can serve SMBs immediately (15 < 20, close enough with price advantage)
- Reaches mid-market in ~4 years
- Reaches enterprise in ~10 years

This gives a **disruption timeline** rather than a binary yes/no assessment.

---

## Common Measurement Errors

**Choosing the wrong performance dimension.** Incumbents compete on what incumbents value. Disruptors often win on a dimension incumbents aren't measuring. If you measure disk drives only on seek time (what IBM measured), you miss that storage density was the disruptive axis for portables.

**Smoothing away the trajectory.** S-curves have inflection points. A trajectory that looks slow in the early stage can accelerate sharply. Use the mid-growth phase rate, not the embryonic rate, for projection.

**Conflating product generation with the trajectory.** The trajectory tracks the best available product at each time point, not an average across installed base. The installed base always lags — disruption acts on what customers can buy now, not what they already own.

**Using revenue as the performance proxy.** Revenue conflates volume × price × mix. Always use a physical or functional attribute (MB, upload speed, error rate) that maps directly to customer utility.

**Assuming linear customer needs.** `N(t)` often has step-function jumps (regulatory changes, platform shifts). Build in explicit scenario branches rather than a single smooth curve when you can identify upcoming threshold events.

---

## Relationship to Asymmetric Motivation

The trajectory model addresses **capability** — whether the entrant *can* eventually satisfy mainstream customers. The separate asymmetric motivation condition addresses **willingness** — whether the incumbent *will* respond.

Both conditions must hold for disruption to succeed:

```
Disruption = Trajectory Convergence (capability) ∧ Asymmetric Motivation (willingness to ignore)
```

A trajectory that converges but where the incumbent responds immediately (IBM PC division in 1981) produces competition, not successful disruption. Always pair the trajectory analysis with the motivation analysis from the parent SKILL.md Step 3.
