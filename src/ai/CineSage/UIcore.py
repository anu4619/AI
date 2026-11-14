
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize model
model = ChatOpenAI(
    model="gpt-6-luna"
)

# Define prompt
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

# Streamlit UI
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph to extract structured information.")

# Input paragraph
para = st.text_area(
    "Movie Paragraph",
    placeholder="Enter your movie description here...",
    height=200
)

# Extract button
if st.button("Extract Information", type="primary"):

    if para.strip():

        final_prompt = prompt.invoke(
            {"paragraph": para}
        )

        with st.spinner("Extracting movie information..."):
            response = model.invoke(final_prompt)

        st.subheader("Extracted Movie Information")
        st.write(response.content)

    else:
        st.warning("Please enter a movie paragraph.")
