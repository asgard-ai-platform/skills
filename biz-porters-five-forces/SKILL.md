---
name: "biz-porters-five-forces"
description: "Apply Porter's Five Forces framework to assess industry competitive dynamics and attractiveness. Use this skill when the user needs to analyze an industry's profitability structure, evaluate market entry barriers, assess supplier or buyer bargaining power, or understand competitive intensity — even if they say 'industry analysis' or 'is this market worth entering' without naming Porter's explicitly."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "porters-five-forces", "industry-analysis"]
---

# Porter's Five Forces Analysis

## Overview

Porter's Five Forces assesses industry-level competitive dynamics by examining five structural forces that determine profitability. Unlike SWOT (company-level) or PESTEL (macro-level), this framework operates at the **industry level** — it answers "is this industry attractive?" not "is this company strong?"

## When to Use

**Trigger conditions:**
- User asks whether an industry or market is attractive or profitable
- User evaluates whether to enter a new market or industry
- User needs to understand competitive dynamics beyond direct competitors
- User mentions "barriers to entry", "supplier power", or "industry structure"

**When NOT to use:**
- For company-specific strengths/weaknesses → use SWOT
- For macro-environment scanning → use PESTEL
- For product portfolio decisions → use BCG Matrix

## Framework

```
IRON LAW: Industry-Level, Not Company-Level

Each force describes the INDUSTRY structure, not a specific company's position.
"Our supplier raised prices" is a company event.
"Suppliers in this industry are concentrated with few alternatives" is an industry force.

NEVER analyze a single company's situation — analyze the structural conditions
all players in the industry face.
```

```
IRON LAW: All Five Forces, Every Time

Analyze ALL five forces before drawing conclusions. Skipping forces produces
misleading assessments. An industry with low rivalry but high substitute threat
is very different from one with low rivalry and no substitutes.
```

### Step 1: Define the Industry Boundary

Before analyzing forces, clearly define:
- **What industry?** Be specific — "food delivery platforms in Taiwan" not "tech"
- **Geographic scope**: global, regional, or national
- **Time horizon**: current state or projected 3-5 years

Getting the boundary wrong invalidates the entire analysis.

### Step 2: Analyze Each Force

Rate each force as **High / Medium / Low** pressure on industry profitability:

**1. Threat of New Entrants** — How easy is it for new players to enter?
- Capital requirements, economies of scale, brand loyalty, regulatory barriers
- Access to distribution channels, switching costs, incumbents' response

**2. Bargaining Power of Suppliers** — Can suppliers dictate terms?
- Supplier concentration, uniqueness of inputs, switching costs
- Forward integration threat, importance of volume to supplier

**3. Bargaining Power of Buyers** — Can customers dictate terms?
- Buyer concentration, price sensitivity, product differentiation
- Backward integration threat, switching costs, information availability

**4. Threat of Substitutes** — Can other products fulfill the same need?
- Price-performance of substitutes, switching costs
- Buyer propensity to substitute, functional equivalence

**5. Industry Rivalry** — How intense is competition among existing players?
- Number and size of competitors, industry growth rate
- Product differentiation, exit barriers, fixed costs structure

### Step 3: Assess Overall Industry Attractiveness

Synthesize the five forces into an overall assessment:
- More forces = High pressure → less attractive (lower profitability)
- More forces = Low pressure → more attractive (higher profitability)
- Identify the **dominant force** — the one that most constrains profitability

### Step 4: Strategic Implications

Based on the analysis:
- Which forces can the company influence or reshape?
- Where should the company position to minimize negative forces?
- What structural changes might shift forces in the future?

## Output Format

```markdown
# Porter's Five Forces: {Industry} in {Geography}

## Industry Definition
- Industry: ...
- Geographic scope: ...
- Time horizon: ...

## Five Forces Assessment

| Force | Pressure | Key Drivers |
|-------|----------|-------------|
| Threat of New Entrants | High/Med/Low | {top 2-3 drivers} |
| Supplier Power | High/Med/Low | {top 2-3 drivers} |
| Buyer Power | High/Med/Low | {top 2-3 drivers} |
| Threat of Substitutes | High/Med/Low | {top 2-3 drivers} |
| Industry Rivalry | High/Med/Low | {top 2-3 drivers} |

### 1. Threat of New Entrants: {rating}
{Analysis with evidence}

### 2. Bargaining Power of Suppliers: {rating}
{Analysis with evidence}

### 3. Bargaining Power of Buyers: {rating}
{Analysis with evidence}

### 4. Threat of Substitutes: {rating}
{Analysis with evidence}

### 5. Industry Rivalry: {rating}
{Analysis with evidence}

## Overall Assessment
- Industry attractiveness: High / Medium / Low
- Dominant force: {which force most constrains profitability}
- Profitability outlook: ...

## Strategic Implications
1. ...
2. ...
```

## Examples

### Correct Application

**Scenario:** Five Forces for the Taiwan bubble tea industry

| Force | Pressure | Reasoning |
|-------|----------|-----------|
| New Entrants | **High** | Low capital requirements (~NT$500K to open a shop), minimal regulatory barriers, many franchise options available |
| Supplier Power | **Low** | Tea leaves and tapioca are commodity inputs with many suppliers; no single supplier has pricing power |
| Buyer Power | **High** | Zero switching costs for consumers, hundreds of options within walking distance, high price sensitivity |
| Substitutes | **Medium** | Coffee, convenience store drinks, and home-brewed tea serve similar "afternoon drink" need, but bubble tea has strong cultural preference |
| Rivalry | **High** | Saturated market with thousands of shops, low differentiation among mid-tier brands, frequent price wars |

**Overall**: Low attractiveness — high entry threat + high rivalry + high buyer power squeeze margins.

### Incorrect Application

**Scenario:** Same bubble tea industry

**What went wrong:**
- "Our flagship store has strong foot traffic" → This is a **company** fact, not an **industry** force. Violates Iron Law: analyze industry structure, not individual company position.
- Only analyzed "Rivalry" and "New Entrants", skipped other three forces → Violates Iron Law: all five forces required. Missing supplier/buyer/substitute analysis gives incomplete picture.

## Gotchas

- **Confusing company position with industry structure**: "We have a strong brand" is not relevant to Five Forces. "Brand loyalty creates high barriers to entry for the industry" is.
- **Overlooking substitutes**: Most analysts underweight this force. Ask: "If prices in this industry doubled, what would customers switch to?"
- **Static analysis**: Five Forces describes current structure. Industries evolve — note emerging shifts (e.g., digital disruption lowering entry barriers).
- **Industry boundary too broad**: "The food industry" is not analyzable. Narrow to a specific segment with shared competitive dynamics.
- **Treating forces as independent**: Forces interact. High buyer power + low switching costs amplifies the effect of new entrants.

## References

- For comparison with SWOT, PESTEL, and other strategy frameworks, see `references/framework-comparison.md`
