# 下载模型
# from huggingface_hub import snapshot_download
#
# snapshot_download(
#     repo_id="thenlper/gte-small-zh",
#     local_dir=r"G:\models\gte-small-zh"
# )

# 导入 ChromaDB 包
import chromadb
# 导入 embedding_functions 模块
from chromadb.utils import embedding_functions

# 创建客户端对象，连接本地数据库
client = chromadb.PersistentClient(path="../chromadb_data")

# 创建向量化模型
mod = embedding_functions.SentenceTransformerEmbeddingFunction(
    # 模型名称
    model_name="thenlper/gte-small-zh",
    # 运行设备
    device="cuda",
    # 设置缓存路径，已下载
    cache_folder=r"G:\models\gte-small-zh"
)

# 设置集合名称
col_name = "cs01"
# 创建集合
result = client.create_collection(
    # 集合名称
    name=col_name,
    # 指定集合使用的向量化模型
    embedding_function=mod
)
print(result)
print(type(result))
# Collection(name=cs01)
# <class 'chromadb.api.models.Collection.Collection'>