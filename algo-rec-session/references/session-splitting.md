# Session Splitting

Session splitting converts a raw clickstream log into discrete sessions that the recommendation model treats as independent sequences. The quality of every downstream prediction depends directly on how well splits capture genuine user intent boundaries.

---

## What a Session Boundary Represents

A session boundary should mark a point where the user's **intent resets** — they are no longer continuing the same shopping or browsing task. A poor boundary definition creates two failure modes:

| Failure | Cause | Effect on predictions |
|---------|-------|-----------------------|
| Under-splitting | Boundary threshold too long | Two separate intents merged; transition matrix learns spurious item pairs |
| Over-splitting | Boundary threshold too short | Sessions too short to form sequence patterns; degrades to popularity fallback too often |

---

## Method 1: Timeout-Based Splitting (Primary Method)

### Rule

Split session at any inactivity gap ≥ **τ** minutes.

```
session_id(event) = session_id(prev_event)  if  Δt < τ
session_id(event) = new_session()            if  Δt ≥ τ
```

Where `Δt = timestamp(event_i) - timestamp(event_{i-1})`.

### Choosing τ

There is no universally correct τ. Use the **inter-event gap distribution** of your own data:

1. Compute all `Δt` values across the raw log (in minutes).
2. Plot the empirical CDF of `Δt`.
3. Find the natural **gap in density** — typically a bimodal distribution with short within-session gaps (seconds to a few minutes) and long between-session gaps (hours).
4. Set τ at the **valley** between the two modes.

**Worked example:**

| Percentile of Δt | Typical e-commerce value |
|-----------------|--------------------------|
| 50th | 1.2 min |
| 75th | 4.8 min |
| 90th | 18 min |
| **95th** | **32 min** ← common τ choice |
| 99th | 4.2 hours |

The 30-minute default cited in the SKILL.md corresponds roughly to the ~95th percentile of within-session gaps in general e-commerce. If your gap distribution shows a clear valley at 15 min, use 15 min.

### Domain Adjustments

| Domain | Suggested τ | Rationale |
|--------|-------------|-----------|
| Fashion / impulse e-commerce | 15–20 min | Users make fast decisions; long gaps = intent reset |
| Electronics / research buying | 45–60 min | Comparison browsing; users pause to think |
| Content streaming | 5–10 min | Between-episode gaps shouldn't merge sessions |
| News reading | 20–30 min | Short bursts followed by long pauses |
| B2B procurement | 60–120 min | Users may leave to consult colleagues |

---

## Method 2: Hard Day Boundary

Always split at midnight, regardless of τ. Apply **in addition to** timeout splitting.

```python
def split_sessions(events, tau_minutes=30):
    sessions = []
    current = []
    for i, event in enumerate(events):
        if i == 0:
            current.append(event)
            continue
        prev = events[i - 1]
        delta_minutes = (event.timestamp - prev.timestamp).total_seconds() / 60
        day_changed = event.timestamp.date() != prev.timestamp.date()
        if delta_minutes >= tau_minutes or day_changed:
            if len(current) >= MIN_SESSION_LENGTH:
                sessions.append(current)
            current = [event]
        else:
            current.append(event)
    if len(current) >= MIN_SESSION_LENGTH:
        sessions.append(current)
    return sessions
```

`MIN_SESSION_LENGTH = 3` is the threshold from the SKILL.md Phase 1 gate.

---

## Method 3: Explicit Session ID (When Available)

If your event log already contains a `session_id` from the frontend (e.g., set at page load, cleared at browser close), prefer it over inactivity-based splitting. Server-assigned session IDs are more accurate because:

- They capture browser-close boundaries that inactivity timeouts miss.
- They handle users who browse slowly but don't pause (long Δt within one intent).

**Validation check**: even with explicit session IDs, apply a τ = 120 min hard cap. Sessions longer than 2 hours are almost always stale (browser left open, device locked) and should be split.

