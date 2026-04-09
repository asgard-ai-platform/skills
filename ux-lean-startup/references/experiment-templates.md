# Experiment Templates

Concrete fill-in-the-blank templates for each Build-Measure-Learn cycle. Each template forces you to state the assumption, the test, and the pass/fail criterion **before** you build anything.

---

## The One-Page Experiment Card

Fill this out before every experiment. If you can't fill in every field, the experiment isn't ready to run.

```
EXPERIMENT CARD
───────────────────────────────────────────────────────
Product:          ___________________________________
Experiment #:     ___  Date:  ___________

ASSUMPTION
We believe that: ___________________________________
For:             [target customer segment]
Who has:         [specific problem or job-to-be-done]

RISKIEST IF WRONG?  [ ] Yes, kills the business
                    [ ] Yes, kills this feature
                    [ ] No, correctible later

MVP / TEST METHOD
We will build/run: _________________________________
Time budget:       ___  Cost budget: ___

MEASURE
Primary metric:   ___________________________________
How collected:    ___________________________________
Sample size:      ___ (minimum before deciding)
Time window:      ___ days/weeks

CRITERIA (set these BEFORE running)
PASS if:  primary metric ≥ ___  (validates assumption)
FAIL if:  primary metric <  ___  (invalidates assumption)
GRAY if:  result is between — do one more cycle

DECISION RULE
Pass → [next assumption to test / double down action]
Fail → [pivot type to consider / kill criteria]
Gray → [what additional data to collect]
───────────────────────────────────────────────────────
ACTUAL RESULT (fill after running)
Primary metric:   ___  (n = ___)
Verdict:          [ ] Pass  [ ] Fail  [ ] Gray
What we learned:  ___________________________________
Next action:      ___________________________________
```

---

## Template 1: Landing Page Experiment

**Tests**: Demand — "Do enough people want this to justify building it?"

**Riskiest assumption**: Customer problem exists AND they'll act on it.

```
EXPERIMENT: Landing Page Demand Test

SETUP
Landing page promise: [one sentence value proposition]
Target segment:       [who you're sending traffic to]
Traffic source:       [ ] Ads  [ ] Cold outreach  [ ] Existing list

METRICS TO CAPTURE
┌──────────────────────────────────┬────────────┬────────────┐
│ Metric                           │ Target     │ Actual     │
├──────────────────────────────────┼────────────┼────────────┤
│ Unique visitors                  │ ≥ 200      │            │
│ Email signup rate                │ ≥ 5%       │            │
│ "Notify me" / waitlist clicks    │ ≥ 10%      │            │
│ Avg. time on page                │ ≥ 45 sec   │            │
│ Scroll depth (past fold)         │ ≥ 60%      │            │
└──────────────────────────────────┴────────────┴────────────┘

DECISION THRESHOLDS
Pass:  Signup rate ≥ 5% AND ≥ 50 actual signups
Fail:  Signup rate < 2% after 200 visitors
Gray:  2-5% — run a second variant (A/B headline or offer)

COMMON FAILURE MODES
- Traffic is wrong audience → check source, segment by referrer
- Page converts but no one uses product → problem was wrong
- High CTR, low signup → pricing or commitment level too high
```

**Worked example**:

> B2B SaaS for restaurant inventory. Landing page with demo video + "Get early access" email form. Drove 312 visitors via LinkedIn ads targeting restaurant owners. Result: 6.4% signup rate (20 signups) → **Pass**. Next experiment: do any of these 20 pay for a concierge trial?

---

## Template 2: Concierge Experiment

**Tests**: Value delivery — "Can we actually solve this problem, and will customers pay?"

**Riskiest assumption**: You can deliver the promised value, and customers experience it as valuable enough to continue.

```
EXPERIMENT: Concierge (Manual Service) Trial

SETUP
Customers recruited:  ___ (target: 5-20, not more)
How recruited:        ___________________________________
What you promised:    ___________________________________
What you'll do manually: ________________________________
Price charged:        $___/[unit]   or   FREE (justify: ___)

WEEK-BY-WEEK TRACKING
┌────────┬──────────────────────────┬────────────────────┐
│ Week   │ Value delivered          │ Customer reaction  │
├────────┼──────────────────────────┼────────────────────┤
│ 1      │                          │                    │
│ 2      │                          │                    │
│ 3      │                          │                    │
│ 4      │                          │                    │
└────────┴──────────────────────────┴────────────────────┘

END-OF-TRIAL QUESTIONS (ask every customer, verbatim)
1. "What changed for you because of this service?"
2. "What would you miss most if we shut it down tomorrow?"
3. "What would you change or add?"
4. "Would you pay $X/month for this ongoing?" (show actual price)
5. "Who else should we talk to?"

DECISION CRITERIA
Pass:  ≥ 60% of customers want to continue AND ≥ 40% willing to pay
Fail:  < 30% want to continue
Gray:  Customers want it but won't pay → revenue model pivot needed

COST-OF-MANUAL FLAG
If manual delivery cost > 3× target price, note it:
  Manual cost/unit: $___ 
  Target price: $___  
  Ratio: ___×
  → If ratio > 3×, product economics require automation proof before scaling
```

