# Taiwan Semiconductor Supply Chain

## Chain Structure: Three Distinct Business Models

Taiwan's semiconductor industry spans the full value chain, but the three major segments operate under fundamentally different economics. Conflating them is the most common analytical error.

```
Design (Fabless) → Foundry (Pure-Play) → Packaging/Test (OSAT)
     ↑                    ↑                       ↑
  MediaTek              TSMC                    ASE Group
  Novatek               UMC                     Amkor (US, TW ops)
  Realtek               Vanguard                SPIL (merged into ASE)
  (Global: Qualcomm,    GlobalFoundries
   NVIDIA, Apple)       (non-TW)
```

### Business Model Comparison

| Dimension | Fabless Design | Pure-Play Foundry | OSAT |
|-----------|---------------|-------------------|------|
| Gross margin | 40–60% | 50–55% (TSMC) / 20–30% (UMC) | 15–25% |
| Capex intensity | Low (<5% revenue) | Extreme (40–50% revenue) | Medium (15–20%) |
| Asset type | IP, engineers | Fabs, equipment | Assembly lines |
| Customer relationship | Brand + ODM pull | Long-term capacity allocation | Order-based |
| Geopolitical exposure | Low (IP moves) | Extreme (fabs don't move) | Medium |
| Pricing power | High (unique IP) | TSMC: high; others: price competitive | Low |

---

## TSMC's Foundry Model: Why 90% at Advanced Nodes

TSMC's dominance at sub-7nm is not accidental — it results from compounding advantages:

### The Virtuous Cycle

```
More leading-edge customers
        ↓
More R&D revenue per node
        ↓
Faster node migration (Moore's Law execution)
        ↓
More yield learning, more customers
        ↓
(repeat)
```

Samsung and Intel Foundry have similar capital but cannot replicate 30+ years of process learning. TSMC's yield rates at N3 (3nm) are estimated to be 15–20 percentage points higher than competitors at comparable nodes — meaning TSMC ships more working chips per wafer at the same cost.

### Node Economics (Illustrative)

TSMC publishes neither yield nor wafer pricing, but industry estimates:

| Node | Wafer price (est.) | Transistor density | Key customers |
|------|-------------------|-------------------|--------------|
| N5/N4 | ~$17,000 | 170M transistors/mm² | Apple, AMD, NVIDIA |
| N3 | ~$20,000 | 290M transistors/mm² | Apple A17, M3 |
| N2 (2025) | ~$25,000+ | ~400M transistors/mm² | Apple A19 |
| N7/N6 | ~$10,000 | 91M transistors/mm² | AMD, broad base |
| N28 (mature) | ~$3,000–4,000 | 37M transistors/mm² | Auto, IoT, MCU |

**Key insight**: Advanced nodes (<7nm) represent ~50% of TSMC revenue but <20% of wafer volume. Mature nodes (28nm+) are the volume backbone for automotive, industrial, and IoT — where the 2020–2022 chip shortage was worst.

---

## UMC's Positioning: The Mature Node Play

UMC exited the sub-14nm race in 2018, a decision widely criticized then, now reconsidered.

**UMC's thesis**: Leading-edge nodes serve a narrow market (smartphones, servers). The broader semiconductor market — automotive, analog, mixed-signal, MEMS — runs on 28nm–65nm for 10–20 year product cycles.

**Why this works**:
- No N3/N2 capex arms race (~$20B per new node)
- Stable customer base: NXP, Renesas, Texas Instruments supply chains
- Geopolitical hedge: mature node fabs in Singapore and Japan reduce single-country risk
- Automotive semiconductor shortage proved demand inelasticity

**Risk**: Chinese SMIC and state-funded foundries are aggressively building 28nm+ capacity with government subsidies, threatening UMC's differentiation at mature nodes by 2026–2028.

---

## ASE Group: The Packaging Bottleneck

Advanced Semiconductor Engineering (ASE) controls ~30% of global OSAT revenue. Packaging is the underanalyzed chokepoint.

### Why Packaging Matters More Now

Traditional chip scaling (Moore's Law) is slowing. Advanced packaging is how the industry continues delivering performance gains:

| Packaging Technology | What it does | ASE capability | Competitors |
|---------------------|-------------|----------------|-------------|
| SiP (System-in-Package) | Multiple chips in one package | Yes | Amkor |
| CoWoS (TSMC proprietary) | HBM + GPU stacking | TSMC only | — |
| Fan-Out Wafer-Level | Thinner, better IO density | Yes | Amkor, JCET (China) |
| 2.5D Interposer | High-bandwidth chip-to-chip | ASE + TSMC | Intel |
| 3D IC | Vertical stacking | Developing | TSMC SoIC |

**CoWoS is the current constraint**: NVIDIA's H100/H200 GPUs require CoWoS packaging — only TSMC can do it at scale. In 2023–2024, CoWoS capacity, not silicon fab capacity, was the limiting factor on AI chip supply. TSMC has been expanding CoWoS aggressively.

### ASE's Margin Dynamics

OSAT operates on thin margins because:
1. Capital intensive (clean rooms, bonding equipment)
2. Labor intensive (assembly operations in Malaysia, Philippines)
3. Low switching cost — customers can dual-source packaging

ASE's moat is scale (more lines = faster yield learning) and advanced packaging know-how for HPC/AI applications where margins are better.

---

## Taiwan's Fabless Ecosystem: MediaTek as Case Study

MediaTek is the world's largest smartphone chipmaker by unit volume (Qualcomm leads by revenue/ASP).

### MediaTek's Market Segmentation Strategy

| Segment | Chipset line | Target customer | Price tier |
|---------|-------------|-----------------|-----------|
| Premium Android | Dimensity 9000+ | Samsung, Xiaomi flagships | High |
| Mid-range | Dimensity 7000 series | OPPO, vivo, Realtek | Mid |
| Entry | Helio G/A series | Emerging market ODMs | Low |
| Smart TV | MT9950/9000 | TCL, Hisense, Samsung | — |
| WiFi/connectivity | Filogic 880 | Router manufacturers | — |
| ASIC | Custom | Alibaba Cloud | Hyperscaler |

**Key dynamic**: MediaTek competes with Qualcomm in premium, and competes with Chinese fabless (Unisoc, HiSilicon) in low-end. US export controls on HiSilicon (Huawei's chip arm) were a windfall for MediaTek: Huawei phones shifted to MediaTek in 2020–2021.

---

## Supply Chain Dependency Map

For an AI chip (e.g., NVIDIA H100):

```
EDA Tools (Synopsys, Cadence) — US
        ↓
NVIDIA chip design — US
        ↓
TSMC N4 wafer fab — Taiwan (Hsinchu)
        ↓
CoWoS interposer — TSMC (Taichung)
        ↓
HBM memory — SK Hynix (Korea)
        ↓
Advanced packaging (CoWoS) — TSMC
        ↓
PCB/substrate — Unimicron, Nan Ya PCB — Taiwan
        ↓
System integration — Foxconn/Quanta server ODM — Taiwan/Mexico
        ↓
Data center — US hyperscaler
```

Taiwan appears at **three separate nodes** in this chain (wafer fab, packaging, PCB/substrate, ODM assembly). This is why Taiwan's geographic risk concentration is a systemic global concern, not just a Taiwan issue.

---

## Geopolitical Risk: Scenario Analysis Framework

Taiwan Strait risk has moved from theoretical to actively priced by institutional investors. Use this framework:

### Scenario Matrix

| Scenario | Probability (analyst consensus) | Supply impact | Duration |
|---------|-------------------------------|--------------|---------|
| Status quo (managed tension) | ~60% | Minimal | Ongoing |
| Economic coercion (blockade-lite) | ~20% | Severe chip supply disruption in 3–6 months | 6–18 months |
| Military conflict | ~10–15% | Catastrophic; TSMC explicitly would shut fabs | Multi-year |
| Unification (peaceful) | <5% | Unclear; US sanctions likely trigger same supply disruption | — |

### "Silicon Shield" Theory — Why It's Disputed

**Argument for**: Taiwan's indispensability to global supply chains creates mutual deterrence. Any conflict destroys the very asset being contested.

**Argument against**:
- Military strategists note that deterrence logic assumes rational actors with full information
- Xi Jinping has stated reunification as a generational mandate, potentially overriding economic calculus
- If China builds its own advanced fabs (SMIC N+2, etc.), the shield weakens over time
- The shield may paradoxically increase rather than decrease conflict temptation ("seize before they relocate")

**Analytical stance**: Treat Silicon Shield as a real but non-bankable risk mitigant. Don't dismiss it, but don't rely on it for investment theses.

### Diversification Moves (Real, In Progress)

| Company | Location | Node | Status (as of 2025) |
|---------|---------|------|---------------------|
| TSMC Arizona | Phoenix, AZ | N4, N3 | N4 in production; N2 planned |
| TSMC Japan (JASM) | Kumamoto | N12/N16/N6 | Production started 2024 |
| TSMC Germany (ESMC) | Dresden | N22/N28 | Under construction |
| UMC Singapore | Singapore | 22nm+ | Expanding |
| ASE Malaysia | Penang | Advanced packaging | Expanding |

**Caveat**: TSMC Arizona cost per wafer is estimated 40–50% higher than Taiwan due to labor costs, ecosystem gaps, and smaller scale. The US CHIPS Act subsidizes capex but not operating cost. Long-term, Taiwan remains the lowest-cost advanced node location.

---

## Valuation Reference Points

For contextualizing company scale (approximate, subject to change):

| Company | Revenue (FY2024 est.) | Net margin | Market cap (2024 peak) |
|---------|----------------------|-----------|----------------------|
| TSMC | ~$90B USD | ~38% | ~$900B USD |
| MediaTek | ~$17B USD | ~18% | ~$60B USD |
| ASE Group | ~$20B USD | ~7% | ~$20B USD |
| UMC | ~$8B USD | ~22% | ~$20B USD |
| Novatek | ~$3B USD | ~25% | ~$8B USD |

TSMC's net margin (~38%) is exceptional for any capital-intensive manufacturer. It reflects pricing power at leading-edge nodes where there is no alternative supplier.

---

## Quick Diagnostics: Common Analysis Errors

**Error**: "Taiwan's chips" → assumes Taiwan designs the chips
**Correct**: Taiwan *manufactures* chips designed elsewhere (Apple, NVIDIA, AMD). Taiwan's IP is in process technology (how to fab), not product design (what to fab).

**Error**: Treating all fab nodes as interchangeable
**Correct**: A factory that makes 28nm chips cannot make 3nm chips. Equipment, process chemistry, and cleanroom specs are entirely different. Retooling takes 3–5 years minimum.

**Error**: Assuming TSMC Arizona "solves" the concentration risk
**Correct**: Arizona will produce <5% of TSMC's wafer volume by 2027. Leading-edge concentration in Taiwan will persist through at least 2030.

**Error**: Using revenue to rank semiconductor companies
**Correct**: Use gross margin-adjusted revenue or operating income. An ODM assembling chips has $50B revenue at 3% margin; a fabless designer has $5B revenue at 55% margin — the latter creates more value.

**Error**: Conflating "chip shortage" with "advanced node shortage"
**Correct**: The 2020–2022 shortage was primarily at mature nodes (40nm–180nm) for automotive/industrial. Advanced nodes (sub-7nm) were tight but not the crisis. These are supply/demand mismatches with different causes and solutions.
