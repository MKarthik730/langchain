"""
Run this to verify all tools work before plugging in your API key.
No OpenAI key needed for this test.
"""
from tools import calculator, get_current_time, get_weather, unit_converter, word_counter


def run(label, fn, *args):
    print(f"\n{'─'*40}")
    print(f"Tool: {label}")
    result = fn.invoke(*args)
    print(result)


if __name__ == "__main__":
    print("Testing all tools...\n")

    run("Calculator",     calculator,     "sqrt(144) + 2 ** 8")
    run("Time",           get_current_time, "UTC")
    run("Unit Converter", unit_converter, "100 km to miles")
    run("Unit Converter", unit_converter, "32 celsius to fahrenheit")
    run("Word Counter",   word_counter,
        "LangChain is great. It makes building AI agents easy!\n\nThis is paragraph two.")
    run("Weather",        get_weather,    "Tokyo")

    print(f"\n{'─'*40}")
    print("All tools tested. If weather worked, you're good to go!")
    print("Add your OPENAI_API_KEY to .env and run: python agent.py")
