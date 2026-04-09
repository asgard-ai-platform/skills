# Learning Period

The **learning period** is the window after a bidding strategy change during which the automated algorithm recalibrates its prediction model. Performance is intentionally unstable during this phase — the system is exploring signal space, not malfunctioning.

---

## What Triggers a Learning Period

Any of the following resets the learning counter:

| Trigger | Typical Learning Period |
|---------|------------------------|
| Switch from Manual CPC → Target CPA | 14–21 days |
| Switch from Target CPA → Target ROAS | 14–21 days |
| Change target CPA by > 20% in one move | 7–14 days |
| Change target ROAS by > 15% in one move | 7–14 days |
| Add or remove conversion action | 14–21 days |
| Significant budget change (> 50%) | 3–7 days |
| Audience list change | 3–7 days |
| Pause campaign > 5 days then resume | 7–14 days |

**IRON LAW reinforcement**: A campaign with < 30 conversions/month cannot exit the learning period meaningfully — the confidence interval on the model is too wide. Do not attempt automated bidding below this threshold regardless of calendar time elapsed.

---

## Phase Breakdown

### Days 1–3: Exploration Phase
The algorithm aggressively tests different bid levels to map the conversion probability curve. Expect:
- CPA 30–60% above target (intentional spend)
- Impression share swings
- Conversion rate variance ± 40%

Do not intervene. This is the system buying information.

### Days 4–10: Calibration Phase
The algorithm narrows its bid distribution using the data from Days 1–3. Expect:
- CPA trending toward target but still ± 25%
- Volume stabilizing
- Quality Score / Ad Rank settling

Still do not intervene unless you see **zero conversions** for more than 5 consecutive days (genuine malfunction signal).

### Days 11–21: Convergence Phase
Normal operational range. CPA should reach within 20% of target. If not, a strategic adjustment is warranted.

---

## Decision Rule: When to Intervene vs. Wait

Use this decision tree during an active learning period:

```
Is it within Days 1-10?
  └─ YES → Are there ANY conversions in the past 7 days?
      ├─ YES → WAIT (exploration is normal)
      └─ NO  → CHECK conversion tracking, then WAIT 3 more days
                 └─ Still zero? → PAUSE and audit tracking

Is it Day 11+?
  └─ Is actual CPA within 20% of target?
      ├─ YES → Learning period complete. Normal optimization resumes.
      └─ NO  → Is the gap closing week-over-week?
                 ├─ YES → WAIT another week
                 └─ NO  → Strategy adjustment warranted (see Adjustment Protocol)
```

---

## The 20% Convergence Test

After the learning period (Day 21), compute:

```
convergence_error = |actual_CPA - target_CPA| / target_CPA
```

**Acceptance threshold**: `convergence_error ≤ 0.20`

**Worked Example:**

```
Target CPA: NT$500
Day 21 actual CPA (7-day average): NT$580

convergence_error = |580 - 500| / 500 = 0.16

Result: 0.16 ≤ 0.20 → PASS. Learning period complete.
```

```
Target CPA: NT$500
Day 21 actual CPA (7-day average): NT$720

convergence_error = |720 - 500| / 500 = 0.44

Result: 0.44 > 0.20 → FAIL. Adjustment protocol required.
```

When calculating actual CPA for this test, always use a **7-day rolling average**, not a single-day snapshot. Single-day CPA is noisy even after convergence.

---

## Adjustment Protocol (Post-Learning Failure)

If the 20% test fails at Day 21+, follow this sequence:

### Step 1: Diagnose the direction of failure

| Actual CPA vs Target | Likely Cause | Action |
|---------------------|--------------|--------|
| Actual >> Target (overspending per conversion) | Target set too aggressive | Relax target by 15–20% |
| Actual << Target AND volume collapsed | Budget too restrictive relative to target | Increase budget OR relax target |
| Actual << Target AND volume normal | Target set too conservatively | Tighten target by 10% |
| Actual CPA erratic (no trend) | Conversion tracking issues | Audit tracking before any bid change |

### Step 2: Apply incremental adjustment (never large jumps)

```
Maximum single adjustment: ±20% of current target
Minimum wait between adjustments: 7 days
```

