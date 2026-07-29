import chromadb
from chromadb.utils import embedding_functions

# 本地模型
embedding = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=r"thenlper/gte-small-zh",
)

client = chromadb.PersistentClient(path="../chroma_data")

collection = client.get_or_create_collection(
    name="cs01",
    embedding_function=embedding
)

# 获取全部数据
result = collection.get()

# 删除所有文档
collection.delete(
    ids=result["ids"]
)

print("删除成功")
print("当前文档数量：", collection.count())