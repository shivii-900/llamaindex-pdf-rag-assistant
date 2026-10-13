import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_CLOUD_PROJECT = os.getenv(
    "GOOGLE_CLOUD_PROJECT",
    "project-7ae2949e-d62f-4ee4-8d9",
)

GOOGLE_CLOUD_LOCATION = os.getenv(
    "GOOGLE_CLOUD_LOCATION",
    "global",
)