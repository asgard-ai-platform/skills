# tw-ecommerce Domain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a coherent Taiwan e-commerce skill domain (29 new skills + infra) on branch `feat/tw-ecommerce-domain` without breaking the repo's flat `{category}-{slug}` architecture.

**Architecture:** Flat skill directories at repo root using `tw-ecom-<layer>-<topic>` naming. Domain cohesion via new `docs/domains/tw-ecommerce.md` navigation doc (not a skill). Three MCP-backed reference skills (`shopline`, `newebpay`, `ezpay-einvoice`) are content-complete; remaining 26 are skeleton-only (frontmatter + When-to-use/Do-NOT + TODO body).

**Tech Stack:** Markdown. No code. Bash + heredoc for file creation. MIT license (repo-level; no per-skill license field).

**Reference docs:**
- Design spec: `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md`
- Repo conventions: `CLAUDE.md`
- Source proposal: `~/Downloads/tw-ecommerce-skills-proposal.md`

---

## File Structure

### New skill directories (29 at repo root)

**Complete** (SKILL.md + references/<file>.md + examples/sample_scenario.md):
- `tw-ecom-shopline-integration/`
- `tw-ecom-payment-newebpay/`
- `tw-ecom-invoice-ezpay/`

**Skeleton** (SKILL.md + references/.gitkeep + examples/.gitkeep):
- Platform: `tw-ecom-platform-selection`, `tw-ecom-91app-integration`, `tw-ecom-shopify-tw-integration`, `tw-ecom-shopee-operations`, `tw-ecom-momo-operations`
- Payment: `tw-ecom-payment-tappay`, `tw-ecom-payment-ecpay`, `tw-ecom-payment-jkopay`, `tw-ecom-payment-dispute`
- Logistics: `tw-ecom-logistics-cvs`, `tw-ecom-logistics-home`, `tw-ecom-logistics-cold-chain`, `tw-ecom-logistics-cross-border`
- Invoice: `tw-ecom-invoice-universalec`, `tw-ecom-invoice-carrier`, `tw-ecom-invoice-void`
- Compliance: `tw-ecom-compliance-consumer`, `tw-ecom-compliance-product`, `tw-ecom-compliance-pdpa`, `tw-ecom-compliance-cross-border`
- Operations: `tw-ecom-operations-promotion`, `tw-ecom-operations-pricing`, `tw-ecom-operations-crm-line-oa`, `tw-ecom-operations-customer-service`
- Analytics: `tw-ecom-analytics-ga4`, `tw-ecom-analytics-benchmarks`

### New / modified non-skill files

- Create: `docs/domains/tw-ecommerce.md`
- Create: `CONTRIBUTING.md`
- Modify: `README.md` (add link to `docs/domains/`)
- Modify: `README.en.md` (same)
- Modify: `TODO.md` (append skeleton backlog)
- Create: `/tmp/tw-ecom-refs/` (local-only, gitignored; MCP README snapshots for authoring)

### Untouched

Existing `tw-*` and `ecom-*` skill directories: **do not modify content**. Only cross-link from domain doc.

---

## Task 1: Fetch MCP reference material

**Files:**
- Create (local only): `/tmp/tw-ecom-refs/mcp-shopline-README.md`
- Create (local only): `/tmp/tw-ecom-refs/mcp-newebpay-README.md`
- Create (local only): `/tmp/tw-ecom-refs/mcp-ezpay-einvoice-README.md`
- Create (local only): `/tmp/tw-ecom-refs/tool-lists.md`

These are local scratch files used only to author the 3 complete skills. They are NOT committed (outside the repo tree).

- [ ] **Step 1: Create local refs directory**

```bash
mkdir -p /tmp/tw-ecom-refs
```

- [ ] **Step 2: Fetch the three MCP repo READMEs via gh**

```bash
gh api repos/asgard-ai-platform/mcp-shopline/readme --jq '.content' | base64 -d > /tmp/tw-ecom-refs/mcp-shopline-README.md
gh api repos/asgard-ai-platform/mcp-newebpay/readme --jq '.content' | base64 -d > /tmp/tw-ecom-refs/mcp-newebpay-README.md
gh api repos/asgard-ai-platform/mcp-ezpay-einvoice/readme --jq '.content' | base64 -d > /tmp/tw-ecom-refs/mcp-ezpay-einvoice-README.md
wc -l /tmp/tw-ecom-refs/*.md
```

Expected: three files, each > 50 lines. If any comes back empty, check repo slug via `gh repo view asgard-ai-platform/<name>`.

- [ ] **Step 3: Extract tool lists for each MCP**

Look for tool names (typically in tables or `list_tools` / `@tool` code). Capture into one combined file:

```bash
cat > /tmp/tw-ecom-refs/tool-lists.md <<'HEADER'
# MCP Tool Lists — snapshot 2026-04-19

## mcp-shopline (143 tools)
HEADER

grep -E '^\| `?[a-z_]+`?' /tmp/tw-ecom-refs/mcp-shopline-README.md >> /tmp/tw-ecom-refs/tool-lists.md 2>/dev/null
echo '' >> /tmp/tw-ecom-refs/tool-lists.md
echo '## mcp-newebpay (8 tools)' >> /tmp/tw-ecom-refs/tool-lists.md
grep -E '^\| `?[a-z_]+`?' /tmp/tw-ecom-refs/mcp-newebpay-README.md >> /tmp/tw-ecom-refs/tool-lists.md 2>/dev/null
echo '' >> /tmp/tw-ecom-refs/tool-lists.md
echo '## mcp-ezpay-einvoice (7 tools)' >> /tmp/tw-ecom-refs/tool-lists.md
grep -E '^\| `?[a-z_]+`?' /tmp/tw-ecom-refs/mcp-ezpay-einvoice-README.md >> /tmp/tw-ecom-refs/tool-lists.md 2>/dev/null

cat /tmp/tw-ecom-refs/tool-lists.md | head -50
```

Expected: three sections with tool rows. If grep misses because the README uses different formatting, open the file and extract manually — the tool list shape matters more than the exact grep pattern.

- [ ] **Step 4: No commit (files are outside repo)**

This task has no commit step — the files are local scratch only.

---

## Task 2: Write tw-ecom-shopline-integration (complete reference skill)

**Files:**
- Create: `tw-ecom-shopline-integration/SKILL.md`
- Create: `tw-ecom-shopline-integration/references/tool-catalog.md`
- Create: `tw-ecom-shopline-integration/examples/sample_scenario.md`

**Content source discipline:** derive all facts from `/tmp/tw-ecom-refs/mcp-shopline-README.md` + Shopline Open API public docs. Mark any unsourced claim as `TODO: verify with <source>` — do not fabricate fee rates or settlement timing.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p tw-ecom-shopline-integration/references tw-ecom-shopline-integration/examples
```

- [ ] **Step 2: Write SKILL.md**

Required sections in this order:
1. **Frontmatter** (YAML)
2. `# Shopline Integration Methodology`
3. `## When to use this skill` (3-5 bullets)
4. `## Do NOT use when` (2-3 bullets)
5. `## Core concepts` (≤200 words — what Shopline is, DTC vs marketplace, shop vs store vs merchant terminology, the read/write tool split)
6. `## Decision tree` (Mermaid or ASCII — which tool family to reach for given: order ops / product ops / member ops / promotion ops / reporting)
7. `## Implementation guidance` (common multi-tool flows: order sync, promotion setup, member sync, inventory sync — each 3-5 bullets with tool names from `tool-lists.md`)
8. `## Gotchas` — 5-6 real pitfalls. Required examples:
   - Shopline async updates: some writes take seconds to propagate; read-after-write can return stale data
   - Pagination: tool responses cap at N items; must loop
   - Rate limits: exact limit to be verified from README
   - Multi-shop accounts: account scoping matters
   - Webhook vs polling: when to use each
   - Sandbox vs production: credential separation
9. `## IRON LAW` — one non-obvious constraint. Candidate: "Never assume a Shopline write is immediately readable — build reconciliation loops, not read-after-write checks." Verify this fits; if not, pick another. Must NOT be a truism.
10. `## Output Format` — Markdown template the agent should produce when completing a Shopline task (see Task 3 & 4 for the pattern)
11. `## Related`
    - `related_mcps`: `mcp-shopline`
    - `related_skills`: `tw-ecom-platform-selection`, `tw-ecom-invoice-ezpay`, `tw-ecom-payment-newebpay`, `ecom-rfm-analysis`, `ecom-promo-roi`, `ecom-inventory-health`
12. `_Last verified: 2026-04_`

Frontmatter template (exact fields):

```yaml
---
name: "tw-ecom-shopline-integration"
description: "Integrate and operate Shopline in Taiwan e-commerce context via mcp-shopline. Use when the user needs to sync orders, manage products, run promotions, or reconcile inventory on Shopline stores; when comparing Shopline vs 91APP/Shopify for Taiwan DTC; or when debugging async write propagation. Do NOT use for API schema lookup (go to mcp-shopline docs) or non-Taiwan Shopline deployments."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: ["mcp-shopline"]
  related_skills: ["tw-ecom-platform-selection", "tw-ecom-invoice-ezpay", "tw-ecom-payment-newebpay", "ecom-rfm-analysis", "ecom-promo-roi", "ecom-inventory-health"]
  last_verified: "2026-04"
  tags: ["taiwan", "e-commerce", "shopline", "platform", "integration"]
---
```

- [ ] **Step 3: Write references/tool-catalog.md**

One-line summary per tool family (read ops grouped, write ops grouped). Source: `/tmp/tw-ecom-refs/mcp-shopline-README.md`. No fabrication — if README doesn't document a tool, omit it.

- [ ] **Step 4: Write examples/sample_scenario.md**

One end-to-end scenario (~80-150 lines): "New order arrives via Shopline → sync to internal ERP → trigger ezPay e-invoice → webhook reconciliation." Show the multi-tool flow with actual tool names. Mark any uncertain tool behavior as `TODO: verify with mcp-shopline tool schema`.

- [ ] **Step 5: Verify file shape**

```bash
wc -l tw-ecom-shopline-integration/SKILL.md tw-ecom-shopline-integration/references/tool-catalog.md tw-ecom-shopline-integration/examples/sample_scenario.md
head -10 tw-ecom-shopline-integration/SKILL.md
awk '/^description:/ { print length($0)-15 }' tw-ecom-shopline-integration/SKILL.md
```

Expected:
- SKILL.md: 150-450 lines (CLAUDE.md cap is 500)
- references/tool-catalog.md: 50-200 lines
- examples/sample_scenario.md: 80-200 lines
- description length (after `description: "`): < 1024 chars

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-shopline-integration/
git commit -m "feat(tw-ecom): add tw-ecom-shopline-integration reference skill"
```

---

## Task 3: Write tw-ecom-payment-newebpay (complete reference skill)

**Files:**
- Create: `tw-ecom-payment-newebpay/SKILL.md`
- Create: `tw-ecom-payment-newebpay/references/integration-flow.md`
- Create: `tw-ecom-payment-newebpay/examples/sample_scenario.md`

**Content source discipline:** derive from `/tmp/tw-ecom-refs/mcp-newebpay-README.md` + NewebPay MPG (MPG2 / CTCB) public docs. Do not invent fee rates — mark as `TODO: verify from NewebPay merchant portal` if unknown.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p tw-ecom-payment-newebpay/references tw-ecom-payment-newebpay/examples
```

- [ ] **Step 2: Write SKILL.md**

Required sections (same order as Task 2). Section-specific content:

- `## Core concepts`: NewebPay position in Taiwan market, payment method families (credit card / ATM / CVS / LINE Pay / Apple Pay / periodical), 3DS 2.0 flow, TradeSha/HashKey signature concept
- `## Decision tree`: when to pick NewebPay over ECPay/TapPay (trigger on: modern API preference, periodical billing, SaaS model)
- `## Implementation guidance`: 3 flows — one-time payment, recurring (定期定額), refund. Each with the exact mcp-newebpay tool to call.
- `## Gotchas` — must include:
  - Signature verification order matters (TradeSha is computed in alphabetical param order)
  - Callback webhook may arrive before return URL redirect → handle order state carefully
  - 定期定額 card expiration handling
  - Test vs production endpoints differ in HashKey rotation
  - Refund window (typically same-bimonthly; verify with docs)
  - Signature IV must be 16 bytes; common off-by-one error when devs re-use older MPG1 keys

