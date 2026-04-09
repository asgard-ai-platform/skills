# CRAAP Test — Source Evaluation Checklist

The CRAAP test is a structured checklist developed by librarians at California State University, Chico (2004) to evaluate source quality. It operationalizes the Four Tests from the parent skill into five scored dimensions, making credibility assessment explicit and auditable.

**When to use CRAAP over the Four Tests framework**: CRAAP is better for academic research contexts where you need a documented, repeatable evaluation across multiple sources. The Four Tests framework is better for rapid triage of a single claim or social media post.

---

## The Five Dimensions

### C — Currency (時效性)

Is the information recent enough for the purpose?

| Topic Type | Acceptable Age |
|------------|---------------|
| Scientific consensus (e.g., climate data) | Up to 5 years for fundamentals; 1 year for latest findings |
| Technology (AI, software, hardware) | 6 months maximum |
| Law and regulation | Check if still in force; amendments may supersede |
| Economic data (GDP, inflation, rates) | Quarterly or annual; specify the reference quarter |
| Historical events (pre-1950) | Age of source is less important than accuracy |
| Medical / clinical guidelines | Follow issuing body's own review cycle (often 2-5 years) |

**Questions to ask:**
- When was the information published or last updated?
- Has the underlying situation changed since publication?
- Are the links and references still active?

**Scoring trap**: A 2015 source on "how to use Docker" is outdated. A 2015 source on "the causes of World War I" is not.

---

### R — Relevance (相關性)

Does the source address your actual question?

**Questions to ask:**
- Does the content match your research question, not just your keywords?
- Is the intended audience appropriate? (peer-reviewed ≠ always right for a practitioner context; popular press ≠ always wrong)
- Is the scope the right level of depth? An encyclopedia entry can answer "what is X"; it cannot answer "what are the second-order effects of X under condition Y"

**Common relevance failure modes:**

| Failure | Example |
|---------|---------|
| Topic drift | Searching "Taiwan semiconductor exports" and citing a general article on "Asia-Pacific trade" |
| Level mismatch | Using a meta-analysis to support a single-case claim |
| Audience mismatch | Citing a medical textbook chapter to support a consumer health claim where terminology diverges |
| Keyword hit without conceptual match | An article mentions "productivity" in passing; you cite it as evidence about productivity |

---

### A — Authority (權威性)

Who created this, and are they qualified?

**Hierarchy of authority signals** (strongest to weakest):

1. **Institutional affiliation + peer review**: Author employed by research institution, article published in peer-reviewed journal with named reviewers
2. **Professional credentials + domain match**: MD writing about cardiology, CPA writing about tax law
3. **Institutional affiliation alone**: Government agency, university, established NGO — credible but unreviewed
4. **Journalistic outlet with editorial standards**: Reputable newspapers with named bylines and editor oversight
5. **Named individual with verifiable track record**: Public intellectual with documented expertise; blog with cited evidence
6. **Anonymous or pseudonymous**: Requires extraordinary corroboration from higher tiers

