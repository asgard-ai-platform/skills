# March (1991) Formal Model of Adaptive Systems

**Source**: March, J.G. (1991). Exploration and Exploitation in Organizational Learning. *Organization Science*, 2(1), 71–87.

---

## What the Model Is

March's 1991 paper is not a verbal argument — it is a computational simulation of mutual learning between an organization and its members. The model demonstrates *formally* why organizations that optimize short-run performance systematically underinvest in exploration.

The model operates on three entities:

| Entity | Represents | State Space |
|--------|-----------|-------------|
| **Reality** (m) | The true state of the environment | Vector of m dimensions, each ∈ {-1, +1} |
| **Organizational Code** (K) | Shared beliefs encoded in strategy, process, culture | Vector of m beliefs, each ∈ {-1, 0, +1} |
| **Individual** (i) | Each of n employees | Vector of m beliefs, each ∈ {-1, +1} |

`0` in the Code means "no belief formed yet on this dimension" — the organization is agnostic on that dimension.

---

## Parameters

| Parameter | Range | Meaning |
|-----------|-------|---------|
| `p1` | [0, 1] | Socialization rate: probability per period that an individual who disagrees with the Code is moved to the Code's belief |
| `p2` | [0, 1] | Code-update rate: probability per period that the Code adopts the belief of a superior individual on a dimension where they differ |
| `n` | integer | Number of individuals in the organization |
| `m` | integer | Number of dimensions in Reality (complexity) |

"Superior" individual = one whose current beliefs match Reality on more dimensions than the Code does.

---

## Dynamics (One Simulation Period)

Each period executes in this order:

```
1. EVALUATE: Score each individual and the Code against Reality
   - individual_score(i) = count of dimensions where belief(i,d) == reality(d)
   - code_score         = count of dimensions where code(d) != 0 AND code(d) == reality(d)

2. UPDATE CODE: For each dimension d where code(d) != reality(d):
   - Find individuals where belief(i,d) == reality(d)
   - If any such individual is "superior" (individual_score > code_score):
       with probability p2: set code(d) = reality(d)

3. SOCIALIZE INDIVIDUALS: For each individual i, for each dimension d:
   - If belief(i,d) != code(d) AND code(d) != 0:
       with probability p1: set belief(i,d) = code(d)

4. INDIVIDUAL LEARNING (slow background process):
   - Individuals occasionally update their own beliefs directly from reality
     (March treats this as slow / noisy — the primary learning channel is the Code)
```

Reality itself can shift slowly across periods to model environmental change.

---

## Key Theorems (Simulation Results)

March does not prove closed-form theorems; his results come from simulation runs averaging over many trials. The key empirical findings from the model:

### Finding 1: High p1 Accelerates Convergence, Reduces Diversity

When socialization is fast (high `p1`), individuals quickly align with the Code. This initially *appears* productive — the organization speaks with one voice. But it reduces the pool of superior individuals who can teach the Code something new. Code-updating (p2 mechanism) then has nothing to learn from.

**Effect**: The Code improves rapidly at first, then stagnates. Diversity of individual belief — the raw material for exploration — is consumed.

### Finding 2: High p2 Makes the Code More Accurate but More Volatile

Fast code-updating means the Code quickly reflects superior individuals' knowledge. But:
- If individual knowledge is noisy (individuals learned via a biased sample), the Code can lock in a local optimum.
- The Code converges faster, but not necessarily to the global optimum.

### Finding 3: The Mutual Learning Trap

The dangerous combination is **high p1 + high p2**:

```
High p1 → individuals converge to Code quickly
High p2 → Code updates from individuals quickly
Result  → Code and individuals converge to each other rapidly,
          but their shared belief is determined by early movers,
          not by Reality
```

This is the formal mechanism behind the **competency trap**: the organization becomes internally coherent and efficient at a belief system that may not match the true environment.

### Finding 4: Slow Socialization Preserves Exploration Value

When `p1` is low, individuals retain idiosyncratic beliefs longer. Some of these beliefs match Reality better than the Code does — they are the explorers. The Code then has more opportunities to learn from them (via p2).

**Tradeoff**: Low p1 makes the organization harder to coordinate. Knowledge stays local. Scale-up is slow.

### Finding 5: Organizational Size Cuts Both Ways

Larger `n` (more individuals) increases the probability that *someone* in the organization has superior knowledge on any given dimension. This benefits code-updating. But larger organizations also apply more socialization pressure, which can suppress that diversity faster.

---

## Worked Numerical Example

**Setup**: m = 5 dimensions, n = 10 individuals, 20 periods.

Reality = `[+1, +1, -1, +1, -1]` (fixed for simplicity)

**Initial state (t=0)**:
- Code = `[0, 0, 0, 0, 0]` (no beliefs yet)
- Individual beliefs: randomly assigned, each ∈ {-1, +1}

**Scenario A: High socialization, moderate updating** (p1=0.9, p2=0.5)

```
t=1:  Code learns from 3 superior individuals → Code = [+1, 0, -1, 0, 0]
      code_score = 2 (matched dims 1 and 3)

t=2:  Socialization: 8 of 10 individuals now match Code on dims 1,3
      Code updates dim 4 from a superior individual → Code = [+1, 0, -1, +1, 0]
      code_score = 3

t=5:  Code = [+1, +1, -1, +1, -1], code_score = 5 ✓
      BUT: all individuals now match Code exactly (high p1 wiped diversity)
      → No more updating possible; Code locked in

[Outcome: Fast convergence to correct answer IF initial superior individuals
existed AND code updated before socialization killed diversity]
```

