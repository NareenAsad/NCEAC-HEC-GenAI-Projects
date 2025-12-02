import os
import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from groq import Groq
from PyPDF2 import PdfReader
import docx
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image
import pytesseract

# ---------------------------
# Initialize LLM Client
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not set. Add it in Secrets on Hugging Face Spaces.")
client = Groq(api_key=GROQ_API_KEY)

# ---------------------------
# Utility Functions
# ---------------------------

def extract_text_from_file(file):
    text = ""
    if file.name.endswith(".pdf"):
        try:
            reader = PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            # OCR fallback
            if not text.strip():
                raise ValueError("Empty text layer")
        except Exception:
            try:
                import fitz  # PyMuPDF
                file_bytes = file.read()
                doc = fitz.open(stream=file_bytes, filetype="pdf")
                for page in doc:
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    text += pytesseract.image_to_string(img)
            except Exception as e:
                text = f"Could not extract text from PDF: {e}"

    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
        text = df.to_string()

    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
        text = df.to_string()

    return text


def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]


def create_faiss_index(chunks, model):
    embeddings = model.encode(chunks)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index, embeddings


def retrieve_context(query, model, chunks, index, k=3):
    if index is None or not chunks:
        return ""
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector).astype("float32"), k)
    return " ".join([chunks[i] for i in indices[0]])


def generate_llm_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content


def generate_summary(text, education_level):
    prompt = f"""
You are an educational AI tutor. Summarize the following study content for a student at the {education_level} level.
Use simple, clear, and age-appropriate explanations. Include examples when possible.

Content:
{text}
"""
    return generate_llm_response(prompt)


def create_pdf(summary_text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    text_object = c.beginText(50, 750)
    for line in summary_text.split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)
    c.save()
    buffer.seek(0)
    return buffer


# ---------------------------
# Streamlit UI
# ---------------------------

st.set_page_config(page_title="📚 AI Study Assistant", layout="wide")
st.title("📚 AI Study Assistant (RAG-based)")

st.sidebar.header("⚙️ Settings")
education_level = st.sidebar.selectbox(
    "Select your education level:",
    ["Primary School", "Middle School", "Secondary School", "High School", "Undergraduate", "Graduate"]
)

st.sidebar.markdown("---")
uploaded_files = st.sidebar.file_uploader(
    "Upload study materials (PDF, DOCX, TXT, CSV, XLSX):",
    accept_multiple_files=True
)

# Process files
all_text = ""
if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")
    for file in uploaded_files:
        extracted = extract_text_from_file(file)
        st.write(f"✅ Processed: {file.name} | Extracted {len(extracted)} characters")
        all_text += extracted + "\n"

if all_text.strip():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunks = chunk_text(all_text)
    index, embeddings = create_faiss_index(chunks, model)
else:
    chunks, index = [], None

# Chat interface
st.markdown("### 💬 Chat with your study materials")
user_query = st.text_input("Ask a question about your study materials or any concept:")

if user_query:
    context = retrieve_context(user_query, model, chunks, index) if all_text.strip() else ""
    system_prompt = f"""
You are a friendly and intelligent AI study assistant helping a {education_level} student.
Answer based on the context below if available, otherwise use general knowledge.

Context:
{context}

Question:
{user_query}
"""
    response = generate_llm_response(system_prompt)
    st.markdown("### 🧠 Answer")
    st.write(response)

    if st.button("📝 Generate Short Summary"):
        summary = generate_summary(context if context.strip() else user_query, education_level)
        st.markdown("### ✨ Summary")
        st.write(summary)

        pdf_buffer = create_pdf(summary)
        st.download_button(
            label="📥 Download Summary as PDF",
            data=pdf_buffer,
            file_name="summary.pdf",
            mime="application/pdf"
        )
else:
    st.info("💡 Type a question above to get started.")
