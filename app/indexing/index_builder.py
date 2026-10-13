import os

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)

from llama_index.core.node_parser import SentenceSplitter

from app.config.embedding_config import embed_model


STORAGE_DIR = "storage"


def create_nodes(documents):

    splitter = SentenceSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    nodes = splitter.get_nodes_from_documents(
        documents
    )

    return nodes


def build_index(nodes):

    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model
    )

    index.storage_context.persist(
        persist_dir=STORAGE_DIR
    )

    return index


def load_index():

    storage_context = StorageContext.from_defaults(
        persist_dir=STORAGE_DIR
    )

    index = load_index_from_storage(
        storage_context,
        embed_model=embed_model
    )

    return index


def index_exists():

    return (
        os.path.exists(STORAGE_DIR)
        and len(os.listdir(STORAGE_DIR)) > 0
    )