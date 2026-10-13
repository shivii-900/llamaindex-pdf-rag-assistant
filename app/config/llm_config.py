from llama_index.llms.google_genai import GoogleGenAI

from app.config.settings import (
    GOOGLE_CLOUD_LOCATION,
    GOOGLE_CLOUD_PROJECT,
)

llm = GoogleGenAI(
    model="gemini-2.5-flash",
    vertexai_config={
        "project": GOOGLE_CLOUD_PROJECT,
        "location": GOOGLE_CLOUD_LOCATION,
    },
)