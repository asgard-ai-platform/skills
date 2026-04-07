---
name: "hum-historical-analogy"
description: "Use historical analogies to inform strategic decisions by identifying structural similarities and differences between past and present situations. Use this skill when the user draws on historical precedent to justify a strategy, needs to evaluate whether a historical comparison is valid, or wants to learn from past events — even if they say 'this is like the dotcom bubble', 'history repeats itself', or 'what can we learn from how X handled this'."
metadata:
  category: "WP-19 文學院/人文"
  tags: ["humanities", "historical-analogy", "strategic-thinking"]
---

# Historical Analogy

## Overview

Historical analogies apply lessons from past events to current decisions. When used rigorously, they provide pattern recognition and foresight. When used carelessly, they mislead by overfitting superficial similarities and ignoring structural differences.

## Framework

```
IRON LAW: Structural Similarity, Not Surface Similarity

A valid analogy requires shared STRUCTURAL features (causal mechanisms,
power dynamics, systemic patterns), not just surface resemblance.

"This startup is the next Apple" because the founder wears turtlenecks =
surface similarity (worthless). "This market has the same demand-side
network effects as early smartphone adoption" = structural similarity (useful).
```

### Analogy Evaluation Steps

1. **State the analogy explicitly**: "Situation A is like historical event B because..."
2. **Map structural similarities**: What causal mechanisms, dynamics, or patterns are shared?
3. **Map structural differences**: What is fundamentally different?
4. **Assess the balance**: Do similarities outweigh differences for the specific question at hand?
5. **Extract lessons carefully**: What specific, actionable insight does the analogy provide?
6. **Identify the analogy's limits**: Where does the analogy break down?

### Common Analogy Traps

| Trap | Description | Example |
|------|-----------|---------|
| **Cherry-picking** | Selecting only the historical case that supports your conclusion | "Kodak failed to adapt, so we must pivot" (ignoring cases where staying the course was right) |
| **Outcome bias** | Using the historical outcome to validate the analogy | "Amazon survived the dotcom bust, so we will too" (survivorship bias) |
| **False precision** | Expecting history to repeat exactly | "The 2008 crisis took 18 months to recover, so this one will too" |
| **Presentism** | Judging past decisions by present knowledge | "They should have seen the crisis coming" (they didn't have today's data) |

## Output Format

```markdown
# Historical Analogy Assessment: {Current Situation} ↔ {Historical Event}

## The Analogy
"{Current situation} is like {historical event} because..."

## Structural Similarities
| Feature | Historical | Current | Similarity |
|---------|-----------|---------|-----------|
| {mechanism} | {how it worked then} | {how it works now} | Strong/Moderate/Weak |

## Structural Differences
| Feature | Historical | Current | Impact on Analogy |
|---------|-----------|---------|------------------|
| {factor} | {then} | {now} | Weakens/Neutral/Strengthens |

## Validity Assessment
- Overall analogy strength: Strong / Moderate / Weak
- Valid for: {what aspects of the decision the analogy informs}
- Invalid for: {where the analogy breaks down}

## Lessons (with caveats)
1. {lesson} — caveat: {where this might not apply}
```

## Examples

### Correct Application
**Scenario:** "AI in 2025 is like the Internet in 1995"

| Structural Similarity | Internet 1995 | AI 2025 | Strength |
|----------------------|---------------|---------|----------|
| General-purpose technology enabling many applications | ✓ | ✓ | Strong |
| Early hype cycle with inflated expectations | ✓ (dotcom) | ✓ (AI bubble concerns) | Strong |
| Infrastructure buildout phase (broadband then, GPU/data centers now) | ✓ | ✓ | Strong |

| Structural Difference | Internet 1995 | AI 2025 | Impact |
|----------------------|---------------|---------|--------|
| Deployment speed | Years for broadband rollout | AI accessible via API in minutes | Weakens (faster adoption) |
| Incumbent response | Incumbents slow to respond (Blockbuster, newspapers) | Incumbents adopting aggressively (Microsoft, Google) | Weakens (harder for startups) |
| Regulatory environment | Minimal regulation | Active AI regulation globally (EU AI Act) | Weakens (more constraints) |

**Verdict**: Moderate analogy — valid for understanding the hype cycle pattern and infrastructure investment phase, but invalid for predicting startup vs incumbent dynamics ✓

### Incorrect Application
- "AI is like the Internet, so all AI companies will succeed" → Cherry-picks the winners (Google, Amazon) and ignores that 90%+ of dotcom companies failed. Survivorship bias + surface similarity only. Violates Iron Law.

## Gotchas

- **Multiple analogies exist**: For any current situation, multiple historical parallels can be drawn — and they may suggest opposite conclusions. Consider 2-3 analogies, not just the most popular one.
- **The most popular analogy is often the worst**: "This is like the dotcom bubble" is thrown around because it's familiar, not because the structural similarities are strong. Popularity ≠ validity.
- **Analogies work best for pattern recognition, not prediction**: "This pattern has led to X before" is useful. "This will lead to X again" is overconfident.
- **Cultural and institutional context changes**: Lessons from US business history may not apply to Taiwan's institutional environment. Account for systemic differences.

## References

- For Neustadt & May's "Thinking in Time" methodology, see `references/thinking-in-time.md`