**Domain specificity rule** (reinforces parent SKILL.md Gotcha #5):

```
Authority is NOT transferable across domains.

Credible on:                    NOT credible on:
Cardiologist                    → nutrition policy
Nobel laureate in physics       → epidemiology
Successful entrepreneur         → macroeconomics
Celebrity                       → anything scientific
```

**Red flag patterns for false authority:**
- Credential without domain match ("PhD in literature endorses supplement")
- Credential that cannot be verified (no institutional affiliation listed)
- "Expert" whose only public profile is promoting this specific claim
- Organization name sounds official but has no verifiable membership or governance (e.g., "Global Health Institute" with a single-page website and no staff list)

---

### A — Accuracy (準確性)

Is the information correct and verifiable?

This maps most directly to **Internal Criticism** in the parent skill's Four Tests framework.

**Verification checklist:**

- [ ] Are claims supported by cited evidence? (not "studies show" — which studies, where?)
- [ ] Can the cited sources be found and do they say what the author claims?
- [ ] Is the data presented with appropriate precision? (not "90% of people" without sample size and method)
- [ ] Are statistics presented with context? (relative risk vs. absolute risk; per-capita vs. total)
- [ ] Does the logic hold? Are conclusions proportionate to the evidence?
- [ ] Has the information been reviewed or corroborated by others?

**Statistical accuracy traps:**

| Trap | Misleading version | Accurate version |
|------|--------------------|-----------------|
| Relative vs. absolute risk | "Drug reduces heart attack risk by 50%" | "Risk drops from 2% to 1% (absolute: 1 percentage point)" |
| Base rate omission | "80% of cases involve X" | "80% of cases involve X, but X is present in 75% of all people" |
| Cherry-picked timeframe | GDP growth shown from 2020 trough | GDP growth shown from pre-pandemic baseline |
| Correlation stated as causation | "Cities with more Starbucks have higher income" | Association; income predicts both |
| Sample size hidden | "Survey shows 73% support..." | n=47 self-selected online respondents |

---

### P — Purpose (目的)

Why does this source exist?

**Source purpose taxonomy:**

| Purpose | Examples | Credibility implication |
|---------|----------|------------------------|
| Inform | Academic journal, government statistics, encyclopedias | High — designed to transmit knowledge accurately |
| Educate | Textbooks, university course materials | High — but may simplify; check edition currency |
| Persuade | Op-ed, advocacy report, think-tank white paper | Medium — data may be accurate; framing is selective |
| Sell | Brand white paper, sponsored content, press release | Low for claims about own product; primary source for official statements |
| Entertain | Satire, tabloid, clickbait | Near-zero — but useful as primary source on public discourse |
| Deceive | Disinformation campaigns, astroturfing | None — treat as adversarial |

**Detecting purpose when it's not disclosed:**

1. **Follow the money**: Who funds the publication or organization? Industry-funded research on industry-related topics warrants higher scrutiny (not automatic disqualification).
2. **Check the domain/about page**: Does the "About" page describe a mission, a funder, a parent organization?
3. **Read the language register**: Emotional language, superlatives, calls to action → persuasive or entertainment purpose
4. **Look for missing counterarguments**: A balanced informational source acknowledges competing evidence; a persuasive source does not

---

## Scoring the CRAAP Test

A numerical scoring approach is optional but useful when comparing multiple sources or when you need a documented audit trail.

### Scoring rubric (per dimension)

| Score | Label | Criteria |
|-------|-------|---------|
| 3 | Strong | Dimension fully satisfied; no significant concerns |
| 2 | Acceptable | Minor concerns; source is usable with caveats |
| 1 | Weak | Significant concerns; use only if no alternatives |
| 0 | Fail | Dimension fails; source is not credible on this dimension |

### Aggregate interpretation

| Total (out of 15) | Verdict |
|-------------------|---------|
| 13–15 | High credibility — cite with confidence |
| 10–12 | Moderate credibility — cite with noted limitations |
| 7–9 | Low credibility — verify against stronger sources before use |
| 0–6 | Discard — do not cite; flag as potential misinformation |

**Important**: A score of 0 on **Authority** or **Accuracy** is disqualifying regardless of total. A source with fabricated credentials or demonstrably false claims should not be used even if it scores well on other dimensions.

---

## Worked Example

**Source**: A report titled "Taiwan's Net Zero Transition: Risks and Opportunities" published on a website called `greeneconomy-asia.org`, dated March 2024, authored by "Dr. James Lin, Senior Fellow."

### Evaluation

**C — Currency: 3/3**
Published March 2024. Net-zero policy is a fast-moving topic; this is within the 1-year acceptable window. Check if any major policy changes have occurred since (e.g., revised 2050 targets).

**R — Relevance: 3/3**
Directly addresses Taiwan's net-zero transition. Scope (risks + opportunities) matches a research question about policy implications. Depth appears substantive (42 pages, executive summary, appendices).

**A — Authority: 1/3**
"Senior Fellow" at `greeneconomy-asia.org`. Problems:
- "Dr." James Lin — no PhD field listed, no university affiliation
- `greeneconomy-asia.org` — no "About" page with governance, no board listed, domain registered 2022
- No prior publications by this author found in Google Scholar
→ Authority cannot be verified. Treat as anonymous.

**A — Accuracy: 2/3**
Report cites MOEA and IEA data. Spot-check: the IEA citation (IEA World Energy Outlook 2023, p. 142) is accurate and does say what the report claims. However, one chart shows "projected renewable capacity" without citing the underlying model or assumptions. Accuracy is partially verifiable.

**P — Purpose: 1/3**
Site has no disclosed funder. The report concludes with a section recommending specific policy consultancy services offered by a linked firm. Likely purpose: generate leads for consultancy. Framing of risks is selective — only regulatory risks are discussed, not energy security risks. Persuasive/commercial purpose.

### Scorecard

| Dimension | Score | Note |
|-----------|-------|------|
| Currency | 3 | Recent enough |
| Relevance | 3 | On-topic and substantive |
| Authority | 1 | Unverifiable credentials, opaque organization |
| Accuracy | 2 | Partially verifiable; one uncited model |
| Purpose | 1 | Commercial interest undisclosed |
| **Total** | **10/15** | |

**Verdict**: Moderate credibility (10/15). Usable only for the specific data points that trace back to verifiable primary sources (MOEA, IEA). Do not rely on the report's own analysis or recommendations without corroboration from sources with verifiable authority. Flag the commercial purpose when citing.

---

## CRAAP vs. Four Tests: When to Use Which

| Situation | Use |
|-----------|-----|
| Rapid triage of a single claim or post | Four Tests (faster) |
| Academic research: selecting among 5+ sources | CRAAP (scored, comparable) |
| Documenting source evaluation for a deliverable | CRAAP (auditable) |
| Detecting misinformation in a viral claim | Four Tests + Red Flags table |
| Teaching source evaluation | CRAAP (structured rubric is easier to teach) |

The two frameworks are compatible: CRAAP's five dimensions map onto the Four Tests as follows:

| CRAAP | Four Tests equivalent |
|-------|----------------------|
| Currency | Currency (identical) |
| Relevance | (no direct equivalent — CRAAP-specific) |
| Authority | External Criticism (partial) + Internal Criticism (expertise) |
| Accuracy | Internal Criticism |
| Purpose | Internal Criticism (bias) + External Criticism (authenticity) |

---

## Limitations of the CRAAP Test

- **Scores can be gamed**: A well-funded disinformation campaign can produce sources that score 14/15. CRAAP is a heuristic, not a proof.
- **Relevance is subjective**: Two researchers may score relevance differently for the same source depending on their research question.
- **Doesn't handle AI-generated content well**: AI content can appear to satisfy Currency, Relevance, Authority (with a plausible byline), and Accuracy superficially. Apply the parent skill's AI-generated content Gotcha: verify that cited sources actually exist before counting Accuracy as satisfied.
- **Not calibrated for all domains**: The scoring thresholds above are general. Legal, medical, and financial research may require higher minimum scores on Authority and Accuracy specifically.
