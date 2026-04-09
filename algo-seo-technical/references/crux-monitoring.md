# CrUX API Usage and Monitoring Setup

## What CrUX Measures

Chrome User Experience Report (CrUX) aggregates real-user performance data from opted-in Chrome users. Google uses CrUX — not Lighthouse — to determine page experience ranking signals.

Key properties:
- **Aggregation window**: 28-day rolling average, updated daily
- **Percentile used**: 75th percentile per metric per URL/origin
- **Device segments**: phone, desktop, tablet (reported separately)
- **Minimum threshold**: URL needs sufficient traffic to appear; low-traffic URLs fall back to origin-level data

## CrUX Data Sources (Ranked by Specificity)

| Source | Granularity | Latency | Free? |
|--------|-------------|---------|-------|
| CrUX API | URL or origin | ~2 days | Yes |
| Search Console (CWV report) | Page group | ~3 days | Yes (property access required) |
| PageSpeed Insights UI | URL | ~2 days | Yes |
| CrUX History API | URL or origin, 25 weeks | ~2 days | Yes |
| BigQuery CrUX dataset | origin, monthly | ~15 days | Free tier |

For programmatic monitoring, use the **CrUX API** or **CrUX History API** directly.

---

## CrUX API: Minimal Working Example

### Endpoint

```
POST https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=YOUR_API_KEY
```

### Request Body (URL-level, mobile)

```json
{
  "url": "https://example.com/product/widget-a",
  "formFactor": "PHONE",
  "metrics": [
    "largest_contentful_paint",
    "interaction_to_next_paint",
    "cumulative_layout_shift"
  ]
}
```

`formFactor` options: `"PHONE"`, `"DESKTOP"`, `"TABLET"`. Omit to get all-devices aggregate.

### Response Structure

```json
{
  "record": {
    "key": {
      "url": "https://example.com/product/widget-a",
      "formFactor": "PHONE"
    },
    "metrics": {
      "largest_contentful_paint": {
        "histogram": [
          {"start": 0, "end": 2500, "density": 0.52},
          {"start": 2500, "end": 4000, "density": 0.28},
          {"start": 4000, "density": 0.20}
        ],
        "percentiles": {
          "p75": 3240
        }
      },
      "interaction_to_next_paint": {
        "histogram": [
          {"start": 0, "end": 200, "density": 0.71},
          {"start": 200, "end": 500, "density": 0.22},
          {"start": 500, "density": 0.07}
        ],
        "percentiles": {
          "p75": 188
        }
      },
      "cumulative_layout_shift": {
        "histogram": [
          {"start": "0.00", "end": "0.10", "density": 0.44},
          {"start": "0.10", "end": "0.25", "density": 0.31},
          {"start": "0.25", "density": 0.25}
        ],
        "percentiles": {
          "p75": "0.18"
        }
      }
    },
    "collectionPeriod": {
      "firstDate": {"year": 2026, "month": 3, "day": 12},
      "lastDate": {"year": 2026, "month": 4, "day": 8}
    }
  }
}
```

**Reading the response:**
- `percentiles.p75` is the single number Google uses for ranking signals
- `histogram` shows the full distribution: bucket 0 = Good, bucket 1 = Needs Improvement, bucket 2 = Poor
- CLS values are strings (`"0.18"`), not numbers — parse accordingly

### Status Classification from p75

```python
def classify_lcp(p75_ms: int) -> str:
    if p75_ms < 2500:
        return "good"
    elif p75_ms < 4000:
        return "needs_improvement"
    return "poor"

def classify_inp(p75_ms: int) -> str:
    if p75_ms < 200:
        return "good"
    elif p75_ms < 500:
        return "needs_improvement"
    return "poor"

def classify_cls(p75: float) -> str:
    if p75 < 0.1:
        return "good"
    elif p75 < 0.25:
        return "needs_improvement"
    return "poor"
```

---

## CrUX History API: Trend Monitoring

For tracking improvement over time, the History API returns 25 weeks of weekly p75 values.

### Endpoint

```
POST https://chromeuxreport.googleapis.com/v1/records:queryHistoryRecord?key=YOUR_API_KEY
```

### Request Body

```json
{
  "url": "https://example.com/product/widget-a",
  "formFactor": "PHONE",
  "metrics": ["largest_contentful_paint", "cumulative_layout_shift"]
}
```

### Response (truncated)

```json
{
  "record": {
    "metrics": {
      "largest_contentful_paint": {
        "percentilesTimeseries": {
          "p75s": [3410, 3380, 3350, 3240, 3100, 2890, 2640]
        },
        "collectionPeriods": [
          {"firstDate": {"year": 2026, "month": 2, "day": 12}, "lastDate": {...}},
          ...
        ]
      }
    }
  }
}
```

Each entry in `p75s` corresponds to one `collectionPeriod` (28-day rolling window, sampled weekly). The array runs oldest → newest.

### Worked Example: Verifying a Fix

Scenario: You preloaded the hero image on 2026-03-15. You expect LCP to improve.

```
Week ending 2026-03-08: p75 = 3410ms  (before fix)
Week ending 2026-03-15: p75 = 3380ms  (fix deployed mid-week)
Week ending 2026-03-22: p75 = 3240ms  (partial bleed-in)
Week ending 2026-03-29: p75 = 2890ms  (fix fully in window)
Week ending 2026-04-05: p75 = 2640ms  (Good threshold reached)
```

The fix takes 3-4 weeks to fully appear because the 28-day window dilutes early data. If p75 hasn't moved after 5 weeks, the fix likely didn't work in production.

---

## URL vs Origin Fallback Logic

