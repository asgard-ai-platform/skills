# URL Normalization for Web Crawlers

URL normalization is the process of converting semantically equivalent URLs into a single canonical form so that the crawler's visited-set deduplication works correctly. Without it, `http://Example.COM/path/` and `http://example.com/path` are treated as distinct pages and crawled twice.

---

## Normalization Pipeline

Apply steps in this exact order. Later steps depend on output from earlier steps.

```
Input URL string
  → 1. Parse into components
  → 2. Scheme normalization
  → 3. Host normalization
  → 4. Port normalization
  → 5. Path normalization
  → 6. Query normalization
  → 7. Fragment stripping
  → 8. Trailing slash normalization
  → 9. Re-serialize
Output: canonical URL string
```

---

## Step 1: Parse into Components

Before any normalization, decompose the URL into its RFC 3986 components:

```
scheme://[userinfo@]host[:port]/path[?query][#fragment]
```

Use a proper URL parser, not string splitting. Python's `urllib.parse.urlparse` or Node's `new URL()` are both correct. Do not hand-roll a regex parser — edge cases (IPv6 hosts, percent-encoded colons in paths) will break it.

```python
from urllib.parse import urlparse, urlunparse, urlencode, parse_qsl

def parse(url: str):
    return urlparse(url)
```

---

## Step 2: Scheme Normalization

**Rule:** Lowercase the scheme.

```
HTTP://example.com  →  http://example.com
HTTPS://example.com →  https://example.com
```

RFC 3986 §3.1: "An implementation should accept uppercase letters as equivalent to lowercase in scheme names."

Do not normalize `http` → `https`. That changes semantics (different server, different content). Only case-fold; do not upgrade.

---

## Step 3: Host Normalization

**Rule:** Lowercase the entire host. For internationalized domain names (IDN), convert to ACE (ASCII Compatible Encoding) form.

```
Example.COM        →  example.com
WWW.EXAMPLE.COM    →  www.example.com
例え.jp (IDN)      →  xn--r8jz45g.jp
```

```python
import idna

def normalize_host(host: str) -> str:
    host = host.lower()
    # Strip brackets from IPv6 literals before processing
    if host.startswith('['):
        return host  # IPv6: [::1] — don't modify
    try:
        return idna.encode(host, alabel_round_trip=True).decode('ascii')
    except (idna.core.InvalidCodepoint, UnicodeError):
        return host  # fall back; log for inspection
```

**IPv4 and IPv6:** Do not normalize IP addresses — `127.1` is technically valid but not equivalent to `127.0.0.1` in all contexts. Treat them as-is; only lowercase the brackets and hex digits of IPv6.

---

## Step 4: Port Normalization

**Rule:** Remove the port if it is the default port for the scheme.

| Scheme  | Default Port |
|---------|-------------|
| http    | 80           |
| https   | 443          |
| ftp     | 21           |

```
http://example.com:80/path   →  http://example.com/path
https://example.com:443/     →  https://example.com/
http://example.com:8080/     →  http://example.com:8080/  (non-default, keep)
```

```python
DEFAULT_PORTS = {'http': 80, 'https': 443, 'ftp': 21}

def normalize_port(scheme: str, netloc: str) -> str:
    host, _, port = netloc.rpartition(':')
    if port.isdigit() and int(port) == DEFAULT_PORTS.get(scheme):
        return host
    return netloc
```

---

## Step 5: Path Normalization

### 5a. Percent-encoding normalization

Percent-encoded characters that represent unreserved characters (A–Z, a–z, 0–9, `-`, `.`, `_`, `~`) must be decoded. Reserved characters that are percent-encoded for structural reasons must stay encoded. Unknown or required encoding must be uppercased.

RFC 3986 §2.3 unreserved characters:
```
ALPHA / DIGIT / "-" / "." / "_" / "~"
```

```
/path/%2F/page    →  /path/%2F/page  (/ is reserved, keep encoded)
/path/%41page     →  /path/Apage     (A is unreserved, decode)
/path/%3a/page    →  /path/%3A/page  (: reserved, uppercase hex digits)
```

```python
import re
from urllib.parse import unquote_to_bytes

UNRESERVED = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~')

def normalize_percent_encoding(path: str) -> str:
    def replace(m):
        char = chr(int(m.group(1), 16))
        if char in UNRESERVED:
            return char
        return m.group(0).upper()
    return re.sub(r'%([0-9A-Fa-f]{2})', replace, path)
```

### 5b. Dot-segment removal

RFC 3986 §5.2.4 defines the algorithm for removing `.` and `..` segments.

