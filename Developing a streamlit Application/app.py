import streamlit as st
from groq import Groq
import os

# Set up API key (use environment variable)
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Please set the GROQ_API_KEY environment variable.")
    st.stop()

client = Groq(api_key=groq_api_key)

st.title("💬 Groq LLM Chatbot")
st.write("Chat with a fast LLM powered by Groq API!")

# Chat interface
user_input = st.text_input("You:", placeholder="Ask me anything...")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": user_input}]
            )
            st.markdown("**Assistant:** " + response.choices[0].message.content)
    else:
        st.warning("Please enter a message.")
