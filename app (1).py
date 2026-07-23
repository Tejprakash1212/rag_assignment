
import streamlit as st
from functions import (
    load_and_chunk_document,
    create_embeddings,
    search_chunks,
    generate_answer
)

 Commented out IPython magic to ensure Python compatibility.
 %%writefile -a app.py
 
 st.title("📚 Simple RAG Application")
 
 uploaded_file = st.file_uploader("Upload a TXT file", type=["txt"])
 
 query = st.text_input("Enter your question")
 
 api_key = st.text_input("Enter Cohere API Key", type="password")
 
 if st.button("Search"):
 
     if uploaded_file is not None and query and api_key:
         with open("uploaded.txt", "wb") as f:
             f.write(uploaded_file.getbuffer())
 
         chunks = load_and_chunk_document("uploaded.txt")
 
         embeddings = create_embeddings(chunks)
 
         results = search_chunks(query, chunks, embeddings)
 
         st.subheader("Top Matching Chunks")
 
         context = ""
 
         for chunk in results:
             st.write(chunk)
             context += chunk + "\n\n"
 
         answer = generate_answer(query, context, api_key)
 
         st.subheader("Generated Answer")
 
         st.success(answer)
     else:
       st.warning("Please upload a file, enter a question, and provide your API key.")
