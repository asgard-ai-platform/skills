---
name: "grad-born-global"
description: "Apply the Born Global framework to analyze firms that internationalize rapidly from inception under resource constraints. Use this skill when the user needs to evaluate whether a startup or SME can pursue early internationalization, identify the capabilities enabling born globals, or design a resource-constrained international market entry strategy."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["born-global", "international-new-ventures", "rapid-internationalization", "knowledge-intensive", "niche-markets", "INV"]
---

# Born Global: Resource-Constrained Rapid Internationalization

## Overview

Born globals are firms that internationalize at or near founding, achieving significant foreign sales (typically 25%+ of revenue) within 3 years of inception. They challenge the Uppsala model's assumption of gradual, stage-based internationalization. Born globals succeed not through scale or accumulated experience, but through knowledge intensity, network relationships, and focus on global niche markets. They are most common in knowledge-intensive, technology-driven industries.

## When to Use

**Trigger conditions:**
- User is evaluating whether a startup should target international markets from day one
- User asks how small firms internationalize without the resources of MNCs
- User needs to assess whether a firm fits the born global profile
- User mentions "born global", "international new venture", "early internationalization", or "global startup"

**When NOT to use:**
- For established firms expanding gradually -> use grad-uppsala
- For FDI mode choice for large multinationals -> use grad-oli
- For industry-level competitive advantage -> use grad-diamond

## Assumptions

```
IRON LAW: Born Globals Succeed Through Knowledge Intensity
          and Network Relationships, NOT Scale

A born global cannot out-resource an MNC. Its advantages are:
1. Unique knowledge or technology (hard to imitate)
2. Network relationships that provide market access and legitimacy
3. Niche focus that large firms find unattractive

If the firm lacks ALL THREE, early internationalization is premature
and will likely fail. Scale-dependent businesses cannot be born global.
```

- The founder's international experience and network are critical enablers
- Niche markets are too small for MNCs to pursue aggressively
- Digital infrastructure lowers the cost of international coordination
- Born globals are resource-constrained and must be highly selective in market choice

## Methodology

### Step 1: Assess Born Global Eligibility

Evaluate whether the firm meets born global preconditions:

| Factor | Required for Born Global | Assessment |
|--------|-------------------------|------------|
| Knowledge intensity | High — proprietary technology, IP, or expertise | Yes / No |
| Founder international experience | Prior work/study abroad, multilingual, global network | Yes / No |
| Niche market orientation | Product serves a global niche too small for MNCs | Yes / No |
| Digital/scalable delivery | Product can be delivered internationally at low marginal cost | Yes / No |
| Home market limitation | Domestic market too small to sustain the business | Yes / No |

If fewer than 3 factors are present, the gradual Uppsala path may be more appropriate.

### Step 2: Identify Key Networks and Relationships

Born globals rely on networks to overcome resource constraints: personal (founder contacts), industry (trade associations), institutional (government programs, accelerators), and customer (referral chains). Map which relationships provide market access, credibility, or knowledge.

### Step 3: Select Target Markets

Born globals cannot enter all markets. Prioritize based on:
- **Lead market**: Where the most demanding, innovative customers are (not necessarily the largest market)
- **Network accessibility**: Markets where existing relationships provide entry
- **Niche density**: Markets with the highest concentration of target customers
- **Institutional support**: Markets where trade agreements or incentives reduce barriers

### Step 4: Design Resource-Light Entry Mode

Born globals typically use low-commitment, high-reach modes:
- Direct online sales (digital products)
- Strategic partnerships and distribution agreements
- Licensing in markets where local presence is needed
- Piggybacking on larger firms' distribution channels
- Avoid wholly-owned subsidiaries in early stages (too resource-intensive)

## Output Format

```markdown
# Born Global Assessment: {Firm}

## Eligibility Check
| Factor | Present? | Evidence |
|--------|----------|----------|
| Knowledge intensity / Founder intl exp / Niche / Digital delivery / Home market limit | Yes/No | {details} |

## Verdict: Born Global Viable / Not Viable

## Network Map
- {Network type}: {key relationships and what they provide}

## Target Markets (prioritized)
1. {Market}: {rationale} | Entry mode: {mode} | Timeline: {milestones}
```

## Gotchas

- **Born global does not mean born everywhere**: Even born globals must be selective. Targeting too many markets simultaneously with limited resources leads to failure. Prioritize ruthlessly.
- **Knowledge intensity decays**: If the technology can be easily imitated, the born global window closes quickly. Speed of internationalization must match speed of imitation.
- **Founder dependency is a risk**: If internationalization depends entirely on the founder's personal network, the firm is fragile. Institutionalize relationships early.
- **Not all tech startups are born globals**: A SaaS product with strong local network effects (e.g., a local marketplace) may need to dominate domestically first.
- **Born global and Uppsala are not mutually exclusive**: A firm may be born global initially (rapid entry into select markets) and then follow Uppsala dynamics for deeper commitment.

## References

- For born global empirical criteria and thresholds, see `references/born-global-criteria.md`
- For comparison with International New Ventures (Oviatt & McDougall, 1994), see `references/inv-framework.md`
