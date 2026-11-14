from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-small',
    dimensions = 64
)
texts = [
    "you are going to learn Gen AI",
    "you are going to learn LLMs",
    "you are going to learn LangChain"
]
vectors = embeddings.embed_documents(texts)
#vector = embeddings.embed_query("you are going to learn Gen AI")
print(vectors)