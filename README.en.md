# Asgard Skills

Open-source library of **293 coding agent skills** across 22 topic-based categories. Each skill is a self-contained Markdown file (`SKILL.md`) following the [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) standard, with optional Python scripts for deterministic calculations.

[繁體中文](README.md)

## Overview

This repository is the **raw ingredient pantry** for the [Asgard AI Platform](https://github.com/asgard-ai-platform). Skills are combined with [Asgard MCPs](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) to assemble [coding agent plugins](https://github.com/asgard-ai-platform) targeting specific user personas (e.g., Taiwan stock analyst, e-commerce operator, policy researcher).

A skill encodes **methodology + judgment + gotchas** for one well-defined task — what an LLM agent would otherwise have to rediscover or get wrong.

## Repository Layout

```
.
├── {category}-{skill-name}/
│   ├── SKILL.md           ← Level 1 frontmatter + Level 2 instructions
│   ├── examples/          ← (always present, populated as needed)
│   ├── references/        ← (heavy/long content offloaded here)
│   └── scripts/           ← (only when deterministic calculator exists)
└── ...
```

## Categories (22 prefixes, 293 skills)

| Prefix | Count | Topic |
|--------|------:|-------|
| `grad-` | 87 | Graduate-level theoretical models (RBV, CAPM, SEM, DID, ...) |
| `algo-` | 62 | Algorithms (PageRank, BM25, ARIMA, EOQ, ...) |
| `biz-` | 22 | Business school frameworks (SWOT, Porter's Five Forces, DCF, ...) |
| `hum-` | 9 | Humanities / critical reasoning |
| `tw-` | 38 | Taiwan-specific knowledge (e-commerce, stock, tax, e-invoice, fintech, ...) |
| `ecom-` | 7 | E-commerce practical |
| `econ-` | 6 | Economics fundamentals |
| `meta-` | 6 | Interdisciplinary mental models |
| `ops-` | 6 | Business operations (OKR, contract review, pitch deck, ...) |
| `law-` | 5 | Legal frameworks |
| `pr-` | 5 | PR & brand communications |
| `cs-` | 4 | Customer service |
| `data-` | 4 | Data analytics |
| `mfg-` | 4 | Manufacturing |
| `mkt-` | 4 | Digital marketing |
| `soc-` | 7 | Social science |
| `stat-` | 4 | Statistical methodology |
| `tech-` | 4 | General tech (API, prompt engineering, MCP server, ...) |
| `ux-` | 4 | Design / UX methodology |
| `fin-` | 2 | Finance practical (modeling, earnings) |
| `xborder-` | 2 | Cross-border commerce |
| `med-` | 1 | Mass communication / journalism |

## Skill Catalog

Every skill below is a directory at the repo root. Click the name to open its `SKILL.md`. Descriptions are condensed from each skill's frontmatter (WHAT + WHEN).


<details>
<summary><b><code>grad-</code></b> — Graduate-level theoretical models (87)</summary>

- [`grad-action-research`](grad-action-research/SKILL.md) — Apply action research through Plan-Act-Observe-Reflect cycles and Participatory Action Research (PAR) to generate knowledge while improving practice.
- [`grad-affordance`](grad-affordance/SKILL.md) — Apply Affordance Theory (Gibson, 1979; Norman, 1988) to analyze the action possibilities that an artifact provides to an actor.
- [`grad-agenda-setting`](grad-agenda-setting/SKILL.md) — Apply agenda-setting theory (McCombs & Shaw) to analyze how media salience transfers to public perception.
- [`grad-ai-ethics`](grad-ai-ethics/SKILL.md) — Apply AI ethics frameworks (fairness, accountability, transparency, privacy) to evaluate AI systems for algorithmic bias, explainability gaps, and value alignment failures.
- [`grad-ambidexterity`](grad-ambidexterity/SKILL.md) — Apply organizational ambidexterity theory to balance exploration and exploitation activities.
- [`grad-ant`](grad-ant/SKILL.md) — Apply Actor-Network Theory (Latour, Callon) to trace how human and non-human actors (actants) form networks through translation processes.
- [`grad-auction-theory`](grad-auction-theory/SKILL.md) — Apply auction theory to compare the four canonical auction formats and assess revenue equivalence.
- [`grad-behavioral-finance`](grad-behavioral-finance/SKILL.md) — Apply behavioral finance theory to identify systematic investor biases and their impact on asset prices.
- [`grad-blooms`](grad-blooms/SKILL.md) — Apply Bloom's revised taxonomy to classify learning objectives and design assessments across six cognitive levels.
- [`grad-born-global`](grad-born-global/SKILL.md) — Apply the Born Global framework to analyze firms that internationalize rapidly from inception under resource constraints.
- [`grad-brand-equity`](grad-brand-equity/SKILL.md) — Apply brand equity frameworks (Aaker, 1991; Keller, 1993) to assess and build customer-based brand value.
- [`grad-business-ecosystems`](grad-business-ecosystems/SKILL.md) — Apply Moore's business ecosystem framework to analyze how firms co-evolve through four stages (birth, expansion, authority, renewal) and occupy different ecosystem roles.
- [`grad-capm`](grad-capm/SKILL.md) — Apply the Capital Asset Pricing Model (CAPM) to estimate expected returns and assess risk-return tradeoffs.
- [`grad-cas`](grad-cas/SKILL.md) — Apply Complex Adaptive Systems theory to analyze phenomena exhibiting emergence, self-organization, co-evolution, and edge-of-chaos dynamics.
- [`grad-case-study`](grad-case-study/SKILL.md) — Apply case study research design (Yin) to investigate how and why questions within real-life contexts using single or multiple case designs and triangulation.
- [`grad-cct`](grad-cct/SKILL.md) — Apply Consumer Culture Theory to analyze consumption as a cultural practice shaped by identity, marketplace cultures, and ideology.
- [`grad-cognitive-load`](grad-cognitive-load/SKILL.md) — Apply Cognitive Load Theory to optimize instructional design by managing intrinsic, extraneous, and germane load within working memory limits.
- [`grad-constructivism`](grad-constructivism/SKILL.md) — Apply constructivist learning theory to design instruction based on active knowledge construction, scaffolding, and the zone of proximal development.
- [`grad-contract-theory`](grad-contract-theory/SKILL.md) — Apply contract theory to design incentive-compatible agreements under moral hazard and adverse selection.
- [`grad-coopetition`](grad-coopetition/SKILL.md) — Apply the Co-opetition Value Net framework (Brandenburger and Nalebuff, 1996) to map cooperative and competitive dynamics in business relationships.
- [`grad-critical-realism`](grad-critical-realism/SKILL.md) — Apply Bhaskar's critical realism to analyze phenomena through three ontological domains (real, actual, empirical), identify generative causal mechanisms via retroduction, and examine structure-agen...
- [`grad-cultivation`](grad-cultivation/SKILL.md) — Apply cultivation theory (Gerbner) to analyze how long-term media exposure shapes worldviews.
- [`grad-diamond`](grad-diamond/SKILL.md) — Apply Porter's Diamond Model to analyze national competitive advantage for a specific industry.
- [`grad-did`](grad-did/SKILL.md) — Apply Difference-in-Differences (DID) to estimate causal treatment effects by comparing changes in outcomes between treatment and control groups.
- [`grad-digital-transformation`](grad-digital-transformation/SKILL.md) — Apply the three-level framework of digital transformation — Digitization, Digitalization, and Digital Transformation — to diagnose and plan organizational change enabled by digital technologies.
- [`grad-disruptive-innovation`](grad-disruptive-innovation/SKILL.md) — Apply Christensen's Disruptive Innovation theory to assess low-end and new-market threats to incumbents.
- [`grad-dual-process`](grad-dual-process/SKILL.md) — Apply dual-process theory to diagnose whether judgments arise from fast intuitive (System 1) or slow analytical (System 2) processing and identify resulting cognitive biases.
- [`grad-elm`](grad-elm/SKILL.md) — Apply the Elaboration Likelihood Model to design persuasion strategies by matching message type to audience elaboration level.
- [`grad-embeddedness`](grad-embeddedness/SKILL.md) — Apply Granovetter's embeddedness theory to analyze how economic behavior is embedded in ongoing social relations, avoiding both over-socialized and under-socialized accounts.
- [`grad-emh`](grad-emh/SKILL.md) — Apply the Efficient Market Hypothesis (Fama, 1970) to evaluate information incorporation in asset prices across weak, semi-strong, and strong forms.
- [`grad-ethnography`](grad-ethnography/SKILL.md) — Apply ethnographic methods including prolonged engagement, participant observation, thick description, and netnography to study cultures and communities.
- [`grad-event-study`](grad-event-study/SKILL.md) — Apply event study methodology to measure abnormal returns and cumulative abnormal returns (CAR) around corporate or market events.
- [`grad-fama-french`](grad-fama-french/SKILL.md) — Apply the Fama-French three-factor model to decompose asset returns into market, size, and value factors.
- [`grad-field-theory`](grad-field-theory/SKILL.md) — Apply Bourdieu's field theory to analyze power relations through the interplay of field, capital, and habitus.
- [`grad-flow`](grad-flow/SKILL.md) — Apply flow theory to diagnose optimal experience conditions and design environments that balance challenge and skill for sustained engagement.
- [`grad-framing`](grad-framing/SKILL.md) — Apply framing theory to analyze how selection, emphasis, and exclusion shape interpretation of issues.
- [`grad-governance`](grad-governance/SKILL.md) — Apply governance theory to analyze multi-level, network, and collaborative governance arrangements beyond traditional government.
- [`grad-grounded-theory`](grad-grounded-theory/SKILL.md) — Apply Grounded Theory (Glaser and Strauss) to build theory inductively from qualitative data through open, axial, and selective coding.
- [`grad-hlm`](grad-hlm/SKILL.md) — Apply Hierarchical Linear Modeling (HLM) to analyze nested data structures with random intercepts and slopes, accounting for intra-class correlation and cross-level interactions.
- [`grad-info-economics`](grad-info-economics/SKILL.md) — Apply information economics to diagnose and remedy market failures caused by asymmetric information.
- [`grad-innovation-diffusion-bass`](grad-innovation-diffusion-bass/SKILL.md) — Apply the Bass Diffusion Model (1969) to forecast innovation adoption using innovation and imitation coefficients.
- [`grad-is-success`](grad-is-success/SKILL.md) — Apply the DeLone and McLean Information Systems Success Model to evaluate IS effectiveness through six interdependent dimensions.
- [`grad-mechanism-design`](grad-mechanism-design/SKILL.md) — Apply mechanism design (reverse game theory) to engineer incentive-compatible rules for allocation problems.
- [`grad-meta-analysis`](grad-meta-analysis/SKILL.md) — Apply meta-analysis to synthesize effect sizes across multiple studies, assess heterogeneity, and evaluate publication bias.
- [`grad-mixed-methods`](grad-mixed-methods/SKILL.md) — Design and conduct mixed methods research using convergent, explanatory sequential, or exploratory sequential strategies with genuine integration of qualitative and quantitative strands.
- [`grad-mm-theorem`](grad-mm-theorem/SKILL.md) — Apply the Modigliani-Miller theorem to analyze capital structure decisions and identify when financing choices affect firm value.
- [`grad-narrative`](grad-narrative/SKILL.md) — Apply narrative research methods to understand human experience through stories, analyzing narrative structure, temporality, and meaning-making in life stories and oral histories.
- [`grad-network-economics`](grad-network-economics/SKILL.md) — Apply network economics to analyze markets with network effects, critical mass dynamics, and platform competition.
- [`grad-oli`](grad-oli/SKILL.md) — Apply Dunning's OLI Paradigm (Eclectic Theory) to evaluate foreign direct investment decisions based on Ownership, Location, and Internalization advantages.
- [`grad-org-ecology`](grad-org-ecology/SKILL.md) — Apply organizational ecology (Hannan and Freeman) to analyze population-level dynamics of organizational founding, failure, and selection.
- [`grad-panel-data`](grad-panel-data/SKILL.md) — Apply panel data analysis with fixed effects, random effects, and dynamic GMM to exploit longitudinal variation and control for unobserved heterogeneity.
- [`grad-paradigms`](grad-paradigms/SKILL.md) — Apply Kuhn's paradigm theory to analyze scientific progress through the cycle of normal science, anomalies, crisis, and revolution.
- [`grad-paradox-theory`](grad-paradox-theory/SKILL.md) — Apply Smith and Lewis's paradox theory to identify and manage organizational tensions across performing, organizing, belonging, and learning dimensions.
- [`grad-pecking-order`](grad-pecking-order/SKILL.md) — Apply pecking order theory (Myers and Majluf, 1984) to analyze how information asymmetry drives financing hierarchy decisions.
- [`grad-phenomenology`](grad-phenomenology/SKILL.md) — Apply phenomenological methods including bracketing (epoche), lived experience inquiry, and Interpretive Phenomenological Analysis (IPA) to uncover the essence of human experience.
- [`grad-platform-economics`](grad-platform-economics/SKILL.md) — Apply platform economics to analyze network effects, solve chicken-and-egg problems, and design multi-sided platform pricing strategies.
- [`grad-pls-sem`](grad-pls-sem/SKILL.md) — Apply Partial Least Squares SEM (PLS-SEM) with reflective and formative measurement models to maximize explained variance in endogenous constructs.
- [`grad-policy-streams`](grad-policy-streams/SKILL.md) — Apply Kingdon's multiple streams framework to analyze how problems, policies, and politics converge to open policy windows.
- [`grad-pragmatism`](grad-pragmatism/SKILL.md) — Apply pragmatist philosophy (Peirce, James, Dewey) to frame knowledge as instrumental for action, evaluate ideas by their practical consequences, and conduct inquiry as problem-solving.
- [`grad-public-choice`](grad-public-choice/SKILL.md) — Apply public choice theory to analyze political decision-making as rational self-interested behavior.
- [`grad-real-options`](grad-real-options/SKILL.md) — Apply real options analysis to value managerial flexibility embedded in investment decisions.
- [`grad-sd-logic`](grad-sd-logic/SKILL.md) — Apply Service-Dominant Logic (Vargo and Lusch, 2004) and value co-creation principles to reframe exchange and value creation.
- [`grad-sdt`](grad-sdt/SKILL.md) — Apply Self-Determination Theory to analyze motivation quality along the autonomy continuum and design interventions that satisfy basic psychological needs.
- [`grad-sem`](grad-sem/SKILL.md) — Apply Structural Equation Modeling (SEM) to test hypothesized causal structures by combining measurement models (CFA) and structural models (path analysis).
- [`grad-sensemaking`](grad-sensemaking/SKILL.md) — Apply Weick's sensemaking theory to analyze how individuals and organizations construct meaning from ambiguous situations.
- [`grad-servqual`](grad-servqual/SKILL.md) — Apply the SERVQUAL model (Parasuraman, Zeithaml, and Berry, 1988) to measure service quality gaps across five dimensions.
- [`grad-signaling`](grad-signaling/SKILL.md) — Apply signaling theory (Spence, 1973) to analyze how agents communicate private information through costly, credible signals under information asymmetry.
- [`grad-social-capital`](grad-social-capital/SKILL.md) — Apply social capital theory (Putnam, Coleman, Bourdieu, Burt) to analyze how network structures and trust generate value or impose constraints.
- [`grad-social-identity`](grad-social-identity/SKILL.md) — Apply Social Identity Theory to analyze how group categorization, identification, and intergroup comparison drive behavior, bias, and conflict.
- [`grad-sociotechnical`](grad-sociotechnical/SKILL.md) — Apply Sociotechnical Systems Theory to analyze and design work systems through joint optimization of social and technical subsystems.
- [`grad-spiral-of-silence`](grad-spiral-of-silence/SKILL.md) — Apply spiral of silence theory (Noelle-Neumann) to analyze how perceived opinion climate suppresses minority expression.
- [`grad-strat-agency`](grad-strat-agency/SKILL.md) — Apply Agency Theory (Jensen and Meckling, 1976) to diagnose principal-agent problems — moral hazard, adverse selection — and design governance mechanisms to align interests.
- [`grad-strat-dynamic-cap`](grad-strat-dynamic-cap/SKILL.md) — Apply the Dynamic Capabilities framework (Teece et al., 1997) — sensing, seizing, and transforming — to analyze how firms adapt, integrate, and reconfigure competences in rapidly changing environme...
- [`grad-strat-institutional`](grad-strat-institutional/SKILL.md) — Apply Institutional Theory (DiMaggio and Powell, 1983) to analyze how coercive, mimetic, and normative isomorphic pressures shape organizational structures and practices.
- [`grad-strat-kbv`](grad-strat-kbv/SKILL.md) — Apply the Knowledge-Based View (Grant, 1996) and Nonaka and Takeuchi's SECI model to analyze how organizations create, transfer, and integrate knowledge for competitive advantage.
- [`grad-strat-rbv`](grad-strat-rbv/SKILL.md) — Apply the Resource-Based View (Barney, 1991) and VRIO framework to evaluate whether a firm's resources and capabilities confer sustained competitive advantage.
- [`grad-strat-stakeholder`](grad-strat-stakeholder/SKILL.md) — Apply Stakeholder Theory (Freeman, 1984) and the Mitchell et al.
- [`grad-strat-tce`](grad-strat-tce/SKILL.md) — Apply Transaction Cost Economics (Williamson, 1975, 1985) to analyze governance structure choices — market, hybrid, or hierarchy — based on transaction characteristics.
- [`grad-strat-upper-echelons`](grad-strat-upper-echelons/SKILL.md) — Apply Upper Echelons Theory (Hambrick and Mason, 1984) to analyze how top management team characteristics — demographics, experiences, values — shape strategic choices and organizational outcomes.
- [`grad-structuration`](grad-structuration/SKILL.md) — Apply Giddens' structuration theory to analyze the duality of structure — how social structures are both the medium and outcome of the practices they organize.
- [`grad-survey-design`](grad-survey-design/SKILL.md) — Apply rigorous survey design principles including construct operationalization, Likert scale development, reliability and validity assessment, and common method variance control.
- [`grad-sustainability`](grad-sustainability/SKILL.md) — Apply sustainability frameworks (triple bottom line, SDGs, ESG, circular economy) to evaluate whether strategies balance economic, social, and environmental dimensions.
- [`grad-systematic-review`](grad-systematic-review/SKILL.md) — Conduct a systematic literature review following the PRISMA framework with explicit search strategy, inclusion and exclusion criteria, quality assessment, and transparent synthesis.
- [`grad-tam-utaut`](grad-tam-utaut/SKILL.md) — Apply the Technology Acceptance Model (Davis, 1989) and Unified Theory of Acceptance and Use of Technology (Venkatesh et al., 2003) to predict technology adoption.
- [`grad-tpack`](grad-tpack/SKILL.md) — Apply the TPACK framework to evaluate and design technology-integrated instruction at the intersection of technological, pedagogical, and content knowledge.
- [`grad-tpb`](grad-tpb/SKILL.md) — Apply the Theory of Planned Behavior to predict behavioral intentions from attitudes, subjective norms, and perceived behavioral control, and identify intervention leverage points.
- [`grad-uppsala`](grad-uppsala/SKILL.md) — Apply the Uppsala Internationalization Model to analyze gradual foreign market entry based on psychic distance and experiential learning.

</details>

<details>
<summary><b><code>algo-</code></b> — Algorithms (62)</summary>

- [`algo-ad-bidding`](algo-ad-bidding/SKILL.md) — Implement and select ad bidding strategies from manual CPC to automated target-CPA and target-ROAS.
- [`algo-ad-budget`](algo-ad-budget/SKILL.md) — Optimize advertising budget allocation across campaigns using marginal returns analysis.
- [`algo-ad-ctr`](algo-ad-ctr/SKILL.md) — Build CTR prediction models for estimating ad click-through rates from features.
- [`algo-ad-gsp`](algo-ad-gsp/SKILL.md) — Implement Generalized Second Price auction for ad slot allocation and pricing.
- [`algo-ad-vcg`](algo-ad-vcg/SKILL.md) — Implement VCG mechanism for incentive-compatible ad slot allocation with truthful bidding.
- [`algo-blockchain-basics`](algo-blockchain-basics/SKILL.md) — Explain blockchain fundamentals including distributed ledger architecture, consensus mechanisms, and block structure.
- [`algo-blockchain-smart-contract`](algo-blockchain-smart-contract/SKILL.md) — Design and implement smart contracts as self-executing programmatic agreements on blockchain.
- [`algo-ecom-bm25`](algo-ecom-bm25/SKILL.md) — Implement BM25 ranking function for e-commerce product search relevance scoring.
- [`algo-ecom-ranking`](algo-ecom-ranking/SKILL.md) — Design multi-objective e-commerce product ranking combining relevance, conversion, and business metrics.
- [`algo-ecom-search`](algo-ecom-search/SKILL.md) — Optimize e-commerce search relevance across the full pipeline from query understanding to result presentation.
- [`algo-forecast-arima`](algo-forecast-arima/SKILL.md) — Build ARIMA models for time series forecasting with trend and seasonality decomposition.
- [`algo-forecast-ensemble`](algo-forecast-ensemble/SKILL.md) — Combine multiple forecasting models into ensemble predictions for improved accuracy.
- [`algo-forecast-exponential`](algo-forecast-exponential/SKILL.md) — Apply exponential smoothing methods for time series forecasting with weighted moving averages.
- [`algo-forecast-prophet`](algo-forecast-prophet/SKILL.md) — Build forecasting models with Meta's Prophet for business time series with holidays and changepoints.
- [`algo-hr-compensation`](algo-hr-compensation/SKILL.md) — Conduct compensation benchmarking analysis to position salaries against market data.
- [`algo-hr-matching`](algo-hr-matching/SKILL.md) — Implement Gale-Shapley stable matching algorithm for two-sided matching problems.
- [`algo-hr-turnover`](algo-hr-turnover/SKILL.md) — Build employee turnover prediction models to identify flight risk and retention drivers.
- [`algo-mfg-cpk`](algo-mfg-cpk/SKILL.md) — Calculate Cpk process capability index to assess whether a process meets specification requirements.
- [`algo-mfg-doe`](algo-mfg-doe/SKILL.md) — Design and analyze factorial experiments to identify significant process factors and optimize settings.
- [`algo-mfg-fmea`](algo-mfg-fmea/SKILL.md) — Conduct FMEA to systematically identify, prioritize, and mitigate potential failure modes.
- [`algo-mfg-spc`](algo-mfg-spc/SKILL.md) — Implement Statistical Process Control charts to monitor production process stability.
- [`algo-net-centrality`](algo-net-centrality/SKILL.md) — Calculate network centrality metrics to identify important nodes in graphs.
- [`algo-net-community`](algo-net-community/SKILL.md) — Implement Louvain community detection to discover densely connected groups in networks.
- [`algo-net-influence`](algo-net-influence/SKILL.md) — Solve the influence maximization problem to select optimal seed nodes for maximum information spread.
- [`algo-nlp-lda`](algo-nlp-lda/SKILL.md) — Implement LDA topic modeling to discover latent topics in document collections.
- [`algo-nlp-ner`](algo-nlp-ner/SKILL.md) — Implement Named Entity Recognition to identify and classify entities in text.
- [`algo-nlp-similarity`](algo-nlp-similarity/SKILL.md) — Calculate text similarity using lexical and semantic methods for matching and deduplication.
- [`algo-nlp-summarization`](algo-nlp-summarization/SKILL.md) — Implement text summarization using extractive and abstractive approaches.
- [`algo-price-bundle`](algo-price-bundle/SKILL.md) — Design bundle pricing strategies using pure bundling, mixed bundling, and consumer surplus analysis.
- [`algo-price-conjoint`](algo-price-conjoint/SKILL.md) — Run conjoint analysis to measure how product attributes drive consumer preferences and willingness to pay.
- [`algo-price-dynamic`](algo-price-dynamic/SKILL.md) — Implement dynamic pricing strategies that adjust prices in real-time based on demand, time, and competition.
- [`algo-price-elasticity`](algo-price-elasticity/SKILL.md) — Calculate price elasticity of demand to quantify how price changes affect sales volume.
- [`algo-price-van-westendorp`](algo-price-van-westendorp/SKILL.md) — Conduct Van Westendorp Price Sensitivity Meter analysis to identify acceptable price ranges.
- [`algo-rank-bayesian`](algo-rank-bayesian/SKILL.md) — Apply Bayesian averaging to rank items by combining observed ratings with prior expectations.
- [`algo-rank-elo`](algo-rank-elo/SKILL.md) — Implement Elo rating system to rank items or players from pairwise comparison outcomes.
- [`algo-rank-trueskill`](algo-rank-trueskill/SKILL.md) — Implement TrueSkill rating system for multiplayer and team-based competitive ranking.
- [`algo-rank-wilson`](algo-rank-wilson/SKILL.md) — Calculate Wilson Score confidence intervals for ranking items by positive proportion with sample size correction.
- [`algo-rec-cf`](algo-rec-cf/SKILL.md) — Implement collaborative filtering for recommendations based on user behavior patterns.
- [`algo-rec-content`](algo-rec-content/SKILL.md) — Implement content-based recommendation by matching item features to user preference profiles.
- [`algo-rec-hybrid`](algo-rec-hybrid/SKILL.md) — Design hybrid recommendation systems combining multiple strategies for improved accuracy.
- [`algo-rec-mf`](algo-rec-mf/SKILL.md) — Implement matrix factorization to decompose user-item interaction matrices into latent factor representations.
- [`algo-rec-session`](algo-rec-session/SKILL.md) — Implement session-based recommendation from short-term user behavior sequences without long-term profiles.
- [`algo-risk-altman-z`](algo-risk-altman-z/SKILL.md) — Calculate Altman Z-Score to predict corporate bankruptcy probability from financial ratios.
- [`algo-risk-benford`](algo-risk-benford/SKILL.md) — Apply Benford's Law to detect anomalies in numerical datasets by analyzing first-digit frequency distributions.
- [`algo-risk-credit`](algo-risk-credit/SKILL.md) — Build credit scoring models to predict default probability from borrower characteristics.
- [`algo-risk-var`](algo-risk-var/SKILL.md) — Calculate Value at Risk to estimate maximum portfolio loss at a given confidence level.
- [`algo-sc-bullwhip`](algo-sc-bullwhip/SKILL.md) — Analyze and mitigate the bullwhip effect where demand variability amplifies upstream in supply chains.
- [`algo-sc-eoq`](algo-sc-eoq/SKILL.md) — Calculate Economic Order Quantity to minimize total inventory cost (ordering + holding).
- [`algo-sc-newsvendor`](algo-sc-newsvendor/SKILL.md) — Solve the newsvendor problem for single-period ordering decisions under uncertain demand.
- [`algo-sc-routing`](algo-sc-routing/SKILL.md) — Solve vehicle routing problems to optimize delivery routes under capacity and time constraints.
- [`algo-sc-safety-stock`](algo-sc-safety-stock/SKILL.md) — Calculate safety stock levels to buffer against demand and lead time uncertainty.
- [`algo-seo-backlink`](algo-seo-backlink/SKILL.md) — Evaluate backlink quality using Domain Authority, Domain Rating, and trust metrics.
- [`algo-seo-content`](algo-seo-content/SKILL.md) — Execute content SEO strategy from keyword research through content planning, writing, and on-page optimization.
- [`algo-seo-crawl`](algo-seo-crawl/SKILL.md) — Implement a web crawler pipeline covering URL discovery, fetching, parsing, and storage.
- [`algo-seo-pagerank`](algo-seo-pagerank/SKILL.md) — Implement PageRank algorithm to compute web page importance scores using the random surfer model.
- [`algo-seo-schema`](algo-seo-schema/SKILL.md) — Implement Schema.org structured data markup in JSON-LD format for enhanced search results.
- [`algo-seo-technical`](algo-seo-technical/SKILL.md) — Optimize Core Web Vitals (LCP, INP, CLS) for better search rankings and user experience.
- [`algo-seo-tfidf`](algo-seo-tfidf/SKILL.md) — Implement TF-IDF scoring to measure term importance relative to a document corpus.
- [`algo-social-engagement`](algo-social-engagement/SKILL.md) — Calculate and benchmark social media engagement rates across platforms and variants.
- [`algo-social-influence`](algo-social-influence/SKILL.md) — Measure social media influence using engagement-weighted metrics beyond follower count.
- [`algo-social-sentiment`](algo-social-sentiment/SKILL.md) — Implement VADER sentiment analysis for social media text scoring.
- [`algo-social-virality`](algo-social-virality/SKILL.md) — Model viral spread dynamics using SIR/SIS/SEIR compartmental models.

</details>

<details>
<summary><b><code>biz-</code></b> — Business school frameworks (22)</summary>

- [`biz-4p-7p`](biz-4p-7p/SKILL.md) — Apply the Marketing Mix (4P/7P) framework to design tactical marketing decisions across Product, Price, Place, Promotion — plus People, Process, Physical Evidence for services.
- [`biz-ansoff`](biz-ansoff/SKILL.md) — Apply Ansoff Matrix to evaluate growth strategy options across market and product dimensions.
- [`biz-bcg-matrix`](biz-bcg-matrix/SKILL.md) — Apply BCG Growth-Share Matrix to analyze a product or business unit portfolio for resource allocation decisions.
- [`biz-blue-ocean`](biz-blue-ocean/SKILL.md) — Apply Blue Ocean Strategy to create uncontested market space through value innovation.
- [`biz-brand-positioning`](biz-brand-positioning/SKILL.md) — Develop brand positioning strategy including positioning statements, perceptual maps, and brand personality/archetype analysis.
- [`biz-breakeven`](biz-breakeven/SKILL.md) — Perform break-even analysis to determine the sales volume or revenue needed to cover all costs.
- [`biz-bsc`](biz-bsc/SKILL.md) — Apply the Balanced Scorecard (BSC) framework to translate strategy into measurable objectives across Financial, Customer, Internal Process, and Learning & Growth perspectives.
- [`biz-cac-ltv`](biz-cac-ltv/SKILL.md) — Calculate and analyze Customer Acquisition Cost (CAC) and Customer Lifetime Value (LTV) to evaluate unit economics and marketing efficiency.
- [`biz-customer-journey`](biz-customer-journey/SKILL.md) — Map and analyze the customer journey across Awareness, Consideration, Decision, Usage, and Advocacy stages.
- [`biz-dcf`](biz-dcf/SKILL.md) — Build Discounted Cash Flow (DCF) valuation models to estimate intrinsic value.
- [`biz-dupont`](biz-dupont/SKILL.md) — Apply DuPont Analysis to decompose Return on Equity (ROE) into profitability, efficiency, and leverage components.
- [`biz-financial-ratios`](biz-financial-ratios/SKILL.md) — Analyze financial health using ratio categories: profitability, liquidity, leverage, efficiency, and valuation.
- [`biz-lean-six-sigma`](biz-lean-six-sigma/SKILL.md) — Apply Lean and Six Sigma principles to eliminate waste and reduce process variation.
- [`biz-pestel`](biz-pestel/SKILL.md) — Apply PESTEL framework to scan the macro-environment across Political, Economic, Social, Technological, Environmental, and Legal dimensions.
- [`biz-porters-five-forces`](biz-porters-five-forces/SKILL.md) — Apply Porter's Five Forces framework to assess industry competitive dynamics and attractiveness.
- [`biz-pricing-strategy`](biz-pricing-strategy/SKILL.md) — Analyze and design pricing strategies including cost-plus, value-based, competitive, penetration, and skimming approaches with psychological pricing techniques.
- [`biz-stp`](biz-stp/SKILL.md) — Apply STP (Segmentation, Targeting, Positioning) framework for market strategy.
- [`biz-supply-chain`](biz-supply-chain/SKILL.md) — Analyze supply chain operations using the SCOR model across Plan, Source, Make, Deliver, and Return processes.
- [`biz-swot`](biz-swot/SKILL.md) — Conduct SWOT analysis with TOWS matrix for strategic planning.
- [`biz-toc`](biz-toc/SKILL.md) — Apply Theory of Constraints (TOC) to identify and manage system bottlenecks.
- [`biz-unit-economics`](biz-unit-economics/SKILL.md) — Analyze unit economics to evaluate per-unit profitability and business model scalability.
- [`biz-value-chain`](biz-value-chain/SKILL.md) — Apply Porter's Value Chain Analysis to identify competitive advantage sources within an organization's activities.

</details>

<details>
<summary><b><code>hum-</code></b> — Humanities / critical reasoning (9)</summary>

- [`hum-critical-thinking`](hum-critical-thinking/SKILL.md) — Apply structured critical thinking — identifying claims, evidence, reasoning chains, hidden assumptions, and logical fallacies — to evaluate or construct specific written arguments rigorously.
- [`hum-dialectics`](hum-dialectics/SKILL.md) — Apply Hegelian dialectics (thesis-antithesis-synthesis) to analyze contradictions and generate higher-order understanding.
- [`hum-discourse`](hum-discourse/SKILL.md) — Apply discourse analysis to examine how language constructs meaning, power relationships, and social reality in texts and communications.
- [`hum-ethics`](hum-ethics/SKILL.md) — Apply ethical frameworks — deontology, utilitarianism, virtue ethics, and justice theory — to analyze moral dilemmas and make principled decisions.
- [`hum-historical-analogy`](hum-historical-analogy/SKILL.md) — Use historical analogies to inform strategic decisions by identifying structural similarities and differences between past and present situations.
- [`hum-narrative`](hum-narrative/SKILL.md) — Apply narrative structure and storytelling techniques for brand, business, and communication contexts.
- [`hum-rhetoric`](hum-rhetoric/SKILL.md) — Apply classical rhetoric — Ethos, Pathos, Logos — to analyze persuasive communication and craft effective arguments.
- [`hum-socratic`](hum-socratic/SKILL.md) — Apply Socratic questioning — systematic inquiry via clarification, assumption-probing, evidence-testing, perspective-shifting, implication-tracing, and meta-questions — to coach learning or surface...
- [`hum-source-criticism`](hum-source-criticism/SKILL.md) — Evaluate source credibility using primary/secondary classification, internal/external criticism, triangulation, and misinformation detection.

</details>

<details>
<summary><b><code>tw-</code></b> — Taiwan-specific knowledge (38)</summary>

- [`tw-einvoice-guide`](tw-einvoice-guide/SKILL.md) — Implement Taiwan's e-invoice (電子發票) system including platform integration, B2B vs B2C formats, carrier consolidation, and tax filing reconciliation.
- [`tw-fintech-compliance`](tw-fintech-compliance/SKILL.md) — Navigate Taiwan fintech regulations including FSC oversight, electronic payment laws, VASP rules, AML/KYC requirements, and the regulatory sandbox.
- [`tw-healthcare-regulations`](tw-healthcare-regulations/SKILL.md) — Navigate Taiwan healthcare regulations including NHI system, medical device classification, drug registration, telemedicine rules, and health data protection.
- [`tw-manufacturing`](tw-manufacturing/SKILL.md) — Analyze Taiwan's manufacturing industry structure including semiconductor, electronics, machinery, and petrochemical sectors.
- [`tw-payment-integration`](tw-payment-integration/SKILL.md) — Integrate Taiwan payment service providers including credit card, ATM transfer, convenience store payment, and mobile wallets (LINE Pay, JKoPay).
- [`tw-retail-landscape`](tw-retail-landscape/SKILL.md) — Analyze Taiwan's retail industry including convenience stores, department stores, supermarkets, hypermarkets, and e-commerce with omnichannel trends.
- [`tw-startup-legal`](tw-startup-legal/SKILL.md) — Guide Taiwan company registration and legal setup including business entity selection, commercial registration, company registration, and tax ID application.
- [`tw-stock-analysis`](tw-stock-analysis/SKILL.md) — Analyze Taiwan-listed stocks using fundamental analysis including EPS, P/E ratio, dividend yield, and financial statement review.
- [`tw-tax-basics`](tw-tax-basics/SKILL.md) — Navigate Taiwan's tax system including corporate income tax (營所稅), business tax (營業稅), personal income tax, withholding obligations, and startup tax incentives.
- [`tw-ecom-analytics-benchmarks`](tw-ecom-analytics-benchmarks/SKILL.md) — Taiwan e-commerce benchmark ranges for CVR, ROAS, LTV, AOV, and repeat rate — for diagnosing performance gaps.
- [`tw-ecom-analytics-ga4`](tw-ecom-analytics-ga4/SKILL.md) — Implement GA4 Enhanced Ecommerce tracking for Taiwan e-commerce stores including event setup and conversion configuration.
- [`tw-ecom-channel-strategy`](tw-ecom-channel-strategy/SKILL.md) — Choose the right e-commerce platform mix for a Taiwan business — DTC (91APP, Shopline, Shopify) vs marketplace (momo, Shopee).
- [`tw-ecom-compliance-consumer`](tw-ecom-compliance-consumer/SKILL.md) — Comply with Taiwan consumer protection law (消保法) — 7-day 鑑賞期 scope, exceptions, and return/refund workflows.
- [`tw-ecom-compliance-cross-border`](tw-ecom-compliance-cross-border/SKILL.md) — Tax and regulatory compliance for cross-border e-commerce involving Taiwan — import duties, tariffs, and B2C filing rules.
- [`tw-ecom-compliance-pdpa`](tw-ecom-compliance-pdpa/SKILL.md) — E-commerce-specific PDPA (個資法) compliance — member consent at signup, cookie consent, and data protection practices.
- [`tw-ecom-compliance-product`](tw-ecom-compliance-product/SKILL.md) — Comply with Taiwan product regulations covering food (食安法), pharmaceuticals (藥事法), and cosmetics — registration and labeling requirements.
- [`tw-ecom-dtc-91app`](tw-ecom-dtc-91app/SKILL.md) — Integrate and operate 91APP in Taiwan e-commerce context via mcp-91app — listings, member system, and O2O features.
- [`tw-ecom-dtc-shopify-localization`](tw-ecom-dtc-shopify-localization/SKILL.md) — Run Shopify stores for Taiwan market — NT$ pricing, Traditional Chinese localization, and payment gateway integration.
- [`tw-ecom-dtc-shopline`](tw-ecom-dtc-shopline/SKILL.md) — Integrate and operate Shopline via mcp-shopline — product management, orders, and promotion setup.
- [`tw-ecom-invoice-carrier`](tw-ecom-invoice-carrier/SKILL.md) — Handle Taiwan e-invoice carriers — 手機條碼, 自然人憑證, member carriers, and 捐贈碼 donation flows.
- [`tw-ecom-invoice-ezpay`](tw-ecom-invoice-ezpay/SKILL.md) — Issue and manage Taiwan e-invoices via ezPay (加值服務中心) through mcp-ezpay-einvoice.
- [`tw-ecom-invoice-universalec`](tw-ecom-invoice-universalec/SKILL.md) — Issue Taiwan e-invoices via UniversalEC (汎宇電商) using mcp-universalec-e-invoice.
- [`tw-ecom-invoice-void`](tw-ecom-invoice-void/SKILL.md) — Void Taiwan e-invoices within the same bimonthly window, or issue allowances (折讓單).
- [`tw-ecom-logistics-cold-chain`](tw-ecom-logistics-cold-chain/SKILL.md) — Ship refrigerated / frozen products in Taiwan — 宅配通 冷藏 / 黑貓宅急便 低溫, packaging, and regulatory requirements.
- [`tw-ecom-logistics-cross-border`](tw-ecom-logistics-cross-border/SKILL.md) — Select carriers and manage cross-border shipping operations for Taiwan export e-commerce.
- [`tw-ecom-logistics-cvs`](tw-ecom-logistics-cvs/SKILL.md) — Ship via Taiwan convenience store pickup (7-11 賣貨便 / 全家 / 萊爾富 / OK) — store selection and cash-on-delivery setup.
- [`tw-ecom-logistics-home`](tw-ecom-logistics-home/SKILL.md) — Ship via Taiwan home delivery carriers — 黑貓宅急便, 宅配通, 新竹物流, 郵局 — pricing rules and delivery SLA.
- [`tw-ecom-marketplace-momo`](tw-ecom-marketplace-momo/SKILL.md) — Operate on momo購物網 — listing approval workflow, price-matching rules, and advertising.
- [`tw-ecom-marketplace-shopee`](tw-ecom-marketplace-shopee/SKILL.md) — Operate a Shopee Taiwan store — listings, promotions, flash sales, and SIP (Shopee Preferred) qualification.
- [`tw-ecom-operations-customer-service`](tw-ecom-operations-customer-service/SKILL.md) — Taiwan e-commerce customer service — LINE / Messenger / email / phone channel mix and response SOPs.
- [`tw-ecom-operations-line-oa`](tw-ecom-operations-line-oa/SKILL.md) — Run CRM and member retention via LINE Official Account — broadcast cost model, segmentation, and Messaging API.
- [`tw-ecom-operations-pricing`](tw-ecom-operations-pricing/SKILL.md) — Set prices for Taiwan e-commerce — 含稅 vs 未稅 presentation, price-ending conventions, and marketplace price-match strategy.
- [`tw-ecom-operations-promotion`](tw-ecom-operations-promotion/SKILL.md) — Run Taiwan e-commerce promotional campaigns — 雙11, 618, 年中慶, 雙12, 週年慶, 母親節 — discount design and ROI calculation.
- [`tw-ecom-payment-dispute`](tw-ecom-payment-dispute/SKILL.md) — Handle Taiwan e-commerce payment disputes — credit card chargebacks, CVS cash-on-delivery disputes, and appeal workflows.
- [`tw-ecom-payment-ecpay`](tw-ecom-payment-ecpay/SKILL.md) — Integrate 綠界 (ECPay) for Taiwan e-commerce — credit card, ATM, CVS code, and cash-on-delivery.
- [`tw-ecom-payment-jkopay`](tw-ecom-payment-jkopay/SKILL.md) — Integrate 街口支付 (JKOPay) for Taiwan e-commerce — web/app flow and JKO 幣 rewards.
- [`tw-ecom-payment-newebpay`](tw-ecom-payment-newebpay/SKILL.md) — Integrate NewebPay (藍新金流) for Taiwan e-commerce via mcp-newebpay — multi-method payment setup.
- [`tw-ecom-payment-tappay`](tw-ecom-payment-tappay/SKILL.md) — Integrate TapPay for Taiwan e-commerce — Web/iOS/Android SDK, 3DS 2.0, and recurring billing.

</details>

<details>
<summary><b><code>ecom-</code></b> — E-commerce practical (7)</summary>

- [`ecom-analytics`](ecom-analytics/SKILL.md) — Analyze e-commerce performance using GA4 metrics, conversion funnel analysis, and key e-commerce KPIs.
- [`ecom-conversational`](ecom-conversational/SKILL.md) — Design conversational commerce experiences across messaging platforms including chatbot flows, product cards, and conversion strategies.
- [`ecom-inventory-health`](ecom-inventory-health/SKILL.md) — Analyze inventory health using turnover ratios, ABC classification, safety stock calculations, and stockout vs overstock diagnostics.
- [`ecom-multilingual-listing`](ecom-multilingual-listing/SKILL.md) — Optimize multilingual product listings for international e-commerce including SEO localization, machine translation workflows, and cultural adaptation.
- [`ecom-promo-roi`](ecom-promo-roi/SKILL.md) — Calculate and analyze promotional ROI including incremental sales lift, margin impact, and promo type comparison.
- [`ecom-rfm-analysis`](ecom-rfm-analysis/SKILL.md) — Perform RFM (Recency, Frequency, Monetary) customer segmentation from transaction data.
- [`ecom-sea-strategy`](ecom-sea-strategy/SKILL.md) — Develop e-commerce strategy for Southeast Asian markets including platform selection, payment infrastructure, logistics challenges, and localization requirements.

</details>

<details>
<summary><b><code>econ-</code></b> — Economics fundamentals (6)</summary>

- [`econ-behavioral`](econ-behavioral/SKILL.md) — Apply behavioral economics concepts including bounded rationality, prospect theory, mental accounting, and nudge theory to analyze decision-making biases.
- [`econ-business-cycle`](econ-business-cycle/SKILL.md) — Analyze business cycle phases (expansion, peak, contraction, trough) and their implications for business strategy and policy response.
- [`econ-game-theory`](econ-game-theory/SKILL.md) — Apply basic game theory concepts including Nash equilibrium, dominant strategies, and the Prisoner's Dilemma to analyze strategic interactions.
- [`econ-macro-indicators`](econ-macro-indicators/SKILL.md) — Interpret macroeconomic indicators including GDP, inflation, unemployment, interest rates, and exchange rates to assess economic health and predict trends.
- [`econ-market-structure`](econ-market-structure/SKILL.md) — Analyze market structures across perfect competition, monopolistic competition, oligopoly, and monopoly to predict firm behavior and market outcomes.
- [`econ-supply-demand`](econ-supply-demand/SKILL.md) — Apply supply and demand analysis to explain price determination, market equilibrium, and the effects of policy interventions.

</details>

<details>
<summary><b><code>meta-</code></b> — Interdisciplinary mental models (6)</summary>

- [`meta-decision-analysis`](meta-decision-analysis/SKILL.md) — Apply structured decision analysis using decision matrices, decision trees, expected value, and multi-criteria decision analysis (MCDA).
- [`meta-first-principles`](meta-first-principles/SKILL.md) — Apply first principles thinking to break problems down to fundamental truths and reason up from there.
- [`meta-mental-models`](meta-mental-models/SKILL.md) — Apply a latticework of mental models from multiple disciplines to improve decision quality.
- [`meta-scenario-planning`](meta-scenario-planning/SKILL.md) — Conduct scenario planning to prepare for multiple plausible futures using driving forces, uncertainty axes, and the 2x2 scenario matrix.
- [`meta-structured-problem`](meta-structured-problem/SKILL.md) — Apply structured problem-solving using MECE principle, issue trees, hypothesis-driven approach, and the Pyramid Principle.
- [`meta-systems-thinking`](meta-systems-thinking/SKILL.md) — Apply systems thinking — causal loop diagrams, stock-and-flow models, system archetypes, and leverage-point analysis — to organizational, economic, or social problems where feedback loops, delays, ...

</details>

<details>
<summary><b><code>ops-</code></b> — Business operations (6)</summary>

- [`ops-business-model-canvas`](ops-business-model-canvas/SKILL.md) — Apply the Business Model Canvas (BMC) to map and evaluate business models across nine building blocks.
- [`ops-contract-review`](ops-contract-review/SKILL.md) — Review business contracts for risk identification including liability clauses, IP ownership, termination terms, and payment conditions.
- [`ops-meeting-minutes`](ops-meeting-minutes/SKILL.md) — Create structured meeting minutes with decisions, action items, and follow-up tracking.
- [`ops-negotiation`](ops-negotiation/SKILL.md) — Apply principled negotiation using BATNA, ZOPA, and the Harvard method to prepare for and conduct negotiations.
- [`ops-okr-planning`](ops-okr-planning/SKILL.md) — Design and implement OKR (Objectives and Key Results) for goal-setting and strategic alignment across organizational levels.
- [`ops-pitch-deck`](ops-pitch-deck/SKILL.md) — Structure and write investor pitch decks covering problem, solution, market, business model, traction, team, and financials.

</details>

<details>
<summary><b><code>law-</code></b> — Legal frameworks (5)</summary>

- [`law-contract`](law-contract/SKILL.md) — Analyze contract fundamentals including formation requirements (offer, acceptance, consideration), essential clauses, and common risk areas.
- [`law-gdpr-pdpa`](law-gdpr-pdpa/SKILL.md) — Analyze data privacy compliance requirements under GDPR, Taiwan's Personal Data Protection Act (PDPA), and related regulations.
- [`law-ip`](law-ip/SKILL.md) — Analyze intellectual property rights across patents, trademarks, copyrights, and trade secrets.
- [`law-irac`](law-irac/SKILL.md) — Apply IRAC (Issue, Rule, Application, Conclusion) method for structured legal analysis.
- [`law-labor`](law-labor/SKILL.md) — Analyze Taiwan labor law fundamentals under the Labor Standards Act including working hours, overtime, leave, and termination rules.

</details>

<details>
<summary><b><code>pr-</code></b> — PR & brand communications (5)</summary>

- [`pr-crisis-communication`](pr-crisis-communication/SKILL.md) — Manage crisis communication across prevention, response, and recovery phases using SCCT theory and crisis statement frameworks.
- [`pr-crisis-response`](pr-crisis-response/SKILL.md) — Manage PR crises using classification, golden hour response, crisis statement templates (3C framework), and reputation recovery planning.
- [`pr-media-monitoring`](pr-media-monitoring/SKILL.md) — Set up and conduct media monitoring to track brand mentions, sentiment, and share of voice across news, social, and online channels.
- [`pr-press-release`](pr-press-release/SKILL.md) — Write effective press releases using inverted pyramid structure, headline best practices, and media distribution strategy.
- [`pr-social-copywriting`](pr-social-copywriting/SKILL.md) — Write platform-optimized social media copy for Instagram, Facebook, LinkedIn, and X/Twitter with hooks, CTAs, and hashtag strategies.

</details>

<details>
<summary><b><code>cs-</code></b> — Customer service (4)</summary>

- [`cs-analytics`](cs-analytics/SKILL.md) — Measure and optimize customer service performance using CSAT, NPS, CES, First Contact Resolution, and text mining on support tickets.
- [`cs-chatbot-design`](cs-chatbot-design/SKILL.md) — Design conversational AI chatbots including intent recognition, slot filling, dialogue flow, and response generation.
- [`cs-notification-strategy`](cs-notification-strategy/SKILL.md) — Design push notification and messaging strategies including channel selection, timing optimization, personalization, and fatigue management.
- [`cs-sop`](cs-sop/SKILL.md) — Design customer service operations including tiered support (L1/L2/L3), response templates, SLA definitions, escalation procedures, and complaint handling.

</details>

<details>
<summary><b><code>data-</code></b> — Data analytics (4)</summary>

- [`data-cohort-analysis`](data-cohort-analysis/SKILL.md) — Conduct cohort analysis to track user behavior over time, build retention matrices, and compare cohort performance.
- [`data-dashboard-design`](data-dashboard-design/SKILL.md) — Design effective data dashboards with proper KPI hierarchy, chart type selection, and interactive features.
- [`data-financial-analysis`](data-financial-analysis/SKILL.md) — Interpret the three core financial statements (income statement, balance sheet, cash flow statement) to assess business health and performance.
- [`data-sql-optimization`](data-sql-optimization/SKILL.md) — Optimize SQL query performance using EXPLAIN analysis, indexing strategies, and common anti-pattern fixes.

</details>

<details>
<summary><b><code>mfg-</code></b> — Manufacturing (4)</summary>

- [`mfg-oee-analysis`](mfg-oee-analysis/SKILL.md) — Calculate and diagnose Overall Equipment Effectiveness (OEE) by decomposing into Availability, Performance, and Quality rates.
- [`mfg-predictive-maintenance`](mfg-predictive-maintenance/SKILL.md) — Design predictive maintenance strategies using sensor data, ML models for remaining useful life (RUL), and the P-F curve framework.
- [`mfg-production-planning`](mfg-production-planning/SKILL.md) — Design production plans using MPS (Master Production Schedule), MRP (Material Requirements Planning), and capacity planning.
- [`mfg-supplier-scorecard`](mfg-supplier-scorecard/SKILL.md) — Evaluate and manage suppliers using weighted scorecards across quality, delivery, price, and service dimensions.

</details>

<details>
<summary><b><code>mkt-</code></b> — Digital marketing (4)</summary>

- [`mkt-ab-testing`](mkt-ab-testing/SKILL.md) — Design and execute marketing A/B tests for landing pages, email campaigns, ad creatives, and pricing with proper test design and result analysis.
- [`mkt-ad-optimization`](mkt-ad-optimization/SKILL.md) — Optimize digital advertising campaigns across Google Ads, Meta Ads, and LINE LAP including bidding strategies, audience targeting, creative testing, and ROAS optimization.
- [`mkt-content-calendar`](mkt-content-calendar/SKILL.md) — Build and manage content calendars for multi-platform content marketing including editorial planning, content type allocation, and team workflow.
- [`mkt-seo-audit`](mkt-seo-audit/SKILL.md) — Conduct technical and on-page SEO audits covering crawlability, site speed, mobile-friendliness, and content optimization.

</details>

<details>
<summary><b><code>soc-</code></b> — Social science (7)</summary>

- [`soc-cialdini`](soc-cialdini/SKILL.md) — Apply Cialdini's six principles of persuasion — Reciprocity, Commitment/Consistency, Social Proof, Liking, Authority, and Scarcity — to analyze or design influence strategies.
- [`soc-cognitive-bias`](soc-cognitive-bias/SKILL.md) — Identify and analyze cognitive biases including confirmation bias, anchoring, availability heuristic, and sunk cost fallacy in decision-making contexts.
- [`soc-innovation-diffusion`](soc-innovation-diffusion/SKILL.md) — Apply Rogers' Diffusion of Innovations theory to analyze how new products, ideas, or technologies spread through populations.
- [`soc-policy-analysis`](soc-policy-analysis/SKILL.md) — Conduct structured policy analysis including problem definition, alternative evaluation, and evidence-based recommendation.
- [`soc-social-network`](soc-social-network/SKILL.md) — Apply social network analysis concepts including nodes, ties, centrality, structural holes, and strong/weak ties to map and analyze relationship structures.
- [`soc-stakeholder`](soc-stakeholder/SKILL.md) — Conduct stakeholder analysis using identification, Power-Interest matrix classification, and influence strategy development.
- [`soc-user-research`](soc-user-research/SKILL.md) — Design and conduct user research using interviews, focus groups, surveys, and field observation.

</details>

<details>
<summary><b><code>stat-</code></b> — Statistical methodology (4)</summary>

- [`stat-ab-testing`](stat-ab-testing/SKILL.md) — Design and analyze A/B tests with proper statistical methodology including sample size calculation, randomization, frequentist and Bayesian approaches, and sequential testing.
- [`stat-causal-inference`](stat-causal-inference/SKILL.md) — Apply causal inference methods — counterfactual framework, instrumental variables, propensity score matching, and difference-in-differences — to estimate causal effects from observational data.
- [`stat-eda`](stat-eda/SKILL.md) — Conduct Exploratory Data Analysis (EDA) using descriptive statistics, visualizations, and data quality checks.
- [`stat-hypothesis-testing`](stat-hypothesis-testing/SKILL.md) — Conduct statistical hypothesis testing including null/alternative hypothesis formulation, p-values, Type I/II errors, and test statistic selection.

</details>

<details>
<summary><b><code>tech-</code></b> — General tech (4)</summary>

- [`tech-api-integration`](tech-api-integration/SKILL.md) — Guide REST API integration including HTTP methods, authentication, error handling, and rate limiting.
- [`tech-data-pipeline`](tech-data-pipeline/SKILL.md) — Design data pipelines covering ETL vs ELT architectures, data source integration, scheduling, quality checks, and warehouse design.
- [`tech-mcp-server-dev`](tech-mcp-server-dev/SKILL.md) — Build MCP (Model Context Protocol) servers including tool definition, schema design, authentication, error handling, and Claude Code integration.
- [`tech-prompt-engineering`](tech-prompt-engineering/SKILL.md) — Debug and harden production LLM prompts — handle prompt injection, output format drift, instruction forgetting in long contexts, and cross-model portability issues.

</details>

<details>
<summary><b><code>ux-</code></b> — Design / UX methodology (4)</summary>

- [`ux-design-thinking`](ux-design-thinking/SKILL.md) — Apply Design Thinking's five stages — Empathize, Define, Ideate, Prototype, Test — to solve user-centered problems.
- [`ux-heuristic`](ux-heuristic/SKILL.md) — Conduct heuristic evaluation of user interfaces using Nielsen's 10 usability principles.
- [`ux-jtbd`](ux-jtbd/SKILL.md) — Apply Jobs to Be Done (JTBD) framework to understand customer motivation through functional, emotional, and social jobs.
- [`ux-lean-startup`](ux-lean-startup/SKILL.md) — Apply Lean Startup methodology — Build-Measure-Learn loop, MVP, validated learning, and pivot decisions.

</details>

<details>
<summary><b><code>fin-</code></b> — Finance practical (2)</summary>

- [`fin-earnings-summary`](fin-earnings-summary/SKILL.md) — Summarize and analyze earnings calls (法說會) including financial highlights, management commentary, guidance, and analyst Q&A key takeaways.
- [`fin-modeling`](fin-modeling/SKILL.md) — Build three-statement financial models (Income Statement, Balance Sheet, Cash Flow) with revenue forecasting, assumption management, and scenario analysis.

</details>

<details>
<summary><b><code>xborder-</code></b> — Cross-border commerce (2)</summary>

- [`xborder-logistics`](xborder-logistics/SKILL.md) — Design cross-border logistics strategies including direct mail, overseas warehousing, and bonded warehouse models for international e-commerce.
- [`xborder-sea-entry`](xborder-sea-entry/SKILL.md) — Plan Southeast Asia market entry including mode selection, regulatory requirements, cultural research, and go-to-market timeline.

</details>

<details>
<summary><b><code>med-</code></b> — Mass communication / journalism (1)</summary>

- [`med-news-reporter`](med-news-reporter/SKILL.md) — Turn user-supplied raw material (transcripts, event notes, data, direct quotes) into a publishable news piece across four types — breaking news, investigative report, feature, and op-ed — with mandatory media-ethics and media-literacy self-checks.

</details>

## Skill Structure

Every `SKILL.md` follows a consistent template:

```markdown
---
name: "{category}-{skill-name}"
description: "[imperative WHAT + WHEN, < 1024 chars, no XML brackets]"
metadata:
  category: "WP-XX Topic Label"
  tags: [...]
---

# {Skill Display Name}

## Overview / Framework
## When to Use (and When NOT to Use)
## Methodology (Phase-Gate or Hub-and-Spoke pattern)
## IRON LAW: {non-obvious constraint}
## Output Format
## Gotchas
## Scripts (if applicable)
## References
```

## Deterministic Scripts

20 skills currently ship Python scripts (pure stdlib, no external dependencies) for calculations that LLMs frequently get wrong:

- **Finance**: `biz-cac-ltv`, `biz-breakeven`, `biz-dcf`, `biz-dupont`, `biz-financial-ratios`, `biz-unit-economics`, `grad-capm`, `fin-modeling`*
- **Risk / Stats**: `algo-risk-altman-z`, `algo-risk-var`*, `mkt-ab-testing`, `algo-mfg-cpk`
- **Supply chain**: `algo-sc-eoq`, `algo-sc-safety-stock`, `algo-sc-newsvendor`
- **Ranking**: `algo-rank-wilson`, `algo-rank-elo`, `algo-rank-bayesian`
- **E-commerce**: `ecom-rfm-analysis`, `algo-price-elasticity`
- **Search**: `algo-seo-tfidf`, `algo-ecom-bm25`

Each script supports `--help`, `--input <json>`, and `--verify` (built-in self-test). Scripts emit JSON to stdout for downstream consumption.

```bash
# Example
python ecom-rfm-analysis/scripts/rfm_score.py --input customers.json
python biz-cac-ltv/scripts/cac_ltv.py --marketing-cost 100000 --new-customers 500 \
  --arpu 50 --gross-margin 0.70 --monthly-churn 0.05
```

## Design Principles

1. **Iron Law**: every skill defines one non-obvious constraint that an agent would otherwise violate
2. **Hub-and-Spoke**: SKILL.md is concise (< 200 lines); heavy content offloaded to `references/`
3. **Phase-Gate** (algorithms): explicit steps with verification gates between
4. **Concrete Verification**: examples must be exact and computable, not approximate ranges
5. **No Over-Teaching**: assume the agent knows fundamentals; focus on what it would get WRONG

See [`AGENTS.md`](AGENTS.md) for full design rules and quality standards.

## Status

| Phase | Status |
|-------|:-:|
| Phase 1: Generate 263 skills across 4 sections | ✅ |
| Phase 1.5: Auto lint (frontmatter, length, IRON LAW) | ✅ 293/293 |
| Phase 1.7: With/without skill eval (4 samples) | ✅ 4/4 with_skill wins |
| Phase 2-3: Quality audit (28 sampled) | ✅ 14 PASS / 13 MINOR / 1 MAJOR |
| Phase 3.5: P0 + P1 remediation | ✅ |
| Phase 4: Description optimization (phantom trigger) | ✅ |
| Tier 1 + 2 deterministic scripts (20 total) | ✅ All `--verify` pass |
| Plugin bundling (Phase 5) | 🟡 In planning ([see `TODO.md`](TODO.md)) |

## Related Repositories

- [`asgard-ai-platform/skill-template`](https://github.com/asgard-ai-platform/skill-template) — Plugin template for creating new coding agent plugins
- [`asgard-ai-platform/mcp-*`](https://github.com/orgs/asgard-ai-platform/repositories?q=mcp-) — MCP servers (data ingredients)
- Plugin bundles (forthcoming) — Curated combinations of skills + MCPs for specific personas

## Domain Navigation

Curated skill indexes for specific workflows live in [`docs/domains/`](docs/domains/):

- [`tw-ecommerce.md`](docs/domains/tw-ecommerce.md) — Taiwan e-commerce (platform, payment, logistics, invoice, compliance, operations, analytics)

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Before submitting a new skill, read [`AGENTS.md`](AGENTS.md) for directory layout and quality standards.

## License

MIT License. See [LICENSE](LICENSE).
