---
name: "biz-dupont"
description: "Apply DuPont Analysis to decompose Return on Equity (ROE) into profitability, efficiency, and leverage components. Use this skill when the user needs to diagnose why ROE is high or low, compare financial performance drivers across companies, or identify which operational lever to pull — even if they say 'why is our ROE declining' or 'how do we improve returns'."
metadata:
  category: "WP-15 商學院—財務"
  tags: ["finance", "dupont", "roe-analysis"]
---

# DuPont Analysis

## Overview

DuPont decomposes ROE into three multiplicative components: Net Profit Margin × Asset Turnover × Equity Multiplier. This reveals whether ROE is driven by profitability, efficiency, or leverage — critical for diagnosis and comparison.

## When to Use

**Trigger conditions:**
- User asks "why is our ROE high/low?"
- User comparing financial performance across companies
- User needs to identify which operational lever improves returns
- User analyzing profitability beyond top-line metrics

**When NOT to use:**
- For company valuation → use DCF
- For comprehensive ratio analysis → use Financial Ratios skill
- For strategic positioning → use SWOT

## Framework

```
IRON LAW: Three-Factor Decomposition

ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
    = (Net Income/Revenue) × (Revenue/Total Assets) × (Total Assets/Equity)

All three factors MUST be calculated and analyzed. Reporting ROE without
decomposition is like reporting a fever without checking symptoms.
```

```
IRON LAW: High Leverage ≠ Good Performance

A high Equity Multiplier (Assets/Equity) inflates ROE through debt.
A company with 5% margin, 1.0x turnover, and 6x leverage has ROE of 30% —
but is one bad quarter away from insolvency. Always flag when leverage
is the dominant driver.
```

### Step 1: Calculate the Three Components

| Component | Formula | What It Measures |
|-----------|---------|-----------------|
| Net Profit Margin | Net Income / Revenue | Profitability — how much of each dollar of revenue becomes profit |
| Asset Turnover | Revenue / Total Assets | Efficiency — how well assets generate revenue |
| Equity Multiplier | Total Assets / Shareholders' Equity | Leverage — how much debt amplifies equity returns |

### Step 2: Diagnose the Driver

Compare each component to industry benchmarks and trends:
- **Margin-driven ROE**: Premium brands, tech companies (high margin, lower turnover)
- **Turnover-driven ROE**: Retail, fast food (low margin, high turnover)
- **Leverage-driven ROE**: Banks, real estate (moderate margin, high leverage) — flag the risk

### Step 3: Trend Analysis

Calculate DuPont components for 3-5 years. Identify:
- Which component is improving/declining?
- Is improving ROE driven by operations (margin, turnover) or financial engineering (leverage)?

### Step 4: Peer Comparison

Compare DuPont components across competitors to identify relative strengths/weaknesses.

## Output Format

> ⚠️ **Decimal vs percent**: The bundled script returns ROE and all margin/burden
> components as **decimals** (`0.2014` means 20.14%, NOT `20.14`). The narrative
> table below renders them as percentages for humans, but JSON outputs and any
> downstream pipeline must use decimals consistently.

```markdown
# DuPont Analysis: {Company}

## ROE Decomposition

| Component | Value | Industry Avg | Trend (3yr) |
|-----------|-------|-------------|-------------|
| Net Profit Margin | X% | X% | ↑/↓/→ |
| Asset Turnover | X.Xx | X.Xx | ↑/↓/→ |
| Equity Multiplier | X.Xx | X.Xx | ↑/↓/→ |
| **ROE** | **X%** | **X%** | ↑/↓/→ |

## Diagnosis
- Primary ROE driver: {margin / turnover / leverage}
- Risk flag: {leverage concern if applicable}

## Peer Comparison
| Company | Margin | Turnover | Leverage | ROE |
|---------|--------|----------|----------|-----|
| {Company} | X% | X.Xx | X.Xx | X% |
| {Peer A} | ... | ... | ... | ... |

## Recommendations
1. {Which lever to improve and how}
```

## Examples

### Correct Application
**Scenario:** DuPont for two Taiwanese retailers

| | Company A | Company B |
|---|---|---|
| Net Profit Margin | 2% | 8% |
| Asset Turnover | 3.5x | 1.2x |
| Equity Multiplier | 2.0x | 2.0x |
| **ROE** | **14%** | **19.2%** |

Diagnosis: Company A is turnover-driven (high-volume, low-margin retail). Company B is margin-driven (premium positioning). Both have similar leverage — ROE difference comes from operations ✓

### Incorrect Application
- ROE is 25% and reported as "excellent" without decomposition. Turns out: Margin 3%, Turnover 1.0x, Leverage 8.3x → Almost entirely leverage-driven, extremely risky. Violates Iron Law: must decompose.

## Gotchas

- **Extended 5-factor DuPont**: For deeper analysis, decompose margin into Tax Burden × Interest Burden × Operating Margin. Useful when comparing across tax jurisdictions.
- **Negative equity breaks the model**: Companies with accumulated losses can have negative equity, making the multiplier meaningless. Note and use alternative metrics.
- **One-time items distort margin**: Use normalized/adjusted net income to avoid single-year spikes from asset sales, write-downs, or legal settlements.
- **Turnover varies wildly by industry**: Asset-light businesses (SaaS) have naturally high turnover. Capital-heavy businesses (manufacturing) have low turnover. Compare within industry only.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/dupont.py` | Decompose ROE into 3-factor or 5-factor DuPont components | `python scripts/dupont.py --help` |

Run `python scripts/dupont.py --verify` to execute built-in sanity tests.

## References

- For 5-factor DuPont extension, see `references/extended-dupont.md`
