import logging
from src.api_client import OpenAIClient
from src.processor import PDFProcessor
from src.vector_db import VectorStore

class RAGBot:
    def __init__(self):
        self.api_client = OpenAIClient()
        self.processor = PDFProcessor()
        self.vector_store = None
        self.chunks = []
        self.memory = []

    def ingest_pdf(self, pdf_path):
        """Processes PDF and builds the vector index."""
        text = self.processor.extract_text(pdf_path)
        if not text:
            raise ValueError("No text extracted from PDF.")
        
        self.chunks = self.processor.split_text(text)
        embeddings = self.api_client.get_embeddings(self.chunks)
        
        dimension = len(embeddings[0])
        self.vector_store = VectorStore(dimension)
        self.vector_store.add_embeddings(embeddings)
        
        return len(self.chunks)

    def ask(self, question):
        """Retrieves context and asks the LLM."""
        if not self.vector_store:
            raise ValueError("Please upload and process a PDF first.")
        
        # 1. Get query embedding
        query_embed = self.api_client.get_embeddings([question])[0]
        
        # 2. Retrieve relevant chunks
        indices = self.vector_store.search(query_embed)
        context = "\n\n".join([self.chunks[i] for i in indices if i < len(self.chunks)])
        
        # 3. Build message history
        messages = [
            {"role": "system", "content": "You are a professional AI assistant. Answer the user's question based strictly on the provided context."}
        ]
        
        # Add limited memory (last 3 turns)
        messages.extend(self.memory[-6:])
        
        messages.append({
            "role": "user", 
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        })
        
        # 4. Get response
        reply = self.api_client.get_chat_completion(messages)
        
        # 5. Update memory
        self.memory.append({"role": "user", "content": question})
        self.memory.append({"role": "assistant", "content": reply})
        
        return reply
