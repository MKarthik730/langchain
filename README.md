# 🔗 LangChain Practice Repository

Hands-on experiments with LangChain, LLMs, tools, agents, and local/remote model backends.

---

## 📁 Project Structure

```
langchain/
├── langchain_agent/        # Full AI Agent with 6 tools + memory
│   ├── agent.py            # Main agent + chat loop
│   ├── tools.py            # All 6 custom tools
│   ├── test_tools.py       # Test tools without API key
│   └── requirements.txt    # Dependencies
│
├── main.py                 # Entry point for LangChain experiments
├── chatai.py               # Chat-based LLM interaction (Streamlit)
├── tools.py                # Custom tool definitions
├── tools_practice.py       # Tool usage and experimentation
├── test_ollama.py          # Local LLM testing with Ollama
├── openapi.py              # OpenAI / LangChain API examples
└── .gitignore
```

---

##  What's Covered

- 🤖 **AI Agent** with tools, memory, and GPT-4o (`langchain_agent/`)
- 💬 **Chat LLM apps** using LangChain + Streamlit
- 🔧 **Tool creation** and tool-calling workflows
- 🦙 **Local LLM** experimentation via Ollama
- 🔑 **Secure API key** usage via environment variables
- 🧪 **Practice scripts** for understanding chains and agents

---

## 🛠️ AI Agent — Tools

Located in `langchain_agent/`. The agent automatically picks the right tool based on your question.

| Tool | What it does |
|------|-------------|
| `calculator` | Safe math — `sqrt`, `sin`, `pi`, `**`, `log` |
| `get_weather` | Live weather for any city (free, no key) |
| `search_web` | DuckDuckGo web search |
| `unit_converter` | km↔miles, kg↔lbs, °C↔°F, etc. |
| `get_current_time` | Current UTC date and time |
| `word_counter` | Words, characters, sentences, paragraphs |

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/MKarthik730/langchain.git
cd langchain
```

### 2. Install dependencies
```bash
pip install -r langchain_agent/requirements.txt
```

### 3. Set your API key
Create a `.env` file in the root:
```
OPENAI_API_KEY=sk-your-key-here
```

### 4. Run the AI Agent
```bash
cd langchain_agent
python test_tools.py   # test without API key first
python agent.py        # start chatting
```

### 5. Run other scripts
```bash
python main.py
python chatai.py       # Streamlit chat UI
python test_ollama.py  # requires Ollama running locally
```

---

## 🦙 Local LLM with Ollama

To use `test_ollama.py`, install [Ollama](https://ollama.com) and pull a model:
```bash
ollama pull gemma3:4b
ollama serve
python test_ollama.py
```

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange?logo=openai)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-black)

---

## 👤 Author

**MKarthik730** — [github.com/MKarthik730](https://github.com/MKarthik730)
