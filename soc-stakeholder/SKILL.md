---
name: "soc-stakeholder"
description: "Conduct stakeholder analysis using identification, Power-Interest matrix classification, and influence strategy development. Use this skill when the user needs to map stakeholders for a project, manage conflicting interests, prioritize communication, or build a stakeholder engagement plan — even if they say 'who needs to approve this', 'how do I get buy-in', or 'who might block this project'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "stakeholder-analysis", "project-management"]
---

# Stakeholder Analysis

## Overview

Stakeholder analysis identifies everyone who affects or is affected by a decision, classifies them by power and interest, and designs engagement strategies for each group. It prevents surprises from forgotten stakeholders and focuses effort on the relationships that matter most.

## Framework

```
IRON LAW: Map ALL Stakeholders Before Engaging Any

Identify the full stakeholder landscape FIRST. Engaging one powerful
stakeholder before understanding the others' positions can create
unintended alliances against you. A stakeholder you forgot to include
becomes your biggest risk.
```

### Power-Interest Matrix

| | Low Interest | High Interest |
|---|---|---|
| **High Power** | **Keep Satisfied** — Monitor, inform proactively, don't bore with details | **Manage Closely** — Active engagement, regular communication, involve in decisions |
| **Low Power** | **Monitor** — Minimal effort, watch for changes in power or interest | **Keep Informed** — Regular updates, address concerns, leverage as advocates |

### Analysis Steps

1. **Identify** all stakeholders (internal and external)
2. **Assess** each on Power (ability to influence outcome) and Interest (degree of concern)
3. **Classify** into the four quadrants
4. **Understand** each stakeholder's position: supportive, neutral, or resistant
5. **Design** engagement strategy per quadrant and position
6. **Monitor** for shifts in power or interest over time

### Engagement Strategies by Position

| Position | Strategy |
|----------|---------|
| **Supporter** | Empower them, give them information to advocate on your behalf |
| **Neutral** | Educate about benefits, reduce perceived risk, address concerns early |
| **Resistant** | Understand their concerns deeply, find common ground, involve in design |

### Conflict Management

When stakeholders have conflicting interests:
1. Identify the specific points of conflict
2. Separate positions (what they say they want) from interests (why they want it)
3. Find solutions that address underlying interests of both parties
4. Escalate only when negotiation fails — and escalate to a stakeholder with power over both

## Output Format

```markdown
# Stakeholder Analysis: {Project/Decision}

## Stakeholder Map
| Stakeholder | Role | Power | Interest | Position | Quadrant |
|-------------|------|-------|----------|----------|----------|
| {name/role} | {relationship} | H/M/L | H/M/L | Support/Neutral/Resist | {strategy} |

## Power-Interest Matrix
| | Low Interest | High Interest |
|---|---|---|
| **High Power** | {names} | {names} |
| **Low Power** | {names} | {names} |

## Engagement Plan
| Stakeholder | Strategy | Frequency | Channel | Key Message |
|-------------|---------|-----------|---------|-------------|
| {name} | {approach} | {weekly/monthly/ad-hoc} | {meeting/email/report} | {tailored message} |

## Conflict Points
| Conflict | Stakeholders | Resolution Approach |
|----------|-------------|-------------------|
| {issue} | {A vs B} | {proposed resolution} |
```

## Examples

### Correct Application
**Scenario:** Stakeholder analysis for implementing a new CRM system at a mid-size company
| Stakeholder | Power | Interest | Position | Strategy |
|-------------|-------|----------|----------|----------|
| CEO | High | Low | Neutral | Keep Satisfied — monthly summary, focus on ROI |
| Sales VP | High | High | Supporter | Manage Closely — co-design, champion role |
| IT Director | High | High | Resistant (worried about integration) | Manage Closely — involve early, address technical concerns |
| Sales reps | Low | High | Resistant (don't want to change tools) | Keep Informed — training, show time savings, address concerns |
| Finance | Medium | Low | Neutral | Monitor — inform about budget when needed |

Key insight: IT Director is high-power + resistant = biggest risk. Address integration concerns before the project gets blocked ✓

### Incorrect Application
- Only mapped internal stakeholders, forgot that the CRM vendor, existing tool vendor (who might resist), and key customers (who'll be affected by the transition) are also stakeholders. Violates Iron Law: map ALL stakeholders.

## Gotchas

- **Power shifts**: A stakeholder who's low-power today may gain power (promotion, organizational change). Reassess quarterly.
- **Hidden stakeholders**: Executive assistants, board members' advisors, union representatives — people with informal but real influence.
- **Don't over-engage low-power stakeholders**: It's tempting to spend time on the most vocal critics, but if they have low power, their resistance won't block you. Focus energy on the high-power quadrants.
- **Resistance ≠ enemy**: Resistant stakeholders often have legitimate concerns. Their input can improve the project. Treat resistance as data, not opposition.
- **Stakeholder fatigue**: Over-communicating with everyone wastes their time and yours. Match communication frequency to the quadrant.

## References

- For negotiation techniques with resistant stakeholders, see `references/negotiation-tactics.md`
