import redis

# 连接 redis 数据库
client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password="123456",
    db=0
)

# 插入，存值
def test_list_push():
    # 左边添加
    left_data= client.lpush("user:1","1","2","3")
    # 右边添加
    right_data = client.rpush("user:1", "a", "b", "c")
    # 查询所有元素
    data = client.lrange("user:1",0,-1)
    print(data)
    print("保存成功")

# 左弹出并删除
def test_list_pop():
    # 左边弹出
    left_data = client.lpop("user:1")
    print(f"左弹出：{left_data}")
    # 右边弹出
    right_data = client.rpop("user:1")
    print(f"右弹出：{right_data}")
    # 查询所有元素
    data = client.lrange("user:1", 0, -1)
    print(data)
    print("删除成功")

# 截取
def test_list_trim():
    # 查询所有元素
    data = client.lrange("user:1", 0, -1)
    print(data)
    # 截取
    ltrim_data = client.ltrim("user:1", 4, -2)
    print(f"截取成功：{ltrim_data}")
    if ltrim_data:
        # 查询所有元素
        data = client.lrange("user:1", 0, -1)
        print(data)


if __name__ == '__main__':
    test_list_push()
    test_list_pop()
    test_list_trim()