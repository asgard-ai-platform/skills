---
name: "econ-macro-indicators"
description: "Interpret macroeconomic indicators including GDP, inflation, unemployment, interest rates, and exchange rates to assess economic health and predict trends. Use this skill when the user needs to evaluate a country's economic outlook, understand monetary/fiscal policy impacts, or contextualize business decisions within the macroeconomic environment — even if they say 'is the economy doing well', 'what do rising interest rates mean for us', or 'explain today's economic data'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "macroeconomics", "economic-indicators"]
---

# Macroeconomic Indicators

## Overview

Macroeconomic indicators measure aggregate economic performance. They divide into leading (predict future), coincident (reflect current), and lagging (confirm past) indicators. Understanding these helps contextualize business decisions within the broader economic environment.

## Framework

```
IRON LAW: Leading, Coincident, or Lagging — Know Which Type

GDP growth is LAGGING — by the time it's published, the economy has already
changed. Stock markets and PMI are LEADING — they predict future direction.
Unemployment is LAGGING — it rises after a recession starts.

Using a lagging indicator to predict the future is looking in the rearview mirror.
Match the indicator type to your analysis purpose.
```

### Key Indicators

**GDP (Gross Domestic Product)**
- Type: Lagging
- Measures: Total economic output
- Key signals: 2 consecutive quarters of negative growth = technical recession
- Taiwan: Published quarterly by DGBAS

**Inflation (CPI/PPI)**
- Type: Coincident
- CPI = consumer prices, PPI = producer prices (leading indicator for CPI)
- Target: Most central banks target ~2%
- Taiwan: CPI published monthly by DGBAS

**Unemployment Rate**
- Type: Lagging
- Natural rate varies by country (~3.5-4% for Taiwan)
- Watch U-3 (official) vs broader measures that include underemployment

**Interest Rates**
- Central bank policy rate (台灣央行重貼現率)
- Raising rates → slows economy, fights inflation, strengthens currency
- Lowering rates → stimulates economy, risks inflation, weakens currency

**Exchange Rate**
- TWD/USD, TWD/JPY, TWD/CNY for Taiwan-centric analysis
- Depreciation → exports cheaper but imports more expensive
- Watch real effective exchange rate (REER) for trade competitiveness

**PMI (Purchasing Managers' Index)**
- Type: Leading
- Above 50 = expansion, below 50 = contraction
- Published monthly, available before GDP data

### Indicator Relationships

```
Central bank raises rates
  → Borrowing costs rise
    → Consumer spending slows + Business investment slows
      → GDP growth slows
        → Unemployment rises (with lag)
          → Inflation falls (the goal)
```

### Analysis Steps

1. **Gather current data** for 5-6 key indicators
2. **Classify each** as leading/coincident/lagging
3. **Identify trends** (improving, stable, deteriorating)
4. **Check for divergence** (leading indicators pointing different direction from lagging = inflection point)
5. **Assess implications** for the specific business/industry context

## Output Format

```markdown
# Macroeconomic Assessment: {Country/Region}

## Indicator Dashboard
| Indicator | Current | Previous | Trend | Type |
|-----------|---------|----------|-------|------|
| GDP Growth | X% | X% | ↑/↓/→ | Lagging |
| CPI Inflation | X% | X% | ↑/↓/→ | Coincident |
| Unemployment | X% | X% | ↑/↓/→ | Lagging |
| Policy Rate | X% | X% | ↑/↓/→ | — |
| PMI | XX | XX | ↑/↓/→ | Leading |
| Exchange Rate | X.XX | X.XX | ↑/↓/→ | — |

## Economic Phase
{Expansion / Peak / Contraction / Trough}

## Key Signals
- Leading indicators suggest: {direction}
- Divergence: {if any — e.g., PMI falling while GDP still positive = slowdown ahead}

## Business Implications
- For {industry}: {specific impact}
```

## Examples

### Correct Application
**Scenario:** Taiwan macro assessment Q4 2025
| Indicator | Value | Signal |
|-----------|-------|--------|
| GDP Growth | 3.2% YoY | Solid but decelerating from 4.1% |
| CPI | 2.1% | Near target, stable |
| Unemployment | 3.6% | Near full employment |
| Policy Rate | 2.0% | Held steady for 3 quarters |
| PMI | 48.5 | Below 50 — **leading indicator of slowdown** |

Diagnosis: GDP looks healthy (lagging) but PMI signals contraction ahead. The economy is likely at or near **peak** phase ✓

### Incorrect Application
- "GDP grew 3.2% last quarter, so the economy will grow next quarter too" → GDP is lagging. PMI at 48.5 suggests otherwise. Violates Iron Law: using lagging indicator to predict future.

## Gotchas

- **Headline vs core inflation**: Headline CPI includes volatile food and energy. Core CPI excludes them. Central banks focus on core for policy decisions.
- **Real vs nominal**: Always specify. "GDP grew 5%" — nominal or real? Real GDP adjusts for inflation and shows true growth.
- **Seasonal adjustment**: Unemployment, retail sales, and many indicators are seasonally adjusted. Compare adjusted-to-adjusted, never adjusted-to-raw.
- **Taiwan-specific**: Taiwan's economy is heavily export-dependent. TSMC's revenue guidance is arguably a better leading indicator for Taiwan than generic PMI.
- **Data revision**: Initial GDP estimates are revised 2-3 times. Don't overreact to first releases.

## References

- For business cycle theory, see the econ-business-cycle skill
- For Taiwan-specific economic data sources, see `references/taiwan-data-sources.md`
