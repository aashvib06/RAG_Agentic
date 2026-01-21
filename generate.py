from openai import OpenAI

client = OpenAI()

def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(
        [chunk["text"] for chunk in retrieved_chunks]
    )

    prompt = f"""
You are a research assistant.
Answer the question ONLY using the context below.
If the answer is not present, say you don't know.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
