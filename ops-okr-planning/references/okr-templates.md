# OKR Templates

Ready-to-copy templates for every stage of the OKR cadence: planning, weekly check-in, mid-quarter review, end-of-quarter scoring, and retrospective. Each section includes a blank template followed by a filled example.

---

## 1. Quarter Planning Template

Use at the start of each quarter. Fill company OKRs first, then cascade to teams.

### Blank

```markdown
# OKR Plan: {Team / Company} — {Q# YYYY}

**Owner:** {name or role}
**Created:** {date}
**Review date:** {mid-quarter date}

---

## Objective 1: {Inspiring, qualitative goal}

| # | Key Result | Baseline | Target | Owner | Leading/Lagging |
|---|------------|----------|--------|-------|-----------------|
| KR1 | | | | | |
| KR2 | | | | | |
| KR3 | | | | | |

**Why this Objective:** {1–2 sentences on strategic rationale}
**Supports:** {Company O# or "company-level"}

---

## Objective 2: {Inspiring, qualitative goal}

| # | Key Result | Baseline | Target | Owner | Leading/Lagging |
|---|------------|----------|--------|-------|-----------------|
| KR1 | | | | | |
| KR2 | | | | | |
| KR3 | | | | | |

**Why this Objective:** {1–2 sentences}
**Supports:** {Company O# or "company-level"}
```

### Filled Example — Product Team, Q2 2025

```markdown
# OKR Plan: Product Team — Q2 2025

**Owner:** Amy Chen (Head of Product)
**Created:** 2025-04-01
**Review date:** 2025-05-14

---

## Objective 1: Make onboarding effortless for new SMB users

| # | Key Result | Baseline | Target | Owner | Leading/Lagging |
|---|------------|----------|--------|-------|-----------------|
| KR1 | Time-to-first-value (days) | 7 days | 1 day | Engineering | Lagging |
| KR2 | Onboarding wizard completion rate | 42% | 80% | Product | Lagging |
| KR3 | Week-1 feature adoption (≥3 features used) | 18% | 45% | Product + Growth | Leading |

**Why this Objective:** Churn analysis shows 60% of cancelled accounts never completed setup. Fixing this is the highest-leverage retention lever.
**Supports:** Company O1 — Become the #1 choice for SMB accounting in Taiwan

---

## Objective 2: Make the core accounting workflow delightful

| # | Key Result | Baseline | Target | Owner | Leading/Lagging |
|---|------------|----------|--------|-------|-----------------|
| KR1 | Task completion time (invoice creation) | 4.2 min | 1.5 min | UX + Eng | Lagging |
| KR2 | In-app NPS (accounting module) | 28 | 50 | Product | Lagging |
| KR3 | Support tickets related to accounting flow | 340/month | 120/month | CS + Product | Leading |

**Why this Objective:** NPS surveys cite "slow and confusing" as top complaint. Fixing UX directly supports the company's differentiation on simplicity.
**Supports:** Company O1
```

---

## 2. Weekly Check-in Template

15-minute team standup. Fill asynchronously before the meeting; discuss only 🔴 rows.

### Blank

```markdown
## OKR Check-in — Week {N} ({date})

| KR | Target | Current | Δ This Week | Confidence | Blocker / Note |
|----|--------|---------|-------------|-----------|----------------|
| O1 KR1 | | | | 🟢/🟡/🔴 | |
| O1 KR2 | | | | 🟢/🟡/🔴 | |
| O1 KR3 | | | | 🟢/🟡/🔴 | |
| O2 KR1 | | | | 🟢/🟡/🔴 | |
| O2 KR2 | | | | 🟢/🟡/🔴 | |
| O2 KR3 | | | | 🟢/🟡/🔴 | |

**Top 3 priorities this week:**
1.
2.
3.

**Blockers requiring leadership decision:**
-
```

### Confidence Signal Guide

| Color | Meaning | Action |
|-------|---------|--------|
| 🟢 | On track to hit target | No action needed |
| 🟡 | At risk — plan exists but uncertain | Surface in meeting, owner explains plan |
| 🔴 | Off track — will miss target without intervention | Escalate, discuss options |

### Filled Example — Week 6

