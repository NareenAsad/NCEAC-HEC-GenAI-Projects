import os
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from groq import Groq

DATA_FILE = "mood_data.csv"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["timestamp", "description", "mood", "confidence"])
    df.to_csv(DATA_FILE, index=False)

def analyze_mood(description: str):
    """Analyze mood using Groq or fallback classifier."""
    if not description.strip():
        return "Please enter a description.", None, None

    fallback = {
        "happy": "Happy",
        "joy": "Happy",
        "sad": "Sad",
        "angry": "Angry",
        "mad": "Angry",
        "anxious": "Anxious",
        "excited": "Excited",
        "bored": "Neutral",
        "tired": "Neutral",
    }
    detected_mood = "Neutral"
    for k, v in fallback.items():
        if k in description.lower():
            detected_mood = v
            break

    confidence = 50
    if client:
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"Classify the mood from this text: '{description}'. Respond only with one of [Happy, Sad, Angry, Anxious, Excited, Neutral].",
                    }
                ],
            )
            detected_mood = response.choices[0].message.content.strip()
            confidence = 90
        except Exception as e:
            detected_mood = f"Error: {e}"
            confidence = 0

    timestamp = datetime.now(timezone.utc).isoformat()
    new_entry = pd.DataFrame(
        [{"timestamp": timestamp, "description": description, "mood": detected_mood, "confidence": confidence}]
    )
    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    return detected_mood, confidence, f"✅ Saved at {timestamp}"

def get_last_entries():
    df = pd.read_csv(DATA_FILE)
    return df.tail(10)

def show_analytics():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return None, None, None

    mood_counts = df["mood"].value_counts()

    # Pie Chart
    fig1, ax1 = plt.subplots(figsize=(4, 4))
    ax1.pie(mood_counts, labels=mood_counts.index, autopct="%1.1f%%", startangle=90)
    ax1.set_title("Mood Distribution")

    # Trend Chart
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    trend = df.groupby(df["timestamp"].dt.date)["mood"].value_counts().unstack().fillna(0)
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    trend.plot(ax=ax2)
    ax2.set_title("Mood Trend Over Days")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Mood Count")
    plt.tight_layout()

    # Bar Chart
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    mood_counts.plot(kind="bar", ax=ax3, color="#6aa6a6")
    ax3.set_title("Mood Frequency")
    plt.tight_layout()

    return fig1, fig2, fig3


# Modern Pastel Theme
custom_css = """
#main-container {
    max-width: 850px;
    margin: 0 auto;
    padding: 1rem 2rem;
    font-family: 'Poppins', sans-serif;
    background-color: #fdfdfd;
}

.gradio-container {
    background: linear-gradient(180deg, #e8f5f5 0%, #f8fbfa 100%);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}

h1, h2, h3, p {
    text-align: center;
    color: #333;
}

.gr-button {
    background-color: #7dc9c3 !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    width: auto !important;
    display: inline-block !important;
}

.gr-button:hover {
    background-color: #5cb4ad !important;
    transform: scale(1.03);
    transition: 0.2s;
}

.gr-textbox, .gr-number, .gr-dataframe {
    border-radius: 10px !important;
}

"""

#  Build Gradio Interface
with gr.Blocks(css=custom_css, title="Mood Tracker App") as demo:
    gr.Markdown("## Mood Tracker")
    gr.Markdown("Track your mood through the day. Enter how you feel — Groq (LLaMA 3.3 70B) classifies it automatically!")

    with gr.Row():
        desc = gr.Textbox(label="How are you feeling?", placeholder="e.g. Feeling calm after coffee", lines=3)
        analyze_btn = gr.Button("Analyze Mood & Save")

    with gr.Row():
        mood_out = gr.Textbox(label="Detected Mood")
        conf_out = gr.Number(label="Confidence (%)")

    status = gr.Textbox(label="Status", interactive=False)

    gr.Markdown("### Recent Entries")
    table = gr.DataFrame(headers=["timestamp", "description", "mood", "confidence"], interactive=False)

    show_btn = gr.Button("Show Analytics")

    with gr.Row():
        pie_chart = gr.Plot(label="Mood Distribution")
        trend_chart = gr.Plot(label="Mood Trend")
        bar_chart = gr.Plot(label="Mood Frequency")

    analyze_btn.click(analyze_mood, inputs=[desc], outputs=[mood_out, conf_out, status]).then(
        fn=get_last_entries, outputs=[table]
    )

    show_btn.click(show_analytics, outputs=[pie_chart, trend_chart, bar_chart])

demo.launch(share=True)
