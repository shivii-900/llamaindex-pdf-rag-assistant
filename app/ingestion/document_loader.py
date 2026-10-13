from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PDFReader


def load_documents():

    documents = SimpleDirectoryReader(
        input_dir="data/documents",
        file_extractor={
            ".pdf": PDFReader()
        }
    ).load_data()

    return documents