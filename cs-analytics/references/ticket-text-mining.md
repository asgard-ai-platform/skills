# Ticket Text Mining

Reference for `cs-analytics` — expands on the **Text Mining on Tickets** workflow.

---

## When to Use Which Method

| Goal | Method | Why |
|------|--------|-----|
| "What are the top complaint phrases this week?" | TF-IDF keyword extraction | Fast, interpretable, no training needed |
| "Cluster 10k tickets into topics automatically" | LDA or BERTopic | Unsupervised, handles large volumes |
| "Detect issues emerging in the last 7 days" | Volume spike on TF-IDF terms | Lightweight, auditable |
| "Is this ticket angry or neutral?" | Lexicon-based sentiment or fine-tuned classifier | Depends on available labeled data |
| "Classify new tickets into known categories" | Supervised classifier (fine-tuned embedding) | Requires ~200+ labeled examples per category |

Start with TF-IDF. Graduate to BERTopic only when ticket volume exceeds ~5k/month and manual category review becomes impractical.

---

## Step 1 — Preprocessing Pipeline

Apply in this exact order. Skipping deduplication inflates counts; skipping normalization fragments the same term into multiple variants.

```python
import re
from collections import Counter

STOP_WORDS = {
    # Generic
    "i", "we", "my", "the", "a", "an", "is", "was", "are", "were",
    "please", "thank", "thanks", "hi", "hello", "dear", "regards",
    # CS-specific noise
    "ticket", "order", "issue", "problem", "help", "need",
    "contact", "support", "team", "customer", "service",
}

def preprocess(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"#\d+", "", text)           # remove ticket IDs
    text = re.sub(r"\S+@\S+", "", text)        # remove emails
    text = re.sub(r"https?://\S+", "", text)   # remove URLs
    text = re.sub(r"[^a-z\s]", " ", text)      # keep only letters
    tokens = text.split()
    tokens = [t for t in tokens if len(t) > 2 and t not in STOP_WORDS]
    return tokens
```

**For Traditional Chinese tickets**, replace the regex step with jieba or ckip-transformers segmentation, then apply a stopword list (`的`, `了`, `是`, `我`, `您`, `請`, `問題`, `訂單` — mirror the English list above).

---

## Step 2 — TF-IDF Keyword Extraction

### Formula

```
TF(t, d)  = count of term t in document d / total tokens in d
IDF(t)    = log(N / df(t))   where N = corpus size, df(t) = docs containing t
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

### Worked Example

Corpus of 5 tickets (N = 5). Term `"refund"` appears in 3 docs → `IDF = log(5/3) = 0.51`.

In ticket #1042 (80 tokens), `"refund"` appears 4 times:
```
TF     = 4 / 80     = 0.050
TF-IDF = 0.050 × 0.51 = 0.026
```

Term `"order"` appears in every ticket → `IDF = log(5/5) = 0`. TF-IDF = 0 regardless of frequency. This is why generic words self-suppress.

### Weekly Top-Phrase Report (corpus = all tickets this week)

```python
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def top_phrases(tickets: list[str], n=20) -> pd.DataFrame:
    """
    tickets: list of raw ticket texts
    returns: DataFrame with phrase and mean tfidf score
    """
    vectorizer = TfidfVectorizer(
        preprocessor=lambda t: " ".join(preprocess(t)),
        ngram_range=(1, 3),   # unigrams + bigrams + trigrams
        min_df=3,             # ignore phrases in < 3 tickets
        max_df=0.6,           # ignore phrases in > 60% of tickets
    )
    matrix = vectorizer.fit_transform(tickets)
    scores = matrix.mean(axis=0).A1
    vocab = vectorizer.get_feature_names_out()
    return (
        pd.DataFrame({"phrase": vocab, "score": scores})
        .sort_values("score", ascending=False)
        .head(n)
        .reset_index(drop=True)
    )
```

**Sample output** for 800 tickets over 7 days:

| # | phrase | score |
|---|--------|-------|
| 1 | shipping delay | 0.089 |
| 2 | wrong item received | 0.071 |
| 3 | refund not processed | 0.063 |
| 4 | account locked | 0.058 |
| 5 | promo code not working | 0.044 |

These five phrases already tell you where to focus process improvement.

---

## Step 3 — Topic Modeling with BERTopic

Use when you need stable topic clusters across months, not just this week's keywords.

### Setup

```bash
pip install bertopic sentence-transformers umap-learn hdbscan
```

```python
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

