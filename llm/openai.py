# import llm azure open ai
import os
os.environ["OPENAI_API_KEY"] = "2b5a9194cc31439ca1925e5f4bb720e8"
os.environ["OPENAI_API_BASE"] = "https://iris-gpt.openai.azure.com/"
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, prompt_template

llm = AzureChatOpenAI(deployment_name="gpt35", model_name="gpt-35-turbo-16k")

print(llm([HumanMessage(content="hello, what is your name?")]))


def summarize_chapter(text) -> str:
