---
name: "biz-lean-six-sigma"
description: "Apply Lean and Six Sigma principles to eliminate waste and reduce process variation. Use this skill when the user needs to improve operational efficiency, identify the seven wastes (TIMWOOD), run DMAIC improvement projects, or streamline workflows — even if they say 'our process is too slow', 'where are we wasting resources', or 'how do we reduce defects'."
metadata:
  category: "WP-16 商學院—營運"
  tags: ["operations", "lean", "six-sigma", "process-improvement"]
---

# Lean Six Sigma

## Overview

Lean eliminates waste (non-value-adding activities). Six Sigma reduces variation (defects and inconsistency). Combined, they improve speed AND quality. Lean answers "are we doing unnecessary things?" Six Sigma answers "are we doing necessary things consistently?"

## Framework

```
IRON LAW: Value Is Defined by the CUSTOMER, Not the Producer

An activity adds value ONLY if: (1) the customer is willing to pay for it,
(2) it transforms the product/service, AND (3) it's done right the first time.
If any condition fails, the activity is waste — eliminate or minimize it.
```

### The Seven Wastes (TIMWOOD)

| Waste | Definition | Example |
|-------|-----------|---------|
| **T**ransportation | Unnecessary movement of materials | Moving inventory between warehouses |
| **I**nventory | Excess stock beyond immediate need | 6 months of raw materials sitting idle |
| **M**otion | Unnecessary movement of people | Walking across factory floor to get tools |
| **W**aiting | Idle time between process steps | Orders waiting for approval |
| **O**ver-production | Making more than needed | Printing 1000 reports when 100 are read |
| **O**ver-processing | More work than the customer requires | Triple-checking a non-critical form |
| **D**efects | Output that requires rework or disposal | Software bugs, manufacturing rejects |

### DMAIC Improvement Cycle (Six Sigma)

1. **Define**: What is the problem? Who is the customer? What is the target metric?
2. **Measure**: What is the current performance? Collect data on defect rate, cycle time, variation.
3. **Analyze**: What causes the problem? Use root cause analysis (5 Whys, fishbone diagram, Pareto chart).
4. **Improve**: What changes will fix it? Design and test solutions.
5. **Control**: How to sustain the improvement? Implement monitoring, SOPs, control charts.

### Kaizen (Continuous Improvement)

Small, incremental improvements made continuously by frontline workers:
- Daily standup to identify one improvement
- Implement immediately if possible
- Document and share across teams

## Output Format

```markdown
# Lean Six Sigma Analysis: {Process}

## Current State
- Process: {description}
- Key metric: {defect rate / cycle time / cost}
- Current performance: {baseline data}

## Waste Identification (TIMWOOD)
| Waste Type | Found? | Description | Impact |
|-----------|--------|-------------|--------|
| Transportation | Y/N | {detail} | H/M/L |
| Inventory | Y/N | ... | ... |
| Motion | Y/N | ... | ... |
| Waiting | Y/N | ... | ... |
| Over-production | Y/N | ... | ... |
| Over-processing | Y/N | ... | ... |
| Defects | Y/N | ... | ... |

## Root Cause Analysis
{5 Whys or fishbone diagram for top waste}

## Improvement Plan (DMAIC)
| Phase | Action | Owner | Timeline |
|-------|--------|-------|----------|
| Define | {problem statement} | ... | ... |
| Measure | {data collection plan} | ... | ... |
| Analyze | {root cause method} | ... | ... |
| Improve | {solution} | ... | ... |
| Control | {monitoring plan} | ... | ... |

## Expected Impact
- {metric}: {current} → {target} ({X% improvement})
```

## Examples

### Correct Application
**Scenario:** Lean analysis of a restaurant kitchen order process
- **Waiting waste**: Orders wait 8 min for expeditor to batch them → Change to real-time ticket system (saves 6 min/order)
- **Motion waste**: Chef walks 15m to reach cold storage per order → Relocate prep station fridge (saves 2 min)
- **Defect waste**: 12% order error rate → Implement kitchen display system with visual confirmation (target 3%)
- Root cause (5 Whys): Errors → handwritten tickets �� poor handwriting → no standardized format �� **no digital order system**

### Incorrect Application
- Identified "the market is declining" as a waste → Market conditions are external, not process waste. TIMWOOD applies to internal processes only.

## Gotchas

- **8th waste — unused talent**: Often added to TIMWOOD. Employees with ideas that aren't heard or skills that aren't utilized.
- **Lean can go too far**: Eliminating ALL inventory (zero buffer) creates fragility. Some "waste" is strategic buffer. Balance efficiency with resilience.
- **Six Sigma requires data**: Without baseline measurements, you can't calculate improvement. Invest in measurement before jumping to solutions.
- **Cultural resistance**: Lean/Six Sigma requires frontline buy-in. Top-down mandates without worker involvement fail.

## References

- For value stream mapping methodology, see `references/value-stream-mapping.md`
- For statistical process control (SPC), see `references/spc-basics.md`