```
/a/b/c/./../../g   →  /a/g
/a/b/../c          →  /a/c
/./path            →  /path
```

Python's `posixpath.normpath` handles this, but beware: it collapses `//` and strips trailing slashes. Use `urllib.parse` resolve instead:

```python
from urllib.parse import urljoin

def remove_dot_segments(base: str, path: str) -> str:
    # urljoin correctly resolves dot segments per RFC 3986
    return urljoin(base, path)
```

Or use the RFC algorithm directly:

```python
def remove_dot_segments(path: str) -> str:
    output = []
    while path:
        if path.startswith('../'):
            path = path[3:]
        elif path.startswith('./'):
            path = path[2:]
        elif path.startswith('/./'):
            path = '/' + path[3:]
        elif path == '/.':
            path = '/'
        elif path.startswith('/../'):
            path = '/' + path[4:]
            if output:
                output.pop()
        elif path == '/..':
            path = '/'
            if output:
                output.pop()
        elif path in ('.', '..'):
            path = ''
        else:
            seg_end = path.index('/', 1) if '/' in path[1:] else len(path)
            output.append(path[:seg_end])
            path = path[seg_end:]
    return ''.join(output)
```

### 5c. Empty path

If the path is empty after normalization and the URL has an authority (host), set the path to `/`.

```
http://example.com   →  http://example.com/
```

---

## Step 6: Query Normalization

### 6a. Sort query parameters

Sorting makes `?b=2&a=1` and `?a=1&b=2` identical. This is a **heuristic** — some servers treat parameter order as meaningful (rare but real). For general crawling, sort.

```
?page=2&sort=asc&filter=active  →  ?filter=active&page=2&sort=asc
```

```python
def normalize_query(query: str) -> str:
    if not query:
        return ''
    params = parse_qsl(query, keep_blank_values=True)
    params.sort(key=lambda kv: kv[0])
    return urlencode(params)
```

### 6b. Remove session and tracking parameters

These parameters make every URL unique per user/session, creating infinite URL space. Maintain a blocklist:

```python
STRIP_PARAMS = {
    # Session identifiers
    'jsessionid', 'phpsessid', 'aspsessionid', 'sid', 'sessionid',
    # Analytics tracking
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'fbclid', 'gclid', 'msclkid', 'mc_cid', 'mc_eid',
    # Common noise
    'ref', 'referrer', '_ga',
}

def strip_tracking_params(query: str) -> str:
    params = [(k, v) for k, v in parse_qsl(query, keep_blank_values=True)
              if k.lower() not in STRIP_PARAMS]
    return urlencode(sorted(params))
```

**Warning:** Do not strip parameters that change page content. `?page=2` and `?lang=fr` are structurally important. Only strip parameters known to be session/tracking identifiers.

### 6c. Empty query

If the query string is empty after normalization, remove the `?` entirely.

```
http://example.com/path?   →  http://example.com/path
```

---

## Step 7: Fragment Stripping

Fragments (`#section`) are never sent to the server. Two URLs differing only by fragment resolve to the same server-side resource.

```
http://example.com/page#section2  →  http://example.com/page
http://example.com/page#top       →  http://example.com/page
```

**Exception:** Single-page applications (SPAs) sometimes use hash-based routing where `#/products` and `#/cart` are different pages rendered client-side. This requires a headless browser — a plain HTTP crawler cannot distinguish them anyway, so strip fragments regardless and handle SPAs separately.

---

## Step 8: Trailing Slash Normalization

This is the most contested step. The canonical rule for a general crawler:

| Path          | Rule                              | Result       |
|---------------|-----------------------------------|--------------|
| `/`           | Root path — keep                  | `/`          |
| `/path/`      | Non-root with trailing slash      | `/path`      |
| `/path`       | Already normalized                | `/path`      |
| `/path.html`  | Has file extension — never touch  | `/path.html` |

```python
def normalize_trailing_slash(path: str) -> str:
    if path == '/' or '.' in path.rsplit('/', 1)[-1]:
        return path
    return path.rstrip('/')
```

**Why this is contested:** Some servers return different content for `/path/` vs `/path`, making them genuinely different resources. When in doubt, preserve the trailing slash as found. The rule above is safe for deduplication because:
1. A correctly configured server 301-redirects one form to the other.
2. Following the redirect will naturally converge to one canonical form.
3. Only apply this normalization to URLs *extracted from links*, not to the seed URL the user provided.

---

## Step 9: Re-serialize

Reassemble from normalized components:

