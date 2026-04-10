我無法直接寫入檔案（MCP 工具未授權，且內建工具在此環境中不可用）。以下是完整的 `sample_scenario.md` 內容，請存入 `soc-innovation-diffusion/examples/sample_scenario.md`：

---

```markdown
# Example: SaaS HR Tool Struggling to Cross the Chasm

## Scenario

**User's question:** "We built an AI-powered performance review tool called *Reflekt*. We launched 14 months ago, have 1,200 paying users across ~80 companies, and growth has completely stalled. Our early customers love it — NPS is 62. But every enterprise sales call ends with 'we'll wait and see.' What's wrong and how do we fix it?"

---

## Analysis

### Step 1 — Identify Current Adoption Stage

- 80 companies, mostly 20–200 person startups and tech-forward SMBs
- Power users are progressive HR leads and founder-CEOs who treat the tool as a strategic advantage
- NPS 62 from this base → strong product love from a specific psychographic
- Enterprise calls stalling → hitting the **Chasm**

**Verdict:** Reflekt is firmly in the **Early Adopter** phase (~5–8% market penetration in addressable SMB HR tech). The enterprise resistance is textbook chasm behavior: pragmatist buyers require proof from other pragmatists, which Reflekt cannot yet provide.

---

### Step 2 — Innovation Profile Assessment

| Factor | Rating | Evidence | Implication |
|--------|--------|---------|------------|
| Relative advantage | **H** | Cuts review cycle from 3 weeks → 4 days; managers report 40% less prep time | Strong — but only visible after adoption |
| Compatibility | **M** | Works alongside Workday/BambooHR via CSV export, but no native integration | Mid-market HR teams won't adopt without HRIS sync |
| Complexity | **M** | Onboarding takes ~2 hours for admin; individual reviewers find it intuitive once set up | The 2-hour admin burden is a blocker for understaffed HR teams |
| Trialability | **L** | 14-day trial exists but requires full data import to see value; most trials abandon before "aha moment" | Trial is high-friction; pragmatists won't invest without seeing results first |
| Observability | **L** | Results are confidential (performance data); no visible proof for peers outside the company | HR tools have an inherent observability problem — fix requires case study collateral, not product change |

**Weakest factors:** Trialability and Observability — both structural barriers for early majority adoption.

---

### Step 3 — Chasm Diagnosis

Early adopters (current base) bought Reflekt because:
- They tolerate the CSV workaround
- They believe in AI-assisted management philosophy
- A founder-CEO could mandate adoption overnight

The early majority (enterprise HR directors at 200–1,000-person companies) need:
- A reference customer in their exact industry/size band
- Complete HRIS integration (not CSV)
- Documented compliance story (SOC 2, GDPR data handling for EU)
- Team-level admin controls and audit logs
- Proof that peers have deployed it without embarrassing failures

**Whole product gap summary:**
1. No BambooHR / Workday native integration
2. No SOC 2 Type II certification
3. No admin dashboard with role-based access
4. Zero reference customers in mid-market SaaS (the most natural first beachhead)

---

### Step 4 — Beachhead Selection

Target segment options evaluated:

| Candidate Niche | Fit | Reference leverage | Decision |
|----------------|-----|-------------------|---------|
| Mid-market SaaS (200–600 employees, Series B–C) | High — already have 6 customers here | High — SaaS HR leads talk at events like Lattice Summit | ✅ **Beachhead** |
| Professional services firms (law, consulting) | Medium — review culture strong | Low — fragmented, slow procurement | ❌ |
| Healthcare / regulated industries | Low — compliance barrier too high | Low — too risk-averse | ❌ |

**Chosen beachhead:** Series B–C SaaS companies, 200–600 employees, US-based, using BambooHR.

Rationale: Reflekt already has 6 logos here. This cohort attends the same conferences, reads the same HR newsletters, and their People Ops leads are highly networked. Winning 15 of them creates a self-referencing cluster.

---

### Step 5 — Adoption Acceleration Plan

Prioritized by impact on weakest factors:

1. **Fix trialability** — Replace 14-day free trial with a "Review Cycle Pilot": offer to run one complete review cycle (6 weeks) for free, with Reflekt's team handling the setup. Goal: pragmatists experience the full value before committing. Estimated cost: $3K/pilot; target 10 pilots in beachhead segment.

2. **Close the whole product gap** — Ship BambooHR native integration (not CSV) within 60 days; contract SOC 2 Type II audit (6-month process, start now). These are table-stakes for the beachhead segment.

3. **Build reference density** — Offer the 6 existing beachhead customers a 30% discount in exchange for a named case study, a 30-minute reference call slot (up to 4/quarter), and a quote for the website. Do not genericize — "Series B SaaS, 340 employees, 98% review completion rate in 5 days" beats "mid-size tech company."

4. **Improve observability** — Publish a quarterly *State of Performance Reviews* benchmark report using anonymized aggregate data. Pragmatists cite industry benchmarks; this makes Reflekt's results visible without violating confidentiality.

5. **Bowling pin expansion** — After establishing 15 wins in Series B–C SaaS, use those references to enter adjacent niche: Series B–C FinTech (similar size, higher compliance awareness → harder, but beachhead proof unlocks it).

---

## Result

```markdown
# Diffusion Analysis: Reflekt AI Performance Review Tool

