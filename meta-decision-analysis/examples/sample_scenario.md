파일을 작성합니다.

```markdown
# Example: Video Infrastructure Vendor Decision

## Scenario

Nexlayer is a B2B SaaS company ($8M ARR) offering async video collaboration features. Their 3-year Mux contract expires end of Q2 2026. Mux has proposed a renewal with a 20% price increase. The CTO has put three alternatives on the table and wants a structured recommendation before the renewal deadline in two weeks.

**Options on the table:**
1. **Renew with Mux** — 3-year contract at new pricing (~$420k total)
2. **Migrate to Cloudflare Stream** — cheaper, less mature, 6-week migration (~$180k total)
3. **Build in-house** — full control, 6-month build (~$510k total: $310k infra + $200k eng)
4. **Do nothing** — extend month-to-month at 40% penalty rates (~$540k over 3 years)

---

## Analysis

### Step 1 — Define Criteria and Weights (Before Scoring)

The CTO, VP Eng, and CFO independently proposed criteria, then aligned on:

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| 3-Year Total Cost | 30% | Company is tightening burn ahead of Series B |
| Engineering Effort (migration) | 20% | Team is mid-sprint on core product |
| Feature Completeness | 25% | Video analytics is a key differentiator for enterprise deals |
| Vendor Reliability / SLA | 15% | Two outages in FY25 cost ~$60k in churn |
| Strategic Flexibility | 10% | Board wants optionality as AI video features emerge |

**Total: 100%** — criteria locked before any option was scored.

---

### Step 2 — Score Each Option (1–5 scale)

Scoring rubric anchors (defined before scoring):
- **Cost** — 5 = lowest TCO, 1 = highest TCO
- **Effort** — 5 = no migration work, 1 = 6+ months of eng time
- **Features** — 5 = full parity + analytics, 1 = missing critical capabilities
- **Reliability** — 5 = 99.99% SLA with proven track record, 1 = unknown/unproven
- **Flexibility** — 5 = month-to-month or full ownership, 1 = multi-year lock-in

| Criterion | Weight | Mux Renew | Cloudflare | Build In-House | Do Nothing |
|-----------|--------|-----------|------------|----------------|------------|
| 3-Year Cost | 30% | 3 ($420k) | 5 ($180k) | 2 ($510k) | 1 ($540k) |
| Eng Effort | 20% | 5 (minimal) | 3 (6 wks) | 1 (6 months) | 5 (none) |
| Feature Completeness | 25% | 5 (best-in-class) | 3 (analytics gaps) | 4 (custom fit) | 5 (same as Mux) |
| Reliability / SLA | 15% | 5 (99.99%, proven) | 3 (99.9%, newer) | 2 (unknown) | 5 (same as Mux) |
| Strategic Flexibility | 10% | 2 (3-yr lock-in) | 4 (1-yr contract) | 5 (full control) | 5 (cancel anytime) |

### Step 3 — Calculate Weighted Totals

| Option | Calculation | **Total** |
|--------|-------------|-----------|
| Mux Renew | 0.30×3 + 0.20×5 + 0.25×5 + 0.15×5 + 0.10×2 | **4.10** |
| Cloudflare Stream | 0.30×5 + 0.20×3 + 0.25×3 + 0.15×3 + 0.10×4 | **3.70** |
| Build In-House | 0.30×2 + 0.20×1 + 0.25×4 + 0.15×2 + 0.10×5 | **2.60** |
| Do Nothing | 0.30×1 + 0.20×5 + 0.25×5 + 0.15×5 + 0.10×5 | **3.80** |

**Matrix winner: Mux Renew (4.10)**

---

### Step 4 — Decision Tree: Expected Value of Cloudflare Migration Risk

Cloudflare's lower score on reliability warrants an explicit EV check. VP Eng estimated:

```
Switch to Cloudflare:
  ├── 70%: Migration succeeds, stable service
  │         Net savings vs Mux: +$240k → Payoff: +$240k
  ├── 20%: 2 major outages in year 1
  │         Savings offset by $80k churn + $50k remediation
  │         → Payoff: +$110k
  └── 10%: Critical failure, emergency rollback to Mux
            $60k emergency costs + $200k churn loss
            → Payoff: −$20k

EV = 0.70(240) + 0.20(110) + 0.10(−20)
   = 168 + 22 − 2
   = +$188k expected net benefit vs renewing with Mux
```

**EV finding**: Cloudflare has positive expected value even with failure scenarios priced in. However, EV ignores that Nexlayer cannot absorb the 10% catastrophic scenario — $200k churn would represent 2.5% ARR lost in a single event, right before a fundraise.

---

### Step 5 — Sensitivity Analysis

**Key question**: How cost-sensitive is this decision?

If the team weights **Cost at 50%** (instead of 30%) and reduces **Feature Completeness to 5%** (treating video analytics as a nice-to-have rather than a differentiator):

| Option | Recalculated Total |
|--------|--------------------|
| Mux Renew | 0.50×3 + 0.20×5 + 0.05×5 + 0.15×5 + 0.10×2 = **3.70** |
| Cloudflare | 0.50×5 + 0.20×3 + 0.05×3 + 0.15×3 + 0.10×4 = **4.10** |
| Do Nothing | 0.50×1 + 0.20×5 + 0.05×5 + 0.15×5 + 0.10×5 = **3.25** |

**Winner flips to Cloudflare** when cost dominates. The decision hinges on one factual question: *Is video analytics a real enterprise deal-blocker, or just nice to have?*

The team pulled 6 months of deal notes: video analytics was mentioned as a requirement in 4 of the last 7 enterprise deals won. **Feature Completeness stays at 25%.**

---

## Result

```markdown
# Decision Analysis: Video Infrastructure Vendor (Q2 2026)

## Alternatives
1. Renew with Mux (3-year, $420k)
2. Migrate to Cloudflare Stream ($180k)
3. Build in-house ($510k)
4. Do nothing — month-to-month ($540k)

## Decision Matrix
| Criterion | Weight | Mux Renew | Cloudflare | In-House | Do Nothing |
|-----------|--------|-----------|------------|----------|------------|
| 3-Year Cost | 30% | 3 | 5 | 2 | 1 |
| Eng Effort | 20% | 5 | 3 | 1 | 5 |
| Feature Completeness | 25% | 5 | 3 | 4 | 5 |
| Reliability / SLA | 15% | 5 | 3 | 2 | 5 |
| Strategic Flexibility | 10% | 2 | 4 | 5 | 5 |
| **Weighted Total** | 100% | **4.10** | **3.70** | **2.60** | **3.80** |

## Sensitivity Analysis
- If Cost weight rises from 30% → 50% (and Feature drops 25% → 5%),
  winner changes from Mux Renew to Cloudflare Stream.
- Confirmed: video analytics appeared in 4/7 recent enterprise deals —
  feature completeness weight stands at 25%.

## Recommendation
**Renew with Mux for 3 years.**

Rationale: Mux leads on the two criteria most tied to revenue risk
(Feature Completeness, Reliability). The $240k cost premium over
Cloudflare is the price of protecting enterprise deal flow and avoiding
a high-risk migration right before a fundraise.

Trade-off acknowledged: Nexlayer accepts the 20% price increase and
3-year lock-in. Revisit at contract midpoint (Q4 2027) once Cloudflare
Stream's enterprise analytics roadmap matures and the company's ARR
base can better absorb migration risk.
```
```
