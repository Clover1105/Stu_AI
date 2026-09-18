import chromadb
import os
import uuid
from dotenv import load_dotenv


"""长期记忆存储"""

class LongMemory:
    def __init__(self):
        load_dotenv()
        # 数据库路径
        path = os.getenv("CHROMA_PATH")
        # 连接数据库
        client = chromadb.PersistentClient(path)
        # 创建集合
        self.collection = client.get_or_create_collection("long_memory")

    # 添加，保存记忆
    def save_long(self,user_id,query):
        # 保持id唯一性
        id = f"memory_{user_id}_{uuid.uuid4()}"
        # 添加数据
        self.collection.add(
            ids=[id],
            documents=[query],
            metadatas=[
                {"user_id": user_id}
            ]
        )
        print("保存数据成功")

    # 查询数据
    def query_long(self, user_id, question):
        rs = self.collection.query(
            query_texts=[question],
            n_results=3,
            where={"user_id": user_id}
        )
        doc = rs["documents"][0]
        print(f"查询出来的文档：\n{doc}")
        return doc










if __name__ == '__main__':
    memory = LongMemory()
    rs = memory.query_long("1","什么是roy最爱的？")
    print(rs)