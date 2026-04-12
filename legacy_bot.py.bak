import pdfplumber
import numpy as np
import requests
import faiss
import streamlit as st

# Fixed: Removed trailing commas that created tuples instead of strings
EURI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJhNTM3YzM3Zi0xNmFkLTRjZTUtYjRhMC0wNTNjYTIyNzE1YTgiLCJlbWFpbCI6InN1ZGhhbnNodUBldXJvbi5vbmUiLCJpYXQiOjE3NDMyMzkyNTYsImV4cCI6MTc3NDc3NTI1Nn0.HRHeCucOK0hPVZQwyvNoD0GaHarvHNivjJ2l6-xU1HA",
EURI_CHAT_URL = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
EURI_EMBED_URL = "https://api.euron.one/api/v1/euri/alpha/embeddings"

conversation_memory = []

def extract_text_from_pdf(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Handle empty pages
                full_text += page_text + "\n"
    return full_text

def split_text(text, chunk_size=5000, overlap=1000):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))  # Prevent overflow
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0: 
            start = 0
    return chunks

def get_euri_embeddings(texts):
    headers = {
        "Authorization": f"Bearer {EURI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "text-embedding-3-small",
        "input": texts
    }
    res = requests.post(EURI_EMBED_URL, headers=headers, json=payload)
    
    # Fixed: Safe API response handling
    if res.status_code != 200:
        raise Exception(f"Embedding API error: {res.status_code} - {res.text}")
    
    response_data = res.json()
    
    # Handle missing 'data' key
    if 'data' not in response_data:
        raise Exception(f"Unexpected API response: {response_data}")
    
    # Extract embeddings safely
    embeddings = []
    for item in response_data['data']:
        if 'embedding' in item:
            embeddings.append(item['embedding'])
    
    return np.array(embeddings)

def build_vector_store(chunks):
    embeddings = get_euri_embeddings(chunks)
    dimension = embeddings.shape[1]  # Dynamic dimension
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

# Fixed: Removed unused embeddings parameter
def retrieve_context(question, chunks, index, top_k=3):
    q_embed = get_euri_embeddings([question])[0]
    D, I = index.search(np.array([q_embed]), top_k)
    return "\n\n".join([chunks[i] for i in I[0]])

def ask_euri_with_context(question, context, memory=None):
    messages = [
        {"role": "system", "content": "You are a helpful assistant answering questions from a document."}
    ]
    
    # Fixed: Handle memory safely
    if memory:
        messages.extend(memory[-6:])  # Use last 3 exchanges
    
    messages.append({
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {question}"
    })

    headers = {
        "Authorization": f"Bearer {EURI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4.1-nano",
        "messages": messages,
        "temperature": 0.3
    }

    res = requests.post(EURI_CHAT_URL, headers=headers, json=payload)
    
    # Fixed: API error handling
    if res.status_code != 200:
        raise Exception(f"Chat API error: {res.status_code} - {res.text}")
    
    response_data = res.json()
    
    # Fixed: Safe response parsing
    if 'choices' not in response_data or len(response_data['choices']) == 0:
        raise Exception("Invalid API response format")
    
    reply = response_data['choices'][0]['message']['content']
    
    # Update memory if provided
    if memory is not None:
        memory.append({"role": "user", "content": question})
        memory.append({"role": "assistant", "content": reply})
    
    return reply

# Streamlit UI
st.title("📄 PDF Knowledge Extraction RAG Bot")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
user_question = st.text_input("Ask a question about the document")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())  # Better for large files
    
    full_text = extract_text_from_pdf("temp.pdf")
    if not full_text.strip():
        st.error("Failed to extract text from PDF")
    else:
        chunks = split_text(full_text)
        index = build_vector_store(chunks)  # Fixed: Only index needed
        
        st.success("PDF loaded and indexed.")
        
        if user_question:
            context = retrieve_context(user_question, chunks, index)
            try:
                response = ask_euri_with_context(user_question, context, conversation_memory)
                st.markdown("### ✅ Answer:")
                st.write(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
