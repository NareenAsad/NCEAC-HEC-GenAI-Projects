import os
import requests
from io import BytesIO
from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile

import streamlit as st
from groq import Groq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ------------------ UI CONFIG ------------------
st.set_page_config(
    page_title="RAG PDF Assistant",
    page_icon="📘",
    layout="wide",
)

st.markdown(
    """
    <h1 style='text-align: center; color:#4A90E2;'>📘 RAG-Based PDF Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
    Upload PDFs OR provide Google Drive links and ask anything!
    </p>
    """,
    unsafe_allow_html=True,
)

# ------------------ Groq Client ------------------
groq_api_key = os.environ.get("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found! Add it in Hugging Face → Settings → Secrets.")
    st.stop()

client = Groq(api_key=groq_api_key)

# ------------------ Helper Functions ------------------

def download_pdf_from_drive(drive_link):
    try:
        file_id = drive_link.split('/d/')[1].split('/')[0]
        download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
        response = requests.get(download_url)

        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise Exception("Failed to download file")
    except:
        raise Exception("Invalid Google Drive link format.")

def extract_text_from_pdf(pdf_stream):
    pdf_reader = PdfReader(pdf_stream)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def create_embeddings_and_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embedding=embeddings)

def get_answer(query, vector_db):
    docs = vector_db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    llm_response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"Use the following context:\n{context}"},
            {"role": "user", "content": query},
        ],
        model="llama3-8b-8192",
    )

    return llm_response.choices[0].message.content


# ------------------ Sidebar ------------------

st.sidebar.header("Upload / Add Documents")

uploaded_pdfs = st.sidebar.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

drive_links_input = st.sidebar.text_area(
    "Google Drive PDF Links (one per line)",
    placeholder="https://drive.google.com/file/d/xxxx/view?usp=sharing"
)

process_btn = st.sidebar.button("⚙️ Process Documents")


# ------------------ Main Logic ------------------

all_chunks = []

if process_btn:
    st.info("⏳ Processing documents... Please wait.")

    # Process uploaded PDFs
    if uploaded_pdfs:
        for file in uploaded_pdfs:
            st.write(f"Processing uploaded file: **{file.name}**")
            pdf_bytes = BytesIO(file.read())
            text = extract_text_from_pdf(pdf_bytes)
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
            st.success(f"✔ Extracted {len(chunks)} chunks")

    # Process Google Drive links
    if drive_links_input.strip():
        drive_links = drive_links_input.splitlines()
        for link in drive_links:
            st.write(f"🔗 Processing Drive Link: {link}")
            try:
                pdf_bytes = download_pdf_from_drive(link)
                text = extract_text_from_pdf(pdf_bytes)
                chunks = chunk_text(text)
                all_chunks.extend(chunks)
                st.success(f"✔ Extracted {len(chunks)} chunks")
            except Exception as e:
                st.error(f"Error: {e}")

    if not all_chunks:
        st.warning("⚠ No valid documents found!")
    else:
        vector_db = create_embeddings_and_store(all_chunks)
        st.success("Documents processed successfully! You can now ask questions.")

        st.subheader("Ask a Question")
        query = st.text_input("Enter your question:")

        if query:
            with st.spinner("Thinking..."):
                try:
                    answer = get_answer(query, vector_db)
                    st.write("### 🤖 Answer:")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error generating answer: {e}")
