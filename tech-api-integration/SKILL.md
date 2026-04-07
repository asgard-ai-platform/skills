---
name: "tech-api-integration"
description: "Guide REST API integration including HTTP methods, authentication, error handling, and rate limiting. Use this skill when the user needs to connect to a third-party API, design an API client, troubleshoot API errors, or understand API concepts — even if they say 'connect to this API', 'why is the API returning errors', 'how do I authenticate', or 'build an API integration'."
metadata:
  category: "WP-11 通用技術"
  tags: ["technology", "api", "rest", "integration"]
---

# REST API Integration Guide

## Framework

```
IRON LAW: Read the Docs, Then Build, Then Handle Errors

1. Read the API documentation completely (auth, endpoints, rate limits, errors)
2. Get a successful request working in isolation (curl/Postman)
3. Build error handling BEFORE building features

Skipping step 1 wastes hours on trial-and-error. Skipping step 3
creates fragile integrations that break silently in production.
```

### HTTP Methods

| Method | Purpose | Idempotent? | Example |
|--------|---------|------------|---------|
| GET | Read data | Yes | `GET /users/123` |
| POST | Create new resource | No | `POST /users` + body |
| PUT | Replace entire resource | Yes | `PUT /users/123` + full body |
| PATCH | Update partial resource | Yes | `PATCH /users/123` + partial body |
| DELETE | Remove resource | Yes | `DELETE /users/123` |

### Status Codes

| Range | Meaning | Common Codes |
|-------|---------|-------------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Moved, 304 Not Modified |
| 4xx | Client error (your fault) | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests |
| 5xx | Server error (their fault) | 500 Internal, 502 Bad Gateway, 503 Service Unavailable |

### Authentication Types

| Type | How It Works | When Used |
|------|-------------|----------|
| **API Key** | Key in header or query param | Simple APIs, server-to-server |
| **Bearer Token** | `Authorization: Bearer <token>` | OAuth 2.0, JWT-based APIs |
| **OAuth 2.0** | Token exchange flow (authorize → token → API call) | User-delegated access (Google, FB) |
| **Basic Auth** | Base64(username:password) in header | Legacy, internal APIs |
| **HMAC Signature** | Sign request with secret key | Payment gateways, high-security |

### Error Handling Strategy

```
try:
    response = api.call(request)
    if response.status == 429:  # Rate limited
        wait(response.headers['Retry-After'])
        retry()
    elif response.status >= 500:  # Server error
        retry_with_backoff(max_retries=3)
    elif response.status >= 400:  # Client error
        log_error(response.body)
        raise ClientError(response.body['message'])
    else:
        return response.json()
```

### Rate Limiting

| Strategy | How |
|----------|-----|
| Respect `Retry-After` header | Wait the specified seconds before retrying |
| Exponential backoff | Wait 1s, 2s, 4s, 8s between retries |
| Token bucket | Track request count, pause when approaching limit |
| Queue requests | Use a job queue (Celery, Bull) for high-volume integrations |

### Integration Checklist

1. [ ] Read API documentation completely
2. [ ] Test auth flow (get valid token/key)
3. [ ] Test each endpoint with curl/Postman first
4. [ ] Implement error handling for all status code ranges
5. [ ] Implement rate limit handling
6. [ ] Implement retry logic with backoff
7. [ ] Log all requests and responses (redact secrets)
8. [ ] Handle API versioning (pin to specific version)
9. [ ] Set timeouts (connect: 5s, read: 30s)
10. [ ] Monitor for API deprecation notices

## Output Format

```markdown
# API Integration Plan: {API Name}

## API Overview
- Base URL: {url}
- Auth: {type}
- Rate limit: {N requests/period}
- Documentation: {link}

## Endpoints Used
| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| {path} | GET/POST | {what it does} | {auth type} |

## Error Handling
| Error | Response | Our Action |
|-------|----------|-----------|
| 401 | Unauthorized | Refresh token, retry |
| 429 | Rate limited | Backoff, retry after Retry-After |
| 500 | Server error | Retry 3x with exponential backoff |

## Implementation Timeline
| Phase | Task | Duration |
|-------|------|----------|
| 1 | Auth + basic call | {days} |
| 2 | Full integration | {days} |
| 3 | Error handling + monitoring | {days} |
```

## Gotchas

- **Sandbox vs production**: Most APIs have a sandbox/test environment. Build and test there first. Production API keys should never be in code.
- **Pagination**: APIs return paginated results. Handle all pages, not just the first. Check for `next_page` token or `offset` parameter.
- **Webhook reliability**: If using webhooks, implement idempotent handlers (same event received twice should not duplicate data). Store event IDs to deduplicate.
- **API changes break things**: Pin to a specific API version. Subscribe to the provider's changelog/deprecation notices.
- **Secrets management**: API keys and tokens NEVER in source code. Use environment variables or a secrets manager (AWS Secrets Manager, HashiCorp Vault).

## References

- For OAuth 2.0 flow details, see `references/oauth-guide.md`
- For webhook implementation patterns, see `references/webhook-patterns.md`
