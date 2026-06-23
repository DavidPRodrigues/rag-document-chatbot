# RAG Document Chatbot

A simple local RAG chatbot that can answer questions about PDF documents.

The project loads a PDF, splits it into smaller text chunks, creates embeddings, stores them in a vector database, retrieves the most relevant chunks, and uses a local Ollama model to generate answers.

## Features

* Load PDF documents
* Split documents into chunks
* Create embeddings using Hugging Face
* Store embeddings in ChromaDB
* Search for relevant document chunks
* Generate answers using Ollama
* Use the chatbot through a Streamlit app

## Tech Stack

* Python
* LangChain
* ChromaDB
* Hugging Face Sentence Transformers
* Ollama
* Streamlit
* PyPDF

## Project Structure

```text
rag-document-chatbot/
│
├── data/documents/          # PDF documents
├── vectorstore/             # Chroma vector database
├── src/
│   ├── load_documents.py
│   ├── create_vectorstore.py
│   ├── query_rag.py
│   ├── generate_answer.py
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

```text
PDF
→ Load document
→ Split into chunks
→ Create embeddings
→ Store in ChromaDB
→ Retrieve relevant chunks
→ Generate answer with Ollama
→ Show answer in Streamlit
```

## Setup

Create a Conda environment:

```bash
conda create -n rag-chatbot python=3.11 -y
conda activate rag-chatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Install Ollama and pull a local model:

```bash
ollama pull llama3.2:1b
```

## Usage

Place your PDF inside:

```text
data/documents/
```

Create the vector store:

```bash
python src/create_vectorstore.py
```

Test retrieval:

```bash
python src/query_rag.py
```

Test answer generation:

```bash
python src/generate_answer.py
```

Run the Streamlit app:

```bash
streamlit run src/app.py
```

Then open the local URL shown in the terminal.

## Example Questions

```text
What is this document about?
Summarize the document.
What skills are mentioned?
What experience is listed?
What are the main points?
```

## Notes

The project runs locally and does not require OpenAI API credits.

The following are ignored by Git:

```text
.env
data/documents/
vectorstore/
```

This keeps private files and generated databases out of GitHub.

## Status

Working local RAG chatbot with PDF loading, local embeddings, ChromaDB retrieval, Ollama answer generation, and a Streamlit interface.
