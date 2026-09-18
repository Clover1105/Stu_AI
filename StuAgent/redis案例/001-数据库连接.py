import redis

client = redis.StrictRedis(
    host="localhost",
    port=6379,
    password="123456",
    db=0
)

if __name__ == '__main__':
    if client.ping():
        client.setex("name",60,"123456")
        print("redis连接成功")