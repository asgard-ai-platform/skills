---
name: "med-health"
description: "Use when writing a medical or health news story — clinical research breakthroughs, public health alerts, drug approvals, epidemiology, health policy, patient stories, risk communication — from research papers, press releases, health authority statements, or interviews. Specializes the med-news-reporter workflow for health-beat discipline: relative risk framing, absolute baseline inclusion, evidence-hierarchy verification, deidentification protocol, and WHO suicide-reporting compliance. Triggers on phrases like '寫一篇醫學新研究', 'draft a health news piece', '整理流行病新聞', '幫我把這份臨床試驗結果寫成新聞', '健康新聞報導', 'write up this drug approval', 'health story from this study'. Do NOT use for medical advice (→ consult healthcare provider), pharmaceutical marketing (→ mkt-pharma), hospital PR/press release in house voice (→ pr-press-release)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "health-news", "medical-journalism", "public-health", "epidemiology", "media-ethics"]
---

# Medical & Health News Reporting

> **This skill specializes med-news-reporter for the medical/health beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **health-specific discipline** on top.

## Overview

Distilled from health-journalism curricula at Stanford Medicine+Muse, Johns Hopkins SFDH, AHCJ (Association of Health Care Journalists), Columbia Mailman, NTU Public Health, and Taiwan health-media ethics standards. Covers five sub-types: **research breakthroughs / public-health alerts / drug approval / health policy / patient stories**. Core challenge: translating statistical evidence for public understanding without misrepresenting risk or false certainty.

```
IRON LAW: Relative Risk Without Absolute Risk Is Misleading

Every medical claim in the form "X% increase/decrease in risk" MUST cite
absolute baseline numbers: baseline incidence, NNT (Number Needed to Treat),
absolute risk reduction, or absolute risk change. "50% reduction in risk of
heart attack" is meaningless without "from 4 in 1000 to 2 in 1000 per year".
LLM default: lead with the relative risk (sounds dramatic), omit baseline.
Readers then overestimate the clinical significance. Override that default
by naming the denominator first, then the percentage.
```

Why this is non-obvious: "50% reduction" *sounds* much more impactful than "2 fewer heart attacks per 1000 per year", yet both describe the same result. Research-to-media translation routinely inverts this — the press release says "50% reduction", the outlet runs that number, and readers assume a larger clinical effect than evidence supports. This is the single most common source of health-news overclaim.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "'50% reduction' is the research result, I'll just quote it" | Quoting a relative-risk figure *without* the absolute baseline is relaying an incomplete fact. The journal paper has the baseline; the press release usually does not. Cite both or cite neither + flag. |
| "The baseline is in the methods section, readers can look it up" | Readers will not. The article is the only context they read. Omitting it is misleading by omission, not just incomplete. |
| "Adding the absolute number makes the story less dramatic" | That is the *point*. Accuracy is not a bug. If the absolute effect is small, the reader deserves to know. |
| "NNT is too technical for general audiences" | True, and it's also the clearest way to show clinical significance. Use NNT in a side sentence ('meaning doctors would need to treat about 500 people to prevent one case'). Not optional. |
| "The researcher said 'statistically significant'—that's the main story" | Statistically significant ≠ clinically significant. A study of 100,000 people can show a 0.5% effect as "significant" if it's real. Report both p-value and effect size. |

---

## When to Use

**Trigger conditions:**
- User supplies health/medical material — journal abstracts, clinical trial results, drug approval announcements, public health advisories, epidemiological data, health-policy statements, patient interviews — and asks for a news piece.
- User asks for "醫學新聞", "健康新聞", "health story", "research reporting", "drug news", "epidemic coverage", "health policy piece", "clinical breakthrough".
- User paraphrases: "寫一篇醫學新研究", "整理流行病新聞", "幫我把這份臨床試驗結果寫成新聞", "turn this NIH press release into a story", "draft a piece on this WHO alert".

**Input signals:**
- Named disease, drug, treatment, researcher, institution, study name, clinical trial identifier, or epidemiological data.
- Direct quotes from clinicians, researchers, health authorities (CDC, 衛福部, WHO, etc.).
- Statistical claims (relative risk, incidence, prevalence, mortality, efficacy, confidence intervals).
- Regulatory status (FDA approval, 食藥署 listing, Phase III trial completion).

**When NOT to use:**
- "What do I have?" / personal medical symptom advice → direct user to healthcare provider, not journalism skill.
- Pharmaceutical company press release in the company's own voice → use `pr-press-release`.
- Hospital marketing / institutional PR ("Our Advanced Surgery Center Achieves...") → use `pr-*`.
- Promotion of unproven remedy or supplement as scientific fact → refuse; suggest user consult source integrity first.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds health-specific Step 7 (Evidence Hierarchy & Risk Framing Audit).

