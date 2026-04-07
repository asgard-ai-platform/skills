---
name: "grad-servqual"
description: "Apply the SERVQUAL model (Parasuraman, Zeithaml, and Berry, 1988) to measure service quality gaps across five dimensions. Use this skill when the user needs to diagnose service quality shortfalls, benchmark customer expectations against perceptions, design service improvement programs, or when they ask 'where is our service failing', 'what do customers expect vs experience', or 'how do we measure service quality'."
metadata:
  category: "WP-25 行銷理論"
  tags: ["SERVQUAL", "service-quality", "gap-model", "Parasuraman", "customer-expectations", "service-marketing"]
---

# SERVQUAL Model

## Overview

SERVQUAL measures service quality as the gap between customer expectations and perceptions across five dimensions: Tangibles, Reliability, Responsiveness, Assurance, and Empathy. The broader Gap Model identifies five organizational gaps that cause service quality failures.

## When to Use

- Measuring and benchmarking service quality
- Identifying which service dimensions need improvement
- Diagnosing root causes of customer dissatisfaction
- Comparing service quality across branches, competitors, or time periods

## When NOT to Use

- Evaluating product quality (use Garvin's 8 dimensions)
- When only transaction-level satisfaction is needed (use CSAT/NPS)
- Pure self-service digital products with no human interaction component

## Assumptions

```
IRON LAW: Service quality = Perception − Expectation. Both sides MUST
be measured independently. Measuring only satisfaction conflates the
two and hides diagnostic insight.
```

Key assumptions:
1. Customers form expectations before the service encounter
2. Quality is judged comparatively (perception vs expectation)
3. The five dimensions are universal across service industries
4. Gaps are additive — multiple small gaps compound into poor overall quality

## Methodology

### Step 1 — Measure expectations and perceptions

Administer paired 7-point Likert scales for each dimension (22 items total):

| Dimension | Focus | Example Item |
|-----------|-------|-------------|
| **Tangibles** | Physical facilities, equipment, appearance | "Modern-looking equipment" |
| **Reliability** | Deliver promised service dependably | "Provide service at promised time" |
| **Responsiveness** | Willingness to help, prompt service | "Employees give prompt service" |
| **Assurance** | Knowledge, courtesy, trust | "Employees instill confidence" |
| **Empathy** | Caring, individualized attention | "Understand specific needs" |

### Step 2 — Calculate gap scores

Gap Score = Perception Score − Expectation Score (negative = shortfall)

### Step 3 — Diagnose organizational gaps

| Gap | Description | Root Cause |
|-----|------------|------------|
| Gap 1 | Management perception vs customer expectation | Poor market research |
| Gap 2 | Service quality specs vs management perception | Inadequate standards |
| Gap 3 | Service delivery vs specifications | Poor execution |
| Gap 4 | External communication vs delivery | Overpromising |
| Gap 5 | Customer perception vs expectation | Cumulative result of Gaps 1-4 |

### Step 4 — Prioritize and intervene

Rank dimensions by gap magnitude weighted by importance. Target the largest negative gaps first.

## Output Format

```markdown
## SERVQUAL Analysis: [Service Context]

### Gap Scores by Dimension
| Dimension | Expectation (E) | Perception (P) | Gap (P-E) | Priority |
|-----------|----------------|-----------------|-----------|----------|
| Tangibles | | | | |
| Reliability | | | | |
| Responsiveness | | | | |
| Assurance | | | | |
| Empathy | | | | |

### Organizational Gap Diagnosis
- Gap 1 (Knowledge): ...
- Gap 2 (Standards): ...
- Gap 3 (Delivery): ...
- Gap 4 (Communication): ...

### Improvement Recommendations
1. [Dimension]: [specific action]
2. ...
```

## Gotchas

- Expectation scores tend to cluster high (ceiling effect), compressing diagnostic variance
- The 22-item instrument is often adapted — document any modifications for validity
- Reliability and Responsiveness typically dominate importance weights across industries
- Zone of tolerance exists between desired and adequate expectations — measure both for richer insight
- SERVPERF (Cronin & Taylor, 1992) argues perception-only measurement is sufficient — know the debate
- Cultural norms shift dimension weights: collectivist cultures weight Empathy higher

## References

- Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12-40.
- Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1985). A conceptual model of service quality and its implications for future research. *Journal of Marketing*, 49(4), 41-50.
- Cronin, J. J., & Taylor, S. A. (1992). Measuring service quality: A reexamination and extension. *Journal of Marketing*, 56(3), 55-68.
