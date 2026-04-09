# Cost-Benefit Analysis

Cost-benefit analysis (CBA) quantifies the net social value of a policy alternative by converting all expected effects into monetary terms. It answers one question: do total benefits exceed total costs? When used alongside the evaluation matrix in the parent skill, CBA provides the **Efficiency** criterion score with numerical backing.

---

## Core Formula

```
NPV = Σ (Bₜ - Cₜ) / (1 + r)ᵗ    for t = 0 to T
```

| Symbol | Meaning |
|--------|---------|
| `NPV` | Net Present Value — the headline result |
| `Bₜ` | Total benefits in year t |
| `Cₜ` | Total costs in year t |
| `r` | Discount rate (social rate of time preference) |
| `T` | Time horizon of the analysis |
| `t = 0` | Present year (no discounting) |

**Benefit-Cost Ratio (BCR):**
```
BCR = PV(Benefits) / PV(Costs)
```
BCR > 1 means benefits outweigh costs. BCR and NPV can rank alternatives differently — use NPV to compare mutually exclusive options, BCR when budget is constrained.

---

## Step-by-Step Procedure

### Step 1: Define the Scope

Before any calculation, fix three boundaries:

- **Perspective**: Whose costs and benefits count? Government budget only? All affected parties in Taiwan? Global externalities?
- **Time horizon**: Long enough to capture major effects. A transit project might need 30 years; a training program might need 5-10.
- **Counterfactual**: Compare against the *status quo* alternative (do nothing), not against an ideal. This aligns with the parent skill's requirement to always include status quo as the baseline.

### Step 2: Enumerate Effects

List every consequence of the policy, positive and negative:

```
For each alternative:
  Benefits:
    - Direct outputs (e.g., injuries prevented, time saved)
    - Indirect/spillover effects (e.g., reduced healthcare burden)
    - Option value (future flexibility preserved)
  Costs:
    - Implementation (capital, setup)
    - Operating (recurring annual)
    - Compliance burden on regulated parties
    - Unintended negative effects
```

**Transfer payments** (taxes, subsidies, transfers between parties) are NOT social benefits or costs — they are distributional. A subsidy shifts money; it doesn't create value. Exclude from NPV, but note in the equity analysis.

### Step 3: Monetize Effects

This is the hardest step. Use the following hierarchy:

| Evidence Type | Method | Example |
|--------------|--------|---------|
| Market price exists | Use market price directly | Cost of materials, labor wages |
| No market but close proxy | Revealed preference | Hedonic pricing for noise pollution (property value drop) |
| Willingness to pay elicited | Stated preference | Contingent valuation surveys |
| Physical unit with literature value | Benefit transfer | VSL (Value of Statistical Life) from existing studies |
| Completely uncertain | Sensitivity analysis range | Use lower/upper bounds |

**Common monetization anchors used in Taiwan policy:**

- **Value of Statistical Life (VSL)**: Taiwan's official figure for road safety analyses is approximately NT$23–27 million per fatality (varies by year; always cite source and year).
- **Value of Time (VOT)**: Ministry of Transportation uses approximately NT$200–350/hour depending on trip purpose.
- **DALY (Disability-Adjusted Life Year)**: For health interventions, WHO-CHOICE threshold for Taiwan is roughly 1–3× GDP per capita per DALY averted ≈ NT$800,000–2,400,000.

### Step 4: Discount Future Values

Choose the discount rate explicitly and defend it:

| Rate | Rationale | Use case |
|------|-----------|---------|
| 3% | Social rate of time preference (long-run growth + pure time preference) | Infrastructure, environment, public health |
| 5% | Government borrowing cost proxy | Budget-constrained government projects |
| 8–10% | Opportunity cost of capital | Projects competing with private investment |

For climate and multi-generational impacts, declining discount rates (3% near-term, 1% long-term) are increasingly standard (Stern Review approach).

**Present Value factor table (for quick estimates):**

| Year | r=3% | r=5% | r=8% |
|------|------|------|------|
| 1 | 0.971 | 0.952 | 0.926 |
| 5 | 0.863 | 0.784 | 0.681 |
| 10 | 0.744 | 0.614 | 0.463 |
| 20 | 0.554 | 0.377 | 0.215 |
| 30 | 0.412 | 0.231 | 0.099 |

### Step 5: Calculate NPV

Sum discounted net benefits across all years.

### Step 6: Sensitivity Analysis

CBA results depend heavily on assumptions. Always test:

1. **Discount rate**: run at r−2%, baseline r, r+2%
2. **Key monetization values**: run at 70%, 100%, 130% of central estimate
3. **Time horizon**: shorter and longer
4. **Participation/take-up rate**: if policy depends on behavior change

Report results as a range, not a single number. A policy whose NPV is positive across all sensitivity runs is robust. A policy that flips from positive to negative under plausible assumptions should be flagged.

