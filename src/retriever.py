import os
import pickle
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI

FILE_PATH = "faiss_store.pkl"
llm = OpenAI(temperature=0.7, max_tokens=500)

def retrieve_answer(query):
    """Retrieves an answer from indexed documents based on the query."""
    if not os.path.exists(FILE_PATH):
        return "No data indexed yet! Please scrape website first."

    with open(FILE_PATH, "rb") as f:
        vectorstore = pickle.load(f)

    retriever = vectorstore.as_retriever()
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)
    result = chain({"question": query}, return_only_outputs=True)

    return result["answer"], result.get("sources", "")
