# 🌤️ AI Mood Tracker (Groq + Gradio + Matplotlib)

An **AI-powered Mood Tracker** that helps you log and analyze your emotions throughout the day.  
Built entirely in **Google Colab** — no local installation required!  
Uses **Groq (LLaMA 3.3 70B)** for natural-language mood classification, **Gradio** for the frontend UI, and **Matplotlib** for interactive charts.

---

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [Mood Tracker App – Hugging Face Demo](https://huggingface.co/spaces/nareen99/mood-tracker-app)

---

## 🧠 Features

- ✍️ **Free-text mood entries** — enter how you feel up to 3–4 times per day  
- 🤖 **AI mood detection** — Groq’s LLaMA 3.3 70B classifies your emotions (Happy, Sad, Angry, etc.)  
- 📊 **Visual analytics dashboard** — pie chart, trend chart, and mood frequency bar chart  
- 💾 **Auto CSV logging** — saves all entries in `mood_data.csv`  
- 🌈 **Modern pastel UI** — soft notebook aesthetic with rounded panels and compact buttons  
- ☁️ **Runs 100% in Google Colab** — no local setup or deployment needed  

---

## 🧩 Tech Stack

| Component     | Technology Used            |
|----------------|----------------------------|
| Frontend       | [Gradio](https://gradio.app/) |
| AI Model       | [Groq LLaMA 3.3 70B](https://groq.com/) |
| Visualization  | [Matplotlib](https://matplotlib.org/) |
| Data Storage   | CSV (via Pandas)           |
| Runtime        | Google Colab               |

---

## 🚀 Getting Started (Google Colab)

### 1️⃣ Clone or upload files
Upload both files into your Colab environment:
```

app.py
requirements.txt

````

### 2️⃣ Install dependencies
```python
!pip install -r requirements.txt
````

### 3️⃣ Set your Groq API key

> ⚠️ You must have a valid Groq API key from [GroqCloud](https://console.groq.com/keys).

```python
import os
os.environ["GROQ_API_KEY"] = "your_groq_api_key_here"
```

### 4️⃣ Run the app

```python
!python app.py
```

Gradio will provide a **shareable public link** (e.g. `https://xxxxx.gradio.live`) that opens your app in a browser.

---

## 💻 App Overview

### **Home Screen**

* Enter your mood description in natural language (e.g., “Feeling relaxed after my walk.”)
* Click **🔍 Analyze Mood & Save** to classify and store your entry.

### **Analytics Section**

* Click **📊 Show Analytics** to view:

  * **Pie chart:** Mood distribution
  * **Line chart:** Mood trend over time
  * **Bar chart:** Frequency of moods

### **Recent Entries**

A table showing your latest logs (timestamp, description, mood, confidence).

---

## 📁 File Structure

```
📦 Mood-Tracker
 ┣ 📜 app.py              # Main application logic
 ┣ 📜 requirements.txt    # Python dependencies
 ┣ 📜 mood_data.csv       # Auto-generated log file
 ┗ 📘 README.md           # Project documentation
```

---

## 🧩 Example Output

| timestamp            | description                                  | mood    | confidence |
| -------------------- | -------------------------------------------- | ------- | ---------- |
| 2025-11-06T16:12:12Z | I am happy because I watched an action drama | Happy   | 90         |
| 2025-11-06T16:03:59Z | Feeling tired but hopeful                    | Neutral | 50         |

---

## 🎨 UI Aesthetic

* Soft pastel background
* Rounded cards
* Compact, centered buttons
* Calming *Poppins* typography
* “Notebook aesthetic” for clean daily journaling

---

## ⚠️ Troubleshooting

| Issue                                               | Solution                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------- |
| `ValueError: Cannot process this value as an Image` | Upgrade to Gradio ≥ 3.50.2 and ensure charts use `gr.Plot`.         |
| Charts not showing                                  | Ensure `matplotlib` is installed and CSV has valid data.            |
| API not working                                     | Check your `GROQ_API_KEY` is set correctly before running `app.py`. |
| Buttons too big                                     | Fixed in the pastel edition (compact button CSS applied).           |

---

## ❤️ Credits

Built with:

* [Groq LLaMA 3.3 70B](https://groq.com/)
* [Gradio](https://gradio.app/)
* [Matplotlib](https://matplotlib.org/)
* [Pandas](https://pandas.pydata.org/)
