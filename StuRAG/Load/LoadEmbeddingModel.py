from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name=r"G:\models\paraphrase-multilingual-MiniLM-L12-v2",
        model_kwargs={
            "device": "cuda",
            "local_files_only": True,
        },
    )
