# 启动服务器
# chroma run --path ./chromadb_data/test01 --host 0.0.0.0 --port 9000

# 导入 ChromaDB 向量数据库
import chromadb

# 创建 ChromaDB HTTP 客户端（用于连接 Chroma Server）
client = chromadb.HttpClient(
    host="localhost",   # 主机地址，localhost 等价于 127.0.0.1，表示连接本机服务器
    port=9000   # 监听的端口号，需要与启动服务器时指定的端口保持一致
)

# 打印客户端对象
print(client)   # <chromadb.api.client.Client object at 0x0000025393430110>