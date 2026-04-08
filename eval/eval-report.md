# Tier 1 + 2 Strict Eval — Results

_Last updated: 2026-04-09. Model: `claude-sonnet-4-6`._

This report covers **two distinct eval methodologies** run against the same 20
Tier 1+2 scripts. Read them in order — the second supersedes the first as the
primary measure of skill value, but both surface useful signals.

## Methodology A: Script ablation (run 2026-04-07)

**Comparison**: `with_script` (SKILL.md + script) vs `without_script` (SKILL.md,
no script). Both arms see the full methodology in the prompt; only script
execution capability differs. This answers: **"given a skill exists, does
bundling a Python script add marginal value?"**

### Methodology A results

| Verdict | Count | Skills |
|---------|------:|--------|
| correctness ⭐ | 3 | `algo-risk-altman-z`, `algo-ecom-bm25`, `biz-financial-ratios` |
| speed | 5 | `algo-rank-wilson`, `biz-dcf`, `algo-rank-elo`, `mkt-ab-testing`, `ecom-rfm-analysis` |
| neither | 12 | rest |

**Hit rate**: 8/20 = 40%. Caveat: the old case prompts contained explicit
methodology hints ("use the Z'' variant", "Q\* is NOT mean", "use 5-factor
DuPont"), which leaked into the without_script arm and understated the value of
SKILL.md methodology. Methodology B below fixes this.

## Methodology B: Skill ablation (run 2026-04-09) — primary

**Comparison**: `with_skill` (SKILL.md inlined + Bash+Read + repo access) vs
`without_skill` (vanilla LLM, no methodology, no tools, no repo). Case prompts
rewritten in raw "user voice" — no formula hints, no trap warnings, no variant
directives. This answers the more fundamental question: **"does the skill add
value over a vanilla LLM at all?"**

### Methodology B results (final)

| Skill | Case verdict | Notes |
|-------|--------------|-------|
| `algo-risk-altman-z` | **correctness** ⭐ | SaaS firm scenario: with_skill picks Z'' correctly; without_skill defaults to original Z. |
| `algo-price-elasticity` | **correctness** ⭐ | arc-elasticity-midpoint: without_skill applies wrong formula. |
| `algo-rank-elo` | **correctness** ⭐ | 2/3 scenarios discriminate: underdog-beats-favorite, elite-upset-low-k. Vanilla LLM errors on K-factor application. |
| `algo-sc-eoq` | **correctness** ⭐ | holding-cost-from-percentage: vanilla LLM mis-parses the "20% of unit cost" quote. |
| `algo-seo-tfidf` | **correctness** ⭐ | 3-doc TF-IDF: without_skill uses a different IDF smoothing. |
| `ecom-rfm-analysis` | **both** ⭐⭐ | 10-customer segmentation: vanilla LLM fails AND is 9.1× slower (332s hand-computing quantiles). Strongest combined signal. |
| `biz-dcf` | **speed** | mixed-tw-units 3.5×, 30yr-decimal-noise 7.8×. Vanilla LLM computes correctly but spends 80-350s. |
| `mkt-ab-testing` | **speed** | 2/3 scenarios 3.8×–11×. Two-proportion z-test arithmetic is slow by hand. |
| `algo-sc-newsvendor` | **speed** | high-margin-order-above-mean: 6.8× (vanilla LLM spent 195s). |
| `algo-mfg-cpk` | neither | 0/3 discriminating. |
| `algo-rank-bayesian` | neither | 0/3 discriminating. |
| `algo-rank-wilson` | neither | 0/4 discriminating (vanilla LLM handles Wilson score well). |
| `algo-sc-safety-stock` | neither | 0/2 discriminating. |
| `biz-breakeven` | neither | 0/2. |
| `biz-cac-ltv` | neither | 0/3. |
| `biz-dupont` | neither | 0/2. |
| `biz-financial-ratios` | neither | 0/1 — this round vanilla LLM picked total_liabilities definition correctly; earlier runs showed non-determinism on this one. |
| `biz-unit-economics` | neither | 0/1. |
| `grad-capm` | neither | 0/2. |
| `algo-ecom-bm25` | **inconclusive** | with_skill also fails on top_score by 3.5% (1.978 vs 2.048) because the SKILL.md didn't document that the script's tokenizer removes stop words — fix committed this session. |

### Methodology B tally

| Verdict class | Count | Skills |
|---------------|------:|--------|
| correctness ⭐ | **5** | `algo-risk-altman-z`, `algo-price-elasticity`, `algo-rank-elo`, `algo-sc-eoq`, `algo-seo-tfidf` |
| both ⭐⭐ | **1** | `ecom-rfm-analysis` |
| speed | **3** | `biz-dcf`, `mkt-ab-testing`, `algo-sc-newsvendor` |
| neither | **10** | 10 skills (see table above) |
| inconclusive | **1** | `algo-ecom-bm25` (skill bug surfaced + fixed) |

**Hit rate (B)**: 9/20 = **45%** provide measurable value. The value *shape* is
different from Methodology A:
- More **correctness** wins (5 vs 3): methodology teaches variant selection,
  formula choice, and gotchas that vanilla LLM misses.
- Fewer **speed** wins (3 vs 5): when vanilla LLM is correct, it's often also
  fast; speed wins concentrate on cases where the arithmetic is genuinely
  intractable by hand.

## Comparing the two methodologies — what changed

| Skill | Method A | Method B | Explanation |
|-------|----------|----------|-------------|
| `algo-rank-elo` | speed | **correctness** | The "draw" and "upset" scenarios trip vanilla LLM's intuition; methodology A already had SKILL.md in both arms so the trap was neutralized. |
| `algo-sc-eoq` | neither | **correctness** | "20% of unit cost" phrasing confuses vanilla LLM without methodology hints. |
| `algo-price-elasticity` | neither | **correctness** | Arc midpoint formula — vanilla LLM picks a variant that's numerically close but wrong. |
| `algo-seo-tfidf` | neither | **correctness** | IDF smoothing variant matters. |
| `ecom-rfm-analysis` | speed | **both** | Hand-computing percentile quantiles for 10 customers is both slow and error-prone. |
| `biz-dcf` | speed | speed | Consistent — the value is latency, not correctness. |
| `mkt-ab-testing` | speed | speed | Consistent. |
| `algo-rank-wilson` | speed | neither | Vanilla LLM handles Wilson score well once the raw stats are given. The old "speed" signal was mild (3.6× on one scenario); not replicable. |
| `algo-ecom-bm25` | correctness | **inconclusive** | Eval exposed a real skill bug: SKILL.md didn't document the script's stop-word removal, so even with_skill miscomputes. |
| `biz-financial-ratios` | correctness | neither | Debt_to_equity trap — vanilla LLM's output is non-deterministic on which definition to use. Single-run eval can flip. |

## Skill quality issues surfaced by the eval

1. **`algo-risk-altman-z`**: SKILL.md pointed to `references/z-score-variants.md`
   and `references/bankruptcy-models.md` — **neither existed**. Fixed: created
   `z-score-variants.md` with Z / Z' / Z'' full formulas and a worked tech-firm
   example; added a mandatory Phase 1.5 "Variant Selection" gate; removed the
   dead pointer. Without this fix, even with_skill couldn't score Z'' correctly.

2. **`biz-financial-ratios`**: "Debt" in leverage ratios was undefined; the
   script uses `total_liabilities` but both "long-term debt" and "interest-bearing
   debt" are common alternatives. Fixed: added explicit ⚠️ note.

3. **`algo-ecom-bm25`**: Multiple IDF variants exist. Fixed in an earlier commit
   to lock the skill to the Lucene-smoothed variant. This session also
   discovered the script removes stop words — fix committed: SKILL.md Phase 1
   now documents the stop list.

4. **`grad-capm` / `biz-dupont` / `biz-financial-ratios`**: Output format didn't
   specify decimal vs percent convention; LLMs returned `35.0` vs `0.35`
   inconsistently. Fixed: ⚠️ notes added to all three Output Format sections.

## Methodological caveats

- **N=1 per scenario**: Each case runs the agent once per arm. LLM output has
  real variance — we observed at least two cases (`biz-financial-ratios`,
  `algo-rank-wilson`) where the verdict flipped between runs due to sampling,
  not skill changes. Correctness wins should ideally be validated across 3–5
  independent runs before claiming the effect is stable.
- **Anthropic API 5xx errors** were frequent during these runs. Runner now
  retries on timeout / overloaded / `api_error` / `Internal server error` with
  exponential backoff (15s × attempt, max 2 retries). Three Method A cases and
  two Method B cases were corrupted by 5xx before retry logic caught them.
- **Single model (Sonnet 4.6)**: Skills that look like "neither" may still be
  valuable when the deploying LLM is weaker. Before removing a script, test
  against Haiku or another lower-capacity model.

## Recommendations

### Keep — correctness / both wins (6 skills)
These stop the vanilla LLM from making concrete formula or variant mistakes.
Removing the skill would regress output quality:

- `algo-risk-altman-z` — variant selection (Z / Z' / Z'')
- `algo-price-elasticity` — arc midpoint formula
- `algo-rank-elo` — K-factor / draw handling edge cases
- `algo-sc-eoq` — holding-cost-as-percentage parsing
- `algo-seo-tfidf` — IDF smoothing variant
- `ecom-rfm-analysis` — quantile binning + RFM segment labels

### Keep — speed wins (3 skills)
Vanilla LLM gets the right answer but spends 3–11× more wall time / tokens:

- `biz-dcf` — 30yr projections
- `mkt-ab-testing` — normal CDF p-value arithmetic
- `algo-sc-newsvendor` — inverse normal CDF

### Review / re-test (1 skill)
- `algo-ecom-bm25` — was correctness-win in Method A, inconclusive in Method B
  because of a now-fixed SKILL.md stop-word gap. Re-run after the fix to
  confirm the skill now passes.

### Removal candidates (10 skills)
No measurable value over Sonnet 4.6 at the difficulties tested. Before removing
any, run the 3–5× replication check AND test against a weaker model:

`algo-mfg-cpk`, `algo-rank-bayesian`, `algo-rank-wilson`, `algo-sc-safety-stock`,
`biz-breakeven`, `biz-cac-ltv`, `biz-dupont`, `biz-financial-ratios`,
`biz-unit-economics`, `grad-capm`.
