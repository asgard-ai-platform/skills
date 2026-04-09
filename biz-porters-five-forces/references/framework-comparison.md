# Framework Comparison: Porter's Five Forces vs. Adjacent Strategy Tools

This reference answers one recurring question: **which framework do I use, and when?**

The SKILL.md already names three frameworks to avoid mixing up — SWOT, PESTEL, and BCG Matrix. This document gives you the concrete decision logic, and shows what happens when you pick the wrong tool.

---

## The Core Distinction: Level of Analysis

Every major strategy framework operates at a different level. Mismatching level to question is the single most common error.

| Framework | Level | Core Question |
|-----------|-------|---------------|
| Porter's Five Forces | **Industry** | Is this industry structurally attractive? |
| SWOT | **Company** | What is this company's competitive position? |
| PESTEL | **Macro-environment** | What external macro forces will affect us? |
| BCG Matrix | **Portfolio** | How should we allocate capital across our business units? |
| Value Chain Analysis | **Company operations** | Where in our operations do we create (or lose) value? |
| Blue Ocean Strategy | **Strategic move** | How do we create uncontested market space? |

**Porter's Five Forces is the only one of these that answers an industry-level question.** If your question starts with "is this market...", "should we enter...", or "what constrains profitability in...", Five Forces is the right starting point. The others are wrong tools for that question.

---

## Framework Selection Decision Tree

```
Q1: Is the question about a SPECIFIC COMPANY's strengths and weaknesses?
    → YES → Use SWOT
    → NO  → continue

Q2: Is the question about MACRO trends (political, economic, social, tech)?
    → YES → Use PESTEL
    → NO  → continue

Q3: Is the question about how to ALLOCATE CAPITAL across business units?
    → YES → Use BCG Matrix
    → NO  → continue

Q4: Is the question about whether an INDUSTRY OR MARKET is worth entering
    or what drives profitability in it?
    → YES → Use Porter's Five Forces
    → NO  → you may need a different tool entirely
```

---

## Head-to-Head: Five Forces vs. SWOT

These are the two most commonly confused frameworks. They answer fundamentally different questions and should almost never substitute for each other.

### Analytical Scope

**Five Forces** maps structural pressures that affect **all players** in an industry equally. High buyer power in an industry is a condition every firm faces — it's like weather.

**SWOT** maps one company's **relative position** within whatever environment it faces. "Our brand loyalty is a strength" is a company statement, not an industry statement.

### Example: Taiwan Coffee Chain Industry

