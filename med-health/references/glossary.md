# Medical & Epidemiological Glossary

## Evidence Hierarchy (Strong → Weak)

- **Systematic Review / Meta-analysis**: Combines results from multiple randomized trials using statistical methods. Highest level. Example: Cochrane review of 15 RCTs on drug efficacy.
- **Randomized Controlled Trial (RCT)**: Participants randomly assigned to treatment or control; blinded when possible. Gold standard for efficacy. Example: WOSCOPS trial (n=6,595).
- **Cohort Study**: Follows groups over time; observational (not randomized). Weaker than RCT but useful for long-term outcomes. Example: Framingham Heart Study.
- **Case-Control Study**: Retrospective; compares people with disease to matched controls. Efficient but prone to recall bias.
- **Case Series / Case Report**: Describes one or few patients. Anecdotal; generates hypotheses, does not prove causation.
- **Expert Opinion / Editorial**: Experienced clinician's judgment. Lowest evidence level.

## Key Statistical Terms

| Term (English) | Term (Chinese) | Definition | Example |
|---|---|---|---|
| **Relative Risk (RR)** | 相對風險 | Ratio of event rate in treatment group to control group | RR = 0.65 means treatment group has 65% of control's risk (35% reduction) |
| **Absolute Risk Reduction (ARR)** | 絕對風險下降 | Difference in event rates between groups (percentage points) | If control 4% and treatment 2%, ARR = 2 percentage points |
| **Number Needed to Treat (NNT)** | 需治療人數 | How many patients must receive treatment to prevent one adverse event | NNT = 50 means treat 50 people to prevent 1 case (inverse of ARR) |
| **Hazard Ratio (HR)** | 危害比 | Risk ratio in time-to-event analysis (survival studies) | HR = 0.8 means treatment reduces instantaneous risk by 20% |
| **Confidence Interval (CI)** | 信賴區間 | Range containing true effect with 95% probability | 95% CI 25–43% means we are 95% sure true RR reduction is between 25–43% |
| **P-value** | P 值 | Probability that observed result occurred by chance (under null hypothesis) | P < 0.05 = statistically significant (conventional threshold) |
| **Statistical Significance** | 統計顯著性 | Result unlikely due to random chance (p < 0.05); does NOT imply clinical importance | Small study with large sample can show statistical significance on tiny effect |
| **Clinical Significance** | 臨床顯著性 | Difference large enough to matter in patient care | NNT < 10 usually clinically significant; NNT > 100 usually not |

## Clinical Trial Phases

| Phase | Size | Purpose | Notes |
|-------|------|---------|-------|
| **Phase I** | 20–100 patients | Safety, dosage, side effects | First-in-human; not efficacy |
| **Phase II** | 100–500 patients | Efficacy, side effects, dosage refinement | Does it work? At what dose? |
| **Phase III** | 500–5,000 patients | Confirm efficacy, monitor side effects, comparison with standard treatment | Required for approval |
| **Phase IV** | Entire population after approval | Post-market surveillance, long-term safety, efficacy in different populations | Ongoing monitoring |

## Disease Measurement Concepts

| Term (English) | Term (Chinese) | Definition | Example |
|---|---|---|---|
| **Incidence** | 發生率 | New cases in a population during a time period | 2,000 new cases of X disease in Taiwan in 2025 |
| **Prevalence** | 盛行率 | Total cases (new + existing) at a point in time | 50,000 people living with X disease in Taiwan (point estimate) |
| **Mortality Rate** | 死亡率 | Deaths divided by population | 10 deaths per 100,000 per year |
| **Case Fatality Rate (CFR)** | 個案致死率 | Deaths divided by confirmed cases (during outbreak) | 200 deaths / 1,000 cases = 20% CFR |
| **Sensitivity** | 敏感度 | Proportion of true cases detected by a test | If test sensitivity 90%, it catches 90% of actual cases |
| **Specificity** | 特異度 | Proportion of non-cases correctly identified | If test specificity 95%, it correctly excludes 95% of non-cases |
| **Positive Predictive Value (PPV)** | 陽性預測值 | Probability a positive test result is truly positive | Depends on prevalence; high prevalence = higher PPV |

