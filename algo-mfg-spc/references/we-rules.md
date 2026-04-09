# Western Electric Rules for Out-of-Control Signal Detection

Western Electric rules (WE rules) are pattern tests applied to a control chart to detect non-random signals that a ±3σ limit test alone would miss. Originally published in *Statistical Quality Control Handbook* (AT&T/Western Electric, 1956).

---

## Zone Definitions

Every WE rule depends on dividing the chart into zones relative to the center line (CL):

```
UCL  ─────────────────────────────  +3σ from CL
      Zone A  (between +2σ and +3σ)
      Zone B  (between +1σ and +2σ)
      Zone C  (between  CL  and +1σ)
CL   ─────────────────────────────
      Zone C  (between  CL  and −1σ)
      Zone B  (between −1σ and −2σ)
      Zone A  (between −2σ and −3σ)
LCL  ─────────────────────────────  −3σ from CL
```

For an X-bar chart, compute zone boundaries from the chart's own control limits:

```
+1σ boundary = CL + (UCL − CL) / 3
+2σ boundary = CL + 2 × (UCL − CL) / 3
```

Because UCL = CL + 3σ_X̄, each zone is exactly 1σ_X̄ wide.

---

## The Four Standard WE Rules

### Rule 1 — One point beyond ±3σ (Zone A or beyond)

**Trigger:** any single point falls outside the UCL or LCL.

```
●  ← signal (above UCL)
─────────────────  UCL
                   Zone A
─────────────────  +2σ
```

**False alarm probability (per point, process in control):** ≈ 0.27%  
Expect one false alarm roughly every 370 points.

---

### Rule 2 — Two of three consecutive points in Zone A or beyond (same side)

**Trigger:** within any window of 3 consecutive points, at least 2 fall at +2σ or beyond (or both at −2σ or beyond). Both points must be on the **same side** of CL.

```
Point index:  1    2    3
              ○    ●    ●   ← Rule 2 signal at point 3
              ──   ──   ──
              +1σ  +2σ  +2σ   (● = in Zone A or beyond)
```

**False alarm probability:** ≈ 0.39% per opportunity (each group of 3).

**Common mistake:** triggering this rule when the two Zone A points are on opposite sides of the center line. Opposite-side Zone A points suggest high variance, not a process shift — investigate differently.

---

### Rule 3 — Four of five consecutive points in Zone B or beyond (same side)

**Trigger:** within any window of 5 consecutive points, at least 4 fall at +1σ or beyond (or at −1σ or beyond, same side).

```
Point index:  1    2    3    4    5
              ●    ○    ●    ●    ●   ← Rule 3 signal at point 5
              +1σ  CL   +1σ  +1σ  +2σ  (● = Zone B or beyond on upper side)
```

The 1 point allowed to be in Zone C or the other side gives this rule tolerance for noise.

**False alarm probability:** ≈ 0.54% per opportunity.

---

### Rule 4 — Eight consecutive points on one side of the center line

**Trigger:** 8 (or more) consecutive points all above CL, or all below CL. Points may be anywhere — Zone C through Zone A — as long as none cross the center line.

```
● ● ● ● ● ● ● ●   ← all above CL, Rule 4 signal at 8th point
─────────────────  CL
```

**False alarm probability:** ≈ 0.39% per opportunity of 8 consecutive points.

**Note on run length:** Some practitioners use 7 instead of 8. The original Western Electric handbook specifies 8. AIAG's SPC manual and Montgomery's *Introduction to Statistical Quality Control* both use 8 for the run-on-one-side rule. If your shop standard uses 7, document it explicitly and apply consistently.

---

## Rules 5–8 (Supplemental — Common Additions)

These are not in the original 1956 WE handbook but appear widely in software (Minitab, JMP) and AIAG SPC references. Use them deliberately; each additional rule increases the false alarm rate.

### Rule 5 — Six points in a row steadily increasing or decreasing (trend)

**Trigger:** 6 consecutive points each strictly higher than the previous (or each strictly lower). Points need not cross zone boundaries.

```
●
  ●
    ●
      ●
        ●
          ●   ← Rule 5 signal at 6th point
```

