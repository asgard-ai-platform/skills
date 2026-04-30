---
name: "med-education"
description: "Use when the user wants to write an education news piece — school policy, research findings, student achievement data, teacher issues, curriculum reform, or campus events — from supplied material (transcripts, press releases, research papers, data, policy documents, interviews). Specializes the parent med-news-reporter skill for the education beat with research-methodology discipline, demographic verification, effect-size auditing, and education-law red lines. Triggers on phrases like 'write up this education story', 'turn this research into a news piece', '整理校園事件成新聞', '寫一篇教育政策新聞', '幫我把這份 108 課綱新聞寫好', 'draft an education research story', '解讀這份 PISA 排名報導'. Do NOT use for press releases (use pr-press-release), school marketing (use mkt-*), or teacher-training content (use tech-teaching or ecom-*)"
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "education-news", "research-methodology", "media-ethics"]
---

# Education News Reporting

> **This skill specializes med-news-reporter for the education beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **education-beat-specific discipline** on top: research evidence auditing, demographic integrity, effect-size verification, and education-law red lines (兒少法, teacher privacy, curriculum interpretation).

## Overview

Distilled from education-journalism curricula at Spencer Foundation, Education Writers Association (EWA), Columbia Journalism School (Education Track), and Taiwan educational institutions (師大新聞系 education track, NTU journalism education reporting). Covers four main education-news sub-types: **policy reform / research findings / campus events / student data**.

```
IRON LAW: Effect Size + Population, Not Just "Research Shows"

Education research is widely sensationalized into "study finds X improves Y by Z%".
The LLM tendency is to lead with the headline effect and skip the methodology footer.
Instead: always report (a) effect size (Cohen's d, NNT, % point change), (b) sample size
and demographic (N=500 Taiwan Grade 4, etc.), (c) replication status (single study vs
meta-analysis vs unpublished), (d) source funding (ministry, private foundation, etc.).

This is not optional. A study with d=0.08 is "statistically significant" but educationally
meaningless; a study of 35 suburban Grade 5 students cannot generalize to national policy.
Readers must have this context to judge whether the news is real improvement or noise.

Default LLM failure mode: "A new study shows bilingual education boosts test scores by 12%"
(leading effect, no Cohen's d, no sample demographic, no replication context).

Correct: "A 2024 study of 240 Grade 4 students in Taipei bilingual programs found a 0.6
standard-deviation improvement in reading (Cohen's d=0.6), sustained in a follow-up cohort
but not replicated in rural schools. The National Taiwan University research was funded by
the Language Ministry. Previous international meta-analyses show effect sizes ranging d=0.2
to d=0.5 depending on classroom intensity."
```

Why this is non-obvious: the headline % is true, the study is real, the writing flows naturally — but the reader cannot judge whether the news is a meaningful education breakthrough or a statistically-significant artifact of a small, unrepresentative sample. This is how education policy gets made on bad evidence.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "The abstract says 'significant improvement', that's enough" | Significance ≠ effect size. A p < 0.05 with N=1,200 and d=0.08 is real but educationally trivial. Always convert to effect size or NNT. |
| "Adding methodology details makes the story less punchy" | Punchy ≠ misleading. A "punchy" headline with no effect-size footer is how bad education policy gets funded. The footer is the story. |
| "It's a meta-analysis, so the effect is robust" | Meta-analyses vary wildly (d=0.1 to d=0.6). Always report the range and heterogeneity, not just the aggregate mean. |
| "The paper is from Stanford/MIT, it must be credible" | Source prestige is not methodology. Stanford studies of n=42 still need effect-size footnotes. Cross-check the paper's own limitations section. |
| "The policy maker said it works, so it's fine" | Policy makers have incentive to overstate. Cite the independent evaluation's effect size, not the policy maker's claim. |
| "Single school case studies are human-interest, not policy claims" | Correct. Mark them as anecdote ("one teacher's experience") not systemic trend. "One school tried X and saw better writing" ≠ "X improves writing" |

---

## When to Use

**Trigger conditions:**
- User supplies education material — 教育部新聞、校園事件、教育研究論文摘要、課程改革公告、升學統計、教師訪談、學生表現數據 — and asks for a news piece.
- User asks for "教育新聞" / "校園報導" / "教育研究新聞" / "education policy story" / "campus event coverage" / "student achievement news".
- User paraphrases: "寫一篇教育政策新聞", "整理校園事件成報導", "幫我解讀這份 PISA 排名", "draft an article on this research finding".

