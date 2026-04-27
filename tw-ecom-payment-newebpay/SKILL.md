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

# NewebPay Integration Methodology

## When to use this skill

- Accepting payment on a Taiwan storefront through NewebPay (藍新金流): credit card, ATM (虛擬帳號), CVS barcode (超商條碼), LINE Pay, Apple Pay, Taiwan Pay, Samsung Pay
- Setting up 定期定額 (credit card recurring billing) — subscription boxes, SaaS, content sites, donation platforms
- Reconciling NewebPay callback webhooks against internal order state, or debugging why an order is "paid on NewebPay" but "open in our DB"
- Issuing refunds, cancelling authorizations, or closing (請款) credit card transactions through `mcp-newebpay`
- Debugging AES-256-CBC / TradeSha signature mismatches, 3DS 2.0 liability shift behavior, or `MPGGateway` form submission failures

## Do NOT use when

- The question is "which gateway should we pick?" — use `tw-payment-integration` (comparison of NewebPay / ECPay / TapPay / LINE Pay Direct)
- The merchant is on ECPay (綠界) or TapPay — those providers have their own skills and different API / signature schemes
- You only need the exact API schema for one NDNF/NDNP endpoint — read `mcp-newebpay` tool descriptions or the NewebPay official PDF (`線上交易─幕前支付技術串接手冊_NDNF` / `信用卡定期定額串接技術手冊_NDNP`)
- The dispute is about chargeback / 爭議款 handling — see `tw-ecom-payment-dispute`

## Core concepts

NewebPay (藍新金流) is one of the three dominant TW payment gateways (with ECPay and TapPay). It is an **aggregator** — one merchant contract covers credit card, ATM, CVS, and wallet rails, each with its own settlement cycle. `mcp-newebpay` wraps 8 official tools covering two API families:

- **NDNF (線上交易)** — one-off transactions. Tools: `create_mpg_payment`, `query_trade`, `cancel_authorization`, `close_refund`, `ewallet_refund`.
- **NDNP (定期定額)** — credit-card recurring mandates. Tools: `create_period_payment`, `alter_period_status`, `alter_period_content`.

NDNF and NDNP are **separate merchant accounts** with separate `MerchantID` + `HashKey` + `HashIV` triples. Configuring one does not enable the other.

**Signature model.** Every request body is AES-256-CBC-encrypted with the merchant's `HashKey` (32 chars) and `HashIV` (16 chars) into a `TradeInfo` blob, and a SHA-256 `TradeSha` is computed over `HashKey=…&{TradeInfo}&HashIV=…` and the result uppercased (the literal format, not a generic param sort — see Gotchas). Version is `2.0`. 3DS 2.0 liability shift is handled by NewebPay's hosted MPG page; merchants never see card PAN.

**Trust boundary.** `create_mpg_payment` / `create_period_payment` return encrypted form data for a **browser-side POST** to `https://ccore.newebpay.com/MPG/mpg_gateway` (or `core.newebpay.com` in prod). The merchant backend never sees card PAN. Payment result is delivered via two channels: **NotifyURL** (server-to-server webhook) and **ReturnURL** (browser redirect). These can arrive out of order.

## Decision tree

```
What is the user asking for?
│
├─ New one-time payment (credit card / ATM / CVS / wallet)?
│    → NDNF: create_mpg_payment
│      Returns {url, form_data} → merchant must render an auto-submit form
│      Result arrives via NotifyURL (trust) + ReturnURL (display only)
│
├─ Subscription / 定期定額 / recurring membership?
│    → NDNP: create_period_payment
│      Separate MerchantID from NDNF — verify both credential sets exist
│      Changes after go-live: alter_period_status (pause/resume/terminate),
│                              alter_period_content (amount/cycle/expiry)
│
├─ "Did this order get paid?" / reconciliation?
│    → NDNF: query_trade  (canonical source of truth for a single MerchantOrderNo)
│      Use this whenever NotifyURL was missed, duplicated, or suspect
│
├─ Refund / cancellation?
│    ├─ Credit card, before close (請款)? → cancel_authorization (NPA-B01)
│    ├─ Credit card, after close?         → close_refund (NPA-B03x)
│    └─ LINE Pay / Taiwan Pay / e-wallet? → ewallet_refund (NPA-B06)
│
└─ Recurring mandate state change?
     ├─ Pause / resume / terminate      → alter_period_status
     └─ Change amount / cycle / expiry  → alter_period_content
```

