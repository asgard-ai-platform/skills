# Factual Consistency Checking for Abstractive Summaries

Abstractive models generate fluent text that may contain facts absent from — or contradicting — the source document. This reference covers three concrete checking strategies, how to score them, and a decision framework for production use.

---

## The Core Problem

Given:
- **S**: source document (ground truth)
- **H**: hypothesis (the generated summary)

A summary is **factually consistent** if every claim in H is entailed by S. Entailment here is the same concept as in NLI tasks: H does not introduce new facts, does not contradict S, and does not hallucinate numeric values or named entities.

Hallucination types to detect:

| Type | Example |
|------|---------|
| Extrinsic entity | Summary names "CEO John Lee" but source only says "the CEO" |
| Intrinsic negation | Source: "revenue grew"; Summary: "revenue declined" |
| Numeric drift | Source: "Q4 revenue $4.2B"; Summary: "revenue exceeded $5B" |
| Unsupported causal | Source describes correlation; Summary states causation |

---

## Method 1: NLI-Based Sentence-Level Checking

### How It Works

Run an NLI model with the source (or source chunk) as the **premise** and each summary sentence as the **hypothesis**. Collect the entailment score for each sentence.

```
score(H_i) = P(entailment | premise=S, hypothesis=H_i)
```

Aggregate across all summary sentences:

```
consistency_score = (1/n) * Σ score(H_i)   for i in 1..n
```

Flag any sentence where `score(H_i) < threshold` (typically 0.5).

### Worked Example

Source (excerpt):
> "Acme Corp reported Q4 revenue of $4.2B, a 12% increase year-over-year. Operating expenses rose to $3.1B due to increased R&D spending."

Summary to check (sentence by sentence):

| # | Summary sentence | NLI score | Status |
|---|-----------------|-----------|--------|
| 1 | "Acme Corp's Q4 revenue reached $4.2B." | 0.91 | ✓ Entailed |
| 2 | "This represents a 15% year-over-year growth." | 0.12 | ✗ Contradicts (source says 12%) |
| 3 | "Operating costs increased due to R&D investment." | 0.83 | ✓ Entailed |

→ Sentence 2 flagged. Summary is **not fully consistent**.

### Recommended Models

- `cross-encoder/nli-deberta-v3-base` — strong accuracy, ~200M params
- `facebook/bart-large-mnli` — zero-shot NLI via BART
- `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` — multilingual, useful for Chinese/English mixed content

### Code Skeleton

```python
from transformers import pipeline

nli = pipeline("text-classification", model="cross-encoder/nli-deberta-v3-base")

def check_nli(source: str, summary: str, threshold: float = 0.5) -> dict:
    sentences = summary.split(". ")
    results = []
    for sent in sentences:
        if not sent.strip():
            continue
        # NLI premise=source, hypothesis=sentence
        out = nli(f"{source} [SEP] {sent}", truncation=True, max_length=512)
        label = out[0]["label"]
        score = out[0]["score"]
        entail_score = score if label == "entailment" else 1 - score
        results.append({
            "sentence": sent,
            "entailment_score": round(entail_score, 3),
            "flagged": entail_score < threshold
        })
    overall = sum(r["entailment_score"] for r in results) / len(results)
    return {"sentence_results": results, "overall_score": round(overall, 3)}
```

**Limitation**: NLI models have a 512-token limit. For long sources, you must chunk (see §4).

---

## Method 2: QA-Based Consistency (QAEval / QAGS)

### Intuition

If a summary makes a claim, a QA model should be able to answer the same question from the source and get the same answer. Disagreement signals hallucination.

### Procedure

1. **QG step**: Generate questions from the summary using a question-generation (QG) model.
2. **QA from summary**: Answer each question using the summary as context → `ans_H`.
3. **QA from source**: Answer each question using the source as context → `ans_S`.
4. **Compare**: Compute token-level F1 between `ans_H` and `ans_S` for each question.

```
QA_consistency = (1/k) * Σ F1(ans_H_j, ans_S_j)   for j in 1..k
```

### Worked Example

Summary: "Acme Corp's Q4 revenue reached $4.2B, a 15% increase year-over-year."

Generated question: "What was Acme Corp's Q4 revenue growth rate?"

| Source of answer | Answer | 
|-----------------|--------|
| Summary (`ans_H`) | "15%" |
| Source doc (`ans_S`) | "12%" |

Token F1("15%", "12%") = 0.0 → flagged.

### Token-Level F1 (same as SQuAD metric)

```python
from collections import Counter

def token_f1(pred: str, gold: str) -> float:
    pred_tokens = pred.lower().split()
    gold_tokens = gold.lower().split()
    common = Counter(pred_tokens) & Counter(gold_tokens)
    n_common = sum(common.values())
    if n_common == 0:
        return 0.0
    precision = n_common / len(pred_tokens)
    recall = n_common / len(gold_tokens)
    return 2 * precision * recall / (precision + recall)
```

