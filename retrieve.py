import numpy as np

def retrieve(query, vector_store, top_k=5):
    query_embedding = vector_store.model.encode([query])
    distances, indices = vector_store.index.search(
        np.array(query_embedding), top_k
    )

    retrieved_chunks = []
    for idx in indices[0]:
        retrieved_chunks.append(vector_store.text_chunks[idx])

    return retrieved_chunks