```python
def split_with_session_id(events, hard_cap_minutes=120):
    # Group by session_id first
    by_session = defaultdict(list)
    for e in events:
        by_session[e.session_id].append(e)
    
    sessions = []
    for sid, evts in by_session.items():
        evts.sort(key=lambda e: e.timestamp)
        # Apply hard cap within the session_id group
        sub = [evts[0]]
        for i in range(1, len(evts)):
            delta = (evts[i].timestamp - evts[i-1].timestamp).total_seconds() / 60
            if delta >= hard_cap_minutes:
                if len(sub) >= MIN_SESSION_LENGTH:
                    sessions.append(sub)
                sub = [evts[i]]
            else:
                sub.append(evts[i])
        if len(sub) >= MIN_SESSION_LENGTH:
            sessions.append(sub)
    return sessions
```

---

## Minimum Length Filtering

After splitting, discard sessions shorter than 3 events. This is the SKILL.md Phase 1 gate. The rationale:

- **Length 1**: Single click. Cannot form any transition pair. No sequence signal.
- **Length 2**: One transition (A→B). Provides one data point but no context window for higher-order Markov. Extremely noisy for training.
- **Length 3+**: Minimum for a meaningful sequence. Supports order-2 Markov (last 2 clicks as context).

**Effect on dataset size**: In typical e-commerce logs, 40–60% of raw sessions are length 1 or 2. Filtering is aggressive but necessary. Do not soften this threshold to increase training set size — short sessions add noise, not signal.

---

## Handling Multi-Device Users

A logged-in user may start a session on mobile and continue on desktop. Inactivity-based splitting will create two separate sessions. This is **correct behavior** for session-based recommendation: each session is treated as independent. Do not merge cross-device sessions unless:

1. You have explicit cross-device identity resolution.
2. The time gap between devices is under τ.

Merging is the responsibility of identity resolution upstream, not session splitting.

---

## Timestamp Precision Requirements

Session splitting requires timestamps with at least **second** precision. Minute-level timestamps cause collisions:

- Events within the same minute get `Δt = 0`, making them indistinguishable from near-simultaneous clicks.
- Click order within the minute is lost; sequence models are sensitive to order.

If your log only has minute-level timestamps, use the raw event sequence order as a proxy within each minute — but flag this as a data quality issue.

---

## Decision Framework

```
START
  │
  ▼
Do events have frontend session_id?
  ├─ YES → Use session_id as primary split
  │         Apply hard cap τ=120min within each session_id
  │
  └─ NO  → Use inactivity timeout τ
              │
              ▼
            Plot Δt distribution from your data
              │
              ├─ Clear bimodal valley found? → set τ = valley point
              │
              └─ No clear valley? → use domain default from table above
  │
  ▼
Apply day-boundary hard split (always)
  │
  ▼
Filter: discard sessions with length < 3
  │
  ▼
Output: list of ordered item sequences, one per session
```

---

## Diagnostic Metrics After Splitting

Run these checks on the split dataset before training:

| Metric | Healthy range | Warning sign |
|--------|--------------|--------------|
| Median session length | 4–8 items | < 3: τ too short or data too sparse |
| % sessions filtered (length < 3) | 40–65% | > 80%: τ too short |
| Max session length | < 200 items | Outliers: stale sessions not capped |
| Sessions per user per day (logged-in) | 1–5 | > 10: τ probably too long |

```python
import statistics

lengths = [len(s) for s in sessions]
print(f"Median length: {statistics.median(lengths)}")
print(f"P95 length: {sorted(lengths)[int(len(lengths)*0.95)]}")
print(f"Max length: {max(lengths)}")
print(f"Total sessions: {len(sessions)}")
```

Run this before committing to a τ value. If median session length is below 4, increase τ. If max length is in the thousands, apply a hard cap.

---

## Connection to the IRON LAW

The SKILL.md Iron Law states: *"the first 2-3 clicks establish the session's intent."* Session splitting directly governs whether those first clicks belong to the right session.

If τ is too long, a session may begin with leftover clicks from a previous, unrelated intent. The model sees `[swimsuit, sandals, laptop_bag, keyboard]` as one session and learns a spurious swimsuit→keyboard transition. The Iron Law is violated not by the model but by the splitting step upstream.

Correct splitting is a prerequisite for the Iron Law to hold: the first click in every session must genuinely represent the start of a fresh intent.
