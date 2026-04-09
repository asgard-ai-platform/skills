# Elasticity

Elasticity measures how responsive quantity is to a change in price (or income, or a related good's price). The core use in supply-demand analysis is **tax/subsidy incidence**: who actually pays a tax or receives a subsidy depends on the relative elasticities of the two curves, not on who the government nominally charges.

---

## Price Elasticity of Demand (PED)

### Formula

```
PED = % change in quantity demanded / % change in price
    = (ΔQd / Qd) / (ΔP / P)
    = (ΔQd / ΔP) × (P / Qd)
```

PED is almost always **negative** (price ↑ → quantity ↓). Convention: report the **absolute value** |PED| unless sign matters for interpretation.

### Midpoint Formula (preferred for finite changes)

```
PED = [(Q2 - Q1) / ((Q2 + Q1) / 2)] / [(P2 - P1) / ((P2 + P1) / 2)]
```

Use midpoint to avoid getting different answers depending on which point you label "before" vs. "after".

### Classification

| |PED| | Label | Meaning |
|----------|-------|---------|
| = 0 | Perfectly inelastic | Quantity does not respond at all |
| 0 < \|PED\| < 1 | Inelastic | Quantity changes less than proportionally |
| = 1 | Unit elastic | Quantity changes proportionally |
| \|PED\| > 1 | Elastic | Quantity changes more than proportionally |
| → ∞ | Perfectly elastic | Any price increase drives quantity to zero |

### Worked Example — PED Calculation

Taiwan's convenience store coffee: price rises from NT$35 to NT$45, and weekly sales drop from 10,000 cups to 8,500 cups.

```
Midpoint PED:
  ΔQ = 8500 - 10000 = -1500
  Q_avg = (10000 + 8500) / 2 = 9250
  %ΔQ = -1500 / 9250 = -16.2%

  ΔP = 45 - 35 = 10
  P_avg = (35 + 45) / 2 = 40
  %ΔP = 10 / 40 = 25%

  PED = -16.2% / 25% = -0.65
  |PED| = 0.65 → Inelastic
```

**Interpretation**: A 10% price increase causes only a 6.5% drop in quantity. Consumers are not very sensitive — convenience coffee is habitual, substitutes are inconvenient.

---

## Price Elasticity of Supply (PES)

```
PES = % change in quantity supplied / % change in price
    = (ΔQs / Qs) / (ΔP / P)
```

PES is **positive** (price ↑ → quantity supplied ↑).

### Classification mirrors PED

| PES | Label |
|-----|-------|
| = 0 | Perfectly inelastic (fixed supply, e.g., land) |
| 0 < PES < 1 | Inelastic |
| = 1 | Unit elastic |
| PES > 1 | Elastic |
| → ∞ | Perfectly elastic |

### Time Horizon Effect on PES

Supply elasticity **increases** over time. Firms need time to adjust capacity, hire workers, build factories:

| Time Horizon | PES Typical Range | Reason |
|-------------|------------------|--------|
| Very short run | ≈ 0 | Output fixed, inventory depletes |
| Short run | 0.2 – 0.8 | Existing plants run overtime |
| Long run | 1.0 – 5.0+ | Entry/exit, new capital |

**Implication for analysis**: A supply shock (e.g., crop failure, chip shortage) causes a larger price spike in the short run than in the long run, because short-run supply is less elastic. Do not apply long-run elasticities to short-run questions.

---

## Tax Incidence: Who Actually Pays?

This is the primary reason to compute elasticities in the context of this skill.

### The Rule

> The **more inelastic** side of the market bears **more** of the tax burden, regardless of whether the government collects from buyers or sellers.

### Formal Split

For a per-unit tax **t**, the buyer's price rises by:

```
ΔP_buyer = t × [PES / (PES + |PED|)]
```

The seller's net price falls by:

```
ΔP_seller = t × [|PED| / (PES + |PED|)]
```

**Check**: ΔP_buyer + ΔP_seller = t ✓

### Worked Example — Tax Incidence

Government imposes a NT$10 per-pack cigarette tax.
- Estimated |PED| for cigarettes = 0.4 (inelastic — addictive good)
- Estimated PES for cigarettes = 1.6 (elastic — tobacco farming can expand)

```
ΔP_buyer = 10 × [1.6 / (1.6 + 0.4)] = 10 × 0.8 = NT$8
ΔP_seller = 10 × [0.4 / (1.6 + 0.4)] = 10 × 0.2 = NT$2
```

Consumers pay NT$8 of the NT$10 tax; producers pay only NT$2. The demand side is more inelastic, so it bears more of the burden.

### Visual Rule of Thumb

```
             Demand Inelastic    Demand Elastic
Supply          Consumers          Split ~50/50
Elastic         bear most          (lean consumers)

Supply          Split ~50/50       Producers
Inelastic       (lean producers)   bear most
```

### Subsidy Incidence (same logic, reversed direction)

For a per-unit subsidy **s**:

```
Benefit to buyer  = s × [PES / (PES + |PED|)]
Benefit to seller = s × [|PED| / (PES + |PED|)]
```

The **more inelastic** side captures **more** of the subsidy. Pharmaceutical subsidies on drugs with inelastic demand tend to be captured partly by manufacturers (they raise pre-subsidy prices), not passed fully to patients.

---

## Cross-Price Elasticity (XED)

```
XED_{AB} = % change in Qd of good A / % change in price of good B
```

| XED Sign | Relationship |
|----------|-------------|
| Positive | Substitutes (A and B compete) |
| Negative | Complements (A and B are used together) |
| ≈ 0 | Unrelated goods |

**Practical use in demand-shift analysis**: If XED between coffee and tea is +0.3 and tea prices rise 20%, expect coffee demand to increase by ~6%. This gives you a quantified demand shift rather than just a directional arrow.

---

## Income Elasticity (YED)

```
YED = % change in Qd / % change in consumer income
```

| YED | Good Type | Example |
|-----|-----------|---------|
| > 1 | Luxury | International travel, designer goods |
| 0 to 1 | Normal necessity | Groceries, basic clothing |
| < 0 | Inferior | Instant noodles, second-hand goods |

**Use case**: When analyzing a demand shift caused by rising incomes, YED tells you whether demand increases or decreases and by how much. Taiwan's rising disposable income predicts increased demand for luxury goods (YED > 1) but potentially decreased demand for cheap substitutes (YED < 0).

---

## Determinants of Elasticity Magnitude

When you don't have a measured elasticity, use these to estimate relative elasticity:

### For Demand

| Factor | More Elastic | Less Elastic |
|--------|-------------|-------------|
| Substitutes available | Many, close substitutes | Few or no substitutes |
| Necessity vs. luxury | Luxury | Necessity (food, medicine) |
| Share of income | Large share | Small share (e.g., salt) |
| Time horizon | Long run | Short run |
| Definition breadth | Narrow (specific brand) | Broad (food in general) |

### For Supply

| Factor | More Elastic | Less Elastic |
|--------|-------------|-------------|
| Time horizon | Long run | Short run |
| Input availability | Inputs abundant | Inputs scarce/fixed |
| Production complexity | Simple assembly | Complex/specialized |
| Inventory storability | Storable goods | Perishables |
| Factor mobility | Mobile (can retool factories) | Immobile (specialized assets) |

---

## Quick-Reference Decision Framework: Tax Burden

```
Step 1: Classify demand
  - Necessity, addictive, or no close substitutes? → Inelastic (|PED| < 1)
  - Luxury, many substitutes, large budget share? → Elastic (|PED| > 1)

Step 2: Classify supply
  - Fixed resource (land, spectrum licenses)? → Inelastic (PES < 1)
  - Competitive industry with easy entry? → Elastic (PES > 1)

Step 3: Apply rule
  - Both inelastic? → Use formula; both sides share burden
  - Demand more inelastic than supply? → Consumers bear majority
  - Supply more inelastic than demand? → Producers bear majority
  - Perfectly elastic supply (common competitive assumption)? → Consumers
    bear 100% of tax (price rises by full tax amount)
```

### Special Case: Perfectly Elastic Supply

In a **competitive market with free entry**, long-run supply is often treated as perfectly elastic (PES → ∞). Then:

```
ΔP_buyer = t × [∞ / (∞ + |PED|)] → t × 1 = t
```

Consumers bear the entire tax. This is why economists often say "business taxes are passed to consumers" in competitive markets — it assumes highly elastic long-run supply.

---

## Common Errors to Avoid

**Confusing elasticity with slope**: Slope is ΔP/ΔQ (units-dependent). Elasticity is unit-free percentage change. A linear demand curve has constant slope but **changing elasticity** along its length (upper half elastic, lower half inelastic, midpoint unit elastic).

**Using point estimates for large changes**: The standard formula gives different answers depending on your base point. Use the **midpoint formula** for any finite price change.

**Applying short-run elasticities to long-run questions**: If a question asks "what happens to the market over the next five years," supply is significantly more elastic than estimates based on monthly price data.

**Assuming symmetry**: |PED| for a price increase ≠ |PED| for a price decrease of the same magnitude, especially for durable goods (consumers can delay purchases when prices rise, but not indefinitely).

**Ignoring that subsidies also shift demand**: The SKILL.md example — EV subsidy to buyers — shifts the **demand curve** right. When computing incidence, use the demand elasticity at the original equilibrium, not the new one.
