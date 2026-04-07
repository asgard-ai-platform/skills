# Pending Work — Asgard Skills

Tracking deferred items by priority. Updated 2026-04-07 after the rename + repo split.

---

## 🟡 Medium Priority — Skill Quality Improvements

### 1. QA Phase 2-3 P2/P3 Remediation

From the 28-skill quality audit (`eval-workspace/qa-report.md` in skill-template before split — recreate here if needed).

**Weak Iron Laws** (5 skills): some Iron Laws are truisms ("be specific", "look at the data first") instead of non-obvious constraints.

- `mkt-content-calendar`
- `xborder-logistics`
- `hum-socratic`
- `meta-systems-thinking`
- `stat-eda`

**Test for a good Iron Law**: "Would a competent agent violate this rule WITHOUT being warned?" If no, the rule is too obvious and should be sharpened.

**Over-teaching in 大學部 methodology skills**: skills explain basic concepts (Nash equilibrium, IRAC steps, EDA workflow) the agent already knows. Compress definitions and expand gotchas/error-modes.

- `econ-game-theory` — over-teaches dominant strategy / NE basics; missing mixed-strategy gotcha
- `soc-cognitive-bias` — bias catalog too long; offload to references/
- `hum-socratic` — over-teaches question types; missing "leading questions" anti-pattern
- `meta-systems-thinking` — over-teaches feedback loop definitions
- `stat-eda` — over-teaches workflow; missing Simpson's paradox, data leakage gotchas

**Populate `examples/` directories** (systemic): currently every `examples/` directory exists only with `.gitignore`. CLAUDE.md says examples are "always required." Inline examples in SKILL.md partially compensate but the standalone files are still missing.

### 2. Strict eval of Tier 1 + 2 scripts

The initial Tier 1 eval (5 skills × with/without script) showed all 5 without_script agents got correct answers manually. The test set was too clean. **Need a harder eval** to actually measure script value:

- **Large datasets** (1000+ rows where hand calculation is impractical)
- **Ambiguous inputs** requiring judgment on which formula/variant to use
- **Messy real data** (CSVs with missing fields, date ranges, etc.)
- **Edge cases** (division by zero, negative values, extreme parameters)
- **Stochastic noise** to expose LLM session-to-session variance

Outcome should inform whether to invest in Tier 3 scripts.

### 3. Tier 3 Scripts (heavier dependencies)

Scripts that require non-stdlib libraries:

- **Needs numpy/networkx/statsmodels:**
  - `algo-seo-pagerank` (sparse matrix iteration)
  - `algo-net-centrality` (networkx for graph metrics)
  - `algo-net-community` (Louvain via python-louvain)
  - `algo-forecast-arima` (statsmodels)
  - `algo-forecast-prophet` (Meta Prophet)
  - `algo-rank-trueskill` (Bayesian message-passing)
- **Needs lexicon data:**
  - `algo-social-sentiment` (VADER lexicon)

Decision gating: complete Tier 1+2 strict eval first to confirm scripts add value on messy data; only then invest in Tier 3.

---

## 🔴 High Priority — Phase 5: Plugin Bundling (Paused)

### Plugin Bundle Strategy

`Plugin = Persona × (Data + Methodology)`. MCPs and Skills are raw ingredients. A plugin is a curated bundle of MCPs + ~10-20 skills targeting ONE specific user workflow. Value comes from CURATION, not completeness.

### Available raw materials

**MCPs (8 under asgard-ai-platform, excluding mcp-template and asgard-mcp-server):**

| MCP | Tools | Domain |
|-----|------:|--------|
| `mcp-tdcc` | 8 | Taiwan TDCC securities custody open data |
| `mcp-tw-ly` | — | Taiwan Legislative Yuan open data |
| `mcp-twfood` | 6 | Taiwan agricultural wholesale market data |
| `mcp-shopline` | 19 | Shopline e-commerce platform |
| `mcp-91app` | 17 | 91app e-commerce platform |
| `mcp-ezpay-einvoice` | 7 | Taiwan ezPay e-invoice |
| `mcp-universalec-e-invoice` | 27 | Universal EC e-invoice |
| `mcp-newebpay` | 8 | NewebPay payment gateway |

(`mcp-cyberbiz` is an empty repo — skip.)

**Skills:** 263 in this repo across 21 categories.

### 4 proposed plugin bundles (personas)

#### Plugin 1: `asgard-ecommerce-analyst` — Taiwan SMB e-commerce owner

