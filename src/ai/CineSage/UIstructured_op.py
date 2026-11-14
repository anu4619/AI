
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize model
model = ChatOpenAI(
    model="gpt-6-luna"
)

# Define Pydantic schema
class Movie(BaseModel):
    title: str
    release_year: Optional[str]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    ratings: Optional[float]
    summary: str


# Initialize parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Define prompt
prompt = ChatPromptTemplate.from_messages([
    ("system",
    """
Extract movie information from a paragraph.

{format_instructions}
"""),
    ("human",
    """
{paragraph}
""")
])

# Streamlit UI
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Extract structured movie information using Pydantic.")

# Input paragraph
para = st.text_area(
    "Enter a movie paragraph",
    placeholder="Enter your movie description here...",
    height=200
)

# Extract button
if st.button("Extract Information", type="primary"):

    if para.strip():

        final_prompt = prompt.invoke({
            "paragraph": para,
            "format_instructions": parser.get_format_instructions()
        })

        with st.spinner("Extracting movie information..."):
            response = model.invoke(final_prompt)
            movie_data=parser.parse(response.content)

        st.subheader("Extracted Movie Information")
        st.write(movie_data)

    else:
        st.warning("Please enter a movie paragraph.")
