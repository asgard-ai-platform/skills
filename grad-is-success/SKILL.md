---
name: "grad-is-success"
description: "Apply the DeLone and McLean Information Systems Success Model to evaluate IS effectiveness through six interdependent dimensions. Use this skill when the user needs to assess system quality, information quality, or service quality of an IS, diagnose why users are dissatisfied, measure net benefits of a system investment, or when they ask 'how do we measure IS success', 'why are users unhappy with this system', or 'is our system delivering value'."
metadata:
  category: "WP-30 資訊管理"
  tags: ["IS-success", "DeLone-McLean", "system-quality", "information-quality", "service-quality", "user-satisfaction", "net-benefits"]
---

# IS Success Model (DeLone & McLean)

## Overview

The DeLone and McLean IS Success Model (1992, updated 2003) identifies six interdependent dimensions of IS success: System Quality, Information Quality, Service Quality, Intention to Use/Use, User Satisfaction, and Net Benefits. These dimensions form a causal chain with feedback loops — net benefits reinforce (or undermine) subsequent use and satisfaction.

## When to Use

- Evaluating overall effectiveness of an information system
- Diagnosing user dissatisfaction or low system utilization
- Building a measurement framework for IS project post-implementation review
- Comparing alternative systems across multiple quality dimensions

## When NOT to Use

- Pre-development requirements gathering (use requirements engineering methods)
- Technology acceptance prediction before deployment (use TAM/UTAUT)
- Measuring individual task performance only (use Task-Technology Fit)

## Assumptions

```
IRON LAW: IS success is MULTIDIMENSIONAL — measuring only one dimension
(e.g., usage) gives an incomplete and potentially misleading picture.
```

Key assumptions:
1. The six dimensions are interdependent, not independent metrics
2. System Quality, Information Quality, and Service Quality are causally prior to Use and Satisfaction
3. Net Benefits feed back to influence future Use and User Satisfaction
4. Context determines which dimensions matter most — there is no universal weighting

## Methodology

### Step 1 — Identify the IS and stakeholder groups

Specify the information system under evaluation, its purpose, and the relevant stakeholder groups (end users, managers, IT staff, customers). Define what "net benefits" means for each group.

### Step 2 — Measure quality dimensions

| Dimension | Representative Measures |
|-----------|------------------------|
| System Quality | Reliability, response time, usability, flexibility, security |
| Information Quality | Accuracy, completeness, timeliness, relevance, consistency |
| Service Quality | Responsiveness, assurance, empathy of IT support (SERVQUAL-adapted) |

### Step 3 — Assess use and satisfaction

Measure actual Use (frequency, duration, extent) or Intention to Use (for pre-deployment). Measure User Satisfaction via overall satisfaction scales and specific feature satisfaction.

### Step 4 — Evaluate net benefits and feedback loops

Quantify Net Benefits at the appropriate level (individual productivity, workgroup efficiency, organizational performance). Trace feedback: positive net benefits should increase future use and satisfaction; negative benefits signal a deterioration loop.

## Output Format

```markdown
## IS Success Assessment: [System Name]

### Quality Dimensions
| Dimension | Rating (1-7) | Strengths | Weaknesses |
|-----------|-------------|-----------|------------|
| System Quality | | | |
| Information Quality | | | |
| Service Quality | | | |

### Use & Satisfaction
- Usage level: [high/moderate/low] — [evidence]
- User Satisfaction: [score] — [key drivers/detractors]

### Net Benefits
| Stakeholder Group | Benefit Type | Assessment |
|-------------------|-------------|------------|
| | | |

### Feedback Loop Diagnosis
- Virtuous cycle present? [yes/no] — [evidence]
- Deterioration risks: ...

### Recommendations
1. [Target dimension]: [action]
2. ...
```

## Gotchas

- Usage is problematic as a success measure when system use is mandatory — satisfaction becomes the better indicator
- The model is a taxonomy, not a causal theory — it identifies what to measure, not precise causal weights
- Service Quality was added in the 2003 update; studies using the 1992 model omit it
- Net Benefits replace the original "Individual Impact" and "Organizational Impact" — define the level of analysis explicitly
- Information Quality and System Quality are highly correlated in practice; use discriminant validity checks
- Context matters enormously — an ERP assessment weights dimensions differently than a consumer app

## References

- DeLone, W. H., & McLean, E. R. (1992). Information systems success: The quest for the dependent variable. *Information Systems Research*, 3(1), 60-95.
- DeLone, W. H., & McLean, E. R. (2003). The DeLone and McLean model of information systems success: A ten-year update. *Journal of Management Information Systems*, 19(4), 9-30.
- Petter, S., DeLone, W., & McLean, E. (2008). Measuring information systems success: Models, dimensions, measures, and interrelationships. *European Journal of Information Systems*, 17(3), 236-263.
