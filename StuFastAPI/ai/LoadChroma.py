from langchain_chroma import Chroma
from ai.LoadEmbeddingModel import load_embedding_model
import os
from dotenv import load_dotenv
load_dotenv()


def load_chroma_conn():
    return Chroma(
    collection_name=os.getenv("CHROMADB_NAME"),
    persist_directory= os.getenv("CHROMADB_PATH"),
    embedding_function=load_embedding_model()
)