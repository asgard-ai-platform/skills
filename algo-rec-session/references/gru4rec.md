# GRU4Rec: Neural Session-Based Recommendation

GRU4Rec (Hidasi et al., 2015/2018) adapts Gated Recurrent Units to model click sequences within a session. Unlike Markov chains, it captures **long-range dependencies** in the sequence — item A two clicks ago can still influence the next recommendation even if B and C appeared since.

---

## Architecture

```
Session sequence:   [A]  →  [B]  →  [C]  →  predict next
                     ↓        ↓        ↓
Input layer:       e_A      e_B      e_C       (item embeddings, dim d)
                     ↓        ↓        ↓
GRU layer(s):      h_1  →  h_2  →  h_3        (hidden state, dim H)
                                      ↓
Output layer:                     ŷ = h_3 · E^T   (scores over all N items)
```

**E** is the item embedding matrix (N × d). The output is a dot product of the final hidden state with all item embeddings, producing N scores. No softmax at inference — raw logits are sufficient for ranking.

---

## GRU Cell (for reference)

At each position t, given input embedding e_t and previous hidden state h_{t-1}:

```
Update gate:    z_t = σ(W_z · e_t + U_z · h_{t-1})
Reset gate:     r_t = σ(W_r · e_t + U_r · h_{t-1})
Candidate:      h̃_t = tanh(W_h · e_t + U_h · (r_t ⊙ h_{t-1}))
Hidden state:   h_t = (1 − z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t
```

The update gate z_t decides how much of the old state to keep. In practice you don't implement this manually — use `nn.GRU` in PyTorch or `tf.keras.layers.GRU`. What matters is understanding that **z_t ≈ 0 means "forget the past; focus on current input"**, which happens when session intent shifts.

---

## Session-Parallel Mini-Batches

The most operationally important GRU4Rec innovation is not the GRU itself — it's the training scheme.

**Problem:** Sessions have variable lengths. Padding all sessions to max length wastes compute and distorts the hidden state.

**Solution:** At each training step, take position t from B different sessions simultaneously.

```
Step 1:   session_1[1], session_2[1], session_3[1], ...  → batch size B
Step 2:   session_1[2], session_2[2], session_3[2], ...
Step 3:   session_1[3], ...
          (session_3 ends here → replace with session_4[1], reset that slot's h to 0)
```

**Key rule:** When a session ends and a new one starts in the same slot, **reset only that slot's hidden state**. Other slots continue from their current h. This is implemented via a reset mask:

```python
# mask[i] = 0 if slot i just started a new session, else 1
h_next = h * mask.unsqueeze(-1) + (1 - mask.unsqueeze(-1)) * 0
```

This keeps GPU utilization high and avoids padding artifacts.

---

## Loss Functions

Two losses are designed for recommendation (ranking) rather than classification.

### TOP1-max (recommended for recall-focused tasks)

For a target item s and B−1 negative samples {n_j}:

```
TOP1-max = (1/B) Σ_j [ σ(ŷ_{n_j} − ŷ_s) + σ(ŷ_{n_j}²) ]
```

The second term `σ(ŷ_{n_j}²)` regularizes negative scores toward zero.

### BPR-max (recommended for MRR-focused tasks)

```
BPR-max = −log( Σ_j softmax(ŷ_{n_j}) · σ(ŷ_s − ŷ_{n_j}) )
```

where softmax(ŷ_{n_j}) weights each negative by its relative score. This focuses learning on the hardest negatives.

**Which to use:**

| Metric priority | Loss      |
|-----------------|-----------|
| Hit Rate @ K    | TOP1-max  |
| MRR / NDCG      | BPR-max   |
| Both matter     | BPR-max (generally more robust in 2018+ experiments) |

**Do not use cross-entropy** for session recommendation. CE treats recommendation as classification over all N items, which requires a full softmax over potentially millions of items and doesn't model pairwise ranking structure.

---

## Negative Sampling Strategy

GRU4Rec uses **in-batch negatives** — other items in the same mini-batch serve as negatives for each sample. This is efficient but has a bias: popular items appear as negatives more often, so the model learns to down-rank them proportionally. This is usually a feature (popularity debiasing), not a bug.

If your catalog has items with highly skewed popularity (Pareto distribution), use **popularity-weighted sampling** so that popular items appear as negatives proportionally to their frequency. Random uniform sampling underrepresents them and undertrains the model's ability to discriminate against them.

---

## Worked Example: Score Computation

Suppose:
- Catalog size N = 10,000 items
- Embedding dim d = 64
- Hidden size H = 100
- Current session: [item_42, item_17, item_305]

**Forward pass:**

