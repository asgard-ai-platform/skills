---
name: "pr-crisis-response"
description: "Manage PR crises using classification, golden hour response, crisis statement templates (3C framework), and reputation recovery planning. Use this skill when the user faces negative media coverage, a viral complaint, product safety issues, executive misconduct, or any situation threatening brand reputation — even if they say 'we're getting destroyed on social media', 'draft a response to this article', 'how do we handle this PR disaster', or 'prepare for potential backlash'."
metadata:
  category: "WP-02 品牌公關"
  tags: ["pr", "crisis-management", "reputation", "communication"]
---

# PR Crisis Management

## Framework

```
IRON LAW: First Response Within 1 Hour

The first hour after a crisis becomes public is the "golden hour."
Silence in this window = others control the narrative. A holding
statement ("We are aware of [issue] and are investigating. We will
provide an update by [time].") is infinitely better than silence.
```

### Crisis Classification

| Level | Description | Examples | Response |
|-------|-----------|---------|----------|
| **Level 1: Noise** | Minor complaint, limited reach | Single negative review, individual social post | Monitor, respond if needed |
| **Level 2: Issue** | Growing attention, media interest possible | Multiple complaints on same topic, minor influencer post | Proactive response, prepare statement |
| **Level 3: Crisis** | Widespread media coverage, significant reputation damage | Product recall, data breach, viral scandal, executive misconduct | Full crisis protocol, C-suite involvement |

### Crisis Response Protocol

**Hour 1: Contain**
1. Activate crisis team (PR, Legal, CEO, relevant department head)
2. Issue holding statement (acknowledge, don't speculate)
3. Secure all internal communications (no unauthorized statements)
4. Begin fact-gathering

**Hours 2-6: Respond**
1. Draft full statement using 3C framework
2. Legal review (balance transparency with liability)
3. Publish on owned channels first, then distribute to media
4. Brief customer-facing teams (CS, sales) with talking points

**Days 1-7: Manage**
1. Monitor media reaction to response
2. Issue updates as new information emerges
3. Respond to media inquiries consistently
4. Address social media individually where appropriate

**Weeks 2-4: Recover**
1. Implement corrective actions (not just promises)
2. Communicate actions taken
3. Re-engage positive narratives
4. Post-mortem: what happened, why, how to prevent

### 3C Crisis Statement Framework

```
[CONCERN] We are deeply concerned about [specific situation].
Our thoughts are with [affected parties].

[COMMITMENT] We are taking immediate action:
1. [Specific action 1]
2. [Specific action 2]
3. [Investigation/review underway]

[CONTROL] We have [crisis team/process] in place. We will provide
updates [when and where]. For questions: [contact info].
```

### What NOT to Say

| Don't | Why | Instead |
|-------|-----|---------|
| "No comment" | Implies guilt or indifference | "We are investigating and will share findings" |
| "We're sorry IF anyone was offended" | Non-apology, dismissive | "We apologize for [specific thing]" |
| Blame others | Looks defensive | Take responsibility for your part |
| Speculate | May be wrong, creates new problems | "Here is what we know so far" |
| Minimize | Alienates affected people | Acknowledge the seriousness |

## Output Format

```markdown
# Crisis Response: {Situation}

## Classification
- Level: 1 (Noise) / 2 (Issue) / 3 (Crisis)
- Type: Product / Personnel / Operational / External
- Current media coverage: {scope}

## Holding Statement (< 1 hour)
{Draft}

## Full Statement (< 6 hours)
{3C framework draft}

## Talking Points (for CS/Sales)
1. {key message}
2. {key message}
3. {redirect: "For further questions, please contact [PR]"}

## Anticipated Questions & Answers
| Question | Answer |
|----------|--------|
| {likely question} | {prepared answer} |

## Recovery Plan
1. {corrective action + timeline}
```

## Gotchas

- **Speed vs accuracy trade-off**: In hour 1, prioritize speed with a holding statement. In hours 2-6, prioritize accuracy with the full statement. Never sacrifice accuracy for speed in the full statement.
- **Social media crises escalate in minutes**: A viral TikTok or PTT post can reach millions before your crisis team assembles. Pre-written holding statements for common scenarios save critical minutes.
- **Internal leaks are the second crisis**: Employees sharing internal discussions on social media compounds the problem. Brief all staff: "All external communication goes through PR."
- **Taiwan media cycle**: Taiwan's 24-hour news channels (TVBS, SET, CTV) and online outlets (ETtoday, UDN) amplify stories rapidly. The PTT → news outlet pipeline means a PTT hot post becomes TV news within hours.
- **Apology culture varies**: In Taiwan/Japan, a sincere public apology (including bowing) is expected and effective. In the US, apologies are often viewed as liability admission. Calibrate to cultural context.

## References

- For social media crisis playbook, see `references/social-crisis.md`
- For post-crisis reputation rebuilding, see `references/reputation-recovery.md`
