from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(embedding_model_name)
        self.index = None
        self.text_chunks = []

    def build_index(self, chunks):
        texts = [c["text"] for c in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)

        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)  #compare vectors 
        self.index.add(np.array(embeddings))

        self.text_chunks = chunks
