# Medical Evidence Reading: Interpreting Research for Journalism

## Evidence Hierarchy in Practice

```
PYRAMID (Strongest → Weakest)

      Level 1: Systematic review / Meta-analysis of multiple RCTs
               ↑
             Level 2: Large RCT (n > 500, multicenter)
               ↑
             Level 3: Small RCT (n < 500) / Cohort study
               ↑
             Level 4: Case-control study / Case series
               ↑
             Level 5: Case report / Expert opinion
```

**Key principle:** A single study, no matter how large, is weaker evidence than a meta-analysis of multiple studies pointing the same direction. Press releases often highlight a single study as "breakthrough"; always ask: "Is this the only study, or is there broader evidence?"

## Red Flags in Single Studies

### Small Sample Size

- Signals high statistical noise (chance variation)
- RCT with n < 100: interpret results with caution
- n < 50: anecdotal, not definitive

**Example:**
```
❌ "Study of 20 patients shows drug X cures disease" 
   → Too small; high variance; prone to false positive

✅ "Preliminary study of 20 patients shows drug X may help; 
    larger trials underway"
   → Acknowledges evidence level
```

### Single-Center, Single-Ethnicity

- Results may not generalize
- Health, genetics, healthcare systems differ by geography

**Example:**
```
❌ "Swedish study proves drug works"
✅ "Swedish study of 500 patients shows efficacy; results need 
    verification in other populations before generalization"
```

### Subgroup Analysis

- **Major problem**: testing multiple subgroups inflates false positive risk
- A study with 10 subgroups will likely find 1 "significant" result by chance
- Real findings require: (1) pre-specified hypothesis, (2) replication in new data

**Example:**
```
❌ "Drug X shows no overall benefit, but works in women over 60"
   → This may be a chance finding; needs separate confirmation

✅ "Drug X shows no overall benefit. A pre-specified subgroup 
    analysis in women over 60 (n=150) showed 20% benefit; 
    this finding requires replication in new trial"
   → Acknowledges exploratory nature; signals need for confirmation
```

## Statistical Misinterpretation Patterns

### P-value Confusion

**What p-value means:**
- Probability that observed result occurred by chance *if the null hypothesis (no effect) were true*
- p < 0.05 = 5% chance of this result if there is truly no effect
- Does NOT mean "95% probability the drug works"

**Common error:**
```
❌ "P-value 0.03 means the drug has 97% chance of working"
   → WRONG. It means 3% chance of observing this result if drug 
      actually has no effect.

✅ "P-value 0.03 means result is unlikely by chance; 
    however, we don't know the probability the drug works 
    without knowing the prior probability of effect"
   → More accurate; acknowledges Bayesian reasoning
```

### Confidence Interval Misreading

**What 95% CI means:**
- If we repeated the study 100 times, the true effect would fall within this range 95 times
- Wide CI = high uncertainty; narrow CI = more precise estimate

**Common error:**
```
❌ "95% CI 25–43% means the effect is between 25–43%" 
   → Misleading; CI is about long-run sampling behavior, 
      not the specific study's true effect

✅ "95% CI 25–43% means we are 95% confident the true effect 
    is in this range; wide range indicates uncertainty"
   → Better framing
```

## Multiple Comparisons & P-Hacking

### The Problem

- If you test 20 hypotheses, ~1 will be "significant" (p < 0.05) by chance alone
- Mining data for "significant" findings is p-hacking
- Published literature skewed toward positive results (publication bias)

**Example:**
```
❌ "Researchers tested 100 patient characteristics and found 
    5 associated with outcome (p < 0.05)"
   → 5 significant by chance; misleading

✅ "Researchers tested 100 patient characteristics; found 5 
    with p < 0.05, but acknowledged multiple-comparisons 
    correction suggests none truly significant"
   → Honest framing
```

### Pre-Registration & Registered Reports

- **Pre-registration**: Study protocol submitted *before* data analysis
- **Registered Report**: Journal pre-approves hypothesis before results known
- Both reduce p-hacking risk

**Red flags for p-hacking:**
- Post-hoc hypothesis ("We discovered that...")
- Many endpoints tested but only positive ones reported
- Subgroup analyses presented as main findings

## Real-World vs. Trial Populations

### Selection Bias

- RCT enrollees often differ from general population
- Trials enroll healthier, younger, more compliant patients
- Results may not apply to elderly, comorbid, or diverse populations

