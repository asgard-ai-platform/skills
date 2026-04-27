# NewebPay Integration Flow — Setup to Reconciliation

End-to-end wiring for a Taiwan merchant integrating NewebPay through `mcp-newebpay`. Tool names are the exact `mcp-newebpay` tools (2026-04 snapshot, 8 tools total). Where official docs are the canonical reference, the NDNF / NDNP PDF page is cited rather than re-copied.

---

## Phase 1 — Merchant setup (one-time)

1. **Sign the NewebPay merchant contract.** Two product lines:
   - **NDNF (線上交易)** — required for any one-off payment. Returns `MerchantID`, `HashKey` (32 chars), `HashIV` (16 chars).
   - **NDNP (信用卡定期定額)** — required for 定期定額 / subscription. Separate application, separate `MerchantID`/`HashKey`/`HashIV`.

   > TODO: verify from NewebPay merchant portal — exact fee rates for credit card, ATM, CVS, LINE Pay. Rates depend on merchant category (MCC) and monthly volume tier; do not hard-code.

2. **Configure `mcp-newebpay` env.** Per the README:

   ```
   NEWEBPAY_ENV=test
   NEWEBPAY_NDNF_MERCHANT_ID=...
   NEWEBPAY_NDNF_HASH_KEY=...
   NEWEBPAY_NDNF_HASH_IV=...
   NEWEBPAY_NDNP_MERCHANT_ID=...
   NEWEBPAY_NDNP_HASH_KEY=...
   NEWEBPAY_NDNP_HASH_IV=...
   ```

   Only set the NDNP group if you will accept 定期定額; otherwise those tools will return a clear "not configured" error.

3. **Whitelist NotifyURL / ReturnURL in the merchant portal.** NewebPay will only POST to URLs pre-registered under the merchant. Common error: forgetting to register the production URL when switching `NEWEBPAY_ENV=production`.

4. **Decide payment methods to enable** per the NDNF PDF §2.2 — `CREDIT`, `VACC` (ATM 虛擬帳號), `CVS`, `BARCODE`, `LINEPAY`, `APPLEPAY`, `SAMSUNGPAY`, `ESUNWALLET`, `TAIWANPAY`. Enabling a method in the request without it being enabled on the merchant portal returns an error at form submission time, not at `create_mpg_payment` time.

---

## Phase 2 — First transaction (one-off, NDNF)

### Step 2.1 — Merchant backend: request form data

```
create_mpg_payment(
  MerchantOrderNo = {your_idempotency_key},   # unique per attempt
  Amt             = {integer TWD},
  ItemDesc        = "...",
  Email           = "{customer email}",
  NotifyURL       = "https://merchant.example.com/newebpay/notify",
  ReturnURL       = "https://merchant.example.com/newebpay/return",
  payment_methods = ["CREDIT", "VACC"],       # subset of enabled methods
  ExpireDate      = "YYYYMMDD",               # ATM / CVS only
)
```

Returns `{url, form_data: {MerchantID, TradeInfo, TradeSha, Version}}`.

### Step 2.2 — Browser: auto-submit form

Merchant's page must render an HTML form with all `form_data` keys as hidden inputs, `action={url}`, and a JS auto-submit on load. Do **not** attempt server-side redirect — 3DS 2.0 requires the customer's own browser.

### Step 2.3 — Customer completes on NewebPay hosted page

NewebPay handles card input, 3DS 2.0 (liability shift to issuer), and OTP. Merchant backend sees nothing during this phase — PAN never touches merchant infrastructure.

### Step 2.4 — NotifyURL (server-to-server) — TRUST THIS

NewebPay POSTs (form-encoded) to `NotifyURL`:

```
Status, MerchantID, Version, TradeInfo, TradeSha
```

Merchant handler must:

1. Verify `TradeSha == SHA256("HashKey={key}&{TradeInfo}&HashIV={iv}").upper()`. Any mismatch → reject (attacker / replay).
2. AES-256-CBC decrypt `TradeInfo` with the same HashKey / HashIV to get the JSON payload with `Status`, `MerchantOrderNo`, `TradeNo`, `Amt`, `PaymentType`, `RespondCode`, etc.
3. Verify `MerchantOrderNo` and `Amt` match the order in your DB (prevents amount tampering).
4. If `Status == "SUCCESS"`, transition order to paid (idempotent on `MerchantOrderNo`) and respond `1|OK` to NewebPay.
5. If `Status != "SUCCESS"`, record the failure reason but do not mark the order paid.

### Step 2.5 — ReturnURL (browser redirect) — UI ONLY

NewebPay redirects the customer's browser to `ReturnURL` with the same payload shape. The merchant page must:

- Show the customer an acknowledgement based on `Status`
- **Not** mutate order state — that is already handled by NotifyURL
- Handle the case where NotifyURL has not yet been processed (race): show "processing" and poll your own DB, or call `query_trade` server-side

See main SKILL.md IRON LAW — ReturnURL is display-only.

---

## Phase 3 — Callback handling edge cases

