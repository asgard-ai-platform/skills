---
name: "ux-lean-startup"
description: "Apply Lean Startup methodology — Build-Measure-Learn loop, MVP, validated learning, and pivot decisions. Use this skill when the user is launching a new product or startup and needs to validate ideas quickly, design an MVP, decide whether to pivot or persevere, or reduce wasted effort on unvalidated assumptions — even if they say 'should we build this', 'how do we test this idea', 'when should we pivot', or 'we're burning cash with no traction'."
metadata:
  category: "WP-21 設計/資訊/傳播/公衛"
  tags: ["product", "lean-startup", "mvp", "validation"]
---

# Lean Startup

## Framework

```
IRON LAW: Validate Before You Build

Every product decision is a hypothesis. The most expensive way to test
a hypothesis is to build the full product. The cheapest is to test the
riskiest assumption FIRST with the minimum possible effort.

"Build it and they will come" is not a strategy — it's a prayer.
```

### Build-Measure-Learn Loop

1. **Build**: Create the smallest possible thing that tests your riskiest assumption (MVP)
2. **Measure**: Collect data on whether the assumption holds (actionable metrics, not vanity metrics)
3. **Learn**: Did the data validate or invalidate the assumption?
   - Validated → double down, test next assumption
   - Invalidated → pivot (change strategy) or persevere (refine execution)

### MVP Types (Ordered by Effort)

| MVP Type | Effort | What It Tests |
|----------|--------|---------------|
| Landing page | Hours | "Do people want this?" (signup conversion) |
| Explainer video | Days | "Do people understand and desire this?" |
| Concierge | Days | "Can we deliver value manually?" (do it by hand for 10 customers) |
| Wizard of Oz | Weeks | "Does the full experience work?" (fake the backend, real frontend) |
| Single-feature | Weeks | "Does this core feature solve the problem?" |
| Functional prototype | Months | "Can we build this and do users adopt it?" |

### Vanity Metrics vs Actionable Metrics

| Vanity (avoid) | Actionable (use) |
|----------------|-----------------|
| Total signups | Activation rate (% who complete onboarding) |
| Page views | Conversion rate (% who take desired action) |
| Downloads | Retention (% who return after 7/30 days) |
| Total revenue | Revenue per user, LTV:CAC |

### Pivot Triggers

Consider pivoting when:
- Metrics flat after 2-3 iteration cycles
- Customer feedback consistently requests something different than what you're building
- Unit economics don't improve with scale
- The team's enthusiasm has shifted to a different problem

### Pivot Types

| Pivot | What Changes |
|-------|-------------|
| Customer segment | Same product, different target |
| Problem | Same customer, different problem to solve |
| Solution | Same problem, different approach |
| Channel | Same product, different distribution method |
| Revenue model | Same product, different pricing/business model |
| Platform | Single product → platform (or vice versa) |

## Output Format

```markdown
# Lean Startup Plan: {Product/Idea}

## Riskiest Assumption
{The one thing that must be true for this to work}

## MVP Design
- Type: {landing page / concierge / etc.}
- What it tests: {specific assumption}
- Build time: {hours/days/weeks}
- Success metric: {specific threshold}

## Build-Measure-Learn Plan
| Cycle | Build | Measure | Learn |
|-------|-------|---------|-------|
| 1 | {MVP} | {metric + threshold} | Validate/Pivot? |
| 2 | {iteration} | {metric} | ... |

## Pivot/Persevere Criteria
- Persevere if: {specific metric threshold met}
- Pivot if: {specific metric threshold not met after N cycles}
```

## Gotchas

- **MVP ≠ crappy product**: Minimum Viable Product is the minimum needed to LEARN, not the minimum you can get away with shipping. Quality still matters where it affects the test.
- **"Build" doesn't always mean code**: A landing page, a spreadsheet, a manual service — anything that tests the assumption counts.
- **Pivot is not failure**: Pivoting means you learned something valuable. The failure is not pivoting when the data says you should.
- **Lean Startup is for uncertainty**: If you're building a well-understood product in a known market, waterfall may be fine. Lean Startup is for when you don't know what to build or for whom.

## References

- For experiment design templates, see `references/experiment-templates.md`
