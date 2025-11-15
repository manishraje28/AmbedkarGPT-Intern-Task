"""
AmbedkarGPT - Local RAG Prototype
Built for: Kalpit Pvt Ltd, UK - AI Intern Hiring : Assignment 1
Author: Manish Raje

This script implements a Retrieval-Augmented Generation (RAG) pipeline using:
- LangChain (Runnables API)
- ChromaDB (local vector store)
- HuggingFace Embeddings (MiniLM-L6-v2)
- Ollama + Mistral (local LLM)

Fully offline, no API keys required.
"""

import os
import sys
from pathlib import Path

# LangChain RAG Components
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama

# Modern LangChain API
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SPEECH_PATH = DATA_DIR / "speech.txt"
CHROMA_DIR = BASE_DIR / "chroma_db"

# Step 1 — Load Document
def load_documents(path: Path):
    if not path.exists():
        print(f"ERROR: speech file not found at {path}")
        sys.exit(1)

    loader = TextLoader(str(path), encoding="utf-8")
    docs = loader.load()
    return docs

# Step 2 — Split Document into Chunks
def split_documents(docs):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50
    )
    return splitter.split_documents(docs)

# Step 3 — Create Embeddings
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# Step 4 — Create or Load Chroma Vector Store
def build_or_load_vectorstore(texts, embeddings, persist_directory="./chroma_db"):
    if os.path.isdir(persist_directory) and os.listdir(persist_directory):
        print("Loading existing Chroma DB...")
        vectordb = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
    else:
        print("Creating Chroma DB for first time...")
        vectordb = Chroma.from_documents(
            texts,
            embeddings,
            persist_directory=persist_directory
        )
        vectordb.persist()

    return vectordb

# Step 5 — Build RAG Retrieval + LLM Pipeline
def build_rag(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
Use ONLY the following context to answer the question.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
""")
    # LLM (local Mistral from Ollama)
    model = Ollama(model="mistral")

    # Runnable graph (retriever → prompt → model)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
    )

    return rag_chain

# Step 6 — Main CLI Loop
def main():
    print("AmbedkarGPT\n")

    docs = load_documents(SPEECH_PATH)
    texts = split_documents(docs)
    embeddings = get_embeddings()

    vectordb = build_or_load_vectorstore(texts, embeddings, str(CHROMA_DIR))

    rag_chain = build_rag(vectordb)

    print("\nAsk any question about the speech (type 'exit' to quit):\n")

    while True:
        try:
            query = input("> ").strip()
        except KeyboardInterrupt:
            print("\nInterrupted. Goodbye!")
            break

        if not query:
            continue
        if query.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        try:
            answer = rag_chain.invoke(query)
            print("\n--- Answer ---")
            print(answer)
            print("----------------\n")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