### When to Prefer QA over NLI

- Source document is very long and NLI truncation is lossy
- You specifically care about named entities, numbers, and dates (QA localizes these)
- You have a domain-specific QA model (e.g., finance, medical)

---

## Method 3: Entity-Level Spot Check

The cheapest and most interpretable check. Run NER on both source and summary; flag any named entity in the summary that does not appear in the source.

```
hallucinated_entities = entities(H) - entities(S)
```

Note: surface form matching requires normalization (e.g., "Q4" vs "fourth quarter", "4.2 billion" vs "$4.2B").

### Code Skeleton

```python
import spacy

nlp = spacy.load("en_core_web_sm")

def entity_check(source: str, summary: str) -> dict:
    src_ents = {ent.text.lower() for ent in nlp(source).ents}
    sum_ents = {ent.text.lower() for ent in nlp(summary).ents}
    hallucinated = sum_ents - src_ents
    return {
        "source_entities": sorted(src_ents),
        "summary_entities": sorted(sum_ents),
        "hallucinated_entities": sorted(hallucinated),
        "flagged": len(hallucinated) > 0
    }
```

**Limitation**: Entity extraction is noisy. "John" in the source may not match "John Smith" in the summary, producing a false positive. Use as a first-pass filter, not a final verdict.

---

## Handling Long Sources (Chunking Strategy)

Both NLI and QA approaches have context limits. Two strategies:

### Strategy A: Most-Relevant-Chunk

1. Split source into overlapping chunks (e.g., 400 tokens, 50-token stride).
2. For each summary sentence, retrieve the top-1 chunk by cosine similarity (using a sentence encoder).
3. Run NLI with `premise = top_chunk`, `hypothesis = summary_sentence`.

```python
from sentence_transformers import SentenceTransformer, util

encoder = SentenceTransformer("all-MiniLM-L6-v2")

def get_best_chunk(source_chunks: list[str], sentence: str) -> str:
    src_embs = encoder.encode(source_chunks, convert_to_tensor=True)
    sent_emb = encoder.encode(sentence, convert_to_tensor=True)
    scores = util.cos_sim(sent_emb, src_embs)[0]
    best_idx = scores.argmax().item()
    return source_chunks[best_idx]
```

### Strategy B: Hierarchical NLI

1. Run NLI on each (chunk, summary_sentence) pair.
2. Take `max(entailment_score)` across chunks as the final score.

Rationale: a claim only needs to be supported by *some* part of the source document.

```
score(H_i) = max over chunks c_j of P(entailment | premise=c_j, hypothesis=H_i)
```

---

## Decision Framework

```
Is accuracy critical? (legal, medical, finance)
│
├─ YES
│   ├─ Is source < 512 tokens?  → Use NLI (Method 1)
│   └─ Is source > 512 tokens?  → Use NLI + chunking (Strategy A or B)
│   └─ Also: always run Entity Check (Method 3) as a cheap pre-filter
│
└─ NO (content curation, general summarization)
    └─ Entity Check (Method 3) alone is often sufficient
    └─ QA-based (Method 2) if you have domain QA models available
```

Threshold guidance for NLI consistency score:

| Score | Interpretation | Action |
|-------|---------------|--------|
| ≥ 0.80 | High consistency | Accept |
| 0.60–0.79 | Moderate — some unsupported claims | Human review |
| < 0.60 | Low — likely hallucinations present | Reject / regenerate |

These thresholds are heuristic. Calibrate against a labeled sample from your domain.

---

## Production Integration Pattern

```
[Abstractive Model] → raw_summary
         ↓
[Entity Check]  → fast pre-filter (< 10ms with small NER model)
         ↓ (if entities OK)
[NLI Check]     → sentence-level scores
         ↓
if overall_score ≥ threshold:
    emit summary with consistency_score in metadata
else:
    retry generation with adjusted decoding params
    OR return extractive fallback
    OR flag for human review
```

Retry approach when NLI fails: increase `no_repeat_ngram_size`, decrease `length_penalty`, or reduce `num_beams`. These reduce hallucination in many seq2seq models.

---

## Caveats

- **NLI models are not perfect**: they can themselves be confused by paraphrase, negation, or domain shift. A high entailment score does not guarantee factual correctness — it means the NLI model believes the claim is supported.
- **Domain gap**: NLI models trained on general corpora (MNLI, SNLI) may underperform on specialized domains (finance, medicine). Consider domain-adapted models or few-shot calibration.
- **Factual consistency ≠ completeness**: a summary can be fully consistent yet omit critical information. These checks only verify that what *is* stated is supported; they do not verify what is *missing*.
- **Numeric sensitivity**: token F1 gives partial credit to "12%" vs "15%". Use exact-match for numeric fields if precision matters.
