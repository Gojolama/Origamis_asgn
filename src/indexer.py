import os
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings # Removed
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Added
from langchain.vectorstores import FAISS

FILE_PATH = "faiss_store.pkl"

def index_documents(docs):
    """Indexes scraped documents into FAISS for retrieval."""
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    chunks = text_splitter.split_text(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # Using Vertex AI Embeddings
    vectorstore = FAISS.from_texts(chunks, embeddings)

    with open(FILE_PATH, "wb") as f:
        pickle.dump(vectorstore, f)

    return "Documents successfully indexed! ✅"