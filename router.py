import re


def route(text: str):
    t = text.lower()

    # Weather
    if "weather" in t:
        city = t.split()[-1]
        return "get_weather", {"city": city}

    # File info
    if "file" in t or "size" in t:
        match = re.search(r"/\S+", text)
        path = match.group(0) if match else "/tmp/test.txt"
        return "get_file_info", {"path": path}

    # Infra
    if "network" in t or "vcn" in t:
        return "explain_network_change", {"change_id": "latest"}

    return None, {}
