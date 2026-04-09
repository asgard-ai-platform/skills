# Search Relevance Evaluation

Relevance evaluation answers one question: **is the pipeline returning the right products in the right order?** There are two complementary approaches — offline evaluation (judgment sets + NDCG) and online evaluation (behavioral metrics). Neither alone is sufficient.

---

## Offline Evaluation: NDCG on a Judgment Set

### Why NDCG

NDCG (Normalized Discounted Cumulative Gain) rewards:
- Highly relevant results ranked higher
- Relevant results appearing earlier in the list

It produces a score between 0 and 1, enabling comparison across queries and across system versions.

### Grading Scale

Use a 4-point scale. Binary (relevant/not) loses too much signal for e-commerce.

| Grade | Label | Meaning |
|-------|-------|---------|
| 3 | Perfect | Exact product match (user searches "iPhone 15 Pro 256GB black", this is it) |
| 2 | Excellent | Right product category, right intent, minor attribute mismatch |
| 1 | Fair | Loosely related, might satisfy intent under some interpretation |
| 0 | Irrelevant | Wrong category, wrong intent, completely off-topic |

**Grading example** — query: `"wireless noise cancelling headphones"`

| Rank | Product | Grade | Rationale |
|------|---------|-------|-----------|
| 1 | Sony WH-1000XM5 | 3 | Exact match |
| 2 | Bose QuietComfort 45 | 3 | Exact match |
| 3 | Sony WH-1000XM4 (older gen) | 2 | Same category, older model |
| 4 | Wired noise-cancelling headphones | 1 | Missing "wireless" |
| 5 | Bluetooth speaker | 0 | Wrong product type |

### NDCG Formula

**DCG at position k:**

```
DCG@k = Σ (rel_i) / log2(i + 1)   for i = 1 to k
```

Where `rel_i` is the relevance grade at rank `i`.

**Ideal DCG (IDCG):** DCG of the perfect ranking (grades sorted descending).

**NDCG:**

```
NDCG@k = DCG@k / IDCG@k
```

### Worked Example

Query: `"wireless noise cancelling headphones"`, grades = [3, 3, 2, 1, 0]

```
DCG@5 = 3/log2(2) + 3/log2(3) + 2/log2(4) + 1/log2(5) + 0/log2(6)
      = 3/1.000 + 3/1.585 + 2/2.000 + 1/2.322 + 0
      = 3.000 + 1.893 + 1.000 + 0.431 + 0
      = 6.324

Ideal grades = [3, 3, 2, 1, 0]  ← already sorted, so IDCG = DCG = 6.324

NDCG@5 = 6.324 / 6.324 = 1.000
```

Now suppose the system ranks them as [3, 2, 1, 3, 0] (grade-3 result slipped to rank 4):

```
DCG@5 = 3/1.000 + 2/1.585 + 1/2.000 + 3/2.322 + 0/2.585
      = 3.000 + 1.262 + 0.500 + 1.292 + 0
      = 6.054

NDCG@5 = 6.054 / 6.324 = 0.957
```

The 4.3% drop in NDCG quantifies the cost of demoting a perfect result.

**Use k=5 or k=10.** E-commerce users rarely scroll past the first page. NDCG@5 is the most actionable cut.

---

## Building a Judgment Set

### Query Selection

Don't use random queries. Stratify by:

| Stratum | Selection method | Suggested share |
|---------|-----------------|-----------------|
| Head queries (top 1% by volume, >80% of traffic) | All of them | 40% |
| Torso queries (1%-10% by volume) | Random sample | 40% |
| Tail queries (bottom 90%) | Random sample, oversample zero-result | 20% |

A judgment set of 300-500 queries is sufficient for most e-commerce platforms. Below 200, variance is too high to detect small improvements.

### Labeling

**Who should label:** Domain experts (merchandisers, category managers) outperform crowdworkers for product search because they know the catalog. For general consumer products, crowdworkers with a clear rubric work.

**Inter-annotator agreement:** Require at least 2 labelers per query-result pair. Compute Cohen's Kappa:

```
κ = (Po - Pe) / (1 - Pe)
```

Where `Po` = observed agreement rate, `Pe` = expected by chance. Target κ ≥ 0.6. Below 0.4 means the grading rubric is ambiguous — fix it before labeling more.

**Refresh cadence:** Re-judge at least 20% of the set every 6 months. Catalog changes (discontinued products, new arrivals) make old judgments stale.

### Minimum Labeled Results per Query

Label at least the top-20 results from the **current system** plus 5-10 randomly sampled from deeper in the results. Without sampling deep results, you'll miss cases where a new system retrieves a highly relevant product the old system never surfaced.

---

## Online Metrics

Offline NDCG and online behavior don't always agree. Both are necessary.

### Primary Metrics

