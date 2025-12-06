from langchain_openai import OpenAI
from text import OPEN_API_KEY


from langchain_core.prompts import PromptTemplate
import streamlit as st

input=st.text_input("enter the text: ")
#os.environ["OPENAI_API-KEY"]=OPEN_API_KEY
lllm = OpenAI(
    model="gpt-4o-mini",     
    temperature=0.6,
    api_key=OPEN_API_KEY, 
)
st.title("simple chat")
prompt=PromptTemplate(
    input_variables=["input"],
    template="give details about {input}"
)
chain=prompt|lllm

if input:
    st.write(chain.run(input))