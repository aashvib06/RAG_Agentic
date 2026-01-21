import os

def load_documents(data_dir):
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                text = f.read()
                documents.append({
                    "source": filename,
                    "text": text
                })
    return documents
