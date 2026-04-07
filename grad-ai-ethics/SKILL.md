---
name: "grad-ai-ethics"
description: "Apply AI ethics frameworks (fairness, accountability, transparency, privacy) to evaluate AI systems for algorithmic bias, explainability gaps, and value alignment failures. Use this skill when the user needs to audit an AI system for ethical risks, design fairness constraints, assess explainability requirements, or when they ask 'is this AI system fair', 'how do we detect algorithmic bias', 'what are the ethical implications of this AI deployment', or 'how do we make this model explainable to stakeholders'."
metadata:
  category: "WP-34 跨學科/新興"
  tags: ["AI-ethics", "fairness", "accountability", "transparency", "algorithmic-bias", "XAI", "explainable-AI", "FATE"]
---

# AI Ethics

## Overview

AI ethics examines the moral dimensions of artificial intelligence systems, centered on four pillars: fairness, accountability, transparency, and privacy (FATE). As AI systems increasingly make consequential decisions, they inherit and amplify the biases embedded in training data and design choices. Ethical AI requires proactive identification of bias, explainability mechanisms, clear accountability structures, and privacy protections.

## When to Use

- Auditing an AI system for fairness before or after deployment
- Designing bias mitigation strategies for machine learning pipelines
- Evaluating explainability requirements for different stakeholder audiences
- Assessing regulatory compliance (EU AI Act, GDPR, sector-specific requirements)

## When NOT to Use

- When the question is purely about model performance without ethical dimensions
- When analyzing non-AI automation or rule-based systems with full transparency
- When the focus is on AI technical architecture without deployment context

## Assumptions

```
IRON LAW: AI systems encode the VALUES of their designers and training
data — there is no value-neutral AI, and "optimizing for accuracy"
without fairness constraints reproduces existing inequalities.
```

Key assumptions:
1. All datasets reflect historical decisions and biases — "ground truth" is socially constructed
2. Fairness has multiple, mathematically incompatible definitions — choosing one is a value judgment
3. Transparency and explainability are not the same — a system can be transparent (open code) but not explainable (no one understands why it decided X)
4. Accountability requires clear chains of responsibility from developer to deployer to affected party

## Methodology

### Step 1: Map the AI System and Stakeholders

Identify the AI system's function, decision domain, affected populations, and the power asymmetry between system operators and subjects.

### Step 2: Assess Fairness

Evaluate using multiple fairness definitions:

| Fairness Metric | Definition | Tension |
|----------------|------------|---------|
| **Demographic parity** | Equal positive outcome rates across groups | May conflict with accuracy |
| **Equalized odds** | Equal true positive and false positive rates across groups | May conflict with calibration |
| **Individual fairness** | Similar individuals receive similar outcomes | Requires defining "similarity" |
| **Calibration** | Predicted probabilities match actual outcomes per group | May conflict with equalized odds |

### Step 3: Evaluate Transparency and Explainability

Assess whether explanations are appropriate for each stakeholder: affected individuals (recourse-oriented), regulators (compliance-oriented), developers (debugging-oriented), and the public (trust-oriented).

### Step 4: Design Accountability and Mitigation

Define responsibility chains, bias mitigation interventions (pre-processing, in-processing, post-processing), ongoing monitoring, and redress mechanisms.

## Output Format

```markdown
## AI Ethics Assessment: [System/Context]

### System Profile
- Function: [what the AI system does]
- Decision domain: [what decisions it makes or supports]
- Affected populations: [who is impacted]
- Power asymmetry: [who controls vs who is subject to the system]

### Fairness Assessment
| Dimension | Status | Evidence | Risk Level |
|-----------|--------|----------|------------|
| Demographic parity | [met/unmet/unknown] | [data] | [high/medium/low] |
| Equalized odds | [met/unmet/unknown] | [data] | [high/medium/low] |
| Individual fairness | [met/unmet/unknown] | [data] | [high/medium/low] |

### Transparency and Explainability
| Stakeholder | Explanation Needed | Currently Provided | Gap |
|-------------|-------------------|-------------------|-----|
| [affected individuals] | [what they need] | [what exists] | [gap] |
| [regulators] | [what they need] | [what exists] | [gap] |

### Accountability Structure
- Developer responsibility: [scope]
- Deployer responsibility: [scope]
- Redress mechanism: [how affected parties can contest decisions]

### Mitigation Recommendations
1. [Pre-processing intervention]
2. [In-processing intervention]
3. [Post-processing intervention]
4. [Monitoring and ongoing audit plan]
```

## Gotchas

- Fairness metrics are mathematically incompatible (Chouldechova, 2017) — you MUST choose which to prioritize, and this is a political decision
- "Removing protected attributes" does not remove bias — correlated proxies perpetuate discrimination
- Explainability methods (LIME, SHAP) explain model behavior, not model reasoning — they are post-hoc rationalizations
- Privacy and fairness can conflict — fairness audits require demographic data that privacy protections restrict
- AI ethics is not a checklist — it requires ongoing engagement, not one-time certification
- Beware "ethics washing" — superficial ethics processes that provide cover without substantive change

## References

- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities*. MIT Press.
- Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, 1(9), 389-399.
- Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. *Proceedings of FAT* 2019*, 59-68.
