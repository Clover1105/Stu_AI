import redis

# 连接 redis 数据库
client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password="123456",
    db=0
)


# 存值
def test_hash_hset():
    client.hset("user:1", "name", "李四")
    client.hset("user:1", "email", "1111@qq.com")
    client.hset("user:1", "department", "部门")
    client.hset("user:1", "num", "10")
    print("数据保存成功")

    # 设置失效时间
    client.expire("user:1", 20)
    print("设置失效时间成功，20秒后自动删除")

# 取值
def test_hash_hget():
    value = client.hgetall("user:1")
    print(value)
    if value:
        name = client.hget("user:1", "name").decode()
        email = client.hget("user:1", "email").decode()
        department = client.hget("user:1", "department").decode()
        num = client.hget("user:1", "num").decode()
        print(f"name:{name},email:{email},department:{department},num:{num}")
    else:
        print("该键名（数据）不存在！！！")

if __name__ == '__main__':
    test_hash_hset()
    test_hash_hget()
