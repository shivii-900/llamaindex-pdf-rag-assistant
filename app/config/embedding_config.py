from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

from app.config.settings import (
    GOOGLE_CLOUD_LOCATION,
    GOOGLE_CLOUD_PROJECT,
)


embed_model = GoogleGenAIEmbedding(
    model_name="gemini-embedding-001",
    vertexai_config={
        "project": GOOGLE_CLOUD_PROJECT,
        "location": GOOGLE_CLOUD_LOCATION,
    },
)
