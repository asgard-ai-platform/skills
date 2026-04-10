直接用 Write tool 建立檔案（Write tool 不在上方可用工具列表中，我用 Bash 代替）。根據 CLAUDE.md，這個 repo 的結構是 `{skill}/examples/`，路徑應為 `tech-mcp-server-dev/examples/sample_scenario.md`。

由於我沒有直接的 Write/Edit 工具可用（這個環境只顯示了特定的 MCP 工具），讓我確認一下可用工具並輸出完整內容供使用者複製：

---

以下是 `tech-mcp-server-dev/examples/sample_scenario.md` 的完整內容，請直接寫入該路徑：

````markdown
# Example: Connecting a SaaS CRM to Claude Code

## Scenario

TalentBridge 是一家台灣本土的 HR 科技新創，旗下 SaaS 產品幫助中小企業管理招募流程。產品工程師 Vivian 收到需求：讓客戶成功（CS）團隊能在 Claude Code 裡直接查詢客戶資料、合約狀態、以及最近 30 天的使用量，省去每次都要登入後台撈資料的時間。

Vivian 的環境：

- 後端：Python FastAPI，PostgreSQL 資料庫
- 客戶資料表：`accounts`、`contracts`、`usage_events`
- 現有 REST API：`GET /accounts`、`GET /contracts?account_id=`、`GET /usage?account_id=&days=`
- 敏感欄位：合約金額、到期日、聯絡人 email

她的問題：「我要怎麼建一個 MCP server，讓 CS 同事可以在 Claude Code 裡問 'TechCorp 的合約還有多久到期？' 然後 Claude 就能直接回答？」

---

## Analysis

### Phase 1: Setup — 定義工具清單

Vivian 先列出 CS 團隊的高頻問題，反推需要哪些 tools：

| CS 問題 | 需要的 tool |
|---------|------------|
| 找客戶帳號 | `search_accounts` |
| 查合約狀態與到期日 | `get_contract` |
| 查最近使用量 | `get_usage_summary` |

> **決策**：不做 `search_and_get_contract` 這種合併 tool — 違反 atomic operations 原則。搜尋與查詢是兩個獨立動作，讓 model 自己串接。

**工具 Schema 設計：**

```json
[
  {
    "name": "search_accounts",
    "description": "Search for customer accounts by company name, domain, or contact email. Use when the user wants to find a specific customer or look up who a company is.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "query": {
          "type": "string",
          "description": "Company name, domain (e.g. techcorp.com), or contact email"
        },
        "limit": {
          "type": "number",
          "description": "Max results to return (default: 5)",
          "default": 5
        }
      },
      "required": ["query"]
    }
  },
  {
    "name": "get_contract",
    "description": "Get contract details for an account including plan type, MRR, expiry date, and renewal status. Use when the user asks about a customer's contract, subscription, pricing, or renewal.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "account_id": {
          "type": "string",
          "description": "Account ID from search_accounts results"
        }
      },
      "required": ["account_id"]
    }
  },
  {
    "name": "get_usage_summary",
    "description": "Get aggregated product usage for an account over the last N days. Use when the user asks about how active a customer is, feature adoption, or usage trends.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "account_id": {
          "type": "string",
          "description": "Account ID from search_accounts results"
        },
        "days": {
          "type": "number",
          "description": "Lookback window in days (default: 30, max: 90)",
          "default": 30
        }
      },
      "required": ["account_id"]
    }
  }
]
```

---

### Phase 2: Data Connection — Python 實作

**選擇 SDK**：`mcp` Python 套件（`pip install mcp`）

