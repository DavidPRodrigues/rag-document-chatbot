import os
import tempfile

import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from generate_answer import generate_answer

if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]


st.title("RAG Document Chatbot")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        pdf_path = tmp.name

    documents = PyPDFLoader(pdf_path).load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)

    st.success(f"Document loaded and split into {len(chunks)} chunks.")

    question = st.text_input("Ask a question about your document:")

    if question:
        docs = vectorstore.similarity_search(question, k=3)
        answer = generate_answer(question, docs)

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Show source chunks"):
            for i, doc in enumerate(docs, start=1):
                st.markdown(f"**Source {i}**")
                st.write(doc.page_content)