AmbedkarGPT – Intern Task (RAG Prototype)

A fully offline, local Retrieval-Augmented Generation (RAG) system built using:

LangChain (latest runnables API)

ChromaDB (local vector store)

HuggingFace Embeddings (MiniLM-L6-v2)

Ollama (Mistral 7B)

Python 3.8+

This model answers questions based only on Dr. Ambedkar’s speech (speech.txt) using custom retrieval.
No API keys, no paid services, no internet required.

🚀 Features

✔ Local RAG pipeline (private, free)
✔ Text loading, chunking & embeddings
✔ Semantic search with ChromaDB
✔ Context retrieval (top 3 chunks)
✔ Mistral LLM via Ollama
✔ Well-commented, clean Python code
✔ CLI question-answering interface

🛠️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task

2️⃣ Create a virtual environment
python -m venv venv
.\venv\Scripts\activate    # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🤖 Install Ollama & Mistral
Install Ollama:

https://ollama.com/download

Pull Mistral 7B:
ollama pull mistral


If mistral fails to download:

ollama pull mistral


Then update:

model = Ollama(model="mistral")

▶️ Run the Application
python src/main.py


Example interaction:

> What does the text say is the real remedy for the caste problem?

--- Answer ---
 The text suggests that the real remedy for the caste problem is to destroy the belief in the sanctity of the shastras.
----------------

> What is considered the real enemy in the text?

--- Answer ---
 In the provided context, the "belief in the sanctity of the shastras" is considered the real enemy.
----------------

> Why does the speaker view the shastras as the foundation of caste?

--- Answer ---
 The speaker views the shastras as the foundation of caste because, according to the given context, he believes that as long as people believe in the sanctity of the shastras, they will never be able to get rid of caste. He suggests that the problem of caste is rooted in the authority of the shastras and that the work of social reform necessitates destroying this belief in their sanctity.
----------------

📚 Technical Architecture (RAG Flow)

1. Load speech.txt

2. Split into 300-character chunks

3. Convert chunks → embeddings

4. Store embeddings in ChromaDB

5. Convert user query → embedding

6. Retrieve top 3 most similar chunks

7. Insert context into prompt template

8. Send to Ollama Mistral for final answer

📦 Deliverables (As Required)

✔ main.py (well-commented)
✔ requirements.txt
✔ speech.txt (/data/speech.txt)
✔ README.md
✔ Public GitHub repository: AmbedkarGPT-Intern-Task

🎉 Done!
