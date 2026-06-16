from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


DOCUMENTS_DIR =  Path('data/documents')

def load_pdf_documents():
    pdf_files = list(DOCUMENTS_DIR.glob("*.pdf"))

    if not pdf_files:
        print('no pdf files found!!')
        return[]
    
    all_documents = []

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file}")

        loader = PyPDFLoader(str(pdf_file))
        documents = loader.load()

        all_documents.extend(documents)

    print(f"\n loaded {len(all_documents)} pages from {len(pdf_files)} PDF fiels")
    return all_documents

if __name__ == "__main__":
    documents = load_pdf_documents()

    if documents:
        print("\n Example page content:")
        print(documents[0].page_content[:500])

        print("\n Metadata:")
        print(documents[0].metadata)

        