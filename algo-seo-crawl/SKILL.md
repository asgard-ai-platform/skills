---
name: "algo-seo-crawl"
description: "Implement a web crawler pipeline covering URL discovery, fetching, parsing, and storage. Use this skill when the user needs to build a site crawler, audit website structure, or collect web data systematically — even if they say 'scrape a website', 'crawl all pages', or 'site audit spider'."
metadata:
  category: "WP-35 SEO 演算法"
  tags: ["seo", "web-crawler", "scraping", "site-audit"]
---

# Web Crawler

## Overview

A web crawler systematically traverses web pages by discovering URLs, fetching content, parsing HTML, and storing results. Uses BFS or priority-based frontier management. Performance is I/O-bound, typically limited by politeness constraints rather than compute.

## When to Use

**Trigger conditions:**
- Building a site audit tool to discover all pages and their link structure
- Collecting structured data from websites at scale
- Mapping site architecture for SEO analysis

**When NOT to use:**
- When you need data from a single API endpoint (use HTTP client directly)
- When a sitemap.xml provides all needed URLs (parse sitemap instead)

## Algorithm

```
IRON LAW: Respect robots.txt and Rate Limits
A crawler MUST:
1. Parse and obey robots.txt before crawling any path
2. Enforce crawl-delay (default 1s if unspecified)
3. Identify itself with a descriptive User-Agent
Ignoring these is unethical and will get your IP blocked.
```

### Phase 1: Input Validation
Parse seed URLs, fetch and parse robots.txt for each domain, set crawl scope (same-domain, subdomain, or cross-domain).
**Gate:** Valid seed URLs, robots.txt rules loaded, scope defined.

### Phase 2: Core Algorithm
1. Initialize URL frontier with seed URLs (priority queue or FIFO)
2. Dequeue URL, check: not visited, allowed by robots.txt, within scope
3. Fetch page with timeout and retry logic, respect crawl-delay
4. Parse HTML: extract links (normalize, deduplicate), extract content/metadata
5. Enqueue discovered URLs, store parsed data
6. Repeat until frontier empty or limit reached

### Phase 3: Verification
Check: no robots.txt violations in crawl log, no duplicate pages stored, all discovered URLs accounted for.
**Gate:** Crawl completed within scope, politeness maintained.

### Phase 4: Output
Return site map with pages, link graph, and extracted metadata.

## Output Format

```json
{
  "pages": [{"url": "...", "status": 200, "title": "...", "links_out": 15, "depth": 2}],
  "metadata": {"pages_crawled": 500, "errors": 12, "duration_seconds": 300, "domain": "example.com"}
}
```

## Examples

### Sample I/O
**Input:** Seed: "https://example.com", max_depth: 2, max_pages: 100
**Expected:** Crawl tree with homepage at depth 0, linked pages at depth 1-2, respecting robots.txt

### Edge Cases
| Input | Expected | Why |
|-------|----------|-----|
| robots.txt disallows / | Zero pages crawled | Must respect full disallow |
| Redirect loop | Stop after 5 redirects | Prevent infinite loop |
| Soft 404 (200 with error page) | Flag as soft 404 | Status code alone is insufficient |

## Gotchas

- **URL normalization**: `http://Example.COM/path/` and `http://example.com/path` are the same URL. Normalize: lowercase host, remove default port, remove trailing slash, sort query params.
- **JavaScript-rendered content**: A basic HTTP fetch misses JS-rendered content. Use headless browser (Playwright/Puppeteer) for SPAs.
- **Trap detection**: Calendar pages, session IDs in URLs, and infinite pagination create crawler traps. Set max depth and URL pattern limits.
- **Rate limiting yourself**: Parallel fetching without per-domain rate limiting will overwhelm small servers. Use per-domain semaphores.
- **Character encoding**: Not all pages are UTF-8. Detect encoding from HTTP headers and meta tags; fall back to charset detection libraries.

## References

- For URL normalization rules (RFC 3986), see `references/url-normalization.md`
- For distributed crawling architecture, see `references/distributed-crawl.md`
