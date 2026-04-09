# Feature Extraction for Content-Based Recommendation

The user profile is a weighted centroid of item feature vectors — so the quality of those vectors determines everything. This document covers how to build item feature vectors from text, categorical, and numerical attributes, with worked examples for each.

---

## Feature Type Decision Table

| Source data | Technique | Resulting vector type |
|---|---|---|
| Item descriptions, tags, titles | TF-IDF | Dense float vector (vocab-sized) |
| Genre, category, brand | One-hot / multi-hot | Sparse binary vector |
| Price, duration, rating count | Min-max normalization | Single float per attribute |
| Embeddings from a language model | Direct use | Dense float vector (model dim) |

In most recommendation systems you'll combine all three into one concatenated vector.

---

## 1. TF-IDF for Text Attributes

### Formula

Given a corpus of I items, for term t in item d:

```
TF(t, d) = count(t in d) / total_terms(d)

IDF(t) = log( (1 + I) / (1 + df(t)) ) + 1      # sklearn smooth IDF

TF-IDF(t, d) = TF(t, d) × IDF(t)
```

After computing the raw vector, normalize each item's vector to unit L2 norm. This is mandatory before computing cosine similarity — without it, longer descriptions dominate.

### Worked Example

Corpus: 4 movie descriptions (stripped to content words).

```
Item A: "action hero fight explosion"        (4 terms)
Item B: "action spy thriller chase"          (4 terms)
Item C: "romance love drama wedding"         (4 terms)
Item D: "documentary history war archive"    (4 terms)
```

Compute IDF for the term **"action"** (appears in items A, B → df=2, I=4):

```
IDF("action") = log((1 + 4) / (1 + 2)) + 1
              = log(5/3) + 1
              = log(1.667) + 1
              = 0.511 + 1
              = 1.511
```

Compute IDF for **"hero"** (appears in item A only → df=1):

```
IDF("hero") = log((1+4) / (1+1)) + 1
            = log(2.5) + 1
            = 0.916 + 1
            = 1.916
```

TF-IDF for "action" in Item A (TF = 1/4 = 0.25):

```
TF-IDF("action", A) = 0.25 × 1.511 = 0.378
```

TF-IDF for "hero" in Item A (TF = 1/4 = 0.25):

```
TF-IDF("hero", A) = 0.25 × 1.916 = 0.479
```

**Observation**: "hero" scores higher than "action" because it's rarer (more discriminative). This is the correct behavior — common terms across many items should carry less weight.

### Vocabulary Pruning (Required)

Raw vocabularies can be huge. Apply these cuts before fitting:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    min_df=2,          # term must appear in at least 2 items
    max_df=0.85,       # term must not appear in >85% of items
    max_features=5000, # cap vocabulary size
    sublinear_tf=True, # use log(1+TF) instead of raw TF
    norm='l2'          # normalize output vectors
)
X = vectorizer.fit_transform(item_descriptions)
```

`sublinear_tf=True` compresses term frequency via `log(1 + TF)` — this prevents a description that uses "action" 10 times from dominating one that uses it 3 times.

---

## 2. One-Hot and Multi-Hot Encoding for Categorical Features

### One-Hot (Single Category per Item)

When each item has exactly one value per field (e.g., primary_genre):

```
Vocabulary: [action, romance, thriller, documentary, sci-fi]

Item A (action):  [1, 0, 0, 0, 0]
Item C (romance): [0, 1, 0, 0, 0]
```

### Multi-Hot (Multiple Categories per Item)

When an item can belong to multiple categories (e.g., a movie tagged both "action" and "sci-fi"):

```
Item A (action + sci-fi): [1, 0, 0, 0, 1]
```

### Handling High-Cardinality Categories

If your category field has hundreds of values (e.g., director name, sub-genre tag), raw one-hot becomes expensive and sparse.

Options:
1. **Frequency threshold**: keep only categories appearing in ≥ N items (N=10 is a reasonable default)
2. **Hashing trick**: map categories to a fixed-size hash bucket (fast, some collisions)
3. **Learned embeddings**: if you have a neural component, embed categories as dense vectors

For pure content-based filtering without neural components, the frequency threshold approach is simplest and interpretable.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Filter rare tags
from collections import Counter
tag_counts = Counter(tag for tags in all_item_tags for tag in tags)
common_tags = {tag for tag, count in tag_counts.items() if count >= 10}

filtered_tags = [[t for t in tags if t in common_tags] for tags in all_item_tags]

mlb = MultiLabelBinarizer()
tag_matrix = mlb.fit_transform(filtered_tags)
```

---

## 3. Numerical Attributes

