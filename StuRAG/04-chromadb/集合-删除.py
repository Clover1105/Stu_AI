import chromadb

# 获取连接对象
client = chromadb.PersistentClient(path="../chromadb_data")
# 集合名称
collection_name = "cs01"
# 获取集合对象
try:
    client.delete_collection(name = collection_name)
    print("删除成功")
except Exception as e:
    print(f"删除失败：{e}")