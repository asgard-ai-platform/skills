---
name: "biz-swot"
description: "Conduct SWOT analysis with TOWS matrix for strategic planning. Use this skill when the user needs to evaluate a company, product, or project by identifying strengths, weaknesses, opportunities, and threats, or wants to generate strategic options from internal and external factors. Also use when the user mentions competitive positioning, strategic assessment, or asks 'what are our advantages and risks', even without naming SWOT explicitly."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "swot", "tows"]
---

# SWOT Analysis with TOWS Matrix

## Overview

SWOT structures strategic assessment by separating internal factors (Strengths, Weaknesses) from external factors (Opportunities, Threats). The TOWS matrix then crosses these four quadrants to generate concrete strategy options. This skill guides the full workflow: from factor identification through prioritization to actionable strategy formulation.

## When to Use

**Trigger conditions:**
- User asks to assess a company, product, team, or project's strategic position
- User needs to identify advantages, risks, or competitive factors
- User wants to turn a situational analysis into strategy options
- User mentions "SWOT", "strengths and weaknesses", or "strategic assessment"

**When NOT to use:**
- For industry-level competitive dynamics → use Porter's Five Forces
- For macro-environment scanning → use PESTEL
- For product portfolio decisions → use BCG Matrix
- When the user only needs financial analysis, not strategic positioning

## Framework

```
IRON LAW: Internal vs External Classification

Strengths and Weaknesses are INTERNAL — they originate from within the
organization and the organization can directly control or change them.
Examples: proprietary technology, brand reputation, team expertise, cost
structure, operational processes.

Opportunities and Threats are EXTERNAL — they originate from the environment
and the organization cannot directly control them.
Examples: market trends, regulatory changes, competitor actions, economic
conditions, technological shifts.

NEVER classify an external trend as a Strength or Weakness.
NEVER classify an internal capability as an Opportunity or Threat.

Test: "Can the organization decide to change this tomorrow?"
  YES → Internal (S or W)
  NO  → External (O or T)
```

```
IRON LAW: Completeness Before Synthesis

Complete ALL four quadrants before generating strategies.
Do NOT jump to recommendations after identifying only strengths and
opportunities. Skipping W or T produces dangerously optimistic strategies.
```

### Step 1: Identify Internal Factors (S and W)

Examine the organization's resources, capabilities, and performance:

- **Tangible**: financial resources, physical assets, technology, patents
- **Intangible**: brand equity, culture, expertise, relationships, reputation
- **Capabilities**: processes, skills, management quality, innovation track record

For each factor, classify as Strength (competitive advantage) or Weakness (competitive disadvantage) relative to competitors. Be specific — "good team" is too vague; "engineering team with 5+ years experience in ML deployment" is actionable.

### Step 2: Identify External Factors (O and T)

Scan the environment across these dimensions:

- **Market**: growth trends, customer needs shifts, new segments
- **Competitive**: competitor moves, new entrants, substitutes
- **Macro**: regulatory, economic, technological, social changes
- **Industry-specific**: supply chain shifts, channel evolution, standards changes

For each factor, classify as Opportunity (favorable) or Threat (unfavorable). Ground each factor in evidence — cite data, trends, or specific events when possible.

### Step 3: Prioritize Factors

Not all factors carry equal weight. For each quadrant, rank factors by:

1. **Impact**: How significantly would this affect the organization? (High / Medium / Low)
2. **Likelihood** (for O and T): How probable is this? (High / Medium / Low)
3. **Urgency**: Is this time-sensitive?

Keep the top 3-5 factors per quadrant for the TOWS matrix. Including too many dilutes the analysis.

### Step 4: Build the TOWS Matrix

Cross the four quadrants to generate four types of strategies:

| | **Opportunities** | **Threats** |
|---|---|---|
| **Strengths** | **SO strategies**: Use strengths to capture opportunities | **ST strategies**: Use strengths to defend against threats |
| **Weaknesses** | **WO strategies**: Address weaknesses to capture opportunities | **WT strategies**: Minimize weaknesses to avoid threats |

For each cell, generate 1-3 specific strategy options. Each strategy must reference at least one factor from each axis (e.g., SO strategy must name a specific strength AND a specific opportunity).

### Step 5: Formulate Action Plan

Convert the most promising TOWS strategies into actionable recommendations:

1. Select the 3-5 highest-impact strategies across all four cells
2. For each, define: objective, owner, timeline, resources needed, success metric
3. Flag dependencies and potential conflicts between strategies

## Output Format

