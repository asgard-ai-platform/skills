---
name: "econ-business-cycle"
description: "Analyze business cycle phases (expansion, peak, contraction, trough) and their implications for business strategy and policy response. Use this skill when the user needs to identify the current economic phase, anticipate cyclical turning points, or adapt business strategy to macroeconomic cycles — even if they say 'are we heading into a recession', 'how should we prepare for a downturn', or 'when will the economy recover'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "business-cycle", "macroeconomics"]
---

# Business Cycle Analysis

## Overview

The business cycle describes recurring fluctuations in economic activity: expansion → peak → contraction → trough → expansion. Understanding the current phase helps businesses time investments, manage inventory, and prepare for downturns or recoveries.

## Framework

```
IRON LAW: Cycles Are Inevitable, Timing Is Not Predictable

Business cycles WILL happen — no economy grows forever. But predicting
EXACTLY when a peak or trough occurs is unreliable. Focus on identifying
the CURRENT phase and preparing for the NEXT one, not predicting exact
turning points.
```

### The Four Phases

| Phase | Characteristics | Key Indicators |
|-------|----------------|----------------|
| **Expansion** | Rising GDP, falling unemployment, growing profits, rising asset prices | PMI > 50, yield curve normal, consumer confidence rising |
| **Peak** | Economy at maximum output, inflation accelerating, capacity constraints | PMI declining from highs, inflation above target, central bank tightening |
| **Contraction** | Falling GDP, rising unemployment, declining profits, credit tightening | PMI < 50, yield curve may invert, layoffs increasing |
| **Trough** | Economy at minimum, excess capacity, low inflation, maximum pessimism | PMI stabilizing, central bank easing, inventories depleted |

### Phase Identification Steps

1. **Check leading indicators**: PMI, yield curve, stock market, consumer confidence, building permits
2. **Check coincident indicators**: Industrial production, retail sales, employment
3. **Check lagging indicators**: Unemployment rate, CPI, corporate profits, loan delinquency
4. **Look for divergence**: Leading indicators turning while lagging are still strong = inflection point

### Strategic Response by Phase

| Phase | Business Strategy | Financial Strategy |
|-------|------------------|-------------------|
| **Expansion** | Invest in capacity, hire, launch new products | Lock in fixed-rate debt, build reserves |
| **Peak** | Reduce inventory, tighten credit terms, prepare cost cuts | Reduce leverage, increase cash position |
| **Contraction** | Cut costs, preserve cash, acquire distressed assets | Extend debt maturities, negotiate with creditors |
| **Trough** | Invest counter-cyclically, acquire talent at lower cost | Deploy cash reserves, buy undervalued assets |

### Recession Indicators

| Indicator | Signal |
|-----------|--------|
| Inverted yield curve | 10Y-2Y Treasury spread negative → recession in 12-18 months (historically ~80% accurate) |
| Sahm Rule | Unemployment 3-month average rises 0.5%+ from 12-month low |
| 2 consecutive quarters negative GDP | Technical recession (lagging confirmation) |
| Conference Board Leading Index | 6+ months of decline |

## Output Format

```markdown
# Business Cycle Assessment: {Country/Region}

## Current Phase: {Expansion / Peak / Contraction / Trough}

## Evidence
| Category | Indicator | Reading | Signal |
|----------|-----------|---------|--------|
| Leading | PMI | XX | {interpretation} |
| Leading | Yield curve | XX bps | {interpretation} |
| Coincident | Industrial production | X% YoY | {interpretation} |
| Lagging | Unemployment | X% | {interpretation} |

## Phase Progression
{Where we are in the cycle and directional signals}

## Strategic Implications
| Domain | Recommendation |
|--------|---------------|
| Investment | {expand/hold/cut} |
| Hiring | {hire/freeze/reduce} |
| Inventory | {build/maintain/liquidate} |
| Pricing | {raise/hold/discount} |
| Cash management | {deploy/conserve} |
```

## Examples

### Correct Application
**Scenario:** Taiwan economy Q4 2025
- PMI: 48.5 (below 50, declining for 3 months) → **Leading: contraction signal**
- Consumer confidence: declining → **Leading: supports contraction**
- GDP: +3.2% YoY → **Lagging: still positive**
- Unemployment: 3.6% → **Lagging: still low**

**Diagnosis**: Likely at or just past **Peak**, entering early contraction. Leading indicators are negative but lagging indicators haven't caught up yet — classic inflection point ✓

**Strategy**: Reduce inventory, tighten receivables, build cash position, delay non-essential capex.

### Incorrect Application
- "GDP is 3.2% and unemployment is 3.6%, everything is fine" → Only looking at lagging indicators while ignoring leading indicators that signal a downturn. Like driving by looking only in the rearview mirror. Violates Iron Law: cycles are inevitable, prepare for the next phase.

## Gotchas

- **Yield curve inversion**: Historically the strongest recession predictor (~12-18 month lead time), but has produced false positives. Use as one signal among many, not a standalone trigger.
- **Policy response changes cycles**: Central bank intervention (QE, rate cuts) can shorten contractions or extend expansions. Modern cycles don't follow textbook patterns exactly.
- **Sector cycles differ**: Tech, real estate, commodities, and consumer staples cycle at different times and amplitudes. Your industry may be contracting while the overall economy expands.
- **Global interconnection**: Taiwan's cycle is heavily influenced by US demand, China's economy, and the global semiconductor cycle. Domestic indicators alone are insufficient.
- **Counter-cyclical opportunity**: The best time to invest is often during contraction (low prices, available talent, weakened competitors). But it requires pre-built cash reserves and courage.

## References

- For macroeconomic indicators interpretation, see the econ-macro-indicators skill
- For historical Taiwan business cycle data, see `references/taiwan-cycles.md`
