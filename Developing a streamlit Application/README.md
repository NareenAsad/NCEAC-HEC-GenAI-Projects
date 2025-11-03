# 💬 Groq LLM Chatbot — Streamlit + Hugging Face Deployment

This project is part of **Module 4** of the **NCEAC–HEC Generative AI Training (Cohort 1)** by **Pak Angels**.
It demonstrates how to build, test, and deploy a **Streamlit-based LLM chatbot** powered by the **Groq API** with a modern conversational UI.

---

## 🚀 Project Overview

This chatbot enables users to have an interactive conversation with a fast, free **Large Language Model (LLM)** hosted by **Groq**.
The front-end interface is built with **Streamlit**, using the latest chat UI components (`st.chat_input()` and `st.chat_message()`), and the backend leverages the Groq API.
It supports persistent chat history, making conversations seamless and natural.

---

## 🧩 Features

✅ Modern chat-style interface with Streamlit’s chat components
✅ Persistent chat history stored during the session
✅ Integrated with Groq’s `llama-3.1-8b-instant` LLM model
✅ Graceful error handling for API issues
✅ Lightweight, responsive, and beginner-friendly
✅ Easily deployable on Hugging Face Spaces or locally

---

## 🛠️ Tech Stack

| Component         | Description         |
| ----------------- | ------------------- |
| **Frontend**      | Streamlit (chat UI) |
| **Backend / API** | Groq LLM API        |
| **Deployment**    | Hugging Face Spaces |
| **Language**      | Python 3            |
| **Environment**   | `requirements.txt`  |

---

## 📁 Project Structure

```
├── app.py                # Main Streamlit app with chat interface
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup (Local or Colab)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NareenAsad/NCEAC-HEC-GenAI-Projects.git
cd <your-repo-name>
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set your Groq API key

Get your API key from [https://console.groq.com/keys](https://console.groq.com/keys).

Set it as an environment variable:

```python
import os
os.environ["GROQ_API_KEY"] = "your_actual_api_key_here"
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🌐 Deployed App

Access the live app here:
👉 **[Live on Hugging Face Spaces](https://huggingface.co/spaces/nareen99/Streamlit_HuggingFace_Deployment)**

---

## 🧩 Example Usage

**User:**

> What is Generative AI?

**Assistant:**

> Generative AI refers to artificial intelligence models that can generate new content such as text, images, audio, and code based on the data they’ve been trained on.

---

## 📚 Learning Outcomes

By working on this project, you will learn:

* How to build conversational UIs with Streamlit’s chat components
* How to manage session state for persistent chat history
* How to interact with Groq’s free LLM API
* How to handle errors gracefully in your app
* How to deploy Streamlit apps on Hugging Face Spaces

---

## ✨ Acknowledgments

This project is developed as part of the **NCEAC–HEC Generative AI Training Program (Cohort 1)** powered by **Pak Angels**.
Special thanks to the instructors and organizers for empowering hands-on AI learning.

---