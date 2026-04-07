---
name: "tech-mcp-server-dev"
description: "Build MCP (Model Context Protocol) servers including tool definition, schema design, authentication, error handling, and Claude Code integration. Use this skill when the user needs to create an MCP server, expose APIs or databases to AI agents, design tool schemas, or integrate with Claude Code — even if they say 'build an MCP server', 'connect Claude to our database', 'expose our API to AI', or 'create a tool for Claude Code'."
metadata:
  category: "WP-11 通用技術"
  tags: ["technology", "mcp", "claude-code", "ai-agents"]
---

# MCP Server Development

## Framework

```
IRON LAW: Tools Must Be Self-Describing

Every MCP tool must have a clear name, description, and input schema
that allows the AI model to understand WHEN and HOW to use it without
any external documentation. If the model can't figure out when to call
your tool from its name and description alone, the tool is poorly designed.
```

### MCP Architecture

```
Claude Code / AI Agent
    ↓ (stdio JSON-RPC 2.0)
MCP Server (your code)
    ↓
Your Data Source (DB, API, file system, etc.)
```

### Protocol Basics

| Concept | What It Is |
|---------|-----------|
| **Transport** | stdio (stdin/stdout) — most common for local servers |
| **Protocol** | JSON-RPC 2.0 |
| **Tools** | Functions the model can call (read data, take actions) |
| **Resources** | Data the model can read (files, database records) |
| **Prompts** | Pre-built prompt templates the model can use |

### Tool Design Principles

1. **Atomic operations**: Each tool does ONE thing. "search_users" not "search_and_update_users"
2. **Clear naming**: verb_noun format. "get_customer", "create_order", "search_products"
3. **Descriptive descriptions**: Include WHEN to use, not just what it does
4. **Strict schemas**: Define all parameters with types, descriptions, and required/optional
5. **Meaningful errors**: Return error messages the model can understand and act on

### Tool Schema Example

```json
{
  "name": "search_customers",
  "description": "Search for customers by name, email, or phone number. Use when the user asks to find or look up a specific customer.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term — can be customer name, email, or phone"
      },
      "limit": {
        "type": "number",
        "description": "Maximum results to return (default: 10)",
        "default": 10
      }
    },
    "required": ["query"]
  }
}
```

### Implementation Steps (Python/TypeScript)

**Phase 1: Setup**
1. Choose SDK: `@modelcontextprotocol/sdk` (TypeScript) or `mcp` (Python)
2. Define tools with schemas
3. Implement tool handlers
4. Test locally with `mcp dev` or `claude mcp add`

**Phase 2: Data Connection**
5. Connect to your data source (DB, API, etc.)
6. Implement authentication (env vars for secrets)
7. Add error handling for all data operations
8. Add logging for debugging

**Phase 3: Integration**
9. Configure in `.mcp.json` for Claude Code
10. Test with real queries
11. Add to project CLAUDE.md so Claude knows about available tools

### .mcp.json Configuration

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["path/to/server.js"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

### Error Handling

```
Tool handler should:
1. Validate input (check required fields, types)
2. Try the operation
3. On success: return structured data (JSON)
4. On error: return { "error": "Human-readable message", "code": "ERROR_CODE" }
   - NOT stack traces or internal error details
   - The MODEL needs to understand the error to retry or inform the user
```

## Output Format

```markdown
# MCP Server Spec: {Server Name}

## Purpose
{What data/capability this server exposes}

## Tools
| Tool | Description | Parameters | Returns |
|------|-----------|-----------|---------|
| {name} | {when to use} | {params} | {return type} |

## Data Source
- Type: {database / API / file system}
- Connection: {how to connect}
- Auth: {env vars needed}

## .mcp.json
```json
{config}
```

## Testing Plan
1. {test case for each tool}
```

## Gotchas

- **Environment variables for secrets**: NEVER hardcode API keys or database passwords. Use `env` in .mcp.json to pass secrets from environment variables.
- **Tool description quality**: The model decides whether to use your tool based SOLELY on the name + description. A bad description means the tool never gets called (or gets called for wrong reasons).
- **Return data size**: Don't return 10,000 rows. The model's context window is limited. Return summarized or paginated results. Default limit = 10-20 items.
- **Idempotent reads, confirmed writes**: Read operations should be safe to call multiple times. Write operations (create, update, delete) should confirm with the user before execution.
- **Test with real model interactions**: Unit tests aren't enough. The real test is whether Claude actually uses your tool correctly in conversation. Test with diverse prompts.

## References

- For MCP SDK documentation, see `references/mcp-sdk.md`
- For advanced MCP patterns (resources, prompts), see `references/mcp-advanced.md`