- `## IRON LAW`: candidate — "NewebPay callback webhooks are the source of truth, not the browser return URL; never close an order based solely on return URL parameters." If this rule is too well-known by NewebPay devs to warrant repeating, pick another non-obvious constraint.

Frontmatter:

```yaml
---
name: "tw-ecom-payment-newebpay"
description: "Integrate NewebPay (藍新金流) for Taiwan e-commerce via mcp-newebpay. Use when accepting credit card / ATM / CVS / LINE Pay / periodical payments on NewebPay, handling 3DS 2.0 flows, computing TradeSha signatures, or reconciling callback webhooks. Do NOT use for comparing gateways (see tw-payment-integration) or for non-NewebPay providers (TapPay, ECPay have their own skills)."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: ["mcp-newebpay"]
  related_skills: ["tw-payment-integration", "tw-ecom-payment-dispute", "tw-ecom-invoice-ezpay"]
  last_verified: "2026-04"
  tags: ["taiwan", "payment", "newebpay", "fintech"]
---
```

- [ ] **Step 3: Write references/integration-flow.md**

Detailed flow: merchant setup → first transaction → callback handling → reconciliation. Reference exact mcp-newebpay tool names from `/tmp/tw-ecom-refs/tool-lists.md`.

- [ ] **Step 4: Write examples/sample_scenario.md**

Scenario (~80-150 lines): "Recurring subscription billing for a content site — set up periodical plan, handle card expiration, issue e-invoice via ezpay on success, handle failed charge with dispute flow."

- [ ] **Step 5: Verify file shape**

```bash
wc -l tw-ecom-payment-newebpay/SKILL.md tw-ecom-payment-newebpay/references/integration-flow.md tw-ecom-payment-newebpay/examples/sample_scenario.md
head -10 tw-ecom-payment-newebpay/SKILL.md
awk '/^description:/ { print length($0)-15 }' tw-ecom-payment-newebpay/SKILL.md
```

Expected: SKILL.md 150-400 lines, description < 1024 chars.

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-payment-newebpay/
git commit -m "feat(tw-ecom): add tw-ecom-payment-newebpay reference skill"
```

---

## Task 4: Write tw-ecom-invoice-ezpay (complete reference skill)

**Files:**
- Create: `tw-ecom-invoice-ezpay/SKILL.md`
- Create: `tw-ecom-invoice-ezpay/references/issuance-flow.md`
- Create: `tw-ecom-invoice-ezpay/examples/sample_scenario.md`

**Content source discipline:** derive from `/tmp/tw-ecom-refs/mcp-ezpay-einvoice-README.md` + ezPay e-invoice API public docs.

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p tw-ecom-invoice-ezpay/references tw-ecom-invoice-ezpay/examples
```

- [ ] **Step 2: Write SKILL.md**

Section-specific content:

- `## Core concepts`: ezPay role as a 加值服務中心 (relationship to 財政部平台), B2B vs B2C, carrier types (手機條碼 / 自然人憑證 / 會員載具), 字軌 assignment, 捐贈碼
- `## Decision tree`: issue vs void vs allowance (折讓) vs reissue; carrier-less B2C vs carrier B2C
- `## Implementation guidance`: 3 flows — issue invoice (one-shot), void invoice (within bimonthly window), allowance (折讓) for cross-period corrections
- `## Gotchas` — must include:
  - 字軌 exhaustion (MOF assigns ranges; depletion blocks issuance — monitor and request early)
  - Void window is same bimonthly only; cross-period requires allowance
  - 手機條碼 format is `/` + 7 chars; scanner config matters
  - Carrier validation must happen client-side before API call (invalid carrier = rejected invoice)
  - Reconciliation vs MOF platform daily (ezPay is middleman, not source of truth)
  - B2B invoices require buyer 統編 — missing 統編 silently defaults to B2C (lottery eligible, wrong tax)

- `## IRON LAW`: candidate — "The MOF platform is source of truth; ezPay state can lag. Always reconcile daily against MOF, not against ezPay's own records."

Frontmatter:

```yaml
---
name: "tw-ecom-invoice-ezpay"
description: "Issue and manage Taiwan e-invoices via ezPay (加值服務中心) through mcp-ezpay-einvoice. Use when issuing B2B/B2C invoices, handling carrier codes (手機條碼, 自然人憑證), voiding within the same bimonthly window, or issuing allowances (折讓) across periods. Do NOT use for direct 財政部 API integration (see tw-einvoice-guide) or for UniversalEC-backed flows (see tw-ecom-invoice-universalec)."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: ["mcp-ezpay-einvoice"]
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-carrier", "tw-ecom-invoice-void", "tw-tax-basics"]
  last_verified: "2026-04"
  tags: ["taiwan", "e-invoice", "ezpay", "tax-compliance"]
---
```

- [ ] **Step 3: Write references/issuance-flow.md**

Cover: registration with ezPay, 字軌 request, certificate setup, sandbox-to-prod migration, daily reconciliation pattern.

- [ ] **Step 4: Write examples/sample_scenario.md**

Scenario (~80-150 lines): "Customer buys via Shopline with 手機條碼 carrier → webhook triggers ezPay invoice issuance → customer later requests return → issue allowance (折讓) since the refund spans bimonthly boundary."

- [ ] **Step 5: Verify file shape**

```bash
wc -l tw-ecom-invoice-ezpay/SKILL.md tw-ecom-invoice-ezpay/references/issuance-flow.md tw-ecom-invoice-ezpay/examples/sample_scenario.md
head -10 tw-ecom-invoice-ezpay/SKILL.md
awk '/^description:/ { print length($0)-15 }' tw-ecom-invoice-ezpay/SKILL.md
```

Expected: SKILL.md 150-400 lines, description < 1024 chars.

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-invoice-ezpay/
git commit -m "feat(tw-ecom): add tw-ecom-invoice-ezpay reference skill"
```

---

## Task 5: Create 5 platform skeletons

**Files (5 skill directories):**
- Create: `tw-ecom-platform-selection/` (SKILL.md, references/.gitkeep, examples/.gitkeep)
- Create: `tw-ecom-91app-integration/` (same)
- Create: `tw-ecom-shopify-tw-integration/` (same)
- Create: `tw-ecom-shopee-operations/` (same)
- Create: `tw-ecom-momo-operations/` (same)

Skeleton SKILL.md shape (applied uniformly): frontmatter + banner + When to use + Do NOT use when + TODO body sections.

- [ ] **Step 1: Create `tw-ecom-platform-selection`**

```bash
mkdir -p tw-ecom-platform-selection/references tw-ecom-platform-selection/examples
touch tw-ecom-platform-selection/references/.gitkeep tw-ecom-platform-selection/examples/.gitkeep
cat > tw-ecom-platform-selection/SKILL.md <<'SKILL'
---
name: "tw-ecom-platform-selection"
description: "Choose the right e-commerce platform mix for a Taiwan business — DTC platforms (Shopline, 91APP, Shopify), marketplaces (Shopee, momo, PChome), or hybrid. Use when comparing platform fees, traffic potential, brand control trade-offs, or designing a go-to-market channel strategy for Taiwan. Do NOT use for specific platform integration details (see platform-specific skills). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: ["mcp-shopline", "mcp-91app"]
  related_skills: ["tw-ecom-shopline-integration", "tw-ecom-91app-integration", "tw-ecom-shopify-tw-integration", "tw-ecom-shopee-operations", "tw-ecom-momo-operations"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "platform", "strategy"]
---

# Taiwan E-Commerce Platform Selection

> **STATUS: SKELETON** — body pending. Prefer `tw-ecom-shopline-integration` for platform-specific depth in the meantime.

## When to use this skill

- Choosing the initial e-commerce platform for a new Taiwan D2C brand
- Deciding whether to sell DTC-only, marketplace-only, or hybrid
- Estimating TCO across platform fees, payment fees, and operational overhead
- Comparing platform unit economics before channel expansion
- Reassessing platform mix when scaling past NT$10M annual revenue

## Do NOT use when

- You already know the platform and need integration specifics → use the platform-specific skill
- The question is about global (non-Taiwan) platform choice → general e-commerce skills apply

## Core concepts

TODO: decision dimensions (fees, traffic, brand control, ops complexity), DTC vs marketplace typology, platform-fee tiers.

## Decision tree

TODO: flow chart keyed on annual revenue / brand strength / ops capacity.

## Implementation guidance

TODO: how to shortlist, pilot, measure, decide.

## Gotchas

TODO: 5-6 specific platform-selection traps for Taiwan businesses.

## IRON LAW

TODO: one non-obvious constraint (candidate: "Platform fees look comparable on paper but traffic acquisition cost is where margins die — always model unit economics with realistic CAC per platform").

## Output Format

TODO: Markdown template for platform selection recommendation.

## Related

- See the platform-specific integration skills for depth
- See `ecom-rfm-analysis` for customer cohort comparison across channels

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-91app-integration`**

```bash
mkdir -p tw-ecom-91app-integration/references tw-ecom-91app-integration/examples
touch tw-ecom-91app-integration/references/.gitkeep tw-ecom-91app-integration/examples/.gitkeep
cat > tw-ecom-91app-integration/SKILL.md <<'SKILL'
---
name: "tw-ecom-91app-integration"
description: "Integrate and operate 91APP in Taiwan e-commerce context via mcp-91app. Use when syncing orders/products/members on 91APP, running OMO (online-merge-offline) flows, integrating 91APP's app-first storefronts, or comparing 91APP vs Shopline/Shopify for mid-market DTC. Do NOT use for Shopline-specific integration (see tw-ecom-shopline-integration). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: ["mcp-91app"]
  related_skills: ["tw-ecom-platform-selection", "tw-ecom-shopline-integration"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "91app", "platform", "integration"]
---

# 91APP Integration Methodology

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating with 91APP via mcp-91app
- Running OMO (online-merge-offline) flows specific to 91APP
- Syncing member data between 91APP and CRM
- Debugging 91APP promotion / coupon flows
- Comparing 91APP vs Shopline for the mid-market DTC segment

## Do NOT use when

- You need generic platform selection guidance → use `tw-ecom-platform-selection`
- You need 91APP API schema docs → consult mcp-91app README directly

## Core concepts

TODO: 91APP app-first positioning, OMO model, member-centric architecture.

## Decision tree

TODO: which mcp-91app tool for which task.

## Implementation guidance

TODO: order sync, member sync, promotion setup, inventory sync flows.

## Gotchas

TODO: 5-6 pitfalls (candidates: OMO state drift, promotion stacking rules, member merge across web/app, quota limits).

## IRON LAW

TODO: one non-obvious constraint.

## Output Format

TODO.

## Related

