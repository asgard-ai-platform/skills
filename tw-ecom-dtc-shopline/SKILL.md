---
name: "tw-ecom-dtc-shopline"
description: "Integrate and operate Shopline in Taiwan e-commerce context via mcp-shopline. Use when the user needs to sync orders, manage products, run promotions, or reconcile inventory on Shopline stores; when comparing Shopline vs 91APP/Shopify for Taiwan DTC; or when debugging async write propagation. Do NOT use for API schema lookup (go to mcp-shopline docs) or non-Taiwan Shopline deployments."
metadata:
  category: "WP-01 電商"
  domain: "ecommerce-tw"
  layer: "platform"
  related_mcps: ["mcp-shopline"]
  related_skills: ["tw-ecom-channel-strategy", "tw-ecom-invoice-ezpay", "tw-ecom-payment-newebpay", "ecom-rfm-analysis", "ecom-promo-roi", "ecom-inventory-health"]
  last_verified: "2026-04"
  tags: ["taiwan", "e-commerce", "shopline", "platform", "integration"]
---

# Shopline Integration Methodology

## When to use this skill

- Syncing orders, products, members, or inventory between Shopline and an internal ERP / data warehouse
- Building a multi-step automation across `mcp-shopline` tools (e.g., order → invoice → logistics)
- Reconciling Shopline state against an external system (accounting, WMS, 電子發票 平台)
- Designing a promotion / coupon / flash-sale workflow that spans read + write tools
- Debugging unexpected behavior: missing orders, stale reads after writes, 403 on channel lookups

## Do NOT use when

- You need the exact API schema for one endpoint — read the tool description or Shopline Open API docs directly
- The merchant is on Shopify, 91APP, Cyberbiz, or a non-Shopline platform — use `tw-ecom-channel-strategy` first
- The Shopline store is non-Taiwan (HK/SG/MY) — currency, invoice, and logistics assumptions in this skill are TWD + Taiwan-specific

## Core concepts

Shopline is a SaaS commerce platform popular with Taiwan DTC and omnichannel brands. A single **merchant** account can own multiple **shops** (storefronts); each shop can sell through multiple **channels** (online + POS retail stores). `mcp-shopline` wraps Shopline Open API v1 into 143 tools (75 read, 68 write), all scoped to one API token = one merchant context.

Two axes matter when picking a tool:

- **Read vs write.** Write tools are prefixed `[WRITE]` in their descriptions and require an API token scope that permits mutation. Read tools are safe; write tools modify production data.
- **Domain.** Orders, Products & Inventory, Analytics, Customers, Categories & Promotions, Order Extended (returns/delivery/conversations/reviews), Store Settings. Analytics tools are pre-aggregated — prefer them over hand-rolling aggregations on top of `query_orders`.

Money is always TWD float. Dates are `YYYY-MM-DD` strings. Online orders use status `confirmed`; POS orders use `completed` — mixing them up silently drops half the data.

## Decision tree

```
What is the user asking for?
│
├─ Aggregate metric (revenue, AOV, top products, trend)?
│    → Analytics / Orders summary tools
│      get_sales_summary · get_top_products · get_sales_trend
│      get_channel_comparison · get_rfm_analysis · get_promotion_roi
│
├─ Specific order / customer / product lookup?
│    → Read-detail tools
│      get_order_detail · get_customer_profile · get_product_variants
│
├─ Inventory question (stock, low-stock, warehouse)?
│    → Products & Inventory read tools
│      get_inventory_overview · get_low_stock_alerts ·
│      get_stock_by_warehouse · get_locked_inventory
│
├─ Promotion / coupon / flash sale?
│    ├─ Read  → list_promotions · get_promotion_detail ·
│    │          list_flash_price_campaigns · list_affiliate_campaigns
│    └─ Write → promotion write tools (12) — split into three sub-families:
│              flat promo · flash price · gift/add-on. See
│              references/tool-catalog.md for exact tool per family.
│
├─ Modify an order (status, tag, fulfill, cancel)?
│    → Order write tools (8) — require write scope
│
├─ Create/update customer, adjust store credits, group membership?
│    → Customer write tools (6)
│
└─ Configuration / debug (token scope, channels, payments, delivery)?
     → Store Settings read tools
       get_token_info (always start here when debugging permissions)
       list_channels · list_payments · list_delivery_options
```

## Implementation guidance

Common multi-tool flows. For each, use the tool names below; see `examples/sample_scenario.md` for an end-to-end walkthrough.

**Order sync (Shopline → internal ERP)**

- Poll with `query_orders` on a date window; include BOTH `confirmed` (online) and `completed` (POS) statuses
- For each order, call `get_order_detail` for line items and `get_order_transactions` for payment records
- If delivery matters, call `get_order_delivery` — note: delivery has its own ID, only available after shipment executes
- Persist the `order.channel.created_by_channel_name` value, not just `created_from`, or you lose the physical store identity
- Checkpoint the high-water-mark date to avoid re-fetching; re-scan the last 24-48h each run to catch late status changes

**Promotion setup and measurement**

- Pre-check: `list_promotions` + `search_promotions` to avoid duplicate campaign names
- Create via the promotion write tool appropriate to type (flat promotion vs flash price vs gift-with-purchase vs add-on)
- After go-live, measure with `get_promotion_analysis` (effectiveness) + `get_promotion_roi` (lift vs baseline)
- For affiliate campaigns, use `get_affiliate_campaign_usage` — requires at least one order that used the campaign

**Member / RFM sync**

