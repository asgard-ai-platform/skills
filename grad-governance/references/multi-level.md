# Multi-Level Governance

## Core Framework

Multi-level governance (MLG) describes political systems in which authority is distributed across multiple territorial levels — supranational, national, regional, and local — and where no single level commands the others. The concept was developed by Liesbet Hooghe and Gary Marks (1993, 2001, 2003) initially to explain EU structural policy, then generalized as a typology applicable to federal, quasi-federal, and international governance systems.

**Central claim:** Governance is not zero-sum across levels. Decentralizing authority to subnational levels does not necessarily reduce supranational authority; both can expand simultaneously if the governance space itself grows.

**Why it matters for analysis:** Standard policy analysis assumes a unitary sovereign. MLG analysis does not. It asks: which level holds which authority, under what conditions, and through what mechanisms?

---

## Type I vs Type II: The Fundamental Distinction

Hooghe and Marks (2003) distinguish two ideal-type multi-level governance architectures:

| Dimension | Type I | Type II |
|-----------|--------|---------|
| **Jurisdictions** | General-purpose (bundle many functions) | Task-specific (single function) |
| **Levels** | Fixed number, nested | Unlimited, may overlap |
| **Boundaries** | Non-overlapping | Overlapping |
| **Design stability** | Durable, system-wide reform required to change | Flexible, created and dissolved by demand |
| **Examples** | Federal states (Germany, USA), EU | Special districts, watershed authorities, metropolitan councils |
| **Accountability** | Electoral at each level | Market-like exit, performance benchmarks |

**Diagnostic question:** When mapping a governance arrangement, ask first: is this Type I (you can draw a clean nested map with no overlaps) or Type II (jurisdictions cross-cut and stack)? Many real systems are hybrids — federal states (Type I backbone) with task-specific agencies overlaid (Type II modules).

**Common error:** Treating Type II arrangements as failures of Type I. A metropolitan water authority that crosses municipal lines is not a broken version of municipal government; it is a different governance architecture optimized for a different task boundary.

---

## The Three Dimensions of Multi-Level Authority

Any governance function can be analyzed along three dimensions:

### 1. Vertical Allocation (Which Level?)

Applies the **subsidiarity principle**: authority should reside at the lowest level capable of efficiently managing the externalities of that decision.

**Allocation heuristic:**

```
IF the externalities of Decision X are:
  → purely local (no spillovers):        → allocate to LOCAL level
  → regional spillovers:                 → allocate to REGIONAL level
  → national spillovers:                 → allocate to NATIONAL level
  → cross-border spillovers:             → allocate to SUPRANATIONAL level
  → global public goods:                 → international regime
```

This is a starting heuristic, not a formula — economies of scale, information advantages, and political feasibility modify the answer.

**Oates' Decentralization Theorem (1972):** For a public good where consumption is limited to a subset of the total population, it is always more efficient (or at least no less efficient) for local governments to provide Pareto-efficient levels than for the central government to provide any single uniform level — *unless* costs of provision fall with centralization or preferences are homogeneous across jurisdictions.

Practical implication: where preferences across regions diverge and cross-regional spillovers are limited, decentralize. Where spillovers are large, centralize or create a coordinating mechanism at the appropriate scale.

### 2. Horizontal Coordination (Across Jurisdictions at the Same Level)

Multi-level systems create horizontal collective action problems. Jurisdictions at the same level may:
- Free-ride on neighbors' public goods
- Engage in regulatory races to the bottom (tax competition, lax environmental standards)
- Fail to coordinate on positive-sum arrangements (joint infrastructure, shared services)

**Coordination mechanisms:**

| Mechanism | Hierarchy shadow required? | Example |
|-----------|--------------------------|---------|
| Intergovernmental agreements (IGAs) | Low | River basin compacts |
| Joint authorities | Medium | Regional transit bodies |
| Federal minimum standards | High | Environmental floor regulations |
| Fiscal equalization transfers | High | German Länderfinanzausgleich |
| Mutual recognition | Low | EU single market product standards |

### 3. Vertical Intergovernmental Relations (How Levels Interact)

Three classic models for how levels relate:

**Dual federalism ("layer cake"):** Each level is sovereign within its own sphere; minimal contact between levels. Associated with early US federalism.

