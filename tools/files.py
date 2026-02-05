import os
from .registry import TOOLS

def get_file_info(path: str) -> str:
    if not os.path.exists(path):
        return f"❌ File not found: {path}"

    stat = os.stat(path)
    return (
        f"📄 File: {path}\n"
        f"Size: {stat.st_size} bytes"
    )

TOOLS["get_file_info"] = get_file_info
