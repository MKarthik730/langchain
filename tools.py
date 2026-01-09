from langchain_core.tools import tool
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

@tool("say-name")
def say(name:str)->str:
   """this tools prints the name
   Args:
       name
    Retuns:
       name
   
   """
   return f" name={name}"
#person=say
#print(person.invoke("karthik"))
#print(person.func("monarch"))
#print(say.name)
class table(BaseModel):
   name:str=Field(default="none", description="name of person")
   age:int=Field(default=-1,description="age of person")
@tool(args_schema=table)
def file_add(name:str="none", age:int=-1)->str:
   """adding data to table
   Args:
   name,age
   Result:
   added
   
   """
   return f"name={name},age={age}"
#igris=file_add
#print(igris.batch([{"name":"karthik","age":19},{"name":"igris","age":100}]))
def process(input):
   llm=ChatOllama(model="llama3.2")
   llm_with_tools=llm.bind_tools([file_add])
   msg=[HumanMessage(content=input)]
   response=llm_with_tools.invoke(msg)
   print(response)
   return response.content


print(process("process karthik age 19"))
