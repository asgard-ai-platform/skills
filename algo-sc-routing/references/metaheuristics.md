# Metaheuristics for VRP

Clarke-Wright savings gets you within ~15–20% of optimal quickly. When that's not good enough, or when the instance has 100+ customers, metaheuristics close the gap. This document covers Simulated Annealing (SA) and Genetic Algorithm (GA) applied to VRP — the two most widely deployed in logistics.

---

## When Metaheuristics Are Warranted

| Condition | Recommended |
|-----------|-------------|
| n < 25 customers | Exact solver (branch and bound) |
| 25 ≤ n ≤ 100 | Clarke-Wright + 2-opt |
| n > 100 | SA or GA (this document) |
| Multiple hard constraints (TW + capacity + driver hours) | GA (constraint encoding easier) |
| Need solution in < 5 seconds | SA with fast cooling |
| Need diverse solutions for scenario analysis | GA (population-based) |

---

## Simulated Annealing (SA)

### Core Idea

SA accepts worse solutions probabilistically, allowing escape from local optima. The acceptance probability decreases over time (annealing), transitioning from global exploration to local exploitation.

### Acceptance Rule

Given current solution cost `f(s)` and candidate cost `f(s')`:

```
if f(s') < f(s):
    accept always
else:
    accept with probability P = exp(-(f(s') - f(s)) / T)
```

Where `T` is the current temperature.

### Cooling Schedule

Use **geometric cooling**: `T_{k+1} = α · T_k`

| Parameter | Typical range | Effect |
|-----------|--------------|--------|
| `T_0` (initial temp) | Set so P(accept 5% worse) ≈ 0.8 | Too low → no exploration; too high → random walk |
| `α` (cooling rate) | 0.95 – 0.995 | Lower α = faster but lower quality |
| `T_min` (stop) | 0.01 · T_0 | |
| `iterations per T` | 100 · n | |

**Setting T_0:** Run 100 random neighbor samples, compute average cost worsening `Δ_avg`. Solve `0.8 = exp(-Δ_avg / T_0)` → `T_0 = -Δ_avg / ln(0.8)`.

For a 50-customer instance where random moves average 12 km worse: `T_0 = -12 / ln(0.8) = -12 / (-0.2231) ≈ 53.8`.

### Neighborhood Operators

Apply these in rotation — each produces a candidate `s'`:

**2-opt (intra-route):** Reverse a segment within one route.
```
Route: depot → A → B → C → D → depot
2-opt(B,D): depot → A → D → C → B → depot
```
Cost change: `Δ = d(A,D) + d(B,depot) - d(A,B) - d(D,depot)`

**Or-opt (inter-route):** Move one customer from route R1 to route R2.
```
R1: depot → A → B → C → depot  (remove B)
R2: depot → X → Y → depot       (insert B between X and Y)
```
Only accept if `load(R2) + demand(B) ≤ capacity`.

**3-opt:** Reconnect three route edges. Stronger but 3× slower — use only when SA converges.

### SA Pseudocode

```python
def simulated_annealing_vrp(routes, distance_matrix, demands, capacity,
                             alpha=0.98, iter_per_T=100, T_min=0.1):
    s = routes                          # current solution (list of routes)
    f_s = total_distance(s)
    best = deepcopy(s)
    f_best = f_s

    T = initial_temperature(s, distance_matrix, target_accept=0.8)

    while T > T_min:
        for _ in range(iter_per_T * num_customers(s)):
            s_prime = random_neighbor(s, distance_matrix, demands, capacity)
            f_prime = total_distance(s_prime)
            delta = f_prime - f_s

            if delta < 0 or random() < exp(-delta / T):
                s = s_prime
                f_s = f_prime
                if f_s < f_best:
                    best = deepcopy(s)
                    f_best = f_s

        T *= alpha

    return best, f_best
```

**`random_neighbor`** picks 2-opt or or-opt with equal probability; discards infeasible moves (capacity violation).

### Worked Example

**Setup:** 8 customers, 2 vehicles (cap=100), depot at (0,0).

