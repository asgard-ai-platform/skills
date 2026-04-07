---
name: "biz-stp"
description: "Apply STP (Segmentation, Targeting, Positioning) framework for market strategy. Use this skill when the user needs to define target customer segments, select which segments to pursue, or craft a positioning statement — even if they say 'who is our customer', 'which market should we focus on', or 'how should we position ourselves'."
metadata:
  category: "WP-14 商學院—行銷"
  tags: ["marketing", "stp", "segmentation", "positioning"]
---

# STP: Segmentation, Targeting, Positioning

## Overview

STP is the foundational marketing strategy framework: divide the market into segments (S), select which to serve (T), and define how to win in chosen segments (P). It must be done in sequence — you cannot position without first choosing a target, and you cannot target without first segmenting.

## When to Use

**Trigger conditions:**
- User launching a new product and needs to define the target audience
- User asks "who is our customer?" or "which segment should we focus on?"
- User wants to craft a positioning statement or differentiation strategy
- User's marketing feels unfocused — "we're trying to be everything to everyone"

**When NOT to use:**
- For competitive industry analysis → use Porter's Five Forces
- For growth path decisions → use Ansoff Matrix
- For internal capability assessment → use SWOT

## Framework

```
IRON LAW: Sequential Execution — S Before T Before P

Segmentation FIRST, then Targeting, then Positioning. In that order.
Choosing a target without segmenting first means you're guessing.
Positioning without a clear target means you're positioning for everyone
(which means no one).
```

```
IRON LAW: Segments Must Be MAMS

Every segment must satisfy all four criteria:
- Measurable: You can estimate the segment's size and purchasing power
- Accessible: You can reach the segment through available channels
- Material: The segment is large enough to be profitable
- Substantial: The segment is distinct enough to respond differently to
  different marketing mixes

A "segment" that fails any criterion is not actionable.
```

### Step 1: Segmentation — Divide the Market

Use one or more segmentation bases:

| Base | Variables | Example |
|------|-----------|---------|
| **Demographic** | Age, gender, income, education, occupation, family size | "25-35 year old urban professionals earning >NT$60K/month" |
| **Geographic** | Country, city, climate, urban/rural, region | "Northern Taiwan metropolitan areas" |
| **Psychographic** | Lifestyle, values, personality, interests | "Health-conscious, willing to pay premium for organic" |
| **Behavioral** | Usage rate, loyalty, benefits sought, purchase occasion | "Heavy users who buy weekly, price-insensitive, value convenience" |

Combine bases for sharper segments (e.g., demographic + behavioral).

Produce 3-6 distinct segments. Fewer than 3 means you haven't segmented; more than 6 is too fragmented to act on.

### Step 2: Targeting — Select Your Segments

Evaluate each segment on:

| Criterion | Question |
|-----------|----------|
| **Size & Growth** | How large is the segment? Is it growing? |
| **Profitability** | What margins can you achieve in this segment? |
| **Competition** | How many competitors serve this segment? How strong? |
| **Fit** | Does this segment align with your capabilities and brand? |
| **Accessibility** | Can you reach this segment cost-effectively? |

Choose a targeting strategy:
- **Concentrated**: Focus on one segment (highest risk, highest specialization)
- **Differentiated**: Target 2-3 segments with tailored offers (moderate risk)
- **Undifferentiated**: Same offer to all (rarely recommended — defeats the purpose of STP)

### Step 3: Positioning — Define Your Place in the Customer's Mind

Craft a positioning statement using this template:

```
For [target segment],
[brand/product] is the [category]
that [key benefit/differentiator]
because [reason to believe].
```

Then validate positioning against three tests:
1. **Relevance**: Does the target segment care about this benefit?
2. **Differentiation**: Can competitors claim the same thing?
3. **Credibility**: Can you deliver on this promise?

### Step 4: Perceptual Map (Optional)

Plot brands on a 2D map using the two most important attributes for the target segment. This visualizes competitive positioning and identifies gaps.

## Output Format

```markdown
# STP Analysis: {Product/Brand}

## Segmentation

| Segment | Profile | Size | Growth | Key Need |
|---------|---------|------|--------|----------|
| Seg A | {description} | {$X / N people} | {X%} | {primary need} |
| Seg B | ... | ... | ... | ... |
| Seg C | ... | ... | ... | ... |

## Targeting

| Segment | Size | Profitability | Competition | Fit | Score |
|---------|------|-------------|-------------|-----|-------|
| Seg A | H/M/L | H/M/L | H/M/L | H/M/L | {total} |

**Selected target(s):** {segment(s)} — {rationale}
**Targeting strategy:** Concentrated / Differentiated

## Positioning

**Statement:**
For {target segment}, {brand} is the {category} that {benefit} because {reason to believe}.

**Validation:**
- Relevance: ✓/✗ — {evidence}
- Differentiation: ✓/✗ — {evidence}
- Credibility: ✓/✗ — {evidence}
```

## Examples

### Correct Application

**Scenario:** STP for a new plant-based protein bar in Taiwan

**Segmentation** (Behavioral + Demographic):
| Segment | Profile | Size | Key Need |
|---------|---------|------|----------|
| Fitness Enthusiasts | 20-35, gym-goers, track macros | ~800K in Taiwan | High protein, clean label |
| Health-Conscious Office Workers | 25-45, desk jobs, skip meals | ~1.5M | Convenient meal replacement, low sugar |
| Vegan/Vegetarian Consumers | All ages, ethical/dietary choice | ~300K | Plant-based, no animal derivatives |

**Targeting**: Health-Conscious Office Workers — largest segment, underserved (most protein bars target gym-goers), high accessibility via convenience stores.

**Positioning**: "For busy professionals who skip meals, PlantBar is the plant-based protein bar that replaces a meal in 60 seconds because each bar has 20g protein, 5g fiber, and all essential vitamins — made entirely from whole food ingredients."

### Incorrect Application

**What went wrong:**
- Positioning statement: "For everyone who likes healthy food" → Not a segment. "Everyone" fails the MAMS test (not Measurable, not Substantial as a distinct group). Violates Iron Law.
- Jumped straight to positioning ("we're the premium option") without segmenting or targeting → Violates Iron Law: S before T before P.

## Gotchas

- **Over-segmentation**: Creating 10+ micro-segments that are too small to serve profitably. Each segment must pass the MAMS test, especially "Material" (large enough).
- **Demographic-only segmentation**: Demographics describe who, not why they buy. Always combine with behavioral or psychographic bases for actionable segments.
- **Positioning on features, not benefits**: "We have 20g protein" is a feature. "Replaces a meal in 60 seconds" is a benefit. Customers buy benefits.
- **Positioning that's not differentiated**: "High quality at a fair price" describes every brand. If your competitor can make the same claim, it's not positioning.
- **Ignoring the perceptual map**: Where customers THINK you are matters more than where you WANT to be. Validate positioning with customer research when possible.

## References

- For perceptual mapping techniques, see `references/perceptual-mapping.md`
- For comparison with other marketing frameworks, see `references/framework-comparison.md`
