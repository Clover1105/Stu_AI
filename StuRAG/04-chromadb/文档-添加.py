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

# 文档
documents = [
    "Python 是一种解释型编程语言。",
    "ChromaDB 是一个轻量级向量数据库。",
    "RAG 可以结合检索结果增强大模型回答能力。"
]

# 元数据
# metadatas=[{"hobby": "like_fruit"} for _ in range(len(docs))]
metadatas = [
    {"chapter": 1, "topic": "Python"},
    {"chapter": 4, "topic": "VectorDB"},
    {"chapter": 7, "topic": "RAG"}
]

# 唯一 id
# ids=[f"doc{str(i)}" for i in range(len(docs))]
ids = ["doc_001", "doc_002", "doc_003"]

# 添加文档
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("文档添加成功")
print("当前文档数量：", collection.count())