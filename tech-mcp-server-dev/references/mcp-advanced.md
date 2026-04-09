# MCP Advanced Patterns: Resources, Prompts, and Subscriptions

## Resources

Resources let your MCP server expose *readable data* — think of them as files or database records the model can pull into context without invoking a full tool call. Unlike tools (which perform actions), resources are read-only and identified by URI.

### When to Use Resources vs. Tools

| Use Resources when... | Use Tools when... |
|----------------------|-------------------|
| The data is relatively static (config, docs, schema) | The model needs to search/filter/query |
| You want Claude Code to index the content automatically | The operation has side effects |
| The URI is stable and predictable | Parameters vary at call time |
| Content is large but the model may read only part of it | You need error handling logic |

**Practical rule**: if the data fits in a `GET /resource/{id}` mental model, use a resource. If it fits in a `POST /query` mental model, use a tool.

### Resource Definition (TypeScript)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "my-server", version: "1.0.0" });

// Static resource — content known at registration time
server.resource(
  "db-schema",
  "schema://database",
  async (uri) => ({
    contents: [{
      uri: uri.href,
      mimeType: "text/plain",
      text: await readDatabaseSchema()   // returns DDL as string
    }]
  })
);
```

### Dynamic Resource Templates (URI Templates)

When the set of resources is open-ended (e.g., one resource per customer), use a URI template:

```typescript
import { ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

server.resource(
  "customer-profile",
  new ResourceTemplate("customers://{customer_id}/profile", { list: undefined }),
  async (uri, { customer_id }) => {
    const customer = await db.customers.findById(customer_id);
    if (!customer) {
      throw new Error(`Customer ${customer_id} not found`);
    }
    return {
      contents: [{
        uri: uri.href,
        mimeType: "application/json",
        text: JSON.stringify(customer, null, 2)
      }]
    };
  }
);
```

URI template variables (`{customer_id}`) are extracted automatically and passed as the second argument.

### Listable Resources

If you want `resources/list` to enumerate available resources (so Claude Code can index them), provide a `list` handler:

```typescript
server.resource(
  "runbooks",
  new ResourceTemplate("runbooks://{slug}", {
    list: async () => ({
      resources: await db.runbooks.findAll().map(r => ({
        uri: `runbooks://${r.slug}`,
        name: r.title,
        description: r.summary,
        mimeType: "text/markdown"
      }))
    })
  }),
  async (uri, { slug }) => { /* ... */ }
);
```

Omit `list` (pass `undefined`) for resources where enumeration is impractical (e.g., `customers://{id}` — you don't want to list all customers upfront).

---

## Prompts

Prompts are pre-built, parameterized message sequences. The model can request them via `prompts/get`; Claude Code surfaces them as slash commands (e.g., `/mcp__my-server__analyze-customer`).

### When to Use Prompts

- Repeated, structured workflows: "generate a weekly sales summary", "review this PR for security issues"
- Domain-specific framing: you want to inject system context, persona, or chain-of-thought scaffolding before the model responds
- Reducing prompt re-entry: the user picks the prompt by name; the server fills in the boilerplate

### Prompt Definition (Python)

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("analytics-server")

@mcp.prompt()
def sales_summary(region: str, period: str) -> list[dict]:
    """
    Generate a structured sales performance summary.
    
    Use this prompt when the user wants a formal sales report
    for a specific region and time period.
    """
    return [
        {
            "role": "user",
            "content": (
                f"Generate a sales performance summary for region '{region}' "
                f"covering {period}. Structure the output as:\n"
                "1. Executive Summary (3 sentences)\n"
                "2. Key Metrics Table (revenue, units, growth %)\n"
                "3. Top 3 wins\n"
                "4. Top 3 risks\n"
                "5. Recommended actions\n\n"
                "Use the get_sales_data tool to retrieve actual numbers before writing."
            )
        }
    ]
```

### Multi-Turn Prompt (Injecting System Context)

```python
@mcp.prompt()
def debug_pipeline(pipeline_name: str) -> list[dict]:
    """Structured debugging session for a named data pipeline."""
    return [
        {
            "role": "user",
            "content": (
                f"I need to debug the '{pipeline_name}' pipeline. "
                "Please:\n"
                "1. Call get_pipeline_status to check current state\n"
                "2. Call get_recent_errors to fetch the last 20 errors\n"
                "3. Identify the root cause pattern\n"
                "4. Propose a fix with the exact code change needed"
            )
        }
    ]
```

**Important**: Prompts don't execute tools — they emit message sequences that instruct the model to call tools. The model still decides how to act; the prompt just provides the framework.

---

## Subscriptions and Change Notifications

MCP supports server-sent notifications for resources that change over time. This is useful for live dashboards, log tails, or monitoring scenarios.

### How Notifications Work

```
Client                          Server
  │                               │
  │── resources/subscribe ───────►│
  │                               │  (resource changes)
  │◄── notifications/resources/  ─│
  │    updated                    │
  │                               │
  │── resources/read ────────────►│  (client re-fetches)
  │◄── resource contents ─────────│
```

The server does not push content — it pushes a change signal, and the client decides when to re-read.

### Implementing Subscriptions (TypeScript)

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "monitor", version: "1.0.0" });

// Track active subscriptions
const subscribers = new Set<string>();

server.resource(
  "system-metrics",
  "metrics://current",
  async (uri) => ({
    contents: [{
      uri: uri.href,
      mimeType: "application/json",
      text: JSON.stringify(await collectMetrics())
    }]
  })
);

// Notify subscribers every 30 seconds
setInterval(async () => {
  if (subscribers.size > 0) {
    await server.server.sendResourceUpdated({ uri: "metrics://current" });
  }
}, 30_000);
```

**Practical note**: Most Claude Code integrations don't poll subscriptions interactively. Reserve subscriptions for server implementations that have a long-lived client (custom agents, persistent Claude sessions).

---

## Tool Result Streaming (Large Outputs)

When a tool may return large amounts of text (e.g., log fetch, full document), prefer pagination over returning everything at once.

### Cursor-Based Pagination Pattern

```python
@mcp.tool()
async def get_logs(
    service: str,
    cursor: str | None = None,
    limit: int = 50
) -> dict:
    """
    Fetch recent logs for a service.
    
    Parameters:
      service: Service name (e.g., 'api-gateway', 'worker')
      cursor:  Pagination cursor from previous call (omit for first page)
      limit:   Number of log lines to return (max 100, default 50)
    
    Returns:
      { logs: [...], next_cursor: "..." | null, total_count: N }
    """
    rows, next_cursor = await db.logs.paginate(
        service=service,
        after_cursor=cursor,
        limit=min(limit, 100)
    )
    return {
        "logs": [{"timestamp": r.ts, "level": r.level, "message": r.msg} for r in rows],
        "next_cursor": next_cursor,
        "has_more": next_cursor is not None
    }
```

The model will call this tool again with `cursor=next_cursor` if it needs more logs. Describe `next_cursor` and `has_more` in the schema so the model knows to paginate.

---

## Composing Multiple Servers in .mcp.json

When a project needs multiple servers, they compose naturally:

```json
{
  "mcpServers": {
    "database": {
      "command": "python",
      "args": ["-m", "my_project.mcp_db"],
      "env": { "DATABASE_URL": "${DATABASE_URL}" }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}" }
    },
    "slack": {
      "command": "node",
      "args": ["slack-mcp/index.js"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    }
  }
}
```

**Naming collision rule**: if two servers define a tool with the same name, Claude Code prefixes them (`database__search` vs `github__search`). Design tool names to be distinctive even without the prefix — the model sees the full prefixed name but humans read only the bare name.

---

## Authentication Patterns

### API Key via Environment Variable (Standard)

```python
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("external-api")

API_KEY = os.environ.get("EXTERNAL_API_KEY")
if not API_KEY:
    raise RuntimeError("EXTERNAL_API_KEY environment variable is required")
```

Fail at startup, not at call time. The error surfaces immediately during `claude mcp add` testing rather than silently at tool call.

### OAuth Token Refresh Pattern

For APIs with expiring tokens, keep the token outside tool handlers:

```python
import time, httpx

_token_cache = {"token": None, "expires_at": 0}

async def get_token() -> str:
    if time.time() < _token_cache["expires_at"] - 60:   # 60s buffer
        return _token_cache["token"]
    
    resp = await httpx.AsyncClient().post(
        "https://auth.example.com/token",
        data={"grant_type": "client_credentials",
              "client_id": os.environ["CLIENT_ID"],
              "client_secret": os.environ["CLIENT_SECRET"]}
    )
    resp.raise_for_status()
    data = resp.json()
    _token_cache["token"] = data["access_token"]
    _token_cache["expires_at"] = time.time() + data["expires_in"]
    return _token_cache["token"]

@mcp.tool()
async def call_protected_api(endpoint: str) -> dict:
    token = await get_token()
    # ...
```

---

## Error Response Conventions

The SKILL.md Iron Law requires errors to be *model-readable*. Advanced pattern: use structured error codes so the model can retry intelligently.

```python
from mcp.types import TextContent

def tool_error(code: str, message: str, retryable: bool = False) -> list[TextContent]:
    """Return a structured error that the model can parse and act on."""
    return [TextContent(
        type="text",
        text=json.dumps({
            "error": True,
            "code": code,
            "message": message,
            "retryable": retryable,
            "hint": RETRY_HINTS.get(code, "Check parameters and try again")
        })
    )]

RETRY_HINTS = {
    "RATE_LIMITED":    "Wait 5 seconds then retry with the same parameters",
    "NOT_FOUND":       "Verify the ID exists by calling search first",
    "PERMISSION":      "This operation requires admin role; inform the user",
    "VALIDATION":      "Check the parameter types and required fields",
    "TIMEOUT":         "The database is slow; try a narrower query (smaller limit, tighter date range)",
}

# Usage inside a tool handler:
@mcp.tool()
async def get_order(order_id: str) -> list[TextContent]:
    try:
        order = await db.orders.get(order_id)
        if order is None:
            return tool_error("NOT_FOUND", f"No order with ID '{order_id}'")
        return [TextContent(type="text", text=json.dumps(order))]
    except TimeoutError:
        return tool_error("TIMEOUT", "Database query timed out", retryable=True)
```

---

## Capability Declaration (Server Info)

When registering, declare which optional MCP capabilities your server uses. Clients use this to know what to negotiate:

```typescript
const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
}, {
  capabilities: {
    resources: { subscribe: true, listChanged: true },
    tools: {},
    prompts: { listChanged: false },
    logging: {}
  }
});
```

Omit capabilities you don't implement — declaring `subscribe: true` without implementing the subscription handler causes client errors.

---

## Minimal Working Server Checklist

Before shipping to `.mcp.json`:

- [ ] `server.name` matches the key in `.mcp.json` (affects tool prefix)
- [ ] Every tool has `name`, `description`, and `inputSchema` with `required` array
- [ ] Secrets come from `env` block, not hardcoded
- [ ] Tool handlers never throw unhandled exceptions (wrap in try/catch, return error JSON)
- [ ] Large results are paginated (default limit ≤ 20, hard cap ≤ 100)
- [ ] Tested with at least 5 diverse natural-language prompts to verify the model calls the right tool
- [ ] Resources that list are explicitly marked `list: async () => ...`; those that don't are `list: undefined`
