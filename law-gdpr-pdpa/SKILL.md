---
name: "law-gdpr-pdpa"
description: "Analyze data privacy compliance requirements under GDPR, Taiwan's Personal Data Protection Act (PDPA), and related regulations. Use this skill when the user needs to assess data privacy obligations, design compliant data handling processes, evaluate cross-border data transfer risks, or understand data subject rights — even if they say 'do we comply with GDPR', 'can we collect this data', 'what are our privacy obligations', or 'how do we handle user data in Taiwan'."
metadata:
  category: "WP-20 法學院"
  tags: ["law", "gdpr", "pdpa", "data-privacy"]
---

# Data Privacy Compliance (GDPR & Taiwan PDPA)

## Overview

Data privacy law governs how organizations collect, process, store, and share personal data. GDPR (EU) is the global benchmark; Taiwan's PDPA (個人資料保護法) applies domestically. Both share core principles but differ in scope, enforcement, and specific requirements.

## Framework

```
IRON LAW: No Collection Without Legal Basis

You CANNOT collect or process personal data just because you want to.
Every data processing activity requires a legal basis:
- GDPR: 6 legal bases (consent, contract, legal obligation, vital interests, public task, legitimate interests)
- Taiwan PDPA: Specific purposes listed in the act, with consent as primary basis

"We need this data for analytics" is NOT a legal basis.
```

### GDPR vs Taiwan PDPA Comparison

| Aspect | GDPR | Taiwan PDPA |
|--------|------|-------------|
| Scope | Any org processing EU residents' data | Any org processing personal data in Taiwan |
| Legal bases | 6 enumerated bases | Consent-centric + specific purpose limitation |
| Consent standard | Freely given, specific, informed, unambiguous, opt-in | Written consent required for sensitive data; implied consent possible for non-sensitive |
| Data subject rights | Access, rectification, erasure, portability, restriction, objection | Access, correction, deletion, cessation of processing |
| Cross-border transfer | Adequacy decision, SCCs, BCRs | Requires central authority approval or adequate protection |
| Breach notification | 72 hours to authority | Report to authority + notify affected individuals "without delay" |
| Penalties | Up to €20M or 4% global turnover | Up to NT$500K per violation (criminal penalties possible) |
| DPO required? | Yes (in certain cases) | Not explicitly required |

### Compliance Assessment Steps

1. **Data inventory**: What personal data do you collect, process, and store?
2. **Legal basis audit**: What legal basis justifies each processing activity?
3. **Purpose limitation**: Is data used only for the stated purpose?
4. **Data minimization**: Are you collecting only what's necessary?
5. **Storage limitation**: How long is data retained? Is there a deletion policy?
6. **Security measures**: Are appropriate technical and organizational measures in place?
7. **Rights fulfillment**: Can you respond to data subject rights requests?
8. **Cross-border transfers**: Does data leave the jurisdiction? Under what mechanism?
9. **Breach response**: Is there a breach notification procedure?

## Output Format

```markdown
# Privacy Compliance Assessment: {Organization}

## Data Inventory
| Data Category | Types | Legal Basis | Purpose | Retention |
|-------------|-------|-------------|---------|-----------|
| {category} | {specific fields} | {basis} | {why collected} | {period} |

## Compliance Gaps
| Requirement | Status | Gap | Priority |
|------------|--------|-----|----------|
| Legal basis | ✓/✗ | {detail} | H/M/L |
| Consent mechanism | ✓/✗ | ... | ... |
| Data subject rights | ✓/✗ | ... | ... |
| Breach notification | ✓/✗ | ... | ... |
| Cross-border transfer | ✓/✗ | ... | ... |

## Remediation Plan
1. {action} — priority: {H/M/L} — timeline: {X weeks}
```

## Examples

### Correct Application
**Scenario:** Privacy assessment for a Taiwanese e-commerce site selling to EU customers

- **Applies**: Both PDPA (Taiwan customers) AND GDPR (EU customers)
- **Gap found**: Cookie consent banner only says "By using this site you agree to cookies" → Fails GDPR (not freely given, not specific, no opt-out for non-essential cookies). Must implement granular cookie consent with opt-in for marketing cookies ✓
- **Gap found**: Customer data shared with logistics partner in China without cross-border transfer mechanism → Fails both GDPR (no adequacy/SCC) and PDPA (no authority approval)

### Incorrect Application
- "We're a Taiwan company, GDPR doesn't apply to us" → GDPR applies to ANY organization processing EU residents' data, regardless of where the organization is located. If you sell to EU customers or monitor EU users' behavior, GDPR applies.

## Gotchas

- **Consent is not always the best legal basis**: Under GDPR, "legitimate interests" may be more appropriate than consent for some processing (e.g., fraud prevention). Consent can be withdrawn, creating operational complexity.
- **"Anonymous" data may not be anonymous**: If data can be re-identified by combining with other datasets, it's pseudonymous, not anonymous, and still subject to privacy law.
- **Taiwan PDPA covers public and private sector**: Unlike GDPR which primarily targets private sector, PDPA applies to government agencies as well.
- **Privacy by design, not afterthought**: Both GDPR and best practice require considering privacy at the system design stage, not bolting it on later.
- **This is educational guidance, not legal advice**: Privacy compliance requires a qualified data protection specialist familiar with applicable jurisdictions.

## References

- For GDPR Article-by-article reference, see `references/gdpr-articles.md`
- For Taiwan PDPA implementation guide, see `references/taiwan-pdpa.md`
