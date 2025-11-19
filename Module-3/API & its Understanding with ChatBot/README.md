# ⚡ Groq ChatBot — Colab + Hugging Face Deployment Guide

This project focuses on **solving API-related errors in Google Colab**, understanding **deployment concepts**, and securely storing API Keys using **Hugging Face Secrets**.
You will build and deploy a stylish **Gen-Z themed AI ChatBot** powered by **Groq LLaMA models** using **Gradio** as the frontend.

---

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [Groq ChatBot – Hugging Face Demo](https://huggingface.co/spaces/nareen99/Groq_Powered_Chat)

---

## 🎯 **Project Objectives**

### ✔ 1. Solve API issues in Google Colab

* Understanding `userdata.get()`
* Fixing environment variable problems
* Avoiding key exposure
* Handling exceptions cleanly

### ✔ 2. Learn Deployment Concepts

* Running apps in Google Colab
* Building a full chatbot UI with Gradio
* Deploying Python apps on Hugging Face Spaces
* Auto-building with `requirements.txt`

### ✔ 3. Saving Secrets the Right Way

* Using **Colab Secrets** for development
* Using **Hugging Face Secrets** for production deployment
* Preventing accidental key leaks

---

## 🚀 **Features of This ChatBot**

* 💬 Powered by **Groq** (`llama3` models)
* 🎨 **Gen-Z themed UI** (rose + sky hues)
* 🤖 Clean multi-turn chat
* 🔐 Secure key handling
* ⚡ Fast + modern design
* 🌐 Deployable on Hugging Face
* 📱 Mobile-friendly layout

---

# 🧩 **How the Project Works**

### **1. Development in Google Colab**

* Install dependencies
* Load API Key from Colab Secrets
* Build chatbot logic (`ask_groq()`)
* Add a beautiful Gen-Z Gradio interface

### **2. Deployment on Hugging Face**

* Prepare `app.py`
* Add dependencies to `requirements.txt`
* Create a Space and choose **Gradio**
* Upload files
* Add your key in:
  `Settings → Secrets → GROQ_API_KEY`

---

# 📂 **Project Structure**

```
.
├── app.py              # Main application for Hugging Face
├── requirements.txt    # Dependencies for the Space
└── README.md           # Project documentation
```

---

# 🖥️ **Local / Colab Development**

In Colab:

```
from google.colab import userdata
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

Run the Gradio chatbot cell, test responses, and fix errors.

---

# 🌐 **Deployment Steps (Hugging Face)**

1. Create a new Space
2. Select **Gradio**
3. Upload:

   * `app.py`
   * `requirements.txt`
4. Add a secret:
   **GROQ_API_KEY**
5. Space auto-builds and launches your chatbot!

---

# ❤️ Credits

**Developer:** *Nareen Asad*
**Powered by:** Groq + Gradio
**Deployed on:** Hugging Face Spaces

