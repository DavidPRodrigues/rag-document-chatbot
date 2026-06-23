from langchain_ollama import OllamaLLM
from query_rag import search_documents

def generate_answer(question: str, k: int = 3):
    docs = search_documents(question, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
 you are a helpful assistant. Answer the question using only the context below.
 If the asnwer is not in the context, say: "I could not find this information in the document."

 context:
 {context}

 Question:
 {question}

 Answer:
 """
    llm = OllamaLLM(model="llama3.2")
    answer = llm.invoke(prompt)

    return answer, docs

if __name__ == '__main__':
    question = input("ask a question:")
    answer, docs = generate_answer(question)

    print("\nAnswer:\n")
    print(answer)