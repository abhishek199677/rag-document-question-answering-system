# 🤖 MemoryBot: Production-Grade RAG Engine

MemoryBot is a professional Retrieval-Augmented Generation (RAG) system designed for intelligent document interaction. It leverages **OpenAI** for advanced embeddings and chat reasoning, coupled with **FAISS** for lightning-fast vector similarity search.

---

## 🏗️ Professional Project Structure
The repository follows industry-standard modular patterns, ensuring scalability and ease of maintenance:

```text
rag-document-question-answering-system/
├── .github/                # CI/CD Workflows
├── data/                   # Knowledge Base (PDF storage)
├── docs/                   # Technical Documentation & Diagrams
├── legacy/                 # Historical/Backup files
├── logs/                   # System Performance & Audit Logs
├── src/                    # Core Source Code
│   ├── api_client.py       # LLM & Embedding Integrations
│   ├── bot.py              # Orchestration Logic
│   ├── processor.py        # Document Parsing & Chunking
│   └── vector_db.py        # Vector Store Management
├── tests/                  # Automated Test Suite
├── .env.example            # Environment Configuration Template
├── LICENSE                 # MIT License
├── main.py                 # Streamlit Production Interface
├── requirements.txt        # Managed Dependencies
└── README.md               # Project Manifesto
```

## 🚀 Key Features
- **Modular RAG Pipeline**: Decoupled ingestion, indexing, and retrieval layers.
- **High-Performance Search**: FAISS-powered semantic retrieval for millisecond response times.
- **Premium UX/UI**: Sleek, responsive Streamlit dashboard with conversational memory.
- **Production-Ready Logging**: Comprehensive logging for debugging and monitoring.
- **CI/CD Integrated**: Automated linting and testing via GitHub Actions.

## 🛠️ Quick Start

### 1. Installation
Clone the repository and install the required packages:
```bash
pip install -r requirements.txt
```

### 2. Configuration
Copy the environment template and provide your API credentials:
```bash
cp .env.example .env
# Edit .env with your OPENAI_API_KEY
```

### 3. Execution
Launch the production server:
```bash
streamlit run main.py
```

## 🧠 Core Architecture
1. **Extraction**: `processor.py` handles multi-page PDF text extraction and semantic chunking.
2. **Embedding**: `api_client.py` transforms text chunks into high-dimensional vectors.
3. **Indexing**: `vector_db.py` constructs a spatial index for efficient querying.
4. **Reasoning**: `bot.py` manages the conversational flow, context injection, and LLM synthesis.

---
Developed with focus on **Reliability**, **Performance**, and **Developer Experience**.
