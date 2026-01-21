from ingest import load_documents
from chunking import chunk_documents
from embed_store import VectorStore
from retrieve import retrieve
from generate import generate_answer
from agent import needs_more_context


documents = load_documents("data/")
chunks = chunk_documents(documents)

vector_store = VectorStore()
vector_store.build_index(chunks)

while True:
    query = input("Ask a question: ")
    retrieved = retrieve(query, vector_store)
    if needs_more_context(query, retrieved):
        retrieved = retrieve(query, vector_store, top_k=8)

    answer = generate_answer(query, retrieved)
    print(answer)

