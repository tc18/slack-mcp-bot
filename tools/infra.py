from .registry import TOOLS

def explain_network_change(change_id: str) -> str:
    # return (
    #     f"🔌 Network Change ({change_id})\n"
    #     f"- Route table updated\n"
    #     f"- Risk: Low"
    # )

    return {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🔌 Network Change"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Change ID* : ID"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Risk* : Risk"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Component* : Component"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Action* : Action"
                    }
                ]
            }
        ]
    }

TOOLS["explain_network_change"] = explain_network_change
