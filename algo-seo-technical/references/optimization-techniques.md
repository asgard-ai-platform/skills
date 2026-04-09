# Element-Specific Optimization Techniques

Core Web Vitals optimization succeeds or fails at the element level. This reference covers concrete, per-element techniques for LCP, INP, and CLS.

---

## LCP: Largest Contentful Paint

### Identifying the LCP Element

The LCP element is determined by the browser at runtime. It can change between page loads. Use Chrome DevTools → Performance panel → "Timings" row to see which element was LCP.

Common LCP elements by page type:

| Page Type | Typical LCP Element |
|-----------|---------------------|
| Landing page | Hero `<img>` or `background-image` |
| Article | First `<img>` inside content, or `<h1>` |
| Product page | Product photo `<img>` |
| SPA (client-rendered) | Skeleton → real content transition |

To audit programmatically:

```javascript
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const lcp = entries[entries.length - 1];
  console.log('LCP element:', lcp.element);
  console.log('LCP time:', lcp.startTime);
}).observe({ type: 'largest-contentful-paint', buffered: true });
```

### LCP Sub-Parts (Waterfall Decomposition)

Google decomposes LCP into four sub-parts. Fixing the right one matters.

```
LCP = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay
```

| Sub-part | Definition | Fix target |
|----------|------------|------------|
| TTFB | Server response for HTML | Server optimization, CDN, caching |
| Resource Load Delay | Gap between TTFB and when resource starts loading | `<link rel="preload">`, remove render-blocking |
| Resource Load Time | Download time for the resource | Image compression, format (WebP/AVIF), CDN |
| Element Render Delay | Gap between resource loaded and paint | Remove render-blocking CSS/JS, reduce main-thread work |

**Decision rule:** Measure each sub-part first. Compressing your hero image helps nothing if the bottleneck is TTFB.

### Fixing Resource Load Delay (Preload)

The most common LCP miss is a hero image discovered late in the resource waterfall (inside CSS, or a JS-injected `<img>`).

Add to `<head>`:

```html
<link rel="preload" as="image" href="/hero.webp"
      imagesrcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1600.webp 1600w"
      imagesizes="100vw"
      fetchpriority="high">
```

Rules for preload:
- Only preload the LCP image. Preloading multiple images competes for bandwidth.
- Set `fetchpriority="high"` on the `<img>` tag itself too.
- If the image is responsive, include `imagesrcset` and `imagesizes` to match exactly what the browser will request.

**Pitfall:** Preloading a URL that doesn't match what the `<img srcset>` actually requests results in a double-download. Verify with DevTools Network panel that the preloaded resource is actually used (green "Used" label).

### Fixing Resource Load Time (Image Optimization)

Target: LCP image should be < 200KB on mobile viewports.

**Format decision tree:**

```
Is browser support for AVIF acceptable? (Can I Use: ~93%)
  YES → serve AVIF; fall back to WebP
  NO  → serve WebP; fall back to JPEG
```

Use `<picture>` for format negotiation without JS:

```html
<picture>
  <source type="image/avif" srcset="/hero.avif">
  <source type="image/webp" srcset="/hero.webp">
  <img src="/hero.jpg" alt="..." fetchpriority="high" width="1600" height="900">
</picture>
```

Compression targets (quality settings in Squoosh / imagemin):

| Format | Quality setting | Typical size vs original JPEG |
|--------|----------------|-------------------------------|
| AVIF | 50-60 | 40-60% smaller |
| WebP | 75-85 | 25-35% smaller |
| JPEG (optimized) | 75-80 | baseline |

### Fixing TTFB

TTFB > 800ms is a hard ceiling on LCP. No amount of image optimization overcomes a slow server.

Checklist:
1. **CDN edge caching**: HTML should be served from edge, not origin. Check `X-Cache` header.
2. **Server-side caching**: full-page cache (Varnish, Nginx FastCGI cache) for cacheable pages.
3. **Database queries on critical path**: profile the first-paint render path; eliminate N+1 queries.
4. **`dns-prefetch` + `preconnect`** for third-party origins used by LCP element:

```html
<link rel="preconnect" href="https://images.cdn.example.com">
<link rel="dns-prefetch" href="https://images.cdn.example.com">
```

---

## INP: Interaction to Next Paint

### What INP Measures

