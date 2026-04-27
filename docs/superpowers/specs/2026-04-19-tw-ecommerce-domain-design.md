# 台灣電商 Skill Domain — Design Spec

**Date**: 2026-04-19
**Branch**: `feat/tw-ecommerce-domain`
**Source**: `~/Downloads/tw-ecommerce-skills-proposal.md` (v0.1)
**Scope**: D2 — Phase 0 infra + 3 MCP-backed reference skills + 26 skeleton skills

---

## 1. Goals

1. Introduce a coherent **Taiwan e-commerce** skill domain into `asgard-ai-platform/skills` without breaking the existing flat repo architecture.
2. Reuse existing `tw-*` / `ecom-*` skills that already cover the landscape layer; only add depth where missing.
3. Ship 3 merge-ready reference skills grounded in MCP-backed official docs, so remaining skeletons have a concrete template to copy.
4. Ship 29-skill **directory footprint** (structure visible) so future contributors see the domain shape.

## 2. Non-goals

- Not implementing all 29 skills' body content in this branch. Only 3 are content-complete; the rest are frontmatter + skeleton.
- Not creating any new MCP or `bundles/` manifest.
- Not touching existing `tw-*` or `ecom-*` skills' content. Cross-linking only.
- Not introducing nested skill directories (`ecommerce-tw/payment/tw-payment-tappay/` from proposal §2.1 is rejected — violates `CLAUDE.md` flat convention).

## 3. Architecture decision — flat skills + domain doc

### 3.1 Chosen approach

All skills remain at repo root as `{category}-{slug}` directories, per `CLAUDE.md`. Domain cohesion is provided by a separate navigation document:

```
skills/
├── tw-ecom-dtc-shopline/      ← new, flat
├── tw-ecom-payment-newebpay/          ← new, flat
├── tw-ecom-invoice-ezpay/             ← new, flat
├── tw-ecom-...                         ← 26 skeletons, flat
├── tw-payment-integration/             ← existing, untouched
├── tw-einvoice-guide/                  ← existing, untouched
├── ecom-rfm-analysis/                  ← existing, untouched
└── docs/domains/
    └── tw-ecommerce.md                 ← NEW: domain map + decision trees + skill index
```

### 3.2 Rejected alternatives

- **Nested `ecommerce-tw/` directory (proposal §2.1)**: would require updating `CLAUDE.md` architecture rule and diverge from 263 existing flat skills. Tooling and lint scripts assume flat.
- **Bundle manifest (`bundles/tw-ecommerce.yaml`)**: premature; belongs to `TODO.md` Phase 5 plugin work. Compatible with flat layout, can be added later without conflict.

### 3.3 Naming convention

- New Taiwan e-commerce skills: `tw-ecom-<layer>-<topic>`
  - Layer ∈ {`platform`, `payment`, `logistics`, `invoice`, `compliance`, `operations`, `analytics`}
  - Examples: `tw-ecom-payment-newebpay`, `tw-ecom-invoice-ezpay`
- Platform-layer exception: use platform name directly (`tw-ecom-dtc-shopline`, `tw-ecom-dtc-91app`), not `tw-ecom-platform-<name>`. Each platform is its own identifier.
- Existing `tw-*` / `ecom-*` skills keep their names (no renaming, avoid breaking consumers).

## 4. Existing skill overlap audit

Proposal §2.1 planned ~30 skills; ~10 are already covered:

| Proposal skill | Existing skill | Action |
|---|---|---|
| `tw-payment-selection` | `tw-payment-integration` | **Do not add**; domain doc points here |
| `tw-invoice-mof` (landscape) | `tw-einvoice-guide` | **Do not add**; domain doc points here |
| Operations: promo ROI | `ecom-promo-roi` | **Do not add**; domain doc points here |
| Operations: inventory | `ecom-inventory-health` | **Do not add**; domain doc points here |
| Analytics: general | `ecom-analytics`, `ecom-rfm-analysis` | **Do not add**; domain doc points here |
| Compliance: general | `tw-startup-legal`, `tw-fintech-compliance`, `tw-tax-basics` | Partial coverage; domain doc cross-links |

Net new skills to create in this branch: **29** (3 complete + 26 skeleton).

## 5. Reference skills (3 complete, merge-ready)

All three are MCP-backed, so content derives from official tool schemas + vendor docs, not speculation.

