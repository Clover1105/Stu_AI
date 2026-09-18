import json
import os

import redis
from dotenv import load_dotenv

load_dotenv()

"""短期记忆 -- 窗口记忆"""

class WindowMemory:
    def __init__(self,session_id):
        self.redis = redis.StrictRedis(host="localhost",port=6379,password="123456",db=0)
        self.window_size = int(os.getenv("WINDOW_MEMORY_ROUND"))
        self.session_id = session_id
        self.key = f"window_memory:{self.session_id}"
        self.window_expire_time = int(os.getenv("WINDOW_MEMORY_EXPIRE_TIME"))

    # 保存记忆
    def save_memory(self,role:str,content:str):
        # 构建字典
        data = {"role":role,"content":content}
        # 添加到列表中
        self.redis.rpush(self.key,json.dumps(data,ensure_ascii=False))
        # 设置保留的窗口记忆
        self.redis.ltrim(self.key,-self.window_size,-1)
        # 设置过期时间
        self.redis.expire(self.key,self.window_expire_time)

    # 提取记忆
    def query(self):
        # 判断键是否存在
        if self.redis.exists(self.key):
            # 反序列化
            data = self.redis.lrange(self.key,0,-1)
            return [json.loads(d) for d in data]

if __name__ == '__main__':
    w = WindowMemory(11)
    # 模拟人类消息添加
    w.save_memory("user", "你好")
    # 模拟AI回复消息
    w.save_memory("ai", "你好，我是AI助手")
    # 模拟人类消息添加
    w.save_memory("user", "你好1")
    # 模拟AI回复消息
    w.save_memory("ai", "你好1，我是AI助手1")
    # 模拟人类消息添加
    w.save_memory("user", "你好2")
    # 模拟AI回复消息
    w.save_memory("ai", "你好2，我是AI助手2")
    # 模拟人类消息添加
    w.save_memory("user", "你好3")
    # 模拟AI回复消息
    w.save_memory("ai", "你好3，我是AI助手2")
    # 查询记忆
    rs = w.query()
    print(rs)
