import os
import gradio as gr
from datetime import datetime
from groq import Groq

# Load API key from Hugging Face Secrets
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please add it in Hugging Face Space → Settings → Repository secrets.")

# Initialize Groq client
client = Groq(api_key=api_key)

# Groq Chat Function
def ask_groq(user_text, model="openai/gpt-oss-120b"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful and friendly chatbot."},
                {"role": "user", "content": user_text},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Chatbot Backend Logic
def respond(message, chat_history):
    bot_reply = ask_groq(message)
    chat_history.append((message, bot_reply))
    return chat_history, ""


# Gen-Z Style UI

with gr.Blocks(theme=gr.themes.Soft(primary_hue="rose", secondary_hue="sky")) as demo:
    gr.Markdown(
        """
        <div style="text-align:center; font-size:2em; font-weight:700; color:#fb7185;">
            ⚡ ChatBot — Groq Powered ⚡
        </div>
        """,
    )

    chatbot = gr.Chatbot(
        label=None,
        height=500,
        bubble_full_width=False,
        avatar_images=(
            "https://cdn-icons-png.flaticon.com/512/1077/1077012.png",
            "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        ),
    )

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Type your message...",
            show_label=False,
            scale=8,
            container=False,
        )
        send = gr.Button("Send", variant="primary", scale=1)

    send.click(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[chatbot, msg])

    gr.Markdown(
        f"""
        <div style="text-align:center; color:#a3a3a3; margin-top:12px;">
            <small>Powered by Groq • {datetime.now().year}</small>
        </div>
        """
    )

demo.launch()