def build_topic_model(tickets: list[str]):
    embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    # Multilingual model handles English + Chinese mixed tickets

    topic_model = BERTopic(
        embedding_model=embedding_model,
        min_topic_size=15,        # minimum 15 tickets per topic
        nr_topics="auto",
        calculate_probabilities=False,
    )
    topics, _ = topic_model.fit_transform(tickets)
    return topic_model, topics
```

### Interpreting BERTopic Output

```python
topic_model.get_topic_info()
# Returns: Topic | Count | Name | Representation
#   -1     |  87  | Outliers | —
#    0     | 320  | shipping_delay_carrier | [shipping, delay, carrier, ...]
#    1     | 210  | refund_process_bank    | [refund, bank, processed, ...]
```

Topic `-1` is the outlier bin — unclustered tickets. If outlier count exceeds 30% of corpus, either lower `min_topic_size` or your tickets are too diverse for clustering without preprocessing.

### Assigning Human-Readable Labels

BERTopic auto-names topics by top keywords. Override with your category taxonomy:

```python
topic_model.set_topic_labels({
    0: "Shipping & Delivery",
    1: "Refund & Payment",
    2: "Account Access",
    3: "Product Defect",
})
```

Once labeled, use `topic_model.transform(new_tickets)` to classify incoming tickets in real time.

---

## Step 4 — Emerging Issue Detection

**Goal**: surface topics that are NEW or GROWING faster than baseline.

### Z-Score Method (lightweight, no ML needed)

For each phrase/topic, compute a Z-score comparing this week's volume to rolling historical average.

```python
import numpy as np

def detect_emerging(
    history: dict[str, list[int]],  # phrase → [week-5, week-4, ..., week-1]
    current: dict[str, int],         # phrase → this week count
    z_threshold: float = 2.0,
) -> list[dict]:
    alerts = []
    for phrase, count in current.items():
        if phrase not in history:
            if count >= 5:  # new phrase with enough volume
                alerts.append({"phrase": phrase, "count": count, "reason": "new"})
            continue
        hist = np.array(history[phrase])
        mean, std = hist.mean(), hist.std()
        if std < 1:
            continue  # not enough variance to compute Z
        z = (count - mean) / std
        if z >= z_threshold:
            alerts.append({"phrase": phrase, "count": count, "z": round(z, 2), "reason": "spike"})
    return sorted(alerts, key=lambda x: x.get("z", 99), reverse=True)
```

### Worked Example

| phrase | wk-5 | wk-4 | wk-3 | wk-2 | wk-1 | mean | std | this wk | Z |
|--------|------|------|------|------|------|------|-----|---------|---|
| shipping delay | 45 | 52 | 48 | 50 | 46 | 48.2 | 2.6 | 49 | 0.3 |
| payment failed | 12 | 11 | 14 | 10 | 13 | 12.0 | 1.5 | **29** | **11.3** |
| app crash | 3 | 4 | 2 | 5 | 3 | 3.4 | 1.0 | **18** | **14.6** |

"app crash" and "payment failed" warrant immediate escalation to engineering. "Shipping delay" is within normal range.

**Alert thresholds**:
- Z ≥ 3.0 → page on-call or create engineering incident
- Z ≥ 2.0 → flag in weekly CS review
- Z < 2.0 → normal variation, no action

---

## Step 5 — Sentiment Analysis

### Option A: Lexicon-Based (no training, works day one)

```python
# pip install vaderSentiment  (English)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def score_ticket(text: str) -> str:
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"
```

VADER is calibrated for short social-media text — close enough to support tickets. Compound score range: -1 (extremely negative) to +1 (extremely positive).

**For Chinese tickets**: use `snownlp` (simplified) or `ckip-transformers` sentiment model for Traditional Chinese.

```python
# Traditional Chinese
from ckip_transformers.nlp import CkipSentenceClassifier

classifier = CkipSentenceClassifier("bert-base")
labels = classifier(["這個問題根本沒有解決", "非常感謝你的協助"])
# → ['negative', 'positive']
```

### Option B: Fine-Tuned Classifier (higher accuracy, needs labeled data)

Use when lexicon accuracy drops below ~70% on your tickets.

Minimum viable training set: **200 labeled tickets per sentiment class** (positive / neutral / negative).

```python
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

