from langchain_ollama import ChatOllama
from text import OPEN_API_KEY
import os

from langchain_core.prompts import ChatPromptTemplate

import streamlit as st
input=st.text_input("enter the text: ")
#os.environ["OPENAI_API-KEY"]=OPEN_API_KEY
lllm = ChatOllama(
    model="llama3.2",     
    temperature=0.6,
    api_key=OPEN_API_KEY, 
)
prompt=ChatPromptTemplate.from_template("deatils about {name}ed person")
st.title("simple chat")
integrate=prompt|lllm
if input:
    st.write(integrate.invoke(input))