```python
def normalize_url(url: str) -> str | None:
    try:
        p = urlparse(url.strip())
    except Exception:
        return None

    if p.scheme not in ('http', 'https'):
        return None  # discard mailto:, javascript:, data:, etc.

    scheme = p.scheme.lower()
    netloc = normalize_host_and_port(scheme, p.netloc)
    path = normalize_percent_encoding(remove_dot_segments(p.path or '/'))
    path = normalize_trailing_slash(path)
    query = strip_tracking_params(normalize_query(p.query))
    fragment = ''  # always strip

    return urlunparse((scheme, netloc, path, '', query, fragment))
```

---

## Worked Example

Input URL extracted from a page:

```
HTTP://WWW.Example.COM:80/About/../Products/./item%41?utm_source=google&page=2&fbclid=xyz#reviews
```

Step-by-step:

| Step | Result |
|------|--------|
| Parse | scheme=HTTP, host=WWW.Example.COM, port=80, path=/About/../Products/./item%41, query=utm_source=google&page=2&fbclid=xyz, fragment=reviews |
| Scheme | http |
| Host | www.example.com |
| Port | 80 = default for http → remove |
| Path dot-segments | /Products/itemA (decoded %41→A, removed ../and ./) |
| Percent encoding | /Products/itemA (A is unreserved, already decoded) |
| Trailing slash | /Products/itemA (no trailing slash) |
| Strip tracking params | page=2 (removed utm_source, fbclid) |
| Sort query | page=2 |
| Strip fragment | (removed) |
| **Output** | **http://www.example.com/Products/itemA?page=2** |

---

## Canonicalization vs. Normalization

These terms are sometimes conflated:

| Term | Meaning | Who decides |
|------|---------|-------------|
| **Normalization** | Mechanical RFC 3986 equivalence (this document) | RFC rules |
| **Canonicalization** | Which URL is the "preferred" version when multiple are valid | Site owner (via `<link rel="canonical">` or 301 redirects) |

A crawler should **normalize first**, then **follow 301 redirects** (which express the site's own canonicalization), then **respect `<link rel="canonical">`** tags in the HTML. Do not skip the mechanical normalization step even if you plan to follow canonicalization signals — normalization is a prerequisite for correct deduplication.

---

## URL Scope Filtering

After normalization, apply scope checks **in this order** (short-circuit on first match):

```python
def in_scope(url: str, seed_domain: str, robots, config) -> bool:
    p = urlparse(url)
    # 1. Scheme must be http or https
    if p.scheme not in ('http', 'https'):
        return False
    # 2. Must be within configured domain scope
    if config.scope == 'same-domain' and p.netloc != seed_domain:
        return False
    if config.scope == 'subdomain' and not p.netloc.endswith('.' + seed_domain):
        if p.netloc != seed_domain:
            return False
    # 3. Robots.txt
    if not robots.can_fetch(config.user_agent, url):
        return False
    # 4. Path pattern traps (calendar, session IDs, etc.)
    if is_trap_url(url):
        return False
    return True
```

---

## Common Trap URL Patterns

These URL patterns generate infinite URL spaces. Detect and skip before adding to the frontier:

```python
import re

TRAP_PATTERNS = [
    re.compile(r'/\d{4}/\d{2}/\d{2}/'),          # /2024/01/15/ calendar paths
    re.compile(r'[?&](s|search|q)='),              # search result pages
    re.compile(r'[?&](page|p|offset)=\d{3,}'),    # page numbers > 99
    re.compile(r'/(tag|label|category)/[^/]+/page/\d+'),  # paginated taxonomies
    re.compile(r'[?&]sessionid=[a-f0-9]{20,}'),   # session IDs in query
    re.compile(r';jsessionid=[A-Z0-9]{20,}'),      # Java session IDs in path
    re.compile(r'/print/'),                         # print versions of pages
    re.compile(r'\.(pdf|jpg|jpeg|png|gif|css|js|ico|woff|woff2|ttf|svg|xml|zip)$', re.I),
]

def is_trap_url(url: str) -> bool:
    return any(p.search(url) for p in TRAP_PATTERNS)
```

---

## Reference: RFC 3986 Sections

| Topic | RFC 3986 Section |
|-------|-----------------|
| Scheme syntax | §3.1 |
| Unreserved characters | §2.3 |
| Reserved characters | §2.2 |
| Percent-encoding | §2.1 |
| Dot-segment removal algorithm | §5.2.4 |
| Normalization and comparison | §6 |
| Case normalization | §6.2.2.1 |
| Percent-encoding normalization | §6.2.2.2 |
| Path segment normalization | §6.2.2.3 |
