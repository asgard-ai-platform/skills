# TPACK Measurement Instruments

TPACK is typically operationalized through three instrument families: self-report surveys, observation rubrics, and performance-based assessments. This file documents concrete instruments, their items, scoring, and known validity threats.

---

## Instrument Family 1 — Self-Report Surveys

### Schmidt et al. (2009) Survey

The most widely cited TPACK survey. Originally developed for pre-service teachers; later adapted for in-service. Uses a 5-point Likert scale (1 = Strongly Disagree → 5 = Strongly Agree).

**Subscale structure and sample items:**

| Subscale | Items (n) | Sample Item |
|----------|-----------|-------------|
| TK | 10 | "I know how to solve my own technical problems." |
| CK | 9 | "I have sufficient knowledge about [subject]." |
| PK | 7 | "I can adapt my teaching style to different learners." |
| PCK | 4 | "I can use a specific strategy to teach a specific concept." |
| TCK | 5 | "I know about technologies that I can use to understand and do [subject]." |
| TPK | 11 | "I can choose technologies that enhance the teaching approaches for a lesson." |
| TPACK | 8 | "I can teach lessons that appropriately combine [subject], technologies, and teaching approaches." |

**Scoring procedure:**

1. Compute subscale mean from raw item scores.
2. Flag any subscale mean ≤ 2.5 as a **critical gap** requiring targeted development.
3. Flag subscale mean 2.6–3.4 as **developing**.
4. Do not aggregate all subscales into a single TPACK score — the seven domains are theoretically distinct; a single composite masks domain-specific weaknesses.

**Known instrument weaknesses:**

- Confirmatory factor analyses have produced mixed fit across populations. The TPK subscale in particular shows cross-loading with TPACK in some studies.
- Self-report inflates scores by 0.4–0.7 points compared to observation-based measures in studies that used both.
- The CK subscale is generic; domain-specific versions (e.g., CK for mathematics vs. CK for history) yield more actionable diagnostics.

---

### Mishra & Koehler Adaptation (TPACK Survey Instrument)

A shorter, 29-item version used in Mishra & Koehler's own research group, focused on in-service K-12 teachers. Similar Likert structure; collapses TK into fewer items by assuming basic technology literacy.

Primary difference from Schmidt: drops redundant TK items and adds context-sensitivity prompts (e.g., "for the subject area you currently teach").

---

### TPACK-Deep Survey (Kabakci Yurdakul et al., 2012)

Designed to measure **depth** of integration, not just presence. Adds a design dimension — whether the teacher can plan TPACK-aligned lessons, not just recognize them.

**Subscales added beyond Schmidt:**

| Subscale | Focus |
|----------|-------|
| Design | Can design instruction that integrates all three knowledge types |
| Explication | Can articulate WHY a technology choice is pedagogically justified |
| Management | Can manage technology-integrated learning environments |

Useful when the diagnostic goal is professional development planning rather than gap identification.

---

## Instrument Family 2 — Observation Rubrics

Self-report is convenient but inflated. Observation rubrics produce more valid scores when classroom access is possible.

### Harris, Mishra & Koehler (2009) Activity Types Rubric

Rather than rating teacher knowledge directly, this rubric codes **lesson activities** against TPACK criteria. Observers code each activity in a lesson plan or recorded lesson.

**Coding dimensions (per activity):**

| Dimension | Rating Scale | Anchor Descriptors |
|-----------|-------------|-------------------|
| Technology presence | 0–2 | 0 = absent; 1 = incidental; 2 = central |
| Pedagogical alignment | 0–3 | 0 = no fit; 1 = substitution only; 2 = enhances strategy; 3 = enables strategy not otherwise possible |
| Content representation accuracy | 0–2 | 0 = misrepresents content; 1 = neutral; 2 = uniquely clarifies content |
| TPACK integration | 0–3 | 0 = TK only; 1 = TPK or TCK; 2 = partial TPACK; 3 = full TPACK |

**TPACK integration score formula (per lesson):**

```
Lesson_TPACK = mean(activity_TPACK_scores) × (1 - gap_penalty)

gap_penalty = max(0, (2 - min(tech_presence, ped_alignment, content_rep)) / 2)
```

The gap_penalty term enforces the IRON LAW: if any single dimension scores very low, the overall TPACK score is penalized even if others are high.

**Worked example:**

A history teacher uses Google Maps to show territorial changes across time periods.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technology presence | 2 | Google Maps is central to the activity |
| Pedagogical alignment | 3 | Spatial visualization enables historical reasoning that a static map cannot |
| Content representation accuracy | 2 | Territorial boundaries are represented accurately and dynamically |
| TPACK integration | 3 | All three knowledge types are genuinely integrated |

```
gap_penalty = max(0, (2 - min(2, 3, 2)) / 2) = max(0, (2-2)/2) = 0
Lesson_TPACK = 3.0 × (1 - 0) = 3.0  → Full TPACK
```

Counter-example: Same teacher uses Google Maps only to show students where a city is located, with no pedagogical elaboration.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technology presence | 2 | Still central |
| Pedagogical alignment | 1 | Substitution — a wall map would work as well |
| Content representation accuracy | 1 | Neutral |
| TPACK integration | 1 | TPK only (tech + pedagogy of "show"), no CK integration |

```
gap_penalty = max(0, (2 - min(2, 1, 1)) / 2) = max(0, 1/2) = 0.5
Lesson_TPACK = 1.0 × (1 - 0.5) = 0.5  → TK without TPACK
```

---

### Low-Inference Classroom Observation Checklist

For large-scale studies where detailed rubric coding is not feasible, a binary checklist is used. Each item is scored 1 (observed) or 0 (not observed). Observers need ~30 minutes of classroom video.

