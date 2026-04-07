---
name: "biz-bsc"
description: "Apply the Balanced Scorecard (BSC) framework to translate strategy into measurable objectives across Financial, Customer, Internal Process, and Learning & Growth perspectives. Use this skill when the user needs to set strategic KPIs, create a strategy map, align organizational goals, or connect daily operations to strategic vision — even if they say 'how do we measure strategy execution' or 'our KPIs feel disconnected'."
metadata:
  category: "WP-13 商學院—策略"
  tags: ["business-strategy", "balanced-scorecard", "performance-management"]
---

# Balanced Scorecard (BSC)

## Overview

The Balanced Scorecard translates strategy into objectives and measures across four perspectives, creating a cause-and-effect chain: Learning & Growth → Internal Processes → Customer → Financial. It answers "are we executing our strategy?" not just "are we profitable?"

## When to Use

**Trigger conditions:**
- User needs to define strategic KPIs beyond financial metrics
- User wants to connect operational activities to strategic goals
- User building a strategy map or performance dashboard
- User says "our KPIs don't reflect our strategy" or "how do we measure execution"

**When NOT to use:**
- For one-time strategic analysis → use SWOT or Porter's
- For project-level OKRs → use OKR framework
- When only financial performance matters (rare)

## Framework

```
IRON LAW: Four Perspectives, Causally Linked

The BSC is NOT four independent lists of KPIs. The four perspectives form
a CAUSAL CHAIN:

  Learning & Growth → Internal Processes → Customer → Financial

Investing in employee skills (L&G) improves process quality (Internal),
which increases customer satisfaction (Customer), which drives revenue (Financial).

If your BSC has no causal links between perspectives, it's just a KPI dump,
not a Balanced Scorecard.
```

```
IRON LAW: Each Objective Gets a Measure, Target, and Initiative

An objective without a measure is a wish.
A measure without a target is a statistic.
A target without an initiative is a hope.

Every BSC objective MUST have all three: measure (how to track), target
(what success looks like), and initiative (what action drives it).
```

### Step 1: Clarify the Strategy

Before building the BSC, state the strategy in one sentence:
- "Grow through customer intimacy" (relationship-driven)
- "Win through operational excellence" (efficiency-driven)
- "Lead through product innovation" (differentiation-driven)

The strategy determines which objectives dominate each perspective.

### Step 2: Define Objectives per Perspective

**Financial** (lagging indicators — outcomes):
- Revenue growth, profitability, cost efficiency, ROI, cash flow
- Question: "What financial results must we deliver to satisfy stakeholders?"

**Customer** (leading indicators for financial):
- Customer satisfaction, retention, acquisition, market share, NPS
- Question: "What must we deliver to customers to achieve financial goals?"

**Internal Processes** (leading indicators for customer):
- Process efficiency, quality, cycle time, innovation pipeline
- Question: "What processes must we excel at to satisfy customers?"

**Learning & Growth** (foundation — enablers):
- Employee skills, culture, technology infrastructure, knowledge management
- Question: "What capabilities must we build to improve our processes?"

### Step 3: Build the Strategy Map

Draw cause-and-effect arrows linking objectives across perspectives:

```
[L&G] Train sales team on consultative selling
  ↓
[Internal] Reduce sales cycle from 60 to 30 days
  ↓
[Customer] Increase customer satisfaction score to 4.5/5
  ↓
[Financial] Grow revenue 20% YoY
```

Every objective should connect to at least one objective in another perspective. Orphan objectives indicate a gap in strategic logic.

### Step 4: Assign Measures, Targets, and Initiatives

For each objective, define:
- **Measure**: Specific metric (quantitative preferred)
- **Target**: Concrete threshold with timeframe
- **Initiative**: Action or project that drives the metric

## Output Format

```markdown
# Balanced Scorecard: {Organization}

## Strategy Statement
{One-sentence strategy}

## Strategy Map

{L&G objectives} → {Internal Process objectives} → {Customer objectives} → {Financial objectives}

## Scorecard

### Financial Perspective
| Objective | Measure | Target | Initiative |
|-----------|---------|--------|-----------|
| {objective} | {metric} | {value by when} | {action} |

### Customer Perspective
| Objective | Measure | Target | Initiative |
|-----------|---------|--------|-----------|
| {objective} | {metric} | {value by when} | {action} |

### Internal Process Perspective
| Objective | Measure | Target | Initiative |
|-----------|---------|--------|-----------|
| {objective} | {metric} | {value by when} | {action} |

### Learning & Growth Perspective
| Objective | Measure | Target | Initiative |
|-----------|---------|--------|-----------|
| {objective} | {metric} | {value by when} | {action} |

## Causal Chain Validation
{Explain how L&G → Internal → Customer → Financial links work}
```

## Examples

### Correct Application

**Scenario:** BSC for a B2B SaaS company with strategy: "Grow through product-led growth"

| Perspective | Objective | Measure | Target | Initiative |
|------------|-----------|---------|--------|-----------|
| Financial | Increase ARR | Annual Recurring Revenue | $10M by Q4 | Expand pricing tiers |
| Customer | Improve retention | Net Revenue Retention | >110% | Launch customer success program |
| Internal | Accelerate feature delivery | Release cycle time | 2 weeks (from 6) | Adopt CI/CD pipeline |
| L&G | Build product analytics capability | % team trained on Mixpanel | 100% by Q2 | Product analytics bootcamp |

**Causal chain**: Analytics training (L&G) → faster, data-driven releases (Internal) → higher retention from better product (Customer) → ARR growth (Financial) ✓

### Incorrect Application

**What went wrong:**
- Listed 15 KPIs with no causal links → KPI dump, not a BSC. Violates Iron Law: perspectives must be causally linked.
- Financial: "Revenue $10M" with no measure, target timeframe, or initiative → Violates Iron Law: need measure + target + initiative.

## Gotchas

- **Too many objectives**: 3-5 per perspective is ideal. More than 5 loses focus. The BSC is about strategic priorities, not a comprehensive KPI list.
- **All lagging indicators**: If every measure is a lagging indicator (revenue, satisfaction score), you can't manage proactively. Balance with leading indicators (training hours, pipeline quality).
- **L&G as an afterthought**: Teams fill Financial and Customer easily but struggle with L&G. This perspective is the foundation — skip it and the whole chain breaks.
- **Cascading confusion**: A corporate BSC and a department BSC should be linked but not identical. Department objectives should contribute to corporate objectives, not copy them.
- **BSC ≠ OKR**: BSC is a strategic management system (4 perspectives, causal links, strategy map). OKR is a goal-setting framework (objectives + key results). They can coexist but serve different purposes.

## References

- For Strategy Map templates and examples, see `references/strategy-maps.md`
- For comparison with OKR and other performance frameworks, see `references/framework-comparison.md`
