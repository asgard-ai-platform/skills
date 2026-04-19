# Sample Scenario: Subscription Content Site — NewebPay 定期定額 + ezPay Invoice + Card Expiry + Dispute

End-to-end walkthrough of the most common `mcp-newebpay` flow for a Taiwan SaaS / content / membership product. Shows the three failure modes that separate a toy integration from a production one: card expiry, invoice on recurring success, and a disputed charge.

**Assumption**: `mcp-newebpay` (NDNP configured), `mcp-ezpay-einvoice`, and an internal billing DB are all reachable. NewebPay merchant portal has NotifyURL / ReturnURL registered for both test and production.

---

## Scenario

A Taiwan content site sells a 12-month membership at NT$149/month via 定期定額. Each successful monthly charge must:

1. Extend the member's access by one month
2. Trigger an ezPay e-invoice (`tw-ecom-invoice-ezpay`) with the carrier the member chose at signup (手機條碼 / 會員載具 / 捐贈碼)
3. Survive card expiry at month 9 (common: 2-year card issued at signup no longer valid)
4. Handle a single-cycle dispute (爭議款) at month 11 without terminating the whole mandate

---

## Tool Flow

### Step 0 — Pre-flight checks

Before any customer sees the checkout button:

- Confirm NDNP env configured: `NEWEBPAY_NDNP_MERCHANT_ID` / `HASH_KEY` / `HASH_IV` all set. Without these, `create_period_payment` will return a clear "not configured" error.
- Confirm `NotifyURL` and `ReturnURL` are registered for NDNP (separate from NDNF URLs) in the NewebPay merchant portal.
- Confirm ezPay merchant account exists (`mcp-ezpay-einvoice` configured).

### Step 1 — Mandate creation (member signs up, month 0)

```
create_period_payment(
  MerOrderNo      = "sub-{member_id}-{timestamp}",
  ProdDesc        = "Content Site Annual Membership",
  PeriodAmt       = 149,
  PeriodType      = "M",
  PeriodPoint     = "05",                     # charge on 5th of each month
  PeriodStartType = 1,                        # 10 TWD verification charge (refunded)
  PeriodTimes     = 12,
  NotifyURL       = "https://site.example.tw/newebpay/period_notify",
  ReturnURL       = "https://site.example.tw/membership/welcome",
  Email           = member.email,
)
```

Returns `{url, form_data}`. Merchant renders auto-submit form; member completes 3DS 2.0 verification on NewebPay's hosted page.

At signup, the UI also collects the invoice carrier preference and stores it in the member DB (NOT in NewebPay — invoice carrier is ezPay's concern, not NewebPay's).

### Step 2 — First-cycle NotifyURL (month 0 activation + month 1 first charge)

NewebPay POSTs to `NotifyURL`. Merchant handler:

