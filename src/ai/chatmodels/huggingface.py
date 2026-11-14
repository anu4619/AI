
from dotenv import load_dotenv
import os

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint
)

load_dotenv()

hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face API token not found!")

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=100
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Hello, how are you?")

print(response.content)
