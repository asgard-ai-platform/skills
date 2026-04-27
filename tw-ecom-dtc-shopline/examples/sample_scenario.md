# Sample Scenario: New Shopline Order → ERP Sync → ezPay e-Invoice → Reconciliation

End-to-end walkthrough of the most common multi-tool Shopline flow in Taiwan DTC. Shows which `mcp-shopline` tools to call, in what order, and where the Taiwan-specific handoffs happen.

**Assumption**: mcp-shopline, mcp-ezpay-einvoice, and an internal ERP are all reachable. Shopline webhooks are not yet supported by mcp-shopline (see `../SKILL.md` Gotchas), so this flow is polling-based.

---

## Scenario

A Taiwan DTC merchant runs one Shopline shop with two sales channels: online storefront and one POS retail store. Each paid order must:

1. Land in the merchant's internal ERP within 15 minutes
2. Trigger an ezPay e-invoice (`tw-ecom-invoice-ezpay`) with the correct carrier type (手機條碼 / 統編 / 捐贈碼)
3. Be reconciled daily against Shopline's authoritative state

---

## Tool Flow

### Step 0 — One-time setup: confirm token scope

```
get_token_info()
→ verify the token covers: orders (read), customers (read), order-extended (read)
```

If the returned scope is missing any of these, stop and request an updated token. Do not proceed with a read-only-partial token — you will get silent 403s downstream.

### Step 1 — Poll for new orders (every 5-15 minutes)

```
query_orders(
  start_date = {last_checkpoint - 48h},   # re-scan 48h to catch late status flips
  end_date   = {today},
  # DO NOT pass a single `status` filter — include both by default:
  # online `confirmed` + POS `completed`
)
```

Persist a high-water-mark checkpoint (max `updated_at` from the returned orders), but always re-scan the trailing 48 hours on the next poll — Shopline back-dates status changes and late POS uploads frequently.

### Step 2 — Fetch full detail per new / changed order

For each order ID returned in Step 1:

```
get_order_detail(order_id = ...)
get_order_transactions(order_id = ...)   # payment records, needed for reconciliation
```

Extract and persist:

- `order.id`, `order.order_number`, `order.total` (TWD float)
- `order.status` — keep the raw value; do NOT collapse `confirmed` and `completed`
- `order.created_from` — `"shop"` or `"pos"`
- `order.channel.created_by_channel_name` — **this is the physical store identity**, carry it forward to ERP; without it you cannot attribute POS sales to the right retail store
- `order.customer.*` — buyer identity (needed for invoice carrier lookup)
- `order.invoice.*` — if the merchant collected 統編 or 手機條碼 at checkout, it is on the order payload

> TODO: verify with mcp-shopline tool schema — exact field path for invoice carrier on the order object (`invoice.carrier_id` vs `invoice.carrier_code`).

### Step 3 — Hand off to internal ERP

Write the enriched order into the ERP with these mandatory fields:

- Shopline order ID (for later reconciliation)
- Channel name (from Step 2)
- Payment method (from `get_order_transactions`)
- Invoice handoff state: `pending_einvoice`

### Step 4 — Trigger ezPay e-invoice

Hand off to `mcp-ezpay-einvoice`:

```
issue_invoice(
  seller_id,
  buyer_id           = {統編 if B2B, else null},
  carrier_type       = {手機條碼 / 自然人憑證 / 會員載具 / 捐贈碼 / none},
  carrier_id         = {extracted from order.invoice.* in Step 2},
  items              = {mapped from order.line_items},
  amount, tax,
)
```

On success, update ERP: `invoice_state = issued`, store `invoice_number` + `random_code`. On failure, leave `invoice_state = pending_einvoice` and retry on the next poll — do not assume the write in ezPay is idempotent with your Shopline order ID; use the ezPay `query_invoice` tool to check before retrying.

### Step 5 — Write back to Shopline (optional)

If the merchant wants the Shopline order to reflect the invoice number, call an order-write tool (e.g., add a tag like `invoice:AB12345678` or a note). Requires order-write scope.

```
[WRITE] update_order_tags(order_id = ..., tags = [..., "invoice:AB12345678"])
```

**Gotcha reminder**: after this write, a following `get_order_detail` may still return the pre-write tag list. Do not gate downstream logic on that read; trust the write response instead. See IRON LAW discussion in the main skill for reconciliation pattern.

### Step 6 — Daily reconciliation

Once per day (run after the Shopline day-close cutoff — TODO: verify the merchant's day-close hour in Shopline admin):

```
get_sales_summary(
  start_date = {yesterday},
  end_date   = {yesterday},
  channel    = "all"
)
get_channel_comparison(
  start_date = {yesterday},
  end_date   = {yesterday}
)
```

Compare against the ERP:

- Total orders in ERP with channel = online → should equal Shopline `confirmed` count for the online channel
- Total orders in ERP with channel = {store name} → should equal Shopline `completed` count for that POS channel (from `get_channel_comparison` rows)
- Revenue totals should match within float rounding tolerance

Any mismatch is investigated by calling `query_orders` for the day and diffing IDs.

### Step 7 — Refund / return handling

Separately poll returns, because returns are not included in `query_orders`:

```
list_return_orders(start_date = ..., end_date = ...)
→ for each: get_return_order_detail(return_id = ...)
→ trigger ezPay allowance:  issue_allowance(original_invoice = ..., amount = ...)
```

> TODO: verify with mcp-shopline — whether return_order has a back-reference to the original order_id or whether it must be joined via customer + line-item match.

---

## Failure modes this flow handles

- **POS orders missing from ERP**: caused by filtering on `status=confirmed` only. Fixed by always including both statuses (Step 1).
- **Wrong store attributed to a POS sale**: caused by using `created_from` as store identity. Fixed by reading `order.channel.created_by_channel_name` (Step 2).
- **Duplicate e-invoices**: caused by retrying `issue_invoice` without checking. Fixed by `query_invoice` before retry (Step 4).
- **Silent 403 on channels**: no mitigation needed — this flow never calls `list_channels`; channel identity comes from the order payload.
- **Late-arriving POS uploads**: caused by narrow polling windows. Fixed by the 48-hour re-scan on every poll (Step 1).

---

## Failure modes this flow does NOT handle

- Full webhook-driven real-time sync (mcp-shopline has no webhook support as of 2026-04 — polling is the only option)
- Multi-merchant token rotation (each merchant needs its own `SHOPLINE_API_TOKEN`; this flow assumes a single merchant)
- Promotion / coupon lifecycle — see `list_promotions` + promotion writes in `../references/tool-catalog.md`