---

## Template 3: Wizard of Oz Experiment

**Tests**: Full-experience viability — "Does the complete user experience work, before we build the real backend?"

**Riskiest assumption**: The end-to-end experience produces the outcome users need, and they'll adopt it.

```
EXPERIMENT: Wizard of Oz Trial

SETUP
User-facing interface:  [what users see — app, website, dashboard]
Hidden manual process:  [what your team does behind the curtain]
User-aware of manual?   [ ] Yes (concierge hybrid)  [ ] No (full Oz)
Ethical note:           If NOT disclosed, ensure no harm from failure

AUTOMATION BOUNDARY
┌─────────────────────────────┬────────────────────────────┐
│ Step (user sees)            │ What actually happens      │
├─────────────────────────────┼────────────────────────────┤
│ User submits request        │ Hits webhook → Slack DM    │
│ "AI processing..." spinner  │ Team member does task      │
│ Results displayed           │ Team manually enters data  │
└─────────────────────────────┴────────────────────────────┘

METRICS
Primary (experience quality):
  Task success rate:      ___% (user got what they needed)
  Time-to-result:         ___ min (target: ___ min)
  
Secondary (adoption signal):
  Return usage rate:      ___% (used again within ___ days)
  Unprompted referrals:   ___ (best signal of genuine value)

Operational (feasibility proxy):
  Manual effort per task: ___ min (target ceiling: ___ min)
  Error rate:             ___% (manual mistakes)

STOP CONDITIONS
Stop the Oz experiment if:
  - Manual effort per task > ___× target → economics won't close
  - Error rate > 10% → experience too degraded to measure real demand
  - Team is burning out → you've proven it works, move to automation
```

---

## Template 4: Single-Feature Functional Prototype

**Tests**: Core value delivery in code — "Does this specific feature solve the problem well enough to retain users?"

```
EXPERIMENT: Single-Feature MVP

FEATURE SCOPED TO: ___________________________________
EXCLUDED (explicitly): ________________________________
RETENTION WINDOW: ___ days

FUNNEL METRICS
┌─────────────────────────────┬──────────┬────────────┐
│ Stage                       │ Target % │ Actual %   │
├─────────────────────────────┼──────────┼────────────┤
│ Signed up                   │ baseline │            │
│ Completed onboarding        │ ≥ 60%    │            │
│ Used core feature once      │ ≥ 40%    │            │
│ Used core feature 3× (D7)   │ ≥ 20%    │            │
│ Returned at D30             │ ≥ 10%    │            │
└─────────────────────────────┴──────────┴────────────┘

COHORT RETENTION TABLE (fill weekly)
         D1    D7    D14   D30
Cohort 1  ___   ___   ___   ___
Cohort 2  ___   ___   ___   ___

QUALITATIVE SIGNAL TRACKER
Interview 5 users who hit D7 retention AND 5 who dropped off by D3.

For retained users:
  "What made you come back?" → _________________________

For churned users:
  "What stopped you from returning?" → ___________________

NORTH STAR ALIGNMENT
North star metric: ___________________________________
  (the one number that best captures value delivered to users)
Current value: ___  Target by end of experiment: ___

PASS/FAIL
Pass:  D7 retention ≥ 20% AND north star metric trending up
Fail:  D7 retention < 10% after 2 cohorts
```

---

## Sample Size and Significance (Quick Reference)

Don't run experiments with too few users to draw conclusions. Use this table for binary metrics (conversion rate, retention — yes/no outcomes).

**Minimum sample per variant** for 80% power, 95% confidence:

| Baseline rate | Minimum detectable effect | Sample needed (each group) |
|---------------|--------------------------|---------------------------|
| 2%            | +1pp (detect 3%)         | 2,350                     |
| 2%            | +2pp (detect 4%)         | 670                       |
| 5%            | +2pp (detect 7%)         | 1,090                     |
| 5%            | +5pp (detect 10%)        | 290                       |
| 10%           | +3pp (detect 13%)        | 1,400                     |
| 10%           | +5pp (detect 15%)        | 510                       |
| 20%           | +5pp (detect 25%)        | 730                       |
| 20%           | +10pp (detect 30%)       | 200                       |

