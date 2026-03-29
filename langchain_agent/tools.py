import math
import json
import requests
from datetime import datetime
from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.
    Supports +, -, *, /, **, sqrt, sin, cos, tan, log, pi, e.
    Example input: '2 ** 10' or 'sqrt(144)' or 'pi * 5 ** 2'
    """
    allowed = {
        "sqrt": math.sqrt,
        "sin":  math.sin,
        "cos":  math.cos,
        "tan":  math.tan,
        "log":  math.log,
        "log2": math.log2,
        "log10":math.log10,
        "abs":  abs,
        "pi":   math.pi,
        "e":    math.e,
    }
    try:
        result = eval(expression, {"__builtins__": {}}, allowed)
        return f"{expression} = {result}"
    except Exception as ex:
        return f"Error evaluating '{expression}': {ex}"


@tool
def get_current_time(timezone: str = "UTC") -> str:
    """
    Returns the current date and time.
    Pass 'UTC' or leave blank for UTC time.
    """
    now = datetime.utcnow()
    return f"Current time (UTC): {now.strftime('%Y-%m-%d %H:%M:%S')}"


@tool
def get_weather(city: str) -> str:
    """
    Fetches current weather for a given city using the Open-Meteo API (free, no key needed).
    Example input: 'London' or 'New York'
    """
    # Step 1: geocode the city
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    try:
        geo = requests.get(geo_url, timeout=5).json()
        if not geo.get("results"):
            return f"Could not find city: {city}"

        loc = geo["results"][0]
        lat, lon = loc["latitude"], loc["longitude"]
        name = loc["name"]
        country = loc.get("country", "")

        # Step 2: fetch weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            f"&current_weather=true"
        )
        weather = requests.get(weather_url, timeout=5).json()
        cw = weather.get("current_weather", {})

        code_map = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Foggy", 61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
            80: "Rain showers", 95: "Thunderstorm",
        }
        condition = code_map.get(cw.get("weathercode", -1), "Unknown")

        return (
            f"Weather in {name}, {country}:\n"
            f"  Temperature : {cw.get('temperature')}°C\n"
            f"  Wind speed  : {cw.get('windspeed')} km/h\n"
            f"  Condition   : {condition}"
        )
    except Exception as ex:
        return f"Weather fetch failed: {ex}"


@tool
def search_web(query: str) -> str:
    """
    Searches the web using DuckDuckGo and returns top results.
    Use this for current events, facts, or anything that needs a web lookup.
    Example: 'latest AI news' or 'who invented Python'
    """
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        if not results:
            return "No results found."
        output = []
        for i, r in enumerate(results, 1):
            output.append(f"{i}. {r['title']}\n   {r['body']}\n   Source: {r['href']}")
        return "\n\n".join(output)
    except Exception as ex:
        return f"Search failed: {ex}"


@tool
def unit_converter(conversion: str) -> str:
    """
    Converts between common units.
    Format: '<value> <from_unit> to <to_unit>'
    Examples: '100 km to miles', '32 celsius to fahrenheit', '5 kg to lbs'
    """
    conversions = {
        # length
        ("km", "miles"):      lambda x: x * 0.621371,
        ("miles", "km"):      lambda x: x * 1.60934,
        ("meters", "feet"):   lambda x: x * 3.28084,
        ("feet", "meters"):   lambda x: x * 0.3048,
        ("cm", "inches"):     lambda x: x * 0.393701,
        ("inches", "cm"):     lambda x: x * 2.54,
        # weight
        ("kg", "lbs"):        lambda x: x * 2.20462,
        ("lbs", "kg"):        lambda x: x * 0.453592,
        ("grams", "ounces"):  lambda x: x * 0.035274,
        # temperature
        ("celsius", "fahrenheit"): lambda x: x * 9/5 + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5/9,
        ("celsius", "kelvin"):     lambda x: x + 273.15,
        ("kelvin", "celsius"):     lambda x: x - 273.15,
    }

    try:
        parts = conversion.lower().split()
        value = float(parts[0])
        from_unit = parts[1]
        to_unit = parts[3]

        key = (from_unit, to_unit)
        if key not in conversions:
            return f"Conversion from '{from_unit}' to '{to_unit}' is not supported."

        result = conversions[key](value)
        return f"{value} {from_unit} = {round(result, 4)} {to_unit}"
    except Exception as ex:
        return f"Conversion error: {ex}. Use format: '100 km to miles'"


@tool
def word_counter(text: str) -> str:
    """
    Counts words, characters, sentences, and paragraphs in a given text.
    """
    words      = len(text.split())
    chars      = len(text)
    chars_ns   = len(text.replace(" ", ""))
    sentences  = text.count('.') + text.count('!') + text.count('?')
    paragraphs = len([p for p in text.split('\n\n') if p.strip()])

    return (
        f"Text stats:\n"
        f"  Words      : {words}\n"
        f"  Characters : {chars} (no spaces: {chars_ns})\n"
        f"  Sentences  : {sentences}\n"
        f"  Paragraphs : {paragraphs}"
    )
