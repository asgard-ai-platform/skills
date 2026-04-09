# Distributed Crawl Architecture

Distributed crawling splits a single-machine crawler across multiple worker nodes to increase throughput while preserving politeness constraints. The core challenge is not parallelism itself — it is **coordinating URL deduplication and per-domain rate limiting across processes that share no memory**.

## When to Distribute

Single-machine crawl capacity (Python `asyncio`, ~50-100 concurrent fetches) handles most site audits under 500k pages within a few hours. Distribute only when:

| Condition | Single Machine | Distributed |
|-----------|---------------|-------------|
| Pages to crawl | < 500k | > 500k |
| Target domains | 1-10 | 100+ |
| SLA (crawl deadline) | hours | minutes |
| Fault tolerance required | No | Yes |

## Architecture: URL Frontier as Shared Queue

The URL frontier (the queue of URLs to visit) must live outside any single worker. A distributed frontier has three components:

```
┌────────────┐     enqueue      ┌─────────────────┐
│  Workers   │ ───────────────► │  Frontier Queue │
│  (N nodes) │ ◄─────────────── │  (Redis/Kafka)  │
└────────────┘     dequeue      └─────────────────┘
      │                                  │
      │ mark visited              ┌──────▼───────┐
      └──────────────────────────►│  Seen Set    │
                                  │  (Redis Set) │
                                  └──────────────┘
```

**Seen Set** is the deduplication layer. Before enqueuing any URL, a worker checks the seen set atomically:

```python
# Redis atomic check-and-add
def enqueue_if_unseen(redis_client, url: str, frontier_key: str, seen_key: str) -> bool:
    normalized = normalize_url(url)
    added = redis_client.sadd(seen_key, normalized)  # returns 1 if new, 0 if exists
    if added:
        redis_client.rpush(frontier_key, normalized)
    return bool(added)
```

Using `SADD` (atomic in Redis) prevents two workers from both enqueuing the same URL discovered simultaneously.

## URL Assignment: Consistent Hashing by Domain

Naïve work-stealing (any worker dequeues any URL) breaks per-domain rate limiting: two workers could simultaneously fetch from the same domain. The fix is **domain-affinity routing** — URLs from the same domain always go to the same worker.

Assign each domain to a worker using consistent hashing:

```python
import hashlib

def domain_to_worker(domain: str, num_workers: int) -> int:
    h = int(hashlib.md5(domain.encode()).hexdigest(), 16)
    return h % num_workers

# Each worker has its own sub-queue
frontier_key = f"frontier:worker:{domain_to_worker(domain, num_workers)}"
```

Each worker then only processes URLs from its assigned sub-queues, and its per-domain rate limiter is local — no distributed lock needed.

**Trade-off**: if one domain has 80% of all URLs, one worker becomes a hotspot. Mitigate by capping per-domain URL count in the frontier.

## Per-Domain Rate Limiting (Token Bucket, Distributed)

When domain-affinity routing is not feasible (e.g., workers are stateless), use a distributed token bucket in Redis.

Token bucket parameters:
- `capacity` = max burst (typically 1-5 requests)
- `refill_rate` = requests per second (1/crawl_delay)

```python
import time

def acquire_token(redis_client, domain: str, refill_rate: float = 1.0, capacity: int = 1) -> bool:
    key = f"ratelimit:{domain}"
    now = time.time()
    pipe = redis_client.pipeline()
    pipe.hgetall(key)
    pipe.execute()  # fetch current state

    result = redis_client.hgetall(key)
    tokens = float(result.get(b"tokens", capacity))
    last_refill = float(result.get(b"last_refill", now))

    elapsed = now - last_refill
    tokens = min(capacity, tokens + elapsed * refill_rate)

    if tokens >= 1.0:
        tokens -= 1.0
        redis_client.hset(key, mapping={"tokens": tokens, "last_refill": now})
        redis_client.expire(key, 3600)
        return True
    return False
```

This is a leaky bucket approximation. For strict crawl-delay compliance, prefer a simpler approach: store `last_fetch_time` per domain and enforce `now - last_fetch_time >= crawl_delay`.

## Frontier Priority: BFS vs. Priority Queue

BFS (FIFO queue) is the default and correct choice for site audits — it discovers shallow pages first, which are usually more important for SEO.

Use a **priority queue** only when:
- You have a relevance score per URL (e.g., anchor text contains target keyword)
- You are recrawling and want to prioritize recently-changed pages

Priority queue in Redis using sorted sets:

```python
# Score: lower = higher priority (depth works directly)
redis_client.zadd("frontier:priority", {url: depth})

# Dequeue lowest-score item
items = redis_client.zpopmin("frontier:priority", count=1)
```

## Worker State Machine

Each worker runs this loop:

