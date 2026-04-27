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

# ezPay E-Invoice Methodology

## When to use this skill

- Issuing B2B or B2C 統一發票 from a Taiwan storefront, POS, or SaaS backend through ezPay (藍新系) as the 加值服務中心
- Attaching a consumer carrier — 手機條碼 (`/XXXXXXX`), 自然人憑證, or 會員載具 — so the invoice is not printed on paper
- Voiding a wrongly-issued invoice within the same bimonthly period, or issuing an allowance (折讓) when the void window has closed
- Issuing or triggering a scheduled invoice (`status="3"`) that must go live on a later date (e.g., subscription renewal)
- Reconciling ezPay-issued invoices against the 財政部電子發票整合服務平台 daily to catch upload lag or dropped records
- Debugging opaque ezPay responses: `LIB10002` encryption failures, `INV20002` void-window errors, `ALW10001` allowance-over-invoice errors

## Do NOT use when

- The merchant connects to the 財政部 platform directly (no 加值中心) — use `tw-einvoice-guide` for the MOF-direct pattern and concepts
- The storefront is on UniversalEC (統一發票整合服務) or another 加值中心 (ECPay 綠界, 銓葳) — they have different tool shapes; this skill's gotchas are ezPay-specific
- You only need the API schema for one ezPay endpoint — read the tool description in `mcp-ezpay-einvoice` or the ezPay developer portal at https://inv.ezpay.com.tw/
- The question is "what is a 手機條碼" or "B2B vs B2C invoice format" — that is foundational material already covered by `tw-einvoice-guide`. This skill assumes you know the landscape

## Core concepts

ezPay is a 加值服務中心 — a middleman that batches merchant invoice requests, uploads them to the 財政部電子發票整合服務平台 on the merchant's behalf, and relays carrier / 捐贈碼 lookups back. The merchant's legal counterparty for tax purposes is **still 財政部**; ezPay is an operational convenience, not the source of truth.

`mcp-ezpay-einvoice` wraps 7 tools over the ezPay API:

- Invoice lifecycle: `issue_invoice`, `trigger_invoice`, `void_invoice`, `query_invoice`
- Allowance (折讓) lifecycle: `issue_allowance`, `trigger_allowance`, `void_allowance`

**Category.** `category="B2B"` requires `buyer_ubn` (統編) — omit it and the invoice silently becomes B2C (lottery-eligible, wrong tax reporting). `category="B2C"` attaches a carrier or prints paper.

**Carriers.** `carrier_type="0"` + `carrier_num="/ABC1234"` for 手機條碼 (slash + 7 chars). `carrier_type="1"` for 自然人憑證 (2 letters + 14 digits). `carrier_type="2"` for ezPay 會員載具. `love_code` (3-7 digits) for 捐贈碼 — mutually exclusive with carriers.

**字軌.** 財政部 assigns invoice-number ranges (字軌) per bimonthly period (e.g., `TE00000000-TE99999999`). ezPay draws from this pool on issuance. Exhausting the range blocks issuance — the MOF assigns the next period's range in advance, but only if you requested it.

**Void vs allowance.** `void_invoice` only works inside the same bimonthly period the invoice was issued (see Gotchas). After the period closes, corrections must go through `issue_allowance` → `trigger_allowance` (status `C`=confirm, `D`=cancel).

## Decision tree

```
What is the user asking for?
│
├─ Issue a NEW invoice?
│    ├─ Buyer has 統編?  → issue_invoice(category="B2B", buyer_ubn=...)
│    └─ Consumer?         → issue_invoice(category="B2C", carrier_type/carrier_num
│                                         OR love_code OR print_flag="Y")
│
├─ Scheduled invoice (issue on a future date)?
│    → issue_invoice(status="3", create_status_time="YYYY-MM-DD")
│      Later: trigger_invoice(invoice_trans_no, merchant_order_no, total_amt)
│
├─ Correct a WRONG invoice?
│    ├─ Issued in the CURRENT bimonthly period?
│    │    → void_invoice(invoice_number, invalid_reason)
│    │      (Then re-issue fresh if needed)
│    └─ Issued in a PAST bimonthly period?
│         → issue_allowance(invoice_no, items, total_amt)
│             → trigger_allowance(allowance_no, allowance_status="C")
│           (Voiding the allowance later: void_allowance)
│
├─ Partial refund (return 1 of 3 items)?
│    → issue_allowance against the original invoice for the returned portion only
│
└─ "Did this invoice issue?" / "What's the status of order X?"
     → query_invoice(search_type="0" by invoice number, "1" by merchant_order_no)
       Treat ezPay's answer as a local cache — MOF platform is the authority
```