- Full membership sync: `list_customers` (paginated) → for each, `get_customer_profile` on demand (not in bulk — expensive)
- Segmentation: call `get_rfm_analysis` instead of computing from raw orders — it's pre-aggregated and respects Shopline's definition of a member
- For tier / points state: `list_membership_tiers`, `list_member_point_rules`, `list_store_credits`
- `get_customer_lifecycle` compares two periods' RFM to surface upgrades and churn

**Inventory sync and replenishment**

- Snapshot: `get_inventory_overview` (totals) + `get_stock_by_warehouse` (per-warehouse matrix)
- Operational signals: `get_low_stock_alerts`, `get_locked_inventory` (reserved by pending orders), `get_slow_movers` (excess stock)
- Transfer planning: `get_stock_transfer_suggestions` — server-side heuristic; treat output as suggestions not commands
- Replenishment: `list_purchase_orders` → `get_purchase_order_detail`; create via purchase-order write tools

## Gotchas

- **Order status split by channel — `confirmed` vs `completed`.** Online orders use `confirmed`; POS uses `completed`. The tools include both by default, but if you pass a custom `status` filter and forget one, you silently lose half the data. Always verify with `get_channel_comparison` that online and POS counts look plausible.
- **Pagination caps.** `per_page` maxes at 50, and search returns are capped at 10,000 results total. For large windows, split the date range (Shopline Open API uses `fetch_all_pages_by_date_segments` internally, but your own multi-step flows need the same discipline). A 30-day top-seller query on a high-volume merchant will hit the cap.
- **Async write propagation — read-after-write can be stale.** After calling a `[WRITE]` tool (e.g., `update_order_status`, `adjust_store_credit`), an immediate read may still return the pre-write state. Do not gate downstream logic on a read-after-write within the same sync step. Build a reconciliation loop, or pass the write response's own `updated_at` forward. (TODO: verify exact propagation window with Shopline Open API support or mcp-shopline maintainers.)
- **No webhook support yet (as of 2026-04).** `mcp-shopline` roadmap lists webhooks as pending. Until then, all event detection is polling. Budget API calls accordingly and pick a poll cadence (5-15 min for orders, hourly for inventory) that respects the 0.2s inter-page delay the tools enforce.
- **Channels endpoint often 403/422; fall back to order payload.** `list_channels` / `get_channel_detail` require a separate permission that most tokens don't carry. The same information (store name, channel type) is available via `order.channel.created_by_channel_name` on any order detail — use that as the authoritative source when channel tools fail.
- **Write tools need explicit scope AND `SHOPLINE_TEST_WRITES=1` in tests.** Tokens default to read-only scope; production write failures usually mean the scope wasn't granted, not that the tool is broken. Start debugging with `get_token_info` to confirm scope before assuming a bug. In test harnesses, writes are gated behind the env var — unset it in CI unless you have a dedicated test store.

## IRON LAW

**Never filter orders on `status` or `created_from` alone.** Online orders use `confirmed`, POS uses `completed`, and the store identity lives on `order.channel.created_by_channel_name` — not on `created_from` (`"shop"` / `"pos"`). Any order query that hard-codes one status or keys off `created_from` will silently drop POS revenue, misattribute store sales, or both. Always pass both statuses (or omit the filter) and always carry the channel name forward in downstream records.

### Rationalization Table

| "但是…" | 為什麼錯 |
|---|---|
| 我只需要線上訂單，`status=confirmed` 就夠了 | POS 訂單用 `completed`，hard-code `confirmed` 會靜默丟失所有實體門市營收 |
| `created_from` 欄位明確標示 `"shop"` vs `"pos"`，用它來分類就好 | `created_from` 不是通路身份的權威來源；門市名稱只在 `order.channel.created_by_channel_name` 中，跨店分析時用 `created_from` 會錯誤合併所有實體店 |
| 只拿 `confirmed` 是效能最佳化，不是資料遺失 | 範圍縮小不等於最佳化；用日期區間分頁才是正確的效能手段，不是靠省略 POS 訂單 |
| 這個報表只給線上部門，POS 不在範圍內 | 商業邏輯範圍不等於查詢範圍；即使報表只看線上，下游 ERP 或發票系統仍可能吃到這份 query 結果 |

## Output Format

When completing a Shopline task, produce this structure:

```markdown
# Shopline Task: {one-line summary}

## Context
- Merchant / shop: {name} (single-merchant token assumed)
- Scope of work: {read-only analysis | sync | write mutation | full integration}
- Date window / entity scope: {…}

## Tool Plan
| Step | Tool | Read/Write | Purpose |
|------|------|-----------|---------|
| 1 | get_token_info | R | Confirm scope covers the tools below |
| 2 | {tool} | R/W | {…} |
| … | … | … | … |

## Assumptions & Open Questions
- {assumption grounded in a Shopline constraint}
- TODO: {anything that needs verification against mcp-shopline or Open API docs}

## Execution Notes
- Both `confirmed` and `completed` statuses included: Y/N
- Channel name carried forward from `order.channel.created_by_channel_name`: Y/N
- Pagination strategy (date segmentation if >10k results): {…}
- Read-after-write handling (reconciliation loop, not immediate re-read): {…}

## Deliverable
{the actual answer, dataset, or change summary}
```

## Related

- **MCPs**: `mcp-shopline`
- **Skills**: `tw-ecom-channel-strategy` (Shopline vs 91APP/Shopify decision), `tw-ecom-invoice-ezpay` (e-invoice handoff), `tw-ecom-payment-newebpay` (payment reconciliation), `ecom-rfm-analysis` (segmentation methodology), `ecom-promo-roi` (lift measurement), `ecom-inventory-health` (stock KPIs)
- **References**: `references/tool-catalog.md` (one-line per tool, grouped by domain), `examples/sample_scenario.md` (end-to-end order → invoice flow)

_Last verified: 2026-04_
