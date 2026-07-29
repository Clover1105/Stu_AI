import chromadb

# 创建客户端对象
client = chromadb.PersistentClient(
    path="../chromadb_data"
)

# 查找集合
list = client.list_collections()

# 打印集合名称
print(list)

# 判断集合是否存在
try:
    exist = client.get_collection(name="test01")
    print("集合存在")
except Exception as e:
    print("集合不存在")