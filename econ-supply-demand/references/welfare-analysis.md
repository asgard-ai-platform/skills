# Welfare Analysis: Consumer Surplus, Producer Surplus, and Deadweight Loss

Welfare analysis quantifies **who gains, who loses, and by how much** when a market moves from one equilibrium to another. It translates curve shifts into dollar amounts.

---

## Core Concepts

### Consumer Surplus (CS)

The difference between what consumers are **willing to pay** (their reservation price) and what they **actually pay**.

```
CS = Area of triangle above market price, below demand curve
   = ½ × Qd × (Pmax - P*)
```

Where:
- `Qd` = equilibrium quantity
- `Pmax` = price at which quantity demanded = 0 (y-intercept of demand curve)
- `P*` = market price

### Producer Surplus (PS)

The difference between what producers **receive** and their **minimum acceptable price** (their cost).

```
PS = Area of triangle below market price, above supply curve
   = ½ × Qs × (P* - Pmin)
```

Where:
- `Pmin` = price at which quantity supplied = 0 (y-intercept of supply curve)

### Total Welfare (Social Surplus)

```
W = CS + PS
```

This is the total net benefit society extracts from the market. **Competitive equilibrium maximizes W** — this is the First Welfare Theorem.

### Deadweight Loss (DWL)

The reduction in total welfare caused by a market distortion (tax, price control, monopoly).

```
DWL = W_competitive - W_actual
    = ½ × |ΔQ| × |ΔP|    [for linear supply/demand with simple interventions]
```

DWL represents transactions that would have created mutual gains but did not occur.

---

## Worked Example: Baseline Market

**Setup:**
- Demand: `P = 100 - 2Q` (so Pmax = 100)
- Supply: `P = 10 + 3Q` (so Pmin = 10)

**Step 1 — Find equilibrium:**
```
100 - 2Q = 10 + 3Q
90 = 5Q
Q* = 18
P* = 100 - 2(18) = 64
```

**Step 2 — Calculate CS:**
```
CS = ½ × Q* × (Pmax - P*)
   = ½ × 18 × (100 - 64)
   = ½ × 18 × 36
   = 324
```

**Step 3 — Calculate PS:**
```
PS = ½ × Q* × (P* - Pmin)
   = ½ × 18 × (64 - 10)
   = ½ × 18 × 54
   = 486
```

**Step 4 — Total welfare:**
```
W = CS + PS = 324 + 486 = 810
```

---

## Policy Interventions

### Per-Unit Tax

A per-unit tax of `t` drives a **wedge** between the price buyers pay (`Pb`) and the price sellers receive (`Ps`):

```
Pb - Ps = t
```

**Finding the new equilibrium with tax:**
1. Set demand = supply + tax: `Pd(Q) = Ps(Q) + t`
2. Solve for `Q_tax`
3. `Pb = Pd(Q_tax)`, `Ps = Pb - t`

**Welfare decomposition after tax:**

| Component | Formula |
|-----------|---------|
| CS (new) | ½ × Q_tax × (Pmax - Pb) |
| PS (new) | ½ × Q_tax × (Ps - Pmin) |
| Tax Revenue | t × Q_tax |
| DWL | ½ × t × (Q* - Q_tax) |
| Total W | CS + PS + Tax Revenue |

Note: Tax revenue is **not lost to society** — it's a transfer to government. Only the DWL triangle is the true social loss.

**Continuing the example with t = 10:**
```
Demand: P = 100 - 2Q
Supply (seller receives): Ps = 10 + 3Q
Buyer pays: Pb = Ps + 10 = 20 + 3Q

Set Pb = demand:
100 - 2Q = 20 + 3Q
80 = 5Q
Q_tax = 16

Pb = 100 - 2(16) = 68
Ps = 68 - 10 = 58

CS = ½ × 16 × (100 - 68) = ½ × 16 × 32 = 256
PS = ½ × 16 × (58 - 10) = ½ × 16 × 48 = 384
Tax Revenue = 10 × 16 = 160
DWL = ½ × 10 × (18 - 16) = 10

Check: 256 + 384 + 160 + 10 = 810 ✓ (equals original W)
```

### Tax Burden Sharing (Elasticity Rule)

The Iron Law from the parent skill applies here with precision:

```
Buyer's share of tax burden  = ΔPb - 0 = Pb - P*
Seller's share of tax burden = P* - Ps

Buyer's burden / Seller's burden = εs / εd
```

Where `εs` = price elasticity of supply, `εd` = |price elasticity of demand|.

**The more inelastic side bears the larger burden.** With perfectly inelastic demand (`εd = 0`), buyers bear 100% of the tax.

