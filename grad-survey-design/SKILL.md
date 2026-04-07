---
name: "grad-survey-design"
description: "Apply rigorous survey design principles including construct operationalization, Likert scale development, reliability and validity assessment, and common method variance control. Use this skill when the user designs questionnaires, develops measurement items, needs to evaluate Cronbach's alpha or AVE, or when they ask 'how do I operationalize this construct', 'is my scale reliable', or 'how do I control for CMV'."
metadata:
  category: "WP-31 量化方法"
  tags: ["survey-design", "questionnaire", "Likert-scale", "reliability", "validity", "CMV", "Cronbachs-alpha"]
---

# 問卷設計 (Survey Design)

## Overview

Survey design translates theoretical constructs into measurable items through systematic operationalization, scale development, and psychometric validation. Rigorous surveys ensure that observed scores reliably and validly represent the intended constructs while controlling for method artifacts such as common method variance.

## When to Use

- Measuring perceptions, attitudes, beliefs, or behavioral intentions
- Operationalizing latent constructs from a theoretical framework
- Developing or adapting multi-item Likert scales
- Planning a quantitative study that relies on self-report data

## When NOT to Use

- Objective behavioral data or archival data are available and more appropriate
- The construct is better measured through experiments or observations
- Population is unreachable via survey (extremely low literacy, no sampling frame)
- Research question is exploratory and constructs are not yet well-defined

## Assumptions

```
IRON LAW: A survey measures PERCEPTIONS, not objective reality — and common
method variance inflates correlations when predictor and criterion come
from the same source.
```

Key assumptions:
1. Respondents understand items as intended (semantic equivalence)
2. Responses are honest and not systematically biased by social desirability
3. The construct domain is adequately sampled by the items
4. Items within a scale are reflective indicators of the same underlying construct

## Methodology

### Step 1 — Construct Operationalization

Define each construct's conceptual domain from theory. Specify dimensions and sub-dimensions. Generate item pool from literature, expert judgment, and qualitative input (3-5 items per dimension minimum).

### Step 2 — Scale Design and Pretesting

Choose response format (5-point or 7-point Likert). Avoid double-barreled, leading, or ambiguous items. Conduct cognitive interviews or expert panel review. Pilot test with N ≥ 30.

### Step 3 — Assess Reliability and Validity

Reliability: Cronbach's alpha ≥ 0.70, composite reliability (CR) ≥ 0.70. Convergent validity: AVE ≥ 0.50, factor loadings ≥ 0.60. Discriminant validity: Fornell-Larcker criterion or HTMT < 0.90. See `references/` for formulas.

### Step 4 — Control for Common Method Variance

Procedural remedies: separate predictor and criterion temporally, use different scale formats, guarantee anonymity. Statistical remedies: Harman's single-factor test (necessary but not sufficient), marker variable technique, CFA with common method factor.

## Output Format

```markdown
## Survey Design: [Study Title]

### Construct Operationalization
| Construct | Dimensions | Items | Source |
|-----------|-----------|-------|--------|
| [name] | [dim] | x items | [adapted from] |

### Reliability Assessment
| Construct | Items | Cronbach's α | CR | AVE |
|-----------|-------|-------------|-----|-----|
| [name] | x | x.xx | x.xx | x.xx |

### Validity Assessment
| Test | Result | Threshold | Assessment |
|------|--------|-----------|------------|
| Factor loadings (min) | x.xx | ≥ 0.60 | [pass/fail] |
| AVE | x.xx | ≥ 0.50 | [pass/fail] |
| HTMT (max) | x.xx | < 0.90 | [pass/fail] |

### CMV Controls
| Remedy | Type | Result |
|--------|------|--------|
| [remedy] | [procedural/statistical] | [finding] |

### Limitations
- [Note any assumption violations]
```

## Gotchas

- Cronbach's alpha is a lower bound of reliability and assumes tau-equivalence; CR is preferred
- High reliability with low validity means you are precisely measuring the wrong thing
- Reverse-coded items reduce acquiescence bias but often form artifactual method factors in CFA
- Harman's single-factor test is widely used but has very low power to detect CMV
- Translation and back-translation do not guarantee measurement invariance across cultures
- Response rate below 30% raises non-response bias concerns even with adequate sample size

## References

- DeVellis, R. F. (2017). *Scale Development: Theory and Applications* (4th ed.). Sage.
- Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research. *Journal of Applied Psychology*, 88(5), 879-903.
- Hair, J. F., Black, W. C., Babin, B. J., & Anderson, R. E. (2019). *Multivariate Data Analysis* (8th ed.). Cengage.
