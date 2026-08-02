from common import RedisUtil

r = RedisUtil.get_redis_conn()
r.setex("key",60,"value")
data = r.get("key")
print(data) # 直接取，类型为字节
# 转码
data1 = str(data, encoding="utf-8")
print(data1)    # 转码后，类型为字符串
data2 = data.decode("utf-8")
print(data2)    # 转码后，类型为字符串
