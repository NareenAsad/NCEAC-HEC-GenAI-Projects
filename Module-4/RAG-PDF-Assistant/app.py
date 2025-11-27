import os
import requests
from io import BytesIO
from PyPDF2 import PdfReader
import streamlit as st

from groq import Groq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ------------------ UI CONFIG ------------------
st.set_page_config(page_title="RAG PDF Assistant", page_icon="📘", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center; color:#3B82F6;'>📘 RAG-Based PDF Assistant</h1>
    <p style='text-align: center; font-size:18px; color:#555;'>
        Upload PDFs or add Google Drive links & ask anything!
    </p>
    <hr style="border:1px solid #ddd;">
    """,
    unsafe_allow_html=True,
)

# ------------------ Groq Client ------------------
groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found! Add it in Hugging Face → Settings → Secrets.")
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
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)

def create_embeddings_and_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embedding=embeddings)

def get_answer(query, vector_db):
    docs = vector_db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])
    llm_response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": f"Use this context:\n{context}"},
            {"role": "user", "content": query},
        ],
        model="openai/gpt-oss-20b",
    )
    return llm_response.choices[0].message.content

# ------------------ Session State ------------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------ Sidebar ------------------
st.sidebar.header("📥 Upload / Add Documents")
uploaded_pdfs = st.sidebar.file_uploader("Upload PDF Files", type=["pdf"], accept_multiple_files=True)
drive_links_input = st.sidebar.text_area(
    "Google Drive PDF Links (one per line)",
    placeholder="https://drive.google.com/file/d/xxxx/view?usp=sharing"
)
process_btn = st.sidebar.button("⚙️ Process Documents")

# ------------------ Process PDFs / Drive Links ------------------
if process_btn:
    st.info("⏳ Processing documents... Please wait.")
    all_chunks = []

    # Uploaded PDFs
    if uploaded_pdfs:
        for file in uploaded_pdfs:
            pdf_bytes = BytesIO(file.read())
            text = extract_text_from_pdf(pdf_bytes)
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
            st.success(f"✔ Processed {file.name} ({len(chunks)} chunks)")

    # Google Drive links
    if drive_links_input.strip():
        for link in drive_links_input.splitlines():
            try:
                pdf_bytes = download_pdf_from_drive(link)
                text = extract_text_from_pdf(pdf_bytes)
                chunks = chunk_text(text)
                all_chunks.extend(chunks)
                st.success(f"✔ Processed link: {link} ({len(chunks)} chunks)")
            except Exception as e:
                st.error(f"❌ Error: {e}")

    if all_chunks:
        st.session_state.vector_db = create_embeddings_and_store(all_chunks)
        st.success("🎉 All documents processed! You can now ask questions.")

# ------------------ Chat Interface ------------------
st.subheader("💬 Ask a Question")

query = st.text_input("Enter your question here:")

if st.button("Send") and query.strip() != "":
    if st.session_state.vector_db is None:
        st.warning("⚠ Please upload PDFs or add Google Drive links first!")
    else:
        with st.spinner("Thinking..."):
            answer = get_answer(query, st.session_state.vector_db)
            st.session_state.chat_history.append({"user": query, "bot": answer})

# ------------------ Display Chat History ------------------
for chat in st.session_state.chat_history:
    st.markdown(f"<div style='background-color:#E3F2FD; padding:8px; border-radius:10px;'><b>You:</b> {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#F1F8E9; padding:8px; border-radius:10px; margin-bottom:5px;'><b>Assistant:</b> {chat['bot']}</div>", unsafe_allow_html=True)
