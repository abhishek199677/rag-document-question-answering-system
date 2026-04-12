import streamlit as st
import os
import logging
from src.bot import RAGBot

# Ensure required directories exist
os.makedirs('logs', exist_ok=True)
os.makedirs('data', exist_ok=True)

# Setup Logging
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Page Config
st.set_page_config(
    page_title="MemoryBot | PDF Intelligence",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .css-1d391kg {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
        color: #1E3A8A;
        font-family: 'Outfit', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Bot in Session State
if 'bot' not in st.session_state:
    st.session_state.bot = RAGBot()

# Sidebar for Upload
with st.sidebar:
    st.title("📁 Document Portal")
    uploaded_file = st.file_uploader("Upload PDF Knowledge Base", type="pdf")
    
    if uploaded_file:
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with st.spinner("Processing Document..."):
            try:
                num_chunks = st.session_state.bot.ingest_pdf(file_path)
                st.success(f"Indexed {num_chunks} text segments!")
            except Exception as e:
                st.error(f"Processing failed: {e}")

# Main Chat Interface
st.title("🤖MemoryBot: Production-Grade RAG Engine")
st.markdown("---")

# Chat Container
chat_container = st.container()

with chat_container:
    if not uploaded_file:
        st.info("👋 Welcome! Please upload a PDF in the sidebar to start querying.")
    
    # Display Memory
    for msg in st.session_state.bot.memory:
        role = "User" if msg["role"] == "user" else "Assistant"
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# User Input
if user_question := st.chat_input("Ask anything about the document..."):
    with st.chat_message("user"):
        st.write(user_question)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.bot.ask(user_question)
                st.markdown(response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Footer
st.markdown("---")
st.caption("Powered by OpenAI & FAISS | Production Grade Implementation")