```markdown
# SWOT Analysis: {Subject}

## Internal Factors

### Strengths
| # | Factor | Evidence | Impact |
|---|--------|----------|--------|
| S1 | {specific strength} | {supporting data} | High/Med/Low |
| S2 | ... | ... | ... |

### Weaknesses
| # | Factor | Evidence | Impact |
|---|--------|----------|--------|
| W1 | {specific weakness} | {supporting data} | High/Med/Low |
| W2 | ... | ... | ... |

## External Factors

### Opportunities
| # | Factor | Evidence | Likelihood |
|---|--------|----------|-----------|
| O1 | {specific opportunity} | {supporting data} | High/Med/Low |
| O2 | ... | ... | ... |

### Threats
| # | Factor | Evidence | Likelihood |
|---|--------|----------|-----------|
| T1 | {specific threat} | {supporting data} | High/Med/Low |
| T2 | ... | ... | ... |

## TOWS Strategy Matrix

| | Opportunities (O1, O2...) | Threats (T1, T2...) |
|---|---|---|
| **Strengths** | SO: {strategy using S to capture O} | ST: {strategy using S to counter T} |
| **Weaknesses** | WO: {strategy to fix W and capture O} | WT: {strategy to minimize W and avoid T} |

## Recommended Actions
1. **{Strategy name}** — {description} (from: {SO/ST/WO/WT})
   - Timeline: ...
   - Success metric: ...
2. ...
```

## Examples

### Correct Application

**Scenario:** SWOT for a mid-size Taiwanese bubble tea chain considering expansion to Japan

**Analysis:**

| Quadrant | Factor | Classification | Reasoning |
|----------|--------|---------------|-----------|
| **S** | Proprietary tapioca pearl recipe with unique texture | Internal ✓ | Company's own R&D product |
| **S** | 50 stores in Taiwan with proven SOP | Internal ✓ | Company's operational asset |
| **W** | No Japanese-speaking management team | Internal ✓ | Company's own resource gap |
| **W** | Limited capital for overseas expansion | Internal ✓ | Company's financial constraint |
| **O** | Japanese bubble tea market growing 15% YoY | External ✓ | Market trend, not company-controlled |
| **O** | Japan-Taiwan tourism recovery post-COVID | External ✓ | Macro environment factor |
| **T** | Established Japanese competitors (Gong Cha, CoCo) | External ✓ | Competitor landscape |
| **T** | Yen depreciation increasing import costs | External ✓ | Economic condition |

**TOWS strategy example:**
- **SO**: Leverage proprietary recipe (S1) to differentiate in the growing Japanese market (O1) — position as "authentic Taiwanese craft tea"
- **WT**: Address capital limitation (W2) by minimizing currency risk (T2) — source ingredients locally in Japan where possible

### Incorrect Application

**Scenario:** Same bubble tea chain

**What went wrong:**

| Factor | Placed In | Should Be | Why |
|--------|-----------|-----------|-----|
| "Japanese bubble tea market growing 15% YoY" | **Strength** ❌ | **Opportunity** | Market growth is an external trend — the company cannot control it. Violates Iron Law: internal factors only in S/W. |
| "Our team lacks experience" | **Threat** ❌ | **Weakness** | Team composition is internal — the company controls who it hires. Violates Iron Law: external factors only in O/T. |
| "Good brand" | **Strength** ⚠️ | Needs specificity | Too vague to be actionable. What makes the brand good? Recognition in Taiwan? Social media following? Specific awards? |

## Gotchas

- **Internal/External confusion with "market position"**: "We are the #3 player" feels internal but the ranking itself is determined by market dynamics. Split it: "Strong distribution network in northern Taiwan" (S, internal capability) vs "Market consolidation reducing number of competitors" (O or T, external trend).
- **Strengths that are actually table stakes**: "We have a website" is not a strength if every competitor also has one. Strengths must be relative advantages vs competitors.
- **Confusing absence of threat with opportunity**: "No major competitor in this niche" is NOT an opportunity — it may signal the niche is not viable. An opportunity requires a positive external trend or event.
- **TOWS strategies that only reference one axis**: "Expand to Japan" is not a TOWS strategy. It must cross quadrants: "Leverage proprietary recipe (S1) to enter the growing Japanese market (O1)."
- **Scope drift**: SWOT for "the company" is too broad. Scope to a specific decision: "SWOT for expanding to Japan" or "SWOT for launching a new product line."
- **Recency bias**: Recent events dominate the analysis. Force consideration of structural, long-term factors alongside current events.

## References

- For detailed TOWS matrix case studies, see `references/tows-case-studies.md`
- For comparison with other strategy frameworks (Porter's, PESTEL, BCG), see `references/framework-comparison.md`