## Innovation Profile
| Factor | Assessment | Implication |
|--------|-----------|------------|
| Relative advantage | H | 3-week → 4-day review cycle; strong once experienced |
| Compatibility | M | CSV-only HRIS sync blocks mid-market; BambooHR integration required |
| Complexity | M | 2-hr admin onboarding is friction; individual UX is fine |
| Trialability | L | Trial requires full data import before value is apparent; redesign as guided pilot |
| Observability | L | Performance data is confidential by nature; fix via case studies + benchmark report |

## Current Adoption Stage
- Estimated penetration: ~5–8% of addressable SMB HR tech market
- Current adopter category: **Early Adopters / Chasm**
- NPS 62 from visionary buyers; enterprise stall is classic chasm symptom

## Chasm Strategy
- Beachhead segment: Series B–C SaaS companies, 200–600 employees, US, BambooHR users
- Whole product gaps:
  - BambooHR native integration (not CSV)
  - SOC 2 Type II certification
  - Admin dashboard with RBAC and audit logs
  - Named reference customers in segment
- Reference strategy: Convert 6 existing beachhead logos to named case studies
  in exchange for 30% renewal discount + reference call slots (4/quarter)

## Adoption Acceleration Plan
1. **[Trialability]** Replace free trial with 6-week guided Review Cycle Pilot
   (Reflekt-managed setup, 10 pilots in beachhead)
2. **[Compatibility]** Ship BambooHR integration within 60 days
3. **[Observability]** Publish quarterly benchmark report using anonymized aggregate data
4. **[References]** Lock in 6 named case studies from current beachhead customers by Q3 2026
5. **[Expansion]** After 15 beachhead wins, open bowling pin to Series B–C FinTech
```

**Key warning:** Resist the temptation to chase enterprise deals already in the pipeline.
A half-won enterprise logo (proof of concept, no full rollout) does not count as a
pragmatist reference. Close the beachhead niche completely first.
```

---

內容說明：

- **場景**：AI HR 工具 *Reflekt*，真實常見的 SaaS 成長停滯情境，NPS 高但企業端卡關
- **五因素評分**：每個都有具體數據支撐（3週→4天、2小時 onboarding、CSV 限制）
- **Chasm 診斷**：明確點出 whole product gap 的四個缺口
- **Beachhead 選擇**：三個候選、理性比較後選定，而非直接給答案
- **Result 區塊**：完全對應 SKILL.md 的 Output Format 模板
