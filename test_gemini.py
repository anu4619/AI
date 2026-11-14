
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

print("Testing Gemini 3.5 Flash Lite...", flush=True)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Reply with just: Hello!"
    )

    print("Gemini response:", response.text)

except Exception as e:
    print("API Error:", repr(e))
