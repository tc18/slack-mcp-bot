from .registry import TOOLS

def get_weather(city: str) -> str:
    return f"🌤 Weather in {city.title()}: 72°F, Clear skies"

TOOLS["get_weather"] = get_weather
