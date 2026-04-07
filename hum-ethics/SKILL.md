---
name: "hum-ethics"
description: "Apply ethical frameworks — deontology, utilitarianism, virtue ethics, and justice theory — to analyze moral dilemmas and make principled decisions. Use this skill when the user presents a concrete moral dilemma, a decision with ethical implications, or needs a structured multi-framework ethical analysis, even if they say 'is this the right thing to do', 'what are the ethical implications of this decision', or 'evaluate this dilemma through different ethical lenses'."
metadata:
  category: "WP-19 文學院/人文"
  tags: ["humanities", "ethics", "moral-philosophy", "decision-making"]
---

# Ethical Analysis

## Overview

Ethical analysis applies moral philosophy frameworks to real-world dilemmas. No single framework provides all answers — the value is in examining a situation through multiple ethical lenses and making the tensions explicit.

## Framework

```
IRON LAW: Apply Multiple Frameworks, Not Just One

Different ethical frameworks can reach DIFFERENT conclusions for the same
dilemma. Analyzing through only one lens is incomplete. Apply at least
two frameworks and explicitly compare where they agree and disagree.
The disagreement IS the insight.
```

### Four Major Frameworks

**1. Deontology (Kant)** — Duty-based ethics
- Actions are right or wrong based on rules/duties, regardless of outcomes
- **Categorical Imperative**: Act only according to rules you could will to be universal
- Test: "If everyone did this, would it still work?"
- Strength: Consistent, protects individual rights. Weakness: Rigid, can't handle conflicting duties.

**2. Utilitarianism (Mill, Bentham)** — Consequence-based ethics
- The right action produces the greatest good for the greatest number
- Calculate total benefit minus total harm across all affected parties
- Test: "Does this maximize overall well-being?"
- Strength: Outcome-focused, pragmatic. Weakness: Can justify harming minorities for majority benefit.

**3. Virtue Ethics (Aristotle)** — Character-based ethics
- Focus on what a virtuous person would do, not rules or outcomes
- Core virtues: courage, temperance, justice, prudence, honesty, compassion
- Test: "What would a person of good character do?"
- Strength: Holistic, context-sensitive. Weakness: Subjective, hard to operationalize.

**4. Justice Theory (Rawls)** — Fairness-based ethics
- Decisions should be made as if from behind a "veil of ignorance" — not knowing your own position in society
- Prioritize the least advantaged members of society
- Test: "Would I accept this outcome if I could be anyone affected?"
- Strength: Addresses inequality. Weakness: Impractical for everyday decisions.

### Analysis Steps

1. **State the dilemma**: What is the decision? What are the options?
2. **Identify stakeholders**: Who is affected? How?
3. **Apply each framework**: What does each framework recommend?
4. **Compare recommendations**: Where do they agree? Where do they diverge?
5. **Make the tensions explicit**: What values are in conflict?
6. **Recommend with justification**: Which framework(s) do you weight most, and why?

## Output Format

```markdown
# Ethical Analysis: {Dilemma}

## Dilemma Statement
- Decision: {what must be decided}
- Options: A) {option} B) {option}
- Stakeholders: {who is affected}

## Framework Analysis
| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | A / B | {duty-based reasoning} |
| Utilitarianism | A / B | {consequence calculation} |
| Virtue Ethics | A / B | {character-based reasoning} |
| Justice Theory | A / B | {fairness reasoning} |

## Convergence / Divergence
- Agree on: {where frameworks align}
- Disagree on: {where they diverge and why}
- Core tension: {the fundamental values in conflict}

## Recommendation
{Decision with explicit justification of which values are prioritized and which trade-offs are accepted}
```

## Examples

### Correct Application
**Scenario:** Should a company share user data with law enforcement without a warrant to help catch a criminal?
| Framework | Recommendation | Reasoning |
|-----------|---------------|-----------|
| Deontology | **No** | Users consented to terms that promise privacy. Breaking that promise violates a duty. Universalizing warrant-less sharing would destroy trust in all digital services. |
| Utilitarianism | **Maybe** | Depends on harm calculus: catching one criminal vs eroding privacy for millions. If the crime is serious enough, total utility might favor sharing. |
| Virtue Ethics | **No** | An honest, trustworthy company keeps its promises. A courageous company stands up to government pressure. |
| Justice (Rawls) | **No** | From behind the veil of ignorance, you'd want your data protected — especially if you're in a vulnerable group subject to wrongful surveillance. |

**Convergence**: 3 of 4 frameworks say no. The tension is between public safety (utilitarian) and individual privacy (deontological, rights-based) ✓

### Incorrect Application
- "Utilitarianism says share the data, so share it" → Only one framework applied. Violates Iron Law: apply multiple frameworks.

## Gotchas

- **Ethical analysis ≠ moral judgment**: The goal is to make the reasoning transparent, not to pronounce someone "good" or "bad."
- **Cultural relativity is real but has limits**: Ethical norms vary across cultures, but some principles (don't torture, don't enslave) are widely considered universal. Acknowledge cultural context without falling into full relativism.
- **Utilitarianism is easily abused**: "Greatest good for the greatest number" can justify horrific acts against minorities. Always pair with rights-based analysis.
- **Real dilemmas have no clean answer**: If the answer were obvious, it wouldn't be a dilemma. The value of the analysis is making trade-offs explicit, not finding "the right answer."
- **Stakeholder identification changes the analysis**: Forgetting a stakeholder group (future generations, non-human animals, indirect affected parties) biases the analysis.

## References

- For trolley problem variations and their implications, see `references/trolley-problems.md`
- For business ethics case studies, see `references/business-ethics-cases.md`
