---
name: "tw-manufacturing"
description: "Analyze Taiwan's manufacturing industry structure including semiconductor, electronics, machinery, and petrochemical sectors. Use this skill when the user needs to understand Taiwan's industrial landscape, evaluate manufacturing sector opportunities, assess supply chain positioning, or contextualize Taiwan in global manufacturing — even if they say 'Taiwan manufacturing overview', 'semiconductor supply chain', 'what does Taiwan make', or 'industrial analysis of Taiwan'."
metadata:
  category: "WP-12 產業知識"
  tags: ["industry", "taiwan", "manufacturing", "semiconductor"]
---

# Taiwan Manufacturing Industry

## Framework

```
IRON LAW: Taiwan Manufacturing = Global Supply Chain Chokepoint

Taiwan's manufacturing is NOT just domestic industry — it's a critical
node in global supply chains. TSMC alone produces ~90% of the world's
most advanced chips. Analyzing Taiwan manufacturing without the global
supply chain context misses the point entirely.
```

### Taiwan Manufacturing Structure

| Sector | Global Position | Key Companies | Revenue Scale |
|--------|----------------|-------------|-------------|
| **Semiconductor** | #1 foundry (TSMC), #1 packaging (ASE) | TSMC, UMC, ASE, MediaTek | ~NT$4T+ |
| **Electronics/ICT** | #1 laptop/server ODM | Foxconn, Quanta, Pegatron, Wistron | ~NT$10T+ |
| **Flat panel display** | #2 (after China) | AUO, Innolux | ~NT$500B |
| **Machinery** | Major machine tool exporter | Hiwin, Tongtai, Fair Friend | ~NT$1T |
| **Petrochemical** | Top 10 globally | Formosa Plastics Group, CPC | ~NT$2T |
| **Bicycle** | #1 premium bicycle maker | Giant, Merida | ~NT$100B |
| **Textile** | Leading functional fabric | Far Eastern, Eclat | ~NT$300B |

### Key Characteristics

- **OEM/ODM model**: Taiwan excels at manufacturing for global brands, not building its own consumer brands (exceptions: ASUS, HTC, Giant)
- **SME-dominated**: 98% of Taiwan companies are SMEs (<200 employees). The manufacturing base is a network of specialized SMEs, not a few megacorps
- **Cluster geography**: Hsinchu (semiconductor), Taichung (machinery/bikes), Tainan (optoelectronics), Kaohsiung (petrochemical/steel)
- **Japan connection**: Many Taiwan manufacturers supply Japanese companies and adopted Japanese production methods (Toyota Production System, TQM)

### Industry Analysis Framework

For any Taiwan manufacturing sector:
1. **Global position**: What share of global production? Indispensable or replaceable?
2. **Value chain position**: OEM (low margin) → ODM (medium) → OBM (high)
3. **Key customers**: Who are the major buyers? (Apple, NVIDIA, etc.)
4. **Geopolitical risk**: Cross-strait tensions, US-China decoupling impact
5. **Talent pipeline**: Engineering talent supply, brain drain concerns
6. **ESG transition**: Carbon reduction targets, RE100 commitments, circular economy

## Output Format

```markdown
# Taiwan Manufacturing Sector Analysis: {Sector}

## Sector Overview
- Global position: {ranking, market share}
- Key players: {top 5 companies}
- Revenue: {NT$ scale}

## Value Chain Position
{Where Taiwan sits: upstream/midstream/downstream}

## Key Trends
1. {trend + impact}
2. {trend}

## Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| {risk} | H/M/L | H/M/L | {how addressed} |

## Opportunities
1. {opportunity for businesses}
```

## Gotchas

- **"Taiwan semiconductor" is not monolithic**: TSMC (foundry), MediaTek (fabless design), ASE (packaging) are very different businesses. Don't lump them together.
- **Revenue ≠ profit in ODM**: Foxconn has massive revenue (~NT$6T) but thin margins (~2-3%). Revenue ranking can be misleading for profitability analysis.
- **Geopolitical risk is THE issue**: Any analysis of Taiwan manufacturing that ignores cross-strait risk is incomplete. Investors, customers, and governments are actively evaluating this.
- **"Silicon Shield" theory**: Taiwan's semiconductor dominance is argued to be a deterrent against military conflict because the global economy depends on it. This is debated and should not be presented as fact.

## References

- For semiconductor supply chain analysis, see `references/semiconductor-chain.md`
