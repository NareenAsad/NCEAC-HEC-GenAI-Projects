# 📚 AI Study Assistant (RAG-based)

This is a Streamlit app that acts as an AI-powered study assistant.  
It uses **Retrieval-Augmented Generation (RAG)** to answer questions based on your uploaded study materials.

## 🌐 Live Demo

🚀 **Try it now on Hugging Face Spaces:**  
👉 [AI Study Assistant – Hugging Face Demo](https://huggingface.co/spaces/nareen99/AI-Study-Assistant)


## Features

- Upload study materials (PDF, DOCX, TXT, CSV, XLSX)
- Automatic text extraction with OCR for scanned PDFs
- Semantic search over documents using **FAISS**
- Chat with your study materials
- Generate simplified summaries tailored to your education level
- Download summaries as PDF

## How to Deploy

1. Create a Hugging Face Space and select **Streamlit**.
2. Add your `GROQ_API_KEY` in **Secrets**.
3. Upload `app.py` and `requirements.txt`.
4. Run the Space.

## Usage

- Upload your study materials on the sidebar.
- Type a question about your study materials.
- Optionally generate a short summary and download it as a PDF.

## Requirements

- Python 3.10+
- Hugging Face account with a Space
- GROQ API key
