---
name: "cs-sop"
description: "Design customer service operations including tiered support (L1/L2/L3), response templates, SLA definitions, escalation procedures, and complaint handling. Use this skill when the user needs to set up a CS team, create service standards, design escalation flows, or improve response quality — even if they say 'our CS is a mess', 'how should we handle complaints', 'set up support tiers', or 'create CS SOPs'."
metadata:
  category: "WP-06 Agent通訊+客服"
  tags: ["customer-service", "sop", "support", "operations"]
---

# Customer Service SOP

## Framework

```
IRON LAW: Tier the Support, Not the Customer

Every customer deserves quality service. But not every issue needs a
senior specialist. Route by ISSUE COMPLEXITY, not by customer "importance."

L1 handles 70-80% of volume (simple, repeatable)
L2 handles 15-20% (requires expertise)
L3 handles 5% (requires engineering or management)
```

### Three-Tier Support Model

| Tier | Handles | Skills Required | Resolution Target |
|------|---------|----------------|------------------|
| **L1 (Basic)** | FAQ, order status, password reset, simple returns | Script-following, product basics, empathy | < 5 minutes, first-contact resolution |
| **L2 (Specialist)** | Technical issues, billing disputes, complex returns, product defects | Deep product knowledge, judgment, negotiation | < 24 hours |
| **L3 (Expert)** | System bugs, legal/compliance, executive escalations, crisis | Engineering, legal, or management involvement | < 72 hours, case-by-case |

### Case Categorization

| Category | Examples | Priority | SLA (First Response) |
|----------|---------|----------|---------------------|
| **Critical** | Service outage, security breach, safety issue | P1 | < 15 minutes |
| **High** | Payment failure, account locked, order error | P2 | < 1 hour |
| **Medium** | Product question, feature request, general complaint | P3 | < 4 hours |
| **Low** | Feedback, suggestion, general inquiry | P4 | < 24 hours |

### Complaint Handling: LAST Framework

1. **Listen**: Let the customer express fully without interrupting
2. **Apologize**: Acknowledge their frustration sincerely ("I'm sorry this happened")
3. **Solve**: Offer a concrete solution or next step
4. **Thank**: Thank them for bringing it to your attention

### Escalation Rules

| Trigger | Escalate To | Timeline |
|---------|-----------|---------|
| L1 can't resolve in 15 min | L2 | Immediate warm handoff |
| Customer requests supervisor | L2 or Team Lead | Within 5 minutes |
| Issue involves refund > NT$X | L2 (approval authority) | Same interaction |
| Legal threat or media mention | L3 + Legal + PR | Immediate |
| Repeat contact (3+ on same issue) | L2 + investigation | After 3rd contact |

### Response Template Structure

```
[Greeting] Hi {name}, thank you for contacting us.

[Acknowledge] I understand you're experiencing {issue}.

[Action] Here's what I've done / Here's what we'll do:
1. {specific action}
2. {timeline}

[Next steps] {what the customer should expect / do next}

[Close] Is there anything else I can help you with?
```

## Output Format

```markdown
# Customer Service SOP: {Business}

## Support Tiers
| Tier | Scope | Team Size | Tools |
|------|-------|----------|-------|
| L1 | {scope} | {N people} | {tools} |
| L2 | {scope} | {N} | {tools} |
| L3 | {scope} | {N} | {tools} |

## SLA Targets
| Priority | First Response | Resolution | Escalation |
|----------|--------------|-----------|-----------|
| P1 | {time} | {time} | {to whom} |
| P2 | ... | ... | ... |

## Top 10 Contact Reasons
| # | Reason | Volume % | Resolution | Template? |
|---|--------|---------|-----------|----------|
| 1 | {reason} | {%} | L1/L2 | Y/N |

## Escalation Flowchart
{Decision tree for when to escalate}

## Quality Metrics
| Metric | Target |
|--------|--------|
| First Contact Resolution | > 70% |
| CSAT | > 4.2/5 |
| Avg Response Time | < {X} hours |
| Escalation Rate | < 20% |
```

## Gotchas

- **SLAs must be MEASURABLE**: "Respond quickly" is not an SLA. "First response within 1 hour for P2 tickets" is. If you can't measure it, you can't manage it.
- **Warm handoff > cold transfer**: When escalating, the L1 agent should brief L2 before transferring. Forcing the customer to repeat their story destroys satisfaction.
- **Empower L1 with resolution authority**: If L1 must escalate every refund, 70% of volume goes to L2 unnecessarily. Give L1 authority for refunds under a threshold (e.g., NT$500).
- **Templates are starting points, not scripts**: Robotic copy-paste responses feel worse than no response. Agents should personalize templates to the specific situation.
- **Taiwan CS expectations**: Taiwan customers expect fast LINE response (within minutes during business hours), polite and apologetic tone, and willingness to go the extra mile. The bar for "good service" is high.

## References

- For CSAT/NPS survey design, see the cs-analytics skill
- For chatbot-human handoff design, see the cs-chatbot-design skill
