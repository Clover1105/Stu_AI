import chromadb
from chromadb.utils import embedding_functions

# 本地模型
embedding = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=r"thenlper/gte-small-zh",
)

# 创建客户端
client = chromadb.PersistentClient(path="../chroma_data")

# 获取集合
collection = client.get_or_create_collection(
    name="cs01",
    embedding_function=embedding
)

# 查询全部文档
result = collection.get()
print(result)
print("*-"*10)

# 根据 id 查询
result = collection.get(
    ids=["doc_002"],
    # include=["embeddings","documents", "metadatas"]
    include=["documents", "metadatas"]
)
print(result)
print("*-"*10)

# 根据 metadata 查询
result = collection.get(
    where={"topic":"RAG"},
    include=["documents", "metadatas"]
)
print(result)
print("*-"*10)

# 根据  document 查询
result = collection.get(
    where_document={"$contains":"Python"},
    include=["documents"]
)
print(result)
print("*-"*10)

# 相似向量检索
result = collection.query(
    query_texts=["什么是向量数据库？"],
    n_results=2,    # 返回数据多少条
    include=["documents","metadatas","distances"]
)
print(result)