```markdown
## OKR Check-in — Week 6 (2025-05-12)

| KR | Target | Current | Δ This Week | Confidence | Blocker / Note |
|----|--------|---------|-------------|-----------|----------------|
| O1 KR1: Time-to-first-value | 1 day | 3.1 days | -0.8 days | 🟡 | Wizard shipped; email verification still manual |
| O1 KR2: Wizard completion rate | 80% | 61% | +6% | 🟡 | Step 4 drop-off high; UX fix in review |
| O1 KR3: Week-1 feature adoption | 45% | 39% | +4% | 🟢 | Trending well |
| O2 KR1: Invoice creation time | 1.5 min | 2.2 min | -0.3 min | 🟡 | New UI in staging; needs QA |
| O2 KR2: In-app NPS | 50 | 35 | +4 | 🟢 | Responsive to UX changes |
| O2 KR3: Support tickets | 120/month | 198/month | -31 | 🟡 | Declining but pace may be too slow |

**Top 3 priorities this week:**
1. Fix Step 4 drop-off (A/B test: simplify field count)
2. Complete QA on new invoice UI and ship to 20% of users
3. Remove manual email verification from onboarding path

**Blockers requiring leadership decision:**
- Email verification change requires security sign-off — need a decision by EOW
```

---

## 3. Mid-Quarter Review Template

Deeper analysis at the midpoint. Goal: adjust, not grade.

```markdown
# Mid-Quarter OKR Review — {Team} — {Q# YYYY}

**Date:** {date}
**Facilitator:** {name}

---

### Progress Summary

| Objective | KRs on track | KRs at risk | KRs off track | Overall confidence |
|-----------|-------------|------------|--------------|-------------------|
| O1: {title} | | | | 🟢/🟡/🔴 |
| O2: {title} | | | | 🟢/🟡/🔴 |

---

### KR-Level Deep Dive

For each 🟡 or 🔴 KR, answer:

**KR:** {name}
**Current:** {value} vs Target: {value}
**Root cause of gap:** {1–2 sentences}
**Decision:** [ ] Keep target  [ ] Adjust target  [ ] Deprioritize  [ ] Add resource
**Revised target (if changed):** {value} — **Reason:** {must be documented}
**Owner's commitment for next 6 weeks:** {specific action}

---

### OKRs to Add / Drop

| Change | Objective | KR | Reason |
|--------|-----------|-----|--------|
| Add | | | {new information / strategic shift} |
| Drop | | | {no longer relevant / can't resource} |

---

### Retrospective Note (save for EOQ)
{Park early observations here so EOQ retro isn't starting from zero}
```

---

## 4. End-of-Quarter Scoring Template

### Scoring Formula

Each KR is scored on a 0.0–1.0 scale:

```
Score = (Actual - Baseline) / (Target - Baseline)

Clamp to [0.0, 1.0] — don't score above 1.0 even if you exceeded target.
```

Objective score = average of its KR scores (equal weight by default; see weighting note below).

**Example:**

```
KR1: Time-to-first-value
  Baseline = 7 days, Target = 1 day, Actual = 2 days
  Score = (7 - 2) / (7 - 1) = 5/6 = 0.83

KR2: Wizard completion rate
  Baseline = 42%, Target = 80%, Actual = 68%
  Score = (68 - 42) / (80 - 42) = 26/38 = 0.68

KR3: Week-1 feature adoption
  Baseline = 18%, Target = 45%, Actual = 47%
  Score = (47 - 18) / (45 - 18) = 29/27 → clamp to 1.0

Objective 1 Score = (0.83 + 0.68 + 1.0) / 3 = 0.84  ✅ Sweet spot
```

### KR Weighting (Optional)

If KRs differ in strategic importance, assign weights that sum to 1.0:

```
Weighted score = Σ (KR_score × KR_weight)

Example:
  KR1 weight = 0.5 (most important)
  KR2 weight = 0.3
  KR3 weight = 0.2

  Weighted O1 score = (0.83 × 0.5) + (0.68 × 0.3) + (1.0 × 0.2)
                    = 0.415 + 0.204 + 0.200 = 0.82
```

Default: equal weighting. Only apply custom weights if the team explicitly agreed on them at the start of the quarter — don't assign weights retroactively to make a score look better.

### Blank Scoring Sheet

