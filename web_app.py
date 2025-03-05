import streamlit as st
from src.agent import agent

st.title("AI-Powered Research Tool 📈")
st.sidebar.title("Enter URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

# Scrape and index articles
if st.sidebar.button("Process URLs"):
    for url in urls:
        # scraped_text = agent.run("Scrape Website", url)
        scraped_text = agent.invoke({"input": f"Scrape Website: {url}"})
        indexing_status = agent.run("Index Documents", scraped_text)
        st.write(indexing_status)

# Query input for RAG pipeline
query = st.text_input("Ask a question:")
if query:
    answer, sources = agent.run("Retrieve Answer", query)

    st.header("Answer")
    st.write(answer)

    if sources:
        st.subheader("Sources:")
        st.write(sources)