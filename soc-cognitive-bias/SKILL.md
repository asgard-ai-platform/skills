---
name: "soc-cognitive-bias"
description: "Identify and analyze cognitive biases including confirmation bias, anchoring, availability heuristic, and sunk cost fallacy in decision-making contexts. Use this skill when the user needs to audit a decision for bias, understand why a team keeps making the same mistakes, design debiasing interventions, or evaluate whether a conclusion is based on evidence or cognitive shortcuts — even if they say 'are we fooling ourselves', 'why do we keep getting this wrong', or 'is this analysis biased'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "cognitive-bias", "decision-making"]
---

# Cognitive Bias Analysis

## Overview

Cognitive biases are systematic deviations from rational judgment. They're not random errors — they're predictable patterns that affect everyone, including experts. This skill helps identify which biases are at play in a specific decision context and design countermeasures.

## Framework

```
IRON LAW: Name the Specific Bias, Not Just "Bias"

"This decision might be biased" is not analysis. Identify the SPECIFIC
bias by name, explain its mechanism, and show how it applies to this
particular situation. Different biases require different countermeasures.
```

### Bias Audit Process

1. **Describe the decision**: What is being decided? By whom? Based on what evidence?
2. **Identify potential biases by name**: Which specific biases (confirmation, anchoring, sunk cost, groupthink, overconfidence, availability, etc.) could be influencing this decision?
3. **Find the evidence**: What specific behavior or reasoning pattern indicates the bias?
4. **Assess impact**: How much does this bias affect the decision quality? (High/Med/Low)
5. **Design countermeasures**: What specific debiasing technique addresses each identified bias?

For the full bias catalog (12 biases × mechanism × example) and
debiasing techniques per bias, see [`references/debiasing-protocols.md`](references/debiasing-protocols.md).

## Output Format

```markdown
# Cognitive Bias Audit: {Decision Context}

## Decision Under Review
- Decision: {what is being decided}
- Decision-makers: {who}
- Current leaning: {which way they're leaning}

## Biases Identified
| Bias | Evidence | Impact | Countermeasure |
|------|----------|--------|---------------|
| {name} | {specific behavior/reasoning} | H/M/L | {debiasing technique} |

## Debiased Recommendation
{What the decision looks like after accounting for identified biases}
```

## Examples

### Correct Application
**Scenario:** Company deciding whether to continue a failing product launch (6 months in, NT$5M spent)

| Bias | Evidence | Impact |
|------|----------|--------|
| **Sunk cost** | "We've already invested NT$5M, we can't stop now" | High — past spending is irrecoverable and irrelevant to the forward decision |
| **Overconfidence** | "Our revised forecast shows it will turn around in Q3" — but previous 3 forecasts were also wrong | Medium — team is systematically overestimating success probability |
| **Confirmation** | Team only citing the 2 positive customer reviews while ignoring 50 negative ones | High — selectively filtering information |

**Debiased question**: "If a competitor offered us this product line for free, would we take it?" If the answer is no, the product should be discontinued regardless of sunk costs ✓

### Incorrect Application
- "The team is biased" without specifying which bias → Not actionable. Violates Iron Law: name the specific bias.

## Gotchas

- **Everyone has biases, including you**: The analyst conducting the bias audit is also biased. Use structured processes (checklists, red teams) rather than relying on self-awareness.
- **Bias identification ≠ bias elimination**: Knowing about a bias reduces but does not eliminate its effect. Debiasing requires structural interventions (processes, incentives), not just awareness.
- **Motivated reasoning looks like analysis**: When someone has a preferred outcome, they unconsciously construct logical-sounding arguments for it. Check: did the conclusion come before or after the analysis?
- **False balance**: Not every decision is biased. Sometimes the team's leaning is correct. Don't force-fit biases where they don't exist.
- **Cultural context**: Some biases manifest differently across cultures. Authority bias is stronger in hierarchical cultures. Groupthink manifests differently in collectivist vs individualist settings.

## References

- For behavioral economics applications of biases, see the econ-behavioral skill
- For group decision-making debiasing protocols, see `references/debiasing-protocols.md`
