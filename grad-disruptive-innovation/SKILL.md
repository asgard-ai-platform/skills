---
name: "grad-disruptive-innovation"
description: "Apply Christensen's Disruptive Innovation theory to assess low-end and new-market threats to incumbents. Use this skill when the user needs to evaluate whether a new entrant poses a disruptive threat, analyze why incumbents fail against inferior-but-cheaper alternatives, or design a disruption strategy targeting overserved customers."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["disruptive-innovation", "christensen", "low-end-disruption", "new-market-foothold", "sustaining-innovation", "incumbent-failure"]
---

# Disruptive Innovation (Christensen, 1997)

## Overview

Disruptive Innovation theory explains how smaller firms with fewer resources can successfully challenge established incumbents. Disruption occurs when entrants target overlooked segments (low-end or non-consumers) with simpler, cheaper offerings, then move upmarket as performance improves. Incumbents rationally focus on profitable mainstream customers and fail to respond until it is too late.

## When to Use

**Trigger conditions:**
- User asks why a startup with an inferior product is gaining market share
- User needs to evaluate whether a new entrant is a disruptive or sustaining threat
- User wants to design a market entry strategy targeting overserved customers
- User mentions "disruption", "low-end market", or "good enough product"

**When NOT to use:**
- For sustaining innovation management (incremental improvements) -> use stage-gate or innovation funnel
- For platform-based competition -> use grad-platform-economics
- For analyzing national-level innovation systems -> use grad-diamond

## Assumptions

```
IRON LAW: Disruption Comes from BELOW

Disruption originates from the LOW END or NEW MARKET — never from a
superior product attacking head-on. Incumbents fail because they
OVER-SERVE mainstream customers, creating a performance overshoot that
opens space for simpler, cheaper alternatives.

If the entrant competes on the SAME performance dimensions as the
incumbent, it is sustaining innovation — NOT disruption.
```

- Performance trajectories improve faster than customer needs evolve
- Incumbents are rational — they chase higher margins upmarket
- Disrupted markets have identifiable overserved segments

## Methodology

### Step 1: Map Performance Trajectories

Plot the incumbent's performance improvement trajectory against the range of customer needs (low-end to high-end). Identify where performance overshoots what mainstream customers can absorb.

### Step 2: Identify the Foothold

Classify the entrant's strategy:
- **Low-end foothold**: Targets overserved customers with a cheaper, simpler, "good enough" product (e.g., discount airlines vs full-service carriers)
- **New-market foothold**: Targets non-consumers who previously could not access the product at all (e.g., personal computers vs mainframes)

### Step 3: Assess Disruption Potential

Evaluate three conditions:
1. **Performance overshoot exists** — mainstream customers do not use all features they pay for
2. **Entrant has an upmarket migration path** — the simpler product can improve over time
3. **Incumbent has asymmetric motivation** — responding means cannibalizing high-margin business

### Step 4: Recommend Response Strategy

For incumbents: autonomous business unit, acquire the disruptor, or create own low-end offering. For entrants: stay below the radar, improve incrementally, move upmarket only when ready.

## Output Format

```markdown
# Disruption Assessment: {Industry/Company}

## Performance Trajectory Analysis
- Incumbent performance vector: {key dimensions}
- Customer need threshold: {what "good enough" looks like}
- Overshoot zone: {where incumbent exceeds needs}

## Entrant Classification
- Type: Low-end foothold / New-market foothold / Sustaining (NOT disruptive)
- Target segment: {who the entrant serves}
- Core advantage: {why target segment prefers entrant}

## Disruption Potential: High / Medium / Low
1. Performance overshoot: {Yes/No — evidence}
2. Upmarket path: {Yes/No — mechanism}
3. Asymmetric motivation: {Yes/No — why incumbent won't respond}

## Strategic Recommendations
- For incumbent: {specific response}
- For entrant: {next moves}
```

## Gotchas

- **Not every innovation is disruptive**: Uber was NOT disruptive to taxis by Christensen's definition — it started in the high end. Label precisely.
- **Disruption is a process, not an event**: It unfolds over years or decades. A snapshot analysis misses trajectory dynamics.
- **Incumbents CAN respond**: Disruption is not inevitable. Autonomous business units (e.g., IBM PC division) can counter disruption.
- **Technology alone is not disruption**: The business model matters as much as the technology. A better mousetrap sold at higher prices is sustaining innovation.
- **Beware hindsight bias**: Many "disruption" narratives are retrofitted. Apply the framework prospectively with testable predictions.

## References

- For mathematical formalization of performance trajectories, see `references/performance-trajectory-model.md`
- For case studies (steel minimills, disk drives), see `references/disruption-cases.md`
