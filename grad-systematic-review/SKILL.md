---
name: "grad-systematic-review"
description: "Conduct a systematic literature review following the PRISMA framework with explicit search strategy, inclusion and exclusion criteria, quality assessment, and transparent synthesis. Use this skill when the user needs to design a reproducible literature search, apply PRISMA flow documentation, develop inclusion and exclusion criteria, assess study quality, or when they ask 'how do I do a systematic review', 'what is PRISMA', or 'how do I make my literature review reproducible'."
metadata:
  category: "WP-32 質性方法"
  tags: ["systematic-review", "PRISMA", "search-strategy", "inclusion-exclusion", "quality-assessment", "meta-synthesis", "evidence-synthesis", "reproducibility"]
---

# Systematic Literature Review (PRISMA)

## Overview

A systematic review uses explicit, pre-defined methods to identify, select, appraise, and synthesize all relevant research on a specific question. Unlike narrative reviews, systematic reviews follow a reproducible protocol that minimizes bias in study selection and interpretation. The PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) framework provides the standard reporting structure, including the iconic flow diagram tracking records through identification, screening, eligibility, and inclusion.

## When to Use

- Synthesizing the totality of evidence on a well-defined research question
- Identifying gaps, contradictions, or consensus in a body of literature
- Establishing what is known before designing new empirical research
- Informing policy or practice guidelines with evidence-based synthesis

## When NOT to Use

- When the research question is too broad to define clear inclusion criteria
- When a scoping review (mapping the landscape) is more appropriate than a systematic review (answering a specific question)
- When time constraints prevent the rigorous protocol required
- When there is very little published research on the topic (consider a scoping review first)

## Assumptions

```
IRON LAW: A systematic review must be REPRODUCIBLE — every search
decision, inclusion criterion, and quality assessment must be documented
so another researcher can replicate the process. If your review cannot
be replicated, it is a narrative review, NOT a systematic review.
```

Key assumptions:
1. Transparency and reproducibility distinguish systematic from narrative reviews
2. A pre-registered protocol reduces bias in study selection and analysis
3. At least two independent reviewers should screen and assess studies to reduce subjective bias
4. Quality assessment of included studies is mandatory — not all evidence is equal

## Methodology

### Step 1: Define the Research Question and Protocol

Formulate a focused question using a framework (PICO for interventions, PEO for qualitative, SPIDER for mixed methods). Register the protocol (e.g., PROSPERO). Define databases, search terms, date ranges, and language restrictions.

| Framework | Components |
|-----------|-----------|
| **PICO** | Population, Intervention, Comparison, Outcome |
| **PEO** | Population, Exposure, Outcome |
| **SPIDER** | Sample, Phenomenon of Interest, Design, Evaluation, Research type |

### Step 2: Execute the Search Strategy

Search at least 3 databases (e.g., Scopus, Web of Science, PubMed). Use Boolean operators (AND, OR, NOT) with controlled vocabulary and free-text terms. Document every search string and date. Supplement with citation chaining (forward and backward), grey literature, and hand-searching key journals.

### Step 3: Screen and Select Studies

Apply inclusion/exclusion criteria in two phases:
1. **Title and abstract screening** — two reviewers independently; resolve disagreements by discussion or third reviewer
2. **Full-text screening** — apply criteria to full papers; record reasons for exclusion

Document the process in a PRISMA flow diagram:
- Records identified → duplicates removed → screened → eligible → included

### Step 4: Extract Data, Assess Quality, and Synthesize

Extract data into a standardized form. Assess quality using appropriate tools (e.g., Cochrane RoB for RCTs, CASP for qualitative, JBI checklists). Synthesize via meta-analysis (quantitative), thematic synthesis (qualitative), or narrative synthesis. Report per PRISMA 2020 checklist.

## Output Format

```markdown
## Systematic Review: [Research Question]

### Protocol
- Question framework: [PICO/PEO/SPIDER]
- Registration: [PROSPERO ID or equivalent]
- Databases searched: [list]
- Date range: [start-end]

### Search Strategy
| Database | Search String | Records Found |
|----------|--------------|---------------|
| [name] | [Boolean query] | [N] |

### PRISMA Flow
- Identified: [N] records
- Duplicates removed: [N]
- Screened (title/abstract): [N]
- Excluded at screening: [N]
- Full-text assessed: [N]
- Excluded at full-text: [N] (reasons: ...)
- Included in synthesis: [N]

### Inclusion/Exclusion Criteria
| Criterion | Include | Exclude |
|-----------|---------|---------|
| Population | [specification] | [specification] |
| Study type | [specification] | [specification] |
| Language | [specification] | [specification] |
| Date | [specification] | [specification] |

### Quality Assessment Summary
| Study | Tool Used | Overall Rating | Key Concerns |
|-------|-----------|---------------|--------------|
| [author, year] | [RoB/CASP/JBI] | [high/moderate/low] | [specific issues] |

### Synthesis
- [Key finding 1 with evidence strength]
- [Key finding 2 with evidence strength]
- Gaps identified: [what remains unknown]

### Limitations
- [Search limitations]
- [Assessment limitations]
```

## Gotchas

- A systematic review without a PRISMA flow diagram is incomplete — the flow diagram is not optional
- Pre-registering the protocol prevents post-hoc changes to inclusion criteria that introduce bias
- Grey literature (theses, conference papers, reports) must be considered to reduce publication bias
- Quality assessment is NOT pass/fail — it informs how much weight to give each study in the synthesis
- Do NOT conflate systematic review with meta-analysis; meta-analysis (statistical pooling) is one possible synthesis method within a systematic review
- Inter-rater reliability for screening and quality assessment should be reported (e.g., Cohen's kappa)

## References

- Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71.
- Higgins, J. P. T., et al. (Eds.). (2023). *Cochrane Handbook for Systematic Reviews of Interventions* (Version 6.4). Cochrane.
- Booth, A., Sutton, A., & Papaioannou, D. (2016). *Systematic Approaches to a Successful Literature Review* (2nd ed.). Sage.
