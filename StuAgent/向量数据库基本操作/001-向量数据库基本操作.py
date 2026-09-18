import chromadb
import os
import uuid
from dotenv import load_dotenv

load_dotenv()


# 数据库路径
path = os.getenv("CHROMA_PATH")

# 连接数据库
client = chromadb.PersistentClient(path)
print("连接数据库成功")

# 创建集合
def create_collection():
    # 创建并获取集合
    collection = client.get_or_create_collection("test01")
    print(f"创建集合 test01 成功")

# 保存数据
def save_data(query,user_id):
    collection = client.get_or_create_collection("test01")
    # 保持id唯一性
    # id = f"memory_{int(time.time())}"
    id = f"memory_{user_id}_{uuid.uuid4()}"
    # 添加数据
    collection.add(
        ids=[id],
        documents=[query],
        metadatas=[
            {"user_id":user_id}
        ]
    )
    print("保存数据成功")

# 查询数据
def query_data(question,user_id):
    collection = client.get_or_create_collection("test01")
    # 查询数据库
    rs = collection.query(
        query_texts=[question],
        n_results=3,
        where={"user_id":user_id}
    )
    print("查询数据成功，如下：")
    for data in rs:
        print(f"查询到的数据：{data}")
    dis = rs["distances"][0]
    doc = rs["documents"][0]
    print(f"相似度：{dis}")
    print(f"文档：{doc}")

# 集合大小
def get_size():
    collection = client.get_or_create_collection("test01")
    print(f"集合大小：{collection.count()}")

# 删除数据
def delete_data():
    collection = client.get_or_create_collection("test01")
    # 条件删除
    collection.delete(where={'user_id':1})
    print("删除数据成功")
    get_size()

# 主函数
if __name__ == '__main__':
    # create_collection()
    # save_data("今天天气好",1)
    # save_data("推开窗门",1)
    # save_data("迎接晨曦到",1)
    # save_data("我喜欢唱歌", 1)
    query_data("今天天气如何，我喜欢什么？",1)
    # delete_data()