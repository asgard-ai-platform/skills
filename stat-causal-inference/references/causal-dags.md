# Causal DAGs (Directed Acyclic Graphs)

A DAG is a visual and mathematical language for encoding causal assumptions before touching data. Every node is a variable; every directed edge (`X → Y`) is a causal claim. "Acyclic" means no variable can cause itself through any path.

**Drawing the DAG first** forces explicit commitment to what is a confounder, what is a mediator, and what is a collider — distinctions that cannot be learned from data alone.

---

## Three Node Types That Drive Everything

### 1. Confounder (Common Cause)

```
Z
↙ ↘
X   Y
```

`Z` causes both the treatment `X` and the outcome `Y`. This creates a spurious association between `X` and `Y` even if `X` has no causal effect on `Y`.

**What to do**: Condition on `Z` (include it in regression, match on it, or stratify). This blocks the backdoor path `X ← Z → Y`.

**Example**: Studying exercise (`X`) → health (`Y`). Income (`Z`) causes both (wealthy people exercise more AND have better healthcare). Without controlling for income, you over-estimate the effect of exercise.

---

### 2. Mediator (On the Causal Path)

```
X → M → Y
```

`M` lies on the causal pathway from `X` to `Y`. Part or all of the effect of `X` on `Y` flows through `M`.

**What to do**: Do NOT condition on `M` if you want the total effect of `X` on `Y`. Conditioning on a mediator blocks the very effect you're trying to estimate.

**Example**: Studying job training (`X`) → earnings (`Y`). Employment (`M`) mediates this (training → gets a job → earns more). If you control for employment status, you block the main channel of the effect.

**Exception**: If you want only the *direct* effect of `X` on `Y` (not through `M`), conditioning on `M` is correct — but this is a specific research question requiring careful justification.

---

### 3. Collider (Common Effect)

```
X → C ← Z
```

`C` is caused by both `X` and `Z`. By default, `C` is NOT a source of confounding — the path `X → C ← Z` is *blocked*.

**IRON LAW REINFORCEMENT — Collider Bias**: Conditioning on a collider *opens* a previously blocked path and creates spurious correlation between `X` and `Z` (and through `Z`, between `X` and `Y`).

**Example**: Studying talent (`X`) → success (`Y`). Suppose effort (`E`) and talent both cause success (`C = success`). If you restrict your sample to "successful people only" (conditioning on `C`), you suddenly see a negative correlation between talent and effort — not because they're truly inversely related, but because conditioning on the collider opened the path.

This is also known as **selection bias** when the collider is a sample selection variable.

---

## The Backdoor Criterion

Pearl's backdoor criterion gives a precise rule for identifying valid adjustment sets.

**Definition**: A set of variables `Z` satisfies the backdoor criterion relative to `(X, Y)` if:
1. No variable in `Z` is a descendant of `X`
2. `Z` blocks every "backdoor path" from `X` to `Y` (paths that go through the back of `X`, i.e., paths with an arrow *into* `X`)

If a set `Z` satisfies the backdoor criterion, then:

```
P(Y | do(X)) = Σ_z P(Y | X, Z=z) × P(Z=z)
```

This is the **adjustment formula** — it converts the interventional distribution `P(Y | do(X))` into something computable from observational data.

### Step-by-Step: Applying the Backdoor Criterion

Given this DAG:

```
U (unobserved)
↙    ↘
X      Y
↑
Z → X → Y
     ↑
     W
```

Let's use a cleaner worked example:

```
Variables: X (treatment), Y (outcome), Z (observed confounder), U (unobserved confounder)

DAG:
  Z → X → Y
  Z → Y
  U → X
  U → Y
```

Backdoor paths from `X` to `Y`:
- `X ← Z → Y` (backdoor through Z)
- `X ← U → Y` (backdoor through U, unobserved)

Can we satisfy the backdoor criterion?
- Conditioning on `Z` blocks `X ← Z → Y` ✓
- `X ← U → Y` remains open — but `U` is unobserved ✗