### Step 1: Classify the health-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Research breakthrough** | Journal paper, pre-print, press release from university/NIH | Evidence level check; RR + AR framing; replication status |
| **Public health alert** | CDC alert, 衛福部 advisory, WHO statement, disease outbreak | Absolute numbers (cases, deaths); transmission risk; at-risk population; response guidance |
| **Drug approval** | FDA/食藥署 approval, Phase III completion, clinical trial results | Trial design rigor; efficacy + side-effect rate; NNT; cost/access; alternative treatments |
| **Health policy** | Coverage decision, vaccine recommendation, screening guideline, regulation | Policy rationale; affected population; evidence basis; expert consensus; dissenting opinion |
| **Patient story** | Interview, testimonial, case narrative | De-identification protocol; generalizability limits; attribution; expert context |

If material spans sub-types (e.g. a policy change triggered by a study), classify by the *primary news driver*.

### Step 2: Source vetting & evidence-hierarchy tagging

Every health claim must carry **evidence-level tag** at first mention:

```
Evidence Hierarchy (strongest → weakest):
1. Meta-analysis / systematic review of RCTs
2. Large RCT (n > 500)
3. Small RCT (n < 500)
4. Cohort study / case-control study
5. Case series / case report
6. Expert opinion / editorials
7. Anecdote / single patient story
```

**Bad tagging:** 「新研究表示...」(which study? what strength?)
**Good tagging:** 「今年發表在 Lancet 的一項 1,200 人隨機對照試驗表示...」or 「基於個案報告（證據等級 5）...但尚未進行人體試驗」

**Source tier (extends med-news-reporter):**

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Government health authority** | CDC, 衛福部、疾管署、食藥署、WHO | Direct citation; highest credibility tier |
| **Peer-reviewed journal** | Lancet, JAMA, BMJ, Nature Medicine, 台灣醫學會期刊 | Always cite journal name + DOI; include publication date |
| **Preprint / not yet peer-reviewed** | medRxiv, bioRxiv | **Must flag as "not yet peer-reviewed"**; requires editor review before publication |
| **University press release** | Without access to actual paper | Treat as Tier 2.5; verify against journal preprint / abstract |
| **Single researcher quote** | Without published evidence | Tier 4; acceptable only as "expert opinion" with explicit caveat |
| **Pharmaceutical company** | Clinical trial sponsor | Tier 3–4; **always disclose funding source**; cross-verify against independent data when possible |
| **Patient anecdote** | Interview, testimonial, Facebook post | Tier 7; only acceptable as illustrative narrative, never as evidence |

### Step 3: Health-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **個人資料保護法 (PDPA) + 醫療法 §72 (Patient Privacy)**:
   - Patient case reports must be de-identified: age range (not exact), no named institution/hospital, no unique medical conditions that allow re-identification.
   - Example: ❌ "63-year-old Mr. Chen A treated at NTU Hospital on March 15 for liver cancer with rare genetic mutation" (re-identifiable)
   - Example: ✅ "A 60–65-year-old male with common cancer type" (anonymized)

2. **WHO Suicide Reporting Guidelines** (essential, non-negotiable):
   - **Do NOT name the method, location, or date** of death.
   - **Do NOT publish a suicide note or detailed narrative.**
   - **ALWAYS include helpline number(s)** (1925, 安心专线, international).
   - **Do use framing**: "died by suicide" or "suicide" (not "committed suicide", "successful attempt").
   - Breaking this rule increases copycat risk (Werther Effect documented by WHO); this is a professional liability.

3. **醫療廣告法 (Medical Advertising Law)**:
   - If a source has financial interest in the product (pharma company, researcher with stock, hospital with proprietary treatment), disclose it.
   - Do not amplify unproven claims (e.g., supplement "cure" claims without RCT evidence).

4. **藥物名稱使用合理性**:
   - Generic name preferred over brand name ("ibuprofen" not "Advil") unless brand is essential to the story.
   - New drugs: include both generic + brand on first mention; thereafter use generic.

5. **傳染病防治法 (Communicable Disease Control Act)**:
   - Early epidemic numbers are often revised as data accumulates. State explicitly: "as of [date], [source] reports X cases".
   - Avoid implied causation ("after the vaccine" ≠ "caused by the vaccine"); use temporal language precisely.

### Step 4: Evidence Hierarchy & Risk Framing Audit (health-specific addition)

Before output, apply:

1. **Evidence Strength Audit**: for each medical claim, verify it cites the evidence level. Single case reports must not be presented as "research shows".
2. **Relative → Absolute Conversion**: every claim of "X% increase/decrease" must be paired with absolute baseline (see Iron Law above).
3. **NNT / ARR / Baseline Incidence**: include at least one of these metrics to ground clinical significance.
4. **Replication Status**: if this is a single study, state so ("first evidence" / "needs confirmation" / "confirms earlier findings").
5. **Confidence Interval / Uncertainty**: include the range, not just the point estimate. "30% to 40%" not just "35%".
6. **Funding Disclosure**: if any source has financial stake in the result, disclose it early ("funded by Pharma Corp X").

---

## Output Format

