# Migration Playbook: Switching Bid Strategies

This playbook covers the operational steps for migrating between bidding strategies without destroying campaign performance. It does **not** cover strategy selection (see SKILL.md) — it assumes you have already decided where you're going.

---

## Migration Paths

Not all transitions are equal. Some are safe; others carry high risk of performance collapse.

```
Manual CPC ──► Maximize Clicks (safe, no conversion data needed)
Manual CPC ──► Maximize Conversions (safe if ≥ 30 conv/month)
Manual CPC ──► Target CPA (moderate; requires ≥ 50 conv/month)
Manual CPC ──► Target ROAS (high risk; requires ≥ 50 conv/month + revenue data)

Maximize Conversions ──► Target CPA (safe upgrade path)
Target CPA ──► Target ROAS (moderate; requires reliable conversion value data)
Target ROAS ──► Target CPA (safe downgrade, typically for revenue data loss)

Target CPA ──► Manual CPC (emergency rollback)
Target ROAS ──► Manual CPC (emergency rollback)
```

**Never skip rungs upward.** Going Manual CPC → Target ROAS in one step is high risk. The algorithm has no campaign-specific prior data and will burn budget during the learning period.

---

## Pre-Migration Checklist

Run through this before touching the strategy setting. A failed pre-check means delay the migration, not skip the check.

### Conversion Data Requirements (Iron Law reinforcement)

| Target Strategy | Min Monthly Conversions | Min Weeks of History | Revenue Data Required? |
|---|---|---|---|
| Maximize Clicks | 0 | 0 | No |
| Maximize Conversions | 30 | 4 | No |
| Target CPA | 50 | 6 | No |
| Target ROAS | 50 | 6 | Yes — accurate values |

Count conversions at the **campaign level**, not account level. Cross-campaign data does not help the algorithm for a specific campaign.

### Conversion Tracking Audit

Before any migration, verify:

1. **Tag fires on the right page** — for purchase, tag must fire on the confirmation/thank-you page, not the checkout page.
2. **No duplicate counting** — load tag manager in preview mode and confirm exactly 1 conversion fires per test purchase.
3. **Attribution window matches purchase cycle** — B2B with 7-day sales cycle needs at least a 7-day click attribution window, ideally 14-day.
4. **Values are accurate (for Target ROAS)** — spot-check 5 transactions: compare reported conversion value vs actual order value in your backend. Variance > 10% is a blocker.

If conversion tracking has been broken for any period in the past 30 days, the historical data is corrupted. Delay migration until you have 4+ clean weeks of data.

### Budget Adequacy Check

For Target CPA, the daily budget must be at least **5–10× the target CPA** to give the algorithm room to operate.

```
Minimum daily budget = target_CPA × 5

Example:
  target_CPA = NT$500
  minimum_daily_budget = NT$500 × 5 = NT$2,500/day
```

If the budget is below this threshold, the algorithm will under-deliver rather than overspend — the campaign will appear to "not work" when the actual problem is budget constraint.

For Target ROAS:
```
Minimum daily budget = (avg_order_value / target_ROAS) × 5

Example:
  avg_order_value = NT$1,500
  target_ROAS = 300% (3.0)
  implied_CPA = NT$1,500 / 3.0 = NT$500
  minimum_daily_budget = NT$500 × 5 = NT$2,500/day
```

---

## Migration Procedures

### Procedure A: Manual CPC → Target CPA

This is the most common migration and the one most likely to cause panic if the operator doesn't understand the learning period.

**Step 1: Establish baseline (Week -2 to 0)**

Record these metrics for the 14 days before migration:
- Average CPA
- Daily conversion volume
- Impression share
- Average CPCmax (highest bids in the campaign)

```
Baseline template:
  period: [start_date] to [end_date]
  avg_CPA: NT$___
  daily_conversions: ___
  impression_share: ___%
  avg_max_CPC: NT$___
```

**Step 2: Set initial target CPA**

