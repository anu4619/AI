
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("Models available to your API key:\n")

for model in client.models.list():
    if "generateContent" in (model.supported_actions or []):
        print(model.name)
