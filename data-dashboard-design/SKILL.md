---
name: "data-dashboard-design"
description: "Design effective data dashboards with proper KPI hierarchy, chart type selection, and interactive features. Use this skill when the user needs to create a dashboard, choose the right visualizations, organize metrics for different audiences, or evaluate dashboard tools — even if they say 'build a dashboard', 'our reports are confusing', 'which chart should I use', or 'executives can't find the metrics they need'."
metadata:
  category: "WP-04 數據分析"
  tags: ["data-analysis", "dashboard", "visualization", "bi"]
---

# Dashboard Design

## Framework

```
IRON LAW: One Dashboard, One Audience, One Purpose

A dashboard that tries to serve the CEO, the marketing team, AND the
engineers will serve none of them well. Each audience has different
questions, different metrics, and different time horizons.

CEO: "Are we growing?" → North Star + revenue + key trends
Marketing: "Which campaigns work?" → CAC, ROAS, conversion by channel
Engineering: "Is the system healthy?" → Latency, error rate, uptime
```

### KPI Hierarchy (Pyramid Structure)

```
          [North Star Metric]
         /                    \
    [L1: 3-5 Business KPIs]
       /         |         \
  [L2: Driving Metrics per KPI]
     /     |     |     |     \
[L3: Diagnostic / Operational Metrics]
```

- **North Star**: ONE metric that best captures value delivery (DAU, MRR, GMV)
- **L1**: Business KPIs that drive the North Star (retention, acquisition, monetization)
- **L2**: Driving metrics teams can act on (conversion rate, ARPU, churn rate)
- **L3**: Diagnostic metrics for debugging (page load time, error rate, funnel step conversion)

### Chart Type Selection

| Question | Chart | Why |
|----------|-------|-----|
| How is the trend? | **Line chart** | Shows change over time |
| How do categories compare? | **Bar chart** (horizontal for many categories) | Easy comparison |
| What's the composition? | **Stacked bar** or **pie** (use sparingly, < 5 slices) | Shows parts of whole |
| What's the distribution? | **Histogram** or **box plot** | Shows spread and outliers |
| What's the relationship? | **Scatter plot** | Shows correlation |
| Where's the geographic pattern? | **Map / choropleth** | Spatial patterns |
| What's the single number? | **Scorecard / big number** | At-a-glance status |
| How are we vs target? | **Gauge** or **bullet chart** | Progress tracking |

### Design Principles

1. **5-second rule**: The dashboard's main message should be clear within 5 seconds
2. **Above the fold**: Most important metrics visible without scrolling
3. **Consistent time range**: All charts on one dashboard should use the same time period by default
4. **Color with purpose**: Use color to encode meaning (red = bad, green = good), not decoration
5. **Comparison context**: Every number needs context — vs prior period, vs target, vs benchmark
6. **Progressive disclosure**: Summary at top → click/drill to detail

### Dashboard Layers

| Layer | Audience | Refresh | Content |
|-------|---------|---------|---------|
| **Executive** | C-suite, board | Weekly/monthly | 5-8 KPIs, trends, alerts |
| **Operational** | Team leads | Daily | 10-15 metrics, filters by team/product |
| **Diagnostic** | Analysts, engineers | Real-time to hourly | 20+ metrics, drill-down, raw data access |

### Tool Comparison

| Tool | Best For | Cost | Learning Curve |
|------|---------|------|---------------|
| **Tableau** | Complex analysis, large datasets | $$$ | Medium-High |
| **Power BI** | Microsoft ecosystem, enterprise | $$ | Medium |
| **Looker** | SQL-centric teams, data modeling | $$$ | High |
| **Metabase** | Quick setup, open-source, self-serve | Free/$ | Low |
| **Google Sheets/Data Studio** | Simple, collaborative, free | Free | Low |
| **Grafana** | Infrastructure/real-time monitoring | Free/$ | Medium |

## Output Format

```markdown
# Dashboard Specification: {Name}

## Purpose & Audience
- Audience: {who}
- Key question: {what they need to answer}
- Refresh: {real-time / daily / weekly}

## KPI Hierarchy
- North Star: {metric}
- L1 KPIs: {3-5 metrics}
- L2 Driving Metrics: {per L1}

## Layout
| Position | Component | Chart Type | Metric |
|----------|-----------|-----------|--------|
| Top-left | {scorecard} | Big number | {North Star} |
| Top-right | {trend} | Line chart | {key KPI over time} |
| Mid-left | {comparison} | Bar chart | {breakdown by segment} |
| ... | ... | ... | ... |

## Filters
- Date range, product, segment, region

## Alerts
| Metric | Threshold | Alert To |
|--------|-----------|---------|
| {metric} | {value} | {team/person} |
```

## Gotchas

- **Dashboard ≠ report**: A report explains what happened (narrative). A dashboard monitors what IS happening (real-time status). Don't make a dashboard that requires reading.
- **Pie charts are almost always wrong**: Humans are bad at comparing angles. Use bar charts for composition with > 3 categories. Pie charts work only for 2-3 slices with very different sizes.
- **Too many metrics = no metrics**: If everything is highlighted, nothing is. Limit executive dashboards to 5-8 metrics. More → use filters or drill-down.
- **Vanity metrics sneak in**: Total users, page views, and downloads feel impressive but rarely drive action. Every metric on the dashboard should answer: "What would we do differently if this number changed?"
- **ETL reliability**: A dashboard is only as good as its data pipeline. If data is stale, incomplete, or wrong, the dashboard becomes a liability. Show "last updated" timestamp prominently.

## References

- For dashboard wireframe templates, see `references/dashboard-templates.md`
- For SQL-based metric definitions, see `references/metric-definitions.md`