**Conclusion**: Backdoor criterion cannot be satisfied here with observed variables. You need IV or another method.

---

## d-Separation Rules

d-separation determines whether two variables are independent given a set of conditioning variables `Z`, by examining all paths between them.

A path between nodes `A` and `B` is **blocked** by conditioning set `Z` if ANY of these apply along the path:

| Path structure | Conditioning on middle node | Effect |
|---|---|---|
| Chain: `A → M → B` | Condition on `M` | Blocks path ✓ |
| Fork: `A ← C → B` | Condition on `C` | Blocks path ✓ |
| Collider: `A → K ← B` | Do NOT condition on `K` | Already blocked ✓ |
| Collider: `A → K ← B` | Condition on `K` (or its descendant) | Opens path ✗ (bad) |

Two variables are **d-separated** given `Z` if ALL paths between them are blocked. d-separation implies conditional independence (assuming Markov condition holds).

### Worked d-Separation Example

```
DAG:
Season → Rain → Sprinkler → WetGrass
Season → WetGrass
Rain → WetGrass
```

Is `Rain ⊥ Sprinkler`? (No conditioning)
- Path: `Rain ← Season → Sprinkler` — this is a fork, not blocked.
- Answer: **No**, Rain and Sprinkler are NOT independent (they're correlated through Season).

Is `Rain ⊥ Sprinkler | Season`? (Conditioning on Season)
- Path: `Rain ← Season → Sprinkler` — fork, conditioned on `Season`, so **blocked**.
- Answer: **Yes**, Rain ⊥ Sprinkler given Season.

Is `Season ⊥ WetGrass | Rain, Sprinkler`?
- Path: `Season → Rain → WetGrass` — chain through Rain (conditioned), blocked ✓
- Path: `Season → WetGrass` — direct path, not blocked ✗
- Answer: **No**, not d-separated.

---

## How to Draw a DAG: Practical Workflow

### Step 1: List all variables

Include treatment `X`, outcome `Y`, and every variable that could plausibly cause either. Include variables even if they're unobserved — you need them in the DAG to reason correctly.

### Step 2: Ask pairwise causal questions

For every pair `(A, B)`: does `A` directly cause `B` (holding all else fixed)? If yes, draw `A → B`. Be strict: only direct effects, not mediated ones.

### Step 3: Find the paths

Enumerate all paths from `X` to `Y`. Identify which are:
- **Front-door paths** (causal): start with `X →`
- **Backdoor paths** (confounding): start with `← X` or go through a common cause

### Step 4: Apply the backdoor criterion

Find a valid adjustment set (or determine that none exists with observed variables). If none exists, look for:
- An instrumental variable
- A front-door path (Pearl's front-door criterion)
- A natural experiment (DID, RDD)

### Step 5: Identify colliders

Explicitly mark any colliders on backdoor paths. Ensure your regression model does NOT include colliders or their descendants as controls.

---

## Common Mistakes in DAG Construction

### Mistake 1: Omitting unobserved confounders

Just because you can't measure `U` doesn't mean it's absent from the DAG. Draw it anyway (with a dashed node). This forces you to acknowledge that OLS alone cannot estimate the causal effect.

```
# Correct DAG notation for unobserved node:
U (dashed) → X
U (dashed) → Y
```

### Mistake 2: Controlling for a post-treatment variable

If `M` is caused by `X` (even partially), conditioning on `M` introduces bias by blocking causal paths or opening collider paths.

**Test**: Check if the variable you want to control for could have been affected by the treatment. If yes, do not condition on it for total effect estimation.

### Mistake 3: Forgetting that sample selection is conditioning on a collider

If you restrict your analysis to a selected sample (e.g., "users who made a purchase", "patients who completed treatment"), you have conditioned on a collider and may have introduced selection bias.

**Example**:
```
Quality → Purchase ← Marketing
                ↓
             (sample)
```
Analyzing only purchasers conditions on `Purchase` — a collider between `Quality` and `Marketing`. Within this sample, Quality and Marketing will appear inversely correlated even if they're independent in the population.

### Mistake 4: Treating proxies as the true variable

If you measure `X_proxy` instead of `X`, your DAG has:
```
X → X_proxy
X → Y
X_proxy → (measurement noise)
```
Conditioning on `X_proxy` is not the same as conditioning on `X`. Measurement error in the treatment causes attenuation bias in IV and OLS.

---

## Minimal Code: DAG in Python with `networkx`

```python
import networkx as nx
import matplotlib.pyplot as plt

# Build the DAG
G = nx.DiGraph()
G.add_edges_from([
    ("Season", "Rain"),
    ("Season", "Sprinkler"),
    ("Rain", "WetGrass"),
    ("Sprinkler", "WetGrass"),
])

# Check for cycles (should be empty for a valid DAG)
assert list(nx.simple_cycles(G)) == [], "Not a DAG — cycles found"

# Find all paths from treatment to outcome
treatment, outcome = "Rain", "WetGrass"
all_paths = list(nx.all_simple_paths(G, treatment, outcome))
print("Causal paths:", all_paths)
# Output: [['Rain', 'WetGrass']]

# Ancestors of outcome (potential confounders to consider)
ancestors = nx.ancestors(G, outcome)
print("Ancestors of outcome:", ancestors)
# Output: {'Season', 'Rain', 'Sprinkler'}

# Draw
nx.draw_networkx(G, arrows=True)
plt.title("Causal DAG")
plt.show()
```

For more sophisticated DAG analysis (d-separation, adjustment set identification), use the `pgmpy` library:

```python
from pgmpy.models import BayesianNetwork
from pgmpy.independencies import Independencies

model = BayesianNetwork([
    ("Season", "Rain"),
    ("Season", "Sprinkler"),
    ("Rain", "WetGrass"),
    ("Sprinkler", "WetGrass"),
])

# Get implied conditional independencies
independencies = model.get_independencies()
print(independencies)
```

Or use the **DAGitty** web tool (dagitty.net) for interactive DAG drawing and automatic adjustment set identification without any coding.

---

## Decision Table: What to Do With Each Node Type

| Node role | Relative to X→Y path | Condition on it? | Reason |
|---|---|---|---|
| Confounder (common cause) | Backdoor | **Yes** | Blocks backdoor path |
| Mediator (on causal path) | Front-door | **No** (for total effect) | Would block causal path |
| Collider (common effect) | Backdoor | **No** | Conditioning opens spurious path |
| Descendant of collider | Backdoor | **No** | Same as conditioning on collider |
| Instrument | Related to X only | **Do not adjust for** | Keep variation in X clean |
| Descendant of X only | Post-treatment | **No** | Post-treatment variable, biases estimate |
| Pure noise (unrelated) | None | **Optional** | Reduces variance but doesn't bias |

---

## The Front-Door Criterion (Advanced)

When ALL paths from `X` to `Y` through backdoor are confounded by unobserved `U`, but there exists a mediator `M` such that:
1. All causal effect of `X` on `Y` flows through `M`
2. There are no unobserved confounders between `X` and `M`
3. All backdoor paths from `M` to `Y` are blocked by `X`

Then the **front-door adjustment** applies:

```
P(Y | do(X)) = Σ_m P(M=m | X) × Σ_{x'} P(Y | X=x', M=m) × P(X=x')
```

**Classic example** (Pearl): Smoking (`X`) → Tar in lungs (`M`) → Cancer (`Y`), with unobserved genetic factor (`U`) confounding smoking and cancer. If all of smoking's effect on cancer goes through tar deposits, front-door adjustment works even without observing `U`.

In practice, front-door criterion requires very strong assumptions about complete mediation and is rarely applicable outside toy examples. IV is usually the preferred solution when unobserved confounding exists.
