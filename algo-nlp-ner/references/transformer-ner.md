# Fine-Tuning Transformers for NER

## Architecture: Token Classification Head

A transformer NER model is a standard pretrained encoder (BERT, RoBERTa, XLM-RoBERTa) with a linear classification head on top of each token's hidden state:

```
Input tokens  →  Transformer encoder  →  [H₁, H₂, ..., Hₙ]  →  Linear(d_model, num_labels)  →  Logits
```

Each token produces independent logits over the label set. The label set uses IOB2 (BIO) encoding — see `references/bio-annotation.md` for the tagging scheme.

For a model with `d_model = 768` and labels `{O, B-PER, I-PER, B-ORG, I-ORG, B-LOC, I-LOC, B-DATE, I-DATE}` (9 labels), the head is a `768 × 9` weight matrix applied per token.

**Loss function**: Cross-entropy over token-level predictions, averaged across all non-padding tokens.

```python
loss = CrossEntropyLoss(ignore_index=-100)(logits.view(-1, num_labels), labels.view(-1))
```

Tokens with `label = -100` are masked from loss — used for subword continuation tokens and `[CLS]`/`[SEP]` special tokens.

---

## The Subword Alignment Problem

This is the single most common source of bugs when fine-tuning NER.

BERT tokenizers split words into subword pieces:

```
"Taipei" → ["Tai", "##pei"]           # 2 subword tokens, 1 word-level label
"Cook"   → ["Cook"]                   # 1 subword token, 1 word-level label
"unwanted" → ["un", "##want", "##ed"] # 3 subword tokens, 1 word-level label
```

Your BIO annotations are at **word level**. Your model receives **subword tokens**. You must align them.

### Alignment Strategy: Label First Subword, Mask the Rest

```
Word:     "Taipei"     Label: B-LOC
Subwords: ["Tai", "##pei"]
→ Labels: [B-LOC, -100]    # only first subword gets real label
```

This is the standard approach used by Hugging Face's `TokenClassificationPipeline`. The alternative (propagating I- labels to continuation subwords) degrades boundary detection.

### Code: Tokenize and Align

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

def tokenize_and_align_labels(examples, label2id, max_length=512):
    tokenized = tokenizer(
        examples["tokens"],          # list of word lists
        truncation=True,
        is_split_into_words=True,    # CRITICAL: tell tokenizer words are pre-split
        max_length=max_length,
        padding="max_length",
    )

    all_labels = []
    for i, word_labels in enumerate(examples["ner_tags"]):
        word_ids = tokenized.word_ids(batch_index=i)
        aligned = []
        prev_word_id = None
        for word_id in word_ids:
            if word_id is None:          # [CLS], [SEP], [PAD]
                aligned.append(-100)
            elif word_id != prev_word_id:  # first subword of new word
                aligned.append(label2id[word_labels[word_id]])
            else:                          # continuation subword
                aligned.append(-100)
            prev_word_id = word_id
        all_labels.append(aligned)

    tokenized["labels"] = all_labels
    return tokenized