In the example:
```
Buyer's burden = 68 - 64 = 4
Seller's burden = 64 - 58 = 6
Total = 10 (the tax) ✓

εd at eq: dQ/dP × P/Q = (-1/2) × (64/18) ≈ -1.78, so |εd| = 1.78
εs at eq: dQ/dP × P/Q = (1/3) × (64/18) ≈ 1.19

Seller bears more because supply is less elastic here (1.19 < 1.78)
```

### Price Ceiling (Pmax < P*)

A price ceiling set **below** equilibrium creates a shortage. Welfare changes:

```
Q_ceiling = Qs(Pmax)   ← supply constrains the market, not demand

CS = uncertain (some consumers gain lower price, others can't buy)
PS = ½ × Q_ceiling × (Pmax - Pmin)  [strictly less than before]
DWL = ½ × (Q* - Q_ceiling) × (Pd(Q_ceiling) - Pmax)
```

The CS effect is ambiguous: consumers who buy gain (lower price), but some consumers who would have bought at P* are now rationed out.

**Continuing example with Pmax = 50:**
```
Qs = solve 50 = 10 + 3Q → Q_ceiling = 40/3 ≈ 13.3

DWL = ½ × (18 - 13.3) × (Pd(13.3) - 50)
Pd(13.3) = 100 - 2(13.3) = 73.4
DWL = ½ × 4.7 × 23.4 ≈ 54.99 ≈ 55
```

### Price Floor (Pmin > P*)

A price floor set **above** equilibrium creates a surplus. Welfare changes:

```
Q_floor = Qd(Pmin)   ← demand constrains the market

PS = uncertain (sellers with cost < Pmin gain, others can't sell)
CS = ½ × Q_floor × (Pmax - Pmin)  [strictly less than before]
DWL = ½ × (Q* - Q_floor) × (Pmin - Ps(Q_floor))
```

### Subsidy

A per-unit subsidy `s` has mirror-image math to a tax: buyers pay less, sellers receive more, quantity exceeds competitive equilibrium.

```
Ps - Pb = s     (sellers receive s more than buyers pay)
Q_sub > Q*      (overproduction relative to optimum)
DWL = ½ × s × (Q_sub - Q*)
```

The subsidy DWL comes from **over-provision** — units produced where social cost exceeds social benefit.

---

## Decision Framework: Which Welfare Effect Matters?

| Question | What to calculate |
|---------|-------------------|
| "Who bears the tax?" | Buyer vs seller burden split using elasticity ratio |
| "How much revenue does government collect?" | `t × Q_tax` |
| "What is the efficiency loss?" | DWL = ½ × t × ΔQ |
| "Are consumers better off with the policy?" | Compare new CS to old CS |
| "Is the policy worth it?" | Compare tax revenue (or policy benefit) to DWL |
| "Does the subsidy help consumers?" | Compare new CS to old CS; also check if producers capture most of the subsidy |

---

## Elasticity and DWL: Key Relationships

```
DWL ∝ (εd × εs) / (εd + εs) × t² / P*
```

This means:
- **More elastic curves → larger DWL** for same tax. Elastic markets have more transactions that "move away" from the wedge.
- **Ramsey Rule** (optimal taxation): tax goods with **inelastic demand** to minimize DWL per dollar of revenue collected. This is why governments tax cigarettes and alcohol heavily.
- **DWL grows with the square of the tax rate**: doubling the tax quadruples the DWL (assuming linear curves). This makes high tax rates particularly costly.

---

## Common Errors in Welfare Analysis

1. **Counting tax revenue as a loss**: Tax revenue is a transfer (CS/PS → government), not a social loss. Only the DWL is lost.

2. **Forgetting the rationing problem with price ceilings**: A price ceiling does not guarantee consumers buy at the controlled price — quantity is constrained by supply. CS calculation must use `Q_ceiling`, not `Qd(Pmax)`.

3. **Applying linear formulas to non-linear curves**: `DWL = ½ × t × ΔQ` only holds for linear supply and demand. For curved functions, integrate.

4. **Ignoring distributional effects**: Total surplus may stay the same while CS and PS redistribute dramatically. A policy with zero DWL can still be highly inequitable.

5. **Conflating DWL with deadweight cost of taxes in public finance**: The Harberger triangle (DWL) measures allocative inefficiency; it does not capture administrative costs, compliance costs, or incidence on factor markets.

---

## Quick Reference: Welfare Effects Table

| Intervention | CS | PS | Gov Revenue | DWL |
|-------------|----|----|-------------|-----|
| Tax | ↓ | ↓ | ↑ | ↑ |
| Subsidy | ↑ | ↑ | ↓ (cost) | ↑ |
| Price ceiling (binding) | Ambiguous | ↓ | 0 | ↑ |
| Price floor (binding) | ↓ | Ambiguous | 0 | ↑ |
| Competitive eq. | Max | Max | 0 | 0 |

All binding interventions create DWL. The size depends on elasticities and the magnitude of the wedge.
