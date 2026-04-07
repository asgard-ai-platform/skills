---
name: "tw-startup-legal"
description: "Guide Taiwan company registration and legal setup including business entity selection, commercial registration, company registration, and tax ID application. Use this skill when the user is starting a business in Taiwan, choosing between sole proprietorship and company, or navigating the registration process — even if they say 'how do I set up a company in Taiwan', 'what's the registration process', 'sole proprietorship vs company', or 'I want to start a business'."
metadata:
  category: "WP-05 台灣創業"
  tags: ["taiwan", "startup", "legal", "company-registration"]
---

# Taiwan Company Registration & Legal Setup

## Framework

```
IRON LAW: Entity Type Determines Everything Downstream

The choice between 行號 (sole proprietorship), 有限公司, and 股份有限公司
determines: liability exposure, tax treatment, fundraising ability, and
exit options. This decision is hard to reverse — choose based on your
3-5 year plan, not just today's simplicity.
```

### Entity Type Comparison

| Feature | 行號 (Sole Prop) | 有限公司 (LLC) | 股份有限公司 (Corp) |
|---------|----------------|--------------|------------------|
| Liability | Unlimited personal | Limited to capital | Limited to capital |
| Min. capital | None (but need proof) | No minimum (since 2018) | No minimum (since 2018) |
| Shareholders | 1 person | 1+ (max no limit) | 2+ (or 1 for gov't/corp shareholder) |
| Fundraising | Cannot issue shares | Limited (no public offering) | Can issue shares, convertible notes, ESOP |
| Tax | Personal income tax | Corporate tax 20% | Corporate tax 20% |
| Best for | Freelancers, side projects | Small teams, lifestyle businesses | Growth startups, seeking investment |

### Registration Process (股份有限公司)

**Phase 1: Pre-Registration (1-2 weeks)**
1. Choose company name → search on 經濟部公司名稱預查系統 (must be unique)
2. Prepare Articles of Incorporation (公司章程)
3. Open a bank escrow account (籌備處帳戶) and deposit capital
4. Obtain capital verification from CPA (會計師資本額查核)

**Phase 2: Company Registration (1-2 weeks)**
5. Submit to 經濟部 (MOEA) for company registration → get 統一編號 (Tax ID)
6. Register with local 商業處 for business registration
7. Register with 國稅局 for tax filing obligations
8. Register with 勞保局 for labor insurance (if hiring)

**Phase 3: Post-Registration (ongoing)**
9. Open company bank account (with 統編)
10. Set up accounting system (帳冊)
11. Register for e-invoice if B2C (see tw-einvoice-guide)
12. Apply for relevant permits (food, medical, financial services have additional requirements)

### Key Documents Needed

| Document | Purpose | Where to Get |
|----------|---------|-------------|
| 公司章程 (Articles) | Defines company structure, rules | Draft with lawyer or use template |
| 股東同意書 | Shareholder consent for formation | Signed by all shareholders |
| 董事願任同意書 | Director acceptance | Signed by directors |
| 會計師資本額查核報告 | Capital verification | CPA firm |
| 公司設立登記表 | Registration application | 經濟部 website |

### Common Startup Legal Tasks

| Task | When | Estimated Cost |
|------|------|---------------|
| Company registration | Day 1 | NT$5K-15K (DIY) or NT$15K-30K (via accountant) |
| Trademark registration (TIPO) | Within first 3 months | NT$3K filing fee + NT$10K-20K if using agent |
| Employment contract template | Before first hire | NT$5K-15K (lawyer draft) |
| Privacy policy (PDPA compliance) | Before collecting user data | NT$5K-10K (lawyer draft) |
| Shareholder agreement | Before accepting investment | NT$20K-50K (lawyer draft) |

## Output Format

```markdown
# Taiwan Startup Legal Checklist: {Company Name}

## Entity Selection
- Recommended type: {行號 / 有限公司 / 股份有限公司}
- Rationale: {why this fits the user's situation}

## Registration Checklist
- [ ] Company name pre-check (經濟部)
- [ ] Articles of Incorporation drafted
- [ ] Capital deposited + CPA verification
- [ ] Company registration (統編 obtained)
- [ ] Tax registration (國稅局)
- [ ] Labor insurance registration (if hiring)
- [ ] Business bank account opened

## Estimated Timeline & Cost
| Step | Timeline | Cost |
|------|----------|------|
| {step} | {days/weeks} | NT${X} |

## Next Steps
1. {immediate action}
```

## Gotchas

- **統一編號 is your identity**: The 8-digit 統編 is used for everything — tax filing, invoicing, contracts, bank accounts. Get it first, then set up everything else.
- **Capital verification is a one-time check**: CPA verifies capital at registration. After that, the money can be used for business operations. You don't need to keep it sitting in the bank.
- **Foreign founders**: Non-ROC nationals can register companies but need an ARC (居留證) or APRC, and there are additional MOEA investment approval requirements.
- **Address matters**: The registered address determines which tax office you deal with. Using a virtual office is legal but may trigger more scrutiny.
- **This is educational guidance, not legal advice**: Taiwan company law is complex. Consult a licensed accountant (會計師) or lawyer (律師) for specific situations.

## References

- For tax obligations after registration, see the tw-tax-basics skill
- For e-invoice setup, see the tw-einvoice-guide skill
