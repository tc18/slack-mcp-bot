####
### .env
```
SLACK_BOT_TOKEN=xoxb-####
SLACK_SIGNING_SECRET=####
```

```
uv venv
uv pip install slack-bolt fastapi uvicorn httpx python-dotenv

uv run uvicorn mcp_server:app --port 3333
uv run uvicorn slack_bot:api --port 3000

ngrok http 3000

put `ngrok http 3000` url into slack.
```

```
@mcp-bot what's the weather in austin
@mcp-bot show file info for /etc/hosts
@mcp-bot explain prod network change
@mcp-bot check vcn update
```

#####
```
Option B (recommended): LLM-based tool selection 🧠🔥

This is what you actually want long-term.

Router prompt (conceptual)
You are a router.
Given a user message, select the best tool and arguments.

Tools:
- get_weather(city)
- get_file_info(path)
- explain_network_change(change_id)

User message: "{text}"

Return JSON:
{ "tool": "...", "args": {...} }


You can plug:

OpenAI

local LLM

OCI GenAI

Claude
later — tools stay unchanged.

```


#####
Next natural upgrades (you’re ready for these)

1️⃣ Replace router.py with an LLM-based router
2️⃣ Auto-generate tool schema (name, args, docstring)
3️⃣ Permissions per Slack user
4️⃣ Observability (tool call tracing)
5️⃣ Feedback loop (👍 / 👎 improves routing)

If you want, next I can:

drop in an LLM router

or refactor this to pure MCP FastMCP style

Just tell me which way you want to go 🚀