Numerical features (price, duration, rating count) must be scaled before concatenation — otherwise a price of 999 will dominate a duration value of 2.0.

### Min-Max Normalization

Scales each feature to [0, 1]:

```
x_scaled = (x - x_min) / (x_max - x_min)
```

Use min-max when:
- The feature has a known bounded range
- Outliers are not extreme

### Z-Score Standardization

```
x_scaled = (x - μ) / σ
```

Use z-score when:
- Distribution is roughly Gaussian
- Outliers exist (z-score is less affected than min-max)
- You care about relative differences more than absolute position in [0,1]

### Worked Example: Movie Duration

```
Durations (minutes): [90, 95, 120, 180, 200]
x_min = 90, x_max = 200

Item with 120 min: (120 - 90) / (200 - 90) = 30/110 = 0.273
Item with 180 min: (180 - 90) / (200 - 90) = 90/110 = 0.818
```

---

## 4. Concatenating Feature Vectors

After computing each feature type separately, concatenate them into one item feature vector. The challenge is **weighting** — you must decide how much each feature type contributes.

### Approach A: Equal Block Weighting

Normalize each block to unit norm independently, then concatenate. Each block contributes equally regardless of dimensionality.

```python
import numpy as np
from scipy.sparse import hstack, csr_matrix

def normalize_block(X):
    norms = np.sqrt((X.multiply(X)).sum(axis=1))  # for sparse
    norms[norms == 0] = 1
    return X.multiply(1 / norms)

tfidf_norm   = normalize_block(tfidf_matrix)     # shape (I, V)
tags_norm    = normalize_block(csr_matrix(tag_matrix))  # shape (I, T)
numeric_norm = numeric_matrix / np.linalg.norm(numeric_matrix, axis=1, keepdims=True)

item_features = hstack([tfidf_norm, tags_norm, csr_matrix(numeric_norm)])
```

### Approach B: Explicit Feature Weights

Multiply each block by a scalar weight before concatenation:

```python
w_text    = 0.5
w_tags    = 0.4
w_numeric = 0.1

item_features = hstack([
    tfidf_norm * w_text,
    tags_norm  * w_tags,
    csr_matrix(numeric_norm * w_numeric)
])
```

How to pick weights: A/B test offline with held-out interaction data, or use domain knowledge (if tags are highly curated and descriptions are auto-generated, weight tags higher).

---

## 5. Minimum Feature Count Threshold

As noted in SKILL.md Gotchas: items with too few features produce unreliable similarity scores. Enforce a minimum before including items as candidates.

```python
def feature_count(item):
    return (
        len(item.get("tags", [])) +
        bool(item.get("description", "").strip()) +  # 1 if description exists
        sum(1 for f in ["price", "duration"] if item.get(f) is not None)
    )

MIN_FEATURES = 3
candidate_items = [item for item in all_items if feature_count(item) >= MIN_FEATURES]
```

Items below the threshold should fall back to a different strategy (e.g., popularity-based ranking) rather than being given artificially similar vectors.

---

## 6. Feature Extraction Pipeline Summary

```
Raw item data
     │
     ├─ Text fields (description, title, tags as text)
     │       → Tokenize → Filter stop words → TF-IDF → L2 normalize
     │
     ├─ Categorical fields (genre, brand, director)
     │       → Frequency filter → Multi-hot encode → L2 normalize
     │
     └─ Numerical fields (price, duration, rating_count)
             → Min-max or z-score scale → L2 normalize
                        │
                        ▼
              Weighted concatenation
                        │
                        ▼
              Final item feature matrix  [I × F]
                        │
                        ▼
              Cosine similarity → user profile matching
```

---

## 7. When Features Are Unavailable or Unreliable

| Situation | Recommendation |
|---|---|
| Item has no description | Rely on tags + numerical only; flag for content team |
| All items share the same category | That feature adds no signal — drop the column |
| Numerical feature has >30% missing values | Impute with median, add a binary "is_missing" indicator column |
| Text is in multiple languages | Run language detection; fit separate TF-IDF vectorizers per language, then combine |
| Tags are user-generated (noisy) | Apply frequency threshold ≥ 10; consider stemming or fuzzy deduplication |

---

## 8. Drift and Refit Schedule

TF-IDF vocabulary and IDF weights are fit on the item corpus at a point in time. As new items are added:

- **New terms** not in the original vocabulary get zero weight → they're invisible to the model
- **IDF weights** become stale as the corpus grows

**Rule of thumb**: refit the vectorizer when the catalog has grown by >20% since the last fit, or at a fixed weekly/monthly cadence. Cache the fitted vectorizer; don't refit on every request.
