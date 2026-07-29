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

# 查看当前数据
print("删除前：")
print(collection.get(include=["documents", "metadatas"]))

# 根据 id 删除
collection.delete(
    ids=["doc_001"]
)

print("删除 doc_001 后：")
print(collection.get(include=["documents", "metadatas"]))

# 根据元数据删除
collection.delete(
    where={
        "topic":"RAG"
    }
)

print("删除 topic=RAG 后：")
print(collection.get(include=["documents", "metadatas"]))