| Skill | MCP | Layer | Tool count |
|---|---|---|---|
| `tw-ecom-dtc-shopline` | `mcp-shopline` | platform | 143 (75 read + 68 write) |
| `tw-ecom-payment-newebpay` | `mcp-newebpay` | payment | 8 |
| `tw-ecom-invoice-ezpay` | `mcp-ezpay-einvoice` | invoice | 7 |

### 5.1 Each complete skill must contain

- `SKILL.md` with:
  - Frontmatter (`name`, `description` with use-when + do-not-use-when, `metadata.domain: ecommerce-tw`, `metadata.layer`, `metadata.related_mcps`, `metadata.related_skills`, `metadata.last_verified: 2026-04`, `metadata.tags`)
  - **Do NOT add a per-skill `license:` field** — not repo convention (verified 0/250 existing skills use it; MIT license is declared at repo root)
  - Core concepts (≤200 words)
  - Decision tree (when to use which tool / gateway / provider)
  - Implementation guidance (basic flow, error handling, settlement/reconciliation)
  - Gotchas (5-6 real, non-obvious pitfalls — match `CLAUDE.md` anti-pattern #4 bar)
  - IRON LAW (non-obvious constraint, not a truism)
  - Output Format template
  - Related (cross-link to `related_mcps` and `related_skills`)
- `references/` directory with at least one file (deep API reference or decision tree detail)
- `examples/` directory with at least one `sample_scenario.md`
- `last verified: 2026-04` note at end (proposal §5.1 在地性 checklist)

### 5.2 Content source discipline

- DO: derive from MCP tool names + schemas + official vendor docs (Shopline Open API, NewebPay MPG, ezPay E-Invoice spec)
- DO: state known facts only, mark `last verified` date
- DON'T: fabricate fee rates, dispute-handling procedures, settlement timing without vendor doc citation — mark as `TODO: verify with <source>` instead

## 6. Skeleton skills (26, scaffold only)

### 6.1 Skeleton contents

Each skeleton directory contains:

- `SKILL.md`:
  - Full frontmatter (valid, lint-passing)
  - `# When to use this skill` — 3-5 bullets
  - `# Do NOT use when` — 2-3 bullets
  - `# Status: SKELETON — body pending` banner
  - `TODO` placeholder sections for Core concepts / Decision tree / Gotchas / IRON LAW / Output Format
- `references/.gitkeep` (empty dir per `CLAUDE.md` requirement)
- `examples/.gitkeep`

### 6.2 Skeleton list (grouped by layer)

**Platform** (5):
- `tw-ecom-channel-strategy` — DTC vs marketplace vs hybrid decision
- `tw-ecom-dtc-91app`
- `tw-ecom-dtc-shopify-localization`
- `tw-ecom-marketplace-shopee`
- `tw-ecom-marketplace-momo`

*Note:* `cyberbiz-integration` intentionally NOT added — `mcp-cyberbiz` is an empty repo (per `TODO.md`), no grounding content available yet.

**Payment** (4):
- `tw-ecom-payment-tappay`
- `tw-ecom-payment-ecpay`
- `tw-ecom-payment-jkopay`
- `tw-ecom-payment-dispute`

**Logistics** (4):
- `tw-ecom-logistics-cvs`
- `tw-ecom-logistics-home`
- `tw-ecom-logistics-cold-chain`
- `tw-ecom-logistics-cross-border`

**Invoice** (3):
- `tw-ecom-invoice-universalec`
- `tw-ecom-invoice-carrier`
- `tw-ecom-invoice-void`

**Compliance** (4):
- `tw-ecom-compliance-consumer`
- `tw-ecom-compliance-product`
- `tw-ecom-compliance-pdpa` — e-commerce specific member consent / cookie / order data
- `tw-ecom-compliance-cross-border` — TW cross-border tariff / VAT

**Operations** (4):
- `tw-ecom-operations-promotion` — 雙11、618、週年慶
- `tw-ecom-operations-pricing` — 含稅價、議價文化、檔期壓價策略
- `tw-ecom-operations-crm-line-oa` — LINE OA (dominant TW channel)
- `tw-ecom-operations-customer-service` — PTT/Dcard reputation + 消保鑑賞期話術

**Analytics** (2):
- `tw-ecom-analytics-ga4` — TW e-commerce GA4 event conventions
- `tw-ecom-analytics-benchmarks` — TW market CVR / ROAS / LTV reference ranges

*Total: 26 skeleton + 3 complete = 29 new skill directories.*

### 6.3 Deliberately excluded skills

| Skill | Why excluded |
|---|---|
| `tw-ecom-advertising` | Ad optimization is mostly cross-geo methodology; existing `mkt-ad-optimization` + `algo-ad-*` cover it. Adding a TW variant risks `CLAUDE.md` anti-pattern #4 (Missing Gotchas — generic content). |
| `tw-ecom-reporting` | Daily/weekly/monthly reporting is a generic methodology with no TW specificity. |
| `tw-ecom-cyberbiz-integration` | `mcp-cyberbiz` is empty per `TODO.md`; no docs to ground against. Add later when MCP has content. |

## 7. Phase 0 infrastructure

This branch also ships:

1. `docs/domains/tw-ecommerce.md` — domain navigation:
   - Overview: what this domain covers, who it's for
   - Decision tree: "I need to do X on Taiwan e-commerce → read skill Y"
   - Full skill index (new + existing, grouped by layer)
   - Related MCPs list (`mcp-shopline`, `mcp-91app`, `mcp-newebpay`, `mcp-ezpay-einvoice`, `mcp-universalec-e-invoice`, `mcp-ecpay`, `mcp-ecpay-logistics`)
2. `CONTRIBUTING.md` at repo root — short guide covering:
   - How to add a skill (directory layout, frontmatter, required sections)
   - Quality bar (the 8 anti-patterns from `CLAUDE.md`)
   - Domain cohesion rule: new skill in an existing domain → update `docs/domains/*.md` index
3. Update `README.md` (and `README.en.md`) to reference the new `docs/domains/` convention.
4. Entry in `TODO.md` — carve out the 26 skeleton skills as tracked follow-up work.

**Explicitly NOT in Phase 0**:
- No lint script (proposal §4.1 item 5). Defer until we have 2+ domain doc patterns to lint against. Avoid premature tooling.
- No CODEOWNERS. Defer until domain has 2+ maintainers.

## 8. Quality bar & verification

Per `CLAUDE.md`:

- No `claude` / `anthropic` in skill names
- Every `examples/` and `references/` directory exists (use `.gitkeep` for empty ones)
- SKILL.md body ≤ 500 lines / 5,000 tokens
- No phantom triggers, no over-teaching, no truism Iron Laws
- Description field < 1024 chars, no XML angle brackets

**Verification before PR**:
- All 29 new SKILL.md files parse as valid YAML frontmatter
- Manually check 3 complete skills against `CLAUDE.md` §Quality Audit Anti-Patterns
- `docs/domains/tw-ecommerce.md` cross-links all skills (new + existing) that belong to the domain

## 9. Risks & open questions

| Risk | Mitigation |
|---|---|
| Skeleton skills get indexed by agents and trigger on vague queries | Explicit `# Status: SKELETON` banner + description says "This skill is under development; prefer <related skill> for now" |
| Reference skills drift from MCP reality (tools renamed, removed) | `last verified: 2026-04` marker; `docs/domains/tw-ecommerce.md` has a "re-verify quarterly" note |
| Shopline skill duplicates `mcp-shopline` README | Methodology focus: when to use which tool, common multi-tool flows, gotchas — not API reference |
| `tw-payment-integration` landscape skill ages poorly as deep skills are added | Out of scope for this branch; flag as a follow-up issue |

**Open questions** (not blocking):

- Should we wait for `mcp-ecpay` / `mcp-ecpay-logistics` READMEs to solidify before adding ECPay skeletons? Current answer: skeleton only, no content dependency.
- Do we want an `en-US` variant of the domain doc for international reach (proposal §7.2)? Not in this branch.

## 10. Follow-up branches (roadmap)

- `feat/tw-ecom-platform-skills` — fill in 5 platform skeletons (platform-selection, 91app, shopify-tw, shopee, momo)
- `feat/tw-ecom-payment-deep-skills` — fill in 4 payment skeletons (tappay, ecpay, jkopay, dispute)
- `feat/tw-ecom-logistics-skills` — fill in 4 logistics skeletons
- `feat/tw-ecom-invoice-deep-skills` — fill in 3 invoice skeletons (universalec, carrier, void)
- `feat/tw-ecom-compliance-skills` — fill in 4 compliance skeletons + cross-link to existing `tw-startup-legal`
- `feat/tw-ecom-operations-skills` — fill in 4 operations skeletons (promotion, pricing, crm-line-oa, customer-service)
- `feat/tw-ecom-analytics-skills` — fill in 2 analytics skeletons (ga4, benchmarks)
- Each follow-up branch handles 2-5 skills. Quarterly re-verification runs as its own branch.

## 11. Next step

Invoke `superpowers:writing-plans` to produce a step-by-step implementation plan for this branch.
