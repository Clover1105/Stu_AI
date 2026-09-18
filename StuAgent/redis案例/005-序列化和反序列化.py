import redis
import json

# 连接 redis 数据库
client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password="123456",
    db=0
)

#序列化
def test01():
    data ={"name":'张三',"age":123}
    #序列化，把python对象转换成json字符串,ensure_ascii=False 保留原始值
    data = json.dumps(data,ensure_ascii=False)
    client.set("user:2",data)
    print("保存成功")

#反序列化
def test02():
    data = client.get("user:2")
    #反序列化:把json字符串转成成python对象
    data = json.loads(data)
    print(data)

if __name__ =="__main__":
    test01()
    test02()