from langchain_google_genai import GoogleGenerativeAI
import os

api_key = "AIzaSyCfmvRKpn2mn0hTj2-O0h8MWA4uxcNzm0U"

llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)
print(
    llm.invoke(
        "What are some of the pros and cons of Python as a programming language?"
    )
)