| Customer | x | y | demand |
|----------|---|---|--------|
| C1 | 2 | 3 | 20 |
| C2 | 5 | 1 | 15 |
| C3 | 6 | 4 | 30 |
| C4 | 1 | 6 | 25 |
| C5 | 8 | 2 | 20 |
| C6 | 9 | 5 | 35 |
| C7 | 3 | 8 | 10 |
| C8 | 7 | 7 | 15 |

Clarke-Wright initial solution (hypothetical):
- R1: depot → C1 → C4 → C7 → depot (load=55, dist=28.4 km)
- R2: depot → C2 → C3 → C5 → C6 → C8 → depot (load=115 — **infeasible!**)

Clarke-Wright would never produce this; shown to illustrate why or-opt is needed. After or-opt moves C6 (demand=35) to R1:

- R1: depot → C1 → C4 → C7 → C6 → depot (load=90, dist=34.1 km)  ← feasible
- R2: depot → C2 → C3 → C5 → C8 → depot (load=80, dist=35.2 km)

SA at T=10 evaluates 2-opt on R1: reverse C4→C7 segment:
- R1_new: depot → C1 → C7 → C4 → C6 → depot (dist=31.8 km)
- Δ = 31.8 - 34.1 = -2.3 → **accept** (improvement)

---

## Genetic Algorithm (GA)

### Representation

Each **chromosome** encodes a complete VRP solution as a permutation of customer IDs. Vehicle splits are implicit via capacity decoding.

```
Chromosome: [C3, C7, C1, | C2, C5, C8, | C4, C6]
            ← route 1 →  ← route 2 →   ← route 3 →
```

**Decoder (Giant Tour Decoding):**
1. Read customers left to right
2. Assign to current route while `current_load + demand(next) ≤ capacity`
3. On overflow, start new route
4. If routes_needed > vehicles_available → **infeasible** (penalize fitness)

This encoding avoids explicitly tracking vehicle splits — the decoder handles it deterministically.

### Fitness Function

```
fitness(chromosome) = total_distance(decoded_routes)
                    + λ · penalty(infeasible_constraints)
```

Use `λ = 10 · avg_route_distance` so a constraint violation always outweighs a distance improvement.

For soft constraints (e.g., driver hour limits), use `λ_soft = 2 · avg_route_distance`.

### GA Operators

#### Selection: Tournament Selection (k=3)
1. Sample 3 chromosomes randomly
2. Return the one with best (lowest) fitness
3. Repeat for each parent slot

Avoids premature convergence better than roulette wheel when fitness values are close.

#### Crossover: Order Crossover (OX)
Preserves relative order of customers — critical because VRP solutions are permutations.

```
Parent 1: [C1, C3, C5, C7, C2, C4, C6, C8]
Parent 2: [C2, C7, C4, C1, C8, C5, C3, C6]

Step 1 — Pick segment from P1 (positions 2-5): [C5, C7, C2, C4]
Step 2 — Copy segment to child at same positions:
Child:    [__, __, C5, C7, C2, C4, __, __]
Step 3 — Fill remaining positions from P2 in order, skipping already-used:
P2 order: C2(skip), C7(skip), C4(skip), C1, C8, C5(skip), C3, C6
Child:    [C1, C8, C5, C7, C2, C4, C3, C6]
```

#### Mutation: Swap + Inversion

Apply one randomly per chromosome at rate `p_mut = 0.1 / n`:

- **Swap:** Exchange two random positions
- **Inversion:** Reverse a random subsequence (equivalent to 2-opt on the tour)

#### Local Search Injection (Memetic GA)

After crossover, apply 2-opt to each offspring for 50 iterations. This "Lamarckian" improvement dramatically accelerates convergence — standard practice in competitive VRP solvers.

### GA Loop

