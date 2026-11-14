from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model = "gpt-6-luna"
)


class Movie(BaseModel):
    title: str
    release_year: Optional[str]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    ratings: Optional[float]
    summary: str


parser= PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system",
"""
Extract movie information from a paragraph
{format_instructions}

"""),
("human",
 """
 {paragraph}
 """)
])

para = input("Give your paragraph about a movie: ")
final_prompt=prompt.invoke(
    {"paragraph": para,
     "format_instructions": parser.get_format_instructions()}
)
response = model.invoke(final_prompt)
movie_data=parser.parse(response.content)
print(movie_data)