```markdown
# OKR Scoring — {Team} — {Q# YYYY}

**Scored by:** {name}
**Date:** {date}

---

### Objective 1: {title}

| KR | Baseline | Target | Actual | Score | Notes |
|----|----------|--------|--------|-------|-------|
| KR1 | | | | | |
| KR2 | | | | | |
| KR3 | | | | | |

**O1 Score:** {average} — {🔴 < 0.4 / 🟡 0.4–0.6 / 🟢 0.7–0.8 / ⭐ 0.9–1.0}

**Reflection:** {2–3 sentences: what drove the score? What would you do differently?}

---

### Objective 2: {title}

| KR | Baseline | Target | Actual | Score | Notes |
|----|----------|--------|--------|-------|-------|
| KR1 | | | | | |
| KR2 | | | | | |
| KR3 | | | | | |

**O2 Score:** {average}

**Reflection:** {2–3 sentences}

---

### Overall Team Score: {average of all O scores}

| Score range | Interpretation |
|-------------|---------------|
| 0.0 – 0.3 | Goals were right; execution broke down — investigate root cause |
| 0.4 – 0.6 | Partial progress; likely realistic goals, hit obstacles |
| 0.7 – 0.8 | Sweet spot: ambitious goals, strong execution |
| 0.9 – 1.0 | Either exceptional execution OR goals weren't ambitious enough |
```

---

## 5. Retrospective Template

Run immediately after scoring, before next-quarter OKR setting.

```markdown
# OKR Retrospective — {Team} — {Q# YYYY}

**Date:** {date}
**Duration:** 45 minutes
**Participants:** {list}

---

### 1. Score Review (5 min)

Quickly read through scores. No debate yet — just ensure everyone has the same numbers.

---

### 2. What drove our best score? (10 min)

**Objective with highest score:** {O#} — Score: {X.X}

- What specifically worked?
- Was the goal well-set, or did we get lucky?
- What should we repeat or scale?

---

### 3. What drove our lowest score? (10 min)

**Objective with lowest score:** {O#} — Score: {X.X}

Root cause (pick one or more):
- [ ] Goal was too ambitious given resources
- [ ] Unexpected external blocker
- [ ] Internal execution failure (specify: {team / process / decision})
- [ ] Goal became irrelevant mid-quarter (should have been dropped)
- [ ] Baseline was wrong / measurement broke

**Decision for next quarter:**
- [ ] Carry forward with same goal
- [ ] Carry forward with adjusted target
- [ ] Drop entirely

---

### 4. OKR Process Health (10 min)

Rate 1–5:

| Question | Score (1–5) | Comment |
|----------|------------|---------|
| Did weekly check-ins surface blockers early enough? | | |
| Were OKRs visible and referenced in day-to-day decisions? | | |
| Did team feel ownership of KRs (vs. assigned by manager)? | | |
| Were baselines accurate at the start of quarter? | | |
| Did we avoid tying OKRs to performance reviews? | | |

---

### 5. Carry-forwards for Next Quarter (10 min)

| Item | Type | Owner | Action |
|------|------|-------|--------|
| {KR to continue} | Carry-forward goal | | Confirm new baseline = last actual |
| {process fix} | Retro action | | |
| {data/baseline to establish} | Instrumentation | | Complete before OKR-setting |

---

### 6. Input for Next Quarter's OKR Setting

**Strategic shifts we're aware of:**

**Things we deliberately will NOT pursue next quarter:**

**New bets we want to propose:**
```

---

## 6. Baseline Establishment Checklist

A common failure: OKRs are set before baselines are measured, so scores are guesses.

Before finalizing any KR, confirm:

```
□ Baseline is measured from real data, not estimated
□ Measurement method is documented (who pulls it, from which system, how often)
□ Baseline period is specified (e.g., "Q1 2025 average" not "recently")
□ Same measurement method will be used for scoring at end of quarter
□ If baseline doesn't exist yet: instrumentation is shipped before Week 2
```

**If you can't check all five boxes, the KR is not ready to commit to.** Either delay (add a KR to establish the measurement in the first two weeks) or replace with a KR you can actually measure.

---

## 7. Common Rewrite Patterns

Tasks and activities masquerade as Key Results. Use these rewrites:

| ❌ Task / Output | ✅ Outcome / KR |
|-----------------|----------------|
| Launch new onboarding wizard | Onboarding completion rate: 42% → 80% |
| Run 3 A/B tests on checkout | Checkout conversion rate: 2.1% → 3.5% |
| Hire 2 engineers | Engineering velocity (story points/sprint): 34 → 50 |
| Write 10 blog posts | Organic search sessions: 12K → 25K/month |
| Hold monthly all-hands | Employee eNPS: 18 → 40 |
| Refactor auth service | Auth service p99 latency: 420ms → 80ms |
| Conduct customer interviews | CSAT on support workflow: 3.2 → 4.5 (5-point scale) |

Pattern: replace "do X" with "move metric Y from A to B as a result of doing X."
