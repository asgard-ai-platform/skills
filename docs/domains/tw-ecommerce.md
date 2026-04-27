# Taiwan E-Commerce Domain Map

**Last updated:** 2026-04-19
**Re-verification cadence:** Quarterly (next: 2026-07)

Taiwan e-commerce brings together platform integration, payment gateways, logistics carriers, e-invoice compliance, consumer-protection law, operational playbooks, and analytics conventions that are distinct from generic e-commerce. This map indexes every skill that applies, whether it's new (`tw-ecom-*`), existing Taiwan-specific (`tw-*`), or existing generic e-commerce (`ecom-*`).

## Who this domain is for

- Founders running a Taiwan D2C brand (Shopline / 91APP / Shopify)
- Marketplace sellers (Shopee / momo / PChome)
- Agencies / SI building stores for TW clients
- Asgard plugin builders assembling a TW e-commerce bundle

## Decision tree — where to start

```
I need to...

├── Choose a platform / channel mix
│   └── tw-ecom-channel-strategy
│
├── Integrate with a specific platform
│   ├── Shopline → tw-ecom-dtc-shopline  ★ reference
│   ├── 91APP → tw-ecom-dtc-91app
│   ├── Shopify TW → tw-ecom-dtc-shopify-localization
│   ├── Shopee → tw-ecom-marketplace-shopee
│   └── momo → tw-ecom-marketplace-momo
│
├── Pick a payment gateway
│   ├── Landscape / selection → tw-payment-integration  (existing)
│   ├── NewebPay deep → tw-ecom-payment-newebpay  ★ reference
│   ├── ECPay deep → tw-ecom-payment-ecpay
│   ├── TapPay deep → tw-ecom-payment-tappay
│   ├── 街口 → tw-ecom-payment-jkopay
│   └── Chargeback / 折讓 → tw-ecom-payment-dispute
│
├── Ship products
│   ├── CVS 超取 → tw-ecom-logistics-cvs
│   ├── 宅配 → tw-ecom-logistics-home
│   ├── Cold-chain → tw-ecom-logistics-cold-chain
│   └── Cross-border → tw-ecom-logistics-cross-border
│
├── Issue e-invoices
│   ├── Landscape → tw-einvoice-guide  (existing)
│   ├── ezPay → tw-ecom-invoice-ezpay  ★ reference
│   ├── UniversalEC → tw-ecom-invoice-universalec
│   ├── Carriers (載具) → tw-ecom-invoice-carrier
│   └── Void / 折讓 → tw-ecom-invoice-void
│
├── Stay compliant
│   ├── 消保法 鑑賞期 → tw-ecom-compliance-consumer
│   ├── 食藥妝 / 酒 → tw-ecom-compliance-product
│   ├── PDPA → tw-ecom-compliance-pdpa
│   ├── Cross-border tax → tw-ecom-compliance-cross-border
│   ├── Startup legal basics → tw-startup-legal  (existing)
│   └── Tax filing → tw-tax-basics  (existing)
│
├── Run operations
│   ├── 檔期 / 雙11 → tw-ecom-operations-promotion
│   ├── Pricing → tw-ecom-operations-pricing
│   ├── LINE OA CRM → tw-ecom-operations-line-oa
│   ├── Customer service → tw-ecom-operations-customer-service
│   ├── Generic RFM → ecom-rfm-analysis  (existing)
│   ├── Promo ROI → ecom-promo-roi  (existing)
│   └── Inventory health → ecom-inventory-health  (existing)
│
└── Measure
    ├── GA4 setup → tw-ecom-analytics-ga4
    ├── TW benchmarks → tw-ecom-analytics-benchmarks
    ├── Generic ecom analytics → ecom-analytics  (existing)
    └── Cohort analysis → data-cohort-analysis  (existing)
```

## Related MCPs

| MCP | Tools | Covered by |
|---|---:|---|
| `mcp-shopline` | 143 | `tw-ecom-dtc-shopline` |
| `mcp-91app` | 17 | `tw-ecom-dtc-91app` (skeleton) |
| `mcp-newebpay` | 8 | `tw-ecom-payment-newebpay` |
| `mcp-ezpay-einvoice` | 7 | `tw-ecom-invoice-ezpay` |
| `mcp-universalec-e-invoice` | 27 | `tw-ecom-invoice-universalec` (skeleton) |
| `mcp-ecpay` | — | `tw-ecom-payment-ecpay` (skeleton) |
| `mcp-ecpay-logistics` | — | `tw-ecom-logistics-cvs` (skeleton) |

(★ = content-complete reference skill. Everything else is either content-complete already or a skeleton pending content. See `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md` for scope.)

## Skill status legend

- **Complete** (no marker): full content, merge-ready
- **Skeleton**: frontmatter + "when to use" only; body pending a follow-up branch. `status: skeleton` in frontmatter.

## Re-verification

The domain touches fast-moving regulation (鑑賞期 exemption list, 境外電商 VAT), vendor fees (NewebPay / ezPay / TapPay rate cards), and platform mechanics (Shopee tier rules). Quarterly cadence:

- Scan each skill's `last_verified` metadata
- If > 6 months stale, open an issue
- Touch fee / rate / regulation numbers: cite source + date in the skill

## See also

- `TODO.md` — skeleton backlog with priority order
- `CONTRIBUTING.md` — how to fill in a skeleton or add a new skill
- `docs/superpowers/specs/2026-04-19-tw-ecommerce-domain-design.md` — design rationale