```

**Verify alignment is working**: print `zip(tokenizer.convert_ids_to_tokens(input_ids), labels)` and manually inspect that `B-` labels land on the first piece of each entity token.

---

## Model Selection Decision Table

| Condition | Recommended model | Why |
|-----------|------------------|-----|
| English, general domain | `bert-base-cased` or `roberta-base` | Casing matters for NER (PER/ORG are often capitalized) |
| English, high accuracy | `roberta-large` | +2-3 F1 over base but 3× slower inference |
| Multilingual | `xlm-roberta-base` | Strong cross-lingual transfer; covers 100 languages |
| Chinese | `bert-base-chinese` or `hfl/chinese-roberta-wwm-ext` | Whole-word masking helps with Chinese NER |
| Domain-specific (biomedical) | `dmis-lab/biobert-base-cased-v1.2` | Domain pretraining; DrugName/Gene entities |
| Low-resource (<500 examples) | `bert-base-cased` + early stopping | Smaller models overfit less |
| Production latency < 50ms | `distilbert-base-cased` | 60% size, ~97% NER quality |

**Rule**: Always start with the pretrained model closest to your domain. Do not start with `bert-base-uncased` for NER — casing is a strong signal for entity detection.

---

## Training Configuration

### Hyperparameters (concrete starting point)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Learning rate | `2e-5` | Safe default; sweep `[1e-5, 2e-5, 5e-5]` if time allows |
| Batch size | 16 | Per device; 32 if memory allows |
| Epochs | 3–5 | Use early stopping on validation F1 |
| Warmup ratio | 0.1 | 10% of steps for linear warmup |
| Weight decay | 0.01 | L2 regularization on non-bias params |
| Max length | 512 | Truncate long docs; use sliding window for longer |
| Scheduler | Linear decay | After warmup, linear decay to 0 |

These values come from the original BERT paper and are robust across most NER datasets. The learning rate is the most sensitive — 5e-5 can cause catastrophic forgetting with small datasets.

### Training Script (Hugging Face Trainer)

```python
from transformers import (
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
    DataCollatorForTokenClassification,
)
import evaluate
import numpy as np

model = AutoModelForTokenClassification.from_pretrained(
    "bert-base-cased",
    num_labels=len(label2id),
    id2label=id2label,
    label2id=label2id,
)

data_collator = DataCollatorForTokenClassification(tokenizer)

seqeval = evaluate.load("seqeval")

def compute_metrics(eval_preds):
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)

    true_labels, true_preds = [], []
    for pred_seq, label_seq in zip(predictions, labels):
        true_labels.append([id2label[l] for l in label_seq if l != -100])
        true_preds.append([
            id2label[p] for p, l in zip(pred_seq, label_seq) if l != -100
        ])

    results = seqeval.compute(predictions=true_preds, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall":    results["overall_recall"],
        "f1":        results["overall_f1"],
    }

