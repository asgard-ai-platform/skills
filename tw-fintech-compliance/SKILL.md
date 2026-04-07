---
name: "tw-fintech-compliance"
description: "Navigate Taiwan fintech regulations including FSC oversight, electronic payment laws, VASP rules, AML/KYC requirements, and the regulatory sandbox. Use this skill when the user is building a fintech product in Taiwan, needs to understand licensing requirements, assess crypto/VASP compliance, or apply for the regulatory sandbox — even if they say 'do we need a license', 'crypto regulation in Taiwan', 'KYC requirements', or 'fintech sandbox application'."
metadata:
  category: "WP-12 產業知識"
  tags: ["industry", "taiwan", "fintech", "compliance", "regulation"]
---

# Taiwan Fintech Compliance

## Framework

```
IRON LAW: In Fintech, Regulation Comes BEFORE Product

Unlike most tech products where you can launch and iterate, financial
services in Taiwan require LICENSING FIRST. Operating without the proper
license is a criminal offense (not just a fine). Determine your regulatory
category and licensing requirements BEFORE writing code.
```

### FSC Regulatory Framework

**金融監督管理委員會 (FSC)** oversees all financial services in Taiwan:

| Category | Governing Law | License Required | FSC Division |
|----------|-------------|-----------------|-------------|
| **Electronic payment** | 電子支付機構管理條例 | 電子支付機構許可 | Banking Bureau |
| **Third-party payment** | 第三方支付服務業管理辦法 | Registration (lighter) | Banking Bureau |
| **P2P lending** | 金融科技發展與創新實驗條例 (sandbox) or crowd-funding rules | Case-by-case | Securities Bureau |
| **Robo-advisory** | 證券投資信託及顧問法 | Investment advisory license | Securities Bureau |
| **Insurance tech** | 保險法 | Insurance broker/agent license | Insurance Bureau |
| **VASP (crypto)** | 虛擬資產服務提供者管理辦法 (2024) | VASP registration + AML compliance | Securities Bureau |
| **Open banking** | 金融機構間資料共享指引 | API partnership with banks | Banking Bureau |

### Electronic Payment vs Third-Party Payment

| Feature | Electronic Payment (電子支付) | Third-Party Payment (第三方支付) |
|---------|---------------------------|-------------------------------|
| Stored value | Yes (e-wallet) | No (pass-through only) |
| P2P transfer | Yes | No |
| Capital requirement | NT$500M+ | NT$5M |
| License | FSC approval (12-18 months) | Registration (1-3 months) |
| Examples | LINE Pay Money, JKoPay, icash Pay | 綠界 ECPay, 藍新 NewebPay |

### VASP (Crypto) Regulations (2024+)

| Requirement | Detail |
|------------|--------|
| Registration | Must register with FSC as VASP |
| AML/CFT | Full compliance with 洗錢防制法 |
| KYC | Identity verification for all users |
| Custody | Customer asset segregation required |
| Marketing | Restrictions on advertising (no promises of returns) |
| Reporting | Suspicious transaction reports (STR) to 調查局 |

### AML/KYC Requirements (All Financial Services)

| KYC Level | When Required | Data Collected |
|-----------|-------------|---------------|
| **Simplified** | Low-risk, small transactions | Name, ID number, DOB |
| **Standard** | Account opening, most transactions | + Address, occupation, source of funds |
| **Enhanced** | High-risk customers, PEPs, large transactions | + Detailed source of wealth, ongoing monitoring |

**Ongoing obligations:**
- Transaction monitoring (unusual patterns)
- Suspicious Transaction Reports (STR) to 法務部調查局
- Sanctions screening (OFAC, UN, EU lists)
- Record keeping: 5+ years after account closure

### Regulatory Sandbox (金融科技創新實驗)

| Aspect | Detail |
|--------|--------|
| Purpose | Test innovative financial services without full licensing |
| Duration | Up to 18 months (extendable to 36) |
| Application | Submit to FSC with: innovation description, consumer protection plan, risk assessment |
| Approval time | 60 business days |
| Scope limitation | Must define user count, transaction limits, geographic scope |
| Exit plan | Path to full license or orderly shutdown |

### Open Banking (Three Phases)

| Phase | Data Shared | Status |
|-------|-----------|--------|
| Phase 1 | Product information (rates, fees) | Launched 2019 |
| Phase 2 | Customer information (with consent) | Launched 2021 |
| Phase 3 | Transaction initiation (payment, transfer) | In development |

## Output Format

```markdown
# Fintech Compliance Assessment: {Product}

## Product Classification
- Service type: {payment / lending / advisory / crypto / insurance}
- Regulatory category: {electronic payment / third-party / VASP / etc.}
- License required: {specific license name}

## Licensing Pathway
| Step | Action | Timeline | Cost |
|------|--------|----------|------|
| 1 | {step} | {months} | NT${X} |

## AML/KYC Requirements
- KYC level: {simplified / standard / enhanced}
- Transaction monitoring: {required / not required}
- STR reporting: {required / not required}

## Key Risks
| Risk | Impact | Mitigation |
|------|--------|-----------|
| {regulatory risk} | H/M/L | {action} |

## Recommendation
- Proceed with licensing / Use sandbox / Restructure product to avoid licensing
```

## Gotchas

- **Third-party vs electronic payment**: The distinction is stored value. If your app holds customer money (e-wallet), you need the much heavier electronic payment license (NT$500M capital). If you just process payments (pass money from buyer to seller), third-party registration is sufficient.
- **Sandbox is not a shortcut**: The sandbox exempts you from licensing temporarily, but you must still comply with AML, consumer protection, and data privacy. And you still need to get a full license to commercialize.
- **VASP regulation is new and evolving**: The 2024 VASP rules are Taiwan's first comprehensive crypto regulation. Expect amendments and additional guidance. Build compliance infrastructure that's adaptable.
- **Foreign fintech entering Taiwan**: Foreign companies must establish a Taiwan entity and obtain Taiwan-specific licenses. A license in another jurisdiction does not transfer.
- **This is educational guidance, not legal/regulatory advice**: Fintech regulation is complex and penalties for non-compliance include criminal charges. Engage a regulatory affairs lawyer specializing in Taiwan financial services.

## References

- For FSC licensing application guides, see `references/fsc-licensing.md`
- For AML/KYC implementation checklist, see `references/aml-kyc-checklist.md`