Void-window boundary: per the README, the cutoff is roughly "before the 14th of the next odd month" (e.g., Mar-Apr invoices must be voided before May 14). Confirm the exact cutoff against the current MOF calendar — it shifts with national holidays.

## Implementation guidance

Three flows. For each, the exact `mcp-ezpay-einvoice` tool is named. See `references/issuance-flow.md` for setup wiring and `examples/sample_scenario.md` for an end-to-end Shopline → ezPay → allowance walkthrough.

**Issue invoice (one-shot, post-payment)**

1. Trigger from the payment-success callback (NotifyURL on NewebPay / ECPay / TapPay). Never issue from the browser ReturnURL — see `tw-ecom-payment-newebpay` IRON LAW.
2. Before calling `issue_invoice`, validate the carrier client-side: `/` + 7 alphanumeric for 手機條碼; 2 letters + 14 digits for 自然人憑證. An invalid carrier string returns a generic ezPay error and the invoice is never created.
3. Call `issue_invoice` with `category`, `tax_type="1"` (應稅), `amt` (pre-tax), `tax_amt`, `total_amt` (`amt + tax_amt`), pipe-delimited item arrays, and `print_flag="N"` when a carrier is supplied.
4. Persist the returned `InvoiceNumber`, `InvoiceTransNo`, and `RandomNumber` keyed on your internal `merchant_order_no`. The random number is required for 中獎 cross-reference later.

**Void invoice (same-period correction)**

1. Call `query_invoice` first to confirm the invoice is still voidable — a previously-voided invoice returns `INV20001`; an out-of-window invoice returns `INV20002`.
2. Call `void_invoice(invoice_number, invalid_reason)`. The reason string is a free-text audit field — keep it specific (e.g., "buyer cancelled before shipment", not "誤開").
3. If you need to re-issue, call `issue_invoice` with a **new** `merchant_order_no` — the old one is now permanently associated with the voided invoice, and re-using it returns `INV10001` (duplicate merchant order number).

**Allowance / 折讓 (cross-period correction or partial refund)**

1. Call `issue_allowance(invoice_no, items[], total_amt)` with only the returned/refunded items. Allowance `total_amt` includes both goods and tax components (per the README example: 65 item + 3 tax = 68 total).
2. Allowance starts in a pending state. Call `trigger_allowance(allowance_no, allowance_status="C")` to confirm (or `"D"` to cancel before it is filed with MOF).
3. If the allowance itself was filed incorrectly, `void_allowance(allowance_no, invalid_reason)` reverses it — but only within the allowance's own voidability window (analogous to invoice void, but tracked separately).
4. Allowance amount must not exceed the original invoice amount — `ALW10001` fires if so. For a full refund that exceeds a single invoice, you need one allowance per invoice, not a combined one.

## Gotchas

- **字軌 exhaustion silently blocks issuance.** MOF assigns number ranges per bimonthly period; ezPay draws from them. If you don't request the next period's range in advance (via the ezPay merchant portal or MOF platform), the first issuance attempt after the rollover fails with an opaque error. Monitor remaining-number count weekly and request the next range at least 1 bimonthly period ahead. (TODO: verify the exact portal path and any ezPay auto-refill option against the current ezPay merchant portal.)
- **Void window is same-bimonthly only; cross-period corrections need 折讓.** Per the README, an invoice issued in March-April can be voided before roughly May 14. A March invoice discovered wrong in June cannot be voided — `void_invoice` returns `INV20002` (void period has passed). The only correction path is `issue_allowance` + `trigger_allowance`. Agents who retry `void_invoice` indefinitely never resolve the error.
- **手機條碼 format is strict: `/` + exactly 7 alphanumeric characters.** `ABC1234` (no slash), `/ABC12345` (8 chars), lowercase, or a scanned barcode with leading whitespace all fail. Validate client-side before `issue_invoice` — ezPay's error for invalid carriers is generic, and the invoice is not created, so you cannot recover by patching. Many POS scanners also need to be configured to emit the `/` prefix; test with real 手機條碼 barcodes, not typed input.
- **Missing `buyer_ubn` on a B2B sale silently becomes B2C.** `category="B2B"` without `buyer_ubn` will be rejected, but `category="B2C"` with a business buyer that SHOULD have had a 統編 issues a B2C invoice — which is lottery-eligible and taxed differently. When the buyer exists in your CRM as a company, enforce `category="B2B"` + `buyer_ubn` in your backend, not the UI. UI-only enforcement is bypassed by webhooks replaying a stale payload.
- **ezPay state can lag the MOF platform — reconcile against MOF, not ezPay.** `query_invoice` returns ezPay's internal record. The 財政部電子發票整合服務平台 is where tax liability is established, and ezPay uploads in batches. A successful `query_invoice` does not prove the invoice is on the MOF platform. Run a daily reconciliation job that fetches the MOF upload status (per invoice or per batch) and reconciles against your DB. Trust neither ezPay's local state nor your own DB as the source of truth for tax filing. (TODO: verify exact ezPay-to-MOF upload latency from the ezPay merchant portal reporting dashboard.)
- **Pipe-delimited item arrays are positional — one misaligned field corrupts every item.** `item_name="拿鐵|蛋糕"`, `item_count="2|1"`, `item_price="65|85"`, `item_amt="130|85"` must all have the same pipe count and the same order. A leading or trailing `|`, or a missing field on one line, shifts every subsequent item's price onto the wrong name. ezPay does not validate alignment — it stores whatever you send. Audit with `query_invoice` after issuance on every flow change.

