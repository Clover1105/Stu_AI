from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# 创建向量化模型
em_model = HuggingFaceEmbeddings(
    # 模型路径
    model_name = r"G:\models\paraphrase-multilingual-MiniLM-L12-v2",
    # 本地化
    model_kwargs={
        "device": "cuda",
        "local_files_only": True,
    }
)

# 创建向量化数据对象
client_db = Chroma(
    persist_directory=r"G:\GitHub\Stu_AI\StuRAG\chromadb_data",
    embedding_function=em_model
)

# 转为检索器接口
retriever = client_db.as_retriever(search_kwargs={"k": 2})
print(retriever)