```python
def genetic_algorithm_vrp(customers, capacity, num_vehicles,
                           pop_size=100, generations=500, elite_k=5):
    population = [random_permutation(customers) for _ in range(pop_size)]

    for gen in range(generations):
        scored = [(fitness(c, capacity, num_vehicles), c) for c in population]
        scored.sort()

        # Elitism: carry top-k unchanged
        next_pop = [c for _, c in scored[:elite_k]]

        while len(next_pop) < pop_size:
            p1 = tournament_select(scored, k=3)
            p2 = tournament_select(scored, k=3)
            child = ox_crossover(p1, p2)
            child = mutate(child, p=0.05)
            child = local_2opt(child, capacity, iterations=50)  # memetic step
            next_pop.append(child)

        population = next_pop

    best = min(scored, key=lambda x: x[0])
    return decode_routes(best[1], capacity, num_vehicles), best[0]
```

### GA Parameters

| Parameter | Recommended | Notes |
|-----------|------------|-------|
| Population size | 50–200 | Larger for n > 200 customers |
| Generations | 300–1000 | Monitor convergence; stop if no improvement in 100 gens |
| Crossover rate | 0.85 | Use OX always; rate controls whether crossover fires |
| Mutation rate | 0.05–0.10 | Higher for diverse populations |
| Elite size | 2–5% of pop | Too high → premature convergence |
| Local search iterations | 50–200 per offspring | Biggest quality lever |

---

## SA vs GA: Decision Guide

| Criterion | SA Wins | GA Wins |
|-----------|---------|---------|
| Time budget | < 30 seconds | Minutes available |
| Problem size | 50–300 customers | 100–1000 customers |
| Constraint type | Capacity only | Multiple hard constraints |
| Need multiple solutions | No | Yes (population) |
| Implementation simplicity | Simpler | More complex |
| Parallelization | Hard | Easy (evaluate population in parallel) |

**Rule of thumb:** Start with SA. If quality is insufficient after tuning cooling schedule, switch to memetic GA.

---

## Convergence Diagnostics

Track these metrics to detect problems early:

**SA:**
- Plot `f_best` vs. iteration. Should decrease steadily then plateau.
- If plateau occurs in first 20% of iterations → `T_0` too low or `α` too aggressive.
- If `f_best` never improves from initial → `iter_per_T` too low.

**GA:**
- Plot `f_best` and `f_avg` per generation.
- If `f_avg` converges to `f_best` rapidly (< 50 generations) → premature convergence; increase mutation rate or population size.
- Acceptable: `f_avg` stays 5–15% above `f_best` throughout.

**Quality benchmark:** After convergence, compare against Clarke-Wright solution.
- Improvement of 5–15%: expected for SA/GA on medium instances
- Improvement < 2%: Clarke-Wright was already near-optimal; stop here
- Improvement > 20%: Clarke-Wright initial solution was poor; check for bugs

---

## Common Failure Modes

**SA — all moves rejected after 100 iterations:** Temperature dropped too fast. Increase `α` from 0.95 to 0.99.

**SA — solution never improves past initial:** Neighborhood operators are generating infeasible solutions (capacity violations). Check that or-opt rejects moves where `new_load > capacity`.

**GA — identical chromosomes after 20 generations:** Add random immigrants: replace bottom 10% of population with random permutations every 50 generations.

**GA — decoder assigns too many vehicles:** Demand distribution requires more vehicles than `num_vehicles`. Detect by counting route splits; if decoder consistently uses `num_vehicles + k`, the problem is infeasible as stated — report this rather than silently producing a plan with too many vehicles.

**Both — oscillating best solution:** Current best flips between two solutions. This is normal for SA (inherent stochasticity); for GA it indicates insufficient elite preservation. Increase elite size.

---

## Integration with Clarke-Wright

Metaheuristics work best when **warm-started** from Clarke-Wright output rather than random permutations:

```python
# SA warm start
initial_routes = clarke_wright(customers, depot, capacity)
sa_result = simulated_annealing_vrp(initial_routes, ...)

# GA warm start
cw_chromosome = routes_to_permutation(initial_routes)
population = [cw_chromosome] + [random_permutation(customers) for _ in range(pop_size - 1)]
```

Warm-starting SA typically reduces required iterations by 40–60% while achieving comparable or better final quality.
