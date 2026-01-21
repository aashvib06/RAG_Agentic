from openai import OpenAI

client = OpenAI()

def needs_more_context(query, retrieved_chunks):
    context = "\n\n".join([chunk["text"] for chunk in retrieved_chunks])

    prompt = f"""
You are evaluating whether enough information is available to answer a question.

Question:
{query}

Context:
{context}

Is the context sufficient to answer the question confidently?
Answer ONLY 'YES' or 'NO'.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    decision = response.choices[0].message.content.strip()
    return decision == "NO"