```
TPACK Classroom Observation Checklist (12 items)

TK Indicators
[ ] Teacher demonstrates fluent use of technology without disrupting lesson flow
[ ] Teacher recovers from technical failure without extended off-task time

PK Indicators
[ ] Lesson includes explicit learning objective stated to students
[ ] Teacher uses formative assessment strategy during the lesson

CK Indicators
[ ] Content explanations are accurate (no observable misconceptions)
[ ] Teacher uses discipline-specific vocabulary correctly

TPK Indicators
[ ] Technology use is referenced in verbal instructions ("use this tool to...")
[ ] Teacher selects a different technology for a different pedagogical purpose
  (not same tool for everything)

TCK Indicators
[ ] Technology represents content in a domain-appropriate way
[ ] Teacher highlights a content concept that the technology makes visible

TPACK Indicators
[ ] Teacher explicitly connects technology choice to content learning goal
[ ] Student activity could not be completed as effectively without the technology
```

**Scoring:**

- 0–4: Insufficient technology integration
- 5–8: Partial integration (likely TPK or TCK without full TPACK)
- 9–12: Strong TPACK integration

A score of 9–12 with both TPACK indicator items checked is required to classify a lesson as demonstrating TPACK.

---

## Instrument Family 3 — Performance-Based Assessment

The most valid but most resource-intensive approach. Requires teachers to produce an artifact and justify it.

### Lesson Design Task (LDT)

**Protocol:**

1. Give the teacher a content topic, a learner level, and a technology constraint (e.g., "tablets available, 1:1").
2. Teacher produces a 45-minute lesson plan within 60 minutes.
3. Teacher records a 5-minute verbal justification of their technology choices.
4. Raters score using the rubric below.

**Scoring rubric (4-point scale per dimension):**

| Dimension | 1 | 2 | 3 | 4 |
|-----------|---|---|---|---|
| **TK Application** | Technology is non-functional or misused | Technology works but is incidental | Technology used appropriately | Technology use shows command of its advanced features |
| **Pedagogical Coherence** | No discernible learning strategy | Strategy present but not linked to objectives | Strategy matches objectives | Strategy is optimized for content and learner level |
| **Content Accuracy** | Content errors present | Content is accurate but generic | Content is accurate and grade-appropriate | Content reflects expert understanding of disciplinary concepts |
| **TPACK Integration** | No integration evident | Two domains integrated (e.g., TPK or TCK) | All three domains present but loosely coordinated | Technology choice is explicitly justified by BOTH pedagogical strategy AND content requirements |

**Inter-rater reliability target:** Cohen's κ ≥ 0.70 before using scores for decisions.

**Minimum passing threshold for pre-service certification:** Score of 3 on TPACK Integration dimension AND score of 3+ on all other dimensions.

---

## Choosing an Instrument

| Use Case | Recommended Instrument | Caution |
|----------|------------------------|---------|
| Large-scale survey (100+ teachers) | Schmidt et al. (2009) | Inflate scores; use for relative comparison only |
| Professional development needs analysis | TPACK-Deep (Kabakci Yurdakul) | Longer; may need translation validation |
| Lesson quality audit | Harris et al. Activity Types Rubric | Requires trained observers; inter-rater training ~4 hours |
| Pre-service teacher certification | Lesson Design Task | High validity; not scalable above ~30 teachers per rater |
| Quick classroom walkthrough | Low-Inference Checklist | Low precision; useful for screening only |

---

## Validity Threats Specific to TPACK Measurement

**1. Social desirability bias (self-report)**
Teachers rate themselves higher on technology items because technology competence is professionally valued. Mitigation: use anonymous administration; pair with at least one observation measure.

**2. Technology familiarity confound**
TK scores reflect exposure to specific tools, not transferable technology knowledge. A teacher who has never used a particular platform will score low on TK even if they are a fast learner. Mitigation: use platform-agnostic TK items or note which tools were referenced.

**3. Context specificity (see SKILL.md Gotchas)**
TPACK varies by content domain. A teacher with high TPACK for science simulations may have low TPACK for teaching writing. Instruments that don't specify subject area produce domain-blurred scores. Mitigation: administer surveys separately for each subject area taught, or use domain-specific CK/TCK subscales.

**4. Survey construct drift over time**
The Schmidt instrument was normed on early-2000s technology contexts. Items referencing "software" and "hardware" are less discriminating in a cloud/mobile era. If using Schmidt, pre-test items for clarity with your population and drop non-discriminating items before deployment.

**5. PCK floor effect**
Teachers with genuinely weak PCK score low on TPACK for the wrong reason — not technology weakness, but content-pedagogy weakness. Running PCK-only diagnostics first helps separate the two problems before prescribing technology-focused professional development.

---

## Quick Reference: TPACK Self-Assessment (7 Items)

For rapid individual reflection (not for research), one item per domain:

```
Rate each 1–5 (1 = not at all confident → 5 = very confident)

TK:    I can troubleshoot technology problems I encounter in my teaching.         ___
PK:    I can select teaching strategies appropriate for different learning goals.  ___
CK:    I have deep knowledge of the content I teach.                              ___
TPK:   I can choose technologies that fit my pedagogical strategies.              ___
TCK:   I know which technologies best represent the concepts in my subject.       ___
PCK:   I can explain difficult content concepts using multiple representations.   ___
TPACK: I can design lessons where technology, content, and pedagogy reinforce
       each other.                                                                ___
```

**Interpretation:**
- Any domain score ≤ 2: critical development need before attempting TPACK design
- TPACK score ≤ PK score AND ≤ CK score but TK score ≥ 4: classic "technology for technology's sake" risk profile
- PCK score < TPACK score: likely self-report inflation on TPACK item; PCK is the prerequisite
