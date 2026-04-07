---
name: "algo-mfg-doe"
description: "Design and analyze factorial experiments to identify significant process factors and optimize settings. Use this skill when the user needs to systematically test factor effects, optimize a manufacturing process, or determine which variables matter most — even if they say 'which factors affect quality', 'optimize process settings', or 'design an experiment'."
metadata:
  category: "WP-48 製造演算法"
  tags: ["manufacturing", "doe", "factorial-design", "optimization"]
---

# Design of Experiments (DOE)

## Overview

DOE systematically varies process factors to identify their effects on responses. Full factorial tests all combinations; fractional factorial tests a strategic subset. Identifies main effects and interactions. More efficient than one-factor-at-a-time (OFAT) which misses interactions. Uses ANOVA for analysis.

## When to Use

**Trigger conditions:**
- Identifying which process factors significantly affect quality/yield
- Optimizing process settings for target performance
- Screening many factors to find the vital few

**When NOT to use:**
- When the process is not stable (stabilize with SPC first)
- For observational data with no ability to manipulate factors

## Algorithm

```
IRON LAW: One-Factor-At-A-Time (OFAT) MISSES Interactions
Changing one factor while holding others fixed cannot detect
interactions (where the effect of A depends on the level of B).
Full factorial or fractional factorial designs test ALL main effects
AND interactions in fewer runs than OFAT. A 2³ factorial (8 runs)
gives more information than 6 OFAT runs at lower cost.
```

### Phase 1: Input Validation
Define: response variable(s), factors (2-7 practical), levels per factor (usually 2 for screening, 3 for optimization), constraints, noise factors.
**Gate:** Factors and levels defined, practical to run all experimental conditions.

### Phase 2: Core Algorithm
**Screening (many factors):** 2^(k-p) fractional factorial. Choose resolution III+ (main effects not confounded with each other).

**Optimization (few factors):** 2^k full factorial or central composite design (CCD) for response surface.

1. Generate design matrix (run order, factor level assignments)
2. Randomize run order (critical for validity)
3. Execute experiments, record responses
4. Analyze: ANOVA for factor significance, effect plots, interaction plots
5. If optimizing: fit response surface model, find optimal settings

### Phase 3: Verification
Check: R² of model is adequate, residuals are normally distributed and random. Confirmation runs at predicted optimal settings match prediction.
**Gate:** Model is significant, residuals OK, confirmation runs pass.

### Phase 4: Output
Return significant factors, effects, and optimal settings.

## Output Format

```json
{
  "significant_factors": [{"factor": "temperature", "effect": 12.5, "p_value": 0.001}, {"factor": "pressure", "effect": -8.2, "p_value": 0.008}],
  "interactions": [{"factors": "temperature×time", "effect": 5.1, "p_value": 0.03}],
  "optimal": {"temperature": 180, "pressure": 50, "time": 30, "predicted_response": 95.2},
  "metadata": {"design": "2^3_full_factorial", "runs": 8, "replicates": 2, "r_squared": 0.94}
}
```

## Examples

### Sample I/O
**Input:** 3 factors (temperature, pressure, time), each at 2 levels, response = yield
**Expected:** 2³ = 8 runs + replicates. ANOVA reveals temperature and temp×pressure interaction are significant.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| 7+ factors | Fractional factorial | Full factorial too expensive (2⁷=128 runs) |
| Factors with constraints | Constrained design | Some factor combinations may be physically impossible |
| Non-linear response | CCD or Box-Behnken | 2-level designs only fit linear models |

## Gotchas

- **Randomization is critical**: Without randomization, time-varying factors (operator fatigue, ambient temperature) confound results. ALWAYS randomize run order.
- **Replication vs repetition**: Replication (re-setup and re-run) estimates error. Repetition (multiple measurements from one run) does not. Include true replicates.
- **Alias structure**: Fractional factorials confound some effects. Know which effects are aliased (confounded) before interpreting results.
- **Center points**: Adding center points to a 2-level design detects curvature (non-linearity) at minimal cost. Always include 3-5 center points.
- **Practical significance vs statistical significance**: A factor can be statistically significant (p<0.05) but practically unimportant (tiny effect). Focus on effect SIZE, not just p-values.

## References

- For fractional factorial design tables, see `references/fractional-tables.md`
- For response surface methodology (RSM), see `references/rsm.md`