**Input signals:**
- Named schools, students (or deidentified cohorts), educators, education institutions, student data, curriculum changes, test scores, research findings.
- Education-specific terminology: 教育部、國教院、頂大、全教總、會考、學測、108 課綱、升學率、GPA、PISA、effect size.

**When NOT to use:**
- School / education institution press release in the institution's own voice → use `pr-press-release`.
- Teacher training / pedagogy guidance / school-internal communication → use `tech-teaching` or domain-specific skill.
- Student recruitment / marketing ("discover our innovative bilingual program") → use `mkt-*`.
- Pure curriculum design or lesson-planning → out of scope for journalism.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1–3, adds education-specific Step 3.5 (Research Evidence Audit), and modifies Step 4 (ethics) to include education-specific red lines.

### Step 1: Classify the education-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|-------------------|
| **Policy reform** | 教育部公告、課綱改革、考試制度異動、教育經費、教師待遇 | Policy text + affected stakeholders (students/teachers/parents) + evidence of impact (if any) + cost source |
| **Research findings** | 論文摘要、研究機構發布、效果研究、實驗性介入 | Effect size + sample demographic + replication status + funding + limitations |
| **Campus events** | 校園事件、學生表現、教師表揚、學校特色 | Deidentify minors; verify with school; avoid generalizing single case to "trend" |
| **Student data / achievement** | 升學率、考試排名、PISA / TIMSS 結果、學習成果統計 | Define the metric (升學率 vs 錄取率 vs 申請成功率); cite official source; note demographic skews |

If ambiguous, **ask the user** — do not guess.

### Step 2: Source vetting & demographic tagging

**Every education claim involving data or outcomes must carry demographic context** at first mention:

