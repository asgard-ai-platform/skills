---
name: "grad-mm-theorem"
description: "Apply the Modigliani-Miller theorem to analyze capital structure decisions and identify when financing choices affect firm value. Use this skill when the user needs to evaluate debt-equity tradeoffs, assess the impact of leverage on firm value, understand tax shield benefits, or when they ask 'does capital structure matter', 'should we take on more debt', or 'what is the optimal leverage ratio'."
metadata:
  category: "WP-26 財務理論"
  tags: ["Modigliani-Miller", "capital-structure", "leverage", "tax-shield", "WACC", "tradeoff-theory"]
---

# Modigliani-Miller Theorem

## Overview

The Modigliani-Miller theorem (1958) establishes that in perfect capital markets, firm value is independent of capital structure. This irrelevance result serves as the benchmark — every real-world reason capital structure matters is a violation of MM's assumptions.

## When to Use

- Evaluating whether a financing decision creates or destroys value
- Identifying which market imperfections make capital structure relevant
- Calculating the value of the tax shield from debt
- Teaching or analyzing the logical foundations of capital structure theory

## When NOT to Use

- As a literal prescription — real markets are never frictionless
- When the analysis requires explicit bankruptcy cost modeling (use tradeoff theory)
- For financial institutions where capital structure is regulated

## Assumptions

```
IRON LAW: MM irrelevance holds ONLY in perfect markets — every
real-world deviation (taxes, bankruptcy costs, agency costs) makes
capital structure matter. MM is the null hypothesis, not the answer.
```

Key assumptions (for irrelevance):
1. No taxes (corporate or personal)
2. No bankruptcy costs or financial distress costs
3. No agency costs — managers act in shareholders' interest
4. Symmetric information — insiders and outsiders know the same things
5. Individuals and firms borrow at the same rate

## Methodology

### Step 1 — State MM Propositions

- **Proposition I (no tax):** VL = VU — firm value is independent of leverage
- **Proposition II (no tax):** Re = R0 + (D/E)(R0 - Rd) — cost of equity rises linearly with leverage
- **Proposition I (with tax):** VL = VU + Tc x D — debt creates a tax shield

### Step 2 — Identify Market Imperfections

For each deviation, assess its magnitude:
- Corporate taxes: create incentive for debt (tax shield)
- Bankruptcy costs: create incentive against excessive debt
- Agency costs: debt disciplines managers (Jensen, 1986) but may cause asset substitution
- Information asymmetry: leads to pecking order behavior

### Step 3 — Apply Tradeoff Framework

Optimal capital structure balances marginal tax shield benefit against marginal bankruptcy and agency costs.

### Step 4 — Compute WACC Impact

WACC = (E/V)Re + (D/V)Rd(1-Tc). Optimal structure minimizes WACC.

## Output Format

```markdown
## Capital Structure Analysis: [Firm]

### Current Structure
| Metric | Value |
|--------|-------|
| Debt (D) | $X |
| Equity (E) | $X |
| D/E Ratio | x.xx |
| WACC | x% |

### MM Imperfections Present
| Imperfection | Magnitude | Direction |
|-------------|-----------|-----------|
| Tax shield | [high/medium/low] | Favors debt |
| Bankruptcy costs | [high/medium/low] | Favors equity |
| Agency costs | [high/medium/low] | [depends] |

### Recommendation
- [Optimal direction of adjustment with reasoning]
```

## Gotchas

- MM Proposition II is frequently misunderstood: WACC stays constant (no tax) because cheaper debt is exactly offset by rising equity cost
- Tax shield value Tc x D assumes perpetual debt — temporary debt requires PV calculation
- Personal taxes (Miller, 1977) can offset corporate tax advantage of debt
- Empirical leverage ratios vary wildly by industry, suggesting no single "optimal" structure
- Financial distress costs are hard to measure but can be 10-20% of firm value
- MM assumes operating cash flows are independent of financing — this fails when leverage affects investment decisions

## References

- Modigliani, F. & Miller, M. (1958). The cost of capital, corporation finance and the theory of investment. *American Economic Review*, 48(3), 261-297.
- Modigliani, F. & Miller, M. (1963). Corporate income taxes and the cost of capital: a correction. *American Economic Review*, 53(3), 433-443.
- Jensen, M. (1986). Agency costs of free cash flow. *American Economic Review*, 76(2), 323-329.
