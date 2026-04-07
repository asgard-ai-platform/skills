---
name: "law-contract"
description: "Analyze contract fundamentals including formation requirements (offer, acceptance, consideration), essential clauses, and common risk areas. Use this skill when the user needs to review a contract, understand contract terms, identify risky clauses, or draft contract provisions — even if they say 'review this agreement', 'what should I watch out for in this contract', or 'is this clause standard'."
metadata:
  category: "WP-20 法學院"
  tags: ["law", "contract", "legal-analysis"]
---

# Contract Analysis

## Overview

Contract law governs enforceable agreements. This skill covers formation requirements, essential clauses, and common risk areas for business contracts. It is educational guidance, not legal advice — always consult a qualified attorney for specific situations.

## Framework

```
IRON LAW: A Contract Requires Offer + Acceptance + Consideration + Legality

All four elements must be present for a valid contract. Missing any one
means no enforceable contract exists — regardless of how formal the document
looks. A signed document without consideration (exchange of value) is
not a contract.
```

### Contract Formation

| Element | Definition | Test |
|---------|-----------|------|
| **Offer** | Clear, definite proposal with intent to be bound | Would a reasonable person understand this as a binding proposal? |
| **Acceptance** | Unqualified agreement to the offer's terms | Mirror image rule: acceptance must match the offer exactly |
| **Consideration** | Something of value exchanged by both parties | Each side gives up something (money, services, rights, promises) |
| **Legality** | Subject matter must be legal and parties must have capacity | No illegal purpose; parties must be competent adults or authorized entities |

### Essential Contract Clauses

| Clause | Purpose | Red Flags |
|--------|---------|-----------|
| **Parties** | Who is bound | Incorrect entity name, no authority to sign |
| **Scope/Subject** | What is being exchanged | Vague deliverables, undefined terms |
| **Payment terms** | When and how payment occurs | No payment schedule, no late payment consequences |
| **Term & Termination** | Duration and exit conditions | Auto-renewal without notice, no termination for cause |
| **Liability & Indemnity** | Who bears risk | Unlimited liability, one-sided indemnification |
| **Confidentiality (NDA)** | Information protection | Overly broad definition, no time limit |
| **IP ownership** | Who owns created work | Ambiguous ownership of work product |
| **Non-compete** | Restrictions after termination | Overly broad scope/geography/duration |
| **Dispute resolution** | How conflicts are resolved | Foreign jurisdiction, mandatory arbitration without consent |
| **Force majeure** | Excused performance for unforeseeable events | Too narrow or too broad definition |

### Contract Review Steps

1. **Identify the parties**: Who is agreeing? Are entity names correct?
2. **Understand the deal**: What is each side giving and receiving?
3. **Check formation elements**: Offer, acceptance, consideration, legality — all present?
4. **Review essential clauses**: Use the table above as a checklist
5. **Flag risk areas**: Unlimited liability, one-sided terms, vague scope, auto-renewal
6. **Check governing law**: Which jurisdiction's law applies? Is the dispute resolution mechanism acceptable?

## Output Format

```markdown
# Contract Review: {Agreement Type}

## Parties
- Party A: {name, role}
- Party B: {name, role}

## Deal Summary
{What is being exchanged — in plain language}

## Clause Review
| Clause | Present? | Assessment | Risk Level |
|--------|---------|-----------|-----------|
| Scope | Y/N | {notes} | 🟢/🟡/🔴 |
| Payment | Y/N | ... | ... |
| Termination | Y/N | ... | ... |
| Liability | Y/N | ... | ... |
| IP | Y/N | ... | ... |
| Non-compete | Y/N | ... | ... |

## Red Flags
1. {specific concern with clause reference}

## Recommendations
1. {suggested modification}
```

## Examples

### Correct Application
**Scenario:** SaaS service agreement review
- **Red flag**: "Vendor may modify pricing with 30 days' notice" → One-sided price change clause. Should be: pricing locked for contract term, changes only at renewal.
- **Red flag**: "Client indemnifies Vendor against all claims" → One-sided indemnification. Should be mutual.
- **Missing**: No SLA (service level agreement) defined → No recourse if service goes down. Recommend adding uptime commitment with credits ✓

### Incorrect Application
- "This contract looks fine because both parties signed it" → Signature doesn't make every clause fair or enforceable. Must review individual clause terms. A signed contract with an unconscionable clause may still be challenged.

## Gotchas

- **"Standard contract" doesn't mean fair**: Vendor-drafted "standard" contracts are drafted in the vendor's favor. Everything is negotiable.
- **Taiwan-specific**: Taiwan's Civil Code governs contracts. Key differences from common law: no consideration requirement (promise for promise is sufficient), mandatory provisions in certain contract types (labor, consumer).
- **Auto-renewal traps**: Many contracts auto-renew unless notice is given 30-90 days before expiry. Calendar the notice deadline.
- **This skill is NOT legal advice**: It provides educational analysis of contract concepts. Always consult a licensed attorney for binding legal decisions.

## References

- For Taiwan-specific contract law (Civil Code), see `references/taiwan-contract-law.md`
- For common contract templates, see `references/contract-templates.md`