- **Missed NotifyURL** (webhook timeout, merchant server down): fall back to `query_trade(MerchantOrderNo, Amt)` on a reconciliation cron (hourly for today, daily for older). Tool returns the same `Status`/`TradeStatus`/`Amt`/`PaymentType`/`CloseStatus`/`BackStatus` as NotifyURL would.
- **Duplicate NotifyURL**: NewebPay retries on non-`1|OK` responses. Handler must be idempotent keyed on `MerchantOrderNo`.
- **ATM/CVS delayed payment**: `create_mpg_payment` for `VACC`/`CVS` returns a virtual account number / barcode. Customer may pay days later. NotifyURL fires only on actual payment, not on form generation. Between form generation and payment, `query_trade` returns `TradeStatus=0` (pending).
- **3DS 2.0 declined by issuer**: NotifyURL fires with `Status != "SUCCESS"` and a specific `RespondCode`. Not a merchant-side bug; surface the code to the customer (NewebPay maps codes in the NDNF PDF §6).

---

## Phase 4 — Post-payment operations

**Close (請款)** — for credit card, the initial authorization must be closed to actually settle funds (default auto-close is usually on, but confirm per merchant contract).

```
close_refund(MerchantOrderNo=..., Amt=..., CloseType="close")
```

**Refund before close** — release the authorization hold:

```
cancel_authorization(MerchantOrderNo=..., Amt=...)
```

**Refund after close** — money was already settled:

```
close_refund(MerchantOrderNo=..., Amt=..., CloseType="refund")
```

**E-wallet refund** (LINE Pay / Taiwan Pay / etc. — NOT credit card):

```
ewallet_refund(MerchantOrderNo=..., Amt=...)
```

Always `query_trade` first to read `CloseStatus` (1=pending, 2=close requested, 3=settled) and `BackStatus` (0=none, 1=refund requested, 2=refunded) before choosing the correct tool. Calling `close_refund` on a wallet transaction, or `ewallet_refund` on a credit card, returns a generic failure.

> TODO: verify from NewebPay merchant portal — refund window (days after close during which `close_refund refund` is allowed). Commonly cited as same-bimonthly / 60 days but varies by acquirer.

---

## Phase 5 — Recurring payment setup (NDNP)

### Step 5.1 — Mandate creation

```
create_period_payment(
  MerOrderNo     = {idempotency key},
  ProdDesc       = "Annual membership",
  PeriodAmt      = 149,
  PeriodType     = "M",                  # D/W/M/Y per NDNP PDF §3.2
  PeriodPoint    = "05",                 # day-of-cycle
  PeriodStartType = 1,                   # 1 = charge 10 TWD to verify card
  PeriodTimes    = 12,                   # 0 = indefinite, else cycle count
  NotifyURL      = "https://merchant.example.com/newebpay/period_notify",
  ReturnURL      = "https://merchant.example.com/newebpay/period_return",
  Email          = "{customer email}",
)
```

Returns `{url, form_data}` — same browser-flow shape as NDNF. Customer does one interactive authorization (usually `PeriodStartType=1` triggers a 10 TWD verification charge that is refunded); after that, NewebPay charges on the cycle automatically.

### Step 5.2 — Per-cycle NotifyURL

Every cycle, NewebPay POSTs to `NotifyURL` with:

- `PeriodNo` — the canonical mandate handle (e.g., `P260403144725zl3MVV`)
- `MerOrderNo` of the original mandate
- `OrderNo` per-cycle (different from MerOrderNo)
- `Status`, `RespondCode`, `NextTime` (next billing date), etc.

Merchant must extend the service period on `Status == "SUCCESS"` and trigger dunning (SMS / email / retry-with-new-card flow) on failure. See Gotchas in main SKILL.md — card expiry does not auto-pause the mandate.

### Step 5.3 — Mandate modifications

- **Pause / resume / terminate** — `alter_period_status(PeriodNo, AlterType="suspend"|"restart"|"terminate")`
- **Change amount / cycle / expiry** — `alter_period_content(PeriodNo, ...)` — takes effect next cycle, not immediately

---

## Phase 6 — Reconciliation

Daily job:

1. For every order in merchant DB with state `paid` in the last 24h, call `query_trade` and verify `TradeStatus=1`, `Amt` matches, `CloseStatus` is as expected.
2. For every order with state `pending` older than 72h (ATM/CVS not paid), call `query_trade` — if still `TradeStatus=0`, mark expired.
3. For every NDNP mandate, compare expected next-charge dates against `NextTime` from the last NotifyURL. If a cycle was skipped with no failure NotifyURL, something is wrong — contact NewebPay support.

> TODO: verify from NewebPay merchant portal — whether the portal exposes a batch reconciliation report export; if so, daily `query_trade` polling is redundant and the export is the preferred reconciliation source.

---

## Tool → API → phase cross-reference

| Tool | API | Phase | Notes |
|------|-----|-------|-------|
| `create_mpg_payment` | NPA-F01 | 2.1 | One-off, browser flow |
| `query_trade` | NPA-B02 | 3, 6 | Canonical server-side truth |
| `cancel_authorization` | NPA-B01 | 4 | Credit card, pre-close only |
| `close_refund` | NPA-B031~34 | 4 | Credit card close / refund / cancel variants |
| `ewallet_refund` | NPA-B06 | 4 | Wallet rails only, NOT credit card |
| `create_period_payment` | NPA-B05 | 5.1 | NDNP mandate creation |
| `alter_period_status` | NPA-B051 | 5.3 | Pause / resume / terminate |
| `alter_period_content` | NPA-B052 | 5.3 | Amount / cycle / expiry |
