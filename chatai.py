from dotenv import load_dotenv
import os
load_dotenv()
from openapi import OpenAI
client=OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
chat=client.chat.completions.create(
    messages=[
        {"role":"user","content":"hello"}
    ],
    model="get-4"    
)
response=chat.choises[0].message.content
print(response)