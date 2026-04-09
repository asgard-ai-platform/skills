# Sparse Matrix Implementation for PageRank

PageRank on real-world web graphs is memory-bound, not compute-bound. A graph with 1M nodes stored as a dense N×N matrix requires 8 TB (float64). Sparse representation reduces this to O(E), where E is the number of edges — typically 10–50× N for web graphs.

---

## Data Structures

### CSR (Compressed Sparse Row) — recommended for PageRank

CSR stores three arrays:

| Array | Length | Content |
|-------|--------|---------|
| `data` | E | out-link destination indices |
| `indptr` | N+1 | row i's edges start at `indptr[i]`, end at `indptr[i+1]` |
| `outdegree` | N | number of outlinks from each node |

For PageRank, you traverse **in-links** to compute rank contributions. Store the **transpose** (in-link graph) in CSR so each row is a destination page and each column is a source.

**Memory cost:** `(E + N) * 4 bytes` for int32 indices + `E * 8 bytes` for float64 weights ≈ `12E + 4N` bytes.

Example — 10M pages, 150M edges:
```
12 * 150_000_000 + 4 * 10_000_000 = 1.84 GB
```
vs. dense: `8 * 10^13 bytes = 80 TB`.

---

## Building the Transpose CSR

```python
def build_transpose_csr(edges: list[tuple[int, int]], n_nodes: int):
    """
    edges: list of (src, dst) pairs (directed: src → dst)
    Returns: (indptr, indices, outdegree)
      - indptr[i]:indptr[i+1] = sources that link INTO node i
      - outdegree[src] = number of outlinks from src
    """
    import array

    outdegree = array.array('i', [0] * n_nodes)
    in_degree = array.array('i', [0] * n_nodes)

    for src, dst in edges:
        outdegree[src] += 1
        in_degree[dst] += 1

    # Build indptr from in-degree (destination-indexed)
    indptr = array.array('i', [0] * (n_nodes + 1))
    for i in range(n_nodes):
        indptr[i + 1] = indptr[i] + in_degree[i]

    # Fill indices (sources of in-links)
    indices = array.array('i', [0] * sum(in_degree))
    pos = array.array('i', indptr[:n_nodes])  # cursor per row

    for src, dst in edges:
        indices[pos[dst]] = src
        pos[dst] += 1

    return indptr, indices, outdegree
```

**Time:** O(E). **Space:** O(E + N). No sorting required.

---

## Core Iteration with CSR

```python
def pagerank_sparse(
    indptr: array,
    indices: array,
    outdegree: array,
    n: int,
    d: float = 0.85,
    epsilon: float = 1e-6,
    max_iter: int = 200,
) -> tuple[list[float], int, bool]:
    """
    Returns (pr_vector, iterations_used, converged).
    IRON LAW: sum(pr_vector) must equal 1.0 ± 0.001 at convergence.
    """
    pr = [1.0 / n] * n
    new_pr = [0.0] * n
    base = (1.0 - d) / n

    for iteration in range(max_iter):
        # Collect dangling rank (nodes with no outlinks)
        dangling_sum = sum(pr[i] for i in range(n) if outdegree[i] == 0)
        dangling_contrib = d * dangling_sum / n

        for i in range(n):
            # Sum contributions from all pages that link INTO i
            contrib = 0.0
            for j_idx in range(indptr[i], indptr[i + 1]):
                src = indices[j_idx]
                contrib += pr[src] / outdegree[src]
            new_pr[i] = base + dangling_contrib + d * contrib

        # L1 convergence check
        delta = sum(abs(new_pr[i] - pr[i]) for i in range(n))
        pr, new_pr = new_pr, pr  # swap buffers, avoid allocation

        if delta < epsilon:
            return pr, iteration + 1, True

    return pr, max_iter, False
```

**Key details:**
- Buffer swap (`pr, new_pr = new_pr, pr`) reuses allocation — no `copy()` call per iteration.
- Dangling sum is O(N) per iteration; acceptable since it's dominated by the O(E) inner loop.
- For N > 10M, replace Python lists with `array.array('d', ...)` to halve memory overhead vs. Python float objects.

---

## NumPy Vectorized Version

When NumPy is available, vectorize the inner loop. The bottleneck is the sparse matrix-vector product (SpMV).

```python
import numpy as np
from scipy.sparse import csr_matrix

def pagerank_scipy(
    src_nodes: np.ndarray,  # shape (E,), int32
    dst_nodes: np.ndarray,  # shape (E,), int32
    n: int,
    d: float = 0.85,
    epsilon: float = 1e-6,
    max_iter: int = 200,
) -> tuple[np.ndarray, int, bool]:
    # Build column-stochastic transition matrix (transpose of link matrix)
    outdegree = np.bincount(src_nodes, minlength=n).astype(np.float64)
    # Avoid division by zero for dangling nodes (handled separately)
    safe_outdeg = np.where(outdegree > 0, outdegree, 1.0)

    # Weight of each edge: 1 / outdegree[src]
    weights = 1.0 / safe_outdeg[src_nodes]

    # Transpose: rows=dst, cols=src (in-link graph)
    M = csr_matrix(
        (weights, (dst_nodes, src_nodes)),
        shape=(n, n),
        dtype=np.float64,
    )

    dangling_mask = outdegree == 0
    pr = np.full(n, 1.0 / n, dtype=np.float64)

    for iteration in range(max_iter):
        dangling_contrib = d * pr[dangling_mask].sum() / n
        new_pr = (1.0 - d) / n + dangling_contrib + d * M.dot(pr)

        delta = np.abs(new_pr - pr).sum()
        pr = new_pr

        if delta < epsilon:
            return pr, iteration + 1, True

    return pr, max_iter, False
```

