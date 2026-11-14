from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 512,"do_sample": False, "repetition_penalty": 1.03, "temperature": 0.7},
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("what is data science?")

print(result.content)