```python
# server.py
import os
import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

API_BASE = os.environ["TALENTBRIDGE_API_URL"]   # e.g. https://api.talentbridge.tw
API_KEY  = os.environ["TALENTBRIDGE_API_KEY"]   # 從 env var 注入，不寫死

app = Server("talentbridge-crm")
http = httpx.Client(
    base_url=API_BASE,
    headers={"X-API-Key": API_KEY},
    timeout=10.0
)

@app.list_tools()
async def list_tools():
    return [...]  # 上方三個 schema

@app.call_tool()
async def call_tool(name: str, arguments: dict):
    try:
        if name == "search_accounts":
            resp = http.get("/accounts", params={
                "q": arguments["query"],
                "limit": arguments.get("limit", 5)
            })
            resp.raise_for_status()
            accounts = resp.json()["data"]
            # 只回傳 CS 需要的欄位，避免 context 爆炸
            slim = [
                {"id": a["id"], "name": a["name"], "domain": a["domain"],
                 "plan": a["plan"], "status": a["status"]}
                for a in accounts
            ]
            return [types.TextContent(type="text", text=str(slim))]

        elif name == "get_contract":
            resp = http.get("/contracts", params={"account_id": arguments["account_id"]})
            resp.raise_for_status()
            contracts = resp.json()["data"]
            if not contracts:
                return [types.TextContent(type="text", text=str(
                    {"error": "No contract found for this account", "code": "NOT_FOUND"}
                ))]
            c = contracts[0]
            return [types.TextContent(type="text", text=str({
                "plan": c["plan_name"],
                "mrr_twd": c["mrr_twd"],
                "start_date": c["start_date"],
                "expiry_date": c["expiry_date"],
                "auto_renew": c["auto_renew"],
                "days_until_expiry": c["days_until_expiry"]
            }))]

        elif name == "get_usage_summary":
            days = min(arguments.get("days", 30), 90)  # 強制上限，保護查詢效能
            resp = http.get("/usage", params={
                "account_id": arguments["account_id"],
                "days": days
            })
            resp.raise_for_status()
            return [types.TextContent(type="text", text=str(resp.json()["summary"]))]

    except httpx.HTTPStatusError as e:
        # 回傳 model 看得懂的錯誤，不是 stack trace
        return [types.TextContent(type="text", text=str({
            "error": f"API request failed with status {e.response.status_code}",
            "code": "API_ERROR",
            "hint": "Check if account_id is valid and the account exists"
        }))]
    except Exception:
        return [types.TextContent(type="text", text=str({
            "error": "Unexpected server error",
            "code": "INTERNAL_ERROR"
        }))]

if __name__ == "__main__":
    import asyncio
    asyncio.run(stdio_server(app))
```

**關鍵設計決策**：

- `days` 上限強制 90 天 — 超過會拖慢 `usage_events` 查詢且 model context 裝不下
- 返回前過濾欄位 — 不把整個 account object 丟回去，只留 CS 需要的欄位
- 錯誤格式統一為 `{"error": "...", "code": "...", "hint": "..."}` — model 可根據 hint 重試

---

### Phase 3: Integration — 接上 Claude Code

**`.mcp.json`（放在 CS 團隊工作目錄）**：

```json
{
  "mcpServers": {
    "talentbridge-crm": {
      "command": "python",
      "args": ["/opt/mcp-servers/talentbridge/server.py"],
      "env": {
        "TALENTBRIDGE_API_URL": "${TALENTBRIDGE_API_URL}",
        "TALENTBRIDGE_API_KEY": "${TALENTBRIDGE_API_KEY}"
      }
    }
  }
}
```

**端對端測試矩陣**：

| 測試提示 | 預期 tool 呼叫順序 | 驗證點 |
|---------|-----------------|--------|
| "TechCorp 的合約還有幾天到期？" | `search_accounts("TechCorp")` → `get_contract(id)` | `days_until_expiry` 正確顯示 |
| "找一下 email 是 cto@beta.io 的客戶" | `search_accounts("cto@beta.io")` | 靠 email 也能搜到正確帳號 |
| "Acme 最近用得怎樣？" | `search_accounts("Acme")` → `get_usage_summary(id)` | summary 欄位完整 |
| "找 xyz123" （不存在） | `search_accounts("xyz123")` | 空陣列，Claude 告知找不到 |
| "看一下 Acme 90 天的用量" | `get_usage_summary(id, days=90)` | days=91 被截為 90 |

---

## Result

```markdown
# MCP Server Spec: TalentBridge CRM

## Purpose
Expose TalentBridge customer account, contract, and usage data to the CS team
via Claude Code — enabling natural language queries without requiring backend login.

## Tools
| Tool | Description | Parameters | Returns |
|------|-----------|-----------|---------|
| search_accounts | Find customers by name, domain, or email | query (req), limit (opt, default 5) | Array of {id, name, domain, plan, status} |
| get_contract | Get contract details for an account | account_id (req) | {plan, mrr_twd, expiry_date, days_until_expiry, auto_renew} |
| get_usage_summary | Get usage rollup for last N days | account_id (req), days (opt, default 30, max 90) | {active_users, sessions, top_features} |

## Data Source
- Type: REST API (internal FastAPI service)
- Connection: HTTPS to `api.talentbridge.tw`
- Auth: `TALENTBRIDGE_API_KEY` via env var (sent as `X-API-Key` header)

## .mcp.json
{
  "mcpServers": {
    "talentbridge-crm": {
      "command": "python",
      "args": ["/opt/mcp-servers/talentbridge/server.py"],
      "env": {
        "TALENTBRIDGE_API_URL": "${TALENTBRIDGE_API_URL}",
        "TALENTBRIDGE_API_KEY": "${TALENTBRIDGE_API_KEY}"
      }
    }
  }
}

## Testing Plan
1. search_accounts — 用公司名、domain、email 各測一次；確認空結果回傳空陣列而非錯誤
2. get_contract — 有效 account_id 查詢；不存在的 id 確認回傳 NOT_FOUND 格式
3. get_usage_summary — days=30 (default)；days=91 確認被截為 90
4. 端對端：「TechCorp 合約快到期了嗎？」確認 Claude 自動串起 search → get_contract
```
````
