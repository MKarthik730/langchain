# LangChain AI Agent

A conversational AI agent with 6 real tools, memory, and a clean chat loop.

## Tools
| Tool | What it does |
|------|-------------|
| `calculator` | Evaluates math — `sqrt`, `sin`, `pi`, `**`, etc. |
| `get_current_time` | Returns current UTC time |
| `get_weather` | Live weather for any city (no API key needed) |
| `search_web` | DuckDuckGo web search |
| `unit_converter` | km↔miles, kg↔lbs, °C↔°F, etc. |
| `word_counter` | Words, chars, sentences, paragraphs |

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your OpenAI key
cp .env.example .env
# edit .env and paste your key

# 3. Test tools (no API key needed)
python test_tools.py

# 4. Run the agent
python agent.py
```

## Example Conversations

```
You: What's the weather in Mumbai?
You: Convert 180 lbs to kg
You: What is sqrt(2) raised to the power of 10?
You: Search the web for latest Python 3.13 features
You: How many words are in "The quick brown fox jumps over the lazy dog"?
```

## Project Structure

```
langchain_agent/
├── agent.py          # Main agent + chat loop
├── tools.py          # All 6 custom tools
├── test_tools.py     # Test tools without API key
├── requirements.txt
└── .env.example
```

## Customization

- **Swap the model**: change `model="gpt-4o"` to `"gpt-3.5-turbo"` in `build_agent()`
- **Add a tool**: define a new `@tool` in `tools.py` and add it to the `tools` list in `agent.py`
- **Adjust memory**: change `memory_window` in `build_agent()` (default: last 10 turns)
