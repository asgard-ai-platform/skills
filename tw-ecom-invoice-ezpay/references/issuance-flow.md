# ezPay Issuance Flow — Setup to Daily Reconciliation

End-to-end wiring for a Taiwan merchant issuing e-invoices through ezPay via `mcp-ezpay-einvoice`. Tool names are the exact `mcp-ezpay-einvoice` tools (2026-04 snapshot, 7 tools). Foundational material (what is 統一發票, what is a carrier) lives in `tw-einvoice-guide` — this doc covers ezPay-specific wiring only.

---

## Phase 1 — Registration with ezPay (one-time)

1. **Open the ezPay merchant account.** Two environments, each with its own signup:
   - **Test**: https://cinv.ezpay.com.tw/ — use for all pre-go-live development. Invoices issued here are NOT reported to MOF and do not consume real 字軌 ranges.
   - **Production**: https://inv.ezpay.com.tw/ — only after the merchant's 統編 and 電子發票 platform registration are complete.

2. **Collect the three credentials** that `mcp-ezpay-einvoice` needs:
   - `EZPAY_MERCHANT_ID` — the merchant identifier assigned by ezPay
   - `EZPAY_HASH_KEY` — 32-character AES-256 key
   - `EZPAY_HASH_IV` — 16-character AES-CBC IV
   - `EZPAY_IS_PRODUCTION` — `false` for test, `true` for prod

   HashKey length = 32, HashIV length = 16. Other lengths silently pad or truncate and every request fails with `LIB10002` (encryption verification failed). If all calls return `LIB10002`, check lengths before anything else.

3. **Register on 財政部電子發票整合服務平台.** The merchant must exist on the MOF platform with ezPay listed as their 加值服務中心. This authorization is what lets ezPay upload invoices on the merchant's behalf. Without it, issuance at ezPay succeeds locally but uploads to MOF fail silently. (TODO: verify the exact MOF-platform authorization form name — commonly referenced as 加值中心委任書 but terminology shifts by year.)

---

## Phase 2 — 字軌 (invoice-number range) request

字軌 is a block of invoice numbers that 財政部 pre-assigns per bimonthly period. Your merchant cannot generate numbers — MOF generates the range, you draw from it.

1. **Request the current-period range** from MOF (via the 財政部電子發票整合服務平台 or your accountant). Ranges are formatted like `TE00000000–TE99999999` for a 8-digit numeric segment under a 2-letter prefix.

2. **Upload/assign the range to ezPay** so ezPay knows which numbers it is authorized to issue against. Without this step, `issue_invoice` returns an error indicating no available number. (TODO: verify the exact ezPay portal path for 字軌 assignment — the ezPay 發票管理 section is the likely home but confirm current UI.)

3. **Request the NEXT period's range at least 2 weeks before rollover.** MOF assigns ranges on request, not automatically. Running out mid-period blocks issuance until the next range is active. Budget range size against historical volume plus growth (50-100% headroom).

4. **Monitor remaining numbers.** The ezPay portal shows remaining count per 字軌; set a weekly cron / alert to flag when usage crosses 70% of the active range.

---

## Phase 3 — Sandbox integration (test env)

1. **Configure `mcp-ezpay-einvoice` env** with test credentials:

   ```
   EZPAY_MERCHANT_ID=<test_merchant_id>
   EZPAY_HASH_KEY=<test_hash_key>
   EZPAY_HASH_IV=<test_hash_iv>
   EZPAY_IS_PRODUCTION=false
   ```

2. **Validate with `scripts/auth/test_connection.py`** (per the README) before any issuance. Failures here are almost always: wrong credential length, wrong environment (prod key against test endpoint), or missing `EZPAY_IS_PRODUCTION`.

3. **Issue representative invoices** covering the shapes you need:
   - B2C with 手機條碼 carrier (`carrier_type="0"`, `carrier_num="/ABC1234"`, `print_flag="N"`)
   - B2C with 捐贈碼 (`love_code="123"` through 7-digit ranges; mutually exclusive with carrier)
   - B2B with 統編 (`category="B2B"`, `buyer_ubn="12345678"`, `print_flag="Y"`)
   - Multi-item with pipe-delimited arrays — verify every item landed on the right row via `query_invoice`
   - Scheduled invoice (`status="3"`, `create_status_time="YYYY-MM-DD"`) then `trigger_invoice` to issue early

4. **Exercise the correction paths:**
   - Void an invoice (`void_invoice`), then `query_invoice` to confirm state
   - Attempt to void the same invoice again → expect `INV20001`
   - Issue an allowance (`issue_allowance`) for a partial refund, then `trigger_allowance` with `allowance_status="C"` to confirm
   - Void the confirmed allowance (`void_allowance`) and confirm the invoice amount rebounds

5. **Decrypt responses.** ezPay returns AES-256-CBC-encrypted bodies with a SHA-256 `CheckCode`. `mcp-ezpay-einvoice` decrypts and verifies for you — do not re-implement unless you have a specific reason (see the README for the exact format).

---

