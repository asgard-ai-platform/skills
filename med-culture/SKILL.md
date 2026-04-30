---
name: "med-culture"
description: "Use when the user wants to write a culture-and-arts news piece — exhibition coverage, performance reviews, artist interviews, cultural policy analysis, art market reporting, or cultural heritage reporting — from supplied material. Activates culture-beat-specific workflow on top of the general news-reporter workflow: cultural appropriation audit, indigenous knowledge protection, source credibility (institutional PR vs. independent critic), aesthetic judgment marking, and translation/cross-cultural framing discipline. Also triggers on phrases like 'draft an exhibition review', 'write up this gallery opening', 'turn into an album review', '整理展覽新聞', '寫一篇評論', '幫我做藝術家訪談', 'cover this museum exhibition', '草擬一篇文化評論'. Defers general news craft to med-news-reporter; do NOT use for art-marketing copy (use mkt-*) or artist/gallery press releases (use pr-press-release)."
metadata:
  category: "WP-50 大眾傳播"
  tags: ["news", "journalism", "culture-news", "arts-journalism", "criticism"]
---

# Culture & Arts Reporting

> **This skill specializes med-news-reporter for the arts/culture beat.** Read med-news-reporter first for the general 6-step workflow (type selection, material audit, fact-check, balance, ethics, literacy). This file adds **culture-beat-specific discipline** on top: cultural appropriation awareness, indigenous knowledge protection, institutional vs. independent source marking, aesthetic judgment transparency, and cross-cultural translation pitfalls.

## Overview

Distilled from culture-journalism curricula at Columbia (Arts & Culture Concentration), NYU Journalism, NCCU 文化人類學, NTU 人類學系, 台藝大文化政策所. Covers the main culture-news sub-types: **exhibition/museum reporting, performance-arts criticism, artist profile, cultural policy/heritage, and art-market reporting.**

```
IRON LAW: Critique Is Marked Opinion, Not Fact

Aesthetic judgments—"the painting is powerful", "the dancer lacked 
precision", "this work pushes boundaries"—are opinions tied to a 
critical framework. They must always be (a) marked as judgment, NOT 
framed as fact; (b) attributed to a named critic / school of thought 
/ institutional voice, with their standpoint disclosed; (c) supported 
by reasoning or observable detail, not bare assertion. Factual reporting 
(artist X exhibits at venue Y on date Z with medium M) is separable 
from aesthetic evaluation. Default LLM behavior conflates them via 
descriptive adjectives that smuggle judgment into "fact" ("the brilliant 
emerging artist", "the disappointing retrospective"). Override this 
explicitly: strip adjectives or attribute them.

Why this is non-obvious: "brilliant" reads like a natural way to 
describe an artwork, not an opinion. But it is. The reader deserves 
to know whether "brilliant" is (i) a direct quote from the artist's 
institution, (ii) an observation by a named art historian with a known 
aesthetic stance, or (iii) an invented consensus the writer assumes.
```

Why this is non-obvious: the aesthetic judgments arrive naturally in prose. A piece on a new exhibition will naturally invite adjectives; defaulting to "powerful" or "striking" silently endorses a reading that may not be universal. Credible critics mark their stance upfront.

**Rationalization Table — these justifications DO NOT override the Iron Law:**

| Claude might think... | Why it's still a violation |
|---|---|
| "The artist's gallery calls the work 'groundbreaking', so I'll use it" | Still an opinion even if uttered by the institution. Mark it: 「該藝廊稱該作『突破性』」, not 「突破性作品」. |
| "The museum website says 'innovative', it's public info" | Institutional description ≠ fact. Separate: "The museum describes the exhibition as X; art critics debate whether Y." |
| "'Derives from' is just describing influence, not judging" | Influence-attribution is a critical claim. Does the named artist agree? Did they cite this influence themselves, or is it art-historical interpretation? Be explicit. |
| "Critics universally praise this artist, so 'acclaimed' is fact" | "Universally praised" is hyperbole that collapses critical diversity. Even if true, say: "Multiple critics praised..." with names/sources. |
| "The work failed to engage the audience" | Describe observable fact: "audience walked out", "low attendance", not an interpretation. If you infer a judgment, cite whose interpretation. |
| "I'm just translating the original artwork's intent" | Translating artistic intent is interpretation, not fact. Even with the artist's own statement, note: "The artist stated intent is X; critics interpret as Y." |

---

## When to Use