INP is the 75th-percentile interaction latency across all user interactions (clicks, taps, key presses) during a page session. It replaced FID in March 2024.

FID only measured the first interaction's input delay. INP measures the full interaction: input delay + processing time + presentation delay.

```
INP = Input Delay + Processing Time + Presentation Delay
```

| Phase | Definition | What causes it |
|-------|------------|----------------|
| Input Delay | Time from interaction to event handler start | Long tasks blocking the main thread |
| Processing Time | Event handler execution | Heavy JS in click/keydown handlers |
| Presentation Delay | Handler end to next frame paint | Layout/style recalculation, large DOM |

### Identifying Slow Interactions

In Chrome DevTools → Performance panel, look for "Interactions" in the timeline. Each interaction shows INP breakdown.

Programmatic capture:

```javascript
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry.duration > 200) {
      console.log('Slow interaction:', {
        type: entry.name,
        duration: entry.duration,
        startTime: entry.startTime,
        element: entry.target
      });
    }
  }
}).observe({ type: 'event', durationThreshold: 200, buffered: true });
```

### Breaking Long Tasks

A long task is any main-thread task > 50ms. Long tasks are the primary cause of input delay.

**Before:** synchronous processing blocks the thread.

```javascript
button.addEventListener('click', () => {
  processLargeDataset(data); // runs for 300ms, blocks input
  updateUI();
});
```

**After:** yield between chunks.

```javascript
async function processInChunks(data) {
  const CHUNK_SIZE = 100;
  for (let i = 0; i < data.length; i += CHUNK_SIZE) {
    const chunk = data.slice(i, i + CHUNK_SIZE);
    processChunk(chunk);
    await scheduler.yield(); // yield to browser; fallback below
  }
}

// Fallback for browsers without scheduler.yield()
function yieldToMain() {
  return new Promise(resolve => setTimeout(resolve, 0));
}
```

Use `scheduler.yield()` (Chrome 115+) over `setTimeout(0)` — it gives the browser back control with higher priority than `setTimeout`.

### `requestIdleCallback` for Non-Critical Work

Non-critical work scheduled during idle time does not impact INP.

```javascript
// Analytics, prefetching, non-visible updates
requestIdleCallback((deadline) => {
  while (deadline.timeRemaining() > 0 && tasks.length > 0) {
    processNextTask(tasks.shift());
  }
}, { timeout: 2000 });
```

**Do not use `requestIdleCallback` for anything that affects the visual response to a user interaction.** If the user tapped a button and expects a state change, that update must happen synchronously in the event handler or via microtask — not idle callback.

### DOM Size and INP

Large DOMs (> 1,500 nodes) increase style recalculation and layout time, inflating Presentation Delay.

Audit DOM size:

```javascript
document.querySelectorAll('*').length; // quick count
```

Mitigation strategies:
- **Virtualize long lists**: render only visible rows (e.g., `@tanstack/virtual`, `react-window`). A 10,000-row table should render ~20-50 DOM nodes.
- **Lazy-render off-screen content**: use Intersection Observer to mount heavy components only when near viewport.
- **`content-visibility: auto`**: tells the browser to skip rendering off-screen sections until needed.

```css
.article-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px; /* estimated height to prevent CLS */
}
```

---

## CLS: Cumulative Layout Shift

### CLS Score Formula

```
CLS = Σ (impact_fraction × distance_fraction) for each unexpected shift
```

- **impact_fraction**: fraction of viewport area affected by the shift
- **distance_fraction**: largest distance any element moved, as fraction of viewport

Example: An element occupying 50% of viewport height shifts down by 25% of viewport height.
```
impact_fraction = 0.50
distance_fraction = 0.25
shift_score = 0.50 × 0.25 = 0.125  → Needs Improvement
```

CLS is the sum of shift scores; shifts separated by > 1 second or triggered by user interaction are excluded.

### Root Cause: Attributing Shifts Correctly

The browser reports the **shifted element**, not the **cause**. Common misattribution:

| Reported shifted element | Actual cause |
|--------------------------|--------------|
| `<h1>` moved down | Ad banner injected above it |
| Product image jumped | Font loaded, changing line heights around it |
| Navigation shifted | Cookie banner inserted at top of page |

To find the cause: in DevTools → Performance, click a Layout Shift event. The "Moved from" / "Moved to" highlights show which element shifted. Then look at what was inserted or resized just before the shift in the DOM mutations.

