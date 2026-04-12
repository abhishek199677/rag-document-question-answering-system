# 🤖 MemoryBot: Industry-Ready PDF RAG Application

MemoryBot is a professional-grade Retrieval-Augmented Generation (RAG) application that allows users to chat with their PDF documents. It uses **OpenAI** for embeddings and chat completions, and **FAISS** for efficient vector similarity search.

---

## 🏗️ Project Structure
```text
RAG_PDF_Application_Memorybot/
├── .env                # API Keys & Configuration
├── requirements.txt    # Dependencies
├── main.py             # Streamlit UI (Entry Point)
├── src/                # Core Logic
│   ├── api_client.py   # OpenAI API Wrapper
│   ├── processor.py    # PDF & Text Processing
│   ├── vector_db.py    # FAISS Vector Management
│   └── bot.py          # RAG Pipeline Coordinator
├── data/               # Temporary storage for uploaded PDFs
├── logs/               # Application performance logs
└── README.md           # Documentation
```

## 🚀 Features
- **Industry Standard Modular Architecture**: Decoupled UI and business logic.
- **Persistent Knowledge Base**: Efficient indexing using FAISS.
- **Premium UI**: Modern Streamlit interface with chat history support.
- **Environment Management**: Secure handling of API keys via `.env`.
- **Structured Logging**: Track application behavior and errors.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.9+
- An API Key from OpenAI

### 2. Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Rename `.env.example` to `.env` and add your API key:
```env
OPENAI_API_KEY=your_key_here
```

### 4. Running the App
Launch the Streamlit dashboard:
```bash
streamlit run main.py
```

## 🧠 How it Works
1. **Ingestion**: The user uploads a PDF. `processor.py` extracts text and chunks it.
2. **Indexing**: `api_client.py` gets embeddings for chunks, and `vector_db.py` stores them in a FAISS index.
3. **Querying**: When a user asks a question, the query is embedded, and relevant chunks are retrieved.
4. **Generation**: The context + question are sent to OpenAI's LLM (GPT-3.5-Turbo) to generate a response.

---
Created by Antigravity AI
