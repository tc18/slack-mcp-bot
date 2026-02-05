from .registry import TOOLS

def explain_network_change(change_id: str) -> str:
    return (
        f"🔌 Network Change ({change_id})\n"
        f"- Route table updated\n"
        f"- Risk: Low"
    )

TOOLS["explain_network_change"] = explain_network_change