**Practical rule for early-stage MVPs**: If your experiment can't reach even the smallest sample size in the table above within 4 weeks, either:
1. Expand traffic/recruitment before running the test, OR
2. Use qualitative methods (concierge) instead of statistical significance

**Do NOT** interpret a result from n=30 as "statistically validated." It's a directional signal only.

---

## Pivot/Persevere Decision Matrix

After each cycle, use this matrix. Requires filling in the Experiment Card first.

```
PIVOT / PERSEVERE MATRIX

                        METRICS          METRICS
                        MET              NOT MET
                     ┌──────────────┬──────────────────────┐
CUSTOMERS SAY        │              │                      │
THEY WANT IT         │  PERSEVERE   │  EXECUTION PROBLEM   │
                     │  (double     │  (improve delivery,  │
                     │   down)      │   don't pivot yet)   │
                     ├──────────────┼──────────────────────┤
CUSTOMERS DO NOT     │  WRONG       │  PIVOT               │
SAY THEY WANT IT     │  SEGMENT     │  (assumption is      │
                     │  (same prod, │   wrong, change      │
                     │  diff target)│   strategy)          │
                     └──────────────┴──────────────────────┘

HOW TO USE:
1. "Metrics met" = primary success metric passed threshold from Experiment Card
2. "Customers say they want it" = ≥ 60% of interviewed users express clear desire
   to continue or strong disappointment if removed

EXECUTION PROBLEM signals (top-right cell):
  - Users understand and want the product
  - But conversion / retention / activation is low
  - Fix: onboarding, UX, pricing, not the core concept

WRONG SEGMENT signals (bottom-left cell):
  - Metrics look ok in aggregate but driven by a small sub-group
  - Most users don't "get it" but a niche does
  - Fix: fire the non-niche users, focus entirely on niche
```

---

## Assumption Priority Ladder

Before writing an Experiment Card, stack-rank your assumptions. Test the highest-risk one first.

```
ASSUMPTION STACK RANKING

Score each assumption: Risk × Unknownness (1-5 scale each)

ASSUMPTION                          RISK  UNKNOWN  SCORE  TEST FIRST?
─────────────────────────────────────────────────────────────────────
[Write your assumptions below]
1. ______________________________    ___    ___     ___      [ ]
2. ______________________________    ___    ___     ___      [ ]
3. ______________________________    ___    ___     ___      [ ]
4. ______________________________    ___    ___     ___      [ ]
5. ______________________________    ___    ___     ___      [ ]

Risk = How bad is it if this is wrong? 
  1 = minor setback, 5 = kills the company

Unknownness = How sure are you this is true?
  1 = certain (you have data), 5 = pure guess

Sort by Score descending. Test Score ≥ 15 first.
Never test Score < 8 before testing all Score ≥ 15.
```

**Worked example**:

| Assumption | Risk | Unknown | Score |
|---|---|---|---|
| Restaurants will share inventory data with software | 5 | 5 | 25 |
| Restaurant owners will pay $99/mo | 4 | 4 | 16 |
| We can reduce spoilage ≥ 15% with our algorithm | 3 | 4 | 12 |
| Owners prefer mobile over desktop | 2 | 3 | 6 |

Test "will share data" (score 25) first — before pricing, before algorithm quality, before mobile vs. desktop. If they won't share data, everything else is irrelevant.

---

## Cycle Log (Running Record)

Maintain this across the life of your product. It's your validated learning ledger.

```
CYCLE LOG

Product: ___________________________  Started: ___________

┌──────┬─────────────────────┬──────────────┬────────────────────────┐
│ Cycle│ Assumption tested   │ Result       │ Decision               │
├──────┼─────────────────────┼──────────────┼────────────────────────┤
│  1   │                     │ Pass/Fail/   │ Persevere / Pivot:     │
│      │                     │ Gray         │                        │
├──────┼─────────────────────┼──────────────┼────────────────────────┤
│  2   │                     │              │                        │
├──────┼─────────────────────┼──────────────┼────────────────────────┤
│  3   │                     │              │                        │
├──────┼─────────────────────┼──────────────┼────────────────────────┤
│  4   │                     │              │                        │
└──────┴─────────────────────┴──────────────┴────────────────────────┘

PIVOT HISTORY
┌──────────┬──────────────────────┬──────────────────────────────────┐
│ Date     │ Pivot type           │ What changed                     │
├──────────┼──────────────────────┼──────────────────────────────────┤
│          │                      │                                  │
└──────────┴──────────────────────┴──────────────────────────────────┘
```

**Rule**: If you reach Cycle 3 without a Pass on your top-priority assumption, hold a formal Pivot/Persevere meeting before starting Cycle 4. Continuing past 3 failed cycles without a deliberate decision is drift, not learning.
