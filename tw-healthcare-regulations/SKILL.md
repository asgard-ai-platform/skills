---
name: "tw-healthcare-regulations"
description: "Navigate Taiwan healthcare regulations including NHI system, medical device classification, drug registration, telemedicine rules, and health data protection. Use this skill when the user is building a health tech product for Taiwan, needs to understand NHI, evaluate medical device regulatory pathways, or assess telemedicine compliance — even if they say 'sell a medical device in Taiwan', 'how does NHI work', 'telemedicine regulations', or 'health data privacy in Taiwan'."
metadata:
  category: "WP-12 產業知識"
  tags: ["industry", "taiwan", "healthcare", "regulation"]
---

# Taiwan Healthcare Regulations

## Framework

```
IRON LAW: NHI Shapes Everything in Taiwan Healthcare

Taiwan's National Health Insurance (全民健保) covers 99.9% of the
population. Any healthcare product or service strategy in Taiwan must
account for NHI — either by getting NHI reimbursement (volume play)
or by positioning as self-pay/premium (margin play).

Ignoring NHI is like ignoring gravity.
```

### NHI System Overview

| Aspect | Detail |
|--------|--------|
| Coverage | 99.9% of population (23M+ people) |
| Single payer | 衛生福利部中央健康保險署 (NHIA) |
| Premium | 5.17% of insured salary (shared: employer 60%, employee 30%, government 10%) |
| Co-pay | Outpatient: NT$50-420. Hospitalization: 5-30% (capped) |
| Drug pricing | NHIA sets reimbursement prices via Drug Expenditure Target (DET) |
| Annual budget | ~NT$800B+ (growing 4-5% annually) |

### Medical Device Regulatory Path

| Class | Risk | Examples | Approval Path | Timeline |
|-------|------|---------|-------------|---------|
| **Class I** | Low | Bandages, tongue depressors | Registration (listing) | 1-2 months |
| **Class II** | Medium | Blood pressure monitors, surgical gloves | Technical review | 6-12 months |
| **Class III** | High | Implants, AI diagnostic software | Full clinical review | 12-24 months |
| **SaMD (Software as Medical Device)** | Varies by intended use | AI diagnosis, clinical decision support | Class II or III depending on risk | 6-24 months |

**Regulatory body**: 衛生福利部食品藥物管理署 (TFDA)

### Digital Health Regulatory Landscape

| Category | Regulation Status | Key Rule |
|----------|------------------|---------|
| **Telemedicine** | Expanded post-COVID (通訊診察治療辦法) | Allowed for follow-up visits, chronic disease, remote areas. Initial visits still require in-person for most cases. |
| **AI diagnostics** | SaMD regulation applies | If AI makes/assists clinical decisions, it's a medical device requiring TFDA approval |
| **Health apps** | Unregulated if wellness-only | Crosses into medical device territory if it diagnoses, treats, or monitors a medical condition |
| **Health data** | 個人資料保護法 (PDPA) + 醫療法 | Medical records have stricter protection than general personal data. Patient consent required for data use. |
| **Electronic medical records** | 醫療機構電子病歷製作及管理辦法 | EMR systems must meet MOHW standards. Cloud storage allowed with conditions. |

### Regulatory Decision Tree for Digital Health Products

```
Does your product diagnose, treat, or monitor a medical condition?
├── NO → Not a medical device. General consumer regulations apply.
└── YES → Medical device (SaMD)
    ├── Does it provide clinical decision support?
    │   ├── Autonomous (AI decides) → Class III
    │   └── Assistive (human decides) → Class II
    └── Does it monitor vital signs?
        ├── Clinical grade → Class II-III
        └── Wellness/fitness → Likely not regulated (but verify with TFDA)
```

## Output Format

```markdown
# Healthcare Regulatory Assessment: {Product}

## Product Classification
- Type: Medical device / Wellness / SaMD / Telemedicine
- Risk class: I / II / III
- Regulatory body: TFDA / NHIA / None

## Regulatory Pathway
| Step | Action | Timeline | Cost |
|------|--------|----------|------|
| 1 | {regulatory step} | {months} | NT${X} |

## NHI Strategy
- NHI reimbursement: Pursuing / Not pursuing
- If pursuing: {reimbursement category, pricing strategy}
- If not: {self-pay positioning, target market}

## Compliance Checklist
- [ ] TFDA classification confirmed
- [ ] Clinical data requirements identified
- [ ] Data privacy (PDPA + medical records) compliant
- [ ] NHI reimbursement strategy decided
```

## Gotchas

- **NHI price pressure is relentless**: NHI reimburses at set prices that are revised downward periodically. Building a business dependent on NHI reimbursement means accepting margin erosion over time.
- **SaMD regulation is evolving rapidly**: TFDA is still developing frameworks for AI-based medical devices. What's unregulated today may require approval tomorrow. Monitor regulatory changes actively.
- **Clinical trials may be required**: Class III devices and some Class II devices need clinical evidence. Budget 12-24 months and NT$5-20M+ for clinical trials in Taiwan.
- **Hospital procurement is relationship-driven**: Taiwan's major hospitals (台大, 長庚, 榮總) have procurement committees, but relationships with key opinion leaders (KOLs) in medicine are critical for adoption.
- **This is educational guidance, not regulatory advice**: Taiwan healthcare regulations are complex and change frequently. Consult TFDA directly or engage a regulatory affairs consultant for specific product submissions.

## References

- For TFDA submission procedures, see `references/tfda-submission.md`
- For NHI reimbursement application process, see `references/nhi-reimbursement.md`
