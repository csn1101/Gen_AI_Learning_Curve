import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage


env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path=env_path)
llm_key = os.getenv('test_key2')

# #llm Model
# llm = OpenAI(openai_api_key=llm_key)
# response = llm.invoke('who is narendra modi?answer in three words')
# print(response)

# #chat model
# chat = ChatOpenAI(openai_api_key=llm_key)
# response = chat.invoke('who is narendra modi?answer in three words')
# print(response)

# #message model
# chat = ChatOpenAI(openai_api_key=llm_key)
# messages=[
#     #this ensures that the ai assistant will answer like a singer
#     SystemMessage(content="You are a singer"),
#     #this is the question we are asking
#     HumanMessage(content="Who is babul suprio?")
# ]
# response = chat.invoke(messages)
# print(response)