**Cooperative federalism ("marble cake"):** Levels share functions; national government sets standards and provides funding, subnational governments implement. Associated with post-New Deal US and most continental European systems.

**Competitive federalism:** Levels compete for mobile citizens and capital; competition disciplines spending and regulation. Associated with Tiebout (1956) and public choice theory of federalism.

Real systems combine elements of all three. Identify which model dominates a given policy sector before diagnosing failures.

---

## Worked Example: EU Cohesion Policy

EU cohesion policy (structural and investment funds) is the paradigmatic MLG case. It allocates roughly €350 billion per programming period across supranational, national, regional, and local levels.

**Governance map:**

| Level | Actor | Function | Authority |
|-------|-------|----------|-----------|
| Supranational | European Commission | Sets eligibility rules, approves programs, disburses funds | Regulatory; withholds funds for non-compliance |
| National | Managing Authorities (ministries) | Negotiates Partnership Agreements, coordinates programs | Administrative; certification authority |
| Regional | Regional governments, NUTS-2 bodies | Implements Operational Programmes, selects projects | Discretionary within EC rules |
| Local | Municipalities, NGOs, firms | Apply for grants, execute projects | Recipient; co-finance obligation |

**Type classification:** Hybrid — national governments are Type I (general-purpose, nested); the Commission's Directorate-General for Regional Policy is a Type II overlay (function-specific, cross-cuts all member states simultaneously).

**MLG tension in this case:**

The Commission pushed "partnership principle" (obligatory involvement of subnational actors in programming). Member states resisted — this bypassed the national level and gave regions direct access to supranational authority. Result: formal partnership requirement, variable implementation. Some states genuinely multi-level; others ran centralized programs with nominal regional consultation.

**Lesson for analysis:** Formal multi-level architecture and actual MLG practice diverge. Always check whether subnational actors have real influence over programming decisions, or merely advisory roles at later implementation stages.

---

## Decision Framework: Diagnosing MLG Problems

Use this sequence when a governance arrangement involving multiple levels is underperforming:

### Step 1: Identify the Mismatch

```
MISMATCH TYPE A — Scale mismatch:
  Problem X has externalities at Scale S, but governance authority
  sits at Scale G ≠ S.
  → Externalities escape the governing jurisdiction.
  → Fix: rescale authority or create coordinating mechanism at S.

MISMATCH TYPE B — Functional mismatch:
  Problem X requires integrated management of Functions F1, F2, F3,
  but they are governed by separate Type II jurisdictions with no
  coordination mechanism.
  → Coordination failure within a level.
  → Fix: joint body, IGA, or merge jurisdictions.

MISMATCH TYPE C — Accountability mismatch:
  Decision-making authority sits at Level L1,
  but electoral accountability sits at Level L2 ≠ L1.
  → Democratic deficit.
  → Fix: create representative institution at L1, or move authority to L2.

MISMATCH TYPE D — Fiscal mismatch:
  Expenditure responsibility at Level L1,
  revenue authority at Level L2 > L1.
  → Vertical fiscal imbalance; soft budget constraint risk.
  → Fix: own-revenue assignment or conditional grant with hard budget rules.
```

### Step 2: Classify the Failure Mode

| Failure | Symptom | Root cause in MLG terms |
|---------|---------|------------------------|
| Race to the bottom | Competing jurisdictions lower standards to attract mobile capital | Horizontal externality, no floor |
| Free-riding | Jurisdiction undersupplies public good, expects neighbors to cover | Scale mismatch — benefit area exceeds jurisdiction |
| Unfunded mandate | Lower level required to implement without adequate resources | Fiscal mismatch |
| Democratic deficit | Decisions made at level with no electoral body | Accountability mismatch |
| Blame diffusion | No level accountable for outcome | Accountability mismatch in network-type MLG |
| Implementation gap | Policy designed at higher level fails at lower level | Capacity mismatch or principal-agent problem |

### Step 3: Select Reform Instrument

Match the failure type to an instrument class. Do not over-centralize (eliminates preference diversity and local information advantages) or over-decentralize (loses coordination gains and allows races to the bottom).