- `tw-ecom-platform-selection`
- `tw-ecom-shopline-integration` (methodology template)

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-shopify-tw-integration`**

```bash
mkdir -p tw-ecom-shopify-tw-integration/references tw-ecom-shopify-tw-integration/examples
touch tw-ecom-shopify-tw-integration/references/.gitkeep tw-ecom-shopify-tw-integration/examples/.gitkeep
cat > tw-ecom-shopify-tw-integration/SKILL.md <<'SKILL'
---
name: "tw-ecom-shopify-tw-integration"
description: "Run Shopify stores for Taiwan market — localization (NT$ pricing, Traditional Chinese, TW address format), payment apps (ECPay / NewebPay / TapPay Shopify apps), shipping apps (CVS / 黑貓), and e-invoice integration. Use when setting up Shopify for TW, choosing TW payment/shipping apps, or adapting a global Shopify theme for TW. Do NOT use for general (non-TW) Shopify dev. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: []
  related_skills: ["tw-ecom-platform-selection", "tw-ecom-payment-newebpay", "tw-ecom-logistics-cvs", "tw-ecom-invoice-ezpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "shopify", "localization"]
---

# Shopify for Taiwan

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Setting up a new Shopify store targeting Taiwan customers
- Adding TW-specific payment apps (ECPay, NewebPay, TapPay) to Shopify
- Adding TW-specific shipping apps (CVS 7-11/全家, 黑貓)
- Integrating e-invoice issuance with Shopify order events
- Adapting a global theme for Traditional Chinese + NT$ pricing

## Do NOT use when

- Non-Taiwan Shopify work → use generic Shopify docs
- Shopline/91APP platform work → use their specific skills

## Core concepts

TODO: Shopify market/region config, app-based extension model (TW via marketplace apps, not native), why no official mcp-shopify yet for TW context.

## Decision tree

TODO: when Shopify beats Shopline/91APP for TW (brand-led international expansion, heavy theme customization need).

## Implementation guidance

TODO: app selection, localization checklist, e-invoice hook.

## Gotchas

TODO: 5-6 pitfalls (theme i18n gaps, app double-charging, payment app settlement differences, CVS shipping quirks).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-platform-selection`
- `tw-ecom-payment-newebpay`
- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Create `tw-ecom-shopee-operations`**

```bash
mkdir -p tw-ecom-shopee-operations/references tw-ecom-shopee-operations/examples
touch tw-ecom-shopee-operations/references/.gitkeep tw-ecom-shopee-operations/examples/.gitkeep
cat > tw-ecom-shopee-operations/SKILL.md <<'SKILL'
---
name: "tw-ecom-shopee-operations"
description: "Operate a Shopee Taiwan store — listings, promotions, flash sales, SIP (Shopee Supported Program) cross-border, ads (蝦皮廣告), and reputation/review management. Use when setting up or running Shopee TW operations, participating in platform campaigns (雙11, 618), or managing seller-center workflows. Do NOT use for Shopee API integration specifics (no official Asgard MCP yet) or DTC platforms. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: []
  related_skills: ["tw-ecom-platform-selection", "tw-ecom-momo-operations", "tw-ecom-operations-promotion"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "shopee", "marketplace"]
---

# Shopee Taiwan Operations

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Running day-to-day operations on Shopee TW seller center
- Planning Shopee platform campaigns (雙11, 618, 蝦皮購物節)
- Setting up 蝦皮廣告 (Shopee Ads) and measuring ROI
- Managing reviews / reputation / seller tier (普通/優選/金卡/商城)
- Cross-border via SIP

## Do NOT use when

- DTC platform work → use Shopline/91APP/Shopify skills
- Ad auction theory → use `algo-ad-*` skills

## Core concepts

TODO: Shopee TW vs Shopee SEA differences, seller tiers and fee tiers, 蝦皮購物 vs 蝦皮商城.

## Decision tree

TODO: when Shopee is the right channel, when to tier up.

## Implementation guidance

TODO: listing optimization, campaign participation, ad setup, dispute handling.

## Gotchas

TODO: 5-6 pitfalls (fee surprises on 免運券, campaign eligibility rules, search algo behavior, review-manipulation penalties).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-platform-selection`
- `tw-ecom-momo-operations`
- `tw-ecom-operations-promotion`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 5: Create `tw-ecom-momo-operations`**

```bash
mkdir -p tw-ecom-momo-operations/references tw-ecom-momo-operations/examples
touch tw-ecom-momo-operations/references/.gitkeep tw-ecom-momo-operations/examples/.gitkeep
cat > tw-ecom-momo-operations/SKILL.md <<'SKILL'
---
name: "tw-ecom-momo-operations"
description: "Operate on momo購物網 — listing approval workflow, price-matching rules, momo's next-day delivery SLA, campaign participation, and fast-fashion SKU rotation. Use when setting up or running momo operations, negotiating MOQ / margin with 採購, or participating in momo campaigns. Do NOT use for Shopee (different platform, different rules) or DTC. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: []
  related_skills: ["tw-ecom-platform-selection", "tw-ecom-shopee-operations", "tw-ecom-operations-promotion"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "momo", "marketplace"]
---

# momo購物網 Operations

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Onboarding product lines to momo via 採購 negotiation
- Managing momo listing approval and SKU rotation
- Planning momo campaign participation (momo 購物節, 雙11)
- Handling price-match events vs competitors
- Managing momo's same-day / next-day delivery SLA

## Do NOT use when

- Shopee operations → `tw-ecom-shopee-operations`
- DTC platform work → platform-specific skills

## Core concepts

TODO: momo vs Shopee/PChome differences, momo 採購 relationship, momo 富邦 payment ecosystem.

## Decision tree

TODO: when momo outperforms Shopee for a given category.

## Implementation guidance

TODO: listing, pricing, campaign, SLA management.

## Gotchas

TODO: 5-6 pitfalls (採購 relationship, price-war cascades, SLA penalties, SKU churn).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-platform-selection`
- `tw-ecom-shopee-operations`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 6: Verify 5 skeletons**

```bash
for d in tw-ecom-platform-selection tw-ecom-91app-integration tw-ecom-shopify-tw-integration tw-ecom-shopee-operations tw-ecom-momo-operations; do
  echo "=== $d ==="
  ls $d $d/references $d/examples
  head -5 $d/SKILL.md
done
```

Expected: 5 directories, each with SKILL.md + references/.gitkeep + examples/.gitkeep, frontmatter parsable.

- [ ] **Step 7: Commit**

```bash
git add tw-ecom-platform-selection tw-ecom-91app-integration tw-ecom-shopify-tw-integration tw-ecom-shopee-operations tw-ecom-momo-operations
git commit -m "feat(tw-ecom): add 5 platform-layer skeletons"
```

---

## Task 6: Create 4 payment skeletons

**Files (4 skill directories):**
- Create: `tw-ecom-payment-tappay/`
- Create: `tw-ecom-payment-ecpay/`
- Create: `tw-ecom-payment-jkopay/`
- Create: `tw-ecom-payment-dispute/`

Same skeleton shape as Task 5. Each with frontmatter + SKELETON banner + When to use + Do NOT use + TODO body.

- [ ] **Step 1: Create `tw-ecom-payment-tappay`**

```bash
mkdir -p tw-ecom-payment-tappay/references tw-ecom-payment-tappay/examples
touch tw-ecom-payment-tappay/references/.gitkeep tw-ecom-payment-tappay/examples/.gitkeep
cat > tw-ecom-payment-tappay/SKILL.md <<'SKILL'
---
name: "tw-ecom-payment-tappay"
description: "Integrate TapPay for Taiwan e-commerce — TapPay Web/iOS/Android SDK, 3DS 2.0 flow, Apple Pay / Google Pay / LINE Pay integration via TapPay, TCS (TapPay Card Service) for tokenized recurring payments. Use when TapPay is chosen as PSP, comparing TapPay vs NewebPay, or debugging 3DS flows. Do NOT use for other gateways. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: []
  related_skills: ["tw-payment-integration", "tw-ecom-payment-newebpay", "tw-ecom-payment-dispute"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "tappay", "fintech"]
---

# TapPay Integration for Taiwan E-Commerce

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating TapPay Web/iOS/Android SDK
- Adding Apple Pay / Google Pay / LINE Pay via TapPay
- Implementing TCS (tokenized recurring payments)
- Debugging 3DS 2.0 flow issues on TapPay
- Comparing TapPay vs NewebPay / ECPay for a specific use case

## Do NOT use when

- Generic TW payment gateway selection → `tw-payment-integration`
- Non-TapPay provider → their specific skill

## Core concepts

TODO: TapPay positioning (mobile-first), TapPay Direct vs TapPay Pay by Prime, TCS flow.

## Decision tree

TODO: when TapPay outperforms NewebPay/ECPay.

## Implementation guidance

TODO: Prime token acquisition, 3DS handling, TCS card binding + charge.

## Gotchas

TODO: 5-6 pitfalls (Prime token TTL, 3DS interstitial UX, TCS unbind on card expiry, Apple Pay domain verification, sandbox-to-prod merchant switch).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-payment-integration` for gateway comparison
- `tw-ecom-payment-dispute` for refund / chargeback handling

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-payment-ecpay`**

```bash
mkdir -p tw-ecom-payment-ecpay/references tw-ecom-payment-ecpay/examples
touch tw-ecom-payment-ecpay/references/.gitkeep tw-ecom-payment-ecpay/examples/.gitkeep
cat > tw-ecom-payment-ecpay/SKILL.md <<'SKILL'
---
name: "tw-ecom-payment-ecpay"
description: "Integrate 綠界 (ECPay) for Taiwan e-commerce — credit card, ATM, CVS 代碼, 超商取貨付款, and CheckMacValue signature. Use when ECPay is chosen as PSP, setting up logistics-payment combined flows (超取+COD), or comparing ECPay vs NewebPay. Do NOT use for non-ECPay providers. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: ["mcp-ecpay"]
  related_skills: ["tw-payment-integration", "tw-ecom-payment-newebpay", "tw-ecom-logistics-cvs"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "ecpay", "fintech"]
---

# ECPay (綠界) Integration

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Integrating ECPay for credit card / ATM / CVS 代碼 / 超商取貨付款
- Combining ECPay logistics + payment in one flow
- Computing / verifying CheckMacValue signatures
- Handling ECPay callback webhooks
- Reconciliation with ECPay merchant portal

## Do NOT use when

- Non-ECPay provider → specific skill for that provider
- Pure logistics (no payment) → `tw-ecom-logistics-cvs`

## Core concepts

TODO: ECPay positioning, CheckMacValue signature, the 超取+COD combined model.

## Decision tree

TODO: when ECPay's combined flow beats separating payment vs shipping.

## Implementation guidance

TODO: merchant setup, first txn, COD-at-pickup reconciliation.

## Gotchas

TODO: 5-6 pitfalls (CheckMacValue param ordering / URL encoding gotchas, COD settlement offset, 超取 failure refund flow, cross-sandbox credential leakage, 境外 card compatibility).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-payment-integration`
- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-payment-jkopay`**

```bash
mkdir -p tw-ecom-payment-jkopay/references tw-ecom-payment-jkopay/examples
touch tw-ecom-payment-jkopay/references/.gitkeep tw-ecom-payment-jkopay/examples/.gitkeep
cat > tw-ecom-payment-jkopay/SKILL.md <<'SKILL'
---
name: "tw-ecom-payment-jkopay"
description: "Integrate 街口支付 (JKOPay) for Taiwan e-commerce — web/app flow, JKO 幣 rewards, merchant settlement cycle, and scan-to-pay vs app-to-pay UX. Use when targeting younger TW demographic or integrating in-app JKO flow. Do NOT use for generic wallet integration (LINE Pay / Apple Pay handled elsewhere). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: []
  related_skills: ["tw-payment-integration", "tw-ecom-payment-tappay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "jkopay", "e-wallet"]
---

# 街口支付 (JKOPay) Integration

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Adding 街口支付 as a payment option (web or in-app)
- Reconciling JKO 幣 rewards / promotions
- Handling refund / void via JKO API
- Comparing JKO vs LINE Pay for the younger TW demographic

## Do NOT use when

- Generic wallet → covered elsewhere
- Non-JKO wallet → specific skill

## Core concepts

TODO: JKO merchant portal, demographic fit, 幣 rewards model.

## Decision tree

TODO: when JKO adds real conversion lift.

## Implementation guidance

TODO: merchant setup, web integration, app integration, refund.

## Gotchas

TODO: 5-6 pitfalls.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-payment-integration`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Create `tw-ecom-payment-dispute`**

```bash
mkdir -p tw-ecom-payment-dispute/references tw-ecom-payment-dispute/examples
touch tw-ecom-payment-dispute/references/.gitkeep tw-ecom-payment-dispute/examples/.gitkeep
cat > tw-ecom-payment-dispute/SKILL.md <<'SKILL'
---
name: "tw-ecom-payment-dispute"
description: "Handle Taiwan e-commerce payment disputes — credit card chargebacks (扣款爭議), refund across bimonthly boundaries (retro 折讓 trigger), acquirer dispute timelines, and evidence packets. Use when a customer files a chargeback, when issuing cross-period refunds that affect invoices, or when building internal dispute SOP. Do NOT use for simple in-period refunds (gateway-specific skills handle those). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: []
  related_skills: ["tw-payment-integration", "tw-ecom-payment-newebpay", "tw-ecom-payment-ecpay", "tw-ecom-invoice-void", "tw-ecom-compliance-consumer"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "payment", "dispute", "chargeback"]
---

# Payment Dispute Handling

> **STATUS: SKELETON** — body pending.

## When to use this skill

- A customer has filed a credit card chargeback
- Issuing a refund that crosses the bimonthly invoice boundary
- Building an internal dispute-handling SOP
- Preparing evidence packets for acquirer review
- Reconciling dispute outcomes against invoice state

## Do NOT use when

- Simple same-period refund → gateway-specific skill
- Consumer-law-level dispute (鑑賞期) → `tw-ecom-compliance-consumer`

## Core concepts

TODO: chargeback vs 退刷 vs 折讓, typical acquirer timelines, reason codes.

## Decision tree

TODO: given reason code → response path.

## Implementation guidance

TODO: evidence packet structure, 折讓 triggering logic, accounting entries.

## Gotchas

TODO: 5-6 pitfalls (bimonthly boundary, dual-refund double-charge, reason-code mismatch, evidence deadline, acquirer dialect differences).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-compliance-consumer`
- `tw-ecom-invoice-void`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 5: Verify 4 payment skeletons**

```bash
for d in tw-ecom-payment-tappay tw-ecom-payment-ecpay tw-ecom-payment-jkopay tw-ecom-payment-dispute; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

Expected: 4 complete skeleton directories.

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-payment-tappay tw-ecom-payment-ecpay tw-ecom-payment-jkopay tw-ecom-payment-dispute
git commit -m "feat(tw-ecom): add 4 payment-layer skeletons"
```

---

## Task 7: Create 4 logistics skeletons

**Files:**
- Create: `tw-ecom-logistics-cvs/` (CVS 超取 — 7-11, 全家, 萊爾富, OK)
- Create: `tw-ecom-logistics-home/` (宅配 — 黑貓, 宅配通, 新竹物流)
- Create: `tw-ecom-logistics-cold-chain/` (生鮮 / 冷凍)
- Create: `tw-ecom-logistics-cross-border/` (跨境出口)

Same skeleton pattern as Task 5/6. Each SKILL.md: frontmatter + SKELETON banner + When to use + Do NOT use + TODO body.

- [ ] **Step 1: Create `tw-ecom-logistics-cvs`**

```bash
mkdir -p tw-ecom-logistics-cvs/references tw-ecom-logistics-cvs/examples
touch tw-ecom-logistics-cvs/references/.gitkeep tw-ecom-logistics-cvs/examples/.gitkeep
cat > tw-ecom-logistics-cvs/SKILL.md <<'SKILL'
---
name: "tw-ecom-logistics-cvs"
description: "Ship via Taiwan convenience store pickup (7-11 賣貨便 / 全家 / 萊爾富 / OK) — store selection API, shipping-label format, pickup SLA, COD reconciliation, return shipping. Use when setting up CVS 超取 on a TW store, choosing which chains to support, or debugging label printing. Do NOT use for home delivery or cross-border. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: ["mcp-ecpay-logistics"]
  related_skills: ["tw-ecom-logistics-home", "tw-ecom-payment-ecpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cvs", "super-pickup"]
---

# Convenience Store Pickup (超商取貨)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Setting up CVS 超取 for a TW e-commerce store
- Choosing which chains to support (7-11 vs 全家 vs 萊爾富 vs OK)
- Integrating store-selection widget on checkout
- Handling COD (超取付款) reconciliation
- Managing CVS return flows

## Do NOT use when

- Home delivery (宅配) → `tw-ecom-logistics-home`
- Cross-border → `tw-ecom-logistics-cross-border`

## Core concepts

TODO: chain-specific quirks, 大宗 vs 一般 pickup, label formats, SLA.

## Decision tree

TODO: chain mix based on customer geo + avg order value.

## Implementation guidance

TODO: widget integration, label print, COD settlement, return flow.

## Gotchas

TODO: 5-6 pitfalls (label format divergence per chain, overweight rejection, address-to-store mismatch, COD settlement lag, store-closed edge case).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-payment-ecpay` (combined COD flow)

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-logistics-home`**

```bash
mkdir -p tw-ecom-logistics-home/references tw-ecom-logistics-home/examples
touch tw-ecom-logistics-home/references/.gitkeep tw-ecom-logistics-home/examples/.gitkeep
cat > tw-ecom-logistics-home/SKILL.md <<'SKILL'
---
name: "tw-ecom-logistics-home"
description: "Ship via Taiwan home delivery carriers — 黑貓宅急便, 宅配通, 新竹物流, 郵局. Use when setting up home delivery, choosing carriers by region / parcel size, integrating label printing, or handling redelivery. Do NOT use for CVS pickup (`tw-ecom-logistics-cvs`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-logistics-cvs", "tw-ecom-logistics-cold-chain"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "home-delivery"]
---

# Home Delivery Logistics (宅配)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Choosing among 黑貓 / 宅配通 / 新竹物流 / 郵局 for home delivery
- Integrating label API / batch printing
- Handling redelivery (二次配) scheduling
- Outer-island (離島) surcharge handling
- Time-slot delivery options

## Do NOT use when

- CVS pickup → `tw-ecom-logistics-cvs`
- Cold-chain / frozen → `tw-ecom-logistics-cold-chain`

## Core concepts

TODO: carrier pricing by 材積 vs weight, regional coverage differences, SLA promises.

## Decision tree

TODO: carrier pick by region / weight / 時效.

## Implementation guidance

TODO: label API, batch upload, tracking webhook.

## Gotchas

TODO: 5-6 pitfalls (材積-based upcharge, 離島 surcharge opacity, tracking update lag, failed delivery handling, fragile-item insurance).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-logistics-cvs`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-logistics-cold-chain`**

```bash
mkdir -p tw-ecom-logistics-cold-chain/references tw-ecom-logistics-cold-chain/examples
touch tw-ecom-logistics-cold-chain/references/.gitkeep tw-ecom-logistics-cold-chain/examples/.gitkeep
cat > tw-ecom-logistics-cold-chain/SKILL.md <<'SKILL'
---
name: "tw-ecom-logistics-cold-chain"
description: "Ship refrigerated / frozen products in Taiwan — 宅配通 宅配通冷藏 / 黑貓宅急便 低溫, cold-chain CVS pickup limitations, packaging (保冷劑 / 乾冰), and shelf-life SLA. Use for 生鮮 / 冷凍 / 冰品 / 藥品 delivery. Do NOT use for ambient-temperature shipping. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-logistics-home", "tw-ecom-compliance-product"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cold-chain"]
---

# Cold-Chain Logistics

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Shipping 生鮮 / 冷凍 / 冰品 / 藥品 / 保健品
- Choosing 冷藏 vs 冷凍 service level
- Packaging spec: 保冷劑 vs 乾冰, insulation grade
- Handling delivery-failure shelf-life loss
- Regional service coverage (離島, 偏遠地區)

## Do NOT use when

- Ambient-temp goods → `tw-ecom-logistics-home` or `-cvs`
- Regulatory aspects of 食品 / 藥品 → `tw-ecom-compliance-product`

## Core concepts

TODO: 冷藏 (0-7°C) vs 冷凍 (-18°C), packaging physics, cost structure.

## Decision tree

TODO: cold-chain required? carrier choice? package spec?

## Implementation guidance

TODO: vendor onboarding, test shipments, insurance, loss SOP.

## Gotchas

TODO: 5-6 pitfalls (Friday / weekend hold risk, 離島 no cold service, CVS cold-chain capacity, insurance claim friction, 乾冰 export restriction).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-logistics-home`
- `tw-ecom-compliance-product`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Create `tw-ecom-logistics-cross-border`**

```bash
mkdir -p tw-ecom-logistics-cross-border/references tw-ecom-logistics-cross-border/examples
touch tw-ecom-logistics-cross-border/references/.gitkeep tw-ecom-logistics-cross-border/examples/.gitkeep
cat > tw-ecom-logistics-cross-border/SKILL.md <<'SKILL'
---
name: "tw-ecom-logistics-cross-border"
description: "Handle cross-border shipping FROM or TO Taiwan — customs (報關 / 海關), HS codes, de minimis thresholds, carrier choices (DHL / FedEx / UPS / 郵局 國際), and returns friction. Use when a TW business ships internationally or sells cross-border to TW. Do NOT use for domestic TW shipping. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "logistics"
  related_mcps: []
  related_skills: ["tw-ecom-compliance-cross-border", "xborder-logistics", "xborder-sea-entry"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "logistics", "cross-border"]
---

# Cross-Border Logistics

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Shipping from TW to overseas customers
- Importing to TW for cross-border e-commerce
- Handling 報關 / de minimis / HS codes
- Choosing among DHL / FedEx / UPS / 郵局 國際
- Managing returns from overseas

## Do NOT use when

- Domestic TW → `tw-ecom-logistics-home` / `-cvs`
- Pure tax / compliance → `tw-ecom-compliance-cross-border`

## Core concepts

TODO: de minimis threshold, HS code basics, duty vs VAT, DDP vs DDU.

## Decision tree

TODO: carrier by destination / weight / speed / DDP preference.

## Implementation guidance

TODO: customs doc prep, label generation, tracking reconciliation.

## Gotchas

TODO: 5-6 pitfalls (HS misclassification, DDP total cost shock, returns black hole, restricted-items list, FTZ vs general customs).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-compliance-cross-border`
- `xborder-logistics`, `xborder-sea-entry`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 5: Verify 4 logistics skeletons**

```bash
for d in tw-ecom-logistics-cvs tw-ecom-logistics-home tw-ecom-logistics-cold-chain tw-ecom-logistics-cross-border; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-logistics-cvs tw-ecom-logistics-home tw-ecom-logistics-cold-chain tw-ecom-logistics-cross-border
git commit -m "feat(tw-ecom): add 4 logistics-layer skeletons"
```

---

## Task 8: Create 3 invoice skeletons

**Files:**
- Create: `tw-ecom-invoice-universalec/`
- Create: `tw-ecom-invoice-carrier/`
- Create: `tw-ecom-invoice-void/`

(Note: `tw-ecom-invoice-ezpay` is the complete skill from Task 4 — not a skeleton.)

- [ ] **Step 1: Create `tw-ecom-invoice-universalec`**

```bash
mkdir -p tw-ecom-invoice-universalec/references tw-ecom-invoice-universalec/examples
touch tw-ecom-invoice-universalec/references/.gitkeep tw-ecom-invoice-universalec/examples/.gitkeep
cat > tw-ecom-invoice-universalec/SKILL.md <<'SKILL'
---
name: "tw-ecom-invoice-universalec"
description: "Issue Taiwan e-invoices via UniversalEC (汎宇電商) using mcp-universalec-e-invoice (27 tools). Use when a merchant uses UniversalEC as their 加值服務中心 instead of ezPay, or when migrating between centers. Do NOT use for ezPay flows (`tw-ecom-invoice-ezpay`) or MOF direct integration (`tw-einvoice-guide`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: ["mcp-universalec-e-invoice"]
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay", "tw-ecom-invoice-carrier", "tw-ecom-invoice-void"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "universalec", "tax-compliance"]
---

# UniversalEC (汎宇電商) E-Invoice Integration

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Merchant uses UniversalEC as 加值服務中心
- Migrating between ezPay and UniversalEC
- Using UniversalEC-specific features (27 tools — richer than ezPay's 7)
- Reconciling UniversalEC ↔ MOF platform

## Do NOT use when

- Using ezPay → `tw-ecom-invoice-ezpay`
- Direct MOF → `tw-einvoice-guide`

## Core concepts

TODO: UniversalEC market position, tool-set breadth.

## Decision tree

TODO: UniversalEC vs ezPay trade-offs.

## Implementation guidance

TODO: the 27 tool categories, common flows.

## Gotchas

TODO.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-invoice-ezpay` (parallel skill)
- `tw-einvoice-guide`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-invoice-carrier`**

```bash
mkdir -p tw-ecom-invoice-carrier/references tw-ecom-invoice-carrier/examples
touch tw-ecom-invoice-carrier/references/.gitkeep tw-ecom-invoice-carrier/examples/.gitkeep
cat > tw-ecom-invoice-carrier/SKILL.md <<'SKILL'
---
name: "tw-ecom-invoice-carrier"
description: "Handle Taiwan e-invoice carriers (載具) — 手機條碼, 自然人憑證, 會員載具, plus 捐贈碼 donation flow. Covers carrier validation, scan-to-store UX, member-carrier consolidation, and prize-draw winner notification. Use when designing carrier scanning UX, debugging invalid-carrier rejections, or implementing donation-code flow. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: []
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "carrier"]
---

# E-Invoice Carriers (載具)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing carrier-scan UX at checkout
- Implementing member-carrier consolidation
- Adding 捐贈碼 donation flow
- Handling prize-draw (中獎) winner notification
- Debugging carrier-format rejections

## Do NOT use when

- Landscape overview → `tw-einvoice-guide`
- Specific 加值中心 API → `tw-ecom-invoice-ezpay` / `-universalec`

## Core concepts

TODO: carrier types, format specs, validation rules.

## Decision tree

TODO: which carrier to default to given context.

## Implementation guidance

TODO: scan widget, validation, member-carrier linking.

## Gotchas

TODO: 5-6 pitfalls.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-einvoice-guide`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-invoice-void`**

```bash
mkdir -p tw-ecom-invoice-void/references tw-ecom-invoice-void/examples
touch tw-ecom-invoice-void/references/.gitkeep tw-ecom-invoice-void/examples/.gitkeep
cat > tw-ecom-invoice-void/SKILL.md <<'SKILL'
---
name: "tw-ecom-invoice-void"
description: "Void Taiwan e-invoices within the same bimonthly window, or issue allowances (折讓) for cross-period corrections. Use when handling returns / refunds that affect invoice state. Do NOT use for initial issuance — see the 加值中心-specific skills. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "invoice"
  related_mcps: []
  related_skills: ["tw-einvoice-guide", "tw-ecom-invoice-ezpay", "tw-ecom-payment-dispute"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-invoice", "void", "allowance"]
---

# Invoice Void & Allowance (作廢 / 折讓)

> **STATUS: SKELETON** — body pending.

## When to use this skill

- A return / refund occurs within same bimonthly → void
- A return / refund crosses bimonthly boundary → 折讓
- Debugging invoice state inconsistency post-refund
- Building void / allowance SOP

## Do NOT use when

- Initial issuance → issuance-layer skill
- Tax filing impact → `tw-tax-basics`

## Core concepts

TODO: void vs 折讓, bimonthly boundary, accounting implications.

## Decision tree

TODO: given refund date vs issuance date → void or 折讓.

## Implementation guidance

TODO: API calls, accounting entries, customer notification.

## Gotchas

TODO: 5-6 pitfalls (boundary off-by-one, 字軌 reservation, lottery invalidation, allowance numbering).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-ecom-invoice-ezpay`
- `tw-ecom-payment-dispute`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Verify 3 invoice skeletons**

```bash
for d in tw-ecom-invoice-universalec tw-ecom-invoice-carrier tw-ecom-invoice-void; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

- [ ] **Step 5: Commit**

```bash
git add tw-ecom-invoice-universalec tw-ecom-invoice-carrier tw-ecom-invoice-void
git commit -m "feat(tw-ecom): add 3 invoice-layer skeletons"
```

---

## Task 9: Create 4 compliance skeletons

**Files:**
- Create: `tw-ecom-compliance-consumer/` (消保法鑑賞期)
- Create: `tw-ecom-compliance-product/` (食藥妝 / 保健 / 酒)
- Create: `tw-ecom-compliance-pdpa/` (e-commerce specific PDPA)
- Create: `tw-ecom-compliance-cross-border/` (cross-border tariff / VAT)

- [ ] **Step 1: Create `tw-ecom-compliance-consumer`**

```bash
mkdir -p tw-ecom-compliance-consumer/references tw-ecom-compliance-consumer/examples
touch tw-ecom-compliance-consumer/references/.gitkeep tw-ecom-compliance-consumer/examples/.gitkeep
cat > tw-ecom-compliance-consumer/SKILL.md <<'SKILL'
---
name: "tw-ecom-compliance-consumer"
description: "Comply with Taiwan consumer protection law (消保法) — 7-day 鑑賞期 scope and exceptions (生鮮 / 客製化 / 數位商品 / 藥品), return / refund timing, disclosure requirements, and unfair-term invalidation. Use when drafting T&C, handling return disputes, or assessing if a SKU is exempt from 鑑賞期. Do NOT use for PDPA (use `tw-ecom-compliance-pdpa`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "compliance"
  related_mcps: []
  related_skills: ["tw-ecom-compliance-product", "tw-ecom-compliance-pdpa", "tw-startup-legal", "law-contract"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "compliance", "consumer-protection"]
---

# Consumer Protection (消保法) Compliance

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Drafting e-commerce T&C for TW
- Handling a 鑑賞期 return dispute
- Assessing whether a SKU qualifies for 鑑賞期 exemption
- Training CS team on consumer-protection scripts
- Responding to 消保官 inquiry

## Do NOT use when

- PDPA → `tw-ecom-compliance-pdpa`
- Product-category regs → `tw-ecom-compliance-product`

## Core concepts

TODO: 消保法 §19 鑑賞期 7 天, exemptions (通訊交易解除權合理例外情事適用準則).

## Decision tree

TODO: SKU → 鑑賞期 yes / no / conditional.

## Implementation guidance

TODO: T&C template, return SOP, CS script.

## Gotchas

TODO: 5-6 pitfalls (opened packaging not = used, digital-goods exemption fine print, gift-with-purchase treatment, partial-return accounting).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-startup-legal`
- `law-contract`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-compliance-product`**

```bash
mkdir -p tw-ecom-compliance-product/references tw-ecom-compliance-product/examples
touch tw-ecom-compliance-product/references/.gitkeep tw-ecom-compliance-product/examples/.gitkeep
cat > tw-ecom-compliance-product/SKILL.md <<'SKILL'
---
name: "tw-ecom-compliance-product"
description: "Comply with Taiwan product-specific regulations — 食品 (食安法), 藥品 (藥事法), 化妝品 (化妝品衛生安全管理法), 保健食品, 酒類 (菸酒管理法), 醫療器材. Covers import permit, product registration, labeling, advertising restrictions, and e-commerce listing compliance. Use when selling any of these categories online. Do NOT use for general consumer protection (`tw-ecom-compliance-consumer`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "compliance"
  related_mcps: []
  related_skills: ["tw-ecom-compliance-consumer", "tw-healthcare-regulations", "tw-startup-legal"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "compliance", "product-regulation"]
---

# Product-Category Regulation

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Selling 食品 / 藥品 / 化妝品 / 保健食品 / 酒 / 醫療器材 online
- Preparing product-registration docs for TFDA
- Drafting listing copy that won't trigger advertising violations
- Handling import permits for regulated SKUs

## Do NOT use when

- General consumer protection → `tw-ecom-compliance-consumer`
- Non-TW regulatory work → out of scope

## Core concepts

TODO: category → governing law mapping, pre-market vs post-market obligations.

## Decision tree

TODO: category → permit required? labeling required? ad restrictions?

## Implementation guidance

TODO: registration flow, labeling checklist, ad-review process.

## Gotchas

TODO: 5-6 pitfalls (薬事法 §69 广告限制, 保健食品 vs 食品 boundary, 化妝品 pre-market change, 酒類 minor verification, parallel-import restrictions).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-healthcare-regulations` (for 醫療器材 depth)
- `tw-ecom-compliance-consumer`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-compliance-pdpa`**

```bash
mkdir -p tw-ecom-compliance-pdpa/references tw-ecom-compliance-pdpa/examples
touch tw-ecom-compliance-pdpa/references/.gitkeep tw-ecom-compliance-pdpa/examples/.gitkeep
cat > tw-ecom-compliance-pdpa/SKILL.md <<'SKILL'
---
name: "tw-ecom-compliance-pdpa"
description: "E-commerce-specific PDPA (個資法) compliance — member consent at signup, cookie consent, order / payment data retention, DSAR (data subject access request) handling, and cross-border data transfer for TW merchants. Use when building a TW e-commerce signup / CRM flow, responding to member data requests, or auditing cookies. For generic PDPA / GDPR basics see `law-gdpr-pdpa`. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "compliance"
  related_mcps: []
  related_skills: ["law-gdpr-pdpa", "tw-ecom-compliance-consumer", "tw-ecom-operations-crm-line-oa"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "compliance", "pdpa", "privacy"]
---

# E-Commerce PDPA Compliance

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing member signup consent for a TW store
- Building cookie-consent banner for TW traffic
- Responding to DSAR (resident data subject access request)
- Designing data-retention policy for order / payment data
- Cross-border transfer (TW → AWS US / GCP APAC)

## Do NOT use when

- Generic PDPA / GDPR concepts → `law-gdpr-pdpa`
- Marketing consent for LINE OA → `tw-ecom-operations-crm-line-oa`

## Core concepts

TODO: 個資法 §5 specific-purpose principle, 第八條 告知義務, 蒐集 vs 處理 vs 利用 split.

## Decision tree

TODO: data flow → consent form design.

## Implementation guidance

TODO: consent form template, DSAR SOP, retention schedule, cross-border transfer assessment.

## Gotchas

TODO: 5-6 pitfalls (opt-in vs opt-out confusion, third-party embed leakage, employee access logging, data-breach 72hr notification).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `law-gdpr-pdpa`
- `tw-ecom-operations-crm-line-oa`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Create `tw-ecom-compliance-cross-border`**

```bash
mkdir -p tw-ecom-compliance-cross-border/references tw-ecom-compliance-cross-border/examples
touch tw-ecom-compliance-cross-border/references/.gitkeep tw-ecom-compliance-cross-border/examples/.gitkeep
cat > tw-ecom-compliance-cross-border/SKILL.md <<'SKILL'
---
name: "tw-ecom-compliance-cross-border"
description: "Tax and regulatory compliance for cross-border e-commerce involving Taiwan — import VAT (5%), duty thresholds, 報單 filing, 境外電商 sales-tax registration, cross-border sales to TW. Use when shipping to/from TW, setting up境外電商 tax registration, or handling HS-code audits. Do NOT use for domestic-only TW ops. STATUS: SKELETON — body pending."
metadata:
  category: "WP-05 台灣創業"
  domain: "ecommerce-tw"
  layer: "compliance"
  related_mcps: []
  related_skills: ["tw-ecom-logistics-cross-border", "tw-tax-basics", "xborder-sea-entry"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "compliance", "cross-border", "tax"]
---

# Cross-Border Compliance

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Setting up 境外電商 Taiwan sales tax registration
- Managing de minimis threshold for inbound parcels
- HS-code classification and 報單 filing
- Cross-border returns (duty-paid rework)
- VAT reconciliation on parallel-import goods

## Do NOT use when

- Pure logistics → `tw-ecom-logistics-cross-border`
- Domestic 營業稅 only → `tw-tax-basics`

## Core concepts

TODO: 境外電商 §6-1, de minimis evolution, 報單 types (一般 vs 簡易).

## Decision tree

TODO: shipment → classification → filing path.

## Implementation guidance

TODO: registration, filing, reconciliation.

## Gotchas

TODO: 5-6 pitfalls.

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `tw-tax-basics`
- `tw-ecom-logistics-cross-border`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 5: Verify 4 compliance skeletons**

```bash
for d in tw-ecom-compliance-consumer tw-ecom-compliance-product tw-ecom-compliance-pdpa tw-ecom-compliance-cross-border; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-compliance-consumer tw-ecom-compliance-product tw-ecom-compliance-pdpa tw-ecom-compliance-cross-border
git commit -m "feat(tw-ecom): add 4 compliance-layer skeletons"
```

---

## Task 10: Create 4 operations skeletons

**Files:**
- Create: `tw-ecom-operations-promotion/`
- Create: `tw-ecom-operations-pricing/`
- Create: `tw-ecom-operations-crm-line-oa/`
- Create: `tw-ecom-operations-customer-service/`

- [ ] **Step 1: Create `tw-ecom-operations-promotion`**

```bash
mkdir -p tw-ecom-operations-promotion/references tw-ecom-operations-promotion/examples
touch tw-ecom-operations-promotion/references/.gitkeep tw-ecom-operations-promotion/examples/.gitkeep
cat > tw-ecom-operations-promotion/SKILL.md <<'SKILL'
---
name: "tw-ecom-operations-promotion"
description: "Run Taiwan e-commerce promotional campaigns — 雙11, 618, 年中慶, 雙12, 週年慶, 母親節. Covers promo calendar, stacking rules across platforms, 檔期 pricing strategy, inventory allocation, and post-campaign 退貨 handling. Use when planning a specific campaign or building a year-round 檔期 schedule. Do NOT use for ad ROI measurement (use `ecom-promo-roi`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "operations"
  related_mcps: []
  related_skills: ["ecom-promo-roi", "tw-ecom-operations-pricing", "tw-ecom-operations-customer-service", "tw-ecom-shopee-operations", "tw-ecom-momo-operations"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "promotion", "campaign"]
---

# Taiwan Promotional Campaign Operations

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Planning a specific 檔期 (雙11, 618, 年中慶, etc.)
- Building year-round 檔期 calendar
- Cross-platform promo stacking design
- Inventory allocation across DTC + marketplace channels during peak
- Post-campaign 退貨 / 爭議 handling

## Do NOT use when

- Ad ROI measurement → `ecom-promo-roi`
- Pricing strategy in isolation → `tw-ecom-operations-pricing`

## Core concepts

TODO: TW promo calendar, stacking hierarchy, DTC vs marketplace behavior during peaks.

## Decision tree

TODO: which 檔期 to participate in, channel mix, discount depth.

## Implementation guidance

TODO: 檔期 plan template, inventory buffer, support staffing.

## Gotchas

TODO: 5-6 pitfalls (stacking over-discount, platform fee waiver traps, inventory over-commit, return spike 2 weeks after peak, marketplace cancelation penalties).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `ecom-promo-roi`
- `tw-ecom-operations-pricing`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-operations-pricing`**

```bash
mkdir -p tw-ecom-operations-pricing/references tw-ecom-operations-pricing/examples
touch tw-ecom-operations-pricing/references/.gitkeep tw-ecom-operations-pricing/examples/.gitkeep
cat > tw-ecom-operations-pricing/SKILL.md <<'SKILL'
---
name: "tw-ecom-operations-pricing"
description: "Set prices for Taiwan e-commerce — 含稅 vs 未稅 presentation, price-ending conventions (0/8/9 endings), marketplace price-match rules (momo best-price), 檔期 discount planning, and cross-channel price-parity. Use when pricing a new SKU for TW, rebalancing prices across platforms, or designing a 檔期 discount ladder. Do NOT use for generic pricing theory (use `biz-pricing-strategy`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "operations"
  related_mcps: []
  related_skills: ["biz-pricing-strategy", "biz-unit-economics", "tw-ecom-operations-promotion", "algo-price-elasticity"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "pricing"]
---

# Taiwan E-Commerce Pricing

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Pricing a new SKU for TW market
- Cross-channel price-parity (DTC vs marketplace)
- 檔期 discount ladder design
- Price-match response to competitor flash sales
- Repricing after cost / FX shift

## Do NOT use when

- Generic pricing theory → `biz-pricing-strategy`
- Elasticity modeling → `algo-price-elasticity`

## Core concepts

TODO: 含稅 convention, price-ending psychology, marketplace price-match rules.

## Decision tree

TODO: channel mix → price matrix design.

## Implementation guidance

TODO: price sheet template, repricing cadence, guardrails.

## Gotchas

TODO: 5-6 pitfalls (momo best-price penalty cascade, marketplace coupon masking, 含稅 display error, FX-driven loss, MAP violation).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `biz-pricing-strategy`
- `tw-ecom-operations-promotion`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Create `tw-ecom-operations-crm-line-oa`**

```bash
mkdir -p tw-ecom-operations-crm-line-oa/references tw-ecom-operations-crm-line-oa/examples
touch tw-ecom-operations-crm-line-oa/references/.gitkeep tw-ecom-operations-crm-line-oa/examples/.gitkeep
cat > tw-ecom-operations-crm-line-oa/SKILL.md <<'SKILL'
---
name: "tw-ecom-operations-crm-line-oa"
description: "Run CRM and member retention via LINE Official Account — broadcast cost model, rich menu, auto-response, tagging, 1-to-1 chat, and LINE Pay integration. Use when designing LINE OA strategy for a TW brand, segmenting members for broadcasts, or measuring LINE OA ROI. Do NOT use for generic CRM (use `ecom-rfm-analysis` or `biz-cac-ltv`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "operations"
  related_mcps: []
  related_skills: ["ecom-rfm-analysis", "biz-cac-ltv", "tw-ecom-compliance-pdpa"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "crm", "line-oa"]
---

# LINE OA CRM Operations

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing LINE OA strategy for a TW brand
- Setting up rich menu, auto-response, tagging
- Segmenting members for broadcasts
- Integrating LINE Pay into OA flow
- Measuring LINE OA ROI vs EDM

## Do NOT use when

- Generic RFM → `ecom-rfm-analysis`
- CAC/LTV framework → `biz-cac-ltv`

## Core concepts

TODO: LINE OA tier pricing (輕用量 / 中用量 / 高用量), broadcast vs narrowcast cost asymmetry, tagging strategy.

## Decision tree

TODO: member behavior → tag → channel.

## Implementation guidance

TODO: onboarding flow, tagging logic, broadcast template, ROI measurement.

## Gotchas

TODO: 5-6 pitfalls (tier upgrade mid-month cost, blocked-user bloat, PDPA consent for broadcast, 1-to-1 latency during peak, LINE Notify deprecation impact).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `ecom-rfm-analysis`
- `tw-ecom-compliance-pdpa`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 4: Create `tw-ecom-operations-customer-service`**

```bash
mkdir -p tw-ecom-operations-customer-service/references tw-ecom-operations-customer-service/examples
touch tw-ecom-operations-customer-service/references/.gitkeep tw-ecom-operations-customer-service/examples/.gitkeep
cat > tw-ecom-operations-customer-service/SKILL.md <<'SKILL'
---
name: "tw-ecom-operations-customer-service"
description: "Taiwan e-commerce customer service — LINE / Messenger / email / phone channel mix, 消保法鑑賞期 scripts, PTT/Dcard reputation monitoring, 負評 response, and SLA targets for the TW market. Use when designing CS SOP, training CS agents, or responding to viral 負評. Do NOT use for generic chatbot design (use `cs-chatbot-design`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "operations"
  related_mcps: []
  related_skills: ["cs-sop", "cs-chatbot-design", "tw-ecom-compliance-consumer", "pr-crisis-response"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "customer-service"]
---

# Taiwan E-Commerce Customer Service

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Designing a CS SOP for a TW store
- Training agents on 鑑賞期 / 退貨 scripts
- Monitoring PTT / Dcard / mobile01 for 負評
- Responding to a viral 負評 thread
- Setting SLA targets (first-response / resolution)

## Do NOT use when

- Generic chatbot design → `cs-chatbot-design`
- Crisis PR (non-CS) → `pr-crisis-response`

## Core concepts

TODO: channel mix, TW consumer complaint culture, PTT / Dcard etiquette.

## Decision tree

TODO: complaint → channel → script template.

## Implementation guidance

TODO: SOP template, escalation ladder, monitoring setup.

## Gotchas

TODO: 5-6 pitfalls (鑑賞期 over-promise, PTT Streisand effect, LINE 1-to-1 burnout, negative-review response template pitfalls, 消保官 tone).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `cs-sop`
- `tw-ecom-compliance-consumer`
- `pr-crisis-response`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 5: Verify 4 operations skeletons**

```bash
for d in tw-ecom-operations-promotion tw-ecom-operations-pricing tw-ecom-operations-crm-line-oa tw-ecom-operations-customer-service; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

- [ ] **Step 6: Commit**

```bash
git add tw-ecom-operations-promotion tw-ecom-operations-pricing tw-ecom-operations-crm-line-oa tw-ecom-operations-customer-service
git commit -m "feat(tw-ecom): add 4 operations-layer skeletons"
```

---

## Task 11: Create 2 analytics skeletons

**Files:**
- Create: `tw-ecom-analytics-ga4/`
- Create: `tw-ecom-analytics-benchmarks/`

- [ ] **Step 1: Create `tw-ecom-analytics-ga4`**

```bash
mkdir -p tw-ecom-analytics-ga4/references tw-ecom-analytics-ga4/examples
touch tw-ecom-analytics-ga4/references/.gitkeep tw-ecom-analytics-ga4/examples/.gitkeep
cat > tw-ecom-analytics-ga4/SKILL.md <<'SKILL'
---
name: "tw-ecom-analytics-ga4"
description: "Implement GA4 for Taiwan e-commerce — Enhanced Ecommerce events (view_item, add_to_cart, begin_checkout, purchase), TW-specific parameter conventions (含稅 revenue, NT$ currency, 統編 as user property), Looker Studio reporting, and Big Query export. Use when instrumenting a TW store with GA4 or auditing existing GA4 setup. Do NOT use for generic analytics (use `ecom-analytics`). STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "analytics"
  related_mcps: []
  related_skills: ["ecom-analytics", "data-cohort-analysis", "tw-ecom-analytics-benchmarks"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "ga4", "analytics"]
---

# GA4 for Taiwan E-Commerce

> **STATUS: SKELETON** — body pending.

## When to use this skill

- Instrumenting a TW store with GA4 Enhanced Ecommerce
- Auditing an existing GA4 setup for TW conventions
- Designing Looker Studio reports for TW KPI
- Setting up BigQuery export
- Attributing across LINE OA / marketplace channels

## Do NOT use when

- Generic analytics → `ecom-analytics`
- Benchmarks only → `tw-ecom-analytics-benchmarks`

## Core concepts

TODO: GA4 event model, 含稅 revenue handling, currency = TWD, content_group usage for 檔期.

## Decision tree

TODO: event → parameter mapping for TW conventions.

## Implementation guidance

TODO: dataLayer template, tag setup, consent mode, BigQuery export.

## Gotchas

TODO: 5-6 pitfalls (含稅 double-count, cross-domain marketplace attribution, LINE IAB tracking block, consent-mode revenue undercount, parameter cardinality limits).

## IRON LAW

TODO.

## Output Format

TODO.

## Related

- `ecom-analytics`
- `tw-ecom-analytics-benchmarks`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 2: Create `tw-ecom-analytics-benchmarks`**

```bash
mkdir -p tw-ecom-analytics-benchmarks/references tw-ecom-analytics-benchmarks/examples
touch tw-ecom-analytics-benchmarks/references/.gitkeep tw-ecom-analytics-benchmarks/examples/.gitkeep
cat > tw-ecom-analytics-benchmarks/SKILL.md <<'SKILL'
---
name: "tw-ecom-analytics-benchmarks"
description: "Taiwan e-commerce benchmark ranges for CVR, ROAS, LTV, AOV, repeat rate, cart-abandon — segmented by vertical (3C, 美妝, 服飾, 母嬰, 生鮮) and channel (DTC, Shopee, momo). Use when a TW merchant asks 'is my CVR / ROAS good?' or when sizing a business case. Source discipline: cite industry report or vendor data; mark undocumented ranges as estimates. STATUS: SKELETON — body pending."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "analytics"
  related_mcps: []
  related_skills: ["ecom-analytics", "tw-ecom-analytics-ga4", "biz-unit-economics", "biz-cac-ltv"]
  last_verified: "2026-04"
  status: "skeleton"
  tags: ["taiwan", "e-commerce", "benchmarks", "metrics"]
---

# Taiwan E-Commerce Benchmarks

> **STATUS: SKELETON** — body pending.

## When to use this skill

- A merchant asks "is my CVR / ROAS / LTV good?"
- Sizing a business case (revenue / ad-spend projections)
- Comparing performance across verticals or channels
- Investor / banker deck benchmarks

## Do NOT use when

- Instrumentation itself → `tw-ecom-analytics-ga4`
- Unit economics framework → `biz-unit-economics`

## Core concepts

TODO: benchmark tables by vertical × channel, sourced ranges with citations.

## Decision tree

TODO: merchant profile → applicable benchmark row.

## Implementation guidance

TODO: comparison template, outlier-flag criteria, what to do when outside range.

## Gotchas

TODO: 5-6 pitfalls (stale benchmarks, vertical misclassification, channel-mix distortion, attribution-model divergence, peak-period distortion).

## IRON LAW

TODO (candidate: "All benchmark ranges must cite source + year. An uncited number is worse than no number.").

## Output Format

TODO.

## Related

- `ecom-analytics`
- `biz-unit-economics`, `biz-cac-ltv`

_Last verified: 2026-04_
SKILL
```

- [ ] **Step 3: Verify 2 analytics skeletons**

```bash
for d in tw-ecom-analytics-ga4 tw-ecom-analytics-benchmarks; do
  echo "=== $d ==="; ls $d $d/references $d/examples; head -5 $d/SKILL.md
done
```

- [ ] **Step 4: Commit**

```bash
git add tw-ecom-analytics-ga4 tw-ecom-analytics-benchmarks
git commit -m "feat(tw-ecom): add 2 analytics-layer skeletons"
```

---

## Task 12: Write domain navigation doc

**Files:**
- Create: `docs/domains/tw-ecommerce.md`

This is the **domain map** — the single entry point for "I need to do Taiwan e-commerce work, where do I start?"

- [ ] **Step 1: Write `docs/domains/tw-ecommerce.md`**

```bash
cat > docs/domains/tw-ecommerce.md <<'DOMAIN'
# Taiwan E-Commerce Domain Map

**Last updated:** 2026-04-19
**Re-verification cadence:** Quarterly (next: 2026-07)

Taiwan e-commerce brings together platform integration, payment gateways, logistics carriers, e-invoice compliance, consumer-protection law, operational playbooks, and analytics conventions that are distinct from generic e-commerce. This map indexes every skill that applies, whether it's new (`tw-ecom-*`), existing Taiwan-specific (`tw-*`), or existing generic e-commerce (`ecom-*`).

## Who this domain is for

- Founders running a Taiwan D2C brand (Shopline / 91APP / Shopify)
- Marketplace sellers (Shopee / momo / PChome)
- Agencies / SI building stores for TW clients
- Asgard plugin builders assembling a TW e-commerce bundle

## Decision tree — where to start

```
I need to...

├── Choose a platform / channel mix
│   └── tw-ecom-platform-selection
│
├── Integrate with a specific platform
│   ├── Shopline → tw-ecom-shopline-integration  ★ reference
│   ├── 91APP → tw-ecom-91app-integration
│   ├── Shopify TW → tw-ecom-shopify-tw-integration
│   ├── Shopee → tw-ecom-shopee-operations
│   └── momo → tw-ecom-momo-operations
│
├── Pick a payment gateway
│   ├── Landscape / selection → tw-payment-integration  (existing)
│   ├── NewebPay deep → tw-ecom-payment-newebpay  ★ reference
│   ├── ECPay deep → tw-ecom-payment-ecpay
│   ├── TapPay deep → tw-ecom-payment-tappay
│   ├── 街口 → tw-ecom-payment-jkopay
│   └── Chargeback / 折讓 → tw-ecom-payment-dispute
│
├── Ship products
│   ├── CVS 超取 → tw-ecom-logistics-cvs
│   ├── 宅配 → tw-ecom-logistics-home
│   ├── Cold-chain → tw-ecom-logistics-cold-chain
│   └── Cross-border → tw-ecom-logistics-cross-border
│
├── Issue e-invoices
│   ├── Landscape → tw-einvoice-guide  (existing)
│   ├── ezPay → tw-ecom-invoice-ezpay  ★ reference
│   ├── UniversalEC → tw-ecom-invoice-universalec
│   ├── Carriers (載具) → tw-ecom-invoice-carrier
│   └── Void / 折讓 → tw-ecom-invoice-void
│
├── Stay compliant
│   ├── 消保法 鑑賞期 → tw-ecom-compliance-consumer
│   ├── 食藥妝 / 酒 → tw-ecom-compliance-product
│   ├── PDPA → tw-ecom-compliance-pdpa
│   ├── Cross-border tax → tw-ecom-compliance-cross-border
│   ├── Startup legal basics → tw-startup-legal  (existing)
│   └── Tax filing → tw-tax-basics  (existing)
│
├── Run operations
│   ├── 檔期 / 雙11 → tw-ecom-operations-promotion
│   ├── Pricing → tw-ecom-operations-pricing
│   ├── LINE OA CRM → tw-ecom-operations-crm-line-oa
│   ├── Customer service → tw-ecom-operations-customer-service
│   ├── Generic RFM → ecom-rfm-analysis  (existing)
│   ├── Promo ROI → ecom-promo-roi  (existing)
│   └── Inventory health → ecom-inventory-health  (existing)
│
└── Measure
    ├── GA4 setup → tw-ecom-analytics-ga4
    ├── TW benchmarks → tw-ecom-analytics-benchmarks
    ├── Generic ecom analytics → ecom-analytics  (existing)
    └── Cohort analysis → data-cohort-analysis  (existing)
```

## Related MCPs

| MCP | Tools | Covered by |
|---|---:|---|
| `mcp-shopline` | 143 | `tw-ecom-shopline-integration` |
| `mcp-91app` | 17 | `tw-ecom-91app-integration` (skeleton) |
| `mcp-newebpay` | 8 | `tw-ecom-payment-newebpay` |
| `mcp-ezpay-einvoice` | 7 | `tw-ecom-invoice-ezpay` |
| `mcp-universalec-e-invoice` | 27 | `tw-ecom-invoice-universalec` (skeleton) |
| `mcp-ecpay` | — | `tw-ecom-payment-ecpay` (skeleton) |
| `mcp-ecpay-logistics` | — | `tw-ecom-logistics-cvs` (skeleton) |

(★ = content-complete reference skill. Everything else is either content-complete already or a skeleton pending content. See `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md` for scope.)

## Skill status legend

- **Complete** (no marker): full content, merge-ready
- **Skeleton**: frontmatter + "when to use" only; body pending a follow-up branch. `status: skeleton` in frontmatter.

## Re-verification

The domain touches fast-moving regulation (鑑賞期 exemption list, 境外電商 VAT), vendor fees (NewebPay / ezPay / TapPay rate cards), and platform mechanics (Shopee tier rules). Quarterly cadence:

- Scan each skill's `last_verified` metadata
- If > 6 months stale, open an issue
- Touch fee / rate / regulation numbers: cite source + date in the skill

## See also

- `TODO.md` — skeleton backlog with priority order
- `CONTRIBUTING.md` — how to fill in a skeleton or add a new skill
- `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md` — design rationale
DOMAIN
```

- [ ] **Step 2: Verify**

```bash
wc -l docs/domains/tw-ecommerce.md
head -20 docs/domains/tw-ecommerce.md
```

Expected: 100-200 lines.

- [ ] **Step 3: Commit**

```bash
git add docs/domains/
git commit -m "docs(domains): add tw-ecommerce domain navigation"
```

---

## Task 13: Write CONTRIBUTING.md

**Files:**
- Create: `CONTRIBUTING.md`

Minimal contribution guide scoped to what a skill author needs to know. Lean on `CLAUDE.md` for the authoritative anti-pattern list — don't duplicate.

- [ ] **Step 1: Write CONTRIBUTING.md**

```bash
cat > CONTRIBUTING.md <<'CONTRIB'
# Contributing to Asgard Skills

Thanks for contributing. This repo is a versioned library of coding-agent methodology — 263+ flat `{category}-{slug}/` skill directories at the repo root. Read [`CLAUDE.md`](CLAUDE.md) first; it is the source of truth for repo conventions.

## Quick start — add a new skill

1. Pick a name: `{category}-{slug}`, all lowercase, hyphen-separated. Categories are listed in `CLAUDE.md`.
2. Create the directory with the required sub-structure:
   ```bash
   mkdir -p <category>-<slug>/{references,examples}
   touch <category>-<slug>/{references,examples}/.gitkeep
   ```
3. Write `<category>-<slug>/SKILL.md`. Required sections:
   - YAML frontmatter: `name`, `description`, `metadata` (with `tags`; optional `domain`, `layer`, `related_mcps`, `related_skills`, `last_verified`)
   - Body ≤ 500 lines / 5,000 tokens
   - IRON LAW block (non-obvious constraint, not a truism)
   - Output Format template
   - Gotchas section (5-6 specific, actionable pitfalls — not generic advice)
4. Offload heavy content to `references/*.md`. Put runnable samples in `examples/sample_scenario.md`.
5. If the skill fits an existing domain, update that domain's `docs/domains/*.md` index.

## Quality bar

Skills are reviewed against the 8 anti-patterns documented in `CLAUDE.md` §"Quality Audit Anti-Patterns to Avoid":

1. Phantom Trigger — description over-matches
2. Kitchen Sink — body crammed with everything
3. Over-Teaching — explains basics the agent already knows
4. Missing Gotchas — generic advice, not specific traps
5. Procedural Straitjacket — too rigid where judgment is needed
6. Truism Iron Law — rule any competent agent would already follow
7. Non-verifiable Sample I/O — algo skills must have exact computable I/O
8. Broken `references/` pointers — SKILL.md references files that don't exist

If your skill fails any of these, the PR will be sent back.

## Frontmatter reference

```yaml
---
name: "category-slug"
description: "WHAT the skill does + WHEN to use it + triggering phrases. Under 1024 chars. No XML angle brackets."
metadata:
  category: "WP-XX <category label>"
  tags: ["topic", "keyword"]
  # Optional domain/layer fields, used when the skill is part of a curated domain:
  domain: "ecommerce-tw"
  layer: "payment"
  related_mcps: ["mcp-shopline"]
  related_skills: ["other-skill-name"]
  last_verified: "2026-04"
---
```

Reserved — do NOT use in skill names: `claude`, `anthropic`.

Not a repo convention — do NOT add: per-skill `license:` field (repo-wide MIT applies).

## Skeletons

A skeleton is a frontmatter + "When to use" only SKILL.md, with `status: skeleton` in the metadata. Skeletons exist to reserve a slot in a domain while content is pending. They must include:

- A `> **STATUS: SKELETON** — body pending.` banner at the top of the body
- Recommendation to the agent to prefer a named alternative (usually the nearest complete reference skill)
- `TODO` placeholder sections (not deleted — the structure stays so the filler knows what to write)

Skeletons are acceptable in a PR if they belong to an approved domain roadmap. Otherwise, ship content-complete skills only.

## Deterministic scripts

If a skill ships a calculator script, follow `CLAUDE.md` §"Scripts":

- Single file in `<skill>/scripts/`
- `--help`, `--input <json>`, `--verify` flags
- Pure stdlib unless documented
- Built-in `verify()` with ≥ 3 assertions

Test: `python <skill>/scripts/<script>.py --verify`

## Domain docs

A domain (e.g., `docs/domains/tw-ecommerce.md`) is a **navigation hub**, not a skill. It indexes new + existing skills that apply to a workflow. When you add a skill that belongs to an existing domain, update the index in the same PR.

## Pull requests

- Branch from `main`.
- One coherent change per PR — either one content-complete skill, or one domain bootstrap (infra + skeletons + a couple of reference skills), not a grab-bag.
- Commit messages: `<type>(<scope>): <subject>`. Types: `feat`, `docs`, `fix`, `chore`. Scope examples: `tw-ecom`, `algo-ecom`, `repo`.
- Reference the design spec in `docs/superpowers/specs/` if the PR implements one.
- Run the verification commands listed in the plan (frontmatter parse, description length, line count) before pushing.

## Getting help

Open an issue with `question` label, or reference the design spec for the domain you're working in.
CONTRIB
```

- [ ] **Step 2: Verify**

```bash
wc -l CONTRIBUTING.md
head -30 CONTRIBUTING.md
```

Expected: 80-150 lines.

- [ ] **Step 3: Commit**

```bash
git add CONTRIBUTING.md
git commit -m "docs: add CONTRIBUTING.md"
```

---

## Task 14: Update README.md + README.en.md

**Files:**
- Modify: `README.md`
- Modify: `README.en.md`

Add a one-paragraph pointer to `docs/domains/` and `CONTRIBUTING.md`. Do NOT restructure the README.

- [ ] **Step 1: Inspect current README structure**

```bash
head -40 README.md
head -40 README.en.md
```

Look for an existing "## See also" / "相關文件" / "## Contributing" section. Insert near it. If none exists, add after the main intro paragraph.

- [ ] **Step 2: Add the pointer block to README.md (zh-TW)**

Find a natural spot (likely near the end, before any license section). Append this block:

```markdown

## Domain 導航

特定領域的 skill 組織索引放在 [`docs/domains/`](docs/domains/)：

- [`tw-ecommerce.md`](docs/domains/tw-ecommerce.md) — 台灣電商（平台、金流、物流、發票、法遵、營運、分析）

## 貢獻指南

請見 [`CONTRIBUTING.md`](CONTRIBUTING.md)。提交新 skill 前務必先讀 [`CLAUDE.md`](CLAUDE.md) 了解目錄與品質標準。
```

Use the Edit tool with the appropriate `old_string` (the surrounding text you confirmed exists) and the block above as `new_string`.

- [ ] **Step 3: Add the pointer block to README.en.md**

Same idea, English:

```markdown

## Domain Navigation

Curated skill indexes for specific workflows live in [`docs/domains/`](docs/domains/):

- [`tw-ecommerce.md`](docs/domains/tw-ecommerce.md) — Taiwan e-commerce (platform, payment, logistics, invoice, compliance, operations, analytics)

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Before submitting a new skill, read [`CLAUDE.md`](CLAUDE.md) for directory layout and quality standards.
```

- [ ] **Step 4: Verify**

```bash
grep -n "docs/domains" README.md README.en.md
grep -n "CONTRIBUTING" README.md README.en.md
```

Expected: both files match.

- [ ] **Step 5: Commit**

```bash
git add README.md README.en.md
git commit -m "docs(readme): point to docs/domains/ and CONTRIBUTING.md"
```

---

## Task 15: Update TODO.md with skeleton backlog

**Files:**
- Modify: `TODO.md`

Append a new priority section for the 26 skeleton skills, organized by layer with follow-up branch names from the design spec.

- [ ] **Step 1: Append new section to TODO.md**

Use Edit tool. Find the marker `## 🟡 Medium Priority — Skill Quality Improvements` (or whichever section is the current #1 priority), and insert **before it** a new section:

```markdown
## 🟡 Medium Priority — tw-ecommerce Skeleton Backlog

Added 2026-04-19 on branch `feat/tw-ecommerce-domain`. 26 skeletons with frontmatter + "when to use" only — bodies pending.

**Design spec:** `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md`
**Domain map:** `docs/domains/tw-ecommerce.md`

Each follow-up branch fills in one layer:

| Branch | Skills to fill |
|---|---|
| `feat/tw-ecom-platform-skills` | `tw-ecom-platform-selection`, `tw-ecom-91app-integration`, `tw-ecom-shopify-tw-integration`, `tw-ecom-shopee-operations`, `tw-ecom-momo-operations` |
| `feat/tw-ecom-payment-deep-skills` | `tw-ecom-payment-tappay`, `tw-ecom-payment-ecpay`, `tw-ecom-payment-jkopay`, `tw-ecom-payment-dispute` |
| `feat/tw-ecom-logistics-skills` | `tw-ecom-logistics-cvs`, `tw-ecom-logistics-home`, `tw-ecom-logistics-cold-chain`, `tw-ecom-logistics-cross-border` |
| `feat/tw-ecom-invoice-deep-skills` | `tw-ecom-invoice-universalec`, `tw-ecom-invoice-carrier`, `tw-ecom-invoice-void` |
| `feat/tw-ecom-compliance-skills` | `tw-ecom-compliance-consumer`, `tw-ecom-compliance-product`, `tw-ecom-compliance-pdpa`, `tw-ecom-compliance-cross-border` |
| `feat/tw-ecom-operations-skills` | `tw-ecom-operations-promotion`, `tw-ecom-operations-pricing`, `tw-ecom-operations-crm-line-oa`, `tw-ecom-operations-customer-service` |
| `feat/tw-ecom-analytics-skills` | `tw-ecom-analytics-ga4`, `tw-ecom-analytics-benchmarks` |

**Content-source discipline** (per design spec §5.2):
- Platform / payment / invoice skeletons should wait for official docs + MCP snapshots before writing; avoid fabricating fee rates.
- Compliance skeletons must cite the law article (e.g., `消保法 §19`) + date.
- Analytics benchmarks must cite industry source + year.
- Mark unsourced numbers as `TODO: verify with <source>` — don't ship.

**Deliberately excluded from the roadmap:** `tw-ecom-advertising`, `tw-ecom-reporting`, `tw-ecom-cyberbiz-integration` (see design spec §6.3).

---
```

- [ ] **Step 2: Verify insertion**

```bash
grep -n "tw-ecommerce Skeleton Backlog" TODO.md
head -40 TODO.md
```

- [ ] **Step 3: Commit**

```bash
git add TODO.md
git commit -m "docs(todo): carve out tw-ecom skeleton backlog"
```

---

## Task 16: Final verification pass

**Files:** none modified. Read-only checks.

- [ ] **Step 1: Confirm all 29 new skill directories exist with required subdirs**

```bash
for d in \
  tw-ecom-shopline-integration tw-ecom-payment-newebpay tw-ecom-invoice-ezpay \
  tw-ecom-platform-selection tw-ecom-91app-integration tw-ecom-shopify-tw-integration tw-ecom-shopee-operations tw-ecom-momo-operations \
  tw-ecom-payment-tappay tw-ecom-payment-ecpay tw-ecom-payment-jkopay tw-ecom-payment-dispute \
  tw-ecom-logistics-cvs tw-ecom-logistics-home tw-ecom-logistics-cold-chain tw-ecom-logistics-cross-border \
  tw-ecom-invoice-universalec tw-ecom-invoice-carrier tw-ecom-invoice-void \
  tw-ecom-compliance-consumer tw-ecom-compliance-product tw-ecom-compliance-pdpa tw-ecom-compliance-cross-border \
  tw-ecom-operations-promotion tw-ecom-operations-pricing tw-ecom-operations-crm-line-oa tw-ecom-operations-customer-service \
  tw-ecom-analytics-ga4 tw-ecom-analytics-benchmarks; do
  [ -f "$d/SKILL.md" ] && [ -d "$d/references" ] && [ -d "$d/examples" ] || echo "MISSING: $d"
done
echo "--- done ---"
```

Expected: no `MISSING:` lines; final `--- done ---` marker.

- [ ] **Step 2: Frontmatter sanity check**

```bash
python3 - <<'PY'
import os, re, sys
errors = []
for d in sorted(os.listdir('.')):
    p = os.path.join(d, 'SKILL.md')
    if not d.startswith('tw-ecom-') or not os.path.isfile(p):
        continue
    with open(p) as f:
        src = f.read()
    if not src.startswith('---\n'):
        errors.append(f"{p}: missing frontmatter")
        continue
    end = src.find('\n---\n', 4)
    if end < 0:
        errors.append(f"{p}: unterminated frontmatter")
        continue
    fm = src[4:end]
    m = re.search(r'^name:\s*"([^"]+)"', fm, re.M)
    if not m:
        errors.append(f"{p}: missing or unquoted name")
    elif m.group(1) != d:
        errors.append(f"{p}: name mismatch ({m.group(1)} vs dir {d})")
    md = re.search(r'^description:\s*"([^"]+)"', fm, re.M)
    if md and len(md.group(1)) > 1024:
        errors.append(f"{p}: description > 1024 chars ({len(md.group(1))})")
    if re.search(r'claude|anthropic', d, re.I):
        errors.append(f"{p}: reserved word in name")
print(f"checked tw-ecom-* skills, {len(errors)} errors")
for e in errors: print("  " + e)
sys.exit(1 if errors else 0)
PY
```

Expected: `checked tw-ecom-* skills, 0 errors` and exit code 0.

- [ ] **Step 3: Line-count check on complete skills**

```bash
for d in tw-ecom-shopline-integration tw-ecom-payment-newebpay tw-ecom-invoice-ezpay; do
  lines=$(wc -l < $d/SKILL.md)
  echo "$d: $lines lines"
  [ "$lines" -le 500 ] || echo "  ⚠️ exceeds CLAUDE.md 500-line cap"
done
```

Expected: all 3 ≤ 500 lines.

- [ ] **Step 4: Check domain map references exist**

```bash
python3 - <<'PY'
import re, os
with open('docs/domains/tw-ecommerce.md') as f:
    src = f.read()
# find every reference like `tw-ecom-<slug>` or `tw-<existing>`
refs = set(re.findall(r'`(tw-[a-z0-9-]+|ecom-[a-z0-9-]+|data-[a-z0-9-]+|biz-[a-z0-9-]+|law-[a-z0-9-]+|cs-[a-z0-9-]+|pr-[a-z0-9-]+)`', src))
missing = [r for r in refs if not os.path.isdir(r)]
print(f"domain map references {len(refs)} skills, {len(missing)} missing")
for m in missing: print("  " + m)
PY
```

Expected: 0 missing.

- [ ] **Step 5: git log summary**

```bash
git log --oneline main..feat/tw-ecommerce-domain
```

Expected: the 2 pre-existing spec commits + 14 new commits from Tasks 2-15 (tasks 1 and 16 have no commit). Total ≈ 16 commits.

- [ ] **Step 6: No push — stop here**

Do NOT push or open a PR in this automation. The user will push manually after review.

---

## Self-Review Checklist (done by plan author, not executor)

Covered:
- [x] Design spec §2 goals 1-4: flat architecture, reuse existing, 3 reference skills, 29-skill footprint → Tasks 2-11 + 12
- [x] Design spec §3 flat naming → Tasks 2-11 all use `tw-ecom-<layer>-<topic>`
- [x] Design spec §4 overlap audit → no new skills duplicate `tw-payment-integration`, `tw-einvoice-guide`, or `ecom-*`; domain map cross-links them (Task 12)
- [x] Design spec §5 three reference skills with MCP-derived content → Tasks 1-4
- [x] Design spec §5.2 content-source discipline → Task 1 fetches MCP READMEs; each reference-skill task tells executor to cite-or-TODO
- [x] Design spec §6 skeleton list (26 skills, 7 layers) → Tasks 5-11
- [x] Design spec §7 Phase 0 infra: domain doc + CONTRIBUTING.md + README updates + TODO.md update → Tasks 12-15
- [x] Design spec §7 explicit "NOT" list (lint script, CODEOWNERS) → correctly absent
- [x] Design spec §8 quality bar (frontmatter parse, 500-line cap, description < 1024 chars, no claude/anthropic in names) → Task 16
- [x] Design spec §9 risk "skeleton skills trigger on vague queries" → every skeleton SKILL.md has `STATUS: SKELETON` banner + "prefer X" recommendation
- [x] Design spec §10 follow-up branches → Task 15 enumerates them in TODO.md

Placeholder scan:
- Every reference-skill task has outline + frontmatter YAML + expected line ranges — no "TBD" / "implement later".
- Every skeleton-creation step ships the full cat-heredoc content — executor doesn't need to author any content from scratch for skeletons.
- "TODO" markers inside heredocs are intentional — they are the placeholder text *inside* the skeleton SKILL.md, not placeholders in the plan itself.

Type consistency:
- Skill names used in `related_skills` cross-refs match the directory names defined in each task (spot-checked: `tw-ecom-shopline-integration`, `tw-ecom-invoice-ezpay`, `tw-ecom-payment-newebpay`, `tw-payment-integration`, `tw-einvoice-guide`, `ecom-rfm-analysis`, `ecom-promo-roi`, `ecom-inventory-health`).
- Frontmatter field names consistent (`domain`, `layer`, `related_mcps`, `related_skills`, `last_verified`, `status`, `tags`) — matches design spec §5.1.
- Branch / commit scope prefix `feat(tw-ecom)` used consistently across layer commits.