---

## Worked Example: Delivery Rider Mandatory Insurance + Training (Option 2)

Using the scenario from the parent SKILL.md.

**Scope:** Government + riders + platforms, 5-year horizon, r = 3%

**Problem baseline (Year 0):**
- 8,000 injury incidents/year involving delivery riders in Taipei
- Average direct cost per incident: NT$180,000 (medical + lost earnings)
- Annual social cost of status quo: 8,000 × NT$180,000 = **NT$1.44 billion/year**

**Policy: Mandatory insurance + 8-hour safety training**

Costs (annual, NT$ million):
```
Year 0 (setup):
  - Regulatory framework + administration:    50
  - Platform compliance systems:             120
  Total Year 0 costs:                        170

Year 1-5 (recurring):
  - Training delivery (~60,000 riders/yr):    90
  - Insurance premium subsidy (partial):     200
  - Enforcement:                              30
  Total annual operating cost:               320
```

Benefits (annual, from Year 1, NT$ million):
```
Injury reduction estimate: 30% (conservative; comparable Singapore program: 35%)
  Injuries avoided: 8,000 × 30% = 2,400/year
  Monetized: 2,400 × NT$180,000 = 432

Severity reduction (surviving serious injuries become minor):
  Additional benefit: ~80

Total annual benefit:                        512
```

**NPV Calculation:**

```python
r = 0.03
T = 5

# Costs
costs = [170, 320, 320, 320, 320, 320]  # Year 0 to Year 5

# Benefits (0 in Year 0, 512M from Year 1)
benefits = [0, 512, 512, 512, 512, 512]

pv_costs = sum(costs[t] / (1 + r)**t for t in range(T+1))
pv_benefits = sum(benefits[t] / (1 + r)**t for t in range(T+1))

npv = pv_benefits - pv_costs
bcr = pv_benefits / pv_costs
```

Results:
```
PV(Costs)    = NT$1,637M
PV(Benefits) = NT$2,343M
NPV          = NT$706M   ← positive: policy passes CBA
BCR          = 1.43      ← NT$1.43 returned per NT$1 spent
```

**Sensitivity check:**

| Scenario | Injury reduction | NPV (NT$M) | BCR |
|----------|-----------------|------------|-----|
| Pessimistic | 15% | −NT$158M | 0.90 |
| Central | 30% | +NT$706M | 1.43 |
| Optimistic | 45% | +NT$1,570M | 1.96 |

**Interpretation:** Policy is NPV-positive under central assumptions but flips negative if the injury reduction effect is below ~22%. This is the key uncertainty to resolve with a pilot program before full rollout.

---

## Common Mistakes

**Double-counting benefits**: If you include "reduced healthcare costs" AND "increased productivity from healthy workers" AND "VSL for injuries prevented" — some of these overlap. Map the causal chain; count each effect once.

**Ignoring distributional effects**: A policy with positive NPV can still be regressive. NPV is aggregate. If NT$700M net benefit flows entirely to platform shareholders while riders bear training costs, NPV is the wrong headline. Report distributional breakdown separately (see Equity criterion in parent skill).

**Optimism bias in costs**: Government project cost estimates are systematically low. Apply a reference class adjustment: infrastructure projects in Taiwan average 30-50% cost overruns. Consider adjusting upward or discounting cost estimates.

**Wrong counterfactual**: Comparing against an impossible ideal ("zero injuries") rather than the realistic status quo inflates apparent benefits. Always compare to what would actually happen without the policy.

**Attributing all correlation to causality**: If injuries decline by 30% after the policy, not all 30% may be *caused* by the policy (secular trends, other concurrent changes). Use quasi-experimental evidence where possible; be explicit when you can't.

---

## When CBA Is Not Sufficient

CBA struggles with:

- **Rights and dignity**: monetizing harm to a person's autonomy is contested
- **Irreversible harms**: extinction, environmental tipping points — standard discounting understates these
- **Distributional justice**: aggregate NPV can mask who wins and loses
- **Uncertainty about effects**: if the mechanism is poorly understood, the numbers are fictional

In these cases, use CBA as one input alongside multi-criteria analysis (the evaluation matrix), not as the decision rule. A policy analyst who presents only NPV and ignores equity and rights has done incomplete work.

---

## Quick Reference: CBA Checklist

```
□ Perspective defined (whose costs/benefits?)
□ Time horizon justified
□ Status quo is the counterfactual baseline
□ Transfer payments excluded from NPV
□ Monetization method stated for each major effect
□ VSL / VOT source and year cited
□ Discount rate chosen and justified
□ Sensitivity analysis run on top 3 uncertain parameters
□ Distributional impact noted separately
□ Optimism bias addressed (cost estimates)
□ Conclusion states NPV range, not a single number
```
