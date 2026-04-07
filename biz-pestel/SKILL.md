---
name: "biz-pestel"
description: "Apply PESTEL framework to scan the macro-environment across Political, Economic, Social, Technological, Environmental, and Legal dimensions. Use this skill when the user needs to assess external macro factors affecting a business, industry, or market — especially before entering a new country, launching a product, or evaluating regulatory risk. Also use when the user mentions 'macro analysis', 'external environment', or 'what trends should we watch'."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "pestel", "macro-environment"]
---

# PESTEL Analysis

## Overview

PESTEL scans the macro-environment across six dimensions to identify external forces that could impact a business or industry. It operates at the **macro level** — broader than industry (Porter's Five Forces) or company (SWOT). Use it to surface trends and risks the organization cannot control but must respond to.

## When to Use

**Trigger conditions:**
- User evaluating a new market or country for expansion
- User needs to understand regulatory, economic, or social trends
- User wants to identify macro risks before strategic planning
- User asks "what external factors should we consider?"

**When NOT to use:**
- For company-specific assessment → use SWOT
- For industry competitive dynamics → use Porter's Five Forces
- For product portfolio decisions → use BCG Matrix

## Framework

```
IRON LAW: Macro-Level Only

PESTEL factors are MACRO-ENVIRONMENT forces — they affect all players in
a market, not just one company. "Our costs are rising" is not a PESTEL factor.
"Inflation is driving up input costs across the industry" is.

Test: "Does this factor affect ALL companies in this market?"
  YES → Valid PESTEL factor
  NO  → It belongs in SWOT or Five Forces, not PESTEL
```

```
IRON LAW: Evidence-Based, Not Speculative

Every PESTEL factor must be grounded in observable data, trends, or events.
"Technology might change" is not a factor. "5G rollout reaching 70% coverage
by 2026 (GSMA data)" is a factor.
```

### Step 1: Define the Scope

- **What entity?** Country, region, or market being analyzed
- **For whom?** Which business or industry perspective
- **Time horizon**: near-term (1-2 years) or medium-term (3-5 years)

### Step 2: Scan Each Dimension

For each of the six dimensions, identify 2-4 key factors with evidence:

**P — Political**: Government stability, trade policy, taxation policy, political risk, corruption, foreign investment rules

**E — Economic**: GDP growth, inflation, interest rates, exchange rates, unemployment, consumer spending power, commodity prices

**S — Social**: Demographics, cultural trends, consumer attitudes, lifestyle changes, education levels, urbanization, health consciousness

**T — Technological**: R&D activity, automation, digital infrastructure, emerging technologies, innovation rate, tech transfer

**E — Environmental**: Climate change, sustainability regulations, resource scarcity, carbon emissions rules, environmental awareness, natural disaster risk

**L — Legal**: Employment law, consumer protection, data privacy (GDPR, PDPA), industry-specific regulation, IP protection, antitrust

### Step 3: Assess Impact and Likelihood

For each factor:
- **Impact on the business**: High / Medium / Low
- **Likelihood of change**: High / Medium / Low
- **Direction**: Favorable (+) or Unfavorable (−)

### Step 4: Prioritize and Connect

1. Rank factors by impact × likelihood
2. Identify cross-dimensional connections (e.g., political instability → economic uncertainty → social unrest)
3. Highlight the top 3-5 factors that require strategic response

## Output Format

```markdown
# PESTEL Analysis: {Market/Country} for {Business Context}

## Scope
- Market: ...
- Perspective: ...
- Time horizon: ...

## PESTEL Factors

| Dimension | Factor | Evidence | Impact | Direction |
|-----------|--------|----------|--------|-----------|
| Political | ... | ... | H/M/L | +/− |
| Economic | ... | ... | H/M/L | +/− |
| Social | ... | ... | H/M/L | +/− |
| Technological | ... | ... | H/M/L | +/− |
| Environmental | ... | ... | H/M/L | +/− |
| Legal | ... | ... | H/M/L | +/− |

### Political
{Detailed analysis}

### Economic
{Detailed analysis}

### Social
{Detailed analysis}

### Technological
{Detailed analysis}

### Environmental
{Detailed analysis}

### Legal
{Detailed analysis}

## Priority Factors
1. {Highest impact factor} — {required response}
2. ...
3. ...

## Cross-Dimensional Connections
- {Factor A} → {Factor B} → {combined implication}
```

## Examples

### Correct Application

**Scenario:** PESTEL for Vietnam market, perspective of a Taiwanese food manufacturer (2025-2028)

| Dimension | Factor | Evidence | Impact | Direction |
|-----------|--------|----------|--------|-----------|
| Political | Vietnam-Taiwan informal trade relations stable; no diplomatic friction | Bilateral trade volume growing YoY | Med | + |
| Economic | Vietnam GDP growth 6.5% (2024), rising middle class | World Bank data, urban consumer spending up 12% | High | + |
| Social | Young population (median age 31), increasing demand for packaged food | UN demographic data, urbanization rate 39% → projected 45% by 2030 | High | + |
| Technological | Cold chain logistics still underdeveloped outside Ho Chi Minh and Hanoi | Only 30% of food supply chain has cold storage (VCCI report) | High | − |
| Environmental | Government tightening plastic packaging regulations | Decree on solid waste management (2024) requiring recyclable packaging | Med | − |
| Legal | Food safety registration (Decree 15/2018) requires 6-month approval cycle | Foreign food products need Certificate of Free Sale + lab testing in-country | High | − |

### Incorrect Application

**Scenario:** Same Vietnam market analysis

**What went wrong:**
- "Our factory is running at 80% capacity" → **Company-level** fact, not macro factor. Violates Iron Law: PESTEL is macro-level only.
- "Technology is changing fast" → No evidence, no specificity. Violates Iron Law: evidence-based, not speculative. What technology? What change? What data?

## Gotchas

- **Overlap between dimensions**: A factor can span multiple dimensions (e.g., "data privacy law" is both Legal and Technological). Place it where the primary impact lies, and note the connection.
- **Country-level, not city-level**: PESTEL typically analyzes national macro factors. If sub-national differences matter (e.g., China's tier-1 vs tier-3 cities), note them as variations within the dimension.
- **Snapshot vs trend**: A PESTEL factor should capture the **direction of change**, not just current state. "GDP is $X" is a fact; "GDP growing at 6.5% with acceleration trend" is a useful factor.
- **Too many factors**: Listing 10+ factors per dimension creates noise. Keep to 2-4 per dimension, prioritized by impact.
- **Missing the "So what?"**: Each factor needs an implication for the business. "Population is aging" without "→ shifting demand toward health products" is incomplete.

## References

- For comparison with other strategy frameworks, see `references/framework-comparison.md`
- For country-specific PESTEL data sources, see `references/data-sources.md`
