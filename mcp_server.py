from fastapi import FastAPI
from pydantic import BaseModel

from router import route
from tools.registry import TOOLS
import tools  # <-- IMPORTANT (triggers registration)

app = FastAPI()


class MCPRequest(BaseModel):
    input: str


@app.post("/mcp")
def handle_mcp(req: MCPRequest):
    tool_name, args = route(req.input)

    if not tool_name:
        return {"output": "🤔 I don’t know how to handle that yet."}

    tool_fn = TOOLS.get(tool_name)
    if not tool_fn:
        return {"output": f"❌ Tool not registered: {tool_name}"}

    result = tool_fn(**args)
    return {"output": result}
