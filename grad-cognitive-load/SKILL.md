---
name: "grad-cognitive-load"
description: "Apply Cognitive Load Theory to optimize instructional design by managing intrinsic, extraneous, and germane load within working memory limits. Use this skill when the user needs to diagnose why learners are overwhelmed, redesign training or documentation for better comprehension, evaluate UI/UX information architecture for cognitive burden, or when they ask 'why is this tutorial confusing', 'how to simplify complex instructions', or 'what causes information overload'."
metadata:
  category: "WP-29 心理學理論"
  tags: ["cognitive-load-theory", "Sweller", "working-memory", "instructional-design", "intrinsic-load", "extraneous-load", "germane-load"]
---

# Cognitive Load Theory (CLT)

## Overview

Cognitive Load Theory (Sweller, 1988) is grounded in the architecture of human cognition: working memory is severely limited in capacity (7 +/- 2 items) and duration, while long-term memory is essentially unlimited. Effective instructional design must manage three types of cognitive load — intrinsic (task complexity), extraneous (poor design), and germane (schema construction) — so that total load does not exceed working memory capacity.

## When to Use

- Diagnosing why learners fail to comprehend or retain instructional material
- Redesigning documentation, tutorials, or training programs for reduced cognitive burden
- Evaluating interface design, dashboards, or information displays for overload
- Sequencing complex learning material to scaffold schema acquisition

## When NOT to Use

- When the problem is motivational rather than cognitive (learner can process but chooses not to)
- For expert audiences where schemas already exist and the expertise reversal effect applies
- When simplification would compromise essential task fidelity (some tasks are irreducibly complex)

## Assumptions

```
IRON LAW: Working memory capacity is FIXED and limited —
instructional design must minimize extraneous load to maximize
germane processing. Total load (intrinsic + extraneous + germane)
must not exceed working memory capacity.
```

Key assumptions:
1. Working memory processes novel information; long-term memory stores schemas that bypass WM limits
2. Intrinsic load is determined by element interactivity — it cannot be reduced without changing the task
3. Extraneous load is under the designer's control and should always be minimized

## Methodology

### Step 1 — Analyze Element Interactivity (Intrinsic Load)

Assess how many information elements must be processed simultaneously:
- **Low interactivity**: elements can be learned independently (vocabulary lists)
- **High interactivity**: elements must be integrated to be understood (grammar rules, circuit design)

### Step 2 — Identify Extraneous Load Sources

| Source | Description | Design Flaw |
|--------|-------------|-------------|
| Split-attention | Integrating spatially/temporally separated sources | Text far from diagram |
| Redundancy | Processing identical information in multiple formats | Narration duplicating on-screen text |
| Transient information | Information disappears before processing completes | Fast animations without pause |
| Expertise reversal | Scaffolding that helps novices but hinders experts | Forced step-by-step for advanced users |
| Seductive details | Interesting but irrelevant information | Decorative images, tangential stories |

### Step 3 — Optimize Load Distribution

Strategies to manage total cognitive load:
- **Worked examples**: reduce intrinsic load for novices by showing solved problems
- **Fading**: gradually transition from worked examples to independent problem-solving
- **Modality effect**: use dual channels (visual + auditory) to expand effective WM capacity
- **Segmenting**: break complex material into learner-paced segments
- **Pre-training**: teach component elements before introducing interactions
- **Eliminate redundancy**: remove duplicate information across channels

### Step 4 — Design for Germane Load

- Encourage self-explanation and elaboration
- Use variability in practice problems to promote schema abstraction
- Provide comparison cases that highlight structural similarities
- Space practice over time (distributed practice) for schema consolidation

## Output Format

```markdown
## Cognitive Load Analysis: [Context]

### Intrinsic Load Assessment
- Element interactivity: [Low/Medium/High]
- Key interacting elements: [list]
- Learner expertise level: [Novice/Intermediate/Expert]

### Extraneous Load Audit
| Source | Present? | Severity | Fix |
|--------|----------|----------|-----|
| Split-attention | [Yes/No] | [High/Med/Low] | [solution] |
| Redundancy | [Yes/No] | [High/Med/Low] | [solution] |
| Transient info | [Yes/No] | [High/Med/Low] | [solution] |
| Seductive details | [Yes/No] | [High/Med/Low] | [solution] |

### Load Budget
- Estimated total load: [Within/Exceeding capacity]
- Extraneous reduction potential: [High/Medium/Low]

### Redesign Recommendations
1. [Primary extraneous load reduction]
2. [Segmenting or sequencing change]
3. [Germane load enhancement]
```

## Gotchas

- The expertise reversal effect means that designs optimal for novices actively harm experts — adaptive or layered design is necessary
- "7 +/- 2" is a rough heuristic; effective WM capacity for novel interacting elements may be as low as 3-4 chunks
- Germane load is debated in recent literature — some researchers subsume it under intrinsic load management rather than treating it as separate
- Reducing extraneous load is always beneficial; reducing intrinsic load may oversimplify and prevent deep learning
- Modality effect applies only when visual and auditory channels carry complementary (not redundant) information
- Cognitive load is difficult to measure directly — proxy measures (performance, subjective ratings, secondary tasks) each have limitations

## References

- Sweller, J. (1988). Cognitive load during problem solving: effects on learning. *Cognitive Science*, 12(2), 257-285.
- Sweller, J., Ayres, P. & Kalyuga, S. (2011). *Cognitive load theory*. Springer.
- Paas, F., Renkl, A. & Sweller, J. (2003). Cognitive load theory and instructional design: recent developments. *Educational Psychologist*, 38(1), 1-4.