### Fix 1: Explicit Dimensions on Images and Videos

The most common CLS source. Without dimensions, the browser allocates zero space until the resource loads.

```html
<!-- BAD: no dimensions, causes layout shift when image loads -->
<img src="/product.jpg" alt="...">

<!-- GOOD: browser reserves correct space immediately -->
<img src="/product.jpg" alt="..." width="800" height="600">
```

For responsive images, the browser uses the aspect ratio from `width`/`height` attributes, scaled to actual display size. Set the **intrinsic** (natural) dimensions in the HTML; CSS handles the responsive scaling.

```css
img {
  max-width: 100%;
  height: auto; /* maintains aspect ratio from HTML attributes */
}
```

### Fix 2: Reserving Space for Ads and Dynamic Embeds

Ads are the #1 CLS source on publisher sites. Reserve the slot before the ad loads.

```css
.ad-slot {
  min-height: 250px;    /* minimum expected ad height */
  width: 300px;
  background: #f0f0f0;  /* placeholder prevents cumulative shift */
}
```

For variable-height ads: use the largest expected ad size as the placeholder. A small visual gap when a smaller ad loads is acceptable; CLS from a zero-height slot is not.

**Sticky/fixed ads injected into page flow**: these always cause CLS. Either:
- Keep them in a fixed container that doesn't affect document flow
- Reserve their full height in the layout before injection

### Fix 3: Font-Induced CLS

Web fonts cause layout shift when the fallback font has different metrics than the loaded font.

**`font-display: swap` does NOT prevent CLS.** It prevents FOIT (invisible text) but trades it for FOUT (layout shift when font swaps).

Solutions ranked by effectiveness:

1. **`size-adjust` + `ascent-override` CSS descriptors** (match fallback metrics to web font):

```css
@font-face {
  font-family: 'FallbackArial';
  src: local('Arial');
  size-adjust: 107%;        /* scale fallback to match web font size */
  ascent-override: 90%;     /* match cap height */
  descent-override: 22%;
  line-gap-override: 0%;
}

body {
  font-family: 'MyWebFont', 'FallbackArial', sans-serif;
}
```

Use [Automatic Font Matching](https://deploy-preview-15-- font-fallback.netlify.app/) tool to calculate exact override values for your specific font pair.

2. **Preload the font file**:

```html
<link rel="preload" as="font" href="/fonts/inter-var.woff2" type="font/woff2" crossorigin>
```

3. **Self-host fonts**: eliminates DNS lookup + connection overhead for third-party font CDNs.

### Fix 4: `content-visibility: auto` and CLS

`content-visibility: auto` can cause CLS if `contain-intrinsic-size` is not set or is wrong. When the browser renders a section that was previously skipped, it may shift the layout.

Always pair:
```css
section {
  content-visibility: auto;
  contain-intrinsic-size: auto 500px; /* estimate; auto keyword allows browser to remember actual size after first render */
}
```

The `auto` keyword in `contain-intrinsic-size: auto 500px` means the browser uses the placeholder `500px` only before the first render, then remembers the real size — preventing repeated shifts on scroll.

---

## Cross-Metric Decision Framework

When multiple metrics fail, fix in this order:

```
1. CLS first — cheapest to fix; often pure HTML/CSS with no perf trade-offs
2. LCP second — highest SEO impact; image/preload fixes are well-understood
3. INP last — requires JS profiling; most context-dependent
```

Exception: if INP is > 500ms (Poor), elevate it above LCP. A page that freezes on interaction signals a severe JS problem that may also be hurting LCP indirectly (main thread saturation).

### Quick Diagnostic Matrix

| Symptom | Most likely cause | First check |
|---------|-------------------|-------------|
| LCP > 4s, TTFB < 200ms | Image too large or loading late | DevTools Network: when does LCP resource start? |
| LCP > 4s, TTFB > 800ms | Slow server | `cf-cache-status` / `X-Cache` header; server logs |
| CLS > 0.25 on mobile only | Ad or banner injected on mobile layout | Test with Network throttling + mobile viewport |
| INP > 500ms on form pages | Heavy validation JS on each keystroke | DevTools → Performance: record typing interaction |
| All metrics fail on SPA | Client-side rendering delay | Measure LCP on hydrated vs server-rendered version |
