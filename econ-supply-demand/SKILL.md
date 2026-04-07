---
name: "econ-supply-demand"
description: "Apply supply and demand analysis to explain price determination, market equilibrium, and the effects of policy interventions. Use this skill when the user needs to analyze how prices are set in a market, predict the effect of taxes/subsidies/price controls, or understand shifts in supply or demand curves — even if they say 'why did the price go up', 'what happens if the government sets a price cap', or 'how does a tariff affect the market'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "supply-demand", "microeconomics"]
---

# Supply and Demand Analysis

## Overview

Supply and demand is the foundational model for price determination in markets. It explains how prices emerge from the interaction of buyers (demand) and sellers (supply), and how external shocks or policy interventions shift the equilibrium.

## Framework

```
IRON LAW: Shift vs Movement Along the Curve

A change in PRICE causes movement ALONG the curve (quantity changes).
A change in OTHER FACTORS (income, costs, preferences, technology) causes
the entire curve to SHIFT.

"Demand increased" means the demand CURVE shifted right (more quantity
at every price), NOT that quantity demanded increased due to a price drop.
Confusing these is the #1 error in supply-demand analysis.
```

```
IRON LAW: Ceteris Paribus — Change One Thing at a Time

When analyzing a shift, hold everything else constant. If both supply
and demand shift simultaneously, the effect on price or quantity (or both)
becomes ambiguous. Analyze each shift separately first, then combine.
```

### Demand Curve Shifters (non-price factors)
- Consumer income (normal goods: ↑income → ↑demand; inferior goods: opposite)
- Prices of related goods (substitutes, complements)
- Consumer preferences and tastes
- Population / number of buyers
- Expectations of future prices

### Supply Curve Shifters (non-price factors)
- Input costs (raw materials, labor, energy)
- Technology improvements
- Number of sellers
- Government policy (taxes, subsidies, regulations)
- Expectations of future prices

### Analysis Steps

1. **Define the market**: What good? What geographic/time scope?
2. **Identify the shock**: What changed? Is it demand-side or supply-side?
3. **Determine shift direction**: Does the curve shift left (decrease) or right (increase)?
4. **Find new equilibrium**: Where do the new curves intersect?
5. **State the result**: What happens to price and quantity?

### Policy Analysis

| Intervention | Effect |
|-------------|--------|
| Price ceiling (below eq.) | Shortage: Qd > Qs, black markets, quality reduction |
| Price floor (above eq.) | Surplus: Qs > Qd, waste, inefficiency |
| Per-unit tax | Supply shifts left by tax amount, price rises (split between buyer and seller based on elasticity) |
| Subsidy | Supply shifts right by subsidy amount, price falls |
| Tariff | Import supply shifts left, domestic price rises |

## Output Format

```markdown
# Supply-Demand Analysis: {Market}

## Market Definition
- Good: ...
- Scope: ...

## Shock Identification
- Event: {what changed}
- Affected curve: Demand / Supply
- Direction: Shift left / right
- Mechanism: {why this shifts the curve}

## Equilibrium Impact
| | Before | After | Change |
|---|--------|-------|--------|
| Price | $X | $X | ↑/↓ |
| Quantity | X units | X units | ↑/↓ |

## Analysis
{Detailed explanation with diagram description}
```

## Examples

### Correct Application
**Scenario:** Effect of a new EV subsidy on Taiwan's electric car market

- **Shock**: Government offers NT$150K subsidy per EV purchase
- **Affected curve**: Demand shifts RIGHT (effectively lowers price for buyers → more quantity demanded at every market price)
- **Result**: Price rises slightly (sellers capture part of subsidy), quantity increases significantly
- Note: Supply curve does not shift — the subsidy goes to buyers, not manufacturers ✓

### Incorrect Application
- "EV prices dropped so demand increased" → This is movement ALONG the demand curve, not a shift. Demand (the curve) didn't increase — quantity demanded increased. Violates Iron Law.
- Analyzed EV subsidy + chip shortage simultaneously without separating → Ambiguous result. Must analyze each shift separately first. Violates ceteris paribus.

## Gotchas

- **Elasticity determines burden**: For taxes/subsidies, the MORE INELASTIC side bears more of the burden. If demand is inelastic (necessities), consumers bear most of a tax increase.
- **Short run vs long run**: Supply is more elastic in the long run (firms can enter/exit, build capacity). Short-run analysis may overestimate price changes.
- **Not all markets fit**: Supply-demand assumes competitive markets. Monopolies, oligopolies, and markets with externalities need different models.
- **"Demand" is not "want"**: Demand requires both willingness AND ability to pay. A billion people wanting iPhones is not demand if they can't afford one.

## References

- For elasticity calculations, see `references/elasticity.md`
- For welfare analysis (consumer/producer surplus), see `references/welfare-analysis.md`
