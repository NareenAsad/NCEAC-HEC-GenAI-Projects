# 💬 Groq LLM Chatbot — Streamlit + Hugging Face Deployment

This project is part of **Module 4** of the **NCEAC–HEC Generative AI Training (Cohort 1)** by **Pak Angels**.  
It demonstrates how to build, test, and deploy a **Streamlit-based LLM chatbot** powered by the **Groq API**.

---

## 🚀 Project Overview

This chatbot allows users to interact with a fast, free **Large Language Model (LLM)** hosted by **Groq**.  
It’s built using **Streamlit** for the front-end interface and deployed seamlessly on **Hugging Face Spaces**.

---

## 🧩 Features

✅ Chat interface built with Streamlit  
✅ Integrated with Groq’s `llama-3.1-8b-instant` model  
✅ Deployed publicly on Hugging Face Spaces  
✅ Supports text-based question answering and conversation  
✅ Lightweight, responsive, and beginner-friendly

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend / LLM API** | Groq |
| **Deployment** | Hugging Face Spaces |
| **Language** | Python 3 |
| **Environment File** | `requirements.txt` |

---

## 📁 Project Structure

```

├── app.py                # Main Streamlit application file
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation

````

---

## ⚙️ Installation & Setup (Local or Colab)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/NareenAsad/NCEAC-HEC-GenAI-Projects.git
cd <your-repo-name>
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set your Groq API key

Get your API key from [https://console.groq.com/keys](https://console.groq.com/keys)

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

You can access the live app here 👇
👉 **[Live on Hugging Face Spaces](https://huggingface.co/spaces/nareen99/Streamlit_HuggingFace_Deployment)**


---

## 🧩 Example Usage

**User:**

> What is Generative AI?

**Assistant:**

> Generative AI refers to artificial intelligence models that can generate new content such as text, images, audio, and code based on the data they’ve been trained on.

---

## 📚 Learning Outcomes

Through this project, you’ll learn:

* How to create interactive front-ends with Streamlit
* How to use Groq’s free LLM API
* How to deploy Streamlit apps on Hugging Face Spaces

---

## ✨ Acknowledgments

This project was developed as part of the **NCEAC–HEC Generative AI Training Program (Cohort 1)**, powered by **Pak Angels** and partners.
Special thanks to the instructors and organizers for enabling hands-on AI learning.

---