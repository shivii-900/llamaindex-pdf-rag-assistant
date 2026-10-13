from app.config.llm_config import llm

from app.ingestion.document_loader import load_documents

from app.indexing.index_builder import (
    create_nodes,
    build_index,
    load_index,
    index_exists,
)

from app.retrieval.retriever import create_retriever

from app.generation.query_engine import generate_answer


def main():

    # -------------------------
    # Load or create index
    # -------------------------

    if index_exists():

        print("Loading existing index...")
        index = load_index()

    else:

        print("No existing index found.")
        print("Creating new index...")

        documents = load_documents()

        print(
            "Documents loaded:",
            len(documents)
        )

        nodes = create_nodes(documents)

        print(
            "Nodes created:",
            len(nodes)
        )

        index = build_index(nodes)

        print(
            "Index created and saved successfully."
        )

    # -------------------------
    # Create retriever
    # -------------------------

    retriever = create_retriever(index)

    # -------------------------
    # Interactive RAG
    # -------------------------

    print("\nPDF Knowledge Assistant")
    print("Type 'exit' to stop.")

    while True:

        query = input("\nAsk a question: ").strip()

        if query.lower() == "exit":
            print("Exiting assistant.")
            break

        if not query:
            print("Please enter a question.")
            continue

        # Retrieve relevant nodes

        retrieved_nodes = retriever.retrieve(
            query
        )

        # Generate grounded answer

        answer = generate_answer(
            query=query,
            retrieved_nodes=retrieved_nodes,
            llm=llm,
        )

        # Display answer

        print("\nAnswer:")
        print(answer)

        # Display sources

        print("\nSources:")

        for result in retrieved_nodes:

            print(
                f"- {result.node.metadata.get('file_name')} "
                f"| Page {result.node.metadata.get('page_label')} "
                f"| Score: {result.score:.4f}"
            )


if __name__ == "__main__":
    main()