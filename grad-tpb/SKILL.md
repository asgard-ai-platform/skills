---
name: "grad-tpb"
description: "Apply the Theory of Planned Behavior to predict behavioral intentions from attitudes, subjective norms, and perceived behavioral control, and identify intervention leverage points. Use this skill when the user needs to predict adoption of a new behavior, diagnose why an intended behavior does not occur, design behavior change campaigns, or when they ask 'why do people not follow through', 'what predicts behavior change', or 'how to increase adoption rates'."
metadata:
  category: "WP-29 心理學理論"
  tags: ["theory-of-planned-behavior", "TPB", "Ajzen", "behavioral-intention", "attitude", "subjective-norms", "perceived-behavioral-control"]
---

# Theory of Planned Behavior (TPB)

## Overview

The Theory of Planned Behavior (Ajzen, 1991) extends the Theory of Reasoned Action by adding perceived behavioral control as a predictor of both intention and behavior. Behavioral intention is determined by three factors: attitude toward the behavior, subjective norms, and perceived behavioral control. Intention is the proximal predictor of behavior, moderated by actual control.

## When to Use

- Predicting whether a target population will adopt a new behavior (health, technology, policy)
- Diagnosing the intention-behavior gap — why people intend to act but do not follow through
- Designing persuasion or behavior change interventions by targeting the weakest predictor
- Evaluating campaign effectiveness on attitude, norm, and control dimensions

## When NOT to Use

- For habitual or automatic behaviors where intention plays a minimal role
- When behavior is primarily driven by unconscious or emotional processes (use dual-process models)
- For behaviors under complete external control (no volitional component)

## Assumptions

```
IRON LAW: Intention predicts behavior ONLY when perceived
behavioral control is high — without actual control, intention
alone is insufficient. The intention-behavior gap widens as
volitional control decreases.
```

Key assumptions:
1. People make reasoned (though not necessarily rational) decisions based on available information
2. Behavioral beliefs, normative beliefs, and control beliefs are the informational foundations
3. The relative weight of attitude, norms, and PBC varies across behaviors and populations

## Methodology

### Step 1 — Specify the Target Behavior

Define the behavior precisely using the TACT framework:
- **T**arget: at what object or person
- **A**ction: what specific action
- **C**ontext: in what situation
- **T**ime: in what time frame

### Step 2 — Measure the Three Predictors

| Predictor | Definition | Underlying Beliefs |
|-----------|------------|--------------------|
| Attitude | Favorable/unfavorable evaluation of performing the behavior | Behavioral beliefs (outcomes x evaluations) |
| Subjective norms | Perceived social pressure to perform or not perform | Normative beliefs (referents x motivation to comply) |
| Perceived behavioral control (PBC) | Perceived ease or difficulty of performing the behavior | Control beliefs (facilitators/barriers x power) |

### Step 3 — Assess Intention and the Intention-Behavior Gap

- Measure behavioral intention as a function of the three predictors
- Identify which predictor is the weakest link (highest leverage for intervention)
- Evaluate actual behavioral control to assess gap risk

### Step 4 — Design Targeted Intervention

- **Attitude-focused**: provide new outcome information, reframe consequences
- **Norm-focused**: make social norms visible, use social proof, engage opinion leaders
- **PBC-focused**: reduce barriers, build self-efficacy, provide skills training
- **Implementation intentions**: bridge the intention-behavior gap with "if-then" planning

## Output Format

```markdown
## TPB Analysis: [Target Behavior]

### Behavior Specification (TACT)
- Target: [object/person]
- Action: [specific behavior]
- Context: [situation]
- Time: [time frame]

### Predictor Assessment
| Predictor | Score | Key Beliefs | Intervention Potential |
|-----------|-------|-------------|----------------------|
| Attitude | [+/-] | [salient beliefs] | [High/Medium/Low] |
| Subjective norms | [+/-] | [key referents] | [High/Medium/Low] |
| PBC | [+/-] | [barriers/facilitators] | [High/Medium/Low] |

### Intention Strength: [Strong/Moderate/Weak]
### Intention-Behavior Gap Risk: [High/Medium/Low]

### Recommended Intervention
1. [Primary lever: weakest predictor]
2. [Implementation intention strategy]
3. [Barrier removal or facilitator enhancement]
```

## Gotchas

- TPB assumes rational information processing; it underestimates the role of emotions, habits, and unconscious drivers
- Subjective norms are consistently the weakest predictor in meta-analyses — but this may reflect measurement issues rather than true irrelevance
- Past behavior often explains more variance than TPB constructs, suggesting habit and automaticity are under-represented
- PBC is not the same as actual control — people systematically overestimate or underestimate their control
- The theory works best for deliberate, one-time decisions; for recurring behaviors, habit formation models should supplement TPB
- Cross-cultural application requires recalibrating normative beliefs — collectivist cultures weight subjective norms more heavily

## References

- Ajzen, I. (1991). The theory of planned behavior. *Organizational Behavior and Human Decision Processes*, 50(2), 179-211.
- Armitage, C. J. & Conner, M. (2001). Efficacy of the theory of planned behaviour: a meta-analytic review. *British Journal of Social Psychology*, 40(4), 471-499.
- Fishbein, M. & Ajzen, I. (2010). *Predicting and changing behavior: the reasoned action approach*. Psychology Press.
