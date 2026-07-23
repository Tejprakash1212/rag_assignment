# rag_assignment
# Document Search & Retrieval Streamlit App

This project is an interactive Streamlit application that implements a document retrieval system using Retrieval-Augmented Generation (RAG) concepts. The application allows users to upload PDF or TXT documents, process the content, and search for relevant information using natural language queries. It performs document loading, text preprocessing, chunk creation, embedding generation, and similarity-based retrieval to find the most meaningful sections related to the user's question.

## Features

- 📄 Upload PDF or TXT documents through a user-friendly interface
- ✂️ Automatically extract text and split documents into smaller chunks
- 🧠 Generate embeddings for document chunks to enable semantic search
- 🔍 Search and retrieve the most relevant document sections based on user queries
- 📌 Display top-k matching chunks with their relevance information
- ⚡ Built using Streamlit for an interactive and easy-to-use web interface

The application demonstrates the complete workflow of a Retrieval-Augmented Generation pipeline, where documents are converted into searchable vector representations and relevant context is retrieved before generating responses. This project helps understand the practical implementation of document-based AI applications, including text processing, embeddings, vector search, and information retrieval.

## Technologies Used

- Python
- Streamlit
- LangChain
- Embedding Models
- Vector Similarity Search
- PDF/TXT Document Processing

## How It Works

1. User uploads a PDF or TXT file.
2. The document content is extracted and divided into smaller text chunks.
3. Each chunk is converted into embeddings.
4. The user's query is also converted into an embedding.
5. The system compares embeddings and retrieves the most relevant chunks.
6. The top-k results are displayed in the Streamlit interface.

This project provides a foundation for building advanced AI-powered document assistants and can be further extended by integrating Large Language Models (LLMs) for complete question-answering capabilities.