When `mcp-newebpay` reports a "tool not configured" error, the corresponding NDNF or NDNP env group was not set — see README `Environment variables` table.

## Implementation guidance

Three flows. For each, the exact `mcp-newebpay` tool is named. See `references/integration-flow.md` for full wiring and `examples/sample_scenario.md` for an end-to-end subscription walkthrough.

**One-time payment (NDNF)**

1. Merchant backend calls `create_mpg_payment` with `MerchantOrderNo` (your idempotency key), `Amt` (integer TWD), `ItemDesc`, `Email`, `NotifyURL`, `ReturnURL`, and which payment methods to enable (`CREDIT`, `VACC` for ATM, `CVS`, `BARCODE`, `LINEPAY`, `APPLEPAY`, ...)
2. Return value is `{url, form_data}`. The merchant **must render an auto-submit HTML form** that POSTs `form_data` to `url`. Do not attempt to follow the redirect server-side — the customer must hit NewebPay's hosted page in their own browser for 3DS 2.0 to work.
3. After the customer pays, NewebPay fires **NotifyURL** (server-to-server POST, decrypt `TradeInfo`, check `Status == "SUCCESS"`). This is the authoritative event. The customer's browser is also redirected to **ReturnURL** — treat this as a UI hint only, never as the completion signal.
4. On reconciliation doubt, call `query_trade(MerchantOrderNo, Amt)` to re-confirm server-side.

**Recurring / 定期定額 (NDNP)**

1. `create_period_payment` — establishes the mandate. Requires NDNP credentials. Returns the same `{url, form_data}` shape; the customer goes through one interactive auth on NewebPay's hosted page to authorize the mandate. After that, NewebPay charges on the cycle automatically and fires NotifyURL on each cycle.
2. Each billing cycle: NewebPay charges the stored card and posts to NotifyURL. Merchant must handle `Status == "SUCCESS"` (grant service period) and failure (card expired, insufficient funds, acquirer decline) separately — failures do not auto-retry.
3. Mandate lifecycle: pause/resume/terminate via `alter_period_status`; amount/cycle/expiry via `alter_period_content`. Treat `PeriodNo` (e.g., `P260403144725zl3MVV`) as the canonical handle — not the merchant order number.

**Refund**

- Credit card path depends on close (請款) state. Before close: `cancel_authorization` releases the hold. After close: `close_refund` with operation `refund` / `cancel_refund`. Close itself is also `close_refund` with operation `close` / `cancel_close`.
- E-wallet (LINE Pay / Taiwan Pay) path is different: `ewallet_refund` — the credit card close_refund tool will not work for wallet rails.
- Always check `query_trade` first to confirm `CloseStatus` (3 = settled) before choosing the refund tool.

## Gotchas

- **TradeSha is NOT a generic alphabetical-sort HMAC.** It is `SHA256("HashKey={key}&{TradeInfo blob}&HashIV={iv}").upper()` — `HashKey` first, `HashIV` last, the literal encrypted `TradeInfo` sandwiched between, and the result in uppercase hex. Developers who treat it as "sort params alphabetically and HMAC them" build something that validates against nothing. `mcp-newebpay` handles this for you; if you hand-roll a verifier for NotifyURL, copy the exact format.
- **NotifyURL can arrive before, after, or simultaneously with ReturnURL.** Never close an order on ReturnURL alone — the browser can be closed, the redirect can fail, or NotifyURL can beat the redirect to your server. Treat ReturnURL as "show the customer a thank-you page"; treat NotifyURL as "the money moved". If your order state machine depends on ordering, you will ship double-fulfillment or ghost-open-orders.
- **NDNF and NDNP use different MerchantID / HashKey / HashIV.** Cross-contaminating them produces a signature-valid-but-wrong-merchant request that NewebPay rejects with a generic error. `mcp-newebpay` uses separate env groups (`NEWEBPAY_NDNF_*` vs `NEWEBPAY_NDNP_*`) specifically to prevent this; do not unify them in wrapper code.
- **HashIV must be exactly 16 bytes; HashKey must be exactly 32 bytes.** Merchants migrating from the older MPG1 protocol often re-use MPG1 keys of the wrong length — AES-256-CBC then pads/truncates silently and every request fails decryption on NewebPay's side with an opaque "參數錯誤" (parameter error). If all requests are failing, check the lengths before anything else.
- **定期定額 does not auto-handle card expiry.** When a customer's card expires, NewebPay marks the mandate as failed on the next cycle and fires NotifyURL with a failure code — but does not automatically suspend the mandate. Your backend must detect the failure code, notify the customer (SMS / email with an update-card link), and decide whether to `alter_period_status` to pause. Silent failures accumulate as unpaid subscription months.
- **Test endpoint is `ccore.newebpay.com`; production is `core.newebpay.com`.** Both accept differently-provisioned MerchantID / HashKey pairs; a test key against the prod endpoint (or vice versa) returns "MerchantID 不存在" which looks like a bad credential but is really a wrong-endpoint bug. `mcp-newebpay` switches via `NEWEBPAY_ENV=test|production`; verify this before debugging credentials.

