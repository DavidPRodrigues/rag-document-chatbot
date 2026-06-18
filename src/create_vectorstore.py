from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from load_documents import load_pdf_documents

load_dotenv()

VECTORSTORE_DIR = "vectorstore/chroma"

def create_vectorstore():
    print('starting vector store creation..')
    
    documents = load_pdf_documents()

    if not documents:
        print('No documents found, add a pdf first')
        return
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap = 150
    )

    chunks = splitter.split_documents(documents)

    print(f"split documents into {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory= VECTORSTORE_DIR
    )

    print(f"vector stored at: {VECTORSTORE_DIR}")

if __name__ == "__main__":
    create_vectorstore()