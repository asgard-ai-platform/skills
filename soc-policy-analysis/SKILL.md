---
name: "soc-policy-analysis"
description: "Conduct structured policy analysis including problem definition, alternative evaluation, and evidence-based recommendation. Use this skill when the user needs to evaluate policy options, compare interventions, assess regulatory impact, or make public sector recommendations — even if they say 'which policy should we adopt', 'what's the best approach to this public problem', or 'evaluate these policy alternatives'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "policy-analysis", "public-policy"]
---

# Policy Analysis

## Overview

Policy analysis is a systematic method for evaluating alternative courses of action to address public problems. It follows a structured process: define the problem → identify alternatives → establish criteria → evaluate → recommend. It applies to government policy, corporate policy, and organizational decision-making.

## Framework

```
IRON LAW: Problem Definition Determines Everything

How you define the problem determines which solutions are considered.
"Traffic congestion" suggests road-building. "Excessive car dependency"
suggests public transit. "Inefficient land use" suggests zoning reform.

The same observable situation can be framed as different problems,
leading to completely different policy responses. Make the framing
explicit and examine alternatives.
```

### The Six Steps

**1. Define the Problem**
- What is the problem? (observable evidence, not just symptoms)
- Who is affected? How severely?
- What causes it? (root cause, not proximate cause)
- How is the problem framed? Are there alternative framings?

**2. Identify Alternatives**
- Status quo (do nothing — always include as baseline)
- Incremental options (modify existing policy)
- Transformative options (fundamentally new approach)
- Aim for 3-5 genuine alternatives, not strawmen

**3. Establish Evaluation Criteria**
Common criteria:
| Criterion | Question |
|-----------|---------|
| **Effectiveness** | Does it solve the problem? |
| **Efficiency** | Benefit relative to cost? |
| **Equity** | Who bears the costs? Who gets the benefits? |
| **Feasibility** | Political, administrative, and technical viability? |
| **Sustainability** | Can it be maintained long-term? |

**4. Evaluate Alternatives**
Score each alternative against each criterion. Use evidence (data, case studies, research) wherever possible. Acknowledge uncertainty.

**5. Recommend**
Select the alternative with the best overall profile. Justify the trade-offs explicitly — no alternative will score highest on every criterion.

**6. Implementation Considerations**
- Political feasibility: Who needs to approve? Who might oppose?
- Administrative capacity: Can existing institutions implement this?
- Timeline and phasing
- Monitoring and evaluation plan

## Output Format

```markdown
# Policy Analysis: {Problem}

## Problem Definition
- Problem: {description}
- Affected population: {who}
- Root cause: {analysis}
- Alternative framings: {other ways to define this problem}

## Alternatives
1. Status quo
2. {Option A}
3. {Option B}
4. {Option C}

## Evaluation Matrix
| Criterion | Status Quo | Option A | Option B | Option C |
|-----------|-----------|----------|----------|----------|
| Effectiveness | L/M/H | L/M/H | L/M/H | L/M/H |
| Efficiency | L/M/H | ... | ... | ... |
| Equity | L/M/H | ... | ... | ... |
| Feasibility | L/M/H | ... | ... | ... |

## Recommendation
**{Selected option}** — {justification including trade-off acknowledgment}

## Implementation Plan
- Political path: {approval process}
- Timeline: {phases}
- Monitoring: {how to measure success}
```

## Examples

### Correct Application
**Scenario:** Policy analysis for reducing food delivery rider injuries in Taipei
- **Problem**: 45% increase in delivery rider traffic injuries (2023-2024)
- **Alternatives**: (1) Status quo, (2) Mandatory insurance + training, (3) Speed limits on delivery apps during peak hours, (4) Platform liability for rider injuries
- **Evaluation**: Option 2 scores highest on feasibility (incremental) and effectiveness (directly addresses risk); Option 4 is most effective but politically difficult (platform lobbying)
- **Recommendation**: Option 2 as immediate action, with Option 4 as medium-term legislative goal ✓

### Incorrect Application
- "The problem is delivery riders drive too fast" → Symptom, not root cause. WHY do they drive fast? Because platform algorithms reward speed, per-delivery pay incentivizes rushing, and there's no penalty for unsafe driving. Different root causes lead to different solutions. Violates Iron Law: problem definition determines everything.

## Gotchas

- **Always include status quo**: "Do nothing" is a valid option and the baseline for comparison. Sometimes it's the best option if alternatives are worse.
- **Avoid strawman alternatives**: Including obviously bad options to make your preferred option look good is intellectually dishonest. All alternatives should be genuine.
- **Equity is often traded for efficiency**: Policies that are most efficient often have unequal distributional impacts. Make this trade-off explicit.
- **Implementation kills good policy**: A brilliant policy that can't be implemented is worthless. Feasibility is not a secondary criterion — it's a prerequisite.
- **Evidence hierarchy**: RCTs > quasi-experiments > case studies > expert opinion > anecdote. Use the strongest evidence available, and be explicit about evidence quality.

## References

- For cost-benefit analysis methodology, see `references/cost-benefit.md`
- For evidence-based policy frameworks, see `references/evidence-hierarchy.md`
