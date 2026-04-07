---
name: "algo-mfg-cpk"
description: "Calculate Cpk process capability index to assess whether a process meets specification requirements. Use this skill when the user needs to evaluate process capability, compare processes, or determine if quality targets are achievable — even if they say 'can our process meet spec', 'process capability', or 'Cpk calculation'."
metadata:
  category: "WP-48 製造演算法"
  tags: ["manufacturing", "cpk", "process-capability", "quality"]
---

# Cpk Process Capability Index

## Overview

Cpk measures how well a process fits within specification limits, accounting for both variation (spread) and centering. Cpk = min((USL - μ) / 3σ, (μ - LSL) / 3σ). Cpk ≥ 1.33 is typically required; Cpk ≥ 1.67 for critical characteristics. Unlike Cp, Cpk penalizes off-center processes.

## When to Use

**Trigger conditions:**
- Assessing whether a manufacturing process can meet customer specifications
- Comparing capability across processes, machines, or time periods
- Qualifying a process for production readiness

**When NOT to use:**
- When the process is not in statistical control (stabilize first with SPC)
- For non-normal distributions without transformation

## Algorithm

```
IRON LAW: Cpk Is Only Valid for a STABLE, IN-CONTROL Process
Computing Cpk on an unstable process gives a meaningless number.
The process MUST be in statistical control (per SPC charts) before
capability analysis. An unstable process with Cpk=2.0 today may
produce defects tomorrow when it shifts.
```

### Phase 1: Input Validation
Collect: 100+ measurements from a stable process. Determine: USL, LSL (customer specifications). Verify process is in control (SPC charts show stability).
**Gate:** Process in control, specifications defined, 100+ data points.

### Phase 2: Core Algorithm
1. Compute process mean: μ = Σxᵢ / n
2. Compute process standard deviation: σ = estimated from R-bar/d₂ or S-bar/c₄ (within-subgroup) — NOT overall std dev
3. Cp = (USL - LSL) / 6σ (potential capability, ignoring centering)
4. Cpk = min((USL - μ) / 3σ, (μ - LSL) / 3σ) (actual capability)
5. Estimate PPM defective from Cpk (e.g., Cpk=1.33 → ~63 PPM)

### Phase 3: Verification
Check: Cp vs Cpk difference indicates centering issue (Cp >> Cpk = off-center). Distribution is approximately normal (histogram, normality test).
**Gate:** Capability computed, centering assessed, normality verified.

### Phase 4: Output
Return capability indices with defect rate estimates.

## Output Format

```json
{
  "capability": {"cp": 1.8, "cpk": 1.45, "ppm_defective": 27},
  "centering": {"mean": 50.2, "target": 50.0, "offset_pct": 0.4},
  "specs": {"usl": 55, "lsl": 45, "target": 50},
  "metadata": {"samples": 200, "sigma_method": "rbar_d2", "normality_p": 0.35}
}
```

## Examples

### Sample I/O
**Input:** USL=55, LSL=45, μ=50.2, σ=1.5
**Expected:** Cp = (55-45)/(6×1.5) = 1.11. Cpk = min((55-50.2)/4.5, (50.2-45)/4.5) = min(1.07, 1.16) = 1.07. Below 1.33 target.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| μ exactly at target | Cp = Cpk | Perfectly centered |
| μ outside specs | Cpk < 0 | Process mean beyond specification limit |
| One-sided spec only | Use Cpk for that side only | e.g., surface finish has only USL |

## Gotchas

- **σ estimation method**: Use within-subgroup σ (R̄/d₂), NOT overall σ. Overall σ includes between-subgroup variation that inflates σ and understates Cpk.
- **Non-normal data**: Cpk assumes normality. For skewed data (surface finish, concentricity), use Box-Cox transformation or non-parametric capability indices.
- **Short-term vs long-term**: Cp/Cpk are short-term (within subgroup variation). Pp/Ppk use overall variation (long-term). Customers often want Ppk.
- **Sample size confidence**: Cpk from 30 samples has wide confidence intervals. Report confidence intervals alongside point estimates.
- **Cpk ≠ defect-free**: Even Cpk=2.0 has a theoretical defect rate (~0.002 PPM). For ultra-critical applications, higher Cpk or process validation is required.

## Scripts

| Script | Description | Usage |
|--------|-------------|-------|
| `scripts/cpk.py` | Compute Cp, Cpk, Cpm, and PPM defective from process data | `python scripts/cpk.py --help` |

Run `python scripts/cpk.py --verify` to execute built-in sanity tests.

## References

- For Cp/Cpk/Pp/Ppk comparison, see `references/capability-indices.md`
- For non-normal capability analysis, see `references/non-normal-capability.md`