Do not set the target to your ideal CPA. Set it to your **current actual CPA** or slightly above (+10–20%). The algorithm needs room to succeed.

```
Conservative initial target = current_avg_CPA × 1.1

Example:
  current_avg_CPA = NT$450
  initial_target_CPA = NT$450 × 1.1 = NT$495
  (round to NT$500 for cleanliness)
```

Setting an aggressive target immediately (e.g., current CPA is NT$450, target set to NT$300) causes the algorithm to restrict bids so aggressively that conversion volume collapses. This is the #1 cause of failed Target CPA migrations.

**Step 3: Switch strategy**

In Google Ads / Meta:
- Change bidding strategy to Target CPA
- Enter the target calculated in Step 2
- Do NOT change budget, ad copy, landing pages, or audience targeting at the same time — you need to isolate the variable

**Step 4: Do not touch anything for 14 days**

The learning period is 7–14 days depending on conversion volume. During this period:
- CPA will fluctuate significantly (±40% swings are normal)
- Volume may drop temporarily
- The "Limited by learning" status badge is expected

The only trigger to intervene early is **catastrophic** performance: zero conversions for 5+ consecutive days with normal impression volume. That indicates a tracking break, not a learning issue.

**Step 5: Post-learning evaluation**

After 14 days, compare actual CPA to target:

```
acceptable_range = [target_CPA × 0.8, target_CPA × 1.2]

If actual_CPA is within range: migration successful, proceed to Step 6
If actual_CPA > target × 1.2: target is too aggressive, raise by 15%
If actual_CPA < target × 0.8: room to lower target by 10-15%
```

**Step 6: Optimization phase (Week 3–8)**

Once stable, reduce target CPA in increments of 5–10% every 2 weeks. Do not reduce by more than 10% at a time — each reduction triggers a mini-learning period.

```
Reduction schedule example:
  Week 2: NT$500 (initial)
  Week 4: NT$475 (-5%)
  Week 6: NT$450 (-5%)
  Week 8: NT$430 (-4.4%) ← approaching floor
```

Stop reducing when conversion volume drops below 80% of pre-migration baseline. That's the efficiency frontier for this campaign.

---

### Procedure B: Target CPA → Target ROAS

This is an upgrade that requires one additional data source: reliable conversion values.

**Pre-condition: Validate conversion value data**

Pull the last 30 days of conversions. For each, compare:
- Reported `conversion_value` in the ad platform
- Actual revenue in your order management system or CRM

```python
# Validation check
discrepancies = [(reported, actual) for reported, actual in value_pairs 
                 if abs(reported - actual) / actual > 0.10]
error_rate = len(discrepancies) / len(value_pairs)

# Block migration if:
if error_rate > 0.05:  # More than 5% of conversions have >10% value error
    raise ValueError(f"Conversion value accuracy too low: {error_rate:.1%}")
```

If conversion values are dynamic (vary per order), also check that the value parameter is being passed correctly in the conversion tag — not hardcoded to a fixed amount.

**Set initial Target ROAS**

```
initial_target_ROAS = (current_conversion_value_total / current_cost) × 0.9

Example:
  last_30_days_revenue = NT$150,000
  last_30_days_cost = NT$50,000
  current_ROAS = 150,000 / 50,000 = 3.0 (300%)
  initial_target_ROAS = 3.0 × 0.9 = 2.7 (270%)
```

Set 10% below current ROAS for the same reason as CPA migration: give the algorithm room to succeed initially. A ROAS target above current performance will cause the algorithm to restrict bids and collapse volume.

**Migration steps** are identical to Procedure A (baseline → switch → no-touch 14 days → evaluate → optimize), with ROAS replacing CPA as the primary metric.

---

### Procedure C: Emergency Rollback to Manual CPC

Use this when automated bidding has failed catastrophically and you need immediate control.

**Indicators for rollback:**
- CPA > 2× target for 5+ consecutive days
- Conversion volume drops to < 30% of baseline for 3+ consecutive days
- Conversion tracking is confirmed broken

