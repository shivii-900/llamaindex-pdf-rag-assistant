def generate_answer(
    query,
    retrieved_nodes,
    llm
):

    context = "\n\n".join(
        node.node.text
        for node in retrieved_nodes
    )

    prompt = f"""
You are a knowledge assistant.

Answer the user's question using only the provided context.

If the answer is not present in the context, say:
"I could not find this information in the provided documents."

Do not use outside knowledge.

Context:
{context}

User Question:
{query}

Answer:
"""

    response = llm.complete(prompt)

    return str(response)