**Example:**
```
❌ "Study proves drug works in everyone"
✅ "Study enrolled 500 patients aged 50–65 with hypertension; 
    75% were white; results may not generalize to older or 
    more diverse populations"
```

### Lead-Time Bias

- **Especially common in screening news**: earlier detection ≠ better outcomes
- Example: PSA screening finds prostate cancer earlier but doesn't reduce mortality in many men

**Example:**
```
❌ "New cancer screening test enables earlier detection; 
    patient survival improves"
   → Confuses lead time (earlier diagnosis) with better prognosis

✅ "New screening test detects cancer 6 months earlier than 
    standard test; it's unclear whether this earlier detection 
    improves survival outcomes"
```

## Preprint vs. Peer-Reviewed

### Preprint (medRxiv, bioRxiv)

- Posted before peer review
- NOT vetted by journal editors or external reviewers
- May contain errors or overstatement
- Common in fast-moving fields (COVID, monkeypox)

**Journalistic protocol:**
1. Flag explicitly: "study not yet peer-reviewed"
2. Verify methods & basic numbers (sample size, endpoints)
3. Seek expert commentary from independent researcher
4. Ask: "Is this the only study, or part of broader evidence base?"

**Example:**
```
❌ "New preprint shows drug X works"
   → Misleading; no editorial scrutiny

✅ "New preprint (not yet peer-reviewed) describes preliminary 
    results of drug X. A peer-reviewed trial of the same drug 
    (published last month) showed similar results, suggesting 
    possible benefit but requiring larger trials"
```

## Relative vs. Absolute Thinking

### The Core Problem

Both statements describe the same finding:
- "50% reduction in heart attack risk"
- "2 fewer heart attacks per 1000 people per year"

But readers perceive them differently.

### How to Frame

**Step 1**: State absolute baseline
- "In the study population, 4 per 1000 per year had heart attacks"

**Step 2**: State the absolute change
- "Among those taking the drug, 2 per 1000 per year had heart attacks"

**Step 3**: Optionally add relative risk
- "This represents a 50% relative risk reduction"

**Example:**
```
❌ "New drug reduces heart attack risk by 50%"
   → Overstated; reads as major breakthrough

✅ "In the study, the drug reduced heart attacks from 4 to 
    2 per 1000 people per year (a 50% relative reduction). 
    This means doctors would need to treat approximately 500 
    people to prevent one heart attack"
```

## Effect Size & Clinical vs. Statistical Significance

### The Distinction

- **Statistically significant**: p < 0.05 (unlikely by chance)
- **Clinically significant**: meaningful difference in patient outcomes

**Example:**
```
Large study of 100,000 patients: drug reduces blood pressure by 
1 mmHg (p < 0.001, statistically significant). But 1 mmHg is 
not clinically meaningful; patients won't notice or benefit.

❌ "Study shows drug is effective (p < 0.001)"
✅ "Study is statistically significant (p < 0.001) but effect 
    size is very small (1 mmHg); unclear if clinically meaningful"
```

## Replication & Robustness

### Single Study is Never Enough

- Even well-designed RCTs can have:
  - Unexpected interactions
  - Population-specific effects
  - Chance findings that don't replicate

### Questions to Ask

1. **Is this the first study of this treatment?** → High uncertainty
2. **Do independent studies reach similar conclusions?** → More confidence
3. **Is there a meta-analysis?** → Most reliable
4. **What did the researcher's prior work show?** → Pattern or outlier?

**Example:**
```
❌ "Breakthrough: New study shows vitamin D prevents cancer"
   (if first major study showing this)

✅ "New study joins two prior meta-analyses suggesting 
    vitamin D may reduce cancer risk, but magnitude is small 
    and data still limited"
```

## Practical Checklist for Evidence Reading

Before citing a study in a news article:

- [ ] **What is the evidence level?** (RCT, observational, case report, etc.)
- [ ] **What is the sample size?** (n > 1000 is better; n < 50 is weak)
- [ ] **Who is the population?** (age, gender, ethnicity, health status — does it match my story population?)
- [ ] **What is the primary outcome?** (not a secondary or exploratory finding)
- [ ] **Are results pre-specified or exploratory?** (pre-specified is stronger)
- [ ] **Is this the only study, or part of a pattern?** (single study vs. multiple corroborating studies)
- [ ] **What is the effect size?** (relative AND absolute risk)
- [ ] **What is the CI?** (wide = uncertain; narrow = precise)
- [ ] **Who funded the study?** (declare financial conflicts)
- [ ] **Are limitations acknowledged?** (good studies acknowledge what they don't answer)

