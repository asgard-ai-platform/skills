---
name: "grad-meta-analysis"
description: "Apply meta-analysis to synthesize effect sizes across multiple studies, assess heterogeneity, and evaluate publication bias. Use this skill when the user needs to combine findings from prior research, compare fixed-effect vs random-effects models, compute pooled effect sizes, or when they ask 'what does the overall evidence say', 'how do I combine results across studies', or 'is there publication bias'."
metadata:
  category: "WP-31 量化方法"
  tags: ["meta-analysis", "effect-size", "heterogeneity", "publication-bias", "I-squared", "systematic-review"]
---

# 後設分析 (Meta-Analysis)

## Overview

Meta-analysis statistically combines effect sizes from multiple independent studies to produce a pooled estimate with greater precision and generalizability. It quantifies between-study heterogeneity and tests for publication bias, providing a rigorous evidence synthesis that goes beyond narrative literature reviews.

## When to Use

- Synthesizing quantitative findings from multiple studies on the same research question
- Resolving conflicting results across studies
- Estimating an overall effect size with tighter confidence intervals
- Identifying moderators that explain heterogeneity across studies

## When NOT to Use

- Studies are too heterogeneous in constructs, measures, or populations to combine meaningfully
- Fewer than 5 studies are available (pooled estimates become unreliable)
- Primary studies have fundamentally different research designs (mixing RCTs with observational)
- The research question is qualitative or conceptual rather than quantitative

## Assumptions

```
IRON LAW: A meta-analysis is only as good as the studies it includes —
garbage in, garbage out. Publication bias inflates pooled effect sizes
because non-significant findings go unpublished.
```

Key assumptions:
1. Studies estimate the same underlying construct (conceptual homogeneity)
2. Effect sizes are statistically independent (one effect per study, or use multilevel models)
3. Study-level moderators are coded reliably and without bias
4. The search strategy captures the relevant population of studies (no systematic omission)

## Methodology

### Step 1 — Extract and Code Effect Sizes

Convert study findings to a common effect size metric (Cohen's d, Hedges' g, r, OR). Code study-level moderators (sample size, design, context). See `references/` for conversion formulas.

### Step 2 — Choose Fixed-Effect vs Random-Effects Model

Fixed-effect assumes one true effect; random-effects assumes effects vary across studies. If studies span different populations or contexts, random-effects is almost always appropriate.

### Step 3 — Assess Heterogeneity

Compute Q statistic (test of homogeneity), I² (proportion of variance due to heterogeneity), and τ² (between-study variance). I² > 75% indicates substantial heterogeneity warranting moderator analysis.

### Step 4 — Test for Publication Bias and Report

Use funnel plot, Egger's regression test, and trim-and-fill method. Report pooled effect, CI, prediction interval, and results of bias assessment.

## Output Format

```markdown
## Meta-Analysis: [Research Question]

### Study Inclusion
| Criterion | Value |
|-----------|-------|
| Studies included (k) | xx |
| Total sample size (N) | xxxx |
| Effect size metric | [d / r / OR] |

### Pooled Effect Size
| Model | Effect | 95% CI | z | p-value |
|-------|--------|--------|---|---------|
| Fixed-effect | x.xx | [x.xx, x.xx] | x.xx | x.xx |
| Random-effects | x.xx | [x.xx, x.xx] | x.xx | x.xx |

### Heterogeneity
| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| Q | x.xx (p = x.xx) | [significant/not] |
| I² | x.xx% | [low/moderate/high] |
| τ² | x.xx | [between-study variance] |

### Publication Bias
| Test | Result | Interpretation |
|------|--------|----------------|
| Funnel plot | [symmetric/asymmetric] | [bias suspected?] |
| Egger's test | p = x.xx | [significant?] |
| Trim-and-fill | adjusted effect = x.xx | [studies imputed: x] |

### Limitations
- [Note any assumption violations]
```

## Gotchas

- Combining apples and oranges: statistically possible but conceptually meaningless if constructs differ
- Random-effects models give more weight to small studies, which are often lower quality
- I² depends on precision of included studies; low I² with imprecise studies does not mean homogeneity
- Funnel plot asymmetry can be caused by factors other than publication bias (small-study effects)
- File-drawer problem: unpublished null results are systematically missing
- Moderator analyses with many subgroups and few studies per subgroup are underpowered and unreliable

## References

- Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to Meta-Analysis*. Wiley.
- Higgins, J. P. T., & Thompson, S. G. (2002). Quantifying heterogeneity in a meta-analysis. *Statistics in Medicine*, 21(11), 1539-1558.
- Rothstein, H. R., Sutton, A. J., & Borenstein, M. (2005). *Publication Bias in Meta-Analysis*. Wiley.
