---
name: "algo-nlp-ner"
description: "Implement Named Entity Recognition to identify and classify entities in text. Use this skill when the user needs to extract people, organizations, locations, dates, or custom entities from documents — even if they say 'extract names from text', 'find companies mentioned', or 'entity extraction'."
metadata:
  category: "WP-45 NLP 演算法"
  tags: ["nlp", "ner", "entity-extraction", "information-extraction"]
---

# Named Entity Recognition

## Overview

NER identifies and classifies named entities in text into predefined categories (Person, Organization, Location, Date, Money, etc.). Approaches: rule-based (regex, gazetteers), statistical (CRF), neural (BiLSTM-CRF, transformer-based). Modern NER uses spaCy or Hugging Face models with F1 scores 85-95%.

## When to Use

**Trigger conditions:**
- Extracting structured entities from unstructured text
- Building knowledge graphs from documents
- Preprocessing for information retrieval or question answering

**When NOT to use:**
- For text classification (categorizing whole documents, not extracting entities)
- For relation extraction between entities (need additional RE model)

## Algorithm

```
IRON LAW: NER Performance Depends on DOMAIN Match
A model trained on news text (OntoNotes) performs poorly on medical
records or legal documents. Domain-specific entities (drug names,
legal citations, product SKUs) require domain-specific training data
or fine-tuning. Always evaluate on YOUR domain's data.
```

### Phase 1: Input Validation
Determine: target entity types (standard: PER, ORG, LOC, DATE, MONEY or custom), input language, domain. Select appropriate pre-trained model or prepare training data.
**Gate:** Entity types defined, model or training data available.

### Phase 2: Core Algorithm
**Pre-trained model approach:**
1. Load model (spaCy, Hugging Face NER pipeline)
2. Process text through the pipeline
3. Extract entity spans with type labels and confidence scores

**Fine-tuning approach:**
1. Annotate 200+ domain-specific examples in BIO format
2. Fine-tune transformer model (BERT, RoBERTa) on annotated data
3. Evaluate on held-out test set

### Phase 3: Verification
Evaluate: precision, recall, F1 per entity type. Check: boundary detection (exact span match) and type classification accuracy.
**Gate:** F1 > 0.80 per entity type on domain-relevant test data.

### Phase 4: Output
Return extracted entities with types, positions, and confidence.

## Output Format

```json
{
  "entities": [{"text": "Apple Inc.", "type": "ORG", "start": 0, "end": 10, "confidence": 0.95}],
  "metadata": {"model": "en_core_web_trf", "entities_found": 15, "types": {"PER": 5, "ORG": 6, "LOC": 4}}
}
```

## Examples

### Sample I/O
**Input:** "Tim Cook announced that Apple will open a new store in Taipei on March 15."
**Expected:** [Tim Cook/PER, Apple/ORG, Taipei/LOC, March 15/DATE]

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| "Apple" (no context) | Ambiguous (fruit or company) | Context-dependent entity typing |
| Nested entities | Depends on scheme | "Bank of America" = ORG, "America" = LOC within |
| Misspelled entity | May miss | "Appel" not in training data |

## Gotchas

- **Boundary errors**: NER often gets the entity type right but the span wrong ("New" vs "New York City"). Evaluate with both exact and partial match metrics.
- **Ambiguity**: "Jordan" can be a person, country, or brand. Context-dependent disambiguation is hard; some models output the most likely type.
- **Chinese/Japanese NER**: No whitespace tokenization makes boundary detection harder. Use language-specific tokenizers (jieba for Chinese).
- **Annotation consistency**: Training data quality is critical. Inconsistent annotations (sometimes labeling "Dr." as part of name, sometimes not) degrade model performance.
- **Entity linking**: NER identifies mentions; entity linking resolves them to knowledge base entries. "Apple" → Apple Inc. (Q312) or apple (fruit). These are separate tasks.

## References

- For BIO annotation format and guidelines, see `references/bio-annotation.md`
- For fine-tuning NER with transformers, see `references/transformer-ner.md`
