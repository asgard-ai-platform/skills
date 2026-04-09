# Advanced LDA Variants

Standard LDA has two critical assumptions that break in practice:

1. **Static topics** — topic-word distributions are fixed across the entire corpus lifetime
2. **Independent topics** — topics are drawn from a Dirichlet prior that treats them as exchangeable and uncorrelated

When either assumption fails, use one of the models below.

---

## Decision Table: Which Model to Use

| Corpus Characteristic | Symptom in Standard LDA | Recommended Model |
|---|---|---|
| Documents span multiple time periods | "Finance" topic mixes 2008 crisis vocabulary with 2023 AI-era vocabulary | Dynamic Topic Model (DTM) |
| Topics cluster together naturally (e.g., "ML" and "Statistics" co-occur) | Dirichlet prior forces topics apart; coherent subtopics won't emerge | Correlated Topic Model (CTM) |
| Documents are short (tweets, titles) | 80%+ documents get assigned K=1 topic with near-certainty | Biterm Topic Model (BTM) or Sparse LDA |
| Hierarchical categories expected | Flat K topics fail to capture sub-topics | Hierarchical Dirichlet Process (HDP) |
| Author/source metadata available | Topics blend across known source boundaries | Author-Topic Model |

---

## Dynamic Topic Model (DTM)

### When to Use

Use DTM when your corpus spans distinct time slices (years, quarters, months) and you expect topic vocabulary to drift. Example: a 10-year news archive where "virus" shifts from biology articles to COVID coverage.

### Core Idea

DTM chains LDA across time slices t = 1, …, T. The topic-word distribution β_{k,t} for topic k at time t evolves from the previous slice via a Gaussian random walk in the natural parameter space:

```
β_{k,t} | β_{k,t-1} ~ N(β_{k,t-1}, σ²I)
```

The document-topic distribution α_t also evolves over time, but each document still generates word tokens via the standard LDA generative process conditioned on its time slice.

### Generative Process (per document d in slice t)

```
1. θ_d ~ Dirichlet(α_t)                 ← document-topic proportions
2. For each word position i in doc d:
   a. z_i ~ Categorical(θ_d)            ← draw topic assignment
   b. w_i ~ Categorical(softmax(β_{z_i, t})) ← draw word from topic at time t
```

### Hyperparameters

| Parameter | Meaning | Default Starting Point |
|---|---|---|
| K | Number of topics | Same as standard LDA; use coherence across slices |
| σ² | Evolution variance | 0.005–0.05; smaller = slower drift |
| Time granularity | Size of each slice | Quarter or year; avoid slices with <100 documents |

**Critical:** if a time slice has too few documents, DTM has insufficient evidence to estimate β_{k,t} reliably. The Gaussian prior will dominate and β_{k,t} ≈ β_{k,t-1}. Minimum practical slice size: ~200 documents.

### Worked Example: Tracking "AI" Topic Over 5 Years

Suppose K=10 and topic 3 is identified as "artificial intelligence". Top words per slice:

| Year | Top 5 Words for Topic 3 |
|---|---|
| 2018 | neural, network, deep, learning, GPU |
| 2019 | BERT, transformer, language, model, pretraining |
| 2020 | GPT, generation, fine-tune, few-shot, prompt |
| 2021 | ChatGPT, instruction, alignment, RLHF, safety |
| 2022 | LLM, agent, reasoning, multimodal, hallucination |

This drift is impossible to capture with standard LDA, which would merge all years into one blurry topic.

### Implementation Note (Python / gensim)

Gensim ships `LdaSeqModel` which implements DTM:

```python
from gensim.models import LdaSeqModel
from gensim.corpora import Dictionary

# corpus_slices: list of lists of (word_id, count) tuples, one per time slice
# time_slice: list of integers, doc count per slice
# e.g., time_slice = [300, 420, 510] for 3 slices

model = LdaSeqModel(
    corpus=corpus_slices,
    id2word=dictionary,
    time_slice=time_slice,
    num_topics=10,
    chunksize=1,       # DTM is slow; reduce if memory-constrained
    passes=10,
)

# Top words for topic 2 at time slice 1 (index 0-based)
model.print_topic(2, time=1, top_terms=10)
```

