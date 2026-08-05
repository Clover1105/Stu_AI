# 构造RAG向量数据库数据集
import pandas as pd
from langchain_core.documents import Document
from langchain_chroma import Chroma
from ai import LoadEmbeddingModel
import os
from dotenv import load_dotenv
load_dotenv()


# 数据集路径
database_path = os.getenv("DATABASE_PATH")

# 向量数据库存储路径
vector_database_path = os.getenv("CHROMADB_PATH")

# 集合名称
collection_name = os.getenv("CHROMADB_NAME")

# pandas读取数据
df = pd.read_csv(database_path)
# print(df['text'])
# print(type(df))

# <class 'pandas.core.frame.DataFrame'> 转 list
data_list = df['text'].tolist()
# print(data_list)

# list 转 list[Document]
documents = [Document(page_content=text, metadata={"source": database_path}) for text in data_list]

# 存入向量数据库
try:
    Chroma.from_documents(
        documents=documents,    # 数据
        embedding= LoadEmbeddingModel.load_embedding_model(),   # 向量化模型
        persist_directory=vector_database_path, # 存储路径
        collection_name=collection_name,    # 集合名称
        collection_metadata={"hnsw:space": "cosine"},   # 匹配规则：余弦相似度

    )
    print("数据存入成功！")
except Exception as e:
    print(f"数据存入失败：{e}")