---
name: "data-cohort-analysis"
description: "Conduct cohort analysis to track user behavior over time, build retention matrices, and compare cohort performance. Use this skill when the user needs to measure retention, understand how user behavior changes after acquisition, compare product versions' impact on engagement, or predict LTV — even if they say 'what's our retention rate', 'are newer users behaving differently', 'build a retention table', or 'how long do customers stick around'."
metadata:
  category: "WP-04 數據分析"
  tags: ["data-analysis", "cohort", "retention", "product-analytics"]
---

# Cohort Analysis

## Framework

```
IRON LAW: Aggregate Metrics Hide Cohort Differences

A 70% monthly retention rate OVERALL can mask that January cohort retains
at 85% while June cohort retains at 50%. Aggregate metrics blend improving
and deteriorating cohorts together, hiding both problems and progress.
ALWAYS analyze by cohort before drawing conclusions.
```

### Core Concepts

**Cohort**: A group of users who share a common characteristic in a specific time period. Most common: acquisition cohort (grouped by signup month).

**Retention Matrix**: Rows = cohorts (by signup month), Columns = time periods after signup (Month 0, 1, 2...). Cells = % of cohort still active.

```
           Month 0  Month 1  Month 2  Month 3
Jan cohort   100%     65%     48%      40%
Feb cohort   100%     60%     42%      35%
Mar cohort   100%     70%     55%      48%  ← Improvement!
```

### Retention Types

| Type | Definition | Use Case |
|------|-----------|----------|
| **N-day** | % active on exactly day N | Games, daily-use apps |
| **N-day bounded** | % active within first N days | General product usage |
| **Week/Month** | % active in week/month N | SaaS, subscriptions |
| **Unbounded** | % who ever return after day N | Low-frequency products |

### Analysis Steps

**Phase 1: Define Cohort and Activity**
- Cohort definition: signup date, first purchase date, or other milestone
- Activity definition: login, purchase, specific action — must match the product's core value
- Time granularity: daily (for daily-use products), weekly, or monthly

**Phase 2: Build Retention Matrix**
- Group users into cohorts
- For each cohort, calculate retention at each time period
- Visualize as a heatmap (darker = higher retention)

**Phase 3: Identify Patterns**
- **Retention curve shape**: Does it flatten (good — stable core users) or keep declining (bad — everyone eventually churns)?
- **Cohort comparison**: Are newer cohorts retaining better or worse than older ones?
- **Drop-off cliff**: Is there a specific period where retention drops sharply? (e.g., Day 1 → Day 7 drops 50%)

**Phase 4: Connect to Actions**
- What changed for the improving/deteriorating cohorts? (product update, marketing channel shift, onboarding change)
- Can you isolate the cause through A/B test or event analysis?

**Phase 5: LTV Projection**
- Use cohort retention curves to project future revenue per cohort
- LTV = Σ (retention_month_n × ARPU_month_n) for all future months

## Output Format

```markdown
# Cohort Analysis: {Product}

## Cohort Definition
- Cohort: {signup month / first purchase}
- Activity: {what counts as "active"}
- Period: {daily / weekly / monthly}

## Retention Matrix
| Cohort | M0 | M1 | M2 | M3 | M4 | M5 | M6 |
|--------|-----|-----|-----|-----|-----|-----|-----|
| {month} | 100% | {%} | {%} | {%} | {%} | {%} | {%} |

## Key Findings
1. {retention curve shape}
2. {cohort trend — improving or deteriorating}
3. {critical drop-off point}

## Cohort Comparison
| Metric | Oldest Cohort | Newest Cohort | Delta |
|--------|-------------|-------------|-------|
| M1 retention | {%} | {%} | {±pp} |
| M3 retention | {%} | {%} | {±pp} |
| Projected LTV | ${X} | ${X} | {%} |

## Recommendations
1. {action to improve retention at critical drop-off point}
```

## Gotchas

- **Define "active" carefully**: Login ≠ value delivery. A user who logs in but doesn't complete the core action (purchase, send message, create document) shouldn't count as "retained."
- **Cohort size matters**: A cohort of 10 users with 50% retention is meaningless (5 users). Ensure cohorts have statistically meaningful sizes.
- **Survivorship bias in aggregates**: "Average retention is improving" may just mean you have more new users (who are always at M0 = 100%) diluting the denominator.
- **Seasonal cohorts behave differently**: December cohorts (holiday shoppers) often retain worse than March cohorts (organic discovery). Compare same-season cohorts YoY.
- **Retention ≠ engagement depth**: A user who returns once per month but uses for 5 hours vs one who returns daily for 30 seconds — same retention, very different engagement. Layer in activity depth metrics.

## References

- For SQL retention query templates, see `references/retention-sql.md`
- For LTV projection from cohort data, see `references/cohort-ltv.md`