**Correct Five Forces entry** (industry-level):
> Buyer Power — **High**. Coffee consumers in Taiwan face near-zero switching costs. Thousands of independent cafés, convenience store coffee (7-Eleven's CITY CAFÉ at NT$35), and chain competitors all serve the "morning caffeine" job. Price sensitivity is acute below the NT$100 threshold.

**Incorrect SWOT-contaminated entry** (company-level smuggled into Five Forces):
> Buyer Power — **Low**. Our loyalty program retains 68% of customers year-over-year.

The second example describes **one company's mitigation** of buyer power — it does not describe the underlying industry force. The structural force (buyer power) is still High; this company has partially insulated itself from it. These are two different facts.

### When to Use Both Together

A full strategic assessment often **sequences** them:

1. **Five Forces first** → defines the structural battlefield (industry-level)
2. **SWOT second** → places the specific company on that battlefield (company-level)

Example sequence:
- Five Forces reveals: high threat of new entrants, low supplier power (Taiwan coffee chain industry)
- SWOT reveals: Strength = proprietary roasting process (raises entry barrier for imitators); Weakness = thin geographic coverage outside Taipei

The Five Forces output informs which SWOT items matter most strategically.

---

## Head-to-Head: Five Forces vs. PESTEL

### What PESTEL Does

PESTEL identifies macro-environment forces — **Political, Economic, Social, Technological, Environmental, Legal** — that affect organizations broadly. It is descriptive and environmental, not structural and competitive.

### The Relationship

PESTEL factors are **inputs that can shift Five Forces**, not substitutes for them.

| PESTEL Event | Five Forces Effect |
|---|---|
| Government deregulation (Political) | Lowers threat-of-new-entrants barriers |
| Rising labor costs (Economic) | Shifts supplier power if labor is a key input |
| Platform shift to mobile (Technological) | Lowers entry barriers, increases substitute threats |
| New environmental regulation (Environmental/Legal) | Raises compliance cost → increases capital requirements for new entrants |

### Practical Rule

Run PESTEL when you need to **time** or **project** your Five Forces analysis. If you're doing Five Forces for "Taiwan solar panel manufacturing in 2030", PESTEL identifies which macro trends will materially shift force ratings by then. Without PESTEL, Five Forces is a snapshot; with it, you can project trajectories.

**Do not use PESTEL as a substitute for Five Forces when the question is "is this industry attractive?"** PESTEL lists external factors; it does not synthesize them into a profitability assessment.

---

## Head-to-Head: Five Forces vs. BCG Matrix

### What BCG Matrix Does

BCG Matrix (Growth-Share Matrix) classifies a company's **existing business units** into four quadrants (Stars, Cash Cows, Question Marks, Dogs) based on relative market share and market growth rate. Its output is a **capital allocation recommendation**.

BCG answers: "Given what we already own, where should we invest, harvest, or divest?"

Five Forces answers: "Structurally, how profitable will players in this industry be?"

### They Are Not Competing Tools

BCG Matrix requires you to already be **inside** an industry with operating business units. Five Forces is most powerful **before entry** or when **reviewing whether to stay**.

| Scenario | Correct Tool |
|---|---|
| Should we enter the Taiwan EV charging market? | Five Forces |
| We're already in 3 markets — where do we double down? | BCG Matrix |
| Our cloud division is growing fast — is it structurally defensible? | Five Forces (for cloud) + BCG (for portfolio position) |

### Common Error

Analysts sometimes use BCG to evaluate a new market by asking "is it a Star opportunity?" This is incorrect — BCG requires **current** market share data your company has actually earned. Applying BCG to a market you haven't entered requires assumptions about relative share that don't yet exist. Use Five Forces for pre-entry decisions.

---

## Head-to-Head: Five Forces vs. Value Chain Analysis

Value Chain Analysis (also Porter) examines **internal company operations** — inbound logistics, operations, outbound logistics, marketing, service — to identify where value is created or destroyed.

### When Each Applies

| Question | Tool |
|---|---|
| Why is profitability low across this industry? | Five Forces |
| Why is **our** margin lower than competitors in the same industry? | Value Chain |
| Is this industry worth entering? | Five Forces |
| Once we're in, where should we invest to build advantage? | Value Chain |

Value Chain Analysis and Five Forces are **complementary Porter tools** that operate at different levels. A complete strategic analysis often uses Five Forces to assess industry attractiveness, then Value Chain to diagnose internal capability gaps.

---

## Hybrid Scenario: Market Entry Decision

A full market entry assessment typically requires **three frameworks in sequence**:

### Phase 1 — Five Forces (Industry Attractiveness)
Determine whether the industry is structurally worth entering. If all five forces create extreme pressure, even a strong entrant will face structural headwinds.

*Output*: Industry attractiveness rating + dominant constraining force

### Phase 2 — PESTEL (Trajectory Check)
Identify macro forces that will shift Five Forces ratings over your investment horizon. A currently unattractive industry might become attractive in 3 years due to regulatory change.

*Output*: List of force-shifting PESTEL factors with directional arrows (improving / worsening each force)

### Phase 3 — SWOT (Company Fit)
Given the industry structure revealed in phases 1-2, assess whether **your company specifically** has the strengths to compete and the capacity to address weaknesses.

*Output*: Fit score — does your company's strength profile match what this industry's structure demands?

### Entry Decision Logic

```
IF Phase 1 = Low attractiveness AND Phase 2 = no improving trajectory
    → Strong case against entry (structural, not contingent)

IF Phase 1 = Medium/High attractiveness AND Phase 3 = poor fit
    → Industry is fine, but company is wrong for it — consider partnership or acquisition

IF Phase 1 = Low attractiveness AND Phase 3 = exceptional fit
    → Possible contrarian entry — your strengths may let you reshape one or more forces
    → Identify specifically which force your capability addresses
```

---

## Quick Reference: Symptom-to-Framework Mapping

| User says... | Likely correct framework |
|---|---|
| "Is this market worth entering?" | Five Forces |
| "What are our competitive advantages?" | SWOT |
| "How will AI affect our business?" | PESTEL |
| "Where should we invest our limited capital?" | BCG Matrix |
| "Why are our margins lower than competitors?" | Value Chain Analysis |
| "How can we escape the price war?" | Blue Ocean Strategy |
| "What's driving low profitability in this sector?" | Five Forces |
| "What are the risks in this new market?" | Five Forces + PESTEL |
| "Should we build, buy, or partner to enter?" | Five Forces (industry) + SWOT (capability gap) |

---

## Reinforcing the Iron Law

Every framework above tempts you to slide toward company-level thinking when doing Five Forces. Watch for these contamination signals during analysis:

| Statement type | Contamination signal | Fix |
|---|---|---|
| "Our patents protect us from..." | "Our" = company level | Rephrase: "Patent protection in this industry creates entry barriers because..." |
| "We have loyal customers so buyer power is low" | Describes one firm's mitigation | Industry buyer power is structural — assess switching costs and concentration industry-wide |
| "Our supplier relationship is strong" | One company's negotiated position | Assess supplier concentration and input uniqueness across the industry |

The Five Forces rating for each force describes **the baseline condition facing a new or average industry participant** — not the position of the most well-positioned incumbent.
