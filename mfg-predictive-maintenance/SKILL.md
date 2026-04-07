---
name: "mfg-predictive-maintenance"
description: "Design predictive maintenance strategies using sensor data, ML models for remaining useful life (RUL), and the P-F curve framework. Use this skill when the user needs to reduce unplanned downtime, transition from reactive to predictive maintenance, evaluate sensor/IoT investments, or estimate equipment failure probability — even if they say 'machines keep breaking down', 'when will this equipment fail', 'should we invest in IoT sensors', or 'reduce unplanned downtime'."
metadata:
  category: "WP-03 製造業"
  tags: ["manufacturing", "predictive-maintenance", "iot", "reliability"]
---

# Predictive Maintenance

## Framework

```
IRON LAW: Predictive > Preventive > Reactive (but each has its place)

Reactive (fix after failure): cheapest per-event, most expensive in downtime
Preventive (fix on schedule): prevents some failures, causes unnecessary maintenance
Predictive (fix based on condition): lowest total cost, requires sensor investment

Not ALL equipment justifies predictive maintenance. Apply to equipment where
unplanned downtime cost >> sensor investment cost.
```

### Maintenance Strategy Comparison

| Strategy | When to Maintain | Advantage | Disadvantage | Best For |
|----------|-----------------|-----------|-------------|----------|
| **Reactive** | After failure | Zero upfront cost | Max downtime, safety risk | Non-critical, cheap-to-replace equipment |
| **Preventive** | On schedule (time/cycles) | Predictable, simple | Over-maintenance (replacing parts that still work) | Equipment with known wear patterns |
| **Predictive** | Based on condition data | Minimize downtime AND maintenance cost | Requires sensors, data infrastructure, models | Critical, expensive, failure-has-cascading-effect equipment |

### P-F Curve (Potential Failure → Functional Failure)

```
Condition
  │
  │  ●─── P (Potential failure detected by sensor)
  │     ╲
  │      ╲  ← P-F Interval (time to act)
  │       ╲
  │        ● F (Functional failure — equipment stops)
  │
  └──────────────────── Time

The P-F interval is your window of opportunity. Detect at P, schedule
repair before F. The longer the P-F interval, the more planning time.
```

### Sensor Data Types

| Data Type | What It Detects | Equipment |
|-----------|----------------|-----------|
| **Vibration** | Bearing wear, imbalance, misalignment | Rotating machinery (motors, pumps, turbines) |
| **Temperature** | Overheating, friction, electrical faults | Motors, transformers, bearings |
| **Current/Power** | Load changes, electrical degradation | Electric motors, drives |
| **Acoustic** | Leaks, cavitation, micro-cracks | Pressure systems, pipes, valves |
| **Oil analysis** | Wear particles, contamination | Gearboxes, hydraulic systems |

### ML Models for RUL (Remaining Useful Life)

| Approach | Method | Data Required |
|----------|--------|-------------|
| **Statistical** | Weibull distribution, exponential degradation | Historical failure times |
| **Classical ML** | Random Forest, Gradient Boosting on sensor features | Labeled run-to-failure datasets |
| **Deep Learning** | LSTM, 1D-CNN on raw sensor time series | Large volumes of sensor data |
| **Anomaly Detection** | Isolation Forest, Autoencoder | Normal operation data only (no failure labels needed) |

### Implementation Steps

**Phase 1: Select Equipment** (criticality analysis)
- Which equipment has highest downtime cost?
- Which has cascading failure effects?
- Prioritize: high cost × high frequency

**Phase 2: Install Sensors**
- Match sensor type to failure mode (see table above)
- Establish data pipeline: sensor → edge/cloud → storage

**Phase 3: Build Baseline**
- Collect 3-6 months of normal operation data
- Establish "healthy" patterns

**Phase 4: Develop Models**
- Start simple: threshold-based alerts (vibration > X = warning)
- Graduate to ML models as data accumulates
- Anomaly detection if you have few/no failure examples

**Phase 5: Operationalize**
- Integrate alerts into maintenance workflow (CMMS)
- Define response procedures for each alert level
- Measure: reduction in unplanned downtime, maintenance cost savings

### ROI Calculation

```
Annual Savings = (Unplanned downtime hours reduced × Downtime cost/hour)
               + (Preventive maintenance events avoided × Cost per event)
               - (Sensor + infrastructure + model development cost)
```

## Output Format

```markdown
# Predictive Maintenance Plan: {Equipment/Line}

## Equipment Criticality
| Equipment | Downtime Cost/hr | Failure Frequency | Cascading? | Priority |
|-----------|-----------------|-------------------|-----------|---------|
| {name} | ${X} | {X/year} | Y/N | H/M/L |

## Sensor Plan
| Equipment | Failure Mode | Sensor Type | P-F Interval |
|-----------|-------------|-------------|-------------|
| {name} | {mode} | {sensor} | {est. hours/days} |

## Projected ROI
| Metric | Before | After | Savings |
|--------|--------|-------|---------|
| Unplanned downtime | {hrs/year} | {hrs/year} | ${X}/year |
| Maintenance cost | ${X}/year | ${X}/year | ${X}/year |
| Sensor investment | — | ${X} one-time | Payback: {months} |
```

## Gotchas

- **Start with vibration monitoring**: It's the most mature, best-understood predictive technique. 80% of rotating equipment failures can be predicted by vibration analysis alone.
- **Data quality > model complexity**: A simple threshold alert on clean sensor data outperforms a sophisticated ML model on noisy, incomplete data. Fix data quality first.
- **False positives kill adoption**: If the model cries wolf too often, maintenance teams ignore it. Tune for high precision (few false alarms) even at the cost of some missed detections early on.
- **Cultural change is harder than technology**: Shifting from "run to failure" culture requires management buy-in and maintenance team training. Technology alone won't change behavior.

## References

- For sensor selection guide by equipment type, see `references/sensor-guide.md`
- For LSTM-based RUL model tutorial, see `references/rul-tutorial.md`
