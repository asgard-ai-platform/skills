---
name: "algo-risk-altman-z"
description: "Calculate Altman Z-Score to predict corporate bankruptcy probability from financial ratios. Use this skill when the user needs to assess a company's financial distress risk, screen for bankruptcy-prone firms, or evaluate credit worthiness — even if they say 'bankruptcy prediction', 'financial distress score', or 'Z-score analysis'."
metadata:
  category: "WP-40 風險演算法"
  tags: ["risk", "altman-z-score", "bankruptcy", "financial-analysis"]
---

# Altman Z-Score

## Overview

Altman Z-Score is a linear discriminant model predicting bankruptcy probability from five financial ratios. Z = 1.2X₁ + 1.4X₂ + 3.3X₃ + 0.6X₄ + 1.0X₅. Zones: Z > 2.99 (safe), 1.81-2.99 (grey), Z < 1.81 (distress). Originally for public manufacturing firms; variants exist for private and non-manufacturing.

## When to Use

**Trigger conditions:**
- Screening companies for bankruptcy risk
- Quick credit assessment using publicly available financials
- Monitoring portfolio companies for financial distress signals

**When NOT to use:**
- For financial institutions (banks, insurers) — different capital structures
- When detailed credit scoring is needed (use logistic regression credit models)

## Algorithm

```
IRON LAW: Z-Score Was Calibrated for PUBLIC MANUFACTURING Firms
Applying the original formula to private firms, service companies, or
emerging markets WITHOUT using the appropriate variant produces
misleading results. Use Z'-Score for private firms, Z''-Score for
non-manufacturing and emerging markets.
```

### Phase 1: Input Validation
Extract from financial statements: working capital, retained earnings, EBIT, market cap (or book equity for private), total assets, total liabilities, sales.
**Gate:** All five inputs available, from same reporting period.

### Phase 1.5: Variant Selection (MANDATORY)

Before touching any formula, pick the right variant — this is the single most common
mistake when applying Altman Z.

| Firm description | Variant | Script flag |
|------------------|---------|-------------|
| Public **manufacturing** firm | Original Z | `--variant original` |
| **Private** manufacturing firm (no market cap) | Z' | `--variant private` |
| **Non-manufacturing** — SaaS, services, retail, tech, finance-light | Z'' | `--variant non_manufacturing` |
| Emerging-market firm of any kind | Z'' | `--variant non_manufacturing` |

**If the user description contains any of these tags**: "SaaS", "cloud", "software",
"services", "retail", "e-commerce", "platform", "tech", "emerging market", "BRICS",
"non-manufacturing" → **use Z''**. Do not default to the original Z just because
that's the "classic" formula.

Full formulas and zone thresholds for each variant live in
[`references/z-score-variants.md`](references/z-score-variants.md). Coefficients,
X₄ definition (market cap vs book equity), and the X₅ treatment all differ between
variants — they are not small tweaks to the original.

### Phase 2: Core Algorithm
1. X₁ = Working Capital / Total Assets (liquidity)
2. X₂ = Retained Earnings / Total Assets (cumulative profitability)
3. X₃ = EBIT / Total Assets (operating efficiency)
4. X₄ = Market Value of Equity / Total Liabilities (leverage)
5. X₅ = Sales / Total Assets (asset turnover)
6. Z = 1.2X₁ + 1.4X₂ + 3.3X₃ + 0.6X₄ + 1.0X₅

### Phase 3: Verification
Check: all ratios in plausible ranges. Compare Z-score against industry peers and historical trend.
**Gate:** Z-score computed, zone classification assigned.

### Phase 4: Output
Return Z-score with component breakdown and zone classification.

## Output Format

```json
{
  "z_score": 2.45,
  "zone": "grey",
  "components": {"X1": 0.12, "X2": 0.25, "X3": 0.08, "X4": 1.5, "X5": 0.9},
  "metadata": {"model": "original", "company": "...", "period": "2024-Q4"}
}
```

## Examples

### Sample I/O
**Input:** WC=200M, RE=500M, EBIT=150M, MktCap=2B, TL=1B, TA=3B, Sales=2.5B
**Expected:** X1=0.067, X2=0.167, X3=0.05, X4=2.0, X5=0.833. Z=1.2(0.067)+1.4(0.167)+3.3(0.05)+0.6(2.0)+1.0(0.833)=2.53 → Grey zone.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| Negative retained earnings | Low X₂, likely distress | Accumulated losses are a strong distress signal |
| Startup with no revenue | X₅ near zero | Z-score not designed for pre-revenue companies |
| Asset-light tech firm | Misleading X₅ | High revenue/low assets inflates turnover |

## Gotchas

- **Model age**: Calibrated in 1968 on 1946-1965 data. Business models, accounting standards, and capital structures have changed. Use as one signal, not sole determinant.
- **Accounting manipulation**: Z-score uses reported financials. Creative accounting (off-balance-sheet debt, revenue recognition games) can mask distress.
- **Industry differences**: Capital-intensive industries naturally have lower asset turnover (X₅). Compare within industry, not across.
- **Trend matters more than level**: A company moving from Z=3.5 to Z=2.1 over two years is concerning even though 2.1 is still in the grey zone.
- **Private firm variant** (Z'): replaces X₄ with Book Equity / Total Liabilities and re-weights: `Z' = 0.717X₁ + 0.847X₂ + 3.107X₃ + 0.420X₄ + 0.998X₅`. Zone thresholds shift to 2.9 / 1.23.
- **Non-manufacturing variant** (Z''): **drops X₅ entirely** and re-estimates the rest: `Z'' = 6.56X₁ + 3.26X₂ + 6.72X₃ + 1.05X₄`. Zone thresholds shift to 2.6 / 1.1. Using original Z on a SaaS / services firm inflates the score via X₅ and can mis-zone a distressed firm as safe.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/altman_z.py` | Compute Altman Z-Score and classify zone | `python scripts/altman_z.py --help` |

Run `python scripts/altman_z.py --verify` to execute built-in sanity tests.

## References

- [`references/z-score-variants.md`](references/z-score-variants.md) — Z / Z' / Z'' full
  formulas, zone thresholds, variant-selection rules, and a worked tech-firm example.
