# Sample Scenario: Shopline Order + 手機條碼 → ezPay Invoice → Cross-Period Return → 折讓

End-to-end walkthrough of the most common `mcp-ezpay-einvoice` flow for a Taiwan DTC merchant. Shows the three ezPay-specific traps that separate a toy integration from a production one: carrier validation before the API call, same-period void vs cross-period allowance, and daily MOF reconciliation.

**Assumption**: `mcp-shopline`, `mcp-newebpay`, and `mcp-ezpay-einvoice` are all configured. ezPay production credentials (`EZPAY_IS_PRODUCTION=true`) and a current 字軌 range (`TE00000000-...`) are active.

---

## Scenario

A Taiwan skincare brand on Shopline sells a NT$1,050 set (NT$1,000 + 5% tax). Consumer chooses 手機條碼 at checkout and pays via NewebPay credit card on **March 28**. Order ships the next day. On **May 2** (next bimonthly period), the customer returns one item worth NT$420 (NT$400 + NT$20 tax). Because the return crosses the bimonthly boundary, the correction must be an allowance (折讓), not a void.

---

## Tool Flow

### Step 0 — Checkout-time carrier capture

On the Shopline checkout page, the customer selects "存手機條碼" and enters `/ABC1234`. The frontend validates with a regex `^\/[A-Z0-9]{7}$` **before** submitting. If invalid, the customer sees "手機條碼格式錯誤" without ever calling the backend — an invalid carrier sent to ezPay creates no invoice and no recovery path exists for that `merchant_order_no`.

The order persists `carrier_type="0"` and `carrier_num="/ABC1234"` against the Shopline order ID. Do NOT try to store this on NewebPay — the payment gateway has no carrier concept.

### Step 1 — Payment success (March 28, NewebPay NotifyURL)

NewebPay fires `NotifyURL` after 3DS 2.0 succeeds. The merchant's handler (see `tw-ecom-payment-newebpay` IRON LAW):

1. Verify `TradeSha` and decrypt `TradeInfo`
2. Confirm `Status == "SUCCESS"` and `Amt == 1050`
3. Transition the Shopline order to `confirmed` (online status)
4. Enqueue an invoice-issuance job — do NOT issue inline; if ezPay is slow, it must not delay the NotifyURL response

Why enqueue: a synchronous `issue_invoice` inside the NotifyURL handler risks NewebPay retrying the webhook (non-`1|OK` response on timeout), which could double-process the order.

### Step 2 — Issue the invoice (March 28, async worker)

```
issue_invoice(
  merchant_order_no = "SL-2026-0328-0471",       # Shopline order ID, your idempotency key
  buyer_name        = "顧客",
  category          = "B2C",
  carrier_type      = "0",
  carrier_num       = "/ABC1234",
  tax_type          = "1",
  tax_rate          = 5,
  amt               = 1000,
  tax_amt           = 50,
  total_amt         = 1050,
  item_name         = "精華液|化妝水|面膜",
  item_count        = "1|1|1",
  item_unit         = "瓶|瓶|盒",
  item_price        = "600|300|150",
  item_amt          = "600|300|150",
  print_flag        = "N",
  status            = "1",
)
```

Returns `SUCCESS` with `InvoiceNumber="TE12345678"`, `InvoiceTransNo`, and `RandomNumber="9393"`. Persist all three against the Shopline order.

**Pipe-alignment audit**: before closing the job, call `query_invoice(search_type="1", merchant_order_no="SL-2026-0328-0471", total_amt=1050)` and confirm every item row matches. A silent pipe misalignment would show up as 精華液 priced at 300 or similar — ezPay does not validate, only stores.

### Step 3 — Daily reconciliation (March 29, 02:00 TW)

Nightly job picks up the invoice from the issued-in-last-48h set:

1. `query_invoice` returns `Status=1` (issued) + MOF upload status — confirms ezPay state
2. Cross-check against MOF platform export: invoice `TE12345678` appears with amount NT$1,050 and carrier `/ABC1234`
3. Three-way match (DB = ezPay = MOF) passes → move to `reconciled` state

If MOF had been missing the invoice, the job would leave it in `ezpay_confirmed_mof_pending` and retry the next night. If still missing after 72h, escalate via the ezPay merchant portal support channel (not via `issue_invoice` retry — that would produce a duplicate if the original actually uploaded late).

### Step 4 — Return request (May 2, customer returns 化妝水)