**Warning:** `LdaSeqModel` uses variational inference approximation, not the original DTM Kalman filter. It is faster but less accurate for detecting subtle drift. For production use, consider the original DTM implementation by Blei & Lafferty (available as a C binary).

---

## Correlated Topic Model (CTM)

### When to Use

Use CTM when you expect topic co-occurrence structure. Standard LDA uses a Dirichlet prior over θ_d, which cannot represent positive or negative correlations between topics. CTM replaces the Dirichlet with a logistic-normal distribution, allowing a full covariance matrix Σ over topics.

### Core Idea

```
η_d ~ N(μ, Σ)                       ← draw from K-dimensional Gaussian
θ_d = softmax(η_d)                   ← project to simplex
```

The covariance matrix Σ captures:
- **Positive correlation** (Σ_{ij} > 0): topics i and j tend to co-appear in the same document
- **Negative correlation** (Σ_{ij} < 0): topics i and j rarely co-appear

### Output: Topic Correlation Matrix

CTM produces an estimated Σ (or correlation matrix derived from it). This is the key value-add over standard LDA:

```
Topic Correlation Matrix (example, 5 topics):
             Finance  Tech  Politics  Sports  Health
Finance      1.00     0.42  0.15     -0.31   0.08
Tech         0.42     1.00  0.10     -0.18   0.22
Politics     0.15     0.10  1.00      0.05   0.33
Sports      -0.31    -0.18  0.05      1.00  -0.12
Health       0.08     0.22  0.33     -0.12   1.00
```

Interpretation: Finance and Tech positively correlated (business tech articles), Finance and Sports negatively correlated (distinct audiences).

### Worked Example: When CTM Beats LDA

Corpus: 5000 academic papers from arXiv, mixed CS/Statistics.

- **LDA result**: Topic 4 = {neural, network, gradient, activation, layer}, Topic 7 = {regression, coefficient, variance, estimator, likelihood}. Topics appear isolated.
- **CTM result**: Same topics, but Σ_{4,7} = 0.61, revealing that papers on neural networks frequently also discuss statistical estimation — which is true for the ML theory literature. This correlation is invisible to LDA.

### Inference Caveat

CTM uses mean-field variational inference (Laplace approximation over the logistic-normal). The covariance Σ is estimated from the corpus but the estimation is approximate. For small corpora (<1000 documents), Σ estimates are noisy. Do not over-interpret weak correlations (|Σ_{ij}| < 0.15).

### Implementation Note

Gensim does not ship CTM. Options:

```python
# Option 1: Use tomotopy (faster, C++ backend)
import tomotopy as tp

model = tp.CTModel(k=10, seed=42)
for doc in preprocessed_docs:
    model.add_doc(doc)

model.train(iter=1000, workers=4)

# Access correlation
import numpy as np
covar = np.array(model.get_correlations())
```

```python
# Option 2: scikit-learn LDA as baseline, then switch to tomotopy CTM
# tomotopy install: pip install tomotopy
```

---

## Biterm Topic Model (BTM) — Short Text Remedy

Short documents (< 20 words) cause LDA to fail because there is not enough within-document word co-occurrence to estimate θ_d reliably. BTM models topics at the **biterm** (word pair) level rather than document level.

### Core Difference

| | Standard LDA | BTM |
|---|---|---|
| Unit of analysis | Document | Biterm (w_i, w_j) |
| Topic assignment | Per word in a document | Per biterm across whole corpus |
| Min viable doc length | ~50 words | ~5 words |
| Corpus assumption | Each document has its own mixture | Whole corpus shares one global mixture θ |

### When BTM Applies

- Twitter / social media posts
- Product review titles
- Search query logs
- Customer support one-liners

**Limitation:** BTM assumes a single global topic mixture θ for the entire corpus. It cannot model per-document topic proportions. All documents are treated as samples from the same mixture — appropriate for short-text streams, wrong for a diverse long-document corpus.

