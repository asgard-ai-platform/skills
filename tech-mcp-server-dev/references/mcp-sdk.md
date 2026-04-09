# MCP SDK Reference

Covers the two official SDKs: TypeScript (`@modelcontextprotocol/sdk`) and Python (`mcp`). Both implement the same JSON-RPC 2.0 protocol over stdio; pick the language that matches your runtime.

---

## TypeScript SDK

### Install

```bash
npm install @modelcontextprotocol/sdk
```

### Minimal working server

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
});

// Register a tool
server.tool(
  "get_customer",                              // tool name
  "Look up a customer by ID. Use when the user asks about a specific customer.",
  {
    customer_id: z.string().describe("The customer's unique ID"),
  },
  async ({ customer_id }) => {
    const customer = await db.customers.findById(customer_id);
    if (!customer) {
      return {
        content: [{ type: "text", text: JSON.stringify({ error: "Customer not found", code: "NOT_FOUND" }) }],
      };
    }
    return {
      content: [{ type: "text", text: JSON.stringify(customer) }],
    };
  }
);

// Start
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Tool registration API

```typescript
server.tool(
  name: string,
  description: string,
  schema: ZodRawShape,          // Zod schema — SDK converts to JSON Schema automatically
  handler: (args) => Promise<CallToolResult>
)
```

`CallToolResult` shape:

```typescript
{
  content: Array<
    | { type: "text";  text: string }
    | { type: "image"; data: string; mimeType: string }
    | { type: "resource"; resource: { uri: string; text?: string; blob?: string } }
  >;
  isError?: boolean;  // set true when returning an error payload
}
```

### Zod schema patterns

```typescript
import { z } from "zod";

// Required string
z.string().describe("Search term")

// Optional with default
z.number().default(10).describe("Max results to return")

// Enum
z.enum(["asc", "desc"]).default("asc").describe("Sort direction")

// Optional field
z.string().optional().describe("Filter by status (omit to return all)")

// Nested object
z.object({
  name: z.string(),
  email: z.string().email(),
}).describe("Customer data to create")

// Array
z.array(z.string()).describe("List of IDs to fetch")
```

The SDK wraps these into `inputSchema` JSON Schema automatically — you never write raw JSON Schema by hand.

### Returning errors

```typescript
// DO: structured error the model can act on
return {
  content: [{ type: "text", text: JSON.stringify({
    error: "Customer not found",
    code: "NOT_FOUND",
    customer_id,
  })}],
  isError: true,
};

// DON'T: raw exception message
throw new Error("Database connection failed at line 47...");
```

Set `isError: true` so the model knows the call failed without having to parse the text content.

---

## Python SDK

### Install

```bash
pip install mcp
```

### Minimal working server

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def get_customer(customer_id: str) -> dict:
    """Look up a customer by ID. Use when the user asks about a specific customer."""
    customer = db.customers.find_by_id(customer_id)
    if not customer:
        return {"error": "Customer not found", "code": "NOT_FOUND"}
    return customer

if __name__ == "__main__":
    mcp.run()
```

FastMCP derives the tool name from the function name, and the description from the docstring. Parameter types and descriptions come from Python type hints and docstring sections.

### Documenting parameters with docstrings

FastMCP supports Google-style docstrings to attach descriptions to each parameter:

```python
@mcp.tool()
def search_customers(query: str, limit: int = 10, status: str | None = None) -> list[dict]:
    """Search for customers by name, email, or phone.

    Use when the user asks to find or look up a specific customer.

    Args:
        query: Search term — can be customer name, email, or phone
        limit: Maximum results to return
        status: Filter by account status (active/suspended). Omit to return all.
    """
    ...
```

This produces the correct `description` fields in the JSON Schema the SDK advertises to the model.

### Async handlers

```python
import asyncio
import httpx

