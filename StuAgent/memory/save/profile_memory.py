import redis

"""用户画像记忆存储"""

class ProfileMemory:
    def __init__(self,user_id):
        self.redis = redis.StrictRedis(host="localhost", port=6379, password="123456", db=0)
        self.key = f"profile_memory:{user_id}"

    # 保存
    def save_profile(self,hashkey,value):
        self.redis.hset(self.key,hashkey,value)

    # 查询
    def query_profile(self):
        # 查询某个用户的用户画像
        rs = self.redis.hgetall(self.key)
        data = ""
        if rs:
            for hashkey ,value in rs.items():
                data += f"{hashkey.decode()}:{self.redis.hget(self.key,hashkey).decode()}"


if __name__ == '__main__':
    p = ProfileMemory(1)
    p.save_profile("name","Roy")
    p.save_profile("age","18")
    # 查询
    p.query_profile()