---

## Hierarchical Dirichlet Process (HDP) — Non-parametric K

HDP removes the need to specify K in advance. It uses a Dirichlet process prior that lets the model infer the number of topics from data.

### When to Use

Use HDP only when you genuinely do not have a prior on K and the corpus is large enough to support inference (>5000 documents). For smaller corpora, coherence-guided K selection (see `references/topic-evaluation.md`) is more reliable.

### Practical Behavior

HDP does not produce a clean K. It produces a "truncated" topic count where many topics have near-zero weight. In practice:

1. Run HDP
2. Observe the weight distribution over topics
3. Threshold: keep only topics where average document-topic weight > 0.01
4. This effective K is your answer

**Common outcome:** HDP with a 10K-document corpus "finds" 40 topics internally but only 12 have non-trivial weight. Use those 12.

```python
from gensim.models import HdpModel

hdp = HdpModel(corpus, id2word=dictionary, random_state=42)

# Get topics above weight threshold
topics = hdp.show_topics(num_topics=20, formatted=False)
# Filter by coherence or weight in post-processing
```

**IRON LAW applies here too:** HDP does not magically discover the "true" K. It provides a data-driven starting point, but the final number of meaningful topics still requires human inspection. HDP frequently over-splits coherent topics into near-duplicate subtopics.

---

## Author-Topic Model

When your corpus has known author metadata, standard LDA ignores a powerful signal. The Author-Topic Model adds an author layer:

```
Generative process:
1. Each author a has a distribution over topics: θ_a ~ Dirichlet(α)
2. For each word in doc d (authored by set A_d):
   a. Sample an author x ~ Uniform(A_d)
   b. Sample topic z ~ θ_x
   c. Sample word w ~ φ_z
```

This produces **author-topic distributions** rather than document-topic distributions. Useful for:
- Academic citation networks (find an author's research themes)
- Journalism analysis (what topics does each reporter cover?)
- Customer segmentation by reviewer patterns

---

## Choosing Between Models: Flowchart

```
Does your corpus span multiple time periods?
├── YES → Does vocabulary drift matter? (e.g., "AI" means different things in 2018 vs 2023)
│          ├── YES → Dynamic Topic Model (DTM)
│          └── NO  → Standard LDA with time as a document-level metadata field
└── NO
    ├── Are documents very short (< 20 words on average)?
    │    ├── YES → Biterm Topic Model (BTM)
    │    └── NO
    │         ├── Do you expect topic co-occurrence patterns to matter?
    │         │    ├── YES → Correlated Topic Model (CTM)
    │         │    └── NO
    │         │         ├── Do you have author/source metadata?
    │         │         │    ├── YES → Author-Topic Model
    │         │         │    └── NO
    │         │         │         └── Is K truly unknown and corpus large (>5K docs)?
    │         │         │              ├── YES → HDP (then threshold topics)
    │         │         │              └── NO  → Standard LDA + coherence K selection
```

---

## Shared Gotchas Across All Variants

- **DTM requires balanced slices.** A slice with 20 documents will have unreliable β estimates; the model will inherit β from the adjacent slice by default. Either merge small slices or assign documents to the nearest well-populated slice.
- **CTM correlation is corpus-specific.** The Σ matrix describes co-occurrence in THIS corpus. Topic A correlating with topic B does not mean they are semantically related — they may co-occur due to a corpus-specific bias (e.g., all documents come from one publication that covers both topics).
- **None of these models auto-label topics.** Regardless of which variant you use, topic labels remain a human judgment task. The word distributions are the raw output; you must interpret them.
- **Reproducibility across variants.** All Gibbs/variational methods are stochastic. DTM and CTM are particularly sensitive to initialization. Run each at least 3 times with different seeds and check if the top-5 words per topic are stable.
- **Do not mix these models with TF-IDF weighting.** All LDA variants expect raw term counts (bag-of-words integers). Passing normalized TF-IDF floats will produce incorrect inference because the generative model assumes integer word tokens.
