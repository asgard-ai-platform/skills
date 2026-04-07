---
name: "econ-behavioral"
description: "Apply behavioral economics concepts including bounded rationality, prospect theory, mental accounting, and nudge theory to analyze decision-making biases. Use this skill when the user needs to understand why people make irrational economic decisions, design choice architectures, or apply nudges to influence behavior — even if they say 'why do customers make bad choices', 'how do we encourage people to save more', or 'design a better default option'."
metadata:
  category: "WP-17 經濟學院"
  tags: ["economics", "behavioral-economics", "decision-making"]
---

# Behavioral Economics

## Overview

Behavioral economics studies how psychological factors cause people to deviate from rational economic predictions. Where classical economics assumes rational actors, behavioral economics documents systematic biases and designs interventions (nudges) to improve decisions.

## Framework

```
IRON LAW: Biases Are Systematic, Not Random

Behavioral biases are PREDICTABLE patterns, not noise. Loss aversion
doesn't sometimes make people risk-seeking and sometimes not — it
consistently makes people overweight losses relative to equivalent gains
(roughly 2:1 ratio). Use specific bias names and their documented effects,
not vague "people are irrational."
```

### Core Concepts

**Bounded Rationality** (Simon): People satisfice (find "good enough") rather than optimize because cognitive resources are limited.

**Prospect Theory** (Kahneman & Tversky):
- **Loss aversion**: Losses hurt ~2x more than equivalent gains feel good
- **Reference dependence**: People evaluate outcomes relative to a reference point, not in absolute terms
- **Diminishing sensitivity**: The difference between $0 and $100 feels larger than between $1000 and $1100

**Mental Accounting** (Thaler): People categorize money into mental "buckets" (rent, fun, savings) and treat them differently, violating fungibility.

**Framing Effect**: Same information presented differently leads to different decisions. "90% survival rate" vs "10% mortality rate" — same fact, different choices.

### Key Biases for Business Application

| Bias | Definition | Business Application |
|------|-----------|---------------------|
| **Anchoring** | First number seen influences subsequent estimates | Show high "original price" before discount |
| **Default effect** | People stick with the pre-selected option | Opt-out > opt-in for subscriptions, organ donation |
| **Social proof** | People follow what others do | "1,000+ customers chose this plan" |
| **Scarcity** | Limited availability increases perceived value | "Only 3 left in stock" |
| **Endowment effect** | People overvalue what they already own | Free trials make cancellation feel like a loss |
| **Present bias** | People overweight immediate rewards vs future | "Start free today" > "Save money over 12 months" |
| **Sunk cost fallacy** | Past investments influence future decisions (shouldn't) | "I've already watched 2 hours, I should finish the movie" |
| **Status quo bias** | Preference for current state over change | Existing customers rarely switch, even when better options exist |

### Nudge Design Framework (Thaler & Sunstein)

**EAST Framework** for effective nudges:
- **Easy**: Reduce friction. Simplify forms, pre-fill data, reduce steps.
- **Attractive**: Make the desired action visually prominent and appealing.
- **Social**: Show what others are doing. Peer comparisons, testimonials.
- **Timely**: Deliver the nudge at the moment of decision, not before or after.

### Analysis Steps

1. **Identify the decision context**: What choice is the user/customer making?
2. **Map relevant biases**: Which systematic biases are likely at play?
3. **Evaluate current choice architecture**: How is the decision currently presented?
4. **Design interventions**: Apply nudges using EAST framework
5. **Test**: A/B test the intervention against the current design

## Output Format

```markdown
# Behavioral Analysis: {Decision Context}

## Decision Context
- Decision-maker: {who}
- Choice: {what they're deciding}
- Current behavior: {what they typically do}
- Desired behavior: {what we want them to do}

## Biases Identified
| Bias | How It Manifests | Impact |
|------|-----------------|--------|
| {bias} | {specific manifestation} | H/M/L |

## Current Choice Architecture
{How the decision is currently structured and why it triggers biases}

## Proposed Nudges
| Nudge | EAST Principle | Expected Effect |
|-------|---------------|----------------|
| {intervention} | Easy/Attractive/Social/Timely | {predicted change} |

## Testing Plan
- Control: {current design}
- Treatment: {nudged design}
- Metric: {conversion rate / opt-in rate / etc.}
- Sample size: {N}
```

## Examples

### Correct Application
**Scenario:** Increasing retirement savings enrollment in a Taiwanese company

**Biases at play:**
- **Status quo bias**: Employees don't enroll because they'd have to actively opt in
- **Present bias**: Retirement is decades away; spending now feels more urgent
- **Loss aversion**: Monthly salary deduction feels like a loss

**Nudge design:**
| Nudge | Principle | Intervention |
|-------|-----------|-------------|
| Auto-enrollment | **Easy** (default) | Change from opt-in to opt-out (3% default contribution) |
| Escalation | **Timely** | "Increase contribution by 1% at each annual raise" — timed to coincide with salary increase so deduction doesn't feel like a loss |
| Social proof | **Social** | "78% of your colleagues contribute to the retirement plan" |

**Predicted effect**: Auto-enrollment alone typically increases participation from ~30% to ~90% (well-documented in literature) ✓

### Incorrect Application
- "People are irrational, so we should manipulate them" → Behavioral economics identifies systematic patterns, not random irrationality. Nudges should help people make decisions aligned with their OWN stated goals, not manipulate against their interests. Violates Iron Law and ethical principles.

## Gotchas

- **Nudges are libertarian paternalism**: They preserve choice while steering toward better outcomes. If the nudge removes choice, it's not a nudge — it's a mandate.
- **Biases interact**: Loss aversion + anchoring + framing can combine. "Save NT$300" (gain frame) vs "Stop losing NT$300/month" (loss frame + anchoring) — the latter is stronger due to compounding biases.
- **Cultural variation**: Some biases vary across cultures. Social proof is stronger in collectivist cultures (Taiwan, Japan) than individualist ones. Calibrate for context.
- **Nudge fatigue**: Too many nudges simultaneously reduce effectiveness. Prioritize the highest-impact one.
- **Ethical boundary**: Using biases to sell products people don't need (dark patterns) is exploitation, not nudging. The test: would the person thank you for the nudge if they knew about it?

## References

- For prospect theory mathematics, see `references/prospect-theory.md`
- For dark patterns vs ethical nudges, see `references/ethics-of-nudging.md`
