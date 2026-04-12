import faiss
import numpy as np
import logging

class VectorStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
    
    def add_embeddings(self, embeddings):
        """Adds embeddings to the FAISS index."""
        try:
            embed_np = np.array(embeddings).astype('float32')
            self.index.add(embed_np)
        except Exception as e:
            logging.error(f"Error adding embeddings to index: {e}")
            raise

    def search(self, query_embedding, top_k=3):
        """Searches for the most similar embeddings."""
        try:
            query_np = np.array([query_embedding]).astype('float32')
            distances, indices = self.index.search(query_np, top_k)
            return indices[0]
        except Exception as e:
            logging.error(f"Error searching index: {e}")
            raise
