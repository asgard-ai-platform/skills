---
name: "algo-mfg-spc"
description: "Implement Statistical Process Control charts to monitor production process stability. Use this skill when the user needs to detect process shifts, set control limits, or distinguish common cause from special cause variation — even if they say 'process monitoring', 'control chart', or 'is our process in control'."
metadata:
  category: "WP-48 製造演算法"
  tags: ["manufacturing", "spc", "control-chart", "quality"]
---

# Statistical Process Control

## Overview

SPC uses control charts to monitor process stability over time. Upper and Lower Control Limits (UCL/LCL) are set at ±3σ from the process mean. Points within limits = common cause variation (stable). Points outside or showing patterns = special cause variation (investigate). Primary charts: X-bar/R, X-bar/S, I-MR, p-chart, c-chart.

## When to Use

**Trigger conditions:**
- Monitoring production process for stability and detecting shifts
- Setting statistically-based control limits for quality metrics
- Distinguishing normal variation from assignable causes

**When NOT to use:**
- For process capability assessment (use Cpk)
- For root cause analysis of known problems (use fishbone/5-why)

## Algorithm

```
IRON LAW: Control Limits Are NOT Specification Limits
Control limits (±3σ) describe what the process IS doing.
Specification limits describe what the process SHOULD do.
A process can be in statistical control (stable) but still produce
out-of-spec products (incapable). Conversely, a capable process may
be out of control (drifting). Monitor control FIRST, then assess capability.
```

### Phase 1: Input Validation
Collect: 25+ subgroups of measurements (5 per subgroup typical for X-bar/R). Verify: measurement system is adequate (gauge R&R < 10%), data collected in time order.
**Gate:** Sufficient subgroups, time-ordered data, measurement system verified.

### Phase 2: Core Algorithm
**X-bar/R Chart (subgroup data):**
1. Compute subgroup means (X̄) and ranges (R)
2. Compute grand mean (X̄̄) and average range (R̄)
3. UCL_X̄ = X̄̄ + A₂×R̄, LCL_X̄ = X̄̄ - A₂×R̄ (A₂ from statistical tables by subgroup size)
4. UCL_R = D₄×R̄, LCL_R = D₃×R̄
5. Plot points, apply Western Electric rules for out-of-control signals

### Phase 3: Verification
Check for: points outside limits, runs (7+ consecutive on one side), trends (7+ consecutive increasing/decreasing), 2 of 3 beyond 2σ, 4 of 5 beyond 1σ.
**Gate:** Chart constructed, out-of-control signals identified.

### Phase 4: Output
Return control chart data with signals and stability assessment.

## Output Format

```json
{
  "chart": {"type": "xbar_r", "center_line": 50.2, "ucl": 52.1, "lcl": 48.3},
  "signals": [{"subgroup": 18, "rule": "point_beyond_ucl", "value": 52.8}],
  "stability": "out_of_control",
  "metadata": {"subgroups": 30, "subgroup_size": 5}
}
```

## Examples

### Sample I/O
**Input:** 25 subgroups of 5 measurements each, all within ±3σ, no patterns
**Expected:** Process in control. No signals triggered.

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| One point just outside UCL | Signal, but may be false alarm | ~0.27% chance per point even when in control |
| Gradual upward trend | Trend rule triggered | Process drifting, investigate |
| All points near center | Suspicious — check data | May indicate data manipulation or measurement issue |

## Gotchas

- **Rational subgrouping**: Subgroups must be collected under similar conditions (same shift, machine, operator). Poor subgrouping inflates within-group variation, making limits too wide.
- **Recalculating limits**: Don't recalculate limits every time you add data. Establish limits from a stable baseline period and keep them fixed until a known process change.
- **Chart type selection**: Variables data (measurements) → X-bar/R or I-MR. Attribute data (counts/proportions) → p-chart, np-chart, c-chart, u-chart. Wrong chart type = wrong limits.
- **Normality assumption**: X-bar chart is robust to non-normality (central limit theorem). Individual charts (I-MR) require approximate normality — check with histogram.
- **Over-adjustment**: Reacting to every small variation (tampering) INCREASES variability. Only investigate special cause signals, not common cause variation.

## References

- For control chart constants tables, see `references/chart-constants.md`
- For Western Electric rules and pattern detection, see `references/we-rules.md`