- **MCPs**: `mcp-shopline` + `mcp-91app` + `mcp-newebpay` + `mcp-ezpay-einvoice`
- **Skills (~15)**: `ecom-rfm-analysis`, `data-cohort-analysis`, `ecom-analytics`, `ecom-inventory-health`, `biz-unit-economics`, `biz-cac-ltv`, `biz-pricing-strategy`, `ecom-promo-roi`, `algo-rec-cf`, `algo-price-elasticity`, `algo-forecast-arima`, `tw-einvoice-guide`, `tw-payment-integration`, `tw-tax-basics`

#### Plugin 2: `asgard-taiwan-stock-analyst` — Taiwan stock researcher ⭐ (start here, simplest)

- **MCPs**: `mcp-tdcc`
- **Skills (~12)**: `tw-stock-analysis`, `fin-earnings-summary`, `biz-dcf`, `biz-financial-ratios`, `biz-dupont`, `data-financial-analysis`, `fin-modeling`, `grad-capm`, `grad-fama-french`, `grad-emh`, `grad-behavioral-finance`

#### Plugin 3: `asgard-taiwan-policy-researcher` — Policy researcher

- **MCPs**: `mcp-tw-ly` + `mcp-twfood`
- **Skills (~15)**: `grad-policy-streams`, `grad-governance`, `soc-policy-analysis`, `grad-case-study`, `grad-grounded-theory`, `grad-narrative`, `grad-systematic-review`, `grad-mixed-methods`, `hum-source-criticism`, `hum-discourse`, `hum-historical-analogy`, `hum-critical-thinking`, `meta-systems-thinking`, `meta-scenario-planning`

#### Plugin 4: `asgard-taiwan-finance-ops` — Taiwan finance/accounting ops

- **MCPs**: `mcp-ezpay-einvoice` + `mcp-universalec-e-invoice` + `mcp-newebpay`
- **Skills (~10)**: `tw-einvoice-guide`, `tw-tax-basics`, `tw-fintech-compliance`, `tw-startup-legal`, `data-financial-analysis`, `biz-financial-ratios`, `biz-breakeven`, `ops-contract-review`, `law-contract`, `ops-meeting-minutes`

### Repo layout decision: Option B → then C

**Phase 5a (prototype):** Add `bundles/` directory in `skill-template` (NOT this repo). Each bundle is a YAML manifest listing its MCPs + curated skills (referencing this repo by path or git submodule). Low risk, fast validation of curation logic.

**Phase 5b (production):** Write a build script that generates independent plugin repos from bundle YAML files. Publish as separate `asgard-<plugin-name>` repos.

### Recommended order

1. Plugin 2 (stock) — simplest (1 MCP + 12 skills), validate the flow
2. Plugin 1 (e-commerce) — most complex (4 MCPs + 15 skills), real-world case
3. Plugin 3, 4 — follow

### Why paused

The user wanted to first improve skills themselves (deterministic scripts, repo split, naming cleanup). Resume Phase 5 after this housekeeping.

---

## ⚪ Low Priority / Watch List

### 5. Phase 4 residual phantom trigger risks

QA validation flagged 3 low-residual risks but they were within acceptable range:

- `hum-socratic` — could over-trigger on "what questions should I ask" (non-coaching brainstorming)
- `meta-systems-thinking` — could over-trigger on "this bug keeps coming back" (non-systems context)
- `hum-critical-thinking` — could over-trigger on "poke holes in my travel plan"

### 6. Subagent sandbox limitation

In Phase 1.7 and Tier 1 evals, 4/5 with_script subagents could not execute Bash. They fell back to reading the script source and simulating the output. This is a Claude Code subagent sandbox limitation, not a skill problem. When publishing plugins, ensure target environments allow Python execution.

---

## Suggested next-step order

| Order | Item | Effort |
|-------|------|--------|
| 1 | Phase 5a: 4 bundle YAMLs (in `skill-template` repo) | Small (~1 hr) |
| 2 | Phase 5a: Plugin 2 (Taiwan stock) prototype | Medium |
| 3 | Strict eval of Tier 1+2 scripts on messy data | Medium |
| 4 | QA P2-P3 fixes (if strict eval shows scripts need help) | Medium |
| 5 | Phase 5b: build script + publish independent plugin repos | Large |
| 6 | Tier 3 scripts (only if plugin scenarios need them) | Large |
