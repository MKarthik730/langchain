import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI()

st.set_page_config(page_title="Chat with OpenAI")
st.title("KAKASHI")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    assistant_message = response.choices[0].message.content


    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_message)
