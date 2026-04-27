# mcp-shopline Tool Catalog

One-line summary per tool, grouped by domain. Sourced from `mcp-shopline` README (2026-04 snapshot, 143 tools = 75 read + 68 write).

For each tool: `R` = read (safe), `W` = write (mutates, requires scope + `[WRITE]` prefix). Write-tool counts here are from the README's domain summary table; individual write tool names are not fully enumerated in the README and should be read off the live tool registry.

---

## Orders — 12 R + 8 W

Read:

- `query_orders` — R — list orders by date, status, channel, store
- `get_sales_summary` — R — revenue, AOV, item price, payment + delivery breakdown
- `get_top_products` — R — product ranking by quantity or revenue
- `get_sales_trend` — R — daily / weekly / monthly sales trend series
- `get_channel_comparison` — R — per-store / per-channel performance
- `get_order_detail` — R — full order with line items
- `get_refund_summary` — R — return-order count and refund amount totals
- `get_archived_orders` — R — archived / closed orders
- `get_order_labels` — R — labels attached to orders
- `get_order_tags` — R — tags attached to orders
- `get_order_action_logs` — R — audit trail for a specific order
- `get_order_transactions` — R — payment transaction records for an order

Write (8 total, names not individually listed in README): update status, add notes, assign labels / tags, cancel, fulfill. Require order-write scope.

---

## Products & Inventory — 9 R + 15 W

Read:

- `get_product_list` — R — product search by keyword / brand
- `get_product_variants` — R — SKU variants (size × color matrix)
- `get_inventory_overview` — R — total inventory summary by brand
- `get_low_stock_alerts` — R — SKUs at or below a threshold
- `get_warehouses` — R — warehouses and store locations
- `get_stock_by_warehouse` — R — per-warehouse stock matrix
- `get_locked_inventory` — R — stock reserved by pending orders
- `list_purchase_orders` — R — replenishment PO list
- `get_purchase_order_detail` — R — single PO detail

Write (15 total): create / update / delete products, manage variants, update stock.

Purchase orders have their own write pair (2 tools): create PO, receive PO.

---

## Analytics — 11 R

All read-only; pre-aggregated (prefer these over rolling your own from `query_orders`).

- `get_rfm_analysis` — R — customer RFM segmentation
- `get_repurchase_analysis` — R — repurchase rate + cycle
- `get_customer_geo_analysis` — R — customer geography distribution
- `get_inventory_turnover` — R — stock turnover rate and days-on-hand
- `get_category_sales` — R — sales by product category
- `get_promotion_analysis` — R — promotion campaign effectiveness
- `get_refund_by_store` — R — return breakdown per store / channel
- `get_stock_transfer_suggestions` — R — auto-suggested inter-warehouse transfers
- `get_promotion_roi` — R — promotion-vs-baseline lift and ROI
- `get_customer_lifecycle` — R — RFM segment migration across two periods
- `get_slow_movers` — R — high-stock / low-sales clearance candidates

---

## Customers — 9 R + 6 W

Read:

- `list_customers` — R — search and list profiles
- `get_customer_profile` — R — full profile for one customer
- `list_customer_groups` — R — segmentation group definitions
- `get_customer_group_members` — R — members in a group (requires at least one group configured)
- `list_store_credits` — R — store-credit balances and history
- `list_membership_tiers` — R — tier definitions
- `get_customer_tier_history` — R — tier upgrade / downgrade history for a customer
- `list_member_point_rules` — R — point earn + redeem rules
- `list_custom_fields` — R — custom field definitions on customer profiles

Write (6 total): create / update customer, adjust store credits, update group membership.

---

## Categories & Promotions — 14 R + 12 W + 3 W (categories) + 7 W (gifts/addons)

Read — Categories:

- `get_category_tree` — R — full hierarchy
- `get_category_detail` — R — one category

Read — Promotions:

- `list_promotions` — R — all promotion campaigns
- `get_promotion_detail` — R — one promotion
- `search_promotions` — R — search by keyword / status

Read — Flash Sale:

- `list_flash_price_campaigns` — R
- `get_flash_price_campaign_detail` — R — requires an active flash campaign to exist

Read — Affiliate:

- `list_affiliate_campaigns` — R
- `get_affiliate_campaign_detail` — R
- `get_affiliate_campaign_usage` — R — requires the campaign to have been used on ≥1 order

Read — Gifts / Add-ons / Subscriptions:

- `list_gifts` — R — gift-with-purchase promotions
- `list_addon_products` — R — add-on product promotions
- `list_product_subscriptions` — R — subscription plans
- `get_product_subscription_detail` — R — requires a subscription-enabled product

Write:

- Promotion / coupon / campaign writes — 12 tools — create / update / delete promotions, coupons, flash sales, affiliate campaigns
- Category writes — 3 tools — create, update, delete categories
- Gift / addon writes — 7 tools — create / update / delete gift and add-on promotions

---

## Order Extended — 8 R + 2 W (returns) + 2 W (conversations) + 6 W (reviews)

Read:

- `list_return_orders` — R — return / refund orders
- `get_return_order_detail` — R — one return (requires a completed return to exist)
- `get_order_delivery` — R — logistics tracking (delivery has its own ID, populated only after shipment)
- `list_conversations` — R — customer-service threads (requires conversations scope)
- `get_conversation_messages` — R — messages inside a thread
- `list_product_reviews` — R — product reviews
- `get_product_review_detail` — R — one review

Write:

- Return-order writes — 2 tools — approve / reject returns
- Conversation writes — 2 tools — reply, update status
- Review writes — 6 tools — reply, approve / reject / hide

---

## Store Settings — 13 R + 3 W (delivery/merchant) + 2 W (media/metafield)

Read:

- `list_merchants` — R — merchant accounts
- `get_merchant_detail` — R — one merchant
- `list_payments` — R — configured payment methods
- `list_delivery_options` — R — configured delivery options
- `get_delivery_option_detail` — R — one delivery option
- `get_delivery_time_slots` — R — available time slots (requires time-slot config)
- `list_channels` — R — sales channels (commonly 403/422; use `order.channel.created_by_channel_name` as fallback)
- `get_channel_detail` — R — one channel (same caveat)
- `get_app_settings` — R — app-level configuration
- `list_taxes` — R — tax configurations
- `get_staff_permissions` — R — staff permission settings
- `get_token_info` — R — current token's scope and metadata (start here when debugging permissions)
- `list_agents` — R — CS agent accounts

Write:

- Delivery / merchant writes — 3 tools — update delivery info, merchant settings
- Media / metafield writes — 2 tools — upload media, set metafields

---

## Quick reference — tool selection heuristics

- **Aggregate question?** Use an Analytics tool. Don't rebuild it from `query_orders`.
- **Single-record lookup?** Use the `get_*_detail` variant, not a list + filter.
- **Unsure if the token can do X?** Call `get_token_info` first.
- **Channel / store attribution?** Read `order.channel.created_by_channel_name`, don't rely on `list_channels`.
- **Big date window?** Segment by date to stay under the 10,000-result search cap.
