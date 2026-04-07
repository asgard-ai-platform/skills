---
name: "ux-jtbd"
description: "Apply Jobs to Be Done (JTBD) framework to understand customer motivation through functional, emotional, and social jobs. Use this skill when the user needs to understand why customers hire or fire a product, discover unmet needs, write job stories, or reframe product strategy around customer outcomes — even if they say 'why do customers buy this', 'what need does this serve', or 'customers aren't using our product as intended'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["product", "jtbd", "jobs-to-be-done", "customer-insight"]
---

# Jobs to Be Done (JTBD)

## Overview

JTBD reframes product strategy around the "job" customers are trying to accomplish. People don't buy products — they "hire" them to make progress in a specific situation. Understanding the job reveals the real competition (which is often not who you think) and unmet needs.

## Framework

```
IRON LAW: The Job Is About the Customer's Progress, Not Your Product

"Help me manage my tasks" is a job. "Use our task management app" is not.
The job exists independently of any solution. Your product is ONE way
to fulfill the job — customers can "hire" a spreadsheet, a notebook,
or a whiteboard for the same job.

Define jobs from the CUSTOMER's perspective, never from the product's.
```

### Three Dimensions of a Job

| Dimension | What It Means | Example (morning coffee) |
|-----------|-------------|------------------------|
| **Functional** | The practical task to accomplish | "Get caffeine to be alert for work" |
| **Emotional** | How they want to feel | "Feel like I'm treating myself, not just surviving" |
| **Social** | How they want to be perceived | "Show colleagues I have good taste (specialty coffee)" |

### Job Story Format

Replace user stories with job stories:

```
When [situation/trigger],
I want to [motivation/job],
so I can [expected outcome].
```

Example: "When I'm rushing to work and haven't had breakfast, I want a quick energy boost that doesn't feel unhealthy, so I can start my morning focused and not guilty about my diet."

### Analysis Steps

1. **Identify the situation/trigger**: What circumstance creates the need?
2. **Uncover the job**: What progress is the customer trying to make?
3. **Map all three dimensions**: Functional + emotional + social
4. **Identify current "hires"**: What do they currently use to do this job?
5. **Find forces of progress**: Push (dissatisfaction with current) + Pull (attraction of new) vs Anxiety (fear of new) + Habit (comfort of current)
6. **Discover unmet needs**: Where do current solutions fall short?

### Forces of Progress (Switch)

```
PUSH (away from current) + PULL (toward new) > ANXIETY (about new) + HABIT (of current)
= Customer switches
```

Understanding these four forces explains why customers switch (or don't).

## Output Format

```markdown
# JTBD Analysis: {Product/Category}

## The Job
When [situation], I want to [job], so I can [outcome].

## Three Dimensions
- Functional: {practical need}
- Emotional: {desired feeling}
- Social: {desired perception}

## Current Hires (Competition)
| Solution | What Job It Does | Where It Falls Short |
|----------|-----------------|---------------------|
| {product/workaround} | {what need it serves} | {unmet need} |

## Forces of Progress
- Push: {what's driving them away from current solutions}
- Pull: {what attracts them to new solutions}
- Anxiety: {what holds them back from switching}
- Habit: {what keeps them using current solutions}

## Unmet Needs & Opportunities
1. {unmet need} → {opportunity}
```

## Examples

### Correct Application
**Scenario:** JTBD for Airbnb

**The Job**: "When I'm planning a trip and want a local experience, I want to stay in a real neighborhood, so I can feel like I belong there rather than being a tourist."

**Real competition**: Not just hotels — also hostels, staying with friends, and even NOT traveling (because hotels feel too "touristy" to be worth it). Airbnb's real competition for this job includes anything that provides "local belonging experience" ✓

### Incorrect Application
- "The job is to use our app" → Product-centric, not customer-centric. Violates Iron Law.

## Gotchas

- **Jobs are stable, solutions change**: "Get from A to B quickly" has been the same job for centuries. Solutions changed from horses to cars to ride-sharing. Design for the job, not the current solution.
- **One product can serve multiple jobs**: Coffee is hired for "wake up" (morning), "social bonding" (café meeting), and "productive break" (afternoon slump). Different situations, different jobs, different competitors.
- **Don't confuse needs with solutions**: "I need a faster horse" is a solution. "I need to get there faster" is a need. Dig deeper.
- **Emotional and social jobs are often more important than functional**: People buy premium coffee not just for caffeine (functional) but for self-care (emotional) and status (social).

## References

- For switch interview methodology, see `references/switch-interviews.md`
