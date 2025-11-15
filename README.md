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
git clone https://github.com/manishraje28/AmbedkarGPT-Intern-Task
cd AmbedkarGPT-Intern-Task
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
.venv\Scripts\activate       # Windows
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
Then update in main.py:
```python
model = Ollama(model="mistral")
```

---

## ▶️ Running the Application
```bash
python src/main.py
```

Sample run:
```
> What does the text say is the real remedy for the caste problem?
Answer:
In the provided context, the "belief in the sanctity of the shastras" is considered the real enemy.

> What is considered the real enemy in the text?
Answer:
 In the provided context, the "belief in the sanctity of the shastras" is considered the real enemy.

> Why does the speaker view the shastras as the foundation of caste?
Answer :
The speaker views the shastras as the foundation of caste because, according to the given context, he believes that as long as people believe in the sanctity of the shastras, they will never be able to get rid of caste. He suggests that the problem of caste is rooted in the authority of the shastras and that the work of social reform necessitates destroying this belief in their sanctity.
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

