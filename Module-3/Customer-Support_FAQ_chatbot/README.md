# RAG Customer Support Assistant with Groq (Kaggle Edition)

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline for customer support, using a **Hugging Face dataset**, **FAISS embeddings**, and **Groq LLM API** in **Kaggle Notebooks**.

---

## 🚀 Features

* Load a **public Hugging Face dataset** of customer support conversations.
* Convert dataset into **question-answer (QA) pairs**.
* **Chunk long conversations** for better retrieval.
* Embed texts with **Sentence-Transformers** (`all-MiniLM-L6-v2`).
* Build a **FAISS vector index** for semantic search.
* Retrieve top-k relevant answers and feed into **Groq LLM** (or a **mock** if API is unreachable).
* Interactive **chat loop** for querying the assistant.

---

## ⚡ Setup (Kaggle)

```python
# Install required packages
!pip install -q datasets sentence-transformers faiss-cpu requests tqdm

# Load Groq API key from Kaggle Secrets
from kaggle_secrets import UserSecretsClient
import os

user_secrets = UserSecretsClient()
os.environ["GROQ_API_KEY"] = user_secrets.get_secret("GROQ_API_KEY")
```

> ⚠️ Kaggle may have network restrictions. If Groq API is not reachable, the notebook will use a **mock response** to allow testing retrieval and chat logic.

---

## 📦 How it Works

1. **Load Dataset**

```python
from datasets import load_dataset
hf_dataset_id = "NebulaByte/E-Commerce_Customer_Support_Conversations"
dataset = load_dataset(hf_dataset_id)
```

* Columns include `conversation`, `issue_category_sub_category`, `customer_sentiment`, etc.
* QA pairs are built using `issue_category_sub_category` as question and `conversation` as answer.

2. **Chunk & Embed**

* Split long answers into chunks (default 400 characters, 50-character overlap).
* Generate embeddings using **Sentence-Transformers**.

3. **Build FAISS Index**

* Store embeddings in **FAISS** for fast semantic retrieval.

4. **Retrieve & Generate**

* For a user query, retrieve top-k relevant answer chunks.
* Build a context-aware prompt.
* Send prompt to **Groq API** (or fallback mock) for generation.

5. **Chat Loop**

```python
chat_loop(embedder, faiss_idx, top_k=3)
```

* Type your questions.
* Assistant responds using only retrieved context.
* Type `exit` or `quit` to leave.

---

## ⚙️ Config

* **Groq API Key**: Set via **Kaggle Secrets**:

```python
from kaggle_secrets import UserSecretsClient
user_secrets = UserSecretsClient()
os.environ["GROQ_API_KEY"] = user_secrets.get_secret("GROQ_API_KEY")
```

* **Embedding Model**: Default `all-MiniLM-L6-v2`, can be changed in `Embedder()`.

* **Mock Fallback**: If Kaggle cannot reach `api.groq.ai`, the assistant will return:

```text
"This is a mock answer. Groq API is unreachable from Kaggle."
```

---

## 📝 Usage Example

```python
from your_module import build_and_save_index_from_hf, chat_loop

# Build FAISS index from Hugging Face dataset
embedder, faiss_idx = build_and_save_index_from_hf(
    "NebulaByte/E-Commerce_Customer_Support_Conversations",
    index_out_prefix="ecommerce_faiss",
    chunk_size=400
)

# Start interactive chat (mock Groq API if unreachable)
chat_loop(embedder, faiss_idx, top_k=3)
```

---

## ⚠️ Notes

* Designed for **public datasets**, no Hugging Face token required.
* Groq API requires a valid key, but **mock fallback** allows testing in Kaggle.
* Large datasets or long conversations may take time to embed and build FAISS index.

---

## 🛠️ Dependencies

* `datasets`
* `sentence-transformers`
* `faiss-cpu`
* `requests`
* `tqdm`
* `pandas`
* `numpy`

---