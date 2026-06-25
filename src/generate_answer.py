from langchain_groq import ChatGroq


def generate_answer(question, docs):
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""You are a helpful assistant. Answer the question using only the context below.
If the answer is not in the context, say: "I could not find this information in the document."

Context:
{context}

Question:
{question}

Answer:"""

    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
    response = llm.invoke(prompt)

    return response.content