```python
import torch
import torch.nn as nn

class GRU4Rec(nn.Module):
    def __init__(self, n_items, d=64, H=100, n_layers=1):
        super().__init__()
        self.emb = nn.Embedding(n_items, d, padding_idx=0)
        self.gru = nn.GRU(d, H, n_layers, batch_first=True)
        self.out = nn.Linear(H, n_items, bias=False)

    def forward(self, seq, hidden=None):
        # seq: (batch, seq_len) item indices
        x = self.emb(seq)              # (batch, seq_len, d)
        out, h = self.gru(x, hidden)   # out: (batch, seq_len, H)
        logits = self.out(out)         # (batch, seq_len, N)
        return logits, h

model = GRU4Rec(n_items=10000, d=64, H=100)

# Inference for one session [42, 17, 305]
seq = torch.tensor([[42, 17, 305]])    # shape (1, 3)
logits, h = model(seq)
next_scores = logits[0, -1, :]        # scores for all 10,000 items after last click
top5 = next_scores.topk(5).indices    # top-5 next item predictions
```

**Incremental inference** (real-time, one click at a time):

```python
# After click on item_42:
seq1 = torch.tensor([[42]])
_, h = model(seq1)            # save h

# After click on item_17:
seq2 = torch.tensor([[17]])
_, h = model(seq2, hidden=h)  # pass previous hidden state

# After click on item_305:
seq3 = torch.tensor([[305]])
logits, h = model(seq3, hidden=h)
next_scores = logits[0, -1, :]
```

Incremental inference avoids reprocessing the full sequence on each new click — critical for real-time latency.

---

## Hyperparameter Defaults (from original paper + community experience)

| Parameter       | Default | Notes |
|----------------|---------|-------|
| Embedding dim d | 64–128  | Larger if catalog > 500k items |
| Hidden size H   | 100–256 | 100 sufficient for most e-commerce |
| GRU layers      | 1       | 2 layers rarely helps; adds latency |
| Dropout         | 0.0–0.5 | On GRU output, not input embedding |
| Batch size B    | 32–512  | Also controls # negative samples |
| Learning rate   | 1e-3    | Adam optimizer |
| Loss            | BPR-max | Default for new projects |

---

## When GRU4Rec Beats Markov Chains

GRU4Rec outperforms Markov chains when:

1. **Sessions are long (5+ clicks)**: GRU captures dependencies beyond order-2 transitions. Markov(2) on a 10-click session ignores clicks 1–8.
2. **Item catalog is large (>10k items)**: Transition matrices become sparse; GRU generalizes via embeddings.
3. **You have training data**: GRU4Rec needs at least ~50k sessions to beat a well-tuned Markov baseline. Below that, Markov wins on data efficiency.

Markov chains win when:
- You need sub-millisecond inference with no GPU
- Sessions are very short (≤3 clicks)
- You have under ~10k training sessions

---

## IRON LAW Alignment: First Clicks Define Session Intent

The IRON LAW in the parent skill states the first 2-3 clicks establish session intent. GRU4Rec's hidden state h_t accumulates all previous clicks, but the **update gate z_t ≈ 0** at early positions means early clicks strongly shape h and persist through the session. This is GRU's correct behavior — but it also means:

- **If the first click is noise** (e.g., user landed from a misclick), GRU will propagate that noise through h for the entire session.
- Mitigation: apply a learned "session start" bias vector to h_0 rather than initializing to zeros. This primes the model to be uncertain before any clicks accumulate.

---

## Serving in Production

**Pre-compute item embeddings**: The output layer `E^T` is static after training. Store all item embeddings in a vector index (FAISS, ScaNN) so you can retrieve top-K without scoring all N items.

**Approximate nearest neighbor (ANN) lookup**:

```
Inference = GRU forward pass (fast) + ANN search over item embeddings (fast)
vs.
Inference = GRU forward pass + full N-dimensional matrix multiply (slow at N > 100k)
```

The ANN approach drops recall by ~1–2% vs exact search but gives 10–100× speedup at large catalog sizes. Acceptable tradeoff.

**State caching**: Store h per session ID in Redis (TTL = session timeout, e.g., 30 min). Each new click:
1. Load h from Redis
2. Forward one GRU step with new item embedding
3. Store updated h back to Redis
4. Run ANN to get top-K candidates

This keeps inference latency under 5ms for H ≤ 256.

---

## Evaluation

Use **leave-one-out** evaluation: for each session, hide the last item, predict with GRU4Rec, check if hidden item appears in top-K.

```
Hit Rate @ K = (# sessions where true next item ∈ top-K) / (# sessions)
MRR         = mean(1 / rank_of_true_next_item)
```

Typical production targets for e-commerce:

| Metric      | Baseline (random) | Good    | Strong  |
|-------------|-------------------|---------|---------|
| Hit@20      | 0.002             | 0.25+   | 0.40+   |
| MRR         | 0.001             | 0.12+   | 0.20+   |

If you're below "Good", check: session splitting correctness, whether you're leaking future data into training, and whether the catalog has sufficient coverage in training sessions.
