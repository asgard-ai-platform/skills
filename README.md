# Asgard Skills

Open-source library of **263 coding agent skills** across 21 topic-based categories. Each skill is a self-contained Markdown file (`SKILL.md`) following the [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) standard, with optional Python scripts for deterministic calculations.

[繁體中文](README.zh-TW.md)

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
└── {{SKILL_NAME}}/        ← Template skeleton for new skills
```

## Categories (21 prefixes, 263 skills)

| Prefix | Count | Topic |
|--------|------:|-------|
| `grad-` | 87 | Graduate-level theoretical models (RBV, CAPM, SEM, DID, ...) |
| `algo-` | 62 | Algorithms (PageRank, BM25, ARIMA, EOQ, ...) |
| `biz-` | 22 | Business school frameworks (SWOT, Porter's Five Forces, DCF, ...) |
| `hum-` | 9 | Humanities / critical reasoning |
| `tw-` | 9 | Taiwan-specific knowledge (stock, tax, e-invoice, ...) |
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

See [`CLAUDE.md`](CLAUDE.md) for full design rules and quality standards.

## Status

| Phase | Status |
|-------|:-:|
| Phase 1: Generate 263 skills across 4 sections | ✅ |
| Phase 1.5: Auto lint (frontmatter, length, IRON LAW) | ✅ 263/263 |
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

## License

MIT License. See [LICENSE](LICENSE).
