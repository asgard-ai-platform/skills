---
name: "grad-diamond"
description: "Apply Porter's Diamond Model to analyze national competitive advantage for a specific industry. Use this skill when the user needs to evaluate why certain nations dominate particular industries, assess a country's attractiveness for industry investment, or diagnose gaps in national competitiveness using the four determinants plus government and chance."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["porter-diamond", "national-competitive-advantage", "factor-conditions", "demand-conditions", "related-industries", "firm-strategy"]
---

# Diamond Model (Porter, 1990): National Competitive Advantage

## Overview

Porter's Diamond Model explains why certain nations become home bases for globally competitive industries. Four interconnected determinants — factor conditions, demand conditions, related and supporting industries, and firm strategy/structure/rivalry — form a self-reinforcing system. Government and chance act as external variables that influence the diamond but are not determinants themselves. Crucially, national advantage is industry-specific, not economy-wide.

## When to Use

**Trigger conditions:**
- User asks why a country dominates a specific industry (e.g., Swiss watches, Korean semiconductors)
- User needs to evaluate a country as a base for a specific industry
- User is comparing national environments for investment or relocation decisions
- User mentions "national competitiveness", "diamond model", "Porter's diamond", or "country advantage"

**When NOT to use:**
- For firm-level competitive strategy -> use Porter's Five Forces
- For firm-level FDI decisions -> use grad-oli
- For gradual market entry -> use grad-uppsala

## Assumptions

```
IRON LAW: National Competitive Advantage Is INDUSTRY-SPECIFIC,
          NOT Country-Wide

A country does not have "competitive advantage" in general.
Germany has advantage in automotive and chemicals, NOT in software.
The US has advantage in tech and finance, NOT in consumer electronics
manufacturing.

NEVER assess a country's competitiveness without specifying the
industry. A "strong diamond" for one industry may be a weak diamond
for another in the SAME country.
```

- Competitive advantage is created, not inherited — advanced factors matter more than basic factors
- Domestic rivalry is a key driver of international competitiveness
- The four determinants reinforce each other as a system — isolated strengths are insufficient
- Government's role is to influence the determinants, not to pick winners

## Methodology

### Step 1: Define the Industry Scope

Specify the industry narrowly. "Manufacturing" is too broad; "precision instruments" or "semiconductor fabrication" is appropriate. The diamond analysis must be industry-specific.

### Step 2: Analyze the Four Determinants

**1. Factor Conditions**: Basic factors (natural resources, unskilled labor) are inherited and easily replicated. Advanced factors (research institutions, skilled engineers, VC ecosystems) are created and drive sustainable advantage.

**2. Demand Conditions**: Size enables scale; sophistication pressures innovation; anticipatory demand (foreshadowing global trends) gives domestic firms a head start.

**3. Related and Supporting Industries**: Internationally competitive suppliers, geographic clustering, knowledge spillovers, and rapid innovation cycles.

**4. Firm Strategy, Structure, and Rivalry**: National culture shapes management practices; intense domestic rivalry drives innovation; capital market structures affect time horizons.

### Step 3: Assess Government and Chance

- **Government**: Policies that strengthen determinants (education investment, R&D subsidies, competition policy, infrastructure). Government should catalyze, not control.
- **Chance**: Exogenous events (wars, oil shocks, technological discontinuities, pandemics) that reshape the diamond.

### Step 4: Evaluate Diamond System Strength

Rate each determinant and assess systemic reinforcement:
- Do strong demand conditions pull advanced factor creation?
- Does domestic rivalry drive innovation that demanding customers then validate?
- Do related industries create clusters that attract specialized talent?

A strong diamond has reinforcing loops. A weak diamond has isolated strengths that do not compound.

## Output Format

```markdown
# Diamond Analysis: {Industry} in {Country}

## Determinant Ratings
| Determinant | Key Evidence | Rating |
|-------------|-------------|--------|
| Factor Conditions (basic/advanced) | {assessment} | Strong/Moderate/Weak |
| Demand Conditions | {assessment} | Strong/Moderate/Weak |
| Related & Supporting Industries | {assessment} | Strong/Moderate/Weak |
| Firm Strategy, Structure & Rivalry | {assessment} | Strong/Moderate/Weak |

## External Variables
- Government: {policies} | Chance: {events}

## System Assessment
- Reinforcing loops: {which determinants strengthen each other}
- Weak links: {gaps} | Overall: Strong/Moderate/Weak for {industry}
- Recommendations: {how to strengthen weak determinants}
```

## Gotchas

- **Country GDP is not industry competitiveness**: A wealthy country can have a weak diamond for a specific industry. Always analyze at industry level.
- **Basic factors are a trap**: Reliance on cheap labor or raw materials leads to the "resource curse." Advanced factors drive sustainable advantage.
- **Domestic rivalry is counterintuitive**: Protecting firms from competition weakens the diamond. Rivalry is painful but essential.
- **The diamond is dynamic**: A once-strong diamond (Detroit for autos) can erode. Reassess longitudinally.
- **Multi-country diamonds exist**: In small open economies the diamond may span borders. Do not force single-country framing.

## References

- For Porter's original diamond factor taxonomy, see `references/diamond-factor-taxonomy.md`
- For double diamond model (Rugman) and extensions, see `references/double-diamond-extensions.md`
