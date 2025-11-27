# 📘 RAG-Based PDF Assistant

**A simple Retrieval-Augmented Generation (RAG) app powered by Groq + FAISS + Sentence Transformers.**
Ask questions from your PDFs or Google Drive documents instantly.

---

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [RAG-Based PDF Assistant – Hugging Face Demo](https://huggingface.co/spaces/nareen99/RAG-Based-Streamlit-App)

---

## 🚀 Features

### ✅ **1. Upload PDFs or Use Google Drive Links**

* Supports **multiple PDF uploads**
* Supports **unlimited Google Drive links**
* Automatically downloads and extracts content

### ✅ **2. Automatic Text Extraction**

* Uses **PyPDF2** for fast text extraction
* Handles multi-page documents easily

### ✅ **3. Smart Chunking + Embeddings**

* Uses **RecursiveCharacterTextSplitter**
* Embeddings created using:
  `sentence-transformers/all-MiniLM-L6-v2`
* Stored in **FAISS CPU** (HuggingFace compatible)

### ✅ **4. Fast LLM Answers (Groq)**

* Uses **openai/gpt-oss-20b (Groq hosted)**
* Responds using both query + document context

### ✅ **5. Clean Streamlit UI**

* Sidebar for uploads and links
* Centered modern interface
* Status updates during processing
* Fully responsive layout

---

## 🧩 How It Works (RAG Pipeline)

1. **Upload PDF or paste Google Drive link**
2. **Extract text** using PyPDF2
3. **Chunk text** into small overlapping parts
4. **Convert chunks into embeddings**
5. **Store embeddings in FAISS vector DB**
6. **User enters query**
7. **Retrieve top relevant chunks**
8. **Send query + retrieved context to Groq LLM**
9. **LLM generates final answer**

---

## 📦 Installation (Local)

Clone the repo:

```bash
git clone <your-repo-url>
cd rag-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Deployment on Hugging Face Spaces

This app is designed to run **perfectly on Hugging Face** using:

```
app.py
requirements.txt
```

### Add Your Secret

In Hugging Face:

```
Settings → Secrets → New Secret
Key: GROQ_API_KEY
Value: your-groq-api-key
```

---

## 📁 Project Files

```
📦 RAG-PDF-Assistant
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Requirements

```
streamlit
requests
PyPDF2
sentence-transformers
transformers
groq
langchain
langchain-community
faiss-cpu
```

---

## 🧠 Model Used

* **Embedding Model:** sentence-transformers/all-MiniLM-L6-v2
* **LLM:** openai/gpt-oss-20b (via Groq API)

---

## ❤️ Credits

Built using:

* **Groq Inference API**
* **FAISS Vector Search**
* **LangChain**
* **Streamlit**
* **Sentence Transformers**
