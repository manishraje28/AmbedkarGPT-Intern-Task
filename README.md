# 🚀 AmbedkarGPT – RAG-Based Q&A System
### _AI Intern Assignment Submission_

---

## 📘 Overview
AmbedkarGPT is a fully offline **Retrieval-Augmented Generation (RAG)** system designed to answer questions **strictly from the provided speech** by Dr. B. R. Ambedkar.

This project uses:
- **LangChain (Runnables API)**
- **ChromaDB (local vector store)**
- **HuggingFace MiniLM-L6-v2 embeddings**
- **Ollama with Mistral 7B LLM**
- **Python 3.8+**

No API keys, no cloud usage, and fully local inference.

---

## 📂 Project Structure
```
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
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
.env\Scriptsctivate       # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama & Pull Mistral 7B Model

### Install Ollama  
Download from:  
https://ollama.com/download

### Pull the Mistral model  
```bash
ollama pull mistral
```

If Mistral fails to download:
```bash
ollama pull mixtral
```
Then update in main.py:
```python
model = Ollama(model="mixtral")
```

---

## ▶️ Running the Application
```bash
python src/main.py
```

Sample run:
```
> Why does Ambedkar criticize social reformers?

Response:
Because they address the branches instead of the roots, and the true root is belief in the authority of the shastras.
```

---

## 🧬 How the RAG Pipeline Works

1. Load `speech.txt`  
2. Split into ~300-character chunks  
3. Generate embeddings (MiniLM-L6-v2)  
4. Store embeddings in ChromaDB  
5. Convert user query into embedding  
6. Retrieve top 3 similar chunks  
7. Format a prompt using retrieved context  
8. Generate final answer using Mistral (via Ollama)

---

## 📦 Deliverables Included
- `main.py` (fully commented)
- `requirements.txt`
- `speech.txt`
- `README.md`
- Complete public GitHub repository as requested

---

## 📜 License
This project is created solely for the AI intern assignment evaluation.

