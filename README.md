🧠 AmbedkarGPT – RAG-Based Q&A System

A Submission for the AI Intern Assignment

AmbedkarGPT is a fully offline Retrieval-Augmented Generation (RAG) system that answers questions only from the provided text of Dr. B. R. Ambedkar’s speech.
It uses:

LangChain (latest runnables API)

ChromaDB (local vector store)

HuggingFace sentence-transformers/all-MiniLM-L6-v2

Ollama + Mistral 7B

Python 3.8+

No API keys, no paid services, no external dependencies — everything runs locally.

📌 Features

Fully offline RAG pipeline

Local semantic search using ChromaDB

Embeddings powered by MiniLM-L6-v2

Context-aware answers using Mistral (via Ollama)

Simple, clean CLI interface for Q&A

Well-structured, production-ready Python code

100% compliant with assignment instructions

📁 Project Structure
AmbedkarGPT-Intern-Task/
│
├── data/
│   └── speech.txt
│
├── src/
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task

2️⃣ Create & activate virtual environment
python -m venv venv
.\venv\Scripts\activate       # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🤖 Install Ollama & Download Mistral 7B
Install Ollama

Download from:
https://ollama.com/download

Pull the model
ollama pull mistral


If mistral fails due to network timeout, pull a smaller fallback:

ollama pull mixtral


Then update in main.py:

model = Ollama(model="mixtral")

▶️ Running the Application

Start the CLI chatbot:

python src/main.py


Example interaction:

> What does Ambedkar identify as the root cause of caste?

--- Answer ---
Ambedkar argues that the root cause of caste is the belief in the sanctity and infallibility of the shastras.

🧬 How the RAG Pipeline Works

The system follows a modern RAG architecture:

Load the input text (speech.txt)

Split into manageable chunks (300 chars + overlap)

Generate embeddings using MiniLM

Store vectors locally using ChromaDB

Convert user query → embedding

Retrieve top 3 most relevant chunks

Insert context + question into a prompt template

Send prompt to Mistral via Ollama

Return a grounded, accurate answer

This ensures zero hallucination and completely local inference.

🗂 Deliverables (as per assignment)

✔ main.py — fully commented, clean Python code

✔ requirements.txt — contains all dependencies

✔ speech.txt — provided speech file

✔ README.md — detailed setup + technical explanation

✔ Public GitHub repository named AmbedkarGPT-Intern-Task

📜 License

This project is created solely for the intern assignment and educational purposes.