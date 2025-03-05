import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from src.scraper import scrape_website
from src.indexer import index_documents
from src.retriever import retrieve_answer
import os


APIKEY = "AIzaSyCL_ub6HPpyqt4hCcGyKf8SnwBcR6mMmyI"
# Securely configure API Key (Use AI Studio API Key)
genai.configure(api_key=os.getenv(APIKEY))

# Correct AI Studio-based Gemini model for LangChain
llm = ChatGoogleGenerativeAI(
    model_name="gemini-1.5-flash",
    google_api_key=APIKEY,
    temperature=0.2,
    exclude_defaults=True,
)

# Tools for the agent
scrape_tool = Tool(
    name="Scrape Website",
    func=scrape_website,
    description="Scrapes text from a given website."
)

index_tool = Tool(
    name="Index Documents",
    func=index_documents,
    description="Indexes scraped documents into FAISS."
)

retrieve_tool = Tool(
    name="Retrieve Answer",
    func=retrieve_answer,
    description="Fetches relevant answers from indexed documents."
)

# Initialize agent with AI Studio Gemini model
agent = initialize_agent(
    tools=[scrape_tool, index_tool, retrieve_tool],
    llm=llm,  # ✅ Using AI Studio-compatible Gemini model
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
