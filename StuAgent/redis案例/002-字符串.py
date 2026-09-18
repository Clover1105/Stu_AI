import redis

# 连接 redis 数据库
client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password="123456",
    db=0
)

# 字符串存取值
def test_str():
    # 初始化自增变量
    client.set("count",0)

    # 判断连接是否成功
    if client.ping():
        # set 存值
        client.set("name","clover")
        client.set("age","18")
        client.set("sex","女")
        print("数据保存成功")
        # 设置过期时间，两种方式
        client.set("name", "sang",ex=60)
        client.setex("age",60, "20")
        client.set("sex", "女")
        print("数据覆盖成功")

        # get 取值
        if client.get("name"):
            name = client.get("name").decode()
            age = client.get("age").decode()
            sex = client.get("sex").decode()
            print(f"name:{name},age:{age},sex:{sex}")
        else:
            print("该键名（数据）不存在！！！")
    else:
        print("redis服务没有启动！！！")

# 自增
def test_incr():
    client.incr("count")
    if client.get("count"):
        num = client.get("count").decode()
        print(f"num = {num}")

# 自减
def test_decr():
    client.decr("count")
    if client.get("count"):
        num = client.get("count").decode()
        print(f"num = {num}")

if __name__ == '__main__':
    # test_str()
    # test_incr()
    test_decr()