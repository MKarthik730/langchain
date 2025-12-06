from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from pydantic import BaseModel,Field
from typing import Optional
class Table(BaseModel):
    name:Optional[str]=Field(default="name", description="name of the person")
    age:Optional[int]=Field(default=-1,description="age of person")
    id:Optional[int]=Field(default=-1,description="id of the person")
@tool(args_schema=Table)
def add_user(name:str,age:int,id:int):
    """
    Docstring for add_user
    
    :param name: Description
    :type name: str
    :param age: Description
    :type age: int
    :param id: Description
    :type id: int
    """
    print("user-add-tool")
    return f"name={name}, age={age},id={id}"
@tool
def search_usr(name:str):
    """
    Docstring for search_usr
 
    :param name: Description
    :type name: str
    """
    print("desearch-usr-tool")
    return f"name={name}"
def run_tools(response):
    tool_calls = getattr(response, "tool_calls", [])
    results = []

    for call in tool_calls:
        name = call["name"]
        args = call["args"]

        if name == "add_user":
            result = add_user.invoke(args)      
        elif name == "search_usr":
            result = search_usr.invoke(args)   
        else:
            result = f"Unknown tool: {name}"

        results.append(result)

    return results
def test(input):
    llm=ChatOllama(model="llama3.2")
    msg=[HumanMessage(content=input)]
    llm_with_tools=llm.bind_tools([search_usr,add_user])
    response=llm_with_tools.invoke(msg)
    result=run_tools(response)
    print("result",result)
    return response
test("karthik 19")
test("karthik")