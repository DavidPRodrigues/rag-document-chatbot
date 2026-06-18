from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


VECTORSTORE_DIR = "vectorstore/chroma"


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=VECTORSTORE_DIR,
        embedding_function=embeddings
    )

    return vectorstore


def search_documents(query: str, k: int = 3):
    vectorstore = load_vectorstore()
    results = vectorstore.similarity_search(query, k=k)
    return results


if __name__ == "__main__":
    while True:
        query = input("\nAsk a question about your document, or type 'q' to quit: ")

        if query.lower() == "q":
            break

        results = search_documents(query)

        print("\nTop relevant chunks:\n")

        for i, doc in enumerate(results, start=1):
            print(f"--- Result {i} ---")
            print(doc.page_content[:800])
            print("\nSource:", doc.metadata)
            print()