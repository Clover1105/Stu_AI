# 一、redis数据库

## （一）定义

Redis（Remote Dictionary Server）是一款开源、高性能的基于内存的非关系型（NoSQL）键值（Key-Value）数据库。

它由 Salvatore Sanfilippo 于 2009 年创建，主要用于缓存、消息队列、分布式锁以及实时数据分析等场景。

## （二）**核心特性**

**极致的读写性能**：

Redis 将数据优先驻留在内存中，避免了传统数据库的磁盘 I/O 瓶颈，读写速度可达微秒级，单机 QPS（每秒查询率）可突破 10 万。

**丰富的数据结构**：

除了简单的键值对，Redis 还支持多种复杂的数据结构，能够直接处理各种业务模型，无需在应用层进行复杂的序列化或转换。

**灵活的持久化机制**：

虽然是内存数据库，Redis 提供了 RDB（快照）和 AOF（日志追加）两种持久化方式，能够异步将内存数据写入磁盘，兼顾了高性能与数据安全性。

**高可用与分布式架构**：

支持主从复制实现读写分离；通过哨兵模式（Sentinel）实现自动故障转移；通过集群模式（Cluster）实现数据的自动分片与水平扩展，满足大规模并发需求。

## （三）核心数据结构

Redis 支持多种数据类型，底层会根据数据规模自动适配最优的编码方式（如 SDS、ziplist、skiplist 等）：

- **String（字符串）**：最基础的类型，可存储文本、整数或浮点数。常用于缓存、计数器和分布式锁。
- **Hash（哈希）**：键值对的嵌套结构，非常适合存储对象（如用户信息），支持对单个字段的独立读写。
- **List（列表）**：有序的字符串列表，支持从两端推入或弹出数据，常用于实现消息队列和最新列表展示。
- **Set（集合）**：无序且唯一的字符串集合，支持交集、并集、差集等数学集合运算，适用于去重和标签系统。
- **ZSet（有序集合）**：在集合的基础上为每个元素关联了一个分数（Score），元素按分数排序，是实现实时排行榜的最佳选择。
- **扩展类型**：还包括 Bitmap（位图）、HyperLogLog（基数统计）、Geospatial（地理位置）、Stream（消息队列）以及 JSON、Vector Set 等。

## （四）底层工作原理

**单线程模型与 IO 多路复用**：

Redis 的核心命令执行采用单线程模型，这完美避免了多线程环境下的上下文切换和锁竞争问题。

同时，结合 IO 多路复用技术（如 epoll），它能够高效监听并处理大量客户端连接，实现极高的并发能力。

- *注：Redis 6.0 及以上版本引入了多线程，但仅用于网络 IO 层面的读写处理，核心的数据命令执行依然保持单线程。*

**内存管理**：

Redis 默认使用 jemalloc 内存分配器，并提供了多种内存淘汰策略（如 LRU、LFU），当内存达到上限时，会自动清理过期键或冷数据以释放空间。

## （五）典型应用场景

**热点数据缓存**：

将高频访问的数据（如首页商品、文章详情）存入 Redis，极大减轻后端关系型数据库（如 MySQL）的压力，提升系统响应速度。

**会话缓存（Session Cache）**：

在分布式系统中集中管理用户的登录状态和会话信息，实现无状态服务架构。

**排行榜与计数器**：

利用 ZSet 的排序特性和 String 的原子递增操作，轻松实现游戏积分排行、视频点赞数、秒杀库存扣减等功能。

**轻量级消息队列**：

利用 List 或 Stream 结构实现异步任务处理和模块间的解耦，平滑流量峰值。

**分布式锁**：

利用 `SETNX` 等原子操作，在分布式环境中实现对共享资源的互斥访问。

# 二、相关操作

## （一）基础操作

安装：

```
pip install redis==4.5.5
```

连接：

```
# 导入相关库
import redis

# 连接本地 Redis（默认端口 6379）
r = redis.StrictRedis(host='localhost', port=6379, password="123456", db=0)

# 测试连接
print(r.ping())  # 返回 True 表示连接成功
```

## （二）字符串

字符串存取值 -- 存：`set/setex`；取：`get`

```python
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
```

自增 -- `incr()`

```python
def test_incr():
    client.incr("count")
    if client.get("count"):
        num = client.get("count").decode()
        print(f"num = {num}")
```

自减 -- `decr()`

```python
def test_decr():
    client.("count")
    if client.get("count"):
        num = client.get("count").decode()
        print(f"num = {num}")
```

取值后为字节类型，转为字符串 -- `decode()`

设置过期时间 -- 第一种：`set("name", "sang",ex=60)`，第二种：`setex("age",60, "20")`

## （三）哈希

存值 -- `hset()`

```python
def test_hash_hset():
    client.hset("user:1", "name", "李四")
    client.hset("user:1", "email", "1111@qq.com")
    client.hset("user:1", "department", "部门")
    client.hset("user:1", "num", "10")
    print("数据保存成功")
```

设置失效时间 -- `expire()`

```
client.expire("user:1", 20)
```

取值 -- `hgetall()/hget()`

```python
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
```

## （四）列表

插入，存值 -- `lpush()/rlpush()`

```python
def test_list_push():
    # 左边添加
    left_data= client.lpush("user:1","1","2","3")
    # 右边添加
    right_data = client.rpush("user:1", "a", "b", "c")
    # 查询所有元素
    data = client.lrange("user:1",0,-1)
    print(data)
    print("保存成功")
```

弹出，删除 -- `lpop()/rpop()`

```python
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
```

截取 -- `ltrim()`

```python
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
```

## （五）序列化和反序列化

Redis 是一个 **键值数据库**，底层只认识 **字节数据（bytes）**，当我们往 Redis 存入复杂的 Python 对象（如字典、列表、自定义类）时，就必须把它 **序列化为字符串或二进制** 才能存进去。

简单说：

- **序列化（serialize）**：把 Python 对象 → 转成可存入 Redis 的字节或字符串

```python
def test01():
    data ={"name":'张三',"age":123}
    #序列化，把python对象转换成json字符串,ensure_ascii=False 保留原始值
    data = json.dumps(data,ensure_ascii=False)
    client.set("user:2",data)
    print("保存成功")
```

- **反序列化（deserialize）**：从 Redis 拿出来的字节 → 转回 Python 对象

```python
def test02():
    data = client.get("user:2")
    #反序列化:把json字符串转成成python对象
    data = json.loads(data)
    print(data)
```

