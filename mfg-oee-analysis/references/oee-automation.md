# OEE Automated Data Collection

Manual OEE tracking — operators filling paper sheets at shift end — routinely underreports downtime by 30-50% and misclassifies losses. Automated collection eliminates the attribution lag and captures events operators never record (sub-minute stops, micro-speed reductions).

---

## Signal Sources and What They Measure

| Signal Type | Hardware | OEE Factor | Captures |
|-------------|----------|-----------|---------|
| Machine run/stop (discrete I/O) | PLC digital output → edge device | Availability | Planned vs. unplanned downtime |
| Part-count pulse | Proximity sensor, encoder, vision trigger | Performance | Actual cycle time per unit |
| Reject signal | Vision system OK/NG output, checkweigher | Quality | Defective count at the source |
| Spindle load / current | Current transducer on motor | Performance | Reduced-speed detection |
| OPC-UA / MQTT from CNC | Machine native protocol | All three | Cycle time, alarms, part count |

**Minimum viable set**: run/stop signal + part count pulse + reject count. These three signals let you compute all three OEE factors.

---

## Signal-to-Factor Mapping (Exact Formulas)

Using the same variables as SKILL.md:

```
PPT  = Planned Production Time (from shift schedule)
DT   = Downtime = sum of all run=0 intervals during PPT
RT   = Run Time = PPT − DT

ICT  = Ideal Cycle Time (design spec, fixed per part number)
TC   = Total Count (part-count pulses during PPT)
GC   = Good Count = TC − reject signals during PPT

Availability = RT / PPT
Performance  = (ICT × TC) / RT
Quality      = GC / TC
OEE          = Availability × Performance × Quality
```

The automation system's only job is to produce `DT`, `TC`, and `GC` with reliable timestamps. Everything else is arithmetic.

---

## Architecture: Three Common Tiers

### Tier 1 — Edge-Only (Single Machine, Low Budget)

```
Machine I/O
    │
    ▼
Edge Device (Raspberry Pi / industrial PC)
    │  reads: run bit, count pulse, reject bit
    │  computes: OEE per shift in real time
    │
    ▼
Local display (7" touchscreen at machine)
    +
CSV export to shared drive for reporting
```

**Cost**: ~$300–800 hardware per machine  
**Latency**: seconds  
**Limitation**: no cross-machine visibility, manual aggregation for plant-level reporting

### Tier 2 — Edge + MQTT Broker

```
Machine I/O ──► Edge Device ──► MQTT Broker (Mosquitto)
                                     │
                        ┌────────────┴────────────┐
                        ▼                         ▼
                 Time-Series DB             Dashboard
                 (InfluxDB / TimescaleDB)   (Grafana)
```

MQTT topic schema (enforce this from day 1 — retrofitting is painful):

```
plant/{site}/line/{line_id}/machine/{machine_id}/oee/run      → 0 or 1
plant/{site}/line/{line_id}/machine/{machine_id}/oee/count    → cumulative int
plant/{site}/line/{line_id}/machine/{machine_id}/oee/reject   → cumulative int
plant/{site}/line/{line_id}/machine/{machine_id}/oee/downtime_code → int
```

**Cost**: adds ~$500–2,000 for broker/DB server (often shared)  
**Latency**: seconds to minutes  
**Gain**: multi-machine comparison, historical trending, alerts

### Tier 3 — MES Integration

Edge devices feed a Manufacturing Execution System (SAP ME, Siemens Opcenter, Tulip, Ignition). MES provides:

- Part number–specific ICT lookup (no hardcoding)
- Shift schedule (PPT comes from the production order, not a config file)
- Downtime reason code library with operator touch confirmation
- Integration with ERP for planned vs. actual output reconciliation

**Cost**: $50K–$500K+ project (primarily integration labor)  
**Use when**: you need OEE linked to specific production orders, lot traceability, or multi-plant benchmarking

---

## Downtime Classification Without Operator Input

Raw run/stop signals tell you *when* the machine was down but not *why*. Two approaches:

### Approach A: Duration-Based Auto-Classification

```python
CLASSIFICATION_RULES = [
    # (min_seconds, max_seconds, category)
    (0,      30,    "micro_stop"),       # Performance loss, not Availability
    (30,     300,   "minor_stop"),       # Availability — idling
    (300,    1800,  "unplanned_repair"), # Availability — breakdown
    (1800,   None,  "major_breakdown"),  # Availability — escalate
]

def classify_downtime(duration_seconds):
    for min_s, max_s, category in CLASSIFICATION_RULES:
        if duration_seconds >= min_s and (max_s is None or duration_seconds < max_s):
            return category
```