## IRON LAW

**NotifyURL is the source of truth, not ReturnURL.** Never transition an order to "paid" — and never trigger downstream effects like e-invoice issuance, fulfillment, or subscription activation — based on ReturnURL parameters or the browser redirect. Two specific failure modes this prevents: (1) double-fulfillment when the customer closes the browser early and retries, arriving on ReturnURL twice; (2) ghost-open orders when NotifyURL fires but the browser never reaches ReturnURL (airplane mode, network drop). If NotifyURL has not been received and verified server-side, the order is open — regardless of what the ReturnURL page says. When in doubt, call `query_trade` to re-confirm; treat that server response as equivalent to a NotifyURL retry.

### Rationalization Table

| "但是…" | 為什麼錯 |
|---|---|
| 客戶已經在感謝頁了，付款應該成功了 | ReturnURL 可以被重新整理重放、也可以在付款失敗後仍然跳轉（NewebPay 某些錯誤路徑仍會跳回 ReturnURL）|
| NotifyURL 和 ReturnURL 幾乎同時到，先用 ReturnURL 更新再等 NotifyURL 確認就好 | 非同步順序無法保證；高流量期間兩者可差數分鐘，先更新會產生競態條件導致雙重履行 |
| 我需要立刻給客戶看訂單確認，等 NotifyURL 太慢 | ReturnURL 完全可以用於顯示 UI（「處理中，請稍候」），訂單狀態變更必須等 NotifyURL；這兩件事不衝突 |
| 我們的 NotifyURL 偶爾收不到，所以 ReturnURL 是備援 | 備援邏輯應是「若 N 分鐘內未收到 NotifyURL，呼叫 `query_trade` 主動查詢」，而非信任 ReturnURL |

## Output Format

When completing a NewebPay task, produce this structure:

```markdown
# NewebPay Task: {one-line summary}

## Context
- API family: {NDNF one-off | NDNP recurring | mixed}
- Environment: {test (ccore) | production (core)}
- Payment methods enabled: {CREDIT, VACC, CVS, LINEPAY, ...}
- MerchantOrderNo scheme: {…}

## Tool Plan
| Step | Tool | Family | Purpose |
|------|------|--------|---------|
| 1 | create_mpg_payment | NDNF | Build encrypted form for browser redirect |
| 2 | (browser POSTs form) | — | Customer completes 3DS 2.0 on NewebPay |
| 3 | NotifyURL handler | — | Decrypt TradeInfo, verify TradeSha, update order |
| 4 | query_trade | NDNF | Reconciliation on doubt |
| … | … | … | … |

## Callback Handling
- NotifyURL verification: TradeSha recomputed with HashKey={…}&{TradeInfo}&HashIV={…} uppercased: Y/N
- ReturnURL treated as UI-only (no state mutation): Y/N
- query_trade fallback on missed NotifyURL: Y/N
- Idempotency key: MerchantOrderNo

## Assumptions & Open Questions
- {assumption grounded in a NewebPay constraint}
- TODO: {anything that needs verification against NewebPay merchant portal or NDNF/NDNP PDF}

## Deliverable
{the actual integration, reconciliation report, or change summary}
```

## Related

- **MCPs**: `mcp-newebpay`
- **Skills**: `tw-payment-integration` (gateway comparison decision), `tw-ecom-payment-dispute` (chargeback / 爭議款 handling), `tw-ecom-invoice-ezpay` (e-invoice handoff after successful payment), `tw-ecom-dtc-shopline` (storefront integration)
- **References**: `references/integration-flow.md` (merchant setup → first transaction → callback → reconciliation), `examples/sample_scenario.md` (subscription billing with ezPay invoice and dispute handling)

_Last verified: 2026-04_
