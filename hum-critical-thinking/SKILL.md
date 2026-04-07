---
name: "hum-critical-thinking"
description: "Apply structured critical thinking — identifying claims, evidence, reasoning chains, hidden assumptions, and logical fallacies — to evaluate or construct specific written arguments rigorously. Use this skill when the user presents a concrete argument, claim, op-ed, research finding, or piece of reasoning to be analyzed for logical validity or flaws, even if they say 'is this argument valid', 'what logical fallacies are in this', or 'what assumptions am I making in this thesis'. Do NOT use for casual plan review, trip planning, project risk brainstorming, or pre-mortems — 'poke holes in my plan' requests are red-team / risk review, not argument analysis."
metadata:
  category: "WP-19 文學院/人文"
  tags: ["humanities", "critical-thinking", "logic", "argumentation"]
---

# Critical Thinking Framework

## Overview

Critical thinking systematically evaluates arguments by decomposing them into claims, evidence, reasoning, and assumptions. It identifies where arguments are strong, weak, or fallacious — not to "win" debates but to arrive at better-justified conclusions.

## Framework

```
IRON LAW: Separate the Argument from the Person

Evaluate the ARGUMENT (claim + evidence + reasoning), not the person
making it. A bad person can make a good argument. A trusted expert
can make a bad argument. Ad hominem (attacking the person) and appeal
to authority (trusting the person) are both fallacies.
```

### Argument Structure

Every argument has four components:
1. **Claim**: What is being asserted? (conclusion)
2. **Evidence**: What facts/data support the claim?
3. **Reasoning**: How does the evidence support the claim? (the logical bridge)
4. **Assumptions**: What unstated premises must be true for the reasoning to hold?

### Evaluation Steps

**Step 1: Identify the claim** — What exactly is being argued? Restate in one sentence.

**Step 2: Examine the evidence**
- Is it factual or anecdotal?
- Is it sufficient (enough data points)?
- Is it relevant (does it actually relate to the claim)?
- Is it current (not outdated)?
- Could the evidence support a different claim?

**Step 3: Evaluate the reasoning**
- Does the evidence logically lead to the claim?
- Are there logical fallacies? (see catalog below)
- Is correlation being mistaken for causation?
- Are there alternative explanations?

**Step 4: Surface assumptions**
- What must be true for this argument to work?
- Are these assumptions reasonable?
- What happens if an assumption is wrong?

### Common Logical Fallacies

| Fallacy | What It Does | Example |
|---------|-------------|---------|
| **Ad hominem** | Attacks the person, not the argument | "You can't talk about economics, you're not an economist" |
| **Straw man** | Distorts the opponent's argument to attack a weaker version | "You want to reduce military spending? So you want us defenseless?" |
| **False dichotomy** | Presents only two options when more exist | "You're either with us or against us" |
| **Slippery slope** | Claims one event will inevitably lead to extreme consequences | "If we allow remote work, soon no one will come to the office ever" |
| **Appeal to authority** | Uses authority status instead of evidence | "The CEO says AI will replace all jobs, so it must be true" |
| **Hasty generalization** | Draws broad conclusion from limited cases | "My two friends who studied art are unemployed, so art degrees are useless" |
| **Red herring** | Introduces irrelevant information to distract | "Yes, our product has bugs, but look at our amazing company culture" |
| **Circular reasoning** | Conclusion is assumed in the premise | "This is the best approach because there's no better one" |

## Output Format

```markdown
# Argument Analysis: {Topic}

## Claim
{One-sentence restatement of the core argument}

## Evidence Assessment
| Evidence | Type | Sufficient? | Relevant? | Current? |
|----------|------|------------|-----------|----------|
| {evidence 1} | {fact/anecdote/expert/stat} | Y/N | Y/N | Y/N |

## Reasoning Evaluation
- Logical validity: {valid / fallacious}
- Fallacies detected: {list with explanation}
- Alternative explanations: {what else could explain the evidence}

## Hidden Assumptions
1. {assumption} — reasonable? {Y/N, why}

## Verdict
- Argument strength: Strong / Moderate / Weak
- Key weakness: {the biggest flaw}
- What would strengthen it: {what evidence or reasoning is missing}
```

## Examples

### Correct Application
**Scenario:** Evaluating the claim "Remote work reduces productivity"
- **Claim**: Remote work reduces productivity
- **Evidence cited**: "Our Q3 output dropped 15% after going remote"
- **Assumption surfaced**: That the output drop was CAUSED by remote work (not by Q3 seasonality, new hires ramping up, product pivot, or pandemic stress)
- **Fallacy**: Post hoc ergo propter hoc (after it, therefore because of it) — correlation assumed to be causation
- **Verdict**: Weak — single data point, confounded by multiple factors, no controlled comparison ✓

### Incorrect Application
- "The CEO said remote work is bad, so the argument must be wrong" → Ad hominem in reverse (dismissing based on who said it). Violates Iron Law: evaluate the argument, not the person.

## Gotchas

- **Strong arguments can have wrong conclusions**: An argument can be logically valid (reasoning follows from premises) but unsound (premises are false). Check both.
- **"I feel" is not evidence**: Emotions are valid as human experiences but not as evidence for factual claims. "I feel unsafe" is a legitimate concern; "I feel this policy doesn't work" is not evidence of policy failure.
- **Burden of proof**: The person making the claim bears the burden of proof. "You can't prove it's wrong" is not evidence that it's right (argument from ignorance).
- **Steelmanning > strawmanning**: Instead of attacking the weakest version of an argument (strawman), construct the STRONGEST version (steelman) and then evaluate it. This produces better analysis.
- **Critical thinking is not cynicism**: The goal is better-justified beliefs, not skepticism of everything. Some arguments are strong. Acknowledging strong arguments is part of critical thinking.

## References

- For formal logic notation and syllogisms, see `references/formal-logic.md`
- For fallacy catalog with extended examples, see `references/fallacy-catalog.md`
