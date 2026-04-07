---
name: "mfg-oee-analysis"
description: "Calculate and diagnose Overall Equipment Effectiveness (OEE) by decomposing into Availability, Performance, and Quality rates. Use this skill when the user needs to measure production line efficiency, identify equipment losses, benchmark manufacturing performance, or justify capital investment — even if they say 'why is our output low', 'machine utilization report', 'production efficiency', or 'how much capacity are we losing'."
metadata:
  category: "WP-03 製造業"
  tags: ["manufacturing", "oee", "production-efficiency"]
---

# OEE Analysis

## Framework

```
IRON LAW: OEE = Availability × Performance × Quality

OEE is a MULTIPLICATIVE metric. 90% × 90% × 90% = 72.9%, not 90%.
Each factor compounds the loss. World-class OEE is 85%+. Most plants
operate at 60-65%. Knowing the TOTAL is useless — you must decompose
to find which factor is dragging performance down.
```

### The Three Factors

| Factor | Formula | Measures | Loss Categories |
|--------|---------|----------|----------------|
| **Availability** | Run Time / Planned Production Time | Uptime vs downtime | Equipment failures, changeovers, material shortages |
| **Performance** | (Ideal Cycle Time × Total Count) / Run Time | Actual speed vs design speed | Minor stops, slow running, idling |
| **Quality** | Good Count / Total Count | Yield, first-pass quality | Defects, rework, scrap, startup rejects |

### Six Big Losses (mapped to OEE factors)

| Loss | OEE Factor | Example |
|------|-----------|---------|
| 1. Equipment failure | Availability | Machine breakdown, unplanned repair |
| 2. Setup & changeover | Availability | Product changeover, die change, cleaning |
| 3. Idling & minor stops | Performance | Sensor blockage, jam clearing, small adjustments |
| 4. Reduced speed | Performance | Running below rated speed due to wear or material |
| 5. Process defects | Quality | In-process rejects, rework |
| 6. Startup rejects | Quality | Scrap during warm-up, first-article failures |

### Calculation Example

```
Planned Production Time: 480 min (8-hour shift)
Downtime (breakdowns + changeover): 60 min
Run Time: 420 min

Ideal Cycle Time: 1 min/unit
Total Units Produced: 380

Good Units: 360
Defective Units: 20

Availability = 420 / 480 = 87.5%
Performance = (1 × 380) / 420 = 90.5%
Quality = 360 / 380 = 94.7%

OEE = 87.5% × 90.5% × 94.7% = 75.0%
```

### Diagnosis Steps

**Phase 1: Calculate OEE** for each production line/machine
**Phase 2: Identify the weakest factor** (Availability, Performance, or Quality)
**Phase 3: Pareto the losses** within that factor (which specific loss is biggest?)
**Phase 4: Root cause analysis** on the top loss (5 Whys, fishbone)
**Phase 5: Improve** and remeasure

### Benchmarks

| OEE Level | Rating | Typical |
|-----------|--------|---------|
| > 85% | World-class | Top manufacturers |
| 60-85% | Typical | Room for improvement |
| 40-60% | Low | Significant losses, urgent action needed |
| < 40% | Critical | Equipment or process fundamentally broken |

## Output Format

```markdown
# OEE Report: {Production Line}

## OEE Summary
| Factor | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Availability | {%} | >90% | 🟢/🟡/🔴 |
| Performance | {%} | >95% | 🟢/🟡/🔴 |
| Quality | {%} | >99% | 🟢/🟡/🔴 |
| **OEE** | **{%}** | **>85%** | 🟢/🟡/🔴 |

## Loss Breakdown
| Loss | Minutes Lost | % of Total Loss | Priority |
|------|-------------|----------------|---------|
| {loss type} | {min} | {%} | 1/2/3 |

## Root Cause (Top Loss)
{5 Whys or fishbone analysis}

## Improvement Plan
| Action | Target Impact | Timeline | Owner |
|--------|-------------|----------|-------|
| {action} | +{X%} OEE | {weeks} | {who} |
```

## Gotchas

- **OEE is per machine, not per plant**: Plant-level OEE averages hide that one machine at 95% and another at 45% average to 70%. Analyze individually.
- **Planned downtime is excluded**: OEE measures losses against PLANNED production time. Scheduled maintenance, no-production shifts, and planned shutdowns are excluded from the denominator.
- **100% OEE is not the goal**: It would mean zero changeovers, zero defects, running at max speed 100% of the time. Pursuing 100% can increase costs (e.g., never doing preventive maintenance). Target 85%+ for critical lines.
- **Data collection is the real challenge**: Manual OEE tracking is inaccurate. Invest in automated data collection (sensors, MES integration) for reliable measurement.

## References

- For TPM (Total Productive Maintenance) methodology, see `references/tpm.md`
- For automated OEE data collection, see `references/oee-automation.md`