Customer contacts customer service on May 2 requesting a return of the NT$300 化妝水 line item. The refund amount including tax is NT$315 (NT$300 + NT$15 tax).

**First instinct check: can we void the invoice?** No — invoice was issued March 28, void window closed roughly May 14 for Mar-Apr invoices... but more importantly, voiding would reverse the entire NT$1,050 invoice, not the NT$315 line. Even within the void window, void is wrong here — this is a partial refund, not a wrong-issuance.

Per the decision tree in SKILL.md:
- Partial refund → 折讓
- Regardless of same-period or cross-period, partial = allowance

Also: the customer return is processed on May 2, which falls in the May-Jun bimonthly period. The original March invoice is in the Mar-Apr period. Cross-period reinforces the allowance decision.

### Step 5 — Issue the allowance (May 2)

```
issue_allowance(
  invoice_no        = "TE12345678",
  merchant_order_no = "SL-2026-0328-0471",
  item_name         = "化妝水",
  item_count        = "1",
  item_unit         = "瓶",
  item_price        = "300",
  item_amt          = "300",
  item_tax_amt      = "15",
  total_amt         = 315,
  status            = "1",
)
```

Returns `SUCCESS` with an `AllowanceNo`. The allowance is now in pending state — NOT yet filed with MOF.

### Step 6 — Confirm the allowance (May 2)

```
trigger_allowance(
  allowance_no    = "<AllowanceNo from Step 5>",
  allowance_status = "C",                       # C=confirm, D=cancel
)
```

Confirmed allowances are queued for MOF upload. Only after this call is the allowance real for tax purposes.

If the customer changes their mind and cancels the return request before Step 6 runs (e.g., CS workflow takes 24h), call `trigger_allowance(..., allowance_status="D")` instead — the allowance is cancelled with no MOF impact.

### Step 7 — Refund the payment (May 2, parallel to Step 6)

Trigger the NewebPay refund:

```
close_refund(
  MerchantOrderNo = "SL-2026-0328-0471",
  Amt             = 315,
  CloseType       = "refund",
)
```

See `tw-ecom-payment-newebpay` for the full close-vs-cancel decision tree. The refund and the allowance are independent MOF and payment-gateway records — if one succeeds and the other fails, reconciliation surfaces the discrepancy.

### Step 8 — Reconciliation after allowance (May 3, 02:00 TW)

Nightly job now also checks the allowance:

1. `query_invoice(search_type="0", invoice_number="TE12345678", total_amt=1050)` → ezPay state shows the original invoice with an attached allowance of NT$315; net remaining = NT$735
2. MOF platform confirms the allowance uploaded under the May-Jun period (allowance period ≠ original invoice period — this is expected)
3. Payment gateway shows the NT$315 refund settled
4. Internal DB order state transitions to `partially_refunded`

Three-way match passes → reconciled.

---

## Failure modes this flow handles

- **Invalid 手機條碼 at checkout**: prevented by regex validation in the frontend before any backend call (Step 0). ezPay errors on invalid carriers cannot be recovered — the invoice is never created.
- **Pipe-misalignment in items**: caught by the post-issuance `query_invoice` audit (Step 2). Without this audit, misalignments sit in MOF silently until a customer disputes a line item.
- **Cross-period return**: correctly routed to allowance (Step 5) instead of a futile void attempt that would return `INV20002`.
- **Allowance staged but not yet confirmed**: customer-cancelled returns use `trigger_allowance("D")` before MOF sees them, keeping books clean.
- **ezPay upload lag to MOF**: detected by the daily three-way reconciliation (Steps 3, 8). Trusting only ezPay's `SUCCESS` would hide upload failures.

## Failure modes this flow does NOT handle

- **字軌 exhaustion**: if the current range runs out between Steps 1 and 2, `issue_invoice` fails and the order is stuck in `paid_no_invoice` state. Prevention is monitoring (see `references/issuance-flow.md` Phase 5), not recovery.
- **Full-order refund**: the allowance model shown here is for partial refunds. For a full refund that crosses the bimonthly boundary, issue an allowance for the full amount. Inside the same bimonthly, prefer void for simpler tax records.
- **B2B buyer with 統編**: scenario assumed B2C. For B2B, add `category="B2B"` and `buyer_ubn=...` at Step 2; allowance amounts still work the same way.
- **Multi-invoice order**: if the NT$1,050 had been split into two invoices (e.g., pre-order + backorder), each invoice has its own allowance. A combined allowance across invoices is not supported by ezPay — `ALW10001` fires.
