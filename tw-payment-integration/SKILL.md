---
name: "tw-payment-integration"
description: "Integrate Taiwan payment service providers including credit card, ATM transfer, convenience store payment, and mobile wallets (LINE Pay, JKoPay). Use this skill when the user needs to accept payments online in Taiwan, choose a payment gateway, understand payment flows, or handle refunds — even if they say 'accept payments on our site', 'which payment provider in Taiwan', 'integrate credit card payments', or 'set up LINE Pay'."
metadata:
  category: "WP-05 台灣創業"
  tags: ["taiwan", "payment", "fintech", "integration"]
---

# Taiwan Payment Integration

## Framework

```
IRON LAW: Support At Least 3 Payment Methods in Taiwan

Taiwan consumers expect choice. Credit card alone misses ~40% of potential
buyers. The minimum viable payment mix for Taiwan e-commerce:
1. Credit card (信用卡)
2. ATM/bank transfer (ATM 虛擬帳號)
3. Convenience store payment (超商代碼/超商取貨付款)

Adding LINE Pay and Apple Pay captures another 10-15%.
```

### Taiwan Payment Landscape

| Method | Market Share | User Profile | Settlement Time |
|--------|------------|-------------|----------------|
| Credit/Debit card | ~45% | All ages, higher spending | T+1 to T+7 |
| ATM virtual account | ~15% | Price-sensitive, no credit card | Instant to T+1 |
| Convenience store (超商代碼) | ~10% | Students, cash-preferred | T+1 to T+3 |
| LINE Pay | ~12% | LINE users (95% of Taiwan) | T+1 to T+7 |
| Apple Pay / Google Pay | ~5% | Mobile-first users | T+1 to T+7 |
| 超商取貨付款 (COD at store) | ~8% | Low trust, want to see product | Upon pickup + T+3 |
| JKoPay / 街口 | ~3% | Younger demographic | T+1 |

### Payment Service Providers (PSP)

| PSP | Strengths | Pricing | Best For |
|-----|----------|---------|----------|
| **綠界 (ECPay)** | Most comprehensive (credit card, ATM, CVS, 超取), largest market share | 2.75% credit card, NT$15/ATM txn | General e-commerce, startups |
| **藍新 (NewebPay)** | Good API design, modern dashboard | 2.5-2.8% credit card | SaaS, subscription businesses |
| **TapPay** | Mobile-first, Apple Pay/Google Pay/LINE Pay integration | 2.5-2.8% credit card | Mobile apps, in-app purchases |
| **PayNow** | Easy setup, no monthly fee | 2.75% credit card | Low-volume, new businesses |
| **Stripe** | International, excellent API | 3.4% + NT$10 per txn | Cross-border, international focus |

### Integration Flow (Standard)

```
1. Customer clicks "Pay" on your site
2. Your server creates an order → sends to PSP API
3. PSP returns a payment page URL (or token for inline)
4. Customer completes payment on PSP-hosted page
5. PSP sends callback (webhook) to your server with result
6. Your server verifies the callback signature
7. Update order status → show confirmation to customer
```

### Key API Concepts

| Concept | What It Is |
|---------|-----------|
| **MerchantID** | Your account identifier with the PSP |
| **HashKey / HashIV** | Secret keys for signature verification |
| **TradeNo** | Your order ID (must be unique per transaction) |
| **PaymentType** | Credit, ATM, CVS, WebATM, etc. |
| **Callback URL** | Webhook endpoint PSP calls after payment |
| **Return URL** | Page to redirect customer after payment |
| **CheckMacValue** | HMAC signature to verify data integrity |

### Refund Handling

| Method | Refund Capability | Timing |
|--------|------------------|--------|
| Credit card | Full or partial refund via API | 1-7 business days |
| ATM | Cannot auto-refund — must wire transfer back | Manual, 3-7 days |
| CVS payment | Cannot auto-refund — must wire transfer back | Manual, 3-7 days |
| LINE Pay | Full refund via API | 1-3 business days |

### Security Requirements

| Requirement | What to Do |
|-------------|-----------|
| **SSL/TLS** | All payment pages must be HTTPS |
| **3D Secure** | Enable 3DS 2.0 for credit card fraud reduction |
| **PCI DSS** | If handling raw card data, need PCI compliance. Using PSP-hosted payment page avoids this. |
| **Tokenization** | Store payment tokens, never raw card numbers |
| **Webhook verification** | Always verify CheckMacValue signature before processing callbacks |
| **Idempotency** | Handle duplicate callbacks gracefully (PSP may retry) |

## Output Format

```markdown
# Payment Integration Plan: {Business}

## Payment Method Selection
| Method | Include? | PSP | Rationale |
|--------|---------|-----|-----------|
| Credit card | Y/N | {provider} | {why} |
| ATM | Y/N | ... | ... |
| CVS | Y/N | ... | ... |
| LINE Pay | Y/N | ... | ... |

## PSP Selection
- Provider: {name}
- Pricing: {rate}
- Rationale: {why this provider}

## Integration Plan
| Phase | Task | Timeline |
|-------|------|----------|
| 1 | Apply for PSP merchant account | 1-2 weeks |
| 2 | Develop payment flow (sandbox) | 1-2 weeks |
| 3 | Implement webhook handler | 1 week |
| 4 | Security review (SSL, signature verification) | 2-3 days |
| 5 | Production testing with real transactions | 1 week |
| 6 | Go-live | 1 day |

## Refund Process
{How each payment method handles refunds}
```

## Gotchas

- **PSP application takes time**: Merchant account approval can take 1-3 weeks. Apply early. Credit card processing requires additional documentation (company registration, bank account proof).
- **ATM and CVS refunds are manual**: Unlike credit cards, ATM and convenience store payments cannot be auto-refunded. You need the customer's bank account to wire money back. Build this into your CS process.
- **Webhook reliability**: PSP callbacks can be delayed or duplicated. Build idempotent handlers and implement a reconciliation job that checks PSP records against your database daily.
- **Foreign credit cards**: Not all Taiwan PSPs support foreign credit cards well. If you have international customers, test with non-Taiwan cards or use Stripe.
- **Recurring payments (subscription)**: 綠界 and 藍新 support recurring billing, but you need the customer's explicit consent and must handle card expiration/update flows.

## References

- For 綠界 API integration guide, see `references/ecpay-api.md`
- For PCI DSS compliance checklist, see `references/pci-checklist.md`
