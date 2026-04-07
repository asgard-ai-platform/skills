---
name: "grad-real-options"
description: "Apply real options analysis to value managerial flexibility embedded in investment decisions. Use this skill when the user needs to evaluate projects with significant uncertainty and flexibility, assess the value of deferring or expanding investments, compare traditional NPV with expanded NPV, or when they ask 'should we wait to invest', 'what is the option to abandon worth', or 'why does NPV undervalue this project'."
metadata:
  category: "WP-26 財務理論"
  tags: ["real-options", "NPV", "managerial-flexibility", "option-to-defer", "investment-decision", "uncertainty"]
---

# Real Options

## Overview

Real options theory applies financial option pricing logic to corporate investment decisions. It recognizes that managers can adapt their decisions as uncertainty resolves — deferring, expanding, contracting, or abandoning projects. Traditional NPV, which assumes a now-or-never commitment, systematically undervalues projects with significant flexibility.

## When to Use

- Evaluating investments with high uncertainty and managerial flexibility
- Comparing staged vs. committed investment strategies
- Valuing natural resource extraction, R&D, or platform investments
- When NPV is near zero but the project has strategic optionality

## When NOT to Use

- For routine, low-uncertainty investments where NPV suffices
- When flexibility is contractually or practically absent
- If the option exercise conditions are unclear or unquantifiable

## Assumptions

```
IRON LAW: Traditional NPV undervalues projects with significant
managerial flexibility. Expanded NPV = Static NPV + Option Value.
Ignoring optionality leads to systematic underinvestment in
high-uncertainty, high-flexibility projects.
```

Key assumptions:
1. Managers can and will exercise flexibility optimally
2. Underlying asset value follows a stochastic process
3. Option exercise is feasible (legal, organizational, technical)
4. Market exists (or proxy exists) to estimate volatility

## Methodology

### Step 1 — Identify Embedded Options

| Option Type | Description | Example |
|-------------|-------------|---------|
| Defer | Wait for better information | Land development |
| Expand | Scale up if successful | Platform investment |
| Contract | Scale down if conditions worsen | Modular production |
| Abandon | Exit and recover salvage value | R&D project |
| Switch | Change inputs or outputs | Flex-fuel plant |

### Step 2 — Map to Option Parameters

- Underlying asset value (S): PV of project cash flows
- Exercise price (K): investment cost or salvage value
- Time to expiration (T): decision window
- Volatility (sigma): uncertainty in project value
- Risk-free rate (r): discount rate for option pricing

### Step 3 — Value the Option

Use binomial lattice or Black-Scholes analog. See `references/` for mathematical formulations.

### Step 4 — Compute Expanded NPV

Expanded NPV = Static NPV + Option Value. If expanded NPV is positive, the project merits investment or preservation of the option.

## Output Format

```markdown
## Real Options Analysis: [Project]

### Static NPV
- NPV = $X (using traditional DCF)

### Embedded Options Identified
| Option | Type | Value Driver |
|--------|------|-------------|
| [name] | [defer/expand/abandon/...] | [key uncertainty] |

### Option Valuation
| Parameter | Value |
|-----------|-------|
| Underlying (S) | $X |
| Exercise price (K) | $X |
| Volatility | x% |
| Time (T) | X years |
| Option value | $X |

### Expanded NPV
- Static NPV + Option Value = $X
- Decision: [invest / defer / preserve option]
```

## Gotchas

- Volatility estimation for real assets is far harder than for traded securities
- Assumes optimal exercise — behavioral biases may cause premature or delayed exercise
- Option interactions matter: exercising one option may kill another (e.g., expand kills abandon)
- Real options can justify procrastination disguised as "preserving flexibility"
- Black-Scholes assumptions (continuous trading, log-normal returns) rarely hold for real assets
- Organizational capability to actually exercise options is often overestimated

## References

- Dixit, A. & Pindyck, R. (1994). *Investment Under Uncertainty*. Princeton University Press.
- Trigeorgis, L. (1996). *Real Options: Managerial Flexibility and Strategy*. MIT Press.
- Myers, S. (1977). Determinants of corporate borrowing. *Journal of Financial Economics*, 5(2), 147-175.
