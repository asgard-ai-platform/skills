---
name: "hum-socratic"
description: "Apply Socratic questioning — systematic inquiry via clarification, assumption-probing, evidence-testing, perspective-shifting, implication-tracing, and meta-questions — to coach learning or surface hidden assumptions in a person's reasoning. Use this skill when the user is explicitly facilitating learning, coaching a person through their own thinking, or needs a structured questioning sequence to probe a held belief, even if they say 'play devil's advocate on this claim' or 'how should I coach my team through this problem via questions'. Do NOT use for open-ended brainstorming, information gathering, or requirements-discovery question lists where no belief is being probed."
metadata:
  category: "WP-19 文學院/人文"
  tags: ["humanities", "socratic-method", "questioning", "pedagogy"]
---

# Socratic Questioning

## Overview

The Socratic method uses disciplined questioning to examine ideas, uncover assumptions, and develop deeper understanding. Instead of providing answers, it guides the thinker to discover insights through their own reasoning — making conclusions more durable and personally meaningful.

## Framework

```
IRON LAW: More Than 3 Consecutive Questions Without Summary Produces
Confusion, Not Insight

Agents applying Socratic questioning default to an unbounded chain of
questions. After ~3 questions, the thinker loses the thread — they can't
hold the question hierarchy in working memory. Pause every 2-3 questions
to SUMMARIZE what the thinker has revealed so far ("So your position is X
because Y, but you're unsure about Z — is that right?"). Then resume.
Without this checkpoint, the session feels like an interrogation, not a
guided inquiry.

Also: never ask a question whose answer you already embedded in the
phrasing. "Don't you think X is problematic?" is a leading assertion
disguised as a question. Rephrase as "What are the consequences of X?"
```

### Facilitation Flow

1. **Clarify** the thinker's claim precisely
2. **Probe assumptions** — what must be true for the claim to hold?
3. **Request evidence** — what supports the belief? Is it sufficient?
4. **Introduce counter-perspectives** — what would a critic say?
5. **Explore implications** — if right, what follows? If wrong, what changes?
6. **Synthesize** (the IRON LAW checkpoint) — summarize, confirm understanding, then continue

For the six question types (clarification, assumptions, evidence, perspectives, implications, meta-questions) and scaffolding techniques (maieutics), see [`references/facilitation-guide.md`](references/facilitation-guide.md).

## Output Format

When applying Socratic questioning, output a structured question sequence:

```markdown
# Socratic Inquiry: {Topic}

## Starting Position
{The thinker's current belief or question}

## Question Sequence
1. [Clarification] {question}
   → Expected insight: {what this reveals}
2. [Assumption] {question}
   → Expected insight: {what this surfaces}
3. [Evidence] {question}
   → Expected insight: ...
4. [Perspective] {question}
   → Expected insight: ...
5. [Implication] {question}
   → Expected insight: ...

## Target Insight
{What the thinker should arrive at through this sequence}
```

## Examples

### Correct Application
**Scenario:** Student says "AI will replace all jobs"

**Socratic sequence:**
1. [Clarification] "When you say 'all jobs', do you mean literally every job, or most jobs?"
2. [Evidence] "What evidence have you seen that suggests this?"
3. [Assumption] "What are you assuming about AI's capabilities? Are there tasks that require something AI can't do?"
4. [Perspective] "Historically, what happened to employment after previous technological revolutions like the Industrial Revolution?"
5. [Implication] "If AI replaced all jobs, how would people earn money to buy the things AI produces?"

→ The student arrives at a more nuanced view: AI will transform jobs, not eliminate all of them ✓

### Incorrect Application
- Student: "AI will replace all jobs" → Teacher: "No it won't. Here's why..." → Provided the answer directly. Not Socratic. Violates Iron Law.

## Gotchas

- **Socratic method can feel adversarial**: Frame questions with genuine curiosity, not as cross-examination. "I'm curious about..." softens the tone.
- **Know when to stop**: If the thinker is frustrated or going in circles, provide a hint or redirect. The method serves learning, not ego.
- **Not all contexts suit Socratic questioning**: Emergency decisions, time-sensitive situations, and purely factual questions ("what's the capital of France?") don't benefit from Socratic inquiry.
- **The facilitator must actually listen**: The next question should respond to what the thinker said, not follow a predetermined script. Flexibility is essential.
- **Cultural sensitivity**: In some cultures, questioning authority or being questioned publicly is uncomfortable. Adapt the setting (one-on-one, written) and framing.

## References

- For classroom facilitation techniques, see `references/facilitation-guide.md`