**Note:** Some references use 7 points for trend; the SKILL.md uses 7. Whichever you choose, "strictly monotone" is the criterion — ties break the streak.

---

### Rule 6 — Fifteen points in a row within Zone C (both sides)

**Trigger:** 15 consecutive points all between +1σ and −1σ.

This signals *reduced* variation, which sounds good but often indicates:
- Measurement system problem (rounding, limited gauge resolution)
- Data fabrication or improper subgrouping (mixing two processes so within-group variation inflates limits artificially)
- A genuine process improvement — verify by checking raw data and measurement logs

---

### Rule 7 — Fourteen points in a row alternating up and down

**Trigger:** each point alternates direction — up, down, up, down — for 14 consecutive points.

Signals systematic oscillation. Common causes: two alternating machines, two alternating operators, measurement order following a fixture rotation.

---

### Rule 8 — Eight points in a row on both sides of CL with none in Zone C

**Trigger:** 8 consecutive points, all in Zone B or A (above or below), with no point in Zone C.

Signals bimodal data — two process streams mixed into one chart. Check for machine-to-machine, shift-to-shift, or cavity-to-cavity stratification.

---

## False Alarm Rate Accumulates with Rule Count

Each rule independently generates false alarms. Running all 8 rules simultaneously on a 25-subgroup baseline dramatically raises the probability of at least one false positive:

| Rules Active | Approx. False Alarm Rate (per 25 points) |
|---|---|
| Rule 1 only | ~6.7% |
| Rules 1–4 | ~20–25% |
| Rules 1–8 | ~40–50% |

**Practical recommendation:** Use Rules 1–4 as the default set. Add Rules 5–8 only when you have a specific hypothesis (e.g., Rule 6 if you suspect data fabrication, Rule 8 if you suspect multiple process streams).

---

## Detection Algorithm (Pseudocode)

```python
def check_we_rules(values: list[float], cl: float, sigma: float) -> list[dict]:
    """
    values: time-ordered sequence of plotted statistics (X-bar, individual, etc.)
    cl:     center line
    sigma:  one sigma of the plotted statistic (NOT of raw measurements)
    
    Returns list of signal dicts: {rule, index, value, description}
    """
    signals = []
    n = len(values)

    def zone(v):
        """Returns signed zone number: ±1=C, ±2=B, ±3=A, ±4=beyond UCL/LCL."""
        distance = (v - cl) / sigma
        sign = 1 if distance >= 0 else -1
        abs_d = abs(distance)
        if abs_d < 1:   return sign * 1
        if abs_d < 2:   return sign * 2
        if abs_d < 3:   return sign * 3
        return sign * 4

    zones = [zone(v) for v in values]

    for i in range(n):
        # Rule 1: beyond ±3σ
        if abs(zones[i]) >= 4:
            signals.append({"rule": 1, "index": i, "value": values[i],
                            "description": "Point beyond 3σ"})

        # Rule 2: 2 of 3 in Zone A or beyond, same side
        if i >= 2:
            w = zones[i-2:i+1]
            for side in [1, -1]:
                if sum(1 for z in w if z * side >= 3) >= 2:
                    signals.append({"rule": 2, "index": i, "value": values[i],
                                   "description": f"2 of 3 in Zone A ({'upper' if side>0 else 'lower'})"})
                    break

        # Rule 3: 4 of 5 in Zone B or beyond, same side
        if i >= 4:
            w = zones[i-4:i+1]
            for side in [1, -1]:
                if sum(1 for z in w if z * side >= 2) >= 4:
                    signals.append({"rule": 3, "index": i, "value": values[i],
                                   "description": f"4 of 5 in Zone B ({'upper' if side>0 else 'lower'})"})
                    break

        # Rule 4: 8 consecutive on one side
        if i >= 7:
            w = zones[i-7:i+1]
            if all(z > 0 for z in w) or all(z < 0 for z in w):
                signals.append({"rule": 4, "index": i, "value": values[i],
                               "description": "8 consecutive on one side of CL"})

        # Rule 5: 6 consecutive trending (strictly monotone)
        if i >= 5:
            w = values[i-5:i+1]
            if all(w[j] < w[j+1] for j in range(5)) or all(w[j] > w[j+1] for j in range(5)):
                signals.append({"rule": 5, "index": i, "value": values[i],
                               "description": "6 consecutive trend"})

    return signals
```

