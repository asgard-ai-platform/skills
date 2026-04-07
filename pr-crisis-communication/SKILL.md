---
name: "pr-crisis-communication"
description: "Manage crisis communication across prevention, response, and recovery phases using SCCT theory and crisis statement frameworks. Use this skill when the user faces a PR crisis, needs to draft a crisis response, plan crisis preparedness, or manage negative public attention — even if they say 'we're getting bad press', 'how do we respond to this scandal', 'draft a public statement', or 'prepare for potential backlash'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["communication", "crisis-management", "pr"]
---

# Crisis Communication

## Framework

```
IRON LAW: Respond in the Golden Hour

The first public response must come within 1 hour of the crisis becoming
public. Silence creates a vacuum that others fill with speculation.
A holding statement ("We are aware and investigating") is better than
no statement. Perfection is the enemy of timeliness.
```

### Three Phases

**1. Prevention** (before crisis)
- Identify potential crises (risk inventory)
- Prepare holding statements and spokesperson training
- Establish a crisis team with clear roles
- Monitor media and social channels

**2. Response** (during crisis)
- Activate crisis team
- Issue holding statement immediately
- Gather facts rapidly
- Issue full statement using 3C framework:
  - **Concern**: Show empathy for affected parties
  - **Commitment**: State what you're doing about it
  - **Control**: Demonstrate you're managing the situation

**3. Recovery** (after crisis)
- Assess damage and lessons learned
- Implement corrective actions
- Rebuild stakeholder trust through actions (not just words)
- Update crisis plan based on learnings

### SCCT (Situational Crisis Communication Theory)

| Crisis Type | Attribution of Blame | Response Strategy |
|------------|---------------------|-------------------|
| **Victim** (natural disaster, rumor) | Low — organization is also a victim | Deny / Diminish |
| **Accidental** (technical error, product defect) | Medium — unintentional | Diminish / Rebuild |
| **Preventable** (human error, organizational failure) | High — could have been avoided | Rebuild (full apology + corrective action) |

### Crisis Statement Template

```
[Concern] We are deeply concerned about [specific situation] and our
thoughts are with [affected parties].

[Facts] Here is what we know: [factual summary, no speculation].

[Commitment] We are taking the following immediate actions:
1. [Action 1]
2. [Action 2]

[Control] We have activated [response team/process] and will provide
updates [frequency and channel].

[Contact] For questions, contact [spokesperson, channel].
```

## Output Format

```markdown
# Crisis Response Plan: {Situation}

## Crisis Assessment
- Type: Victim / Accidental / Preventable
- Severity: Low / Medium / High
- Stakeholders affected: {list}
- Media attention level: {current state}

## Immediate Response (< 1 hour)
- Holding statement: {draft}
- Spokesperson: {who}
- Internal notification: {who needs to know}

## Full Response (< 24 hours)
- Full statement: {draft using 3C framework}
- Key messages (3 max): ...
- Channel strategy: {where to publish}
- Q&A preparation: {anticipated questions + answers}

## Recovery Plan
- Corrective actions: ...
- Trust-rebuilding steps: ...
- Timeline: ...
```

## Gotchas

- **Never lie or speculate**: If you don't know, say "We are investigating." A wrong fact in a crisis statement becomes the next crisis.
- **Social media accelerates everything**: A crisis that would have taken days to develop in 2010 takes hours in 2025. Speed of response must match speed of spread.
- **Internal communication first**: Employees should hear from you before they hear from the media. Issue internal statement before or simultaneously with external.
- **Apology requires specificity**: "We're sorry if anyone was offended" is not an apology. "We apologize for [specific action] that caused [specific harm]" is.
- **Legal vs PR tension**: Legal team wants to say nothing (liability). PR team wants to say everything (trust). The right answer is usually: acknowledge facts, show empathy, commit to action — without admitting legal liability prematurely.

## References

- For social media crisis response playbook, see `references/social-crisis.md`
