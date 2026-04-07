# Frame Analysis Coding Methodology

## Overview

Systematic frame analysis requires a reproducible coding scheme. This guide covers both inductive (emergent) and deductive (theory-driven) approaches.

## Approach 1: Deductive (Theory-Driven)

Use when an existing frame typology fits your research question.

### Common Generic Frames (Semetko & Valkenburg, 2000)

| Frame | Definition | Coding Question |
|-------|------------|----------------|
| **Conflict** | Emphasizes disagreement between individuals/groups | Does the story reflect disagreement between parties? |
| **Human Interest** | Personalizes, emotionalizes | Does the story contain a personal story or emotional angle? |
| **Economic Consequences** | Focuses on financial impacts | Does the story mention financial losses/gains? |
| **Morality** | Puts event in religious/moral context | Does the story contain moral messages or religious references? |
| **Responsibility** | Attributes cause/solution to individuals or government | Does the story suggest who is responsible? |

### Coding Procedure

1. Define the unit of analysis (article, paragraph, sentence)
2. For each unit, mark presence/absence of each frame (binary) or intensity (1-5 scale)
3. Use at least 2 coders, compute intercoder reliability (Krippendorff's α > 0.80)
4. Resolve disagreements through discussion, not averaging
5. Report reliability statistics in all publications

## Approach 2: Inductive (Emergent)

Use when you don't know in advance what frames exist.

### Entman's Four Functions

Every frame performs up to four functions. Code each text for:
1. **Problem definition**: What is the issue?
2. **Causal interpretation**: What caused it?
3. **Moral evaluation**: Is it good or bad? For whom?
4. **Treatment recommendation**: What should be done?

Frames emerge from the patterns of co-occurring answers across texts.

### Procedure

1. **Open coding**: Read a subset (~20% of sample) and note every framing element
2. **Cluster**: Group similar elements into candidate frames
3. **Define**: Write clear definitions with inclusion/exclusion criteria
4. **Test**: Apply candidate frames to new texts
5. **Refine**: Merge, split, or redefine frames based on fit
6. **Finalize**: Lock the coding scheme
7. **Code systematically**: Apply to the full sample

## Key Frame Elements to Code

| Element | What to Look For |
|---------|-----------------|
| **Keywords** | Recurring phrases that signal the frame |
| **Metaphors** | "War on X", "Epidemic of Y" |
| **Exemplars** | Which cases are highlighted as representative |
| **Depictions** | How are actors portrayed (hero/villain/victim) |
| **Sources** | Who gets quoted, who doesn't |
| **Visual images** | Photos, graphics that reinforce the frame |

## Intercoder Reliability

| Metric | Use When | Acceptable Level |
|--------|----------|-----------------|
| **Percent agreement** | Nominal, 2 coders | Not sufficient alone |
| **Cohen's κ** | Nominal, 2 coders | > 0.80 |
| **Fleiss' κ** | Nominal, 3+ coders | > 0.80 |
| **Krippendorff's α** | Any data type, missing data | > 0.80 (good), > 0.67 (minimum) |

## Common Coding Errors

1. **Double-counting**: Same element coded under multiple frames without justification
2. **Researcher bias**: Only seeing frames that confirm hypotheses
3. **Insufficient training**: Coders apply criteria inconsistently
4. **Mixing inductive and deductive**: Starting deductive but drifting to inductive without documentation
5. **Ignoring visual frames**: Photos and graphics often frame more powerfully than text

## Software Tools

- **NVivo**: Qualitative coding with inter-coder comparison
- **ATLAS.ti**: Similar to NVivo, strong for visual analysis
- **R package `irr`**: Computes reliability statistics
- **Python `nltk` + manual coding**: For large-scale automated pre-filtering

## References

- Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51-58.
- Semetko, H. A., & Valkenburg, P. M. (2000). Framing European politics. *Journal of Communication*, 50(2), 93-109.
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology* (4th ed.).