**Bad**: Target CPA is NT$500, performance is poor → change to NT$300 immediately.
**Good**: Target CPA is NT$500, performance is poor → change to NT$600, wait 7 days, evaluate.

Each target change triggers a mini-learning period of 5–7 days.

### Step 3: Document the baseline

Before adjusting, record:
```
Date:
Target (before): 
7-day actual CPA (before):
Impression share:
Conversion volume (last 30 days):
Reason for adjustment:
Target (after):
```

This prevents compounding changes from obscuring causality.

---

## Protecting the Learning Period from Business Pressure

The most common failure mode is **premature intervention** driven by stakeholder anxiety. A campaign showing NT$800 CPA on Day 5 (target: NT$500) is not failing — it is in exploration phase.

Establish a **communication protocol before launch**:

1. Brief stakeholders on the 14–21 day timeline at campaign launch.
2. Set a "Do Not Touch" calendar hold for the first 14 days.
3. Send a mid-period status update at Day 7 with the message: "CPA is [X], expected to converge to [target] by Day 21. No action required."
4. Only share optimization results at Day 21+.

---

## Seasonality and Forced Re-Learning

Automated bidding learns from **recent conversion history**, typically a rolling 30-day window. External events that change user behavior faster than the window can break a stable model:

| Event Type | Lead Time to Act | Recommended Action |
|-----------|-----------------|-------------------|
| Major sale (Black Friday, 11/11) | 1 week before | Enable seasonality adjustment (if platform supports) OR temporarily switch to Maximize Conversions |
| Competitor exits market | Immediate | Monitor CPCs; may need to tighten target if CPCs drop |
| Product goes viral | Immediate | Monitor conversion rate spike; automated bidding will over-bid until model adapts (3–5 days) |
| Attribution window change | Before applying | Treat as a full strategy reset; re-enter learning period tracking |

**Seasonality adjustment mechanics (Google Ads example):**

```
Adjustment period: 1–7 days
Expected conversion rate change: +50% (e.g., during a flash sale)
Platform applies a temporary multiplier to its bid predictions
Expires automatically at end of adjustment window
```

Do not use seasonality adjustments for permanent trend changes — only for known, bounded events.

---

## Conversion Delay and Its Effect on Learning

If your conversion has a long attribution window (e.g., B2B lead that closes in 14 days), the algorithm is learning on **incomplete data during the learning period**.

**Effective learning period formula:**

```
effective_learning_days = stated_learning_period + attribution_window_days
```

For a 21-day learning period with 14-day attribution window:

```
effective_learning_days = 21 + 14 = 35 days
```

Practical implication: do not evaluate convergence until Day 35, not Day 21. The algorithm appears to be failing during Days 21–35 because conversions from those days have not yet fully attributed.

**Mitigation options:**
- Use a shorter-window micro-conversion as a training signal (add-to-cart, form start) while tracking the real conversion for reporting
- Enable modeled conversions if the platform supports it
- Accept the extended evaluation window as a business constraint

---

## Quick Reference: Learning Period Checklists

### Before Launching Automated Bidding
- [ ] Conversion tracking firing correctly on at least 30 events in the past 30 days
- [ ] Conversion action tagged with correct value (for ROAS) or binary (for CPA)
- [ ] Attribution window matches sales cycle
- [ ] Budget is at least 5–10× daily target CPA (so the algorithm has room to explore)
- [ ] No major promotions or seasonality events in the next 21 days (or plan for seasonality adjustments)
- [ ] Stakeholders briefed on 14–21 day no-touch window

### During Learning Period (Days 1–21)
- [ ] Daily check: are conversions occurring? (If zero for 5+ days → investigate)
- [ ] Do NOT change target CPA/ROAS
- [ ] Do NOT change budget by more than 20%
- [ ] Do NOT add/remove conversion actions
- [ ] Do NOT restructure ad groups or keywords significantly

### Evaluating Convergence (Day 21)
- [ ] Calculate 7-day average actual CPA
- [ ] Apply convergence test: `|actual - target| / target ≤ 0.20`
- [ ] If FAIL → diagnose direction (over/under target, volume behavior)
- [ ] If PASS → enter normal optimization cadence (biweekly target reviews)