**Critical OEE implication**: micro-stops (< 30 s) should NOT be classified as Availability losses — they are Performance losses (Six Big Loss #3: Idling & Minor Stops). Misclassifying them inflates Availability and hides Performance problems.

### Approach B: Reason Code Touch Panel

Operator taps a touchscreen when downtime starts: `Breakdown / Changeover / Material / Planned`. System records the code with timestamp. Duration-based rules apply only if operator forgets to enter a code within N minutes.

**Recommended**: Approach B for machines with operators; Approach A for fully automated cells.

---

## Detecting Performance Loss Automatically

Performance loss (running below ideal cycle time) is the hardest factor to automate because the machine shows as "running" — no alarm, no stop signal.

### Method: Cycle Time Deviation Detection

```python
def detect_performance_loss(actual_cycle_times: list[float], ICT: float,
                             threshold: float = 1.10) -> list[dict]:
    """
    Flag any cycle longer than threshold × ICT as a performance loss event.
    threshold=1.10 means >10% slower than ideal.
    """
    losses = []
    for i, ct in enumerate(actual_cycle_times):
        if ct > ICT * threshold:
            losses.append({
                "unit_index": i,
                "actual_ct": ct,
                "ideal_ct": ICT,
                "excess_seconds": ct - ICT,
                "loss_type": "reduced_speed" if ct < ICT * 3 else "minor_stop"
            })
    return losses
```

**Worked example**:

```
ICT = 60 s/unit
Cycle times observed (seconds): [61, 62, 58, 145, 63, 60, 210, 61]
Threshold: 1.10 × 60 = 66 s

Flagged:
  Unit 4: 145 s → minor_stop (145 < 180 = 3 × ICT)
  Unit 7: 210 s → minor_stop (210 > 180, still minor_stop by this threshold)

Performance = (60 × 8) / (61+62+58+145+63+60+210+61)
            = 480 / 720
            = 66.7%
```

If you only had a run/stop signal and the machine never fully stopped, you would measure Performance = 100% and miss the 33% loss.

---

## Shift Schedule Integration

PPT must come from a shift calendar, not a hardcoded constant. Hardcoding 480 min/shift will corrupt OEE on shortened shifts, holidays, and overtime.

### Minimal Shift Calendar Schema (SQLite / Postgres)

```sql
CREATE TABLE shift_schedule (
    shift_id       TEXT PRIMARY KEY,  -- e.g. '2025-03-15-A'
    line_id        TEXT NOT NULL,
    shift_date     DATE NOT NULL,
    shift_code     TEXT NOT NULL,     -- 'A', 'B', 'C'
    planned_start  TIMESTAMP NOT NULL,
    planned_end    TIMESTAMP NOT NULL,
    planned_breaks INTEGER NOT NULL   -- total break minutes (excluded from PPT)
);

-- PPT for a shift:
-- EXTRACT(EPOCH FROM (planned_end - planned_start))/60 - planned_breaks
```

The edge device queries this table at shift start. If the query fails, it falls back to the previous shift's PPT and logs a data-quality flag — it does NOT silently use a hardcoded value.

---

## Data Quality Flags

Every OEE record should carry a `data_quality` field. Downstream reports must filter or disclose these.

| Flag | Condition | Effect on OEE |
|------|-----------|--------------|
| `SIGNAL_GAP` | Run/stop signal offline > 5 min | Availability may be overstated |
| `COUNT_FROZEN` | Part count unchanged for > 2 × ICT while run=1 | Performance understated |
| `SHIFT_OVERRIDE` | PPT from fallback constant, not schedule | PPT denominator uncertain |
| `REJECT_SENSOR_OFFLINE` | Reject signal not received for full shift | Quality = 100% (untrustworthy) |
| `PARTIAL_SHIFT` | Shift ended early / started late | OEE valid but PPT differs from standard |

```python
def compute_oee_with_quality(rt, ppt, ict, tc, gc, flags: set) -> dict:
    availability = rt / ppt if ppt > 0 else None
    performance  = (ict * tc) / rt if rt > 0 else None
    quality      = gc / tc if tc > 0 else None

    if availability and performance and quality:
        oee = availability * performance * quality
    else:
        oee = None

    return {
        "availability": availability,
        "performance":  performance,
        "quality":      quality,
        "oee":          oee,
        "data_quality": sorted(flags) or ["OK"]
    }
```

---

## Sampling Rate Recommendations

| Signal | Minimum Rate | Recommended | Reason |
|--------|-------------|-------------|--------|
| Run/stop | 1 Hz | 10 Hz | Catch micro-stops < 1 s |
| Part count | Event-driven (pulse) | Event-driven | Counting errors if polled |
| Reject | Event-driven | Event-driven | Same |
| Cycle time | Derived from count timestamps | — | No separate polling needed |
| Current/load | 1 Hz | 10 Hz | Speed ramp detection |

Storage implication: 10 Hz × 3 signals × 10 machines × 8-hour shift = ~8.6 million rows/shift. Use a time-series DB (InfluxDB, TimescaleDB) — row-oriented SQL will not sustain this write rate without significant tuning.

Aggregate to 1-minute buckets for OEE dashboards; keep raw events for root-cause drill-down.

---

## Common Implementation Failures

**Counting parts at the wrong point**: Count at the end of the machine (output), not at the feed (input). Counting input inflates Total Count and hides in-process scrap — Quality will appear higher than actual.

**Using calendar time instead of planned production time**: If a machine sits idle because there are no orders, that is not an OEE loss. Dividing by calendar time produces a metric called TEEP (Total Effective Equipment Performance), not OEE. TEEP is valid for capacity planning but conflating it with OEE leads to wrong improvement priorities.

**Treating all downtime as unplanned**: Changeovers are planned; breakdowns are not. Grouping them gives you one number that combines two completely different problems with different solutions. Enforce the reason code split from day one.

**Resetting cumulative counters without logging**: If a PLC counter rolls over at 65,535 or is reset by an operator, the edge device will see a count decrease and compute negative production. Log every counter reset as an event; detect decreases and treat them as resets, not negative production.

**Applying one ICT to all part numbers**: A machine running product A at 60 s/unit and product B at 90 s/unit should use separate ICT values per active production order. A single global ICT will make Performance appear artificially high or low depending on the product mix that shift.

---

## Validation Checklist Before Going Live

- [ ] Run/stop signal verified against physical machine state (PLC force test)
- [ ] Part count matches hand-counted physical units for a 30-minute test run
- [ ] Reject count matches visual inspection rejects for same test run
- [ ] Shift schedule query tested for holiday, shortened shift, and overtime scenarios
- [ ] Counter rollover handling tested (force counter to max, verify no data corruption)
- [ ] Data quality flags appear in output when signals are disconnected
- [ ] Computed OEE for test run matches hand-calculated OEE from raw numbers
- [ ] Time zone handling confirmed (machine local time vs. UTC storage)
