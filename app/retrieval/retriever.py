def create_retriever(index):

    retriever = index.as_retriever(
        similarity_top_k=2
    )

    return retriever