---
name: "biz-dcf"
description: "Build Discounted Cash Flow (DCF) valuation models to estimate intrinsic value. Use this skill when the user needs to value a company, evaluate an investment, estimate fair share price, or build financial projections — even if they say 'what is this company worth', 'should we acquire them', or 'build me a valuation model'."
metadata:
  category: "WP-15 商學院—財務"
  tags: ["finance", "dcf", "valuation"]
---

# Discounted Cash Flow (DCF) Valuation

## Overview

DCF estimates a company's intrinsic value by projecting future free cash flows and discounting them to present value using WACC. It answers "what is this business worth based on its future cash generation ability?"

## When to Use

**Trigger conditions:**
- User needs to value a company or business unit
- User evaluating M&A targets or investment opportunities
- User asks "what's the fair price?" or "build a valuation model"

**When NOT to use:**
- For early-stage startups with no revenue → use comparables or venture method
- For quick relative valuation → use multiples (P/E, EV/EBITDA)
- For portfolio-level decisions → use BCG Matrix

## Framework

```
IRON LAW: Garbage In, Garbage Out

DCF output is ONLY as good as its assumptions. Every assumption (growth rate,
margin, WACC, terminal growth) must be explicitly stated with justification.
A DCF without an assumptions table is worthless.
```

```
IRON LAW: Terminal Value Dominates — Handle with Care

Terminal value typically represents 60-80% of total DCF value. If your
terminal growth rate exceeds long-term GDP growth (~2-3%), you're implying
the company will eventually become larger than the economy. Cap terminal
growth at the risk-free rate or GDP growth.
```

### Step 1: Project Free Cash Flows (5-10 years)

```
FCF = EBIT × (1 - Tax Rate) + Depreciation - CapEx - ΔWorking Capital
```

Build projections from:
- Revenue growth assumptions (top-down or bottom-up)
- Operating margin trajectory
- Capital expenditure requirements
- Working capital changes

### Step 2: Calculate WACC

```
WACC = (E/V × Re) + (D/V × Rd × (1 - Tax))
```

Where:
- Re = Cost of equity (use CAPM: Rf + β × Market Risk Premium)
- Rd = Cost of debt (interest rate on borrowings)
- E/V = Equity weight, D/V = Debt weight

### Step 3: Calculate Terminal Value

**Gordon Growth Model (preferred):**
```
TV = FCF_final × (1 + g) / (WACC - g)
```
Where g = terminal growth rate (cap at 2-3%)

**Exit Multiple Method (alternative):**
```
TV = EBITDA_final × EV/EBITDA multiple
```

### Step 4: Discount to Present Value

```
Enterprise Value = Σ FCFt / (1 + WACC)^t + TV / (1 + WACC)^n
Equity Value = Enterprise Value - Net Debt
Per Share Value = Equity Value / Shares Outstanding
```

### Step 5: Sensitivity Analysis

Test key assumptions: WACC (±1%), terminal growth (±0.5%), revenue growth (±2%). Present as a sensitivity table.

## Output Format

```markdown
# DCF Valuation: {Company}

## Key Assumptions
| Assumption | Value | Justification |
|-----------|-------|---------------|
| Revenue growth (Y1-5) | X% | {basis} |
| Operating margin (terminal) | X% | {basis} |
| WACC | X% | {calculation} |
| Terminal growth | X% | {basis} |

## Projected Free Cash Flows
| Year | Revenue | EBIT | FCF |
|------|---------|------|-----|
| Y1 | ... | ... | ... |

## Valuation Summary
- PV of FCFs: $X
- PV of Terminal Value: $X (X% of total)
- Enterprise Value: $X
- Less: Net Debt: $X
- Equity Value: $X
- Per Share: $X

## Sensitivity Table
| WACC \ Terminal g | 1.5% | 2.0% | 2.5% |
|-------------------|------|------|------|
| 8% | $X | $X | $X |
| 9% | $X | $X | $X |
| 10% | $X | $X | $X |
```

## Examples

### Correct Application
**Scenario:** DCF for a Taiwanese SaaS company (ARR NT$500M, growing 25%)
- Projected 5 years of FCF with declining growth (25% → 15%)
- WACC 10.5% (justified: Rf 1.5%, β 1.2, ERP 6%, debt cost 4%)
- Terminal growth 2.5% (Taiwan GDP growth proxy)
- TV = 72% of enterprise value — within normal range ✓
- Sensitivity table shows $X range across ±1% WACC

### Incorrect Application
- Terminal growth rate of 8% → Implies the company outgrows the economy forever. Violates Iron Law.
- No assumptions table — just "Enterprise Value = NT$2.5B" → No way to validate. Violates Iron Law.

## Gotchas

- **Terminal value sensitivity**: Small changes in terminal growth or WACC swing valuation 20-30%. Always present a range, not a point estimate.
- **Circular reference in WACC**: WACC needs equity value (market cap), but DCF calculates equity value. Iterate or use target capital structure.
- **FCF vs Net Income**: DCF uses Free Cash Flow, not earnings. Companies with high capex or working capital needs can have positive earnings but negative FCF.
- **Country risk premium**: For Taiwan/emerging market companies, add a country risk premium to WACC (typically 1-3%).
- **Negative FCF in early years**: Growth companies may have negative FCF initially. This is fine — the value comes from later years and terminal value.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/dcf.py` | Compute DCF enterprise value with terminal value | `python scripts/dcf.py --help` |

Run `python scripts/dcf.py --verify` to execute built-in sanity tests.

## References

- For WACC calculation details, see `references/wacc-calculation.md`
- For comparable company multiples approach, see `references/comparables.md`