Use the med-news-reporter base format, with health-specific additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 醫學研究報導 / 公衛警訊 / 藥品核准 / 健康政策 / 患者故事
**字數**: approx. XXX
**消息來源層級**: 政府公衛機構 N / 同儕評審期刊 N / 預印本 N / 企業新聞稿 N / 專家意見 N / 患者訪談 N
**醫學證據稽核**:
- 每項醫學宣稱之證據等級: ✅ / ⚠️ (列出未標的)
- 相對風險 + 絕對風險配對: ✅ / ⚠️ (列出缺項: RR 未伴絕對值、NNT、基礎風險)
- 單一研究 vs 系統性評論: ✅ / N/A / ⚠️
- 95% CI / 不確定性表述: ✅ / ⚠️ (列出未含的宣稱)
**患者隱私檢核**:
- 去識別化: ✅ / ⚠️ (列出仍可追蹤身份的資訊)
- 同意書揭露: ✅ / N/A / ⚠️
**WHO 自殺守則**:
- 適用: N/A / ✅ (已遵守) / ❌ (違反項目)
**利益衝突揭露**:
- 資金來源: ✅ / N/A / ⚠️ (列出未揭露的利益相關)
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

See `examples/` directory for:
- `sample_input.md` — realistic health-news source material (clinical study press release + health authority statement + medical society response + patient anecdote)
- `sample_output.md` — produced piece + meta footer + skill-trace explanation

---

## Gotchas

- **WHO 自殺報導守則不可選擇遵守**: 不報導方法、地點、遺書;必附求助專線(1925);違反導致 copycat 效應(Werther Effect)之文件風險。這是法律 + 倫理 + 公衛的三重義務,不是新聞美學選擇。
- **絕對風險不伴相對風險才是報導失敗**: 「某藥物將 X 病死亡風險降低 50%」若不說明基礎風險(例如 1000 人中 4 人 → 2 人),讀者高估臨床意義。必須兩項並列,或都不列。
- **預印本 (preprint) 是非同儕評審版本**: medRxiv / bioRxiv 的論文尚未經 peer review,在描述時必須明確標註「未經同儕評審」。發稿前應檢驗是否已正式發表在期刊。
- **單一研究 ≠ 醫學共識**: 即使 Lancet 刊登,一篇論文不足以宣稱「科學證明」。需meta-analysis / 多中心驗證或醫學會聲明。LLM 傾向誇大單一研究的通用性。
- **NNT 的臨床意義直覺優於百分比**: 「需治療 500 人才有 1 人受益」 vs 「療效提升 0.2%」——同一結果,直觀度差異極大。優先用 NNT;若無法計算則注明。
- **製藥/醫療機構資助須在引述時點明**: 研究由廠商贊助、醫師兼任產業顧問、醫院銷售新技術——這些利益衝突不揭露等同隱瞞。放在第一次引述該來源時,不要藏在尾註。
- **患者故事去識別化不等於「模糊化」**: 「一名 60 歲男性患者 A」≠ 「患者 X 是成功病例」;前者遵守個資法 §72,後者若細節足夠仍可追蹤(就醫時間+地點+罕見疾病組合)。審核時逐項檢驗。
- **疫情数据更新快,引用需註明日期**: 「確診人數 X」不標明「截至 4 月 29 日」會在重新整理後過時或誤導。時間戳必要。
- **「治癒率」/ 「完治」/ 「成功率」各有定義**: 無定冠詞引用會混淆:是 5 年存活率?完全緩解?部分緩解?必須明確定義或引用原始文件。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 台灣衛生醫療消息來源、機構、官方資料庫 | Step 2 source vetting |
| `references/glossary.md` | 醫學統計、流行病學、臨床試驗術語對照 | When unfamiliar medical terminology appears |
| `references/ethics_and_law.md` | PDPA / 醫療法 §72 / 醫療廣告法 / 自殺守則 | Step 3 risk check |
| `references/medical_evidence_reading.md` | 證據等級金字塔、相對風險誤導、P-hacking | Step 1/4 evidence hierarchy |
| `references/risk_communication.md` | 風險溝通原則、絕對 vs 相對、不確定性表述 | Step 4 risk framing |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-political` — health policy & regulatory news
- `stat-hypothesis-testing` — deeper statistical literacy on RCTs and meta-analyses
- `stat-causal-inference` — for causation claims in observational studies
- `hum-source-criticism` — source vetting frameworks

---

## Limitations

- **Does not verify against live clinical trial databases or medical journals.** This skill flags claims that need verification; it does not query ClinicalTrials.gov, PubMed, or Cochrane. Editor/user must verify or supply.
- **Jurisdictional scope**: legal references (PDPA, 醫療法, 醫療廣告法) reflect Taiwan law. For US (HIPAA), EU (GDPR), UK, HK, or PRC contexts, principles still apply but substitution required.
- **WHO Suicide Reporting Guidelines apply globally**, but enforcement and consequence differ by jurisdiction. Always apply these guidelines regardless of country of publication.
- **Statistical literacy**: judges poll quality, p-hacking risk, effect-size interpretation — *partially* covered in `references/medical_evidence_reading.md`, but for deep methodological critique use `stat-hypothesis-testing` or `grad-survey-design`.
- **Not a substitute for legal review.** Health-news pieces with named patients, drug/treatment criticism, or regulatory disputes should have attorney review before publication.
- **Does not generate original reporting.** If supplied material is insufficient or contradictory, this skill flags gaps — it will not source additional interviews or find additional studies.
