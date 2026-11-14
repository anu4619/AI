from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model = "gpt-6-luna"
)





prompt = ChatPromptTemplate.from_messages([
    ("system",
"""
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2–3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""),
("human",
 """
 Extract inforation from this paragraph:
 {paragraph}
 """)
])

para = input("Give your paragraph about a movie: ")
final_prompt=prompt.invoke(
    {"paragraph": para}
)
response = model.invoke(final_prompt)
print(response.content)