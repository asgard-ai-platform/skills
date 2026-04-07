---
name: "biz-unit-economics"
description: "Analyze unit economics to evaluate per-unit profitability and business model scalability. Use this skill when the user needs to assess whether each transaction, customer, or product unit is profitable, evaluate startup viability, or optimize contribution margins — even if they say 'does our business model work', 'what's our margin per order', or 'can we scale profitably'."
metadata:
  category: "WP-15 商學院—財務"
  tags: ["finance", "unit-economics", "business-model"]
---

# Unit Economics

## Overview

Unit economics measures profitability at the single-unit level — per customer, per transaction, or per product. If unit economics are negative, scaling makes losses worse, not better. Positive unit economics are the prerequisite for sustainable growth.

## Framework

```
IRON LAW: If Unit Economics Are Negative, Growth = Faster Death

Scaling a business with negative unit economics means losing more money
faster. "We'll make it up in volume" only works if variable costs per unit
decrease with scale (economies of scale). If they don't, more volume = more losses.

Prove unit economics are positive BEFORE investing in growth.
```

### Key Metrics by Business Model

**Subscription/SaaS:**
| Metric | Formula |
|--------|---------|
| CAC | Total acquisition spend / New customers |
| LTV | ARPU × Gross Margin × (1/Churn Rate) |
| LTV:CAC | Must be > 3:1 |
| Payback Period | CAC / (Monthly ARPU × Gross Margin) |
| Net Revenue Retention | (Starting MRR + Expansion - Contraction - Churn) / Starting MRR |

**E-commerce/Marketplace:**
| Metric | Formula |
|--------|---------|
| AOV | Total Revenue / Number of Orders |
| Contribution Margin per Order | AOV - COGS - Shipping - Payment fees - Returns |
| Repeat Rate | Returning customers / Total customers |
| Fully-loaded CAC | Total marketing / New customers |

**On-demand/Delivery:**
| Metric | Formula |
|--------|---------|
| Revenue per Trip | Order value × Take rate |
| Cost per Trip | Driver pay + Support + Insurance + Incentives |
| Contribution per Trip | Revenue - Cost per Trip |
| Orders per Day per Driver | Utilization metric |

### Analysis Steps

1. **Define the unit**: What is one "unit"? (customer, order, trip, seat)
2. **Calculate revenue per unit**: What does each unit generate?
3. **Calculate variable cost per unit**: What does each unit cost?
4. **Calculate contribution margin**: Revenue - Variable cost
5. **Layer fixed costs**: At what volume do you cover fixed costs? (→ break-even)
6. **Assess scalability**: Do unit economics improve or degrade at 10x volume?

## Output Format

```markdown
# Unit Economics: {Business}

## Unit Definition
- Unit: {customer / order / trip}
- Time period: {monthly / per-transaction}

## Per-Unit Economics
| Metric | Value |
|--------|-------|
| Revenue per unit | ${X} |
| Variable cost per unit | ${X} |
| Contribution margin | ${X} ({X%}) |

## Scalability Assessment
| Volume | Unit Revenue | Unit Cost | CM | Notes |
|--------|-------------|-----------|-----|-------|
| Current ({N}) | ${X} | ${X} | {X%} | baseline |
| 3x ({N}) | ${X} | ${X} | {X%} | {economies of scale?} |
| 10x ({N}) | ${X} | ${X} | {X%} | {what changes?} |

## Verdict
{Positive/negative unit economics, scalability assessment, key lever to improve}
```

## Examples

### Correct Application
**Scenario:** Unit economics for a Taiwan food delivery startup
- Revenue per order: NT$350 × 30% take rate = NT$105
- Variable costs: Driver pay NT$65 + Payment fee NT$10 + Support NT$5 = NT$80
- **Contribution margin: NT$25/order (23.8%)** ✓
- At 10x scale: Driver pay drops to NT$55 (better routing), CM improves to NT$35 (33%)
- Verdict: Marginally positive, scale-dependent — needs volume for viability

### Incorrect Application
- "Revenue per customer is NT$500, cost per customer is NT$200, so we make NT$300 per customer" — but excluded customer support (NT$150) and payment processing (NT$50). True margin is NT$100. Must include ALL variable costs per unit.

## Gotchas

- **"We'll achieve economies of scale"**: Maybe. Identify WHICH costs decrease with scale and by how much. Delivery driver pay may not decrease. Server costs for SaaS typically do.
- **Contribution margin ≠ profit**: CM covers variable costs only. You still need enough total CM to cover fixed costs (see Break-Even Analysis).
- **Blended vs cohort**: Blended unit economics across all customers hides that early customers (organic) may be profitable while recent customers (paid acquisition) are not.
- **Negative unit economics can be strategic**: Temporarily, in land-grab markets with network effects (ride-sharing, marketplaces). But the path to positive must be explicit.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/unit_economics.py` | Compute SaaS unit economics (NRR, GRR, LTV, CAC payback, magic number, burn multiple) | `python scripts/unit_economics.py --help` |

Run `python scripts/unit_economics.py --verify` to execute built-in sanity tests.

## References

- For CAC-LTV deep dive, see the biz-cac-ltv skill
- For break-even analysis, see the biz-breakeven skill