**Trigger conditions:**
- User supplies culture/arts material — 展覽新聞、演出評論、藝術家訪談、文化政策、美術館新聞稿、評論草稿、演出影片節摘錄、文物借展公告 — and asks for a news/criticism piece.
- User asks for "exhibition report", "performance review", "art criticism", "gallery profile", "cultural policy tracker", "museum feature", "整理展覽新聞", "寫一篇評論", "藝術家專訪", "評論展覽".
- User paraphrases: "幫我把這份策展自述寫成報導", "寫一篇關於 X 美術館的新聞", "整理成一篇演出評論", "draft a piece on this artist opening", "turn this interview into a profile".

**Input signals:**
- Named artists, galleries, museums, cultural institutions, exhibition titles, artwork titles, performance venues, dates.
- Curatorial statements, artist interviews, critic reviews, institutional PR, attendance figures, cultural policy documents.
- Direct quotes from artists, curators, collectors, critics.

**When NOT to use:**
- Gallery/artist/museum press release in the institution's own voice → use `pr-press-release`.
- Art-market price prediction or investment advisory → use `fin-*` or decline.
- Marketing copy for an exhibition or art product → use `mkt-*.`
- Pure entertainment industry news (celebrity, awards ceremony) → use `med-entertainment`.

---

## Methodology

### Step 0: Defer general workflow to med-news-reporter

Read or have already loaded `med-news-reporter` for: material audit, fact-checking, source-strength tagging, balance principle, media-ethics check, media-literacy self-check. **Do not re-implement those steps here.** This file specializes Steps 1, 2, 3, and adds a culture-specific Step 7 (Aesthetic Judgment Audit + Cross-Cultural Sensitivity Audit).

### Step 1: Classify the culture-story sub-type

| Sub-type | Signals | Sub-template focus |
|----------|---------|--------------------|
| **Exhibition/museum** | Opening date, venue, artist/curator name, artworks, theme | Curatorial intent + artwork description separate from judgment; source marking (PR vs. independent review) |
| **Performance review** | Venue, troupe, performer, date, genre (劇場/音樂/舞蹈), attendance | Aesthetic judgment tied to named critic or review publication; descriptive detail before evaluation |
| **Artist profile** | Artist bio, background, major works, recent exhibition/residency | Career trajectory via public record; quotes attributed; avoid "rising star" unless cited |
| **Cultural policy/heritage** | 文化部政策、文資法、世界遺產、古蹟保存、文化補助機制 | Policy text + stakeholder impact + indigenous/minority voice included; legal/administrative accuracy |
| **Art market** | 拍賣、藝術基金、畫廊銷售、藝術家身價、收藏趨勢 | Price ≠ artistic quality (separate fact from market signal); conflict-of-interest disclosure (auction house estimator, dealer stake) |