**Rollback steps:**

1. Switch to Manual CPC immediately
2. Set initial bids using the last-known Average CPCmax from your baseline record
3. If you don't have a baseline record, use the platform's recommended bid estimate as a floor and add 20%
4. Investigate root cause before attempting any automated strategy again

After a rollback, wait until the conversion data issue is resolved **and** accumulate at least 4 new weeks of clean data before migrating again. The corrupted data from the failed migration period poisons the algorithm's recent signal.

---

## Worked Migration Example

**Scenario:** Mid-sized e-commerce, fashion apparel, Taiwan market

**Starting state (Manual CPC):**
- Monthly conversions: 95
- Avg CPA: NT$420
- Daily budget: NT$8,000
- Goal: Maintain CPA while growing volume

**Pre-migration check:**
```
✓ Monthly conversions: 95 ≥ 50 (meets Target CPA threshold)
✓ Conversion tracking: verified, no duplicates
✓ Budget adequacy: NT$8,000/day ÷ NT$420 CPA ≈ 19× (well above 5× minimum)
✓ Attribution window: 7-day click (purchase cycle is same-day, window is fine)
```

**Initial target CPA calculation:**
```
current_avg_CPA = NT$420
initial_target_CPA = NT$420 × 1.1 = NT$462 → round to NT$460
```

**Week 1-2 (Learning period):**
```
Day 1-3:  CPA = NT$380–NT$510 (high variance, expected)
Day 4-7:  CPA = NT$400–NT$480 (stabilizing)
Day 8-14: CPA = NT$430–NT$460 (within range)
Daily conversions: 2-4 (vs pre-migration avg of 3.2/day — acceptable)
```

**Post-learning evaluation (Day 15):**
```
14-day avg CPA = NT$445
target CPA = NT$460
acceptable_range = [NT$368, NT$552]
Result: NT$445 ∈ [NT$368, NT$552] → SUCCESS
```

**Optimization schedule:**
```
Day 15: target NT$460 → NT$440 (-4.3%)
Day 29: actual 14-day CPA = NT$432, target still NT$440 → lower to NT$420
Day 43: actual 14-day CPA = NT$418, target NT$420 → lower to NT$400
Day 57: actual 14-day CPA = NT$428, volume dropped 22% → STOP, hold at NT$400
```

**Final state:** CPA reduced from NT$420 to NT$400 (-4.8%), volume maintained within 10% of pre-migration level. The efficiency floor was hit at NT$400 — further reduction caused volume collapse.

---

## Common Migration Failure Modes

| Failure | Symptom | Root Cause | Fix |
|---|---|---|---|
| Aggressive initial target | Volume collapses immediately | Target set far below current CPA | Raise target to current CPA + 10% |
| Impatient optimization | Repeated target changes week 1 | Not respecting learning period | Hold for 14 days minimum |
| Budget too tight | Spend < 50% of budget, low volume | Budget < 5× CPA | Raise budget or raise CPA target |
| Micro-conversion mismatch | Volume up, revenue flat | Algorithm optimized for proxy event | Switch to final purchase conversion |
| Seasonality shock | CPA spikes during peak season | Algorithm unprepared for demand shift | Use seasonality adjustments; revert briefly to manual during peaks |
| Value data mismatch (ROAS) | ROAS in platform ≠ actual revenue | Tag hardcoded or misfiring | Fix tag before attempting ROAS strategy |

---

## Timing Constraints

**Avoid migrating during:**
- Peak season (Black Friday, Double 11, CNY) — algorithm has insufficient prior data for the new volume pattern
- Active promotions — discounted prices shift conversion value and confuse ROAS optimization
- First 30 days of a new campaign — insufficient historical data
- Within 2 weeks of a major landing page or offer change — separating variables is impossible

**Prefer migrating during:**
- Stable, non-promotional periods
- When you have 8+ weeks of clean historical data
- When you have ≥ 30 days before the next major peak season (to complete learning before you need peak performance)