**Scenario B: Low socialization, moderate updating** (p1=0.1, p2=0.5)

```
t=1–5: Individuals retain diverse beliefs; Code updates slowly
t=10:  Code = [+1, 0, -1, +1, 0], code_score = 3
       But 4 individuals still have belief(dim 2) = +1 (correct)
       → Code has opportunities to still learn dim 2

t=15:  Code = [+1, +1, -1, +1, -1], code_score = 5 ✓
       Several individuals still hold non-Code beliefs (exploration reserve)

[Outcome: Slower convergence but more robust; diversity maintained longer
means Code continues learning even after partial convergence]
```

**Scenario C: High socialization, low updating** (p1=0.9, p2=0.1)

```
t=1–3: Individuals rapidly converge to Code
        But Code updates slowly → Code = [+1, 0, 0, 0, 0] at t=3
t=5:   All individuals now believe [+1, 0, 0, 0, 0] (Code's partial belief)
        → No superior individuals remain on dims 2,3,4,5
        → Code cannot update further; stuck at code_score = 1

[Outcome: COMPETENCY TRAP. The organization is perfectly coordinated
around an incomplete, wrong model of reality]
```

**Summary table**:

| Scenario | p1 | p2 | Periods to full accuracy | Risk |
|----------|----|----|--------------------------|------|
| A | 0.9 | 0.5 | ~5 (if lucky) | Diversity gone early; brittle |
| B | 0.1 | 0.5 | ~15 | Slow but robust |
| C | 0.9 | 0.1 | Never | Competency trap |

---

## The Competency Trap: Formal Definition

From the model, a competency trap occurs when:

```
p1 >> p2 / (expected fraction of superior individuals)
```

In plain terms: socialization outruns the Code's ability to identify and absorb superior knowledge. By the time the Code is ready to learn, the pool of individuals with superior knowledge has been homogenized away.

**Organizational translation**: If HR onboarding, performance management, and promotion criteria (p1 mechanisms) move faster than strategic review cycles and R&D pipeline evaluation (p2 mechanisms), the firm will become excellent at its current model before it can challenge that model.

---

## The Failure Trap: Formal Definition

The failure trap is the mirror condition. It occurs when p2 is so high relative to signal quality that the Code updates on noise:

- Individuals' beliefs are noisy (they've seen limited data)
- Code updates rapidly from whoever appears superior in a given period
- Code oscillates — never settles on a stable, accurate belief system

**Organizational translation**: Too many strategic pivots, over-rotation on the most recent data, abandoning experiments before they can generate valid signals.

---

## Parameter → Organizational Design Mapping

| Model Parameter | Organizational Lever | Exploitation Direction | Exploration Direction |
|-----------------|---------------------|----------------------|----------------------|
| p1 (socialization) | Onboarding speed, culture enforcement, performance standards | High p1: fast cultural alignment | Low p1: hire heterodox thinkers, protect dissent |
| p2 (code update) | Strategic review cycles, R&D pipeline gates, leadership learning | Low p2: stable strategy, slow pivots | High p2: fast integration of new findings |
| n (population) | Headcount, diversity of hire | Small n: tight team, fast coordination | Large n: more diversity of belief |
| m (complexity) | Domain complexity of the environment | Low m: specialize deeply | High m: broad sensing capability needed |

**The March prescription for ambidexterity**: Keep p1 *lower* than the typical large firm instinct, and keep p2 *higher* than the typical bureaucratic instinct. The organization must stay permeable to individual-level learning even after it has formed a Code.

---

## Environmental Turbulence Extension

March also runs the model with a *shifting* Reality (random dimension flips each period). Key finding under turbulence:

- Organizations with **low p1** (retained individual diversity) adapt faster to Reality shifts because they have explorers who may already match the new Reality.
- Organizations with **high p1** (socialized into old Code) must wait for the Code to detect the change and then re-socialize — a multi-period lag.

**Implication**: In fast-moving markets, the cost of high socialization is not just innovation stagnation — it is **delayed adaptation to external shifts**. The firm that homogenized too fast must unlearn before it can relearn.

This is the formal basis for the SKILL.md IRON LAW: the balance must be *actively managed* because environmental dynamism continuously shifts the optimal (p1, p2) operating point.

---

## What the Model Does NOT Explain

Honest limitations to avoid over-applying the model:

1. **It treats Reality as objective and fixed (or slowly shifting)** — it does not model enacted environments where firms shape their own competitive context (see Weick's enactment theory).

2. **Individuals are symmetric** — the model does not distinguish between expert individuals and novices; all superior-scoring individuals are equally valid teachers of the Code.

3. **No power dynamics** — in real organizations, whose beliefs update the Code is a political process, not a meritocratic one. The model's p2 mechanism assumes meritocratic code-updating.

4. **No explicit market feedback** — the Code is evaluated against an abstract "Reality," not against revenue or customer signals. The mapping from model to business KPIs requires the analyst to make assumptions.

5. **Sequential equilibrium not analyzed** — March's simulation finds steady-state averages, not the dynamics of firms deliberately switching between exploration and exploitation phases (sequential ambidexterity). For that, the model must be extended.
