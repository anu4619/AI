from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEmbeddings
HuggingFaceEmbeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "you are going to learn Gen AI",
    "you are going to learn LLMs",
    "you are going to learn LangChain"
]
vectors = HuggingFaceEmbeddings.embed_documents(texts)
#vector = HuggingFaceEmbeddings.embed_query("you are going to learn Gen AI")
print(vectors)