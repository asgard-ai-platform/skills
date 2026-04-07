---
name: "cs-analytics"
description: "Measure and optimize customer service performance using CSAT, NPS, CES, First Contact Resolution, and text mining on support tickets. Use this skill when the user needs to evaluate CS team performance, identify top complaint drivers, optimize staffing, or build CS dashboards — even if they say 'is our CS team doing well', 'what are customers complaining about', 'how many agents do we need', or 'build a CS dashboard'."
metadata:
  category: "WP-06 Agent通訊+客服"
  tags: ["customer-service", "analytics", "nps", "csat"]
---

# Customer Service Analytics

## Framework

```
IRON LAW: Measure Satisfaction AND Efficiency — Never Just One

High CSAT with terrible resolution time = unsustainable (agents spend
too long per ticket). Fast resolution with low CSAT = cutting corners.
Both dimensions must be tracked and balanced.
```

### Key Metrics

**Satisfaction Metrics**
| Metric | What It Measures | How to Collect | Benchmark |
|--------|-----------------|---------------|-----------|
| **CSAT** | Satisfaction with specific interaction | Post-interaction survey (1-5 scale) | > 4.0/5 |
| **NPS** | Likelihood to recommend | "How likely to recommend?" (0-10) | > 30 |
| **CES** | Effort required to resolve | "How easy was it to resolve?" (1-7) | > 5.0/7 |

**Efficiency Metrics**
| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **First Contact Resolution (FCR)** | Resolved on first contact / Total contacts | > 70% |
| **Average Handle Time (AHT)** | Total handle time / Total contacts | 5-8 min (varies by industry) |
| **Average Response Time** | Time from ticket creation to first response | < SLA target |
| **Backlog** | Open tickets / Daily throughput | < 1 day |
| **Escalation Rate** | Escalated tickets / Total tickets | < 20% |
| **Reopen Rate** | Reopened tickets / Resolved tickets | < 5% |

**Operational Metrics**
| Metric | Formula | Use |
|--------|---------|-----|
| **Ticket Volume** | Tickets per day/week/month | Staffing planning |
| **Channel Mix** | % by channel (email, chat, phone, LINE) | Resource allocation |
| **Peak Hours** | Volume by hour-of-day | Shift scheduling |
| **Category Distribution** | % by issue type | Process improvement priority |

### Analysis Workflows

**1. Top Contact Reason Analysis**
- Categorize all tickets by reason (auto-tag or manual)
- Pareto chart: top 5 reasons usually account for 60-80% of volume
- For each top reason: can it be self-served? Automated? Eliminated at source?

**2. Text Mining on Tickets**
- Extract frequent keywords/phrases from ticket descriptions
- Cluster into topics (LDA, BERTopic, or simple TF-IDF)
- Identify emerging issues (new topics appearing in recent weeks)
- Sentiment analysis on customer messages

**3. Staffing Optimization**
```
Required Agents = Peak Hour Volume × AHT / (60 × Utilization Target)

Example: 50 tickets/hour × 8 min AHT / (60 × 0.75 utilization) = 8.9 → 9 agents
```

Add buffer for breaks, meetings, and training (~15-20%).

**4. Agent Performance**
| Metric | Compare | Action |
|--------|---------|--------|
| Individual CSAT vs team avg | Identify coaching needs | Training for below-average |
| Individual AHT vs team avg | Identify efficiency gaps | Shadow high-performers |
| FCR by agent | Identify knowledge gaps | Knowledge base improvements |

### VOC (Voice of Customer) Tracking

| Signal | Source | Frequency |
|--------|--------|-----------|
| Emerging complaints | Ticket text mining | Weekly |
| Feature requests | Tagged tickets + surveys | Monthly |
| Churn signals | "Cancel" intent tickets, low CSAT patterns | Weekly |
| Praise patterns | High CSAT + positive comments | Monthly (share with team) |

## Output Format

```markdown
# CS Analytics Report: {Period}

## Summary Dashboard
| Metric | Current | Prior | Target | Status |
|--------|---------|-------|--------|--------|
| CSAT | {X}/5 | {X}/5 | >4.0 | 🟢/🟡/🔴 |
| FCR | {%} | {%} | >70% | 🟢/🟡/🔴 |
| Avg Response Time | {hrs} | {hrs} | <{X}hrs | 🟢/🟡/🔴 |
| Ticket Volume | {N} | {N} | — | ↑/↓ |

## Top Contact Reasons (Pareto)
| # | Reason | Volume | % | Self-Servable? |
|---|--------|--------|---|---------------|
| 1 | {reason} | {N} | {%} | Y/N |

## Emerging Issues
{New topics detected in text mining this period}

## Staffing
- Current agents: {N}
- Required (based on volume): {N}
- Gap: {over/under-staffed by N}

## Recommendations
1. {highest-impact improvement}
```

## Gotchas

- **CSAT response bias**: Only 10-20% of customers respond to surveys, usually the very happy and very unhappy. The silent majority's experience is unknown. Supplement with behavioral data (repeat contact, churn).
- **NPS is strategic, CSAT is tactical**: NPS measures overall brand loyalty (long-term). CSAT measures specific interaction quality (short-term). Don't use NPS to evaluate individual agents.
- **AHT optimization can hurt quality**: Pressure to reduce AHT may cause agents to rush, reducing FCR and CSAT. Optimize FCR first, then look at AHT.
- **Ticket categorization drift**: Categories become outdated as products evolve. Review and update the category taxonomy quarterly.
- **Correlation ≠ causation in CS data**: "Agents who use more templates have higher CSAT" might mean templates help, OR that experienced agents (who happen to use templates) are just better.

## References

- For NPS survey design, see `references/nps-methodology.md`
- For text mining on support tickets, see `references/ticket-text-mining.md`
