---
name: "grad-affordance"
description: "Apply Affordance Theory (Gibson, 1979; Norman, 1988) to analyze the action possibilities that an artifact provides to an actor. Use this skill when the user needs to evaluate technology design from an affordance perspective, identify why users struggle with an interface, analyze IT-enabled organizational change through affordance actualization, or when they ask 'what does this technology afford', 'why can't users figure out this feature', or 'how does technology enable new practices'."
metadata:
  category: "WP-30 資訊管理"
  tags: ["affordance", "Gibson", "Norman", "perceived-affordance", "actualization", "design", "HCI"]
---

# Affordance Theory (Gibson / Norman)

## Overview

Affordance Theory explains how actors perceive and realize action possibilities offered by objects or environments. Gibson's ecological view holds that affordances are relational properties existing between actor and environment, independent of perception. Norman adapted the concept for design — perceived affordances guide user interaction, and signifiers communicate where action is possible. In IS research, affordance theory explains how technology enables (or constrains) organizational action.

## When to Use

- Analyzing why users can or cannot effectively use a technology
- Designing interfaces that communicate functionality clearly
- Explaining how the same technology produces different outcomes in different organizations
- Bridging the gap between technology features and organizational practices

## When NOT to Use

- Predicting adoption likelihood (use TAM/UTAUT)
- Measuring usability metrics quantitatively (use SUS or heuristic evaluation)
- When the focus is purely on aesthetic design without functional implications

## Assumptions

```
IRON LAW: An affordance exists in the RELATION between actor and artifact —
it is neither a property of the object alone nor of the user alone.
```

Key assumptions:
1. Affordances are relational — they depend on both artifact properties and actor capabilities
2. Affordance existence differs from affordance perception differs from affordance actualization
3. The same technology affords different actions to different actors (role, skill, goal-dependent)
4. Constraints are the complement of affordances — what the artifact prevents or discourages

## Methodology

### Step 1 — Identify actors and artifacts

Specify the technology artifact and the actor groups. Characterize actor capabilities, goals, and context. The same artifact affords different things to a novice versus an expert.

### Step 2 — Enumerate affordances

For each actor-artifact pair, identify:

| Affordance Type | Description |
|----------------|-------------|
| Existence | What action possibilities objectively exist in the relation |
| Perception | Which affordances actors actually perceive (Norman's focus) |
| Actualization | Which perceived affordances actors act upon |

Include constraints (actions the artifact prevents) alongside affordances.

### Step 3 — Analyze gaps

Identify three critical gaps:
- **Perception gap**: affordances that exist but are not perceived (design/signifier problem)
- **Actualization gap**: affordances perceived but not actualized (motivation/skill/resource problem)
- **False affordance**: actions perceived as possible but that do not actually exist

### Step 4 — Recommend design or organizational interventions

For perception gaps: improve signifiers, onboarding, or documentation. For actualization gaps: provide training, resources, or remove organizational barriers. For false affordances: fix misleading cues in the interface.

## Output Format

```markdown
## Affordance Analysis: [Artifact] x [Actor Group]

### Actor Profile
- Role: ...
- Capabilities: ...
- Goals: ...

### Affordance Map
| Affordance | Exists? | Perceived? | Actualized? | Gap Type |
|-----------|---------|------------|-------------|----------|
| | | | | |

### Constraints
- [constraint]: [effect on actor behavior]

### Gap Analysis
- Perception gaps: ...
- Actualization gaps: ...
- False affordances: ...

### Recommendations
1. [Gap type]: [intervention]
2. ...
```

## Gotchas

- Do not conflate Gibson's affordances (relational, objective) with Norman's perceived affordances (subjective, design-focused) — state which lens you are using
- "Feature" is not "affordance" — features are artifact properties; affordances emerge from the actor-artifact relation
- Affordance theory is explanatory, not predictive — it helps interpret why things happen, not forecast adoption rates
- In IS research, affordance actualization depends on organizational context (norms, routines, power structures), not just individual perception
- Beware affordance creep — listing every conceivable action possibility without prioritizing those relevant to the research question
- Norman later preferred "signifier" over "perceived affordance" to reduce confusion — use current terminology

## References

- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.
- Norman, D. A. (1988). *The Design of Everyday Things*. Basic Books.
- Markus, M. L., & Silver, M. S. (2008). A foundation for the study of IT effects: A new look at DeSanctis and Poole's concepts of structural features and spirit. *Journal of the AIS*, 9(10/11), 609-632.
- Volkoff, O., & Strong, D. M. (2013). Critical realism and affordances: Theorizing IT-associated organizational change processes. *MIS Quarterly*, 37(3), 819-834.
