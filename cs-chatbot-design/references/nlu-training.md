# NLU Training Data Best Practices

## The Core Problem: Intent Classifiers Fail at the Edges

A classifier trained on 10 sanitized examples per intent will hit 90%+ accuracy in your test set and 60% in production. The gap is **distribution mismatch**: your training data reflects how you think users talk, not how they actually talk.

Rule of thumb: **train on the long tail, not the happy path**.

---

## Minimum Viable Training Set

| Intent type | Min examples | Notes |
|-------------|-------------|-------|
| High-traffic (top 5 intents) | 30-50 | These carry the most failure cost |
| Mid-traffic | 15-20 | Standard coverage |
| Low-traffic / edge | 10-15 | Below 10 is unreliable |
| `fallback` / `out_of_scope` | 50-100 | Deliberately diverse; see below |

The `fallback` intent is unlike others: it must cover the **infinite space** of things your bot cannot handle. Train it with varied off-topic inputs — competitor questions, gibberish, questions about unrelated domains — not just one type of "I don't know what this means."

---

## Collecting Real Training Data: A Step-by-Step Procedure

### Step 1 — Mine Existing Logs

If you have any historical data (chat logs, email subjects, support tickets, search queries):

1. Export raw text, strip PII (names, order IDs, phone numbers → replace with placeholders like `[NAME]`, `[ORDER_ID]`)
2. Sample 200-500 messages randomly
3. Label each with an intent — do this in two passes: one person labels, a second person reviews disagreements
4. Calculate **inter-annotator agreement** (Cohen's κ):

```
κ = (P_o - P_e) / (1 - P_e)

P_o = observed agreement (fraction of labels that match)
P_e = expected agreement by chance = Σ(p_i_annotator1 × p_i_annotator2)
```

Target κ ≥ 0.7 before using the data. Below 0.6 means your intent definitions are ambiguous — fix the definitions, not the labels.

### Step 2 — Write Seed Examples

For each intent, write 5-8 seed examples that cover:

| Variation type | Example for `check_order_status` |
|---------------|----------------------------------|
| Direct question | "What's the status of my order?" |
| Short form | "order status" |
| Implicit | "I'm waiting for my package, any updates?" |
| With entity | "Where's order #12345?" |
| Colloquial | "did my stuff ship yet" |
| Polite/formal | "Could you please provide an update on my recent purchase?" |
| Error-tolerant | "waht is statu of my ordr" (typos are real) |

### Step 3 — Augment Systematically

Augmentation multiplies your seed examples. Apply these in order of reliability:

**1. Paraphrase with an LLM (high yield)**

Prompt pattern:
```
Generate 10 alternative phrasings for the utterance: "{seed example}"
Context: A customer service chatbot for an e-commerce platform.
Constraints: Each phrasing must convey the exact same intent. 
Vary formality, length, and phrasing. Output one per line, no numbering.
```

After generating, **review every output** — LLMs introduce subtle intent drift. A paraphrase of "cancel my order" might produce "I want to return my order" which is a different intent (`initiate_return`).

**2. Slot substitution (deterministic)**

Take one example with a named entity, substitute the entity:

```python
template = "Where is order {ORDER_ID}?"
order_ids = ["#12345", "#99001", "my order from last week", "the one I placed yesterday"]
# → 4 new training examples
```

Keep a substitution list per entity type. Do NOT reuse the same 3 examples with only the entity swapped — the classifier learns the template, not the intent.

**3. Back-translation (moderate yield, high diversity)**

Translate to a second language (e.g., Chinese), then back to English. This produces grammatically unusual but semantically correct variations — good for robustness.

Example:
- Original: "Can I cancel my order?"
- Via Chinese: "我可以取消我的訂單嗎？" → "Is it possible to cancel my order?"
- Via Japanese: "注文をキャンセルできますか？" → "Can I cancel the order?"

**4. What NOT to augment with**

- Do not use synonym replacement on function words ("what" → "which") — this produces unnatural text without semantic diversity
- Do not augment your test set, ever
- Do not augment `fallback` — it must stay diverse by construction, not by transformation of a few seeds

### Step 4 — Split Correctly

```
Total labeled data → 70% train / 15% dev / 15% test

- Test set: locked; only evaluated at the end; never used to tune
- Dev set: used during development to check progress
- Train set: all augmented data goes here
```

**Stratify by intent** so each split has proportional class representation. If you have 200 examples of `check_order_status` and 20 of `change_shipping_address`, a random split might put 0 examples of the rare intent in dev.

```python
from sklearn.model_selection import train_test_split

# Stratified split
train, temp = train_test_split(df, test_size=0.30, stratify=df['intent'], random_state=42)
dev, test   = train_test_split(temp, test_size=0.50, stratify=temp['intent'], random_state=42)
```

---

## Intent Boundary Definition

The hardest NLU problem is not "classify the clear cases" — it's "what do we do with the ambiguous cases?"

### Ambiguity Decision Framework

When two intents overlap, choose one of:

| Situation | Resolution |
|-----------|-----------|
| User intent is always the same action | Merge into one intent |
| User intent differs but triggers same bot response | Keep separate for analytics, merge for routing |
| Intent depends on a slot value | Use one intent + extract the distinguishing slot |
| Genuinely different user goals | Keep separate, add training examples that highlight the difference |

**Worked example: `check_order_status` vs `track_shipment`**

Ambiguous case: "Where is my package?" — is the user asking for order status or shipment tracking?

Decision: These have different system actions (one queries the OMS, one queries the carrier API). Keep separate. The distinguishing signal is:
- "order status" → questions about processing, payment, fulfillment
- "track shipment" → questions about delivery location, carrier, ETA

Add contrastive examples to both intents:
```
check_order_status: "Has my order been processed?", "Is it shipped yet?"
track_shipment: "Where is my package right now?", "What's the tracking number?", "When will it arrive?"
```

### The Inclusion Test

Before adding an example to an intent, ask: **if the bot acts on this intent, will the user feel understood?**

"I want to destroy my account" → intent: `delete_account` ✓  
"I'm so frustrated with this order" → intent: `delete_account` ✗ (emotional venting, should route to `express_frustration` or `fallback`)

---

## Evaluating NLU Quality

### Per-Intent Metrics

For each intent, compute:

```
Precision_i = TP_i / (TP_i + FP_i)
Recall_i    = TP_i / (TP_i + FN_i)
F1_i        = 2 × (Precision_i × Recall_i) / (Precision_i + Recall_i)
```

Report **macro-averaged F1** (average F1 across all intents, unweighted) alongside **weighted F1** (weighted by class frequency). A high weighted F1 can hide a broken low-traffic intent.

Target thresholds:

| Metric | Minimum | Healthy |
|--------|---------|---------|
| Macro F1 | 0.75 | > 0.85 |
| Recall on `fallback` | 0.70 | > 0.80 |
| Precision on high-traffic intents | 0.85 | > 0.92 |

### Confusion Matrix Analysis

Generate a confusion matrix. The useful signal is not the diagonal — it's the **off-diagonal concentrations**. A cluster of misclassifications between two intents tells you:

1. The intents may need merging (if the confusion is symmetric and frequent)
2. You need contrastive training examples (if one intent is "stealing" from another)
3. Your intent definitions are ambiguous (if human annotators also disagree on these)

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_true, y_pred, labels=intent_list)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=intent_list)
disp.plot(xticks_rotation=45)
plt.tight_layout()
plt.savefig("confusion_matrix.png")
```

### Confidence Calibration

A classifier that outputs 90% confidence but is right only 70% of the time is **overconfident** — dangerous because your dialogue manager trusts that score.

Check calibration with a reliability diagram:

1. Bucket predictions by confidence: [0.5-0.6), [0.6-0.7), ..., [0.9-1.0]
2. For each bucket, compute actual accuracy
3. Plot confidence (x) vs accuracy (y) — a well-calibrated model produces a diagonal line

If your model is systematically overconfident, apply temperature scaling:

```python
# Logits before softmax
scaled_logits = logits / temperature  # temperature > 1 softens the distribution

