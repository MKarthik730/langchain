import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools import (
    calculator,
    get_current_time,
    get_weather,
    search_web,
    unit_converter,
    word_counter,
)

load_dotenv()


# ── System prompt ──────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a smart, helpful AI assistant with access to a set of tools.

Your available tools:
- calculator      : evaluate math expressions
- get_current_time: get the current UTC time
- get_weather     : fetch live weather for any city
- search_web      : search the internet via DuckDuckGo
- unit_converter  : convert between units (km, miles, kg, lbs, °C, °F, etc.)
- word_counter    : count words, characters, sentences in text

Guidelines:
- Always use a tool when the task calls for it — don't guess facts you can look up.
- If a tool fails, explain why and offer an alternative.
- Keep responses clear and concise.
- Remember context from earlier in the conversation.
"""


def build_agent(model: str = "gpt-4o", temperature: float = 0.3, memory_window: int = 10):
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    tools = [
        calculator,
        get_current_time,
        get_weather,
        search_web,
        unit_converter,
        word_counter,
    ]

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    memory = ConversationBufferWindowMemory(
        k=memory_window,
        memory_key="chat_history",
        return_messages=True,
    )

    agent = create_openai_tools_agent(llm, tools, prompt)

    executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True,
    )

    return executor


def chat(executor: AgentExecutor, user_input: str) -> str:
    response = executor.invoke({"input": user_input})
    return response["output"]


def main():
    print("=" * 55)
    print("  LangChain AI Agent")
    print("  Tools: calculator, weather, search, converter")
    print("  Type 'exit' or 'quit' to stop")
    print("=" * 55)

    agent = build_agent()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "bye"):
            print("Goodbye!")
            break

        response = chat(agent, user_input)
        print(f"\nAgent: {response}")


if __name__ == "__main__":
    main()
  