1. Verify `TradeSha` using the exact `HashKey={...}&{TradeInfo}&HashIV={...}` format — **not** a generic alphabetical-sort HMAC (see main SKILL.md Gotchas).
2. AES-256-CBC decrypt `TradeInfo` using NDNP `HashKey` / `HashIV` (not NDNF's — separate merchant).
3. Persist the `PeriodNo` (e.g., `P260403144725zl3MVV`) — this is the canonical mandate handle for all future operations.
4. Grant the member 1 month of access.
5. Respond `1|OK` to NewebPay.

> Note: Do not rely on `ReturnURL` to activate membership. The browser might not reach it (network drop, closed tab) but NotifyURL is still authoritative. See IRON LAW in main SKILL.md.

### Step 3 — Issue ezPay e-invoice on successful charge

After NotifyURL success, look up the member's stored carrier preference and hand off to `mcp-ezpay-einvoice`:

```
issue_invoice(
  seller_id,
  buyer_id      = {統編 if B2B, else null},
  carrier_type  = member.carrier_type,       # 手機條碼 / 會員載具 / 捐贈碼 / null
  carrier_id    = member.carrier_id,
  items         = [{name: "Content Site Annual Membership (month N)", qty: 1, unit_price: 149}],
  amount        = 149,                        # assumed tax-inclusive (5%); confirm amount/tax semantics with tw-ecom-invoice-ezpay
  tax           = 7,                           # 149 − (149 / 1.05) ≈ 7.10, rounded per ezPay convention
)
```

On success, record the invoice number against the cycle's `OrderNo` (per-cycle) and `MerOrderNo` (mandate-wide). On ezPay failure, leave the invoice in `pending` and retry on the reconciliation cron — use `query_invoice` to avoid double-issuing.

### Step 4 — Months 2-8, normal billing

Each month, NewebPay auto-charges the stored card on the 5th, fires NotifyURL on success, merchant extends membership + issues invoice. No merchant-initiated action required.

### Step 5 — Card expiry (month 9) — realistic failure

At month 9, the customer's card expires. NewebPay's acquirer declines the authorization. NewebPay fires NotifyURL with `Status` indicating failure and a `RespondCode` like `G12` / `54` (expired card).

**Critical**: the mandate is **not** auto-suspended. The next cycle will attempt another charge and fail the same way.

Merchant handler must:

1. Record the failure against `PeriodNo`.
2. Send the member a dunning email / SMS with a "update card" link.
3. Decide policy:
   - **Soft dunning**: leave mandate active, let NewebPay retry next cycle (some cards re-activate after issuer update). Risk: repeated failed charges look bad in reporting.
   - **Hard pause**: `alter_period_status(PeriodNo, AlterType="suspend")`. Then when the member updates their card, create a *new* mandate via `create_period_payment` (old `PeriodNo` cannot have its card changed — NewebPay does not expose card-update on an existing mandate).

   > TODO: verify from NewebPay merchant portal — whether NDNP v1.0.7+ exposes any card-update-on-existing-mandate endpoint. As of the PDF cited in the mcp-newebpay README, the documented path is mandate replacement, not card replacement.

4. Do NOT issue an ezPay invoice for this cycle — no payment happened.

Membership access for month 9 is paused in the site DB until a new mandate is established. When the new mandate's first NotifyURL arrives (Step 2 pattern repeated), activate month 9-12 under the new `PeriodNo`.

### Step 6 — Dispute at month 11 (爭議款 / chargeback)

Member's card issuer raises a dispute on the month-11 charge (perhaps member forgot they subscribed). NewebPay notifies merchant via the merchant portal (not via NotifyURL — disputes are a separate channel).

Merchant options:

- **Accept the dispute**: issue a refund via `close_refund(MerOrderNo={cycle_11_order}, Amt=149, CloseType="refund")`. Then `issue_allowance` in ezPay to offset the invoice. The mandate itself stays active for month 12 unless you also `alter_period_status(PeriodNo, AlterType="terminate")`.
- **Contest the dispute**: submit evidence through the NewebPay merchant portal (login, transaction history showing prior 10 successful charges, membership activity logs proving service was delivered). `mcp-newebpay` does not expose dispute-evidence submission — it is a portal-only workflow.

See `tw-ecom-payment-dispute` skill for the evidence-package playbook. The decision (accept vs contest) is a cost/benefit judgment — not a NewebPay API question.

### Step 7 — Month 12 final cycle + mandate completion

At month 12, NewebPay charges and fires the final NotifyURL. Because `PeriodTimes=12` was set at creation, the mandate auto-terminates after the 12th successful charge. `query_trade` on the mandate (via the portal or NDNP query endpoint) will show the completed state.

> TODO: verify whether `query_trade` accepts NDNP per-cycle `OrderNo` or if NDNP reconciliation requires merchant portal export.

If the member wants renewal, repeat Step 1 with a fresh `MerOrderNo`.

---

## Failure modes this flow handles

- **Card expires mid-mandate**: detected on NotifyURL failure code, dunning + mandate replacement (Step 5). Naive implementations that only listen to success callbacks silently lose months 9-12 of revenue.
- **Double-fulfillment from browser refresh**: prevented by `MerOrderNo`-keyed idempotency in the NotifyURL handler (Step 2). Never mutate state on ReturnURL.
- **Invoice double-issued on NotifyURL retry**: prevented by ezPay `query_invoice` before `issue_invoice` (Step 3).
- **Chargeback**: handled via portal evidence + `close_refund` + `issue_allowance` (Step 6), without terminating remaining cycles.

## Failure modes this flow does NOT handle

- **Cross-border card BIN decline** (non-TW card): NewebPay will reject at mandate creation. Pre-screen in UI or surface the error cleanly.
- **NDNF one-off payments**: this scenario is subscription-only (NDNP). For one-off checkout, use the NDNF flow in `../references/integration-flow.md` Phase 2.
- **Multi-gateway fallback**: if the merchant also has ECPay / TapPay for redundancy, routing logic is outside this skill — see `tw-payment-integration`.