# Find optimal temperature on the dev set using NLL minimization
from scipy.optimize import minimize_scalar

def nll(T):
    scaled = logits_dev / T
    probs = softmax(scaled)
    return -np.mean(np.log(probs[np.arange(len(y_dev)), y_dev] + 1e-9))

result = minimize_scalar(nll, bounds=(0.5, 5.0), method='bounded')
best_temperature = result.x
```

---

## Handling Low-Resource Intents

Some intents cannot accumulate 15+ examples because they're rare in the wild (e.g., `report_fraud`, `request_accessibility_accommodation`).

### Few-Shot Strategies

**Option A: Zero-shot with embedding similarity**

Represent each intent by the average embedding of its 3-5 examples. Classify by nearest centroid:

```python
# Using sentence-transformers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Build intent centroids
centroids = {}
for intent, examples in training_data.items():
    embeddings = model.encode(examples)
    centroids[intent] = embeddings.mean(axis=0)

def classify(utterance, threshold=0.6):
    vec = model.encode([utterance])[0]
    scores = {k: cosine_similarity(vec, v) for k, v in centroids.items()}
    best_intent = max(scores, key=scores.get)
    if scores[best_intent] < threshold:
        return 'fallback', scores[best_intent]
    return best_intent, scores[best_intent]
```

**Option B: Escalate to LLM for low-confidence cases**

Use your primary classifier as a first pass. If confidence < threshold, pass to an LLM with a constrained prompt:

```
System: You are classifying customer service intents. 
Respond ONLY with one of: [check_order_status, cancel_order, report_fraud, 
change_address, fallback].