@mcp.tool()
async def get_weather(city: str) -> dict:
    """Get current weather for a city."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://api.example.com/weather?city={city}")
        resp.raise_for_status()
        return resp.json()
```

Both sync and async functions work. Use async when calling external APIs or databases with async drivers.

### Error handling pattern

```python
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP("my-server")

@mcp.tool()
def get_order(order_id: str) -> dict:
    """Retrieve an order by ID."""
    try:
        order = db.orders.get(order_id)
        if order is None:
            return {"error": f"Order {order_id} not found", "code": "NOT_FOUND"}
        return order
    except DatabaseError as e:
        # Log internally, return safe message to model
        logger.error("DB error: %s", e)
        return {"error": "Database temporarily unavailable", "code": "DB_ERROR"}
```

Never let raw exceptions propagate to the model — the SDK will catch them and return an opaque error string. Return a structured dict instead.

---

## SDK Comparison

| Feature | TypeScript SDK | Python SDK (FastMCP) |
|---------|---------------|---------------------|
| Schema definition | Zod | Python type hints + docstrings |
| Async support | Native (async/await) | Native (async def) |
| Transport setup | Explicit `StdioServerTransport` | `mcp.run()` handles it |
| Resources | `server.resource()` | `@mcp.resource()` |
| Prompts | `server.prompt()` | `@mcp.prompt()` |
| Error return | `{ isError: true, content: [...] }` | Return dict with `"error"` key |
| Entry point | `await server.connect(transport)` | `mcp.run()` |

---

## Resources (read-only data)

Resources are data the model can read — think of them as files or records that appear in the model's context. Use resources for reference data; use tools for actions.

### TypeScript

```typescript
import { ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

// Static resource
server.resource(
  "config",
  "config://app",
  async (uri) => ({
    contents: [{ uri: uri.href, text: JSON.stringify(appConfig) }],
  })
);

// Parameterized resource template
server.resource(
  "customer-record",
  new ResourceTemplate("customers://{id}", { list: undefined }),
  async (uri, { id }) => {
    const customer = await db.customers.findById(id);
    return {
      contents: [{ uri: uri.href, text: JSON.stringify(customer) }],
    };
  }
);
```

### Python

```python
@mcp.resource("customers://{id}")
def customer_record(id: str) -> str:
    """A customer record."""
    customer = db.customers.find_by_id(id)
    return json.dumps(customer)
```

Resources vs. Tools decision rule:
- **Tool** → model triggers an action or query with parameters it chooses
- **Resource** → model reads a known piece of data by URI (stable address)

---

## Prompts

Pre-built prompt templates the model can invoke. Useful for complex, multi-step instructions that should be consistent across sessions.

### Python

```python
from mcp.types import UserMessage, TextContent

@mcp.prompt()
def analyze_customer(customer_id: str) -> list:
    """Analyze a customer's purchase history and suggest upsells."""
    return [
        UserMessage(content=TextContent(
            type="text",
            text=f"Please analyze customer {customer_id}: "
                 f"retrieve their orders, identify patterns, and suggest 3 upsell opportunities."
        ))
    ]
```

---

## Testing locally

### Option 1: MCP Inspector (browser UI)

```bash
# TypeScript
npx @modelcontextprotocol/inspector node path/to/server.js

# Python
npx @modelcontextprotocol/inspector python path/to/server.py
```

Opens a browser UI where you can call tools manually and inspect the JSON-RPC messages.

### Option 2: Claude Code CLI

```bash
# Add to Claude Code
claude mcp add my-server node path/to/server.js

# Verify it's registered
claude mcp list

# Remove if needed
claude mcp remove my-server
```

After adding, start a new Claude Code session — the tools appear automatically.

### Option 3: Raw stdio test

```bash
# Pipe a JSON-RPC request directly
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | node server.js
```

Expected response lists all registered tools with their schemas. If you get no output or a parse error, the server is crashing before it can respond.

---

## Environment variables for secrets

Never hardcode credentials. Pass them through `.mcp.json`:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["server.js"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}",
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

Read in TypeScript:
```typescript
const dbUrl = process.env.DATABASE_URL;
if (!dbUrl) throw new Error("DATABASE_URL is required");
```

Read in Python:
```python
import os
db_url = os.environ["DATABASE_URL"]  # raises KeyError if missing — fail fast at startup
```

Fail fast at startup (not at first tool call) so the error is obvious during setup rather than in the middle of a conversation.

---

## Pagination pattern

The model's context window is finite. Never return unbounded result sets.

```python
@mcp.tool()
def search_orders(
    query: str,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """Search orders by customer name or product.

    Args:
        query: Search term
        limit: Max results (1-50)
        offset: Pagination offset for fetching next page
    """
    limit = min(limit, 50)  # hard cap — never trust the model to stay within limits
    results = db.orders.search(query, limit=limit, offset=offset)
    total = db.orders.count(query)
    return {
        "results": results,
        "total": total,
        "offset": offset,
        "limit": limit,
        "has_more": (offset + limit) < total,
    }
```

Include `has_more` and `total` so the model knows whether to ask for the next page.

---

## Common startup errors

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `Cannot find module '@modelcontextprotocol/sdk'` | Package not installed | `npm install @modelcontextprotocol/sdk` |
| `ModuleNotFoundError: No module named 'mcp'` | Package not installed | `pip install mcp` |
| Server starts but no tools appear in Claude Code | Wrong entry point or crash at startup | Run with MCP Inspector; check stderr |
| Tool appears but model never calls it | Bad description | Rewrite description to include WHEN to use it |
| Tool called but returns empty | Handler throws and swallows exception | Add try/except and return error dict |
| `isError` not recognized | Using raw SDK (`Server`) not `McpServer` | Use `McpServer` from `server/mcp.js` |
