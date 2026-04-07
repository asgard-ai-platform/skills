---
name: "grad-tam-utaut"
description: "Apply the Technology Acceptance Model (Davis, 1989) and Unified Theory of Acceptance and Use of Technology (Venkatesh et al., 2003) to predict technology adoption. Use this skill when the user needs to evaluate user acceptance of a new system, diagnose adoption barriers, design interventions to improve technology uptake, or when they ask 'why aren't users adopting this', 'what drives technology acceptance', or 'how do we increase adoption rates'."
metadata:
  category: "WP-25 行銷理論"
  tags: ["TAM", "UTAUT", "technology-acceptance", "adoption", "Davis", "Venkatesh", "behavioral-intention"]
---

# Technology Acceptance Model (TAM) and UTAUT

## Overview

TAM posits that Perceived Usefulness (PU) and Perceived Ease of Use (PEOU) determine behavioral intention to use technology. UTAUT synthesizes eight prior models into four core constructs — Performance Expectancy, Effort Expectancy, Social Influence, and Facilitating Conditions — moderated by age, gender, experience, and voluntariness.

## When to Use

- Predicting user adoption of a new technology or system
- Diagnosing why a technology rollout has low uptake
- Designing interventions to improve acceptance rates
- Comparing adoption drivers across user segments

## When NOT to Use

- Post-adoption continuance (use Expectation-Confirmation Model)
- Organizational-level diffusion (use DOI or TOE framework)
- When adoption is mandatory with no behavioral variance

## Assumptions

```
IRON LAW: Technology adoption is driven by PERCEIVED value, not actual
capability. A superior system with poor perceived usefulness will be
rejected; an inferior system perceived as useful will be adopted.
```

Key assumptions:
1. Users are rational actors who form intentions before behavior
2. Perceptions can be measured via self-report instruments
3. External variables influence adoption only through the core constructs
4. Behavioral intention is the primary predictor of actual use

## Methodology

### Step 1 — Define the technology and user population

Specify the system under evaluation, target users, and usage context. Identify whether adoption is voluntary or mandatory.

### Step 2 — Measure core constructs

**TAM constructs:**
- Perceived Usefulness (PU): "Using X improves my job performance"
- Perceived Ease of Use (PEOU): "Using X is free of effort"

**UTAUT constructs:**
| Construct | Definition | TAM Equivalent |
|-----------|-----------|----------------|
| Performance Expectancy | Degree system helps job performance | PU |
| Effort Expectancy | Ease of using the system | PEOU |
| Social Influence | Important others think I should use it | Subjective Norm |
| Facilitating Conditions | Infrastructure supports use | (external) |

### Step 3 — Identify moderators and barriers

Map moderating variables: age, gender, experience, voluntariness. Identify specific barriers per construct (e.g., poor training → low Effort Expectancy).

### Step 4 — Design interventions

Target the weakest construct(s) with specific interventions: training (Effort), demonstrations of value (Performance), champion programs (Social), IT support (Facilitating).

## Output Format

```markdown
## TAM/UTAUT Analysis: [Technology/Context]

### Construct Assessment
| Construct | Score (1-7) | Key Drivers | Key Barriers |
|-----------|-------------|-------------|--------------|
| Performance Expectancy | | | |
| Effort Expectancy | | | |
| Social Influence | | | |
| Facilitating Conditions | | | |

### Moderator Effects
- Age: ...
- Experience: ...
- Voluntariness: ...

### Intervention Recommendations
1. [Target construct]: [specific action]
2. ...
```

## Gotchas

- TAM explains intention, not actual sustained use — add habit and continuance constructs for long-term prediction
- PEOU has diminishing effect as users gain experience; PU dominates over time
- Social Influence matters most under mandatory settings and for early adopters
- Self-report bias inflates correlations between constructs (common method variance)
- UTAUT2 adds hedonic motivation, price value, and habit for consumer contexts
- Cultural context shifts construct weights — do not assume Western-validated weights universally apply

## References

- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly*, 13(3), 319-340.
- Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. *MIS Quarterly*, 27(3), 425-478.
- Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology: Extending the UTAUT. *MIS Quarterly*, 36(1), 157-178.