User message: "{utterance}"
Intent:
```

This hybrid approach keeps costs low (LLM only sees ~15% of traffic) while handling rare intents correctly.

---

## Active Learning Loop (Production)

After launch, use production traffic to improve your model continuously:

```
Week 1-2: Deploy → collect logs → tag fallback triggers
Week 3:   Review failed conversations → identify missing intents
Week 4:   Add 15 examples for each new intent → retrain → A/B test
Repeat
```

Specifically:

1. **Sample 50 random conversations per week** (not just failures — failures are biased toward edge cases)
2. **Review all `fallback` triggers** — each is a training opportunity
3. **Flag low-confidence correct predictions** (confidence 0.5-0.7, correct outcome) — these are near the decision boundary and most informative for retraining
4. **Never add data without re-evaluating on your locked test set** — "improvement" that degrades a different intent is not an improvement

### Annotation Workflow for Production Logs

```
Raw log message
    ↓
[Auto-label with current model + confidence score]
    ↓
Confidence > 0.85? → Add to training pool (no human review needed)
Confidence 0.6-0.85? → Human review queue (verify label)
Confidence < 0.6? → Human label queue (relabel from scratch)
    ↓
[Reviewed data] → Merge into training set → Retrain monthly
```

---

## Common Training Data Mistakes

**1. Mirror data**: All your examples are grammatically perfect because you wrote them at a desk. Real users type "wher is my order", "pls hlep order wrong item", "???". Add at least 20% colloquial/error-prone examples per intent.

**2. Entity leakage**: You train `check_order_status` with "Where is order #12345?" and the model learns to fire this intent only when an order ID is present. Test with "I ordered something last week, any update?" — no entity, same intent.

**3. Polarity blindness**: "I want to cancel my order" and "I do NOT want to cancel my order" have identical bag-of-words representations. Include negation examples explicitly.

**4. Dataset drift**: You collected training data in Q1, but in Q3 you launched a new product line. Users now say "my subscription" and "my bundle" — phrases your model has never seen. Schedule a training data refresh every 6 months minimum.

**5. Over-fitting to the test set**: If you evaluate on your test set more than 3-4 times during development, you have implicitly tuned to it. Split off a final holdout set that you evaluate exactly once before go-live.