**Why `csr_matrix` not `lil_matrix`?** `lil_matrix` is for construction; `csr_matrix` is optimized for `dot()`. Convert once, iterate many times.

---

## Worked Example: 5-Node Graph

Graph edges (src → dst):
```
0→1, 0→2, 1→2, 2→0, 3→2, 3→4, 4→3
```
N=5, E=7, d=0.85

**Step 1 — Build outdegree:**
```
node 0: outdeg=2
node 1: outdeg=1
node 2: outdeg=1
node 3: outdeg=2
node 4: outdeg=1
```
No dangling nodes.

**Step 2 — Transpose in-link lists:**
```
node 0 ← [2]           (1 in-link)
node 1 ← [0]           (1 in-link)
node 2 ← [0, 1, 3]     (3 in-links)
node 3 ← [4]           (1 in-link)
node 4 ← [3]           (1 in-link)
```

**Step 3 — Initialize:** `pr = [0.2, 0.2, 0.2, 0.2, 0.2]`

**Step 4 — Iteration 1:**
```
base = (1-0.85)/5 = 0.03

PR(0) = 0.03 + 0.85 * (PR(2)/1)             = 0.03 + 0.85*0.2 = 0.200
PR(1) = 0.03 + 0.85 * (PR(0)/2)             = 0.03 + 0.85*0.1 = 0.115
PR(2) = 0.03 + 0.85 * (PR(0)/2+PR(1)/1+PR(3)/2) = 0.03 + 0.85*(0.1+0.2+0.1) = 0.370
PR(3) = 0.03 + 0.85 * (PR(4)/1)             = 0.03 + 0.85*0.2 = 0.200
PR(4) = 0.03 + 0.85 * (PR(3)/2)             = 0.03 + 0.85*0.1 = 0.115
```
Sum = 1.000 ✓

After convergence (~40 iterations at ε=1e-6), node 2 scores highest due to three in-links.

---

## Memory vs. Speed Trade-offs

| Graph size (N, E) | Recommended structure | Notes |
|---|---|---|
| N < 50K, E < 500K | Python lists + `array.array` | Pure stdlib, no dependencies |
| N < 5M, E < 100M | NumPy + SciPy CSR | `scipy.sparse.csr_matrix.dot()` uses MKL |
| N > 5M | Chunked iteration or GraphX/Spark | CSR won't fit in single machine RAM |

For the pure-stdlib path, `array.array('i', ...)` stores 4 bytes per int vs. Python `list` which stores 28 bytes per int object. For 100M edges, this saves ~2.4 GB for the index arrays alone.

---

## Chunked Iteration for Large Graphs

When the full CSR doesn't fit in RAM, partition nodes into chunks and process rows in batches:

```python
def pagerank_chunked(indptr, indices, outdegree, n, d=0.85, chunk_size=100_000):
    pr = [1.0 / n] * n
    base = (1.0 - d) / n

    for iteration in range(200):
        new_pr = [base] * n
        dangling_sum = sum(pr[i] for i in range(n) if outdegree[i] == 0)
        dangling_contrib = d * dangling_sum / n

        for chunk_start in range(0, n, chunk_size):
            chunk_end = min(chunk_start + chunk_size, n)
            for i in range(chunk_start, chunk_end):
                contrib = sum(
                    pr[indices[j]] / outdegree[indices[j]]
                    for j in range(indptr[i], indptr[i + 1])
                )
                new_pr[i] += dangling_contrib + d * contrib

        delta = sum(abs(new_pr[i] - pr[i]) for i in range(n))
        pr = new_pr
        if delta < 1e-6:
            break

    return pr
```

This pattern keeps only one chunk of `new_pr` rows "hot" at a time, improving cache utilization. For disk-backed graphs, replace `indptr`/`indices` with memory-mapped files (`mmap`).

---

## Correctness Invariants

After every iteration, verify:

```python
assert abs(sum(pr) - 1.0) < 0.001, f"PR sum drift: {sum(pr)}"
assert all(v >= 0 for v in pr), "Negative PR value detected"
```

**Why PR sum can drift:**
- Dangling node rank not redistributed correctly (most common bug).
- Float accumulation over many iterations with single precision.
- Off-by-one in `indptr` slicing (`indptr[i]:indptr[i+1]`, not `indptr[i]:indptr[i]`).

The IRON LAW from SKILL.md — `sum(PR) = 1.0` — is enforced here by explicit dangling redistribution. Without it, rank leaks out of the system each iteration.

---

## Debugging Sparse Bugs

| Symptom | Likely cause | Check |
|---|---|---|
| `sum(PR) < 1.0` after convergence | Dangling nodes not redistributed | Count `outdegree == 0` nodes |
| One node captures nearly all rank | Spider trap without damping | Verify `d < 1` applied every iteration |
| `sum(PR) > 1.0` | Edge counted twice in CSR build | Check for duplicate edges in input |
| Never converges | `epsilon` too small for graph size | Try `epsilon = 1e-4` first |
| `indptr` index error | Off-by-one in CSR construction | Assert `indptr[-1] == len(indices)` |
