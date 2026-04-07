---
name: "soc-user-research"
description: "Design and conduct user research using interviews, focus groups, surveys, and field observation. Use this skill when the user needs to understand customer needs, validate product assumptions, gather qualitative insights, or design a research study — even if they say 'we need to talk to users', 'how do we validate this idea', or 'what do our customers actually think'."
metadata:
  category: "WP-18 社會科學院"
  tags: ["social-science", "user-research", "qualitative-methods"]
---

# User Research Methods

## Overview

User research uncovers what people need, want, and do — through direct observation and conversation, not assumptions. This skill covers four core methods: depth interviews, focus groups, surveys, and field observation, plus when to use each.

## Framework

```
IRON LAW: Method Follows Question

Choose the method based on what you need to learn, not what's convenient.
"Why" questions → Interviews/Observation (qualitative)
"How many" questions → Surveys (quantitative)
"What do they really do" → Observation (behavioral)

Running a survey to answer "why" produces misleading data.
```

### Method Selection

| Method | Best For | Sample | Depth | Cost |
|--------|---------|--------|-------|------|
| **Depth Interview** | Understanding motivations, pain points, mental models | 8-15 people | Very high | Medium |
| **Focus Group** | Exploring reactions, generating ideas, social dynamics | 6-10 per group, 2-3 groups | Medium | Medium |
| **Survey** | Measuring prevalence, preferences, demographics at scale | 100+ responses | Low | Low-Med |
| **Field Observation** | Understanding actual behavior in context (not self-reported) | 5-10 sessions | Very high | High |

### Depth Interview Guide

1. **Warm-up**: Build rapport (2 min) — "Tell me about your role/day"
2. **Context**: Understand their world (5 min) — "Walk me through the last time you..."
3. **Core questions**: Explore the topic (20 min) — Open-ended, no leading questions
4. **Probing**: Go deeper on interesting threads — "Tell me more about that", "Why?"
5. **Wrap-up**: Summarize and confirm (3 min) — "Did I understand correctly that...?"

**Rules**:
- Ask about past behavior, not hypothetical future ("What did you do?" not "What would you do?")
- Never ask "Would you use this?" — people are terrible at predicting their own behavior
- Silence is a tool — let them fill the gap

### Survey Design

1. Start with screening questions (qualify respondents)
2. Move from general to specific
3. Put sensitive/demographic questions last
4. Limit to 15-20 questions (5-7 min completion)
5. Use validated scales where possible (Likert, NPS, SUS)

**Question types to avoid**:
- Double-barreled: "Is the product fast and reliable?" (which one?)
- Leading: "Don't you think our app is easy to use?"
- Hypothetical: "Would you pay $10/month for this feature?"

### Analysis

**Qualitative** (interviews, observation):
- Affinity mapping: Group observations into themes
- Look for patterns across 5+ participants
- Quote verbatim — don't paraphrase

**Quantitative** (surveys):
- Descriptive stats first (means, distributions)
- Cross-tabulate by segments
- Statistical significance for comparisons (p < 0.05)

## Output Format

```markdown
# User Research Plan: {Project}

## Research Questions
1. {what we need to learn}

## Method
- Type: {interview / focus group / survey / observation}
- Rationale: {why this method for this question}
- Sample: {who, how many, recruitment criteria}
- Timeline: {duration}

## Discussion Guide / Survey Instrument
{Key questions or survey structure}

## Analysis Plan
{How findings will be synthesized}
```

## Examples

### Correct Application
**Scenario:** Understanding why users abandon a food delivery app at checkout
- **Method**: Depth interviews (need to understand "why", not "how many")
- **Sample**: 10 users who abandoned in the last 30 days (recruit via in-app data)
- **Key question**: "Walk me through your last order that you didn't complete. What happened?" (behavioral, past-tense, open-ended ✓)

### Incorrect Application
- Survey asking "Would you complete your order if we removed the delivery fee?" → Hypothetical. Users will say yes but behavior may not change. Should observe actual behavior or test with a real experiment.

## Gotchas

- **5 users find 85% of usability problems** (Nielsen): For usability testing, diminishing returns after 5. For understanding motivations, need 8-15.
- **Self-reported behavior ≠ actual behavior**: People overestimate how healthy they eat, how often they exercise, and how much they'd pay. Observation and behavioral data > self-report.
- **Recruitment bias**: If you recruit "users of our app", you miss non-users and churned users. Define the population carefully.
- **Interviewer bias**: The interviewer's reactions (nodding, "great!") influence responses. Stay neutral.
- **Surveys measure what you ask, not what matters**: If you didn't think to ask about a pain point, the survey won't reveal it. Use qualitative research first to discover the right questions.

## References

- For interview script templates, see `references/interview-templates.md`
- For survey design best practices, see `references/survey-design.md`
