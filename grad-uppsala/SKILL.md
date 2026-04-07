---
name: "grad-uppsala"
description: "Apply the Uppsala Internationalization Model to analyze gradual foreign market entry based on psychic distance and experiential learning. Use this skill when the user needs to plan a staged internationalization sequence, understand why firms enter culturally similar markets first, or evaluate whether a firm's international expansion follows the establishment chain from export to subsidiary."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["uppsala-model", "psychic-distance", "internationalization-process", "experiential-learning", "establishment-chain", "johanson-vahlne"]
---

# Uppsala Internationalization Model (Johanson & Vahlne, 1977)

## Overview

The Uppsala Model explains internationalization as a gradual, path-dependent process driven by experiential learning. Firms enter foreign markets incrementally, starting with psychically close countries (similar language, culture, institutions) and progressing through an establishment chain: no regular export, export via agent, sales subsidiary, production subsidiary. Each stage builds market knowledge that enables the next commitment.

## When to Use

**Trigger conditions:**
- User is planning a staged international expansion strategy
- User asks which foreign markets to enter first and in what order
- User needs to evaluate the pace and sequence of internationalization
- User mentions "psychic distance", "gradual internationalization", "Uppsala", or "establishment chain"

**When NOT to use:**
- For firms that internationalize rapidly from inception -> use grad-born-global
- For FDI mode selection (OLI-based) -> use grad-oli
- For national competitive advantage assessment -> use grad-diamond

## Assumptions

```
IRON LAW: Internationalization Is Path-Dependent

Firms enter PSYCHICALLY CLOSE markets first — those with similar
language, culture, political systems, and business practices.
Each market entry builds experiential knowledge that reduces the
perceived risk of entering the NEXT, more distant market.

Skipping stages (e.g., jumping from no exports to production
subsidiary in a distant market) violates the model and dramatically
increases failure risk — UNLESS the firm has compensating mechanisms
(acquisitions, network relationships, prior international experience).
```

- Market knowledge is primarily experiential, not codifiable
- Uncertainty reduction comes from operating in the market, not from research alone
- Commitment decisions are incremental and tied to accumulated knowledge
- The model applies best to manufacturing SMEs with limited international experience

## Methodology

### Step 1: Map Current Internationalization State

For each market the firm operates in, document:
- Current mode: Export / Agent / Sales subsidiary / Production subsidiary
- Years of presence
- Market knowledge level: Low / Medium / High
- Resource commitment level: Low / Medium / High

### Step 2: Rank Target Markets by Psychic Distance

Assess psychic distance from the home market across: language, culture (Hofstede/GLOBE), political system, economic development, and business practices. Create a ranking: Near, Moderate, Far.

### Step 3: Define the Establishment Chain

For each target market, plan the progression:

| Stage | Activity | Knowledge Required | Commitment Level |
|-------|----------|-------------------|-----------------|
| 1 | No regular export | Minimal market awareness | None |
| 2 | Export via independent agent | Basic market demand knowledge | Low |
| 3 | Sales subsidiary | Customer relationships, distribution knowledge | Medium |
| 4 | Production subsidiary | Deep operational knowledge, local supply chains | High |

Specify trigger conditions for advancing to the next stage (e.g., revenue threshold, relationship maturity).

### Step 4: Plan the Learning Cycle

The Uppsala model is a dynamic feedback loop:
1. **State variables**: Market knowledge + Market commitment (current state)
2. **Change variables**: Commitment decisions + Current activities (actions taken)
3. Activities generate knowledge -> knowledge enables commitment -> commitment generates more activities

Design explicit learning mechanisms: expatriate rotations, local hires, partnership structures.

## Output Format

```markdown
# Uppsala Internationalization Plan: {Firm}

## Current Footprint
| Market | Mode | Years | Knowledge | Commitment |
|--------|------|-------|-----------|------------|
| {Market A} | {mode} | {N} | {L/M/H} | {L/M/H} |

## Psychic Distance Ranking from {Home Country}
- Near: {markets} | Moderate: {markets} | Far: {markets}

## Recommended Entry Sequence
1. {Market}: {mode} -> {next mode} (trigger: {condition})

## Learning Mechanisms
- {Mechanism}: {how it builds market knowledge}
```

## Gotchas

- **Psychic distance is perceptual, not objective**: Managers may perceive the UK as "close" to the US despite significant differences. Validate with data.
- **Weakest for born globals**: Knowledge-intensive and digital firms routinely skip stages. Recognize when the model does not apply.
- **Psychic distance paradox**: Firms may UNDERPERFORM in close markets because perceived similarity breeds overconfidence.
- **Networks substitute for experiential knowledge**: The 2009 revision emphasizes network position can accelerate internationalization.
- **Gradual does not mean slow**: Strong learning capabilities allow rapid progression through stages.

## References

- For the 2009 revised Uppsala model (network-based), see `references/uppsala-2009-revision.md`
- For psychic distance measurement instruments, see `references/psychic-distance-scales.md`
