
import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("💬 AI Chatbot")
st.caption("Choose your AI personality and start chatting!")

# AI modes
modes = {
    "😂 Funny Mode": "You are a funny assistant. respond with humor and jokes",
    "🎓 Serious Mode": "You are a serious assistant.keep your tone serious and straight forward",
    "😏 Sarcastic Mode": "You are a sarcastic assistant. respond with sarcasm and witty remarks",
    "😡 Angry Mode": "You are an angry assistant. respond with anger and frustration"
}

# Mode selection
choice = st.selectbox(
    "Choose your AI mode",
    list(modes.keys())
)

mode = modes[choice]

# Initialize model
model = ChatOpenAI(
    model="gpt-6-luna"
)

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.current_mode = choice

# Update system prompt if mode changes
if st.session_state.current_mode != choice:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.current_mode = choice

messages = st.session_state.messages

# Display conversation
for message in messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Add human message
    messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(messages)
            st.write(response.content)

    # Add AI message
    messages.append(AIMessage(content=response.content))