## IRON LAW

**MOF is the source of truth; ezPay state can lag.** Never close the books, never file 401 (營業稅), and never tell the customer "invoice issued" based solely on an ezPay `SUCCESS` response or a `query_invoice` hit. ezPay is a batching 加值中心 — its local record can be ahead of, behind, or silently out-of-sync with the 財政部電子發票整合服務平台. Run daily reconciliation against the MOF platform's upload status for every invoice issued in the prior 48 hours. Any ezPay record without a confirmed MOF upload is pending, not issued. Two failure modes this prevents: (1) 營業稅 filing with phantom invoices that MOF never received (audit finding, fine); (2) customer-facing claims of "invoice issued" when the carrier/lottery record does not exist on MOF (consumer complaint, brand damage). When in doubt, MOF wins.

### Rationalization Table

| "但是…" | 為什麼錯 |
|---|---|
| `issue_invoice` 回傳 `SUCCESS`，發票一定開出去了 | `SUCCESS` 只代表 ezPay 本地接受請求；上傳財政部是非同步批次，可能延遲數小時或靜默失敗 |
| `query_invoice` 查得到這張發票，代表 MOF 也有 | `query_invoice` 查的是 ezPay 本地快取，不是財政部電子發票整合服務平台 |
| 客戶手機條碼已經收到通知，所以發票在 MOF 上了 | 載具通知由 ezPay 發送，與 MOF 上傳是不同的非同步流程，兩者可不同步 |
| 每張都對帳太耗效能，ezPay 不太會出錯 | 出錯頻率低不等於零；稅務申報錯誤的代價（罰款、重審）遠高於每日對帳的成本 |

## Output Format

When completing an ezPay invoice task, produce this structure:

```markdown
# ezPay Invoice Task: {one-line summary}

## Context
- Environment: {test (cinv.ezpay.com.tw) | production (inv.ezpay.com.tw)}
- Category: {B2B | B2C | mixed}
- Carrier strategy: {手機條碼 | 自然人憑證 | 會員載具 | 捐贈碼 | 紙本}
- Trigger source: {payment NotifyURL | scheduled | manual | reconciliation}

## Tool Plan
| Step | Tool | Purpose |
|------|------|---------|
| 1 | query_invoice | Pre-check for duplicate merchant_order_no |
| 2 | issue_invoice | B2B/B2C issuance with validated carrier |
| 3 | (MOF reconciliation) | Confirm upload status against MOF platform |
| … | … | … |

## Correction Path (if applicable)
- Same-period: void_invoice → (optionally) re-issue_invoice with new merchant_order_no
- Cross-period or partial: issue_allowance → trigger_allowance (status="C")

## Assumptions & Open Questions
- Tax semantics: {tax_type="1" 應稅 with tax_rate=5, amt/tax_amt/total_amt consistent}
- Carrier validated client-side before API call: Y/N
- 統編 validated against company registry (if B2B): Y/N
- TODO: {anything that needs verification against ezPay merchant portal or MOF platform}

## Reconciliation
- ezPay → MOF upload check window: {24h / 48h / …}
- Mismatch handling: {retry / manual portal fix / support ticket}
- Daily reconciliation job: Y/N, cron at {…}

## Deliverable
{the actual issuance record, correction summary, or reconciliation report}
```

## Related

- **MCPs**: `mcp-ezpay-einvoice`
- **Skills**: `tw-einvoice-guide` (MOF platform landscape, B2B/B2C/carrier basics), `tw-ecom-invoice-carrier` (carrier-specific patterns — skeleton), `tw-ecom-invoice-void` (void vs allowance decision — skeleton), `tw-tax-basics` (營業稅 401 filing reconciliation), `tw-ecom-payment-newebpay` (upstream trigger via payment NotifyURL), `tw-ecom-dtc-shopline` (order-to-invoice handoff)
- **References**: `references/issuance-flow.md` (registration → 字軌 → sandbox → prod → daily reconciliation), `examples/sample_scenario.md` (Shopline 手機條碼 order → ezPay invoice → cross-period refund → 折讓)

_Last verified: 2026-04_
