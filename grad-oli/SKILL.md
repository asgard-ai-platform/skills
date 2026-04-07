---
name: "grad-oli"
description: "Apply Dunning's OLI Paradigm (Eclectic Theory) to evaluate foreign direct investment decisions based on Ownership, Location, and Internalization advantages. Use this skill when the user needs to decide whether to invest abroad, choose between FDI modes (wholly-owned subsidiary, joint venture, licensing), or explain why a firm internationalizes through FDI rather than export or licensing."
metadata:
  category: "WP-24 創新與國際化"
  tags: ["OLI-paradigm", "dunning", "eclectic-theory", "FDI", "ownership-advantage", "location-advantage", "internalization-advantage"]
---

# OLI Paradigm (Dunning, 1977): Eclectic Theory of FDI

## Overview

The OLI Paradigm explains why firms engage in foreign direct investment (FDI) rather than exporting or licensing. Three conditions must hold simultaneously: the firm possesses Ownership advantages (proprietary assets), the foreign Location offers advantages over the home market, and Internalization is preferable to market-based transactions (licensing/franchising). The configuration of OLI advantages also determines the FDI mode.

## When to Use

**Trigger conditions:**
- User is deciding whether to invest in a foreign market via FDI
- User asks why a firm should own foreign operations rather than export or license
- User needs to choose between wholly-owned subsidiary, joint venture, or licensing
- User mentions "FDI decision", "OLI", "internationalization mode", or "eclectic theory"

**When NOT to use:**
- For gradual internationalization process -> use grad-uppsala
- For early-stage rapid internationalization -> use grad-born-global
- For national competitive advantage analysis -> use grad-diamond

## Assumptions

```
IRON LAW: ALL Three OLI Advantages Must Be Present to Justify FDI

- Ownership (O) alone -> License or export (no need to be there)
- Ownership + Location (O+L) -> Export (no need to internalize)
- Ownership + Internalization (O+I) -> Domestic production (no location pull)

Only when O + L + I are ALL present does FDI make economic sense.
If ANY one is missing, a different entry mode is optimal.
```

- Firms are rational actors seeking to minimize transaction costs
- Market imperfections (information asymmetry, opportunism) drive internalization
- OLI advantages are firm-specific, industry-specific, and country-specific

## Methodology

### Step 1: Assess Ownership Advantages (O)

Identify firm-specific advantages foreign competitors lack: asset-based (Oa: patents, technology, brand) and transaction-based (Ot: managerial capabilities, scale economies). If no clear O advantage exists, STOP -- the firm has no basis for FDI.

### Step 2: Assess Location Advantages (L)

Evaluate why the foreign location is superior to serving from home:
- **Market-seeking**: Large market size, growing demand, trade barriers making export unviable
- **Resource-seeking**: Low-cost labor, raw materials, specialized talent
- **Efficiency-seeking**: Scale economies, favorable tax regimes, supply chain optimization
- **Strategic asset-seeking**: Access to technology clusters, R&D ecosystems, knowledge networks

If no clear L advantage exists -> Export from home is sufficient.

### Step 3: Assess Internalization Advantages (I)

Evaluate why internal governance is preferable to licensing or franchising:
- **High transaction costs**: Tacit knowledge that is hard to codify and transfer
- **Quality control**: Brand reputation requires tight operational control
- **Opportunism risk**: Licensee may become a competitor or degrade quality
- **Contractual incompleteness**: Cannot write contracts covering all contingencies

If no clear I advantage exists -> License or franchise instead of FDI.

### Step 4: Determine Entry Mode

| OLI Configuration | Recommended Mode |
|-------------------|-----------------|
| O + L + I (all strong) | Wholly-owned subsidiary (greenfield or acquisition) |
| O + L + I (I moderate) | Joint venture (share control, reduce risk) |
| O + L (no I) | Licensing / franchising |
| O only (no L, no I) | Export from home |
| No O | Do not internationalize |

## Output Format

```markdown
# OLI Assessment: {Firm} -> {Target Country/Market}

## Ownership Advantages (O)
- Asset-based: {list with strength rating}
- Transaction-based: {list with strength rating}
- O assessment: Strong / Moderate / Weak

## Location Advantages (L)
- Motivation: Market / Resource / Efficiency / Strategic asset
- Key L factors: {list}
- L assessment: Strong / Moderate / Weak

## Internalization Advantages (I)
- Transaction cost drivers: {list}
- Opportunism risk: High / Medium / Low
- I assessment: Strong / Moderate / Weak

## OLI Configuration: {O+L+I / O+L / O only / etc.}

## Recommended Entry Mode: {mode with rationale}
```

## Gotchas

- **OLI is a static snapshot**: Advantages evolve. A location advantage (cheap labor) may erode. Reassess periodically.
- **O advantages can be imitated**: Patents expire, knowledge diffuses. Sustainable O requires continuous innovation.
- **Government policy changes L overnight**: Tax incentives, trade agreements, or political instability can flip L assessments.
- **JVs are a distinct strategy, not a compromise**: Do not default to JV out of uncertainty. JVs carry their own risks.
- **OLI does not address timing**: It answers "should we FDI?" not "when?" For sequencing, combine with Uppsala.

## References

- For OLI mathematical formalization and extensions, see `references/oli-formalization.md`
- For OLI application to service sector FDI, see `references/oli-services.md`
