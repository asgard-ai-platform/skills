---
name: "grad-event-study"
description: "Apply event study methodology to measure abnormal returns and cumulative abnormal returns (CAR) around corporate or market events. Use this skill when the user needs to quantify the market impact of announcements, design event and estimation windows, or when they ask 'did this event affect stock price', 'how do I calculate abnormal returns', or 'what is the market reaction to this announcement'."
metadata:
  category: "WP-31 量化方法"
  tags: ["event-study", "abnormal-return", "CAR", "market-reaction", "event-window", "finance"]
---

# 事件研究法 (Event Study)

## Overview

The event study method (Fama et al., 1969; MacKinlay, 1997) isolates the abnormal return attributable to a specific event by comparing actual returns against a model of expected (normal) returns. Cumulative abnormal returns (CAR) over an event window quantify the total market reaction.

## When to Use

- Measuring market reaction to earnings announcements, M&A, policy changes, or regulatory events
- Testing semi-strong form market efficiency
- Quantifying the economic significance of corporate disclosures
- Comparing market reactions across different event types or firm characteristics

## When NOT to Use

- The event date is ambiguous or the information leaked gradually
- Confounding events overlap with the event window
- The firm's stock is illiquid with many zero-return days
- The event was widely anticipated and fully priced before the event window

## Assumptions

```
IRON LAW: Event study validity requires that the event was UNANTICIPATED —
if the market priced it in before the event window, abnormal returns will
be zero even if the event matters.
```

Key assumptions:
1. Event date is precisely identifiable and the event was unexpected
2. No confounding events occur within the event window
3. The normal return model is correctly specified during the estimation window
4. Market microstructure effects (thin trading, bid-ask bounce) do not distort returns

## Methodology

### Step 1 — Define Event and Windows

Identify the event date (day 0). Set estimation window (e.g., [-250, -11]) to estimate normal returns. Set event window (e.g., [-1, +1] or [-5, +5]) to capture the reaction.

### Step 2 — Estimate Normal Returns

Use the market model: Ri,t = αi + βi × Rm,t + εi,t estimated over the estimation window. Alternatives include constant mean return or Fama-French factors. See `references/` for model specifications.

### Step 3 — Compute Abnormal and Cumulative Abnormal Returns

AR = Actual return - Expected return for each day in the event window. CAR = sum of ARs over the event window. Compute CAAR (cumulative average abnormal return) across firms.

### Step 4 — Statistical Testing

Test H₀: CAR = 0 using parametric tests (cross-sectional t-test, Patell test) and non-parametric tests (sign test, rank test). Report both for robustness.

## Output Format

```markdown
## Event Study: [Event Description]

### Window Design
| Window | Period | Rationale |
|--------|--------|-----------|
| Estimation | [-250, -11] | [rationale] |
| Event | [-1, +1] | [rationale] |

### Abnormal Returns
| Day | AR (%) | t-stat |
|-----|--------|--------|
| -1 | x.xx | x.xx |
| 0 | x.xx | x.xx |
| +1 | x.xx | x.xx |

### Cumulative Abnormal Returns
| Window | CAR (%) | t-stat | p-value | Significant? |
|--------|---------|--------|---------|-------------|
| [-1, +1] | x.xx | x.xx | x.xx | [Yes/No] |

### Cross-Sectional Analysis
- [If applicable: regression of CAR on firm characteristics]

### Limitations
- [Note any confounding events or assumption violations]
```

## Gotchas

- Clustering of event dates (e.g., industry-wide regulation) violates cross-sectional independence
- Short estimation windows produce noisy normal return parameters
- Long event windows increase the probability of confounding events
- Penny stocks and illiquid securities inflate abnormal returns artificially
- The market model assumes constant beta — structural breaks invalidate this
- Publication bias: studies finding zero CAR are rarely published

## References

- MacKinlay, A. C. (1997). Event studies in economics and finance. *Journal of Economic Literature*, 35(1), 13-39.
- Fama, E. F., Fisher, L., Jensen, M. C., & Roll, R. (1969). The adjustment of stock prices to new information. *International Economic Review*, 10(1), 1-21.
- Kolari, J. W., & Pynnönen, S. (2010). Event study testing with cross-sectional correlation of abnormal returns. *Review of Financial Studies*, 23(11), 3996-4025.
