---
name: "algo-seo-technical"
description: "Optimize Core Web Vitals (LCP, INP, CLS) for better search rankings and user experience. Use this skill when the user needs to diagnose page speed issues, improve Largest Contentful Paint, reduce layout shift, or pass Google's page experience signals — even if they say 'my site is slow', 'Core Web Vitals failing', or 'page speed optimization'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "core-web-vitals", "performance", "page-speed"]
---

# Core Web Vitals Optimization

## Overview

Core Web Vitals are Google's page experience metrics: LCP (loading), INP (interactivity), and CLS (visual stability). Measured on real user data (CrUX). Pass thresholds: LCP < 2.5s, INP < 200ms, CLS < 0.1.

## When to Use

**Trigger conditions:**
- Diagnosing why a site fails Core Web Vitals assessment
- Optimizing page load performance for SEO
- Reducing layout shift or improving interactivity

**When NOT to use:**
- When the issue is content relevance, not speed (use content SEO)
- When analyzing link authority (use PageRank / backlink analysis)

## Algorithm

```
IRON LAW: CrUX Field Data Is the Source of Truth
Lab scores (Lighthouse) that pass can still FAIL in the field.
Google ranks based on REAL USER data (75th percentile):
- LCP < 2.5s (Good), 2.5-4.0s (Needs Improvement), > 4.0s (Poor)
- INP < 200ms (Good), 200-500ms (Needs Improvement), > 500ms (Poor)
- CLS < 0.1 (Good), 0.1-0.25 (Needs Improvement), > 0.25 (Poor)
```

### Phase 1: Input Validation
Collect field data from CrUX API or Search Console. Run Lighthouse for lab baseline. Identify which metrics fail.
**Gate:** Have both field and lab data; failing metrics identified.

### Phase 2: Core Algorithm
**LCP fixes:** 1. Optimize largest element (hero image/text). 2. Preload critical resources. 3. Reduce server response time (TTFB). 4. Eliminate render-blocking resources.

**INP fixes:** 1. Break long tasks (> 50ms) into smaller chunks. 2. Reduce JavaScript execution time. 3. Use `requestIdleCallback` for non-critical work. 4. Minimize main thread blocking.

**CLS fixes:** 1. Set explicit dimensions on images/videos. 2. Reserve space for ads/embeds. 3. Avoid inserting content above existing content. 4. Use CSS `contain` for dynamic elements.

### Phase 3: Verification
Re-run Lighthouse, deploy, then monitor CrUX for 28-day rolling average improvement.
**Gate:** Lab scores pass; await field data confirmation (28-day cycle).

### Phase 4: Output
Return audit results with specific fix recommendations prioritized by impact.

## Output Format

```json
{
  "audit": {"lcp": {"value_ms": 3200, "status": "poor", "element": "hero-image.jpg", "fixes": ["preload", "compress"]}},
  "metadata": {"url": "...", "data_source": "crux", "device": "mobile"}
}
```

## Examples

### Sample I/O
**Input:** URL with LCP=4.1s, CLS=0.32, INP=150ms
**Expected:** LCP and CLS flagged as poor; INP passes. Fix priorities: CLS (image dimensions) → LCP (hero image preload)

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| SPA with client rendering | High LCP likely | No server-rendered content for LCP element |
| Page with ads | High CLS likely | Ad slots inject content dynamically |
| All metrics pass in lab | May still fail field | Real devices on slow networks differ from lab |

## Gotchas

- **Lab vs field gap**: Lighthouse runs on a simulated fast device. Real users on 3G with old phones produce very different numbers.
- **LCP element changes**: The LCP element can differ across page loads (image vs text). Optimize for the MOST COMMON LCP element, not just one.
- **CLS attribution**: Layout shifts are blamed on the element that moved, but the CAUSE is often an element inserted above it. Trace the cause, not the symptom.
- **INP replaced FID**: As of March 2024, INP replaces FID. Old references to FID are outdated.
- **28-day lag**: CrUX uses a 28-day rolling window. Fixes take up to a month to reflect in field data.

## References

- For element-specific optimization techniques, see `references/optimization-techniques.md`
- For CrUX API usage and monitoring setup, see `references/crux-monitoring.md`