| Failure | Preferred instrument class | Caution |
|---------|--------------------------|---------|
| Scale mismatch | Rescale jurisdiction; regional/supranational body | New body may duplicate; require sunset clause |
| Free-riding | Minimum standards; matching grants | Standards may be too blunt for preference heterogeneity |
| Unfunded mandate | Conditional grant; own-revenue devolution | Grants create dependency; revenue devolution needs capacity |
| Democratic deficit | Directly elected body at governing level | Adds veto player; may slow decisions |
| Blame diffusion | Clear lead-agency designation; performance contracts | Simplification may ignore genuine interdependence |
| Implementation gap | Capacity building; administrative co-production | Long lead time; may require changing civil service incentives |

---

## The Shadow of Hierarchy in MLG

Even in multi-level or network governance, higher-level governments typically retain:

1. **Constitutional authority** to restructure lower levels
2. **Fiscal dominance** through grants, equalization, and conditional transfers
3. **Regulatory override** through minimum standards or preemption

This is the "shadow of hierarchy." Subnational and non-state actors negotiate within it. Their behavior is shaped by what the higher level *could* do, not only what it currently does.

**Analytical implication:** Do not interpret network or collaborative governance at the local or regional level as evidence of autonomous horizontal governance. Map the shadow first. Ask: what would happen if collaboration broke down? Who has the authority to intervene? The answer identifies the actual power center.

**Empirical test:** Trace one episode where the governance arrangement faced a significant failure or crisis. Which actor had the final authority to intervene and impose a solution? That actor defines the effective apex of the multi-level hierarchy, regardless of formal arrangements.

---

## Fiscal Federalism as the Quantitative Complement

MLG analysis is primarily institutional and qualitative. Fiscal federalism theory provides quantitative indicators:

**Vertical fiscal imbalance (VFI):** The share of subnational expenditure funded by intergovernmental transfers rather than own-source revenue.

```
VFI = (Intergovernmental transfers received) / (Total subnational expenditure)

High VFI (> 0.5): Subnational governments are expenditure agents
                  of higher levels; limited fiscal autonomy.
Low VFI (< 0.2):  Subnational governments are fiscally autonomous;
                  risk of insufficient equalization.
```

**Soft budget constraint indicator:** Subnational governments that expect central bailout face soft budget constraints. Observable signals:
- Subnational debt rising without fiscal adjustment
- History of central government bailouts
- No binding subnational insolvency mechanism

High soft budget constraint risk correlates with fiscal mismatch and is a governance failure independent of which level formally holds expenditure authority.

---

## Limits of MLG as Analytical Framework

MLG is strong on describing *structure* (who has authority at what level) and weaker on predicting *outcomes* (what policies result, and whether they perform well).

**What MLG does not explain well:**

- Why some levels gain authority while others lose it (for this, use historical institutionalism or political economy of federalism)
- How non-territorial actors (multinational firms, transnational NGOs) interact with territorial MLG (for this, network governance analysis is needed)
- Whether more levels always improves governance performance (evidence is mixed; more levels can mean more veto players and slower adaptation)

**Complementary frameworks to combine with MLG:**

| Gap | Complement |
|-----|------------|
| Actor behavior within levels | Principal-agent theory |
| Interest group influence on level-allocation | Public choice theory |
| Path dependency in federal design | Historical institutionalism |
| Cross-sector (state/market/civil society) at each level | Network governance |
| Normative evaluation of arrangements | Democratic legitimacy theory |

---

## Key Sources

- Hooghe, L. & Marks, G. (2003). Unraveling the central state, but how? *American Political Science Review*, 97(2), 233–243. — introduces Type I/II distinction
- Marks, G. (1993). Structural policy and multilevel governance in the EC. In A. Cafruny & G. Rosenthal (Eds.), *The State of the European Community*, Vol. 2. — original MLG formulation
- Oates, W. E. (1972). *Fiscal Federalism*. Harcourt Brace. — foundational decentralization theorem
- Tiebout, C. (1956). A pure theory of local expenditures. *Journal of Political Economy*, 64(5), 416–424. — competitive federalism baseline
- Bache, I. & Flinders, M. (Eds.) (2004). *Multi-level Governance*. Oxford University Press. — application beyond EU context
