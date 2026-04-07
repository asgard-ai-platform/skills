---
name: "biz-breakeven"
description: "Perform break-even analysis to determine the sales volume or revenue needed to cover all costs. Use this skill when the user needs to calculate break-even point, assess margin of safety, evaluate operating leverage, or decide pricing and volume trade-offs — even if they say 'how many units do we need to sell', 'when will we be profitable', or 'what happens if we lower the price'."
metadata:
  category: "WP-15 商學院—財務"
  tags: ["finance", "breakeven", "cost-analysis"]
---

# Break-Even Analysis

## Overview

Break-even analysis finds the point where total revenue equals total costs — zero profit, zero loss. It separates costs into fixed and variable, then calculates the volume (units or revenue) needed to cover fixed costs through contribution margin.

## Framework

```
IRON LAW: Fixed vs Variable Classification Must Be Rigorous

Fixed costs do NOT change with volume (rent, salaries, insurance).
Variable costs change PROPORTIONALLY with volume (materials, shipping per unit, commissions).

"Salaries" is NOT always fixed — a sales commission is variable.
"Rent" is NOT always fixed — a percentage-rent lease is variable.
Misclassification directly corrupts the break-even calculation.
```

### Core Formulas

```
Contribution Margin per Unit = Selling Price - Variable Cost per Unit
Break-Even Units = Fixed Costs / Contribution Margin per Unit
Break-Even Revenue = Fixed Costs / Contribution Margin Ratio
Contribution Margin Ratio = Contribution Margin per Unit / Selling Price
Margin of Safety = (Actual Sales - Break-Even Sales) / Actual Sales
Degree of Operating Leverage (DOL) = Contribution Margin / Net Income
```

### Step 1: Classify All Costs

Separate every cost line into fixed or variable. For semi-variable costs (e.g., electricity with a base charge + usage), split into fixed and variable portions.

### Step 2: Calculate Break-Even Point

- **Single product**: BEP units = Fixed Costs / CM per unit
- **Multiple products**: Use weighted-average CM based on product mix, then BEP = Fixed / Weighted CM

### Step 3: Assess Margin of Safety

How far above break-even are current sales? Higher margin of safety = more resilience to downturns.

### Step 4: Scenario Analysis

Test: What happens if price drops 10%? If volume drops 20%? If fixed costs increase? Build a scenario table.

## Output Format

```markdown
# Break-Even Analysis: {Product/Business}

## Cost Structure
| Category | Amount | Fixed/Variable |
|----------|--------|---------------|
| {item} | ${X} | F/V |

## Break-Even Calculation
- Fixed Costs: ${X}/period
- Variable Cost per Unit: ${X}
- Selling Price per Unit: ${X}
- Contribution Margin: ${X} ({X%})
- **Break-Even: {N} units / ${X} revenue**
- Margin of Safety: {X%}

## Scenario Analysis
| Scenario | BEP Units | Margin of Safety |
|----------|-----------|-----------------|
| Base case | {N} | {X%} |
| Price -10% | {N} | {X%} |
| Volume -20% | N/A | {X%} |
| Fixed costs +15% | {N} | {X%} |
```

## Examples

### Correct Application
**Scenario:** Break-even for a Taiwanese bubble tea shop
- Fixed costs: NT$150,000/month (rent NT$60K, staff NT$70K, utilities NT$20K)
- Variable cost: NT$25/cup (ingredients NT$15, cup/straw NT$5, packaging NT$5)
- Price: NT$55/cup
- CM = NT$30/cup (54.5%)
- **BEP = 150,000 / 30 = 5,000 cups/month ≈ 167 cups/day** ✓

### Incorrect Application
- Classified staff wages as variable cost → For a shop with fixed staff (not per-cup labor), wages are fixed. This understates BEP. Violates Iron Law.

## Gotchas

- **Step-fixed costs**: Rent is fixed until you need a second location. Staff is fixed until you need another shift. These "step" at certain volume thresholds — model them as fixed within their relevant range.
- **Multi-product businesses**: Most real businesses sell multiple products. Use weighted-average CM or calculate BEP in revenue (not units).
- **Break-even ignores time value**: BEP tells you the volume, not when you'll reach it. A business that breaks even at 10,000 units but takes 3 years to get there may run out of cash.
- **Contribution margin is not gross margin**: Gross margin uses COGS (which may include fixed manufacturing overhead). CM uses only variable costs.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/breakeven.py` | Compute break-even quantity, revenue, and contribution margin | `python scripts/breakeven.py --help` |

Run `python scripts/breakeven.py --verify` to execute built-in sanity tests.

## References

- For multi-product break-even methodology, see `references/multi-product-bep.md`