- ❌ Vague: 「研究顯示,雙語教育提升閱讀成績。」
- ✅ Specific: 「一項由台灣大學 2024 年進行的研究,針對 240 位台北市雙語班四年級學生,發現閱讀成績提升 0.6 個標準差(Cohen's d=0.6)。」
- ✅ With limitation: 「該研究樣本侷限於市區雙語班;在農村地區試行時效果未再現。」

**Education source tier tagging** (extends med-news-reporter):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Public education data** | 教育部統計、PISA / TIMSS 官方報告、聯招中心數據 | Direct citation; verify source year + calculation method |
| **Institutional official** | 學校發言人、教育局長、大學主任秘書 | Name + title; note if statement is preliminary vs final |
| **Researcher / academic paper** | 論文摘要、研究者本人、教育研究機構 | Always extract effect size + sample + replication from paper, not author's summary |
| **Teacher / student** | Named educators, named or deidentified students | 兒少法 §69 protection; parental consent; no name + school combo |
| **Interest group** | 教師工會、家長團體、教育評鑑機構 | Identify stake; separate fact claims from advocacy positions |

### Step 3: Education-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **兒少法 §69** — do NOT disclose name + school + identifying details of minors:
   - ❌ "12 歲的王小華就讀範例國中"
   - ✅ "一位 12 歲女學生" / "示範國中一名四年級男童"
   - Even with parental consent, err toward deidentification.

2. **升學率 / 錄取率口徑混淆**:
   - "升學率"(進入高等教育比例) ≠ "錄取率"(申請者中被錄取比例) ≠ "申請成功率"(報考人數 ÷ 錄取人數)
   - Always cite official source (聯招中心、教育部) and definition. If ambiguous in source, flag as `[待查證: 升學率定義]`.

3. **研究結果過度延伸(Goodhart's Law)**:
   - "One school improved writing with Method X" does not support "Method X should be national policy".
   - "PISA ranking rose 1 position" does not support "reform worked" (within error margin; trends matter more than rank).
   - Mark speculative cause-effect as conditional: "如果..." / "可能" / "若要推廣至全國,須進一步驗證".

4. **教師受訪許可**:
   - Teachers employed by schools usually need school approval to speak publicly.
   - 「受訪時曾言及」need confirmation: did the school grant permission? Mark risk if unclear.

5. **校園隱私與實驗倫理**:
   - Classroom data (test scores, attendance, behavioral notes) may contain PII.
   - Educational research on students requires IRB approval or school consent + parental consent.
   - If data source unclear, ask before citing.

### Step 3.5: Research Evidence Audit (education-specific addition)

For every research-based claim, extract and verify:

1. **Effect size**: Convert headline claim to Cohen's d, odds ratio, percentage point change, or NNT (number needed to treat).
   - If not in abstract, read Methods + Results. If absent, flag as `[待查證: 效果量統計值]`.
   - Benchmark: education interventions with d < 0.2 are weak; d > 0.5 are strong.

2. **Sample size and demographic**:
   - Who? (Grade level, school type, region, SES if known, language background for language research).
   - How many? (N = total sample size).
   - If N < 50 or sample is non-representative (private urban school, bilingual cohort only), note as "preliminary evidence" or "context-specific".

3. **Replication and consistency**:
   - Is this a single published study, a pre-print, a meta-analysis, or a series of replications?
   - If single study: "a study found" not "studies show".
   - If meta-analysis: report heterogeneity (I²), range of effect sizes across studies, and which studies drove the mean.

4. **Funding and conflict of interest**:
   - Who paid for the research? (Ministry, private foundation, school, textbook company?).
   - Relevant conflict (e.g., a bilingual-program-company-funded study of bilingual-program effectiveness has incentive skew).
   - Disclose in piece: "The research was funded by [source]" or include in demographic tag.

5. **Publication status**:
   - Peer-reviewed journal > preprint > press release > blog.
   - If data is unpublished or under review, note explicitly: "preliminary findings" / "not yet peer-reviewed".

---

## Output Format

Use the med-news-reporter base format, with these education additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 教育政策新聞 / 研究新聞 / 校園事件 / 升學新聞
**字數**: approx. XXX
**消息來源層級**: 教育部公開資料 N / 具名教育者 N / 研究論文 N / 學校 N / 利益相關團體 N / 學生/家長 N
**教育專業檢核**:
- 人口統計完整性: ✅ / ⚠️ (列出缺項: 樣本數 / 地區 / 年級 / 家庭背景)
- 效果量稽核: ✅ / N/A / ⚠️ (報告 Cohen's d / 百分點 / 其他指標 + 樣本)
- 研究複製狀態: ✅ / ⚠️ (單一研究 vs 後續複製 vs 後設分析)
- 兒少法 §69 保護: ✅ / ⚠️ (無名字 + 學校組合 / 數據去識別)
- 升學率定義澄清: ✅ / N/A / ⚠️ (列出採用之定義與來源)
**經費與利益揭露**: 〔研究經費來源、利益關係人〕
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

### Good Example

**Scenario:** User supplies (a) 國家教育研究院 2024 年一份教科書閱讀理解研究摘要(樣本 640 名中部六年級學生),報告採用新編版與舊版教科書的效果比較,Cohen's d=0.45,95% CI [0.28, 0.62];(b) 教育部新聞稿回應;(c) 親子天下與報導者過往類似研究的對比。要求寫 900 字教育新聞。

**Analysis:**
1. Step 1: classified as **research findings** (研究新聞),焦點是教科書介入的效果證據。
2. Step 2: source tier — 國教院論文屬 Tier 1(academic); 教育部新聞稿屬 Tier 1(institutional); 先前研究為背景參考。
3. Step 3: risk check — 樣本為國小六年級,中部地區,無兒少法問題(因為報告已去識別)。
4. Step 3.5 (Research Evidence Audit):
   - 效果量: Cohen's d=0.45 —— 屬中等效果,教育上有意義。
   - 樣本: N=640, 台灣中部六年級 —— 樣本大,但侷限於一地區、一年級,全國推廣需後續驗證。
   - 複製狀態: 此為首次研究;未來應進行rural區校驗。
   - 經費: 國教院主導,中立來源。
5. Output footer 標示效果量、樣本demographic、複製狀態,以及後續驗證需求。

Result: 讀者清楚知道:改革有evidence support(d=0.45),但證據來自特定地區特定年級,推廣需謹慎與後續評估。

### Bad Example

**Scenario:** Same input. Writer produces piece that (a) leads with "教科書改革提升學生閱讀成績達 12%" without effect size or sample context, (b) omits sample demographic ("中部六年級" → 改為泛稱「台灣學生」), (c) cites 親子天下 過往發現 as "一致證據" without reporting that past study had N=85 and d=0.2 (much weaker), (d) removes methodological footer because "it looks clean".

**What went wrong:**
- (a) The "12%" headline is 真的,但12 % point ≠ 0.45 Cohen's d。讀者無法判斷是meaningful reform還是統計雜訊。
- (b) Demographic omission makes readers think evidence applies to "all Taiwan students", not "600+ students in Central region". Single-region, single-grade studies do not automatically generalize.
- (c) Treating d=0.45 and d=0.2 as equally "consistent evidence" misleads. The new study is stronger; the historical comparison is less so. Reader needs that hierarchy.
- (d) Removing methodology footer hides the real limitation: this study alone cannot support national policy.

Net:每個句子都technically true,但讀者會高估evidence strength,導致政策決定可能過度樂觀。

---

## Gotchas

- **「一項研究發現」就開始鬼扯推廣**: single study without replication does not support sweeping claims. Distinguish "preliminary evidence" (d=0.4, N=240, one school) from "established finding" (meta-analysis, d=0.3-0.5, multiple regions, 5+ studies). If only one study exists, say so.
- **升學率、錄取率、申請成功率混用是新聞硬傷**: 「上榜率 90%」可能意思是「報考人中 90% 至少被某校錄取」而非「錄取人數 ÷ 招生名額 = 90%」。查教育部 / 聯招中心公開定義,不要自己猜。
- **PISA 排名變動 1-2 名常在誤差範圍內**: 國家排名 year-over-year 波動通常在統計雜訊內; 改革效果需 3-5 年與趨勢觀察,不是單年名次。把trend當rank報導是政策麻木不仁的來源。
- **「校園事件」 ≠ 「教育趨勢」**: 一所學校發生的事不代表全國或全市現象。不要把"一個學生寫很好的小說"改寫成"108 課綱提升創意寫作能力"。加「一個案例」的記號;系統主張須系統證據。
- **教師受訪許可風險被低估**: 公立教師(或按聘僱契約)通常須學校同意才能公開發言。直接訪問教師而學校不知,可能違反僱傭規約或公務員身分限制。事先確認:學校知道嗎?有沒有同意?
- **兒少法 §69 疏漏導致法律風險**: 不得揭露兒少身分(姓名、就讀學校、住址、相片等)。即使有家長同意也建議謹慎;二次傳播時無法控制。學生用代號或deidentify。
- **研究經費來源不揭露會誤導**: 「一項研究發現雙語教育更優」未說明是自費教科書公司資助,讀者無法自行judging bias。永遠註明誰付的錢。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 教育線消息來源、機構、官方資料庫、主要利益相關者 | Step 2 source vetting |
| `references/glossary.md` | 教育專業術語:升學率 vs 錄取率、108 課綱、會考 vs 學測、PISA / TIMSS | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 兒少法 §69、校園隱私、教師言論限制、教育資料去識別 | Step 3 risk check |
| `references/research_evidence_reading.md` | 效果量判讀、樣本代表性、複製危機、Goodhart's law in education | Step 3.5 research audit |
| `references/policy_landscape.md` | 台灣教育制度概覽、近年重大改革(108 課綱、雙語政策、少子化) | Background context |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-political` — for education-policy stories with strong political dimension
- `stat-hypothesis-testing` — for deep methodological critique of research
- `stat-eda` — exploratory data analysis on education datasets
- `grad-survey-design` — for evaluating educational surveys and sampling
- `hum-source-criticism` — source vetting frameworks

---

## Limitations

- **Does not verify live education databases**: this skill flags claims that need verification; it does not query 教育部統計、聯招中心即時數據、或校務評鑑資料。Operator must verify or supply.
- **Jurisdictional scope**: legal references (兒少法、個資法) reflect Taiwan context. For US (FERPA), EU (GDPR), HK, or PRC, the principles still apply but specific statutes differ — substitute jurisdiction-specific references.
- **Not a curriculum-design skill**: judging whether a proposed curriculum is pedagogically sound requires subject-matter expertise beyond this journalism skill. This skill flags research claims; does not evaluate curriculum itself.
- **Effect-size threshold opinions**: guidelines like "d > 0.4 is strong" reflect international benchmarks; Taiwan education ministry may have different policy thresholds. Check ministry guidance for policy-relevant effect-size floors.
- **Education-policy lag**: reforms typically show effects 3-5 years after implementation. Attributing short-term score changes to new policy is common and often wrong. Flag temporal claims carefully.
- **Student recruitment marketing claims** disguised as news: some "education stories" from institutions are low-key marketing. If the piece is originated/heavily promoted by the school being featured, disclose the source relationship.
