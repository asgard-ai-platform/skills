---
name: "ops-okr-planning"
description: "Design and implement OKR (Objectives and Key Results) for goal-setting and strategic alignment across organizational levels. Use this skill when the user needs to set team or company goals, align departments to strategy, track quarterly progress, or transition from KPI to OKR systems — even if they say 'set our quarterly goals', 'how does OKR work', 'align team goals with company vision', or 'our goals feel disconnected'."
metadata:
  category: "WP-10 通用商業"
  tags: ["business", "okr", "goal-setting", "performance"]
---

# OKR Planning

## Framework

```
IRON LAW: Objectives Are Ambitious, Key Results Are Measurable

Objective: Qualitative, inspiring, directional. "Become the #1 choice
for SMB accounting in Taiwan."

Key Result: Quantitative, measurable, time-bound. "Increase NPS from
32 to 50 by Q4."

If you can't measure it, it's not a Key Result. If it's not ambitious,
it's not an Objective.
```

### OKR vs KPI

| Aspect | OKR | KPI |
|--------|-----|-----|
| Purpose | Drive change, set direction | Monitor ongoing performance |
| Ambition | Stretch goals (70% achievement = success) | Targets (100% achievement expected) |
| Cadence | Quarterly | Ongoing |
| Scope | Strategic priorities (3-5 per level) | Operational metrics (many) |
| Scoring | 0.0 - 1.0 scale | Threshold-based |

### OKR Structure

```
Objective: {Inspiring, qualitative goal}
├── KR1: {Measurable result} — baseline: X → target: Y
├── KR2: {Measurable result} — baseline: X → target: Y
└── KR3: {Measurable result} — baseline: X → target: Y
```

Rules:
- 3-5 Objectives per level (company, team, individual)
- 2-5 Key Results per Objective
- At least one KR should be a leading indicator (not just lagging)
- 70% achievement on stretch goals is the "sweet spot"

### Alignment (Cascading)

```
Company OKR: "Become the market leader in Taiwan SMB accounting"
    ↓
Product Team: "Make onboarding effortless"
  KR: Reduce time-to-first-value from 7 days to 1 day
    ↓
Engineering: "Ship self-serve onboarding flow"
  KR: Launch wizard by March 15, 80% completion rate
```

Each level's OKRs should CONTRIBUTE to the level above, but shouldn't be copy-paste. Teams translate company objectives into their domain.

### OKR Cadence

| Activity | Frequency | Participants |
|----------|-----------|-------------|
| **Set OKRs** | Start of quarter | Leadership + team leads |
| **Weekly check-in** | Weekly (15 min) | Team standup |
| **Mid-quarter review** | Mid-quarter | Team + manager |
| **End-of-quarter scoring** | End of quarter | Everyone |
| **Retrospective** | After scoring | Team |

### Scoring Guide

| Score | Meaning |
|-------|---------|
| 0.0-0.3 | Failed to make meaningful progress |
| 0.4-0.6 | Made progress but fell short |
| 0.7-0.8 | Sweet spot — ambitious goal, strong execution |
| 0.9-1.0 | Either nailed it (great!) or goal wasn't ambitious enough |

## Output Format

```markdown
# OKR Plan: {Team/Company} — {Quarter}

## Company Objectives
### O1: {Objective}
- KR1: {metric} — {baseline} → {target}
- KR2: {metric} — {baseline} → {target}
- KR3: {metric} — {baseline} → {target}

## Team OKRs (aligned to company)
### {Team Name}
#### O1: {Team objective} (supports Company O{N})
- KR1: {metric} — {baseline} → {target}
- KR2: ...

## Check-in Template
| KR | Target | Current | Confidence | Blocker |
|-----|--------|---------|-----------|---------|
| KR1 | {target} | {current} | 🟢/🟡/🔴 | {if any} |
```

## Gotchas

- **OKRs are not a to-do list**: "Launch feature X by March" is a task, not a KR. Reframe as: "Increase user activation rate from 30% to 50%" — the KR measures the OUTCOME, not the output.
- **100% achievement means not ambitious enough**: If every OKR scores 1.0, goals were too easy. Encourage stretch.
- **Don't tie OKRs to compensation directly**: This makes people set safe, achievable goals instead of ambitious ones. Use OKRs for alignment and learning, not bonuses.
- **Start with company OKRs first**: Team OKRs without company OKRs lead to misalignment. Top-down direction, bottom-up input on how to achieve it.
- **3-5 objectives MAX**: More objectives = less focus. If everything is a priority, nothing is.

## References

- For OKR scoring templates, see `references/okr-templates.md`
- For BSC comparison, see the biz-bsc skill
