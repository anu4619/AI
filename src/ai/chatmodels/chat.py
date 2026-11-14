

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model


model = init_chat_model(
    "gemini-3.5-flash-lite",
    model_provider="google_genai"
)


response = model.invoke("Say hello to the world!")

print(response.content)
