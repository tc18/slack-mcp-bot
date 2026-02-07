import os
import httpx
from fastapi import FastAPI, Request
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from dotenv import load_dotenv

load_dotenv()

app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"],
)

api = FastAPI()
handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_mention(event, say, logger):
    # Remove <@BOTID>
    logger.info(event)
    print(event)
    text = event["text"].split(">", 1)[-1].strip()
    logger.info(f"Slack input: {text}")

    try:
        r = httpx.post(
            "http://localhost:3333/mcp",
            json={"input": text},
            timeout=10,
        )
        say(r.json()["output"], thread_ts=event["ts"])
    except Exception:
        logger.exception("MCP error")
        say("⚠️ MCP server is not available")


@api.post("/slack/events")
async def slack_events(req: Request):
    return await handler.handle(req)