training_args = TrainingArguments(
    output_dir="./ner-model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    num_train_epochs=5,
    weight_decay=0.01,
    warmup_ratio=0.1,
    fp16=True,          # speed; disable if on CPU
    logging_steps=50,
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()
```

---

## Data Requirements by Scenario

### Minimum Viable Dataset

| Entity types | Minimum annotated examples | Recommended |
|-------------|---------------------------|-------------|
| 1–2 standard types (PER, ORG) | 200 sentences | 500 |
| 3–5 mixed types | 500 sentences | 1,000–2,000 |
| Custom domain entities (drug names, product SKUs) | 800 sentences | 2,000+ |

"Annotated examples" = sentences containing at least one entity of each type. A dataset with 2,000 sentences but only 50 DATE mentions will produce weak DATE recall.

### Entity Distribution Check

Before training, count entity occurrences per type:

```python
from collections import Counter

entity_counts = Counter()
for sentence in train_data:
    for tag in sentence["ner_tags"]:
        if tag.startswith("B-"):
            entity_counts[tag[2:]] += 1

print(entity_counts)
# Counter({'ORG': 840, 'PER': 612, 'LOC': 488, 'DATE': 91})  ← DATE is underrepresented
```

If any entity type has fewer than 100 B- occurrences in training, expect F1 < 0.70 for that type. Either annotate more, or remove that type and handle it with rules/regex.

---

## Evaluation: Entity-Level vs Token-Level

Always use **entity-level (span-level) F1**, not token-level accuracy. Token accuracy is misleading because `O` tokens dominate most NER corpora.

### seqeval Scoring

The `seqeval` library (used above) implements CoNLL-style entity-level evaluation:

- **Exact match**: both the entity type AND the full span must be correct
- Partial span matches count as false positives AND false negatives

Example:
```
Gold:      [Tim Cook]/PER announced
Predicted: [Tim]/PER [Cook]/PER announced

→ 2 false positives, 1 false negative, 0 true positives for PER
   F1 for this example = 0.0
```

This is why boundary errors are so costly. Check boundary errors separately:

```python
def boundary_only_f1(true_spans, pred_spans):
    """Ignore entity type; only check span boundaries."""
    true_set = {(s, e) for s, e, _ in true_spans}
    pred_set = {(s, e) for s, e, _ in pred_spans}
    tp = len(true_set & pred_set)
    precision = tp / len(pred_set) if pred_set else 0
    recall = tp / len(true_set) if true_set else 0
    f1 = 2*precision*recall / (precision+recall) if (precision+recall) else 0
    return {"boundary_precision": precision, "boundary_recall": recall, "boundary_f1": f1}
```

If `boundary_f1` >> `seqeval_f1`, your model has good span detection but type confusion (common for PER/ORG). If `boundary_f1` ≈ `seqeval_f1`, boundary detection is the problem.

---

## Inference: Aggregating Subword Predictions Back to Words

At inference time you need to reverse the alignment:

```python
from transformers import pipeline

ner_pipeline = pipeline(
    "token-classification",
    model="./ner-model",
    aggregation_strategy="first",  # use first subword's prediction for the word
)

results = ner_pipeline("Tim Cook announced that Apple will open a store in Taipei.")
# [{"entity_group": "PER", "word": "Tim Cook", "start": 0, "end": 8, "score": 0.98},
#  {"entity_group": "ORG", "word": "Apple",    "start": 24, "end": 29, "score": 0.97},
#  {"entity_group": "LOC", "word": "Taipei",   "start": 50, "end": 56, "score": 0.96}]
```

`aggregation_strategy` options:
- `"first"` — use first subword's label (standard; matches training alignment)
- `"average"` — average subword logits before argmax (slightly more robust for long words)
- `"max"` — use highest-confidence subword (can help with ambiguous tokens)

For production, `"first"` is the correct choice because it matches the training objective.

---

## Long Document Handling

BERT-family models have a 512-token limit. For longer documents, use a sliding window:

```python
def ner_long_document(text, pipeline, window=400, stride=50):
    """
    Process long text with overlapping windows.
    window: tokens per chunk
    stride: overlap between consecutive chunks
    """
    words = text.split()
    results = []
    seen_spans = set()

    for start in range(0, len(words), window - stride):
        chunk = " ".join(words[start:start + window])
        chunk_results = pipeline(chunk)

        for entity in chunk_results:
            # Adjust character offsets to global positions
            global_start = len(" ".join(words[:start])) + (1 if start > 0 else 0) + entity["start"]
            global_end = global_start + (entity["end"] - entity["start"])
            span_key = (global_start, global_end, entity["entity_group"])

            if span_key not in seen_spans:
                seen_spans.add(span_key)
                results.append({**entity, "start": global_start, "end": global_end})

    return sorted(results, key=lambda x: x["start"])
```

Entities in the overlap zone may be detected twice — deduplicate by span key.

---

## Common Failure Modes and Fixes

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| F1 < 0.50 overall | Domain mismatch (IRON LAW) | Switch to domain-specific pretrained model or annotate domain data |
| Good PER/ORG, poor DATE | Too few DATE examples in training | Augment DATE annotations; add regex postprocessing for common date formats |
| High precision, low recall | Model too conservative; misses entities | Lower decision threshold; check if entities appear in `O`-heavy context |
| High recall, low precision | Model over-triggers | Check for annotation inconsistencies; add negative examples |
| Entities split across boundaries | Boundary detection failure | Review BIO annotation; check tokenization alignment code |
| Good val F1, poor production F1 | Distribution shift | Annotate from production data; check preprocessing differences |
| `[UNK]` tokens in output | Tokenizer vocab mismatch | Use cased model for cased text; check domain-specific terms |

---

## Reinforcing the IRON LAW

Domain mismatch is the dominant failure mode, not model architecture or hyperparameter choice.

A `bert-base-cased` model fine-tuned on 500 in-domain examples consistently outperforms `roberta-large` applied out-of-the-box on domain-specific entities. Before requesting more data or a larger model, always:

1. Run the target model on 20 held-out sentences from YOUR domain
2. Manually inspect errors
3. Categorize errors: boundary errors, type confusion, or missing entities (recall failures)

If most errors are "missing entities" (recall failures), the model has never seen that entity form — you need domain training data, not a larger model.
