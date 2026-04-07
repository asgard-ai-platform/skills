---
name: "tw-einvoice-guide"
description: "Implement Taiwan's e-invoice (電子發票) system including platform integration, B2B vs B2C formats, carrier consolidation, and tax filing reconciliation. Use this skill when the user needs to set up e-invoicing for a Taiwan business, integrate with the MOF platform, understand carrier codes, or troubleshoot invoice issues — even if they say 'set up e-invoice', 'how does 電子發票 work', 'integrate with 財政部', or 'carrier barcode scanning'."
metadata:
  category: "WP-05 台灣創業"
  tags: ["taiwan", "e-invoice", "tax-compliance", "integration"]
---

# Taiwan E-Invoice System (電子發票)

## Framework

```
IRON LAW: E-Invoice Is Mandatory for Most B2C Businesses

Since 2019, businesses using 統一發票 must issue electronic invoices
through the 財政部電子發票整合服務平台. Paper invoices are being phased
out. Non-compliance triggers penalties and may affect 營業稅 filing.
```

### System Architecture

```
Your System (POS/ERP/E-commerce)
    ↓ API / Turnkey
財政部電子發票整合服務平台 (einvoice.nat.gov.tw)
    ↓
Consumer (via 載具: 手機條碼 / 自然人憑證 / App)
    ↓
國稅局 (tax reconciliation)
```

### Integration Methods

| Method | How It Works | Best For | Complexity |
|--------|-------------|----------|-----------|
| **Turnkey** | Install MOF-provided software, batch upload invoices | Traditional businesses, low volume | Medium |
| **API (加值服務中心)** | Connect via 加值中心 API (e.g., 綠界、藍新) | E-commerce, SaaS, high volume | Low-Medium |
| **Direct API** | Connect directly to MOF platform | Large enterprises with IT team | High |
| **POS integration** | POS vendor handles e-invoice natively | Retail, F&B | Low (vendor does it) |

### B2B vs B2C Invoice Differences

| Aspect | B2B (營業人對營業人) | B2C (營業人對消費者) |
|--------|-------------------|-------------------|
| Buyer info | Buyer's 統編 required | No 統編 (consumer) |
| Format | 三聯式 | 二聯式 |
| Tax display | Tax amount shown separately | Tax included in price |
| Carrier | N/A | 手機條碼, 自然人憑證, or membership carrier |
| Prize eligibility | No | Yes (中獎機制) |

### Carrier Types (載具)

| Carrier | Code Format | Use Case |
|---------|-----------|----------|
| 手機條碼 | /XXXXXXX (slash + 7 chars) | Most common consumer carrier |
| 自然人憑證 | 2 letters + 14 digits | Government ID-linked |
| 會員載具 (membership) | Defined by business | Loyalty program integration |
| 捐贈碼 | 3-7 digits | Donate invoice to charity |

### Implementation Steps

**Phase 1: Registration**
1. Register on 財政部電子發票整合服務平台
2. Apply for 加值服務中心 AppID (if using API method)
3. Set up certificate and authentication

**Phase 2: Development/Integration**
4. Choose integration method (Turnkey vs API vs POS)
5. Implement invoice issuance: create, void, void-and-reissue
6. Implement carrier scanning (手機條碼 barcode)
7. Handle 捐贈碼 (donation codes)

**Phase 3: Testing**
8. Test in sandbox environment
9. Issue test invoices, verify on MOF platform
10. Test void/reissue flows

**Phase 4: Go-Live**
11. Switch to production environment
12. Monitor daily: match issued invoices vs MOF records
13. Bimonthly: reconcile with 營業稅 filing (401 form)

### Common API Flows

**Issue Invoice:**
```
POST /invoice → { seller_id, buyer_id (optional), items[], amount, tax, carrier_type, carrier_id }
→ Response: { invoice_number, invoice_date, random_code }
```

**Void Invoice:**
```
POST /invoice/void → { invoice_number, invoice_date, void_reason }
```

**Query Invoice:**
```
GET /invoice/{number} → { status, items, amount, carrier }
```

## Output Format

```markdown
# E-Invoice Implementation Plan: {Business}

## Current State
- Business type: B2B / B2C / Both
- Current invoicing: Paper / Partial e-invoice / None
- Transaction volume: {N}/month

## Integration Method
- Method: {Turnkey / API / POS integration}
- Provider: {加值中心 name, if applicable}
- Rationale: {why this method}

## Implementation Checklist
- [ ] MOF platform registration
- [ ] AppID obtained
- [ ] Integration developed
- [ ] Sandbox testing passed
- [ ] Carrier scanning implemented
- [ ] Donation code support
- [ ] Production go-live
- [ ] Reconciliation process documented

## Timeline
| Phase | Duration | Milestone |
|-------|----------|-----------|
| Registration | 1-2 weeks | AppID obtained |
| Development | 2-4 weeks | Integration complete |
| Testing | 1-2 weeks | Sandbox verified |
| Go-live | 1 day | First production invoice |
```

## Gotchas

- **Invoice number format is assigned by MOF**: You don't generate invoice numbers. The MOF assigns number ranges (字軌) that you request in advance. Run out of numbers = can't issue invoices. Request well ahead of time.
- **Void window is limited**: Invoices can be voided within the same bimonthly period. After the period closes, voiding requires a more complex process (折讓).
- **手機條碼 scanning**: The barcode is a slash + 7 characters. Many POS scanners need configuration to read this format correctly. Test with real 手機條碼 barcodes.
- **Prize drawing (中獎)**: B2C e-invoices are automatically entered into the government lottery (統一發票兌獎). Your system must support winner notification if the invoice was stored in a membership carrier.
- **Reconciliation is critical**: The MOF platform is the source of truth. If your system's invoice records don't match the platform, your 營業稅 filing will have discrepancies. Reconcile daily.

## References

- For 加值服務中心 API documentation, see `references/einvoice-api.md`
- For 營業稅 filing reconciliation, see the tw-tax-basics skill