If the material spans sub-types (e.g., an artist's first major museum show), classify by the *primary news driver*.

### Step 2: Source vetting & institutional-voice tagging

**Every cultural institution quoted must be tagged for PR affinity** at first mention:

- ❌ Vague: 「該美術館表示...」
- ✅ Specific: 「國立故宮博物院策展部主任王大明表示...」
- ✅ When PR interest matters: 「舉辦單位 / 參展藝廊林小華表示...」(signals institutional interest in promotion)
- ✅ When independent: 「獨立評論家 / 藝評人 王大明表示...」or 「ArtForum 評論員表示...」

**Source tier tagging** (extends med-news-reporter's tiering with culture-specific tiers):

| Tier | Examples | Treatment |
|------|----------|-----------|
| **Public record / official document** | 文化部施政報告、世界遺產名單、古蹟登錄公告、展覽官方新聞稿 | Direct citation; note source is institutional. |
| **Curatorial/artist statement (on record)** | 策展人訪談、藝術家自述、美術館展覽說明頁面 | Direct quote with role tag; note: this is institution's framing, not independent view. |
| **Independent critic/reviewer** | 藝評人刊登於獨立媒體之評論、學者論文、展評 | Direct quote; include publication/credentials to let reader calibrate standpoint. |
| **Collector / dealer** | 拍賣公司、畫廊、私人收藏家 | Quote with interest disclosure: "Sotheby's estimated [price]" signals auction-house stake in high valuation. |
| **Audience/community** | Visitor comment, indigenous/minority community perspective on cultural heritage | Include voice especially when discussing cultural appropriation, indigenous knowledge, or community impact. |

### Step 3: Culture-specific risk check

Beyond med-news-reporter's general ethics check, add:

1. **文化挪用 (Cultural Appropriation) audit**:
   - If reporting on cross-cultural artwork (Western artist depicting East Asian imagery, etc.): does the piece include the perspective of the source culture / originating community? Or only outsider framing?
   - Report should signal: "praised by Western critics for aesthetic innovation" vs. "criticized by East Asian artists' collectives for appropriation without acknowledgment."
   - If a practice is sacred (宗教儀式、部落傳統), does the reporting frame it as "external observation" or implicitly as common knowledge? Label the frame.

2. **原住民族傳統智慧創作保護條例 (Indigenous IP Protection)**:
   - When reporting on indigenous art, cultural symbols, myths, or music: verify whether use requires 部落同意 (tribal consent).
   - Avoid treating indigenous knowledge as "public domain" in reporting. If an artwork samples indigenous symbols, check whether artist obtained consent and credit was given.

3. **著作權與合理使用 (Copyright & Fair Use in Arts Criticism)**:
   - Quoting poetry, song lyrics, artwork descriptions: review `references/ethics_and_law.md` for fair-use thresholds.
   - Entire-poem quotation in a review = copyright violation. Excerpt + attribution = fair use.

4. **肖像權 & Privacy in portraits/photography**:
   - If artwork depicts identifiable people: include consent / privacy disclaimers if needed.
   - If artist is interviewed and expresses private views: respect off-record signals.

5. **Auction / appraisal interest disclosure**:
   - When citing artwork valuation or market price: state who estimated/appraised it and their financial interest.
   - "Sotheby's estimates the work at NT$5M" ≠ "the work is worth NT$5M." First is fact (auction-house prediction with $ stake); second is opinion disguised as fact.

### Step 4: Aesthetic Judgment Audit (culture-specific addition)

Before output, sweep the draft for:

1. **Judgment-adjective audit**: highlight every aesthetic claim ("powerful", "delicate", "derivative", "innovative", "haunting"). For each: replace with (a) observable detail, OR (b) attribute to a named critic / publication / school, with their stance disclosed, OR (c) delete if unsupported.
2. **Curatorial vs. independent framing**: does the piece rely mainly on the museum/gallery's own description of the exhibition? If yes, explicitly label it ("The museum describes the exhibition as...") and add an independent critic's view for balance.
3. **Price vs. value slippage**: check for "the work sold for NT$10M, proving its significance" (conflates market signal with artistic judgment). Separate them: "sold for NT$10M (market signal)" vs. "critics argue its significance lies in X" (judgment).
4. **Translation loss disclosure**: if reviewing a work in translation (play, poetry, opera libretto), note that the original language may carry layers lost in translation. Example: "The original Taiwanese pun in the dialogue does not translate to English."
5. **Minority/indigenous voice inclusion**: in pieces on cultural heritage, appropriation, or community cultural impact, does the reporting include voices of affected communities, or only institutional/expert voices? Flag if absent.

### Step 5: Cross-Cultural Sensitivity & Frame Audit

1. **Inside vs. outside frame**: when describing religious rituals, indigenous ceremonies, or minority cultural practices, does the report mark whether the observer is an insider or outsider? Example: "As described by ethnographers observing..." vs. "From within the community..." signals different epistemic position.
2. **Essentialism check**: avoid "X culture is inherently Y" framings. Replace with: "In the context of X community's Y tradition, this practice means Z" (specific, not universal).
3. **Political sensitivity (China/Taiwan/Hong Kong terms)**: when discussing artwork origins or artist nationality, use precise terms. "Made in Taiwan" ≠ "Chinese artist" ≠ "Hong Kong contemporary". Verify how the artist/work self-identifies.
4. **Translator/interpreter credit**: if the artwork title or artist statement is in a non-English language, include the translator's name. Translation is interpretation; reader should know who interpreted.

---

## Output Format

Use the med-news-reporter base format, with these culture additions to the meta footer:

```markdown
[Headline / sub-headline / body paragraphs per med-news-reporter]

---

**稿件類型**: 即時展覽新聞 / 演出評論 / 藝術家專訪 / 文化政策追蹤 / 藝術市場分析
**字數**: approx. XXX
**消息來源層級**: 公開記錄 N / 機構 (PR) N / 獨立評論 N / 藝術家/策展人 N
**文化敏感度稽核**:
- 機構聲音標記: ✅ / ⚠️ (列出未標記的機構引述)
- 獨立評論或平衡: ✅ / ⚠️ (機構PR vs. 獨立評論的比例)
- 審美判斷標記: ✅ / ⚠️ (列出未標記的評價形容詞)
- 文化挪用檢查: ✅ / N/A / ⚠️
- 原住民族聲音: ✅ / N/A / ⚠️ (涉及時)
- 翻譯 / 跨文化框架: ✅ / N/A / ⚠️
- 價格 ≠ 價值分離: ✅ / N/A / ⚠️
**待查證事項**: ...
**倫理 / 識讀檢核摘要**: 〔交給 med-news-reporter 的 Step 4-5 footer〕
```

---

## Examples

See `examples/sample_input.md` and `examples/sample_output.md` for a full worked exhibition-reporting scenario.

---

## Gotchas

- **「機構聲音」和「評論」不能混為一談**: 美術館的展覽說明頁面、策展自述都有推廣展覽的利益。獨立評論家的批評角度可能很不同。不要讓讀者以為策展人的「大膽創新」 vs 評論家的「形式疲軟」是同一種聲音。前者標註為機構立場,後者標註為獨立評論。
- **「票房好」≠「藝術優秀」;「拍賣價高」≠「大師傑作」**: 商業成功是市場訊號,不是藝術判準。一篇報導若寫「該藝術家因作品拍賣創高價成為新興大師」,實際上混淆了。應寫「作品在拍賣會達 X 價格,業界視為市場認可;藝評人對其藝術貢獻的評估則不一」。
- **評論寫作的「事實基礎」**: 說「畫面色彩大膽」需要能指出「怎樣的色彩配置」(可驗證的觀察);說「表演力度不足」需要能說「與同場演員的對比」或「與該演員其他演出的對比」(comparative fact)。光說評價不說依據,讀者無法判讀你的品味是否值得採納。
- **翻譯作品評論須註明**: 評論一齣外文劇本、一首譯詩、一本譯作時,至少要說「根據 X 譯者的譯本」。不同譯者的詮釋差很大;讀者該知道你評的是哪個版本。
- **文化挪用辨識不易,但框架要誠實**: 「西方藝術家詮釋東亞文化」不自動等於挪用,也不自動等於無罪。應報導:該社群怎麼看?藝術家有無致謝 / 協作?評論家怎麼爭論?不要預設立場,要呈現爭議的樣貌。
- **原住民族相關報導時,應主動求聲音**: 涉及原民文化藝術、傳統工藝、文化資產時,報導中應包含部落 / 社群的視角,不要只引學者 / 官方。其聲音的缺席本身就是個信號。

---

## References

| File | Purpose | When to read |
|------|---------|--------------|
| `references/sources_and_beats.md` | 文化線消息來源(文化部、各美術館、評論刊物、國際資源) | Step 2 source vetting |
| `references/glossary.md` | 文化、藝術、文資領域術語對照與定義 | When unfamiliar terminology appears |
| `references/ethics_and_law.md` | 著作權法合理使用、文化資產保存法、原住民族傳統智慧創作保護、肖像權 | Step 3 risk check |
| `references/cultural_sensitivity.md` | 文化挪用辨識、原住民族報導守則、宗教/儀式報導框架、跨文化翻譯陷阱 | Step 4-5 sensitivity audits |
| `references/critique_writing.md` | 描述 vs 評價之分界、評論的事實基礎、價格≠價值、市場趨勢≠藝術品質 | Step 4 aesthetic judgment audit |

Related skills:
- `med-news-reporter` — general news workflow (this skill specializes it)
- `med-entertainment` — for film/TV/streaming-specific coverage (separate beat focus)
- `hum-source-criticism` — source vetting frameworks
- `hum-rhetoric` — deeper analysis of persuasion structures (useful for critique analysis)
- `grad-ethnography` — ethnographic / cultural-context research methodology

---

## Limitations

- **Does not perform live institutional fact verification**: this skill flags claims about museum hours, exhibition dates, or curator credentials that need verification; it does not check live museum websites or institutional databases. Editor must verify or user must supply current info.
- **Does not arbitrate cultural appropriation**: this skill flags when a piece lacks the source culture's voice or appropriate framing; it does not make the final judgment about whether something is appropriative. That judgment belongs to affected communities and informed critics — the skill just ensures the reporting includes their perspectives.
- **Cross-cultural interpretation is inherently contested**: describing an artwork from another culture always involves interpretation. This skill requires explicit framing (inside/outside perspective) but cannot eliminate the fundamental epistemic challenge.
- **Original-language loss in translation**: when reviewing translated works, this skill flags the issue; it does not solve it. A full engagement with translation loss requires either the original language or explicit scholar/translator consultation.
- **Price data is time-sensitive**: artwork valuations and auction estimates change. Always verify against current market data; do not rely on historical prices as present-day facts.