embedder = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def train_sentiment(texts: list[str], labels: list[str]):
    X = embedder.encode(texts, show_progress_bar=False)
    clf = LogisticRegression(max_iter=1000, C=1.0)
    clf.fit(X, labels)
    return clf, embedder

def predict_sentiment(clf, embedder, texts: list[str]) -> list[str]:
    X = embedder.encode(texts, show_progress_bar=False)
    return clf.predict(X).tolist()
```

### Sentiment Aggregation by Category

Don't report global sentiment — it hides signal. Report by topic:

| Topic | Tickets | % Negative | Avg Compound |
|-------|---------|-----------|--------------|
| Shipping & Delivery | 320 | 61% | -0.42 |
| Refund & Payment | 210 | 74% | -0.58 |
| Account Access | 145 | 35% | -0.18 |
| General Inquiry | 98 | 8% | +0.12 |

Refund & Payment has the worst sentiment despite not having the highest volume. This is where to focus process improvement.

---

## Step 6 — Pareto Chart Construction

The SKILL.md states: "top 5 reasons usually account for 60-80% of volume." Verify this with a proper Pareto.

```python
def pareto_table(category_counts: dict[str, int]) -> pd.DataFrame:
    df = pd.DataFrame(
        list(category_counts.items()), columns=["category", "count"]
    ).sort_values("count", ascending=False)
    df["pct"] = df["count"] / df["count"].sum() * 100
    df["cumulative_pct"] = df["pct"].cumsum()
    df["rank"] = range(1, len(df) + 1)
    return df[["rank", "category", "count", "pct", "cumulative_pct"]].round(1)
```

**Sample output** (N = 1,200 tickets/month):

| rank | category | count | % | cumulative % |
|------|----------|-------|---|-------------|
| 1 | Shipping & Delivery | 384 | 32.0 | 32.0 |
| 2 | Refund & Payment | 252 | 21.0 | 53.0 |
| 3 | Account Access | 180 | 15.0 | 68.0 |
| 4 | Product Defect | 144 | 12.0 | 80.0 |
| 5 | Promo / Coupon | 96 | 8.0 | 88.0 |
| 6+ | Other | 144 | 12.0 | 100.0 |

Top 4 categories = 80% of volume. Focus automation and self-service efforts here first.

---

## Operationalizing: Weekly Workflow

```
Monday morning (automated):
  1. Pull tickets from Sunday midnight → Saturday midnight
  2. Run preprocess() → TF-IDF top_phrases()
  3. Run detect_emerging() against 4-week history
  4. Run sentiment by topic
  5. Post digest to #cs-analytics Slack channel

Monthly (analyst review):
  1. Re-run BERTopic on last 30 days
  2. Compare topic distribution to prior month
  3. Update category taxonomy if new clusters stabilized
  4. Review outlier (-1) bucket — recurring patterns become new categories
```

---

## Common Pitfalls

**Analyzing ticket titles instead of full descriptions.** Titles like "shipping problem" are too short for meaningful clustering. Always mine the full body text. If your helpdesk only exports titles, push for full export.

**TF-IDF on a single week with low volume.** With fewer than ~100 tickets, IDF estimates are unstable. Pool at least 2-3 weeks for the IDF baseline, then compute TF only on the current week.

**Treating BERTopic clusters as ground truth.** Topic models surface statistical patterns, not business categories. A cluster might mix "damaged product on arrival" with "missing parts" because both use the word "broken." Manual review of 10-20 tickets per cluster is required before labeling.

**Re-running BERTopic on every new batch.** BERTopic reshuffles topic IDs on each fit — topic 0 this week ≠ topic 0 last week. Either use `transform()` on a frozen model, or use consistent string labels, not integer IDs, for trend tracking.

**Sentiment on templated agent responses.** If your export includes both the customer message and the agent response, strip agent responses before sentiment analysis. Agent-side text ("I'd be happy to help!") inflates positive scores and masks actual customer frustration.

**Over-relying on keyword extraction for root cause.** "Refund not processed" is a symptom. The root cause might be a 3rd-party payment gateway timeout, an internal SLA gap, or a policy misunderstanding. Text mining identifies WHAT customers are saying, not WHY it's happening — escalate to operations review for root cause.
