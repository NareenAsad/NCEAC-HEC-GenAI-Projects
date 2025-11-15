# 🤖 RAG Pipeline with Fine-Tuned Embeddings

A complete **Retrieval-Augmented Generation (RAG)** system built in Google Colab that combines fine-tuned embeddings, FAISS vector search, and the Groq API for intelligent question-answering.

---

## 🚀 Try It Now!

**Ready to get started?** Click the button below to open the notebook in Google Colab and run it instantly:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HgBD3vBsNlagdtfLw2BNGCVVrzJ7k4N7?usp=sharing)

---

## 🎯 Overview

This project implements a state-of-the-art RAG system that:

- **Fine-tunes** SentenceTransformer embeddings on your custom dataset
- **Indexes** documents using FAISS for lightning-fast similarity search
- **Generates** contextual answers using Groq's LLM API
- **Persists** models and indices for reusability
- **Evaluates** retrieval accuracy with multiple metrics

Perfect for building:
- 💼 Internal knowledge bases
- 🎓 Educational Q&A systems
- 📞 Customer support chatbots
- 📚 Document search engines
- 🔬 Research assistants

---

## ✨ Features

### 🧠 **Intelligent Retrieval**
- Fine-tuned embeddings on domain-specific data
- FAISS vector similarity search (L2 distance)
- Configurable top-k retrieval (1-10 documents)
- Similarity scores for transparency

### 🚀 **Powerful Generation**
- Groq API integration (llama-3.1, mixtral models)
- Context-aware answer generation
- Adjustable temperature (0.0-1.0)
- Multiple model support

### 📂 **Flexible Data Loading**
- **JSON**: FAQ pairs, structured data
- **CSV**: Tabular data with auto-detection
- **TXT**: Plain text with chunking
- **PDF**: Document extraction (multi-page)

### 💾 **Persistence**
- Save/load fine-tuned embedding models
- Save/load FAISS indices
- Save/load document stores
- Quick reload for production

### 📊 **Evaluation Metrics**
- Retrieval accuracy
- Mean Reciprocal Rank (MRR)
- Average cosine similarity
- Custom metrics support

---

## 🏗️ Architecture

```
┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Embedding Model        │
│  (Fine-tuned MiniLM)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  FAISS Vector Store     │
│  (Similarity Search)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Top-K Documents        │
│  (Retrieved Context)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Groq API               │
│  (Answer Generation)    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Final Answer           │
└─────────────────────────┘
```

---

## 🛠️ Installation

### **Prerequisites**
- Python 3.8+
- Google Colab account (recommended)
- Groq API key ([Get one here](https://console.groq.com))

### **Dependencies**

```bash
pip install sentence-transformers faiss-cpu groq pandas numpy scikit-learn PyPDF2 torch transformers
```

Or use the provided requirements:

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### **Option 1: Run in Google Colab (Recommended)**

Click the badge below to open the notebook directly in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HgBD3vBsNlagdtfLw2BNGCVVrzJ7k4N7?usp=sharing)

### **Option 2: Run Locally**

**Step 1: Clone/Download the Notebook**

Open the notebook in Jupyter.

**Step 2: Set Your API Key**

```python
GROQ_API_KEY = "your_groq_api_key_here"  # Get from https://console.groq.com
MODEL_NAME = "llama-3.1-8b-instant"
```

**Step 3: Run All Cells**

The notebook will:
1. Install dependencies
2. Load sample HR FAQ dataset
3. Fine-tune embeddings (3 epochs)
4. Build FAISS index
5. Save models and indices
6. Run 3 test queries
7. Display results with similarity scores

**Step 4: Test with Your Own Query**

```python
query = "What are the vacation benefits?"
result = rag.query(query, top_k=3, temperature=0.7)

print(f"Answer: {result['answer']}")
print(f"Retrieved {result['num_retrieved']} documents")
```

**Expected Output:**
```
Answer: Full-time employees receive 20 vacation days per year, 
plus 10 public holidays and 5 sick days. This is part of our 
comprehensive benefits package...

Retrieved 3 documents
```

---

## 🙏 Acknowledgments

Built with:
- [SentenceTransformers](https://www.sbert.net/) - Embedding models
- [FAISS](https://github.com/facebookresearch/faiss) - Vector search
- [Groq](https://groq.com/) - Fast LLM inference
- [PyTorch](https://pytorch.org/) - Deep learning framework

---