```
┌──────────────────────────────────────────────────────┐
│  IDLE → dequeue URL from assigned sub-queue          │
│  CHECK → robots.txt allowed? scope check? seen?      │
│  WAIT → enforce crawl-delay (token bucket)           │
│  FETCH → HTTP GET with timeout (default 10s)         │
│  PARSE → extract links + metadata                    │
│  STORE → write result to output store                │
│  ENQUEUE → push new URLs to frontier (if unseen)     │
│  → back to IDLE                                      │
└──────────────────────────────────────────────────────┘
```

If the sub-queue is empty, a worker does **not** immediately terminate — it polls with exponential backoff (1s, 2s, 4s, max 30s) to handle the case where other workers are about to produce new URLs. Terminate only when the queue has been empty for N consecutive polls (N = 3 is reasonable).

## robots.txt in a Distributed Setting

Each domain's robots.txt must be fetched once and shared across workers. Cache it in Redis with a TTL matching the crawl duration (typically 1 hour):

```python
def get_robots(redis_client, domain: str, user_agent: str) -> RobotFileParser:
    cache_key = f"robots:{domain}"
    cached = redis_client.get(cache_key)
    if cached:
        parser = RobotFileParser()
        parser.parse(cached.decode().splitlines())
        return parser

    url = f"https://{domain}/robots.txt"
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": user_agent})
        content = resp.text if resp.status_code == 200 else ""
    except Exception:
        content = ""

    redis_client.setex(cache_key, 3600, content)
    parser = RobotFileParser()
    parser.parse(content.splitlines())
    return parser
```

**IRON LAW reinforcement**: every worker checks robots.txt before every fetch. Caching robots.txt in Redis means all workers share one authoritative copy — a late robots.txt update will be picked up after TTL expiry.

## Output Storage

For distributed crawls, write results to a shared store rather than local files. Append-only writes avoid merge conflicts:

| Option | Use Case | Notes |
|--------|----------|-------|
| Redis LIST | Small crawls, fast access | Fits in memory; no persistence by default |
| PostgreSQL | Structured queries needed | Use `INSERT ON CONFLICT DO NOTHING` on URL as PK |
| S3 / object store | Large-scale, raw HTML needed | One object per page; key = `sha256(url)` |
| Apache Kafka | Stream processing downstream | Workers produce, consumers index/analyze |

For most SEO site audits, PostgreSQL with this schema is sufficient:

```sql
CREATE TABLE pages (
    url TEXT PRIMARY KEY,
    status_code INT,
    title TEXT,
    depth INT,
    links_out INT,
    crawled_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE links (
    source_url TEXT,
    target_url TEXT,
    PRIMARY KEY (source_url, target_url)
);
```

## Failure Handling

**Worker crash**: URLs dequeued but not processed are lost unless you use a reliable queue pattern. With Redis, use `BRPOPLPUSH` to move a URL from the main queue to a worker-specific in-progress list. On startup, a worker re-enqueues any URLs left in its in-progress list from a prior crash.

```python
# Reliable dequeue: atomically move to in-progress list
url = redis_client.brpoplpush("frontier:worker:3", "inprogress:worker:3", timeout=5)
# ... process url ...
redis_client.lrem("inprogress:worker:3", 1, url)  # remove on success
```

**Fetch timeout**: retry up to 3 times with exponential backoff (2s, 4s, 8s). After 3 failures, write to an error log and continue — do not block the frontier.

**Memory pressure**: cap the seen set. At 10 bytes per URL hash (using SHA-1 truncated to 80 bits), 10 million URLs costs ~100MB. If that exceeds Redis budget, use a Bloom filter for the seen set — false positives cause a URL to be skipped, not recrawled. Acceptable for large-scale crawls where completeness is less critical than memory.

## Worked Example: 5-Worker Crawl of a 100k-Page Site

**Setup:**
- 5 workers, domain-affinity routing, 1 req/s per domain
- Redis for frontier + seen set + robots.txt cache
- PostgreSQL for output

**Expected throughput:**
- Each worker handles ~20 domains → 20 req/s per worker
- Total: 100 req/s across cluster
- 100k pages / 100 req/s = ~1,000 seconds (~17 minutes)

**Bottlenecks to watch:**
1. Redis throughput: `SADD` + `RPUSH` per URL discovered. At 15 links per page × 100 req/s = 1,500 Redis ops/sec — well within single Redis instance limits (~100k ops/sec).
2. PostgreSQL write rate: 100 inserts/sec is trivial; only an issue if storing raw HTML (use S3 instead).
3. DNS resolution: cache DNS results per worker process to avoid repeated lookups on the same domain.

**Scaling further**: adding workers beyond the number of distinct domains provides no benefit under domain-affinity routing. The effective parallelism cap is `min(num_workers, num_domains)`.