## Phase 4 — Production migration

1. **Swap credentials.** Replace test credentials with production:

   ```
   EZPAY_MERCHANT_ID=<prod_merchant_id>
   EZPAY_HASH_KEY=<prod_hash_key>
   EZPAY_HASH_IV=<prod_hash_iv>
   EZPAY_IS_PRODUCTION=true
   ```

   Test and production are entirely different endpoints (`cinv.ezpay.com.tw` vs `inv.ezpay.com.tw`) with separate merchant IDs. A test merchant ID against the production endpoint returns `LIB10001` (merchant ID does not exist) — looks like a bad credential, is really a wrong-environment bug.

2. **Confirm the first live invoice end-to-end:**
   - Issue a minimal real-value invoice (e.g., NT$1 internal test)
   - `query_invoice` to confirm ezPay state = issued
   - Check the 財政部電子發票整合服務平台 manually within 24h to confirm the invoice uploaded
   - Void or allowance it immediately so it does not stay on the books

3. **Pre-flight failure-mode checklist** before opening the firehose:
   - [ ] 字軌 range active and has headroom for expected daily volume
   - [ ] Carrier validation in the backend (not the UI only)
   - [ ] Allowance path tested end-to-end
   - [ ] Daily reconciliation job (Phase 5) deployed and green on day 1

---

## Phase 5 — Daily reconciliation (ezPay ↔ MOF)

The IRON LAW: MOF is the source of truth, ezPay is a cache. Reconcile every issuance against MOF once per day.

### Daily job (recommended cron: 02:00 TW time, after ezPay's nightly batch settles)

For every invoice issued in the last 48 hours:

1. **Internal DB → ezPay**: call `query_invoice(search_type="1", merchant_order_no, total_amt)`. Expected: `SUCCESS` + matching `InvoiceNumber` + `Status=1` (issued). Mismatch → flag for manual review; do NOT auto-retry `issue_invoice` (would create duplicates).

2. **ezPay → MOF platform**: fetch the MOF upload status for the invoice number. Two shapes:
   - MOF platform manual export (CSV by bimonthly period)
   - (TODO: verify whether ezPay portal exposes a per-invoice MOF-upload-status field, which would let the reconciliation be a single `query_invoice` parse.)

3. **Three-way reconciliation**: internal DB = ezPay = MOF. Any divergence goes into a `reconciliation_queue` table with enough context to fix manually:
   - DB has invoice, ezPay does not → `query_invoice` returned empty; investigate whether issuance actually fired (check app logs for ezPay response)
   - DB + ezPay agree, MOF missing → upload lag (wait 24h then escalate); if >72h, support ticket to ezPay
   - DB + MOF agree, ezPay state stale → safe (MOF is truth); log and move on
   - DB voided, ezPay issued → race condition; call `void_invoice` with audit trail

4. **Allowance reconciliation** runs on the same cadence: internal refund records ↔ ezPay allowance state ↔ MOF. Confirmed allowances (`allowance_status="C"`) must appear on MOF; cancelled (`"D"`) must not.

### Weekly

- Count remaining 字軌 numbers per active range. If any range is <30% remaining, request the next one.
- Export the bimonthly MOF platform 401 data and diff against internal revenue. Any missing invoice identified here is already a filing problem — fix before the 15th of the next odd month.

---

## Tool → phase cross-reference

| Tool | Phase | Notes |
|------|-------|-------|
| `issue_invoice` | 3 (sandbox), 4-5 (prod) | Validate carrier + category client-side first |
| `trigger_invoice` | 3, 5 | Only if invoice was created with `status="3"` (scheduled) |
| `void_invoice` | 3, 5 | Same-bimonthly only; else use allowance path |
| `issue_allowance` | 3, 5 | Partial refunds, cross-period corrections |
| `trigger_allowance` | 3, 5 | `"C"` to confirm / `"D"` to cancel before filing |
| `void_allowance` | 3, 5 | Only within allowance's own void window |
| `query_invoice` | 3-5 | ezPay cache — NOT a substitute for MOF reconciliation |

---

## Common error codes (from README)

| Code | Meaning | Typical cause |
|------|---------|---------------|
| `LIB10001` | Merchant ID does not exist | Wrong env (test key on prod endpoint or vice versa) |
| `LIB10002` | Encryption verification failed | HashKey ≠ 32 chars or HashIV ≠ 16 chars |
| `LIB10003` | Timestamp expired | Client clock skew; sync NTP |
| `INV10001` | Duplicate merchant order number | Retrying issuance after a prior success; use `query_invoice` first |
| `INV10003` | Invoice number does not exist | Typo or querying a voided-then-purged record |
| `INV20001` | Invoice already voided | Double-void attempt; state is already correct |
| `INV20002` | Void period has passed | Cross-bimonthly — switch to `issue_allowance` |
| `ALW10001` | Allowance exceeds invoice amount | Split into multiple allowances across original invoices |
| `ALW10002` | Allowance number does not exist | Stale handle; re-query |

For the full list, see the ezPay developer portal.