Not every URL has enough CrUX data. Follow this decision tree:

```
Query URL-level data
    │
    ├── Record exists? ──YES──> Use URL p75
    │
    └── NO (404 from API, or "NOT_FOUND")
            │
            └── Query origin-level data
                    │
                    ├── Record exists? ──YES──> Use origin p75
                    │                          (note: origin = aggregate of all pages)
                    └── NO ──> Insufficient traffic; no CrUX signal
```

**Origin query** — just change the request body:

```json
{
  "origin": "https://example.com",
  "formFactor": "PHONE"
}
```

**Implication for auditing:** if you're auditing a low-traffic product page and only origin data is available, the origin p75 blends in high-traffic pages (often homepage). Origin data may show "Good" while the product page is actually "Poor." Flag this clearly in your audit output.

---

## Monitoring Script: Batch URL Checker

```python
import urllib.request
import urllib.error
import json
import time

API_KEY = "YOUR_API_KEY"
ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"

THRESHOLDS = {
    "largest_contentful_paint": (2500, 4000),
    "interaction_to_next_paint": (200, 500),
    "cumulative_layout_shift": (0.1, 0.25),
}

def query_crux(url: str, form_factor: str = "PHONE") -> dict | None:
    body = json.dumps({
        "url": url,
        "formFactor": form_factor,
        "metrics": list(THRESHOLDS.keys())
    }).encode()

    req = urllib.request.Request(
        f"{ENDPOINT}?key={API_KEY}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None  # not enough data
        raise

def classify(metric: str, p75) -> str:
    good, ni = THRESHOLDS[metric]
    val = float(p75)
    if val < good:
        return "good"
    elif val < ni:
        return "needs_improvement"
    return "poor"

def audit_urls(urls: list[str]) -> list[dict]:
    results = []
    for url in urls:
        data = query_crux(url)
        if data is None:
            results.append({"url": url, "status": "no_data"})
            time.sleep(0.5)
            continue

        metrics = data["record"]["metrics"]
        row = {"url": url, "status": "ok", "metrics": {}}
        for metric, values in metrics.items():
            p75 = values["percentiles"]["p75"]
            row["metrics"][metric] = {
                "p75": p75,
                "classification": classify(metric, p75)
            }
        results.append(row)
        time.sleep(0.5)  # respect rate limits

    return results

# Usage
urls = [
    "https://example.com/",
    "https://example.com/product/widget-a",
    "https://example.com/blog/post-1",
]
report = audit_urls(urls)
print(json.dumps(report, indent=2))
```

**Rate limits:** The CrUX API has a default quota of 150 queries/minute per API key. Insert `time.sleep(0.5)` between requests when batching.

---

## Search Console CWV Report: What It Shows vs Doesn't

Search Console's "Core Web Vitals" report groups URLs into "page groups" based on URL pattern similarity. This means:

- One row may represent hundreds of URLs with similar structure (e.g., `/product/*`)
- The p75 shown is for the entire page group, not individual URLs
- Status shown: "Good", "Needs Improvement", "Poor" — no raw ms values

**When to use Search Console vs CrUX API:**

| Need | Use |
|------|-----|
| Overview of site health | Search Console |
| Specific URL diagnosis | CrUX API |
| Historical trend (25 weeks) | CrUX History API |
| Competitor comparison | PageSpeed Insights (URL-level, their URLs) |
| Automated CI monitoring | CrUX API |

---

## 28-Day Rolling Window: Planning Fixes

The CrUX window always covers the 28 days ending approximately 2 days ago. This has two practical consequences:

**Consequence 1: Regression detection lag**

If you accidentally deploy a performance regression on Day 1, CrUX won't show full impact until Day 29 (when all 28 days in window contain the regression). Use Lighthouse and lab monitoring to catch regressions fast; don't wait for CrUX.

**Consequence 2: Fix validation timeline**

After deploying a fix on Day 0:

```
Day 0-2:   Fix live; CrUX not yet reflecting
Day 3-7:   p75 starts improving slowly (few days of good data diluted by 25+ days of bad)
Day 14:    Roughly half the window contains fixed data
Day 28-30: p75 fully reflects the fix
```

Set a calendar reminder for Day 30 after each significant fix. Check CrUX History API at that point to confirm the trend moved in the right direction.

---

## API Error Handling Reference

| HTTP Code | Meaning | Action |
|-----------|---------|--------|
| 200 | Success | Parse response |
| 404 | URL/origin has no CrUX data | Fall back to origin; mark as no_data |
| 429 | Rate limit exceeded | Exponential backoff; check quota |
| 400 | Malformed request | Check formFactor spelling, URL format |
| 401/403 | API key invalid or missing | Verify key; enable CrUX API in Google Cloud Console |

**Enabling the API:** In Google Cloud Console → APIs & Services → Enable → search "Chrome UX Report API". The API key must have this API enabled; it is not on by default.

---

## Composite Pass/Fail: How Google Scores a Page

A page passes Core Web Vitals assessment only if **all three metrics** are "Good" at the 75th percentile for the **phone** segment (primary ranking signal). Desktop is tracked separately and does not gate the phone signal.

```
page_passes = (
    lcp_phone_p75 < 2500 AND
    inp_phone_p75 < 200 AND
    cls_phone_p75 < 0.1
)
```

If any one metric is "Poor" or "Needs Improvement", the page fails the assessment regardless of the others. Prioritize fixes by:

1. Move any "Poor" metric to at least "Needs Improvement" first
2. Then move all metrics to "Good"

This is the correct triage order because Google's assessment is binary (pass/fail), not additive scoring.