**Important:** `sigma` here is the sigma of the *plotted statistic*, derived from the average range or average standard deviation via the appropriate constant — NOT the raw process σ. For X-bar charts:

```
σ_X̄ = R̄ / (d₂ × √n)   [or equivalently (UCL_X̄ − CL) / 3]
```

---

## Worked Example

**Setup:** X-bar chart, n=5 per subgroup, 20 subgroups.

| Constants | Values |
|---|---|
| Grand mean X̄̄ | 50.00 |
| Average range R̄ | 3.60 |
| A₂ (n=5) | 0.577 |
| UCL_X̄ | 50.00 + 0.577×3.60 = **52.08** |
| LCL_X̄ | 50.00 − 0.577×3.60 = **47.92** |
| σ_X̄ | (52.08 − 50.00) / 3 = **0.693** |

Zone boundaries:

| Boundary | Value |
|---|---|
| +3σ (UCL) | 52.08 |
| +2σ | 51.39 |
| +1σ | 50.69 |
| CL | 50.00 |
| −1σ | 49.31 |
| −2σ | 48.61 |
| −3σ (LCL) | 47.92 |

Subgroup X-bar values (selected):

```
Subgroup:  1     2     3     4     5     6     7     8
X-bar:    50.1  50.4  50.8  51.0  51.2  50.9  51.4  51.5
Zone:     +C    +C    +B    +B    +B    +B    +B    +B
```

**Rule 3 check at subgroup 8** (window: subgroups 4–8):  
Zones: +B, +B, +B, +B, +B → 5 of 5 in Zone B or beyond (upper side) → **Rule 3 triggered** (4 of 5 threshold exceeded).

**Rule 4 check at subgroup 8** (window: subgroups 1–8):  
All 8 zones are positive → **Rule 4 triggered**.

Both signals fire simultaneously. Rule 4 indicates a sustained shift above CL; Rule 3 is redundant here. Report both but investigate as a single event: the process mean appears to have drifted upward starting around subgroup 3.

---

## Signal Prioritization

When multiple rules fire on the same chart simultaneously:

1. **Rule 1 overrides all others** — a point outside the control limit is the most definitive signal. Start investigation there.
2. **Rules 2 and 3** typically indicate a gradual shift earlier than Rule 4 catches it. If Rule 2 or 3 fires without Rule 1, the shift is subtle — trace back to the earliest point in the triggering window.
3. **Rule 4** (run on one side) confirms a sustained shift that Rules 2/3 already flagged. Reinforces rather than adds new information.
4. **Rules 5–8** are diagnostic — they indicate the *type* of disturbance (trend, stratification, oscillation). Use them to guide root cause hypotheses, not as primary action triggers.

---

## Common Misapplications

**Applying WE rules to R or S charts without adjustment:**  
The R chart is skewed (not symmetric around its center line), especially for small n. Rule 4's "8 on one side" is less meaningful because R values cluster below R̄ more often than above. For R and S charts, rely primarily on Rule 1 (beyond UCL) and Rule 5 (trend upward = increasing variation).

**Checking rules against specification limits instead of control limits:**  
Zone boundaries must be computed from ±σ_X̄ relative to CL, not from engineering tolerances. This is a direct consequence of the Iron Law in the parent skill.

**Running WE rules during Phase 1 (baseline establishment):**  
During baseline, you use WE rules to identify and *remove* out-of-control points before calculating final limits. Removing signals and recalculating is correct here. After limits are established (Phase 2, ongoing monitoring), you do not remove signals — you investigate them.

**Treating every signal as a defect:**  
A WE rule signal means "the process behaved unexpectedly — investigate." It does not mean product is out of spec. A signal on the X-bar chart while the R chart is stable suggests a mean shift, not necessarily wider spread. Always look at both charts together.
