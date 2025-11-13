import streamlit as st
from groq import Groq
import os

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- LOAD API KEY ----
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("🚨 Please set your GROQ_API_KEY environment variable.")
    st.stop()

client = Groq(api_key=groq_api_key)

# ---- HEADER ----
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>Groq LLM Chatbot</h1>
    <p style='text-align: center; color: gray;'>Powered by <b>Groq’s free Llama 3 API</b></p>
    <hr style='border: 1px solid #eee;'>
    """,
    unsafe_allow_html=True
)

# ---- SESSION STATE FOR CHAT HISTORY ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": " Hi! I'm your Groq assistant. How can I help you today?"}
    ]

# ---- DISPLAY CHAT HISTORY ----
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"🧑‍💻 {msg['content']}")
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(f"🤖 {msg['content']}")

# ---- CHAT INPUT ----
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(f"🧑‍💻 {user_input}")

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=st.session_state.messages
                )
                assistant_reply = response.choices[0].message.content
            except Exception as e:
                assistant_reply = f"⚠️ Error: {str(e)}"

            st.markdown(f"🤖 {assistant_reply}")

    # Add assistant reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
