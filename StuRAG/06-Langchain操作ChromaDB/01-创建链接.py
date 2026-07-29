from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

"""
更准确地说，是为了将需要存入向量数据库的文本向量化，而不是将向量数据库向量化
向量化模型负责计算向量，向量数据库负责存储向量

为什么要先创建向量化模型：因为向量数据库不会自己计算向量
"""

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

print(client_db)

