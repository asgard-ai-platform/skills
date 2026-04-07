---
name: "mfg-supplier-scorecard"
description: "Evaluate and manage suppliers using weighted scorecards across quality, delivery, price, and service dimensions. Use this skill when the user needs to assess supplier performance, compare vendors for selection, design a supplier rating system, or manage supplier development — even if they say 'which supplier should we choose', 'rate our vendors', 'this supplier keeps delivering late', or 'build a vendor evaluation system'."
metadata:
  category: "WP-03 製造業"
  tags: ["manufacturing", "procurement", "supplier-management"]
---

# Supplier Scorecard

## Framework

```
IRON LAW: Evaluate on QCDS (Quality, Cost, Delivery, Service) — Not Just Price

The cheapest supplier who delivers defective parts late with no support
is the most expensive supplier. Total Cost of Ownership (TCO) includes:
purchase price + incoming inspection + rework + downtime from defects +
expediting fees + management overhead.

NEVER select suppliers on price alone.
```

### Four Evaluation Dimensions (QCDS)

| Dimension | Weight (typical) | KPIs |
|-----------|-----------------|------|
| **Quality** | 30-40% | Defect rate (PPM), incoming inspection pass rate, certifications (ISO 9001), corrective action responsiveness |
| **Cost** | 20-30% | Unit price, total cost of ownership, price stability, payment terms |
| **Delivery** | 20-30% | On-time delivery rate, lead time, lead time variability, flexibility for rush orders |
| **Service** | 10-20% | Responsiveness, communication quality, technical support, willingness to collaborate on improvements |

### Scoring Method

1. **Define KPIs** per dimension (2-3 per dimension)
2. **Set weights** (must sum to 100%)
3. **Score each KPI**: 1-5 scale with clear definitions:
   - 5 = Excellent (top 10% of suppliers)
   - 4 = Good (meets all requirements consistently)
   - 3 = Acceptable (meets most requirements)
   - 2 = Below expectations (frequent issues)
   - 1 = Unacceptable (critical problems)
4. **Calculate weighted total**
5. **Classify**: A (>4.0), B (3.0-4.0), C (2.0-3.0), D (<2.0)

### Supplier Classification & Actions

| Grade | Score | Strategy |
|-------|-------|---------|
| **A** | >4.0 | Preferred supplier, increase business, joint development |
| **B** | 3.0-4.0 | Approved supplier, maintain, targeted improvement |
| **C** | 2.0-3.0 | Conditional, improvement plan required within 90 days |
| **D** | <2.0 | Phase out, begin alternative sourcing immediately |

### Risk Assessment

| Risk Factor | Question | Mitigation |
|-------------|---------|-----------|
| **Single source** | Is this supplier the only source for a critical component? | Develop backup supplier |
| **Geographic** | Is the supplier in a region prone to disruption? | Dual-source across regions |
| **Financial** | Is the supplier financially stable? | Monitor credit, require financial disclosures |
| **Capacity** | Can the supplier scale with our growth? | Capacity commitment agreements |
| **IP** | Does the supplier have access to our proprietary designs? | NDA + IP clauses in contract |

### Supplier Development Program (SDP)

For C-grade suppliers worth keeping:
1. **Gap analysis**: Where specifically are they falling short?
2. **Improvement plan**: Specific, measurable, time-bound targets
3. **Support**: Provide training, share best practices, co-invest if needed
4. **Review**: Monthly progress checks, 90-day formal reassessment
5. **Decision**: Improved to B+ → continue. Still C or worse → phase out.

## Output Format

```markdown
# Supplier Scorecard: {Supplier Name}

## Overall Score: {X.X} / 5.0 — Grade: {A/B/C/D}

## Detailed Scores
| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|---------|
| Quality | {%} | {X.X} | {X.XX} |
| Cost | {%} | {X.X} | {X.XX} |
| Delivery | {%} | {X.X} | {X.XX} |
| Service | {%} | {X.X} | {X.XX} |
| **Total** | **100%** | — | **{X.XX}** |

## KPI Details
| KPI | Target | Actual | Score |
|-----|--------|--------|-------|
| Defect rate | <500 PPM | {X} PPM | {1-5} |
| On-time delivery | >95% | {%} | {1-5} |
| ... | ... | ... | ... |

## Risk Assessment
| Risk | Level | Mitigation |
|------|-------|-----------|
| {risk} | H/M/L | {action} |

## Action Plan
{Based on grade: preferred/maintain/improve/phase out}
```

## Gotchas

- **Weighting should reflect YOUR priorities**: A medical device company should weight Quality at 50%+. A commodity buyer might weight Cost at 40%. Don't use generic weights.
- **Score inflation**: Purchasing teams may inflate scores to avoid difficult conversations with suppliers. Require data-backed evidence for each score.
- **Review frequency**: A-grade quarterly, B/C-grade monthly, D-grade weekly until resolved.
- **Supplier relationship matters**: Scorecards are tools for improvement, not punishment. Share results with suppliers transparently — the best suppliers want feedback.
- **TCO includes hidden costs**: Don't forget: incoming inspection labor, warehouse space for safety stock (to cover unreliable delivery), engineering time for quality issues, customs/logistics for overseas suppliers.

## References

- For TCO calculation methodology, see `references/tco-calculation.md`
- For supplier audit checklists, see `references/supplier-audit.md`