## Trial Design Terms

| Term | Meaning | Implication |
|------|---------|-------------|
| **Randomized** | 隨機分配 | Treatment assignment by chance, not selection; reduces bias | Gold standard; removes selection bias |
| **Double-blind** | 雙盲 | Neither participants nor researchers know who receives treatment/placebo | Reduces expectation bias |
| **Placebo-controlled** | 安慰劑對照 | Control group receives inert substance, not standard care | Strong for efficacy; less practical for serious diseases |
| **Active-control** | 主動對照 | Control group receives standard treatment (not placebo) | More ethical; harder to show superiority |
| **Intent-to-Treat (ITT)** | 意向治療 | Analyzes all enrolled participants as assigned (regardless of adherence) | Conservative; reflects real-world outcomes |
| **Per-Protocol** | 按協議 | Analyzes only those who completed treatment as assigned | Optimistic; may overestimate efficacy |

## Common Pitfalls in Reading Medical News

| Error | Definition | Example |
|-------|-----------|---------|
| **Confounding** | Third variable explains the association, not the treatment | Coffee drinkers have more heart disease (confound: smoking) |
| **Correlation vs. Causation** | Association ≠ causation | Vaccines given before illness started; post hoc ergo propter hoc |
| **Lead-time Bias** | Early detection improves measured survival without extending life | PSA screening finds cancer earlier but doesn't improve survival |
| **Selection Bias** | Who enrolls in study differs systematically from general population | Trial enrolls younger, healthier patients than real-world population |
| **Publication Bias** | Positive results more likely published than negative; skews evidence base | Meta-analysis inflated if unpublished negative trials exist |
| **P-hacking** | Testing many hypotheses until one reaches p < 0.05 by chance | 100 comparisons tested; 5 likely "significant" by chance alone |
| **Subgroup Analysis** | Breaking data into subgroups increases false-positive risk | Trial shows no overall benefit, but one subgroup appears to benefit (needs replication) |

## Regulatory Approval Terms

| Term (English) | Term (Chinese) | Taiwan Process |
|---|---|---|
| **Expedited Review** | 加速審查 | FDA FDA Taiwan fast-tracks promising drugs (e.g., orphan disease, unmet need) | 食藥署可核准加速審查;縮短審核期 |
| **Breakthrough Therapy** | 突破性治療認定 | FDA designation accelerating review for serious diseases with preliminary evidence of substantial improvement | Not standard Taiwan process; FDA designation may influence 食藥署 |
| **Conditional Approval** | 條件核准 | Approval with post-market monitoring requirements | 食藥署核准並要求廠商進行上市後監測 |
| **Recall** | 回收 | Product withdrawn from market due to safety issue | 食藥署發布公告下架或回收 |

## Taiwan-Specific Legal/Regulatory Terms

| Term | Definition | Relevance to news |
|------|-----------|-------------------|
| **食藥署** | Taiwan FDA equivalent | Primary source for drug/device approvals and safety alerts |
| **健保署** | National Health Insurance Administration | Coverage & reimbursement decisions; budgetary impact |
| **衛福部** | Ministry of Health & Welfare | Policy umbrella; vaccine policy, health campaigns |
| **疾管署** | Taiwan CDC | Disease surveillance, outbreak response, epidemiological data |
| **臨床試驗** | Clinical trial (formally registered) | Must report results within specified timeframe |
| **PDPA (個人資料保護法)** | Personal Data Protection Act | Restricts patient identity disclosure; impacts de-identification |
| **醫療法 §72** | Medical Care Act, Article 72 | Patient privacy in medical records; restricts disclosure without consent |