**Zero-result rate (ZRR)**
```
ZRR = (queries returning 0 results) / (total queries)
```
Target: < 5%. Above 10% is an emergency — users are bouncing immediately.

**Click-through rate on first page (CTR@page1)**
```
CTR@page1 = (sessions with ≥1 click on page 1) / (sessions that reached page 1)
```
Target: > 30%. Below 20% means either the result set is irrelevant OR presentation is broken (check images, titles, prices).

**Mean reciprocal rank of first click (MRR)**
```
MRR = (1/N) * Σ (1 / rank_of_first_click_i)
```
MRR = 1.0 means users always click the #1 result. MRR = 0.3 means users frequently skip the top results — a ranking signal.

**Search-to-cart rate**
```
S2C = (sessions with add-to-cart after search) / (sessions with ≥1 search)
```
The ultimate business metric. Moves slower, requires more traffic to detect changes.

### Metric Sensitivity by Change Type

| Change type | ZRR | CTR@page1 | MRR | S2C |
|-------------|-----|-----------|-----|-----|
| Add synonym | High | Medium | Low | Medium |
| Re-rank results | None | Medium | High | Medium |
| Fix spell correction | High | Low | Low | Low |
| Change presentation (images, layout) | None | High | Medium | High |
| Adjust retrieval boosting | Low | Medium | High | Medium |

Use this table to choose which metric to instrument for each experiment.

---

## A/B Testing Search

### The Dilution Problem

Search changes affect all queries simultaneously, but improvements are uneven. A single A/B experiment might:
- Improve head queries (high volume, high confidence)
- Regress rare long-tail queries (low volume, hard to detect)

Aggregate CTR can show +2% while 15% of query types get worse. **Always stratify results by query type** (head / torso / tail) and intent (product / brand / category).

### Minimum Sample Size

For CTR detection:

```
n = 2 * (z_α + z_β)² * p(1-p) / δ²
```

Where:
- `p` = baseline CTR (e.g. 0.30)
- `δ` = minimum detectable effect (e.g. 0.02 absolute, i.e., 30% → 32%)
- `z_α` = 1.96 (α=0.05, two-tailed)
- `z_β` = 0.84 (80% power)

**Worked calculation** for baseline CTR=0.30, MDE=0.02:

```
n = 2 * (1.96 + 0.84)² * 0.30 * 0.70 / 0.02²
  = 2 * 7.84 * 0.21 / 0.0004
  = 2 * 1.646 / 0.0004
  = 8,232 sessions per variant
```

At 10,000 daily search sessions, this experiment needs ~2 days per variant to be powered. Never call an experiment early.

### Interleaving as an Alternative

When traffic is insufficient for traditional A/B tests, **interleaving** is more sensitive:

1. For each search query, merge results from system A and system B, alternating positions (A gets odd ranks, B gets even ranks — or use team-draft interleaving).
2. Measure which system's results get more clicks in the blended list.
3. Declare a winner when the click share is statistically significant.

Interleaving requires 5-10x less traffic than a traditional A/B test for the same statistical power. Trade-off: it measures preference, not absolute CTR impact.

---

## Metric Scorecard Template

Use this after each evaluation cycle to track progress:

```
Evaluation: [date] vs [baseline date]
Judgment set: [N queries, version X.Y]

OFFLINE
  NDCG@5:          0.71 → 0.76  (+7.0%)  ✓
  NDCG@10:         0.68 → 0.72  (+5.9%)  ✓

ONLINE (A/B, N=50k sessions, 14 days)
  Zero-result rate: 8.2% → 5.1%  (-3.1pp) ✓  [target <5%]
  CTR@page1:       27.4% → 29.8% (+2.4pp) ✓  [target >30%, not yet]
  MRR:             0.41  → 0.44  (+7.3%)  ✓
  Search-to-cart:  6.1%  → 6.3%  (+0.2pp) —  [not significant]

STRATIFIED
  Head queries:    NDCG +5.1%
  Torso queries:   NDCG +9.2%
  Tail queries:    NDCG +6.7%
  Zero-result queries resolved: 38 / 92 (41%)

Decision: SHIP — offline and online aligned, no regressions in strata.
```

---

## When Offline and Online Disagree

| Situation | Likely cause | Action |
|-----------|-------------|--------|
| NDCG up, CTR flat | Judgment set is stale or unrepresentative | Re-judge top-failing queries using real click data |
| NDCG flat, CTR up | Presentation change (not relevance) confounding CTR | Isolate presentation from relevance in the experiment |
| NDCG down, CTR up | Judgment set has wrong labels | Audit judgment set against recent user behavior |
| Both down | Real regression | Roll back and diagnose |
| Both up | Genuine improvement | Ship with confidence |

The IRON LAW applies here too: if online metrics are good but offline NDCG is bad, don't trust the win — your judgment set is probably broken. Fix the judgment set first.
