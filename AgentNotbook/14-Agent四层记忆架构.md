# 一、四层记忆架构

## （一）介绍

### 1. 本质

没有记忆的 Agent 只是一次性问答机器人；拥有四层记忆的 Agent 才具备长期交互和企业应用能力

四层记忆本质解决四个问题：

| 问题           | 解决方案       |
| -------------- | -------------- |
| 刚才说了什么？ | Window Memory  |
| 以前聊过什么？ | Summary Memory |
| 长期喜欢什么？ | Long Memory    |
| 用户是谁？     | Profile Memory |

### 2. 记忆架构四层设计

```
                          用户输入
                             │
                             ▼
                    ConversationManager
                             │
      ┌──────────────┼────────────────┼────────────────┐
      ▼              ▼                ▼                ▼
 WindowMemory   SummaryMemory   LongTermMemory ，Profile Memory
      │              │                │                │
      └──────────────┼────────────────┼────────────────┘
                             ▼
                       PromptBuilder
                             │
                             ▼
                       create_agent()
                             │
                             ▼
                            LLM
                             │
                             ▼
                        AI Response
                             │
                             ▼
                  ConversationManager.save()
```

### 3. 和Checkpointer 的区别

**四层记忆架构（Memory Architecture）**：保存 Agent 需要理解的用户信息（Memory）

**LangGraph/LangChain 1.0 Checkpointer**：保存 Agent 的运行状态（State）

- **`memory = InMemorySaver()`**：创建 Checkpointer 实例（地基），它决定了记忆存放在哪里（这里选择了内存）
- **`config = {'configurable': {'thread_id': user_id}}`**：为 Checkpointer 分配存储键（门牌号），它决定了记忆存放在哪个具体的“房间”（会话）里

## （二）架构总览

AI Agent 实现了四层记忆架构，将记忆能力拆分为**记忆存储**与**记忆提取**两大子系统，分别负责数据的持久化管理和智能化处理。

```
┌──────────────────────────────────────────────────────────────────┐
│                       ConversationManager                        │
│                     (对话管理器 · 全局入口)                         │
│                                                                  │
│   save_user() → save_ai() → build_prompt() → MemoryManager      │
└──────────────┬────────────────────────────────────┬──────────────┘
               │                                    │
    ┌──────────▼──────────┐              ┌──────────▼──────────┐
    │   第一部分：记忆存储   │              │  第二部分：记忆提取   │
    │   (memory_save/)     │              │ (memory_retrieval/) │
    │                      │              │                     │
    │  WindowMemory    L1  │              │  SummaryAgent   L2  │
    │  SummaryMemory   L2  │              │  LongMemoryAgent L3 │
    │  LongMemory      L3  │              │  ProfileAgent   L4  │
    │  ProfileMemory   L4  │              │  MemoryManager      │
    │  PromptBuilder       │              │   (更新调度器)        │
    └──────────────────────┘              └─────────────────────┘
```

## （三）四层记忆对照表

| 层级 | 名称     | 存储介质   | 生命周期      | 存储层类      | 提取层类        |
| ---- | -------- | ---------- | ------------- | ------------- | --------------- |
| L1   | 窗口记忆 | Redis List | 1小时自动过期 | WindowMemory  | — (直接读写)    |
| L2   | 摘要记忆 | PostgreSQL | 永久存储      | SummaryMemory | SummaryAgent    |
| L3   | 长期记忆 | 向量数据库 | 永久(可清理)  | LongMemory    | LongMemoryAgent |
| L4   | 用户画像 | Redis Hash | 永久存储      | ProfileMemory | ProfileAgent    |

## （四）完整对话生命周期

```
               用户发送消息
                   │
                   ▼
┌────────────────────────────────────────────┐
│ 1. save_user()                             │
│    ConversationManager 将用户消息写入 L1    │
│    └─► WindowMemory.add("user", question)  │
└──────────────────┬─────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────┐
│ 2. build_prompt()                          │
│    PromptBuilder 组装四层记忆为 Prompt      │
│    ┌─ L2 摘要记忆                           │
│    ├─ L3 长期记忆 (Top 5)                   │
│    ├─ L4 用户画像                           │
│    └─ L1 窗口记忆 + 当前问题                 │
└──────────────────┬─────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────┐
│ 3. LLM 推理生成回复                         │
└──────────────────┬─────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────┐
│ 4. save_ai()                               │
│    ConversationManager 将回复写入 L1        │
│    └─► WindowMemory.add("assistant", resp) │
└──────────────────┬─────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────┐
│ 5. MemoryManager.update()                  │
│    记忆提取层调度更新                         │
│    ┌─ L4: ProfileAgent  → 提取用户属性      │
│    ├─ L3: LongMemoryAgent → 提取长期记忆    │
│    └─ L2: SummaryAgent → 条件触发摘要生成   │
└────────────────────────────────────────────┘
```

# 二、代码流程

## （一）准备工作

### 1. 会话管理器

主要负责四层记忆的对象创建和提示词的生成

> - **初始化会话管理对象**：在创建 `SessionManager` 实例时，同步完成以下核心组件的装配
>     - 接收全局唯一的 `session_id` 作为当前会话的标识符
>     - 实例化 `WindowMemory` 对象，完成底层 Redis 连接与短期记忆滑动窗口的配置
>     - 实例化 `BuilderPrompt` 对象，将 `session_id` 传入，为后续的提示词组装与格式化做好准备
> - **保存记忆流程**（Save Memory）：调用保存方法时，执行以下委托操作
>     - 接收外部传入的角色（`role`）与内容（`content`）参数
>     - 将数据写入操作无缝委托给底层的 `WindowMemory` 实例，由其完成序列化、入队、窗口裁剪及过期时间重置等原子化操作
>     - 屏蔽底层存储细节，对外提供统一的写入接口
> - **构建提示词流程**（Builder Prompt）：调用构建方法时，执行以下组装与格式化操作
>     - 调用 `BuilderPrompt` 的构建方法，由其内部自动查询并提取完整的短期对话上下文
>     - 将提取出的历史消息按照预设模板进行拼接与格式化，生成包含完整上下文的纯文本提示词
>     - 将组装好的提示词封装为标准的 OpenAI 消息字典格式（`{"role":"system", "content":...}`），以便直接注入大模型的请求链路中
> - **引入会话管理器**：核心意义在于**架构解耦**与**统一控制**
>     - **统一入口（门面模式）**：对外提供唯一接口，调用方无需关心内部有多少种记忆模块，直接调用即可
>     - **扩展多记忆融合**：未来增加长期记忆、摘要记忆时，由它负责统筹拼接，而不是让外部业务代码去处理复杂的记忆合并逻辑
>     - **解耦与标准化**：隔离底层存储（如 Redis）与业务逻辑，同时统一输出标准格式（如直接返回 `{"role":"system", ...}`），简化主流程调用

```python
from memory.save.window_memory import WindowMemory
from memory.manager.builder_prompt import BuilderPrompt
from memory.save.summary_memory import SummaryMemory
from memory.save.long_memory import LongMemory
from memory.save.profile_memory import ProfileMemory

class SessionManager:
    def __init__(self,session_id:str,user_id):
        self.window_memory = WindowMemory(session_id)
        self.session_id = session_id
        self.b_p = BuilderPrompt(self.session_id,user_id)
        self.summary_memory = SummaryMemory(self.session_id)
        self.long_memory = LongMemory()
        self.profile_memory = ProfileMemory(user_id)

    # 添加窗口记忆
    def save_window_memory(self,role:str,content:str):
        self.window_memory.save_memory(role,content)

    # 构建提示词
    def builder_prompt(self,user_id,question):
        prompt = self.b_p.builder_prompt(user_id,question)
        return {"role":"system","content":prompt}

```

### 2. 记忆管理器

管理记忆的更新

```python
from memory.retrieval.SummaryAgent import SummaryAgent
from memory.manager.session_manager import SessionManager
from memory.retrieval.LongAgent import LongAgent
from memory.retrieval.ProfileAgent import ProfileAgent

class MemoryManager:
    def __init__(self,sessionManager:SessionManager):
        # 摘要智能体
        self.summary_agent = SummaryAgent(sessionManager.summary_memory)
        # 获取窗口记忆对象
        self.window_memory = sessionManager.window_memory
        # 创建长期记忆智能体
        self.long_agent = LongAgent(sessionManager.long_memory)
        # 创建用户画像智能体
        self.profile_agent = ProfileAgent(sessionManager.profile_memory)

    def update(self,user_id,question):
        # 查询，获取窗口记忆
        query_window = self.window_memory.query()
        # 更新长期记忆
        self.long_agent.update(user_id,question)
        # 更新用户画像记忆
        self.profile_agent.update(question)
        # 触发摘要
        if len(self.window_memory.query()) >= 2:
            # 更新摘要记忆
            self.summary_agent.update(query_window)
```

### 3. 连接池

数据库连接池是一种用于管理和维护数据库连接的技术。简单来说，它就像一个“连接缓存池”，在应用程序启动时预先创建一定数量的数据库连接，并集中管理、循环复用，从而避免频繁创建和销毁连接带来的性能开销

#### （1）核心功能

**提高性能与响应速度（连接复用）**
建立数据库连接是一个耗时的操作（涉及TCP握手、身份验证等）。如果没有连接池，每次请求都新建和销毁连接，会浪费大量时间。连接池允许应用程序在用完连接后将其“归还”而不是关闭，下次请求直接复用现有连接，极大地减少了系统开销，提升了响应速度。

**控制并发与保护数据库（资源限制）**
数据库服务器的连接资源是有限的。代码中的 `max_size=20` 参数限制了连接池最多只能创建20个连接。这可以防止在高并发场景下，应用程序瞬间发起大量请求从而压垮数据库（如引发 `Too many connections` 错误）。

**保证基础可用性（最小空闲连接）**
代码中的 `min_size=10` 参数确保连接池中始终至少保持10个空闲连接。这样在系统低峰期或冷启动时，请求可以直接获取到连接，无需等待新建，保证了业务的基础响应能力。

**统一管理与健康检查**
连接池会自动管理连接的生命周期，包括定期检测连接的有效性、自动回收长时间未使用的空闲连接，以及处理异常断开的连接，从而避免连接泄漏，提高系统的稳定性和可靠性。

#### （2）配置连接池

配置连接池就是为了**“降本增效”**——既提高了应用程序的并发处理能力和性能，又保护了底层数据库不被过载，是现代应用开发中必不可少的标准组件

```python
from psycopg_pool import ConnectionPool

# 配置连接池
pool = ConnectionPool(
    conninfo="host=127.0.0.1 port=5432 dbname=postgres user=postgres password=123456",
    max_size=20,    # 最大连接数，生成环境是20个
    min_size=10,     # 最小连接数，生成环境是10个
)
```

## （二）更新记忆（写入）

### 1. 创建管理器（会话、记忆）

创建会话管理器

```python
session_manager = SessionManager("001",1)
```

创建一个窗口记忆

```python
session_manager.save_window_memory("user", que)
```

初始化记忆管理器

```python
memory_manager = MemoryManager(session_manager)
```

更新记忆

```
memory_manager.update(1, que)
```

### 2. 窗口记忆

**记忆管理器**获取了**会话管理器**中的**窗口记忆对象**

直接调用窗口记忆对象的 `query` 方法，获取当前的短期对话内容

> - **初始化窗口记忆对象**：在创建窗口记忆实例时，同步完成以下核心配置
>     - 初始化并连接至 Redis 数据库
>     - 从环境变量中读取并设置滑动窗口大小（`window_size`，即保留的对话轮数）以及会话的唯一标识符（`session_id`）
>     - 基于 `session_id` 生成专属的 Redis Key（如 `window_memory:{session_id}`）
>     - 设定窗口记忆的过期时间（`expire_time`），确保短期记忆不会无限期驻留
> - **保存记忆流程**（Save Memory）：调用保存方法时，执行以下原子化操作
>     - 将当前的角色（`role`）与内容（`content`）封装为字典，序列化为 JSON 字符串后，追加至 Redis 列表的尾部（使用 `RPUSH`）
>     - 立即执行列表裁剪操作（使用 `LTRIM`），仅保留列表末尾指定数量（`window_size`）的元素，自动剔除超出窗口的历史旧消息
>     - 每次写入新记忆后，重置该 Key 的 TTL（生存时间），保证短期记忆在会话活跃期内有效，会话结束后自动清理
> - **选择 Redis List 数据结构**：
>     - 因为其原生的 `RPUSH` 与 `LTRIM` 组合能够以极高的效率实现固定长度的滑动窗口，在保障对话时序的同时自动清理超限的旧记忆
> - **提取记忆流程**（Query Memory）：调用提取方法时，执行以下安全读取操作
>     - 首先检查目标 Key 是否存在，避免对空键进行无效查询
>     - 若 Key 存在，则按顺序获取列表中的所有元素（使用 `LRANGE 0 -1`），还原完整的短期对话上下文
>     - 将获取到的 JSON 字符串列表批量反序列化为字典格式，以便后续直接注入大模型的 Prompt 中

```python
# 文件 -- 窗口记忆

import json
import os
import redis
from dotenv import load_dotenv

load_dotenv()

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
```

### 3. 长期记忆

**记忆管理器**创建了**长期记忆智能体**实例，并将**会话管理器**中创建的**长期记忆实例**作为参数传入

**更新长期记忆**

- 触发**长期记忆智能体**的 `update` 方法。
- 智能体调用大模型对问题进行语义分析和关键信息提取。

```python
# 文件 -- 长期记忆智能体

from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.long_memory import LongMemory

class LongAgent:
    def __init__(self,long_memory:LongMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取长期记忆的保存对象
        self.long_memory = long_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个长期记忆助手
         -- 任务：
            - 根据用户问题提取相关的长期记忆信息
         -- 规则：
            - 如果用户输入是陈述句（例如：“我叫张三”，“我喜欢Python”），请从中提取关键事实（如姓名、爱好、技能等），并以简洁的第三人称形式输出，用于更新记忆。
            - 如果用户输入是疑问句（例如：“我叫什么？”，“我擅长什么？”），请直接输出“NO_UPDATE”，表示无需更新记忆。
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,user_id,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        self.long_memory.save_long(user_id,result['messages'][-1].content)
        print("长期记忆更新成功")
```

- 触发**长期记忆实例**的保存方法，将大模型提取出的结构化事实存入向量数据库（ChromaDB）中

```python
# 文件 -- 长期记忆

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
```

### 4. 用户画像记忆

**记忆管理器**创建了**用户画像智能体**实例，并将**会话管理器**中创建的**用户画像记忆实例**作为参数传入

**更新用户画像记忆**

- 触发**用户画像智能体**的 `update` 方法。
- 智能体调用大模型从问题中提取用户的个人信息（如姓名、职业、爱好等）。

```python
# 文件 -- 用户画像记忆智能体

from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.profile_memory import ProfileMemory
from pydantic import BaseModel,Field

class ProfileParams(BaseModel):
    name:str = Field(description="姓名")
    age:int = Field(description="年龄")
    job:str = Field(description="职业")
    address:str = Field(description="地址")
    hobby:str = Field(description="爱好")
    xueli:str = Field(description="学历")

class ProfileAgent:
    def __init__(self,profile_memory:ProfileMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.profile_memory = profile_memory

    def get_prompt(self):
        self.prompt = """
        -- 角色：你是一个用户画像提取助手
        -- 任务：
            - 根据用户问题提取相关用户画像信息
        -- 规则：
            - 用户画像信息包含以下信息：姓名，年龄，爱好，职业，地址，学历
            - 去掉闲聊内容
            - 避免重复
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
            - 如果没有用户画像信息，返回空
        -- 输出：
            - 只输出姓名，年龄，职业，地址，学历
        -- 示例：
            用户输入：我喜欢打游戏
            输出:{'name': '', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
             
            用户输入：我是张三
            输出:{'name': '张三', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[],
            response_format=ProfileParams
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        data = result['structured_response'].model_dump()
        for key,value in data.items():
            if value:
                print("有用户画像")
                print(f"{key}:{value}")
                self.profile_memory.save_profile(key,value)
        return data
```

- 触发**用户画像记忆实例**的 `save_profile` 方法，将提取到的键值对以 Hash 格式存入 Redis 中。

```py
# 文件 -- 用户画像记忆

import redis

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
```

### 5. 摘要记忆

**记忆管理器**创建了**摘要记忆智能体**实例，并将**会话管理器**中创建的**摘要记忆实例**作为参数传入。

**触发摘要记忆更新**

- **判断条件：** 检查窗口记忆的内容数量是否达到阈值（代码中设定为 `>= 2`）。
- 若达到上限：
    - 触发**摘要记忆智能体**的 `update` 方法，并将查询到的窗口记忆内容作为参数传入。
    - 智能体内部先调用摘要记忆实例的查询方法，获取旧的摘要内容。
    - 将旧摘要与窗口记忆中的用户问题进行拼接，组成包含上下文的新 Prompt。
    - 调用大模型对新 Prompt 进行回复，生成更新后的摘要。

```python
# 文件 -- 摘要智能体

from langchain.agents import create_agent
from model.my_model import MyModel
from memory.save.summary_memory import SummaryMemory
from langchain_core.messages import HumanMessage

class SummaryAgent:
    def __init__(self,summary_memory:SummaryMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.summary_memory = summary_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个摘要生成助手
         -- 任务：
            - 根据旧摘要和最新的聊天记录生成新的摘要
         -- 规则：
            - 保留重要信息
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 只返回新的摘要
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=False,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,messages):
        # 查询旧摘要
        old_summary = self.summary_memory.query_summary()
        # 最新聊天记录
        prompt = ""
        for i in messages:
            if i['role'] == 'user':
                prompt += f"用户提问：{i['content']}"
            # else:
            #     prompt += f"AI回复：{i['content']}"
        # 问题
        que = f"请根据旧摘要：{old_summary}和最新聊天记录：{prompt}"
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=que)]})
        # 把新摘要存入到摘要记忆中
        self.summary_memory.save_summary(result['messages'][-1].content)
```

- 若达到上限：
    - 触发**摘要记忆实例**的 `save_summary` 方法，将新摘要存入 PostgreSQL 数据库中（使用 Upsert 逻辑）。

```python
# 文件 -- 摘要记忆

from psycopg_pool import ConnectionPool

# 配置连接池
pool = ConnectionPool(
    conninfo="host=127.0.0.1 port=5432 dbname=postgres user=postgres password=123456",
    max_size=20,    # 最大连接数，生成环境是20个
    min_size=10,     # 最小连接数，生成环境是10个
)

class SummaryMemory:
    def __init__(self,session_id):
        self.session_id = session_id

    # 保存
    def save_summary(self,summary:str):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                sql =f"INSERT INTO conversation_summary(session_id, summary) VALUES('{self.session_id}','{summary}') ON CONFLICT(session_id) DO UPDATE SET summary=EXCLUDED.summary,update_time=NOW()"
                cur.execute(sql)
                # 提交事务
                conn.commit()

    # 查询
    def query_summary(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                sql = f"select summary from conversation_summary where session_id ='{self.session_id}'"
                cur.execute(sql)
                # 查询单个值
                result = cur.fetchone()
                if result:
                    return result[0]
                else:
                    return ""
```

## （三）构建记忆的提示词（读取）

调用会话管理器中的builder_prompt方法

```python
memory_prompt = session_manager.builder_prompt(1, que)
```

会话管理器创建构建提示词实例，将会话id和用户id作为参数传入

触发构建提示词实例的builder_prompt方法

> - **初始化构建提示词对象**：
>     - 创建窗口示例，方便后续提取记忆
> - **构建提示词流程**：
>     - 创建提示词【角色、任务。。。】
>     - 调用实例方法，提取存储的记忆
>     - 将记忆拼接到提示词中（按角色拼接），然后返回拼接好的提示词

### 1. 初始化

```python
# 文件 -- 构建提示词

from memory.save.window_memory import WindowMemory
from memory.save.summary_memory import SummaryMemory
from memory.save.long_memory import LongMemory
from memory.save.profile_memory import ProfileMemory

class BuilderPrompt:
    def __init__(self,session_id,user_id):
        self.window_memory = WindowMemory(session_id)
        self.summary_memory = SummaryMemory(session_id)
        self.long_memory = LongMemory()
        self.profile_memory = ProfileMemory(user_id)

    # 构建提示词
    def builder_prompt(self,user_id,que):
        prompt = """
         -- 角色：你是一个记忆提取助手
         -- 任务：
            - 理解用户需求
            - 根据用户问题，提取相关记忆
        """
```

分别获取四层记忆所存储的内容后，依次拼接到初始提示词上，并返回

### 2. 窗口记忆

```python
# 文件 -- 构建提示词

    window_memory = self.window_memory.query()
    prompt += "短期记忆 -- 窗口记忆"
    for i in window_memory:
        if i['role'] == 'user':
            prompt += f"用户提问：{i['content']}"
        else:
            prompt += f"AI回复：{i['content']}"
```

### 3. 摘要记忆

```python
# 文件 -- 构建提示词

    summary_memory = self.summary_memory.query_summary()
    prompt += "短期记忆 -- 摘要记忆"
    prompt += summary_memory
```

### 4. 长期记忆

```python
# 文件 -- 构建提示词

    long_memory = self.long_memory.query_long(user_id,que)
    prompt += "长期记忆"
    for x in long_memory:
        prompt += x+'\n'
```

### 5. 用户画像记忆

```python
# 文件 -- 构建提示词

    profile_memory = self.profile_memory.query_profile()
    prompt += f"用户画像：{profile_memory}"
    return prompt
```

## （四）创建智能体

### 1. 系统提示词

```python
prompt = f"""
    	-- 角色：你是一个专业的聊天助手
    	-- 任务：
    	    - 理解用户问题，回答用户问题
    	-- 规则：
    	    - 你只需要回答用户问题，回复内容不需要每次携带记忆内容
    	    - 请严格根据以下【用户记忆】来回答用户的问题，如果记忆中有答案，请直接回答：

        【用户记忆】：
        {memory_prompt['content']}
    """
```

### 2. 大模型

```python
model = my_model.MyModel.get_model()
```

### 3. 工具

```python
tools = []
```

### 4. 智能体

```python
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=False,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[]
)
```

## （五）调用智能体

### 1. 传入信息

```python
human_msg = {"messages":[
    HumanMessage(content=que),
    SystemMessage(content=prompt),
]}
```

### 2. 调用

```python
result = agent.invoke(human_msg)    # 非流式输出
data = result["messages"][-1].content
```

## （六）添加窗口记忆

将刚得到的回复存储到窗口记忆中

```python
session_manager.save_window_memory("assistant", data)
```



# ssssssss





## （四）验证

```python
from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

# 创建提示词 -- 系统提示词
prompt = """
	-- 角色：你是一个专业的聊天助手
"""

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[]
)

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("1")
    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)
    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt()

    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que),memory_prompt]}
    # 6. 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content
    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)
    print(data)
    return data


if __name__ == '__main__':
    q1 = "我叫张三，今年23岁"
    q2 = "我喜欢打篮球"
    q3 = "我在学习langchain"
    q4 = "我在学习什么"
    q5 = "我是谁，今年多大了"
    create_email_agent(q3)
```

- **初始化 Agent 运行环境**：在启动智能体交互前，同步完成以下核心组件的装配
    - 初始化大语言模型（LLM）实例，作为智能体的核心推理引擎
    - 准备工具集（Tools）列表，赋予智能体执行外部操作的能力
    - 设定系统级提示词（System Prompt），确立智能体的角色与行为准则
    - 调用 `create_agent` 方法，将模型、工具与提示词进行绑定，生成具备自主推理能力的 Agent 对象
- **会话记忆注入与上下文构建流程**：在处理用户请求时，执行以下记忆与消息组装操作
    - 基于当前会话的唯一标识符（`session_id`）实例化 `SessionManager`，接管当前会话的生命周期
    - 将用户最新的提问（`user` 角色）写入窗口记忆，触发 Redis 的滑动窗口更新与旧数据裁剪
    - 调用会话管理器构建提示词，自动从 Redis 中提取历史对话上下文，并将其封装为标准的 System Message 格式
- **消息协议组装与 Agent 调度流程**：在触发大模型推理前，执行以下标准化协议转换操作
    - 将用户的最新提问封装为 `HumanMessage` 对象，与上一步生成的系统记忆提示词共同组装为标准的 `messages` 列表
    - 将组装好的结构化消息字典传入 Agent 的 `invoke` 方法，触发 ReAct（推理-行动）循环
    - 拦截 Agent 的返回结果，提取消息列表末尾的最终回复内容（`content`），完成单次交互闭环
- **记忆闭环机制**：在获取 Agent 响应后，执行以下状态同步操作
    - 提取大模型返回的最终回复文本，将其作为 `assistant` 角色的内容
    - 再次调用 `SessionManager` 的保存方法，将 AI 的回复追加至 Redis 窗口记忆中
    - 确保“用户提问”与“AI 回复”成对落盘，为下一轮多轮对话提供完整且连贯的上下文支撑

# 三、摘要记忆

## （二）流程

摘要记忆（Summary Memory）的流程可以概括为**“数据存取、上下文注入、异步提炼”**三个核心环节

### 1. 初始化与准备阶段

当用户发起会话时，系统通过 `SessionManager` 统一创建该会话的专属实例，其中包括初始化 `SummaryMemory`（用于连接数据库进行摘要的读写）和 `WindowMemory`（用于在 Redis 中维护短期的滑动窗口消息）。

### 2. 记忆注入与对话生成（读取摘要）

在聊天智能体（Agent）生成回复之前，系统会调用 `BuilderPrompt`。此时，`SummaryMemory.query_summary()` 会从 PostgreSQL 数据库中查询该会话的历史摘要，并将其作为“长期记忆”拼接到系统提示词中。这使得大模型在回答当前问题时，能够“记住”用户的历史背景（例如知道用户叫张三、喜欢打篮球），从而生成连贯的回复。

### 3. 窗口记忆更新（短期记忆）

聊天智能体生成回复后，系统会将用户的提问和 AI 的回复双双存入 `WindowMemory`。Redis 会利用 `ltrim` 机制自动维护一个固定大小的滑动窗口，始终只保留最近 N 轮的对话记录。

### 4. 触发摘要提炼（写入摘要）

在每次对话结束后，`MemoryManager` 会介入进行记忆更新。它会检查 `WindowMemory` 中的消息数量，当消息数达到设定阈值（如 `>= 2` 条）时，触发摘要更新机制。

### 5. 摘要智能体工作流（生成并保存）

触发后，`MemoryManager` 会调用 `SummaryAgent.update()`：

- **读取旧摘要**：再次从数据库获取当前的摘要内容。
- **提取新对话**：从窗口记忆中提取最新的对话记录（当前代码逻辑仅提取了 User 的提问）。
- **大模型提炼**：将“旧摘要”和“新对话”组合成提示词，交给 `SummaryAgent` 中的大模型。大模型根据预设规则（保留重要信息、去除闲聊、控制在200字以内等）生成一段高度浓缩的新摘要。
- **持久化存储**：最终，`SummaryMemory.save_summary()` 会将这段新摘要通过 `UPSERT`（有则更新，无则插入）的方式安全地写回 PostgreSQL 数据库，完成一次记忆的迭代。

## （三）存储和查询

```python
class SummaryMemory:
    def __init__(self,session_id):
        self.session_id = session_id

    # 保存
    def save_summary(self,summary:str):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                sql = f"INSERT INTO conversation_summary(session_id, summary) VALUES({self.session_id},{summary}) ON CONFLICT(session_id) DO UPDATE SET summary=EXCLUDED.summary,update_time=NOW()"
                cur.execute(sql)
                # 提交事务
                conn.commit()

    # 查询
    def query_summary(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                sql = f"SELECT summary FROM conversation_summary WHERE session_id={self.session_id}"
                cur.execute(sql)
                # 查询单个值
                result = cur.fetchone()
                if result:
                    return result[0]
                else:
                    return None
```

- `with`关键字 -- 用于实现**上下文管理器（Context Manager）**机制
    - 核心作用：**自动管理资源的分配和释放**，确保无论代码块中的操作是否发生异常，相关的清理工作（如关闭文件、释放连接等）都能被正确执行
    - `with pool.connection() as conn:`
        - 从连接池中借出一个数据库连接，并在代码块执行完毕后自动归还
        - 如果不使用 `with`，你需要手动调用 `conn.close()` 或 `pool.putconn(conn)` 来归还连接。如果中间代码报错，很容易忘记归还，导致**连接泄漏**，最终耗尽连接池。使用 `with` 可以确保连接在操作结束后（哪怕是发生异常时）一定会被安全地归还到连接池中

    - `with conn.cursor() as cur:`
        - 创建一个数据库游标，并在代码块执行完毕后自动关闭该游标
        - 游标（Cursor）是执行 SQL 语句的载体，它本身也会占用内存和数据库资源。使用 `with` 可以确保 SQL 执行完毕后，游标被立即释放，避免资源浪费

- `INSERT INTO conversation_summary(session_id, summary) VALUES({self.session_id},{summary}) ON CONFLICT(session_id) DO UPDATE SET summary=EXCLUDED.summary,update_time=NOW()` -- 尝试向表中插入一条新记录，如果因为主键或唯一键冲突导致插入失败，则自动更新该条已存在的记录
- `fetchonr` -- 用于从查询结果集中获取下一行数据，返回一个元组，如果没有更多数据则返回 `None`

## （四）会话管理

会话管理中只需要创建实例就可以了，供后续智能体调用，执行摘要的读取与保存

```python
# 原本导入的
......
# 导入
from memory.save.summary_memory import SummaryMemory

class SessionManager:
    def __init__(self,session_id):
        # 之前创建的实例
        ......
        # 创建实例
        self.summary_memory = SummaryMemory(self.session_id)

    # 添加窗口记忆
    ......

    # 构建提示词
    ......
```

## （五）提示词

查询已有的摘要记忆，拼接到提示词中，返回给会话管理统一使用

```python
# 原本导入的
......
from memory.save.summary_memory import SummaryMemory

class BuilderPrompt:
    def __init__(self,session_id):
        # 原本创建的实例
        ......
        self.summary_memory = SummaryMemory(session_id)

    # 构建提示词
    def builder_prompt(self):
        prompt = """
         -- 角色：你是一个记忆提取助手
         -- 任务：
            - 理解用户需求
            - 根据用户问题，提取相关记忆
        """
        
        # 查询窗口记忆 -- 提取记忆
        ......

        # 查询摘要记忆 -- 提取记忆
        summary_memory = self.summary_memory.query_summary()
        prompt += "短期记忆 -- 摘要记忆"
        prompt += summary_memory

        return prompt
```

## （六）Agent记忆提取

初始化摘要智能体的同时：

- 创建实例对象：大模型、提示词、智能体、摘要记忆

创建摘要智能体提示词，创建摘要智能体

业务代码：记忆更新，传入参数为窗口记忆的消息

- 调用摘要记忆，获取旧摘要
- 定义空提示词，将窗口记忆中用户的问题（多轮对话的多个问题）拼接到提示词中（回复不需要拼接，因为会显得冗余）
- 将拼接好的提示词和旧摘要作为问题传递给智能体，生成回复
- 将生成的回复，也就是新的摘要存储到摘要记忆中

```python
from langchain.agents import create_agent
from model.my_model import MyModel
from memory.save.summary_memory import SummaryMemory
from langchain_core.messages import HumanMessage

class SummaryAgent:
    def __init__(self,summary_memory:SummaryMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.summary_memory = summary_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个摘要生成助手
         -- 任务：
            - 根据旧摘要和最新的聊天记录生成新的摘要
         -- 规则：
            - 保留重要信息
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 只返回新的摘要
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=False,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,messages):
        # 查询旧摘要
        old_summary = self.summary_memory.query_summary()
        # 最新聊天记录
        prompt = ""
        for i in messages:
            if i['role'] == 'user':
                prompt += f"用户提问：{i['content']}"
        # 问题
        que = f"请根据旧摘要：{old_summary}和最新聊天记录：{prompt}"
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=que)]})
        # 把新摘要存入到摘要记忆中
        self.summary_memory.save_summary(result['messages'][-1].content)
```

## （七）记忆管理器

初始化记忆管理器的同时：创建摘要智能体实例对象，窗口记忆实例对象

更新记忆：先调用窗口记忆`window_memory.py`查询原窗口记忆，若窗口记忆长度超过限制则触发摘要记忆，调用摘要智能体`SummaryAgent.py`

```python
from memory.retrieval.SummaryAgent import SummaryAgent
from memory.manager.session_manager import SessionManager
"""
记忆管理器，管理记忆的更新
"""

class MemoryManager:
    def __init__(self,sessionManager:SessionManager):
        # 摘要智能体
        self.summary_agent = SummaryAgent(sessionManager.summary_memory)
        # 获取窗口记忆对象
        self.window_memory = sessionManager.window_memory

    def update(self):
        # 查询，获取窗口记忆
        query_window = self.window_memory.query()
        # 触发摘要
        if len(self.window_memory.query()) >= 2:
            # 更新摘要记忆
            self.summary_agent.update(query_window)
```

## （八）验证

创建聊天智能体，用于生成用户问题的回复

在调用聊天智能体之前：通过会话管理创建会话实例对象，创建窗口记忆，构建提示词，滑动窗口存储AI生成的回复

获得智能体回复之后：通过记忆管理器，更新摘要记忆

```python
from langchain_core.messages import HumanMessage, SystemMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager
from memory.manager.memory_manager import MemoryManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

# 创建提示词 -- 系统提示词
prompt = """
	-- 角色：你是一个专业的聊天助手
	-- 任务：
	    - 理解用户问题，回答用户问题
	-- 规则：
	    - 你只需要回答用户问题，不需要每次携带记忆内容
"""

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=False,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[]
)

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("1")
    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)
    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt()

    # 提问
    human_msg = {"messages":[HumanMessage(content=que),memory_prompt]}
    # 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)

    # 更新记忆
    memory_manager = MemoryManager(session_manager)
    memory_manager.update()

    print(data)
    return data


if __name__ == '__main__':
    q1 = "我叫张三，今年23岁"
    q2 = "我喜欢打篮球"
    q3 = "我在学习langchain"
    q4 = "我在学习什么"
    q5 = "我是谁，今年多大了"
    for q in [q1, q2, q3, q4, q5]:
        print("---------------------")
        create_email_agent(q)
```

# 四、长期记忆

## （一）长期与短期记忆

长期与短期记忆的核心区别：跨会话

**容量与时效**：

- 短期记忆（窗口记忆）容量极小（仅保留最近几轮对话），且随时间快速遗忘；
- 长期记忆（摘要记忆）容量几乎无限，能够长久保存。

**信息形态**：

- 短期记忆保留了对话的原始细节（一问一答）；
- 长期记忆则是经过大模型深度加工、高度浓缩的“核心要点”。

**运作机制**：

- 短期记忆是被动记录；
- 而长期记忆需要主动触发（如 `MemoryManager` 在消息达到阈值时，调用 `SummaryAgent` 进行提炼和覆盖保存）。

## （二）添加与查询

`long_memory.py` 是一个**长期记忆存储与检索模块**，基于 ChromaDB 向量数据库实现。它的核心作用是持久化保存用户的事实性信息（如姓名、年龄、爱好、技能等），并在对话中根据当前问题检索相关记忆，以供智能体使用。

```python
import chromadb
import os
import uuid
from dotenv import load_dotenv

class LongMemory:
    def __init__(self):
        load_dotenv()
        # 数据库路径
        path = os.getenv("CHROMA_PATH")
        # 连接向量数据库
        client = chromadb.PersistentClient(path)
        # 创建向量集合
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
```

**初始化**

- 加载环境变量（`CHROMA_PATH`）获取数据库存储路径。
- 连接 ChromaDB 持久化客户端，并获取或创建名为 `"long_memory"` 的集合（Collection）。

**保存记忆（`save_long`）**

- 接收参数 `user_id`（用户标识）和 `query`（待存储的事实描述，如“用户擅长Python”）。
- 生成唯一 ID（格式：`memory_{user_id}_{uuid}`）。
- 将 `query` 作为文档（`documents`）存入集合，并附带元数据 `{"user_id": user_id}`。
- 输出成功日志。

**查询记忆（`query_long`）**

- 接收参数 `user_id` 和 `question`（当前用户提问，如“我擅长什么？”）。
- 调用集合的 `query` 方法，使用 `question` 进行语义检索，返回最相似的 3 条文档（`n_results=3`），并限定 `where={"user_id": user_id}` 确保只检索该用户的记忆。
- 打印查询到的文档并返回文档列表（`doc`）。

## （三）会话管理器

主要负责四层记忆的对象创建和提示词的生成

`SessionManager` 作为会话管理的核心，负责**长期记忆对象的初始化**以及**将长期记忆内容整合进系统提示词**，供智能体在回答时使用。

```python
。。。。。。
# 导入
from memory.save.long_memory import LongMemory

class SessionManager:
    def __init__(self,session_id:str):
        。。。。。。
        # 创建实例
        self.long_memory = LongMemory()

    # 添加窗口记忆
    。。。。。。

    # 构建提示词 -- 添加形参：用户id和问题
    def builder_prompt(self,user_id,question):
        prompt = self.b_p.builder_prompt(user_id,question)
        return {"role":"system","content":prompt}
```

**初始化**

- 在 `__init__` 中创建 `LongMemory` 实例并赋值给 `self.long_memory`，以便后续操作。

**提示词构建**

- 调用 `builder_prompt(user_id, question)` 时，它会通过 `self.b_p.builder_prompt(user_id, question)` 触发 `BuilderPrompt` 的构建方法。
- 在 `BuilderPrompt.builder_prompt` 内部，会调用 `self.long_memory.query_long(user_id, que)` 查询该用户的长期记忆（基于当前问题语义检索）。
- 查询结果被拼接到提示词的“【用户记忆】”部分，最终返回 `{"role":"system","content":prompt}`，其中 `prompt` 包含了长期记忆内容。

`SessionManager` **不直接操作**长期记忆的增删改，只负责**持有** `LongMemory` 对象，并在提示词构建时**间接调用**其查询方法，确保长期记忆被注入到系统消息中，从而影响智能体的回答

## （四）提示词

在构建系统提示词时，**调用长期记忆模块**，根据当前用户 ID 和问题语义检索相关记忆，并将检索结果以可读格式嵌入提示词中，供后续智能体使用。

```python
。。。。。。
from memory.save.long_memory import LongMemory

class BuilderPrompt:
    def __init__(self,session_id):
        。。。。。。
        self.long_memory = LongMemory()

    # 构建提示词
    def builder_prompt(self,user_id,que):
        prompt = """
         -- 角色：你是一个记忆提取助手
         -- 任务：
            - 理解用户需求
            - 根据用户问题，提取相关记忆
        """
        
        # 查询窗口记忆 -- 提取记忆
        。。。。。。

        # 查询摘要记忆 -- 提取记忆
        。。。。。。

        # 查询长期记忆 -- 提取记忆
        long_memory = self.long_memory.query_long(user_id,que)
        prompt += "长期记忆"
        for x in long_memory:
            prompt += x+'\n'
            
        return prompt
```

**初始化**

- `__init__` 中实例化 `LongMemory`，并赋值给 `self.long_memory`。

**构建提示词**（`builder_prompt` 方法）

- 方法内部调用 `self.long_memory.query_long(user_id, que)`，传入用户标识和当前问题。
- 该方法返回最相关的 3 条长期记忆文档（列表形式）。
- 遍历该列表，将每条记忆拼接为字符串，添加前缀“长期记忆”并换行，最终合并到 `prompt` 变量中。
- 返回完整的 `prompt` 字符串（包含所有记忆类型，但长期记忆部分已按上述方式整合）。

## （五）长期记忆Agent

`LongAgent.py` 是一个**长期记忆更新智能体**，负责根据用户输入判断是否需要提取事实性信息，并将有效信息以结构化形式存入长期记忆向量数据库。它专门处理**陈述句**（提取事实）和**疑问句**（跳过更新）的区分。

```python
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.long_memory import LongMemory

class LongAgent:
    def __init__(self,long_memory:LongMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取长期记忆的保存对象
        self.long_memory = long_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个长期记忆助手
         -- 任务：
            - 根据用户问题提取相关的长期记忆信息
         -- 规则：
            - 如果用户输入是陈述句（例如：“我叫张三”，“我喜欢Python”），请从中提取关键事实（如姓名、爱好、技能等），并以简洁的第三人称形式输出，用于更新记忆。
            - 如果用户输入是疑问句（例如：“我叫什么？”，“我擅长什么？”），请直接输出“NO_UPDATE”，表示无需更新记忆。
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,user_id,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        self.long_memory.save_long(user_id,result['messages'][-1].content)
        print("长期记忆更新成功")
```

**初始化**

- 接收 `LongMemory` 实例，用于后续保存操作。
- 加载大模型（`MyModel.get_model()`），并基于预设的提示词创建智能体（`create_agent`）。

**更新入口（`update(user_id, question)`）**

- 将用户问题（`question`）作为 `HumanMessage` 发送给智能体。
- 智能体根据提示词规则判断：
    - **陈述句**（如“我叫张三”）→ 提取关键事实，以简洁的第三人称形式输出（如“用户姓名为张三”）。
    - **疑问句**（如“我擅长什么？”）→ 直接输出 `"NO_UPDATE"`。
- 将智能体的输出内容（`result['messages'][-1].content`）调用 `self.long_memory.save_long(user_id, ...)` 存入长期记忆库（即使是 `"NO_UPDATE"` 也会被存储，这是个潜在问题，但不影响主流程）。
- 打印成功日志。

**辅助方法**

- `get_prompt()`：返回系统提示词，定义角色、任务和规则。
- `get_agent()`：创建并返回 LangChain 智能体实例。

## （四）记忆管理器

作为记忆管理的总控制器，在用户交互发生时**触发长期记忆的更新**，并协调长期记忆智能体执行事实提取与存储。

```python
from memory.retrieval.SummaryAgent import SummaryAgent
from memory.manager.session_manager import SessionManager

# 导入智能体
from memory.retrieval.LongAgent import LongAgent

class MemoryManager:
    def __init__(self,sessionManager:SessionManager):
        self.summary_agent = SummaryAgent(sessionManager.summary_memory)
        self.window_memory = sessionManager.window_memory
        
        # 创建长期记忆智能体
        self.long_agent = LongAgent(sessionManager.long_memory)

    def update(self,user_id,question):
        query_window = self.window_memory.query()
        
        # 更新长期记忆
        self.long_agent.update(user_id,question)
        
        if len(self.window_memory.query()) >= 2:
            self.summary_agent.update(query_window)
```

**初始化**

- 在 `__init__` 中从 `SessionManager` 获取 `long_memory` 对象，并创建 `LongAgent` 实例，将其赋值给 `self.long_agent`。

**更新入口（`update(user_id, question)`）**

- 调用 `self.long_agent.update(user_id, question)`，将当前用户问题和用户 ID 传递给长期记忆智能体。
- 该调用会触发长期记忆的提取（陈述句）或跳过（疑问句），并将结果存入向量数据库。
- 更新操作独立于其他记忆类型（摘要、窗口），不受窗口长度或摘要条件影响，每次用户提问都会执行。

`MemoryManager` 对长期记忆的操作仅为**触发更新**，不涉及查询或检索。查询由 `BuilderPrompt` 在其他流程中完成。此模块确保每次对话都会尝试更新长期记忆，以保持事实信息持续累积。

## （五）验证

这是一个**测试脚本**，用于验证长期记忆是否能够在对话中被正确检索并用于回答。它模拟了一个完整的对话流程：接收用户问题 → 更新记忆 → 构建包含长期记忆的提示词 → 调用智能体回答 → 保存回答

```python
from langchain_core.messages import HumanMessage, SystemMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager
from memory.manager.memory_manager import MemoryManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("001")

    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)

    # 更新记忆
    memory_manager = MemoryManager(session_manager)
    memory_manager.update(1, que)

    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt(1, que)

    # 创建提示词 -- 系统提示词
    prompt = f"""
    	-- 角色：你是一个专业的聊天助手
    	-- 任务：
    	    - 理解用户问题，回答用户问题
    	-- 规则：
    	    - 你只需要回答用户问题，回复内容不需要每次携带记忆内容
    	    - 请严格根据以下【用户记忆】来回答用户的问题，如果记忆中有答案，请直接回答：

        【用户记忆】：
        {memory_prompt['content']}
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=False,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que),
        SystemMessage(content=prompt),
    ]}

    # 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)

    print(data)
    return data


if __name__ == '__main__':
    q1 = "我叫张三，今年23岁"
    q2 = "我擅长python"
    q3 = "我在学习langchain"
    q4 = "我在学习什么"
    q5 = "我擅长什么"
    create_email_agent(q5)
```

**初始化**

- 加载大模型（`my_model.MyModel.get_model()`）和空工具列表。

**定义智能体创建函数 `create_email_agent(que)`**

- 每次调用时：
    a. **创建会话管理器**（`SessionManager("001")`），负责管理四层记忆对象。
    b. **保存当前用户问题到窗口记忆**（调用 `save_window_memory("user", que)`）。
    c. **更新长期记忆**：创建 `MemoryManager`，调用其 `update(1, que)`，触发 `LongAgent` 提取事实并存入向量库。
    d. **构建记忆提示词**：调用 `session_manager.builder_prompt(1, que)`，从各层记忆中检索并拼接内容（包括长期记忆），获得系统提示词。
    e. **创建回答智能体**：使用自定义系统提示词（包含“【用户记忆】”部分）和对话消息（`HumanMessage` + `SystemMessage`）调用 `agent.invoke`，获取非流式回答。
    f. **保存 AI 回复到窗口记忆**（`save_window_memory("assistant", data)`），并打印回答。

**主程序**

- 预先定义了 5 个问题（q1~q5）
- 先运行 q1~q3 来填充长期记忆，然后清空窗口和摘要，仅保留长期记忆，以测试是否能正确检索。
- 执行 `create_email_agent(q5)`（“我擅长什么”），查看长期记忆是否有效

# 五、用户图像记忆

**用户画像记忆（User Profile Memory）**。这里的“用户画像”并不是指一张真实的照片，而是系统从历史交互中提炼出的一份**结构化“人物小传”**。

具体来说，它主要包含以下几个维度的信息：

1. **基本与偏好信息**：记录用户的职业、所在城市、回复风格偏好（如喜欢简洁）等相对稳定的特征。
2. **具体事实与习惯**：沉淀用户在对话中提到的具体经历、兴趣爱好和行为习惯。
3. **动态更新机制**：这些画像信息会随着每次对话自动提取和更新，并带有“置信度”权重，以区分用户的随口一说和长期稳定的偏好。

**核心作用**：它让AI或系统从“只记得当前聊了什么”升级为“真正认识你是谁”，从而在跨会话时提供高度个性化的服务和主动推荐。

## （一）保存与查询

实现了一个**基于 Redis 的用户画像记忆存储模块**。

核心功能是将用户的特征信息（如姓名、年龄等）以键值对的形式持久化存储到 Redis 数据库中，以便后续快速读取和更新。

```python
import redis

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
```

- **初始化连接**
    程序启动时，`ProfileMemory` 类会根据传入的 `user_id` 初始化 Redis 连接，并生成一个唯一的存储键（格式为 `profile_memory:{user_id}`），用于隔离不同用户的数据。
- **保存数据**
    调用 `save_profile(hashkey, value)` 方法时，程序会利用 Redis 的哈希结构，将具体的属性（如 "name"）和对应的值（如 "Roy"）写入到该用户的存储键下。
- **查询数据**
    调用 `query_profile()` 方法时，程序会从 Redis 中获取该用户键下的所有字段和值，将其解码并拼接成字符串格式，从而还原出用户的完整画像信息。

## （二）会话管理器

实现了一个**会话管理器（SessionManager）**，它就像整个记忆系统的“总控台”，负责把不同类型的记忆模块（如短期、长期、画像等）组装起来，统一对外提供“构建提示词”的服务。

- **初始化加载**：当 `SessionManager` 启动时，会根据传入的 `user_id` 立即实例化 `ProfileMemory` 对象，建立与该用户画像数据的连接。
- **参与构建**：当系统需要生成回复（调用 `builder_prompt`）时，管理器会调用提示词构建器（`BuilderPrompt`）。此时，`ProfileMemory` 中存储的用户特征会被提取出来，作为背景信息注入到提示词中，让 AI 能基于对用户的了解来回答问题。

```python
......
from memory.save.profile_memory import ProfileMemory


class SessionManager:
    def __init__(self,session_id:str,user_id):
        ......
        self.b_p = BuilderPrompt(self.session_id,user_id)
        ......
        self.profile_memory = ProfileMemory(user_id)

    # 添加窗口记忆
    ......

    # 构建提示词
    ......
```

## （三）提示词

实现了一个**提示词构建器（BuilderPrompt）**，它就像一个“记忆组装工厂”，负责把分散在不同地方的记忆（短期、长期、画像）收集起来，拼装成一段完整的背景信息给 AI 看。

- **初始化**：在构建器启动时，它会根据传入的 `user_id` 实例化 `ProfileMemory` 对象，准备好读取该用户画像数据的通道。
- **提取与组装**：当调用 `builder_prompt` 方法构建提示词时，它会执行 `self.builder_prompt.query_profile()`。这一步会从存储中把该用户的画像信息提取出来，拼接到最终的提示词字符串中（格式为 `用户画像：...`），让 AI 在回答当前问题前，先“复习”一遍用户的基本特征。

```python
......
from memory.save.profile_memory import ProfileMemory

class BuilderPrompt:
    def __init__(self,session_id,user_id):
        ......
        self.profile_memory = ProfileMemory(user_id)

    # 构建提示词
    def builder_prompt(self,user_id,que):
        prompt = """
         -- 角色：你是一个记忆提取助手
         -- 任务：
            - 理解用户需求
            - 根据用户问题，提取相关记忆
        """
        
        # 查询窗口记忆 -- 提取记忆
        ......

        # 查询摘要记忆 -- 提取记忆
        ......

        # 查询长期记忆 -- 提取记忆
        ......

        # 查询用户画像 -- 提取记忆
        profile_memory = self.profile_memory.query_profile()
        prompt += f"用户画像：{profile_memory}"
        return prompt
```

## （四）用户图像记忆Agent

实现了一个**用户画像提取智能体（ProfileAgent）**。

它就像是一个专门负责“听”和“记”的助手，利用大模型从用户的自然语言对话中自动识别并提取关键个人信息（如姓名、爱好等），然后将其结构化存储：

`{'name': 'roy', 'age': 0, 'job': '', 'address': '', 'hobby': '蹦蹦跳跳', 'xueli': ''}`

核心任务是从用户的闲聊或提问中，精准筛选出关于**姓名、年龄、职业、地址、学历、爱好**这六类画像信息，过滤掉无关的闲聊内容，实现用户画像的自动构建与更新

- **初始化**：启动时，它会加载一个预设了提取规则的提示词（Prompt），告诉大模型需要关注哪些字段，并实例化一个用于存储数据的 `ProfileMemory` 对象。
- **提取信息**：当调用 `update(question)` 方法传入用户问题时，智能体会将问题发送给大模型。大模型会根据提示词规则，从文本中分析并输出一个结构化的数据对象（如 `{'name': 'Roy', 'hobby': '蹦蹦跳跳'}`）。
- **保存画像**：程序接收到大模型返回的结构化数据后，会遍历其中的键值对。如果发现某个字段有值（非空），就调用 `self.profile_memory.save_profile(key, value)` 方法，将这些信息持久化保存下来。

```python
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.profile_memory import ProfileMemory
from pydantic import BaseModel,Field

class ProfileParams(BaseModel):
    name:str = Field(description="姓名")
    age:int = Field(description="年龄")
    job:str = Field(description="职业")
    address:str = Field(description="地址")
    hobby:str = Field(description="爱好")
    xueli:str = Field(description="学历")

"""
用户画像记忆智能体
"""

class ProfileAgent:
    def __init__(self,profile_memory:ProfileMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.profile_memory = profile_memory

    def get_prompt(self):
        self.prompt = """
        -- 角色：你是一个用户画像提取助手
        -- 任务：
            - 根据用户问题提取相关用户画像信息
        -- 规则：
            - 用户画像信息包含以下信息：姓名，年龄，爱好，职业，地址，学历
            - 去掉闲聊内容
            - 避免重复
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
            - 如果没有用户画像信息，返回空
        -- 输出：
            - 只输出姓名，年龄，职业，地址，学历
        -- 示例：
            用户输入：我喜欢打游戏
            输出:{'name': '', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
             
            用户输入：我是张三
            输出:{'name': '张三', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[],
            response_format=ProfileParams
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        data = result['structured_response'].model_dump()
        for key,value in data.items():
            if value:
                print("有用户画像")
                print(f"{key}:{value}")
                self.profile_memory.save_profile(key,value)
```

## （五）记忆管理器

实现了一个**记忆管理器（MemoryManager）**，它就像整个记忆系统的“指挥官”，负责统一调度和协调摘要、长期记忆、用户画像等不同记忆模块的更新工作

核心职责是**自动更新用户画像**。通过调用专门的 `ProfileAgent`（画像智能体），它能从用户的最新提问中识别并提取关键个人信息，确保系统对用户的认知是动态且准确的

- **初始化**：在管理器启动时，它会根据传入的 `SessionManager` 中的 `profile_memory`（画像存储对象），来创建并初始化一个 `ProfileAgent` 实例，为后续更新做好准备。
- **触发更新**：当外部调用 `update(user_id, question)` 方法，传入用户的最新问题时，管理器会立即执行 `self.profile_agent.update(question)`。这一步会将用户的问题交给画像智能体去处理，智能体分析后会自动将提取到的新信息保存起来，完成画像的更新。

```python
。。。。。。
from memory.retrieval.ProfileAgent import ProfileAgent

class MemoryManager:
    def __init__(self,sessionManager:SessionManager):
        # 摘要智能体
        。。。。。。
        # 获取窗口记忆对象
        。。。。。。
        # 创建长期记忆智能体
        。。。。。。
        # 创建用户画像智能体
        self.profile_agent = ProfileAgent(sessionManager.profile_memory)

    def update(self,user_id,question):
        # 查询，获取窗口记忆
        。。。。。。
        # 更新长期记忆
        。。。。。。
        # 更新用户画像记忆
        self.profile_agent.update(question)
        # 触发摘要
        。。。。。。
```

## （六）验证

这是一个用于**验证用户画像记忆功能的集成测试脚本**。

它通过模拟一个“告知信息 -> 验证回忆”的完整闭环，来测试 AI 系统能否成功记住并利用用户的个人信息进行对话。

该脚本的核心功能是验证 AI 的记忆系统是否正常工作。它不关心 AI 的通用聊天能力，而是专注于测试一个特定流程：

1. **写入记忆**：向 AI 提供关于“我是谁”的个人信息（如姓名、年龄、爱好）。
2. **读取记忆**：在后续的对话中，询问 AI 之前提供的信息，检查它是否能准确回答。

```
from langchain_core.messages import HumanMessage, SystemMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager
from memory.manager.memory_manager import MemoryManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("001",1)

    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)

    # 更新记忆
    memory_manager = MemoryManager(session_manager)
    memory_manager.update(1, que)

    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt(1, que)

    # 创建提示词 -- 系统提示词
    prompt = f"""
        -- 角色：你是一个专业的聊天助手
        -- 任务：
            - 理解用户问题，回答用户问题
        -- 规则：
            - 你只需要回答用户问题，回复内容不需要每次携带记忆内容
            - 请严格根据以下【用户记忆】来回答用户的问题，如果记忆中有答案，请直接回答：

        【用户记忆】：
        {memory_prompt['content']}
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=False,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que),
        SystemMessage(content=prompt),
    ]}

    # 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)

    print(data)
    return data
```

**初始化会话管理器**

- 首先，程序会创建一个 `SessionManager` 实例。这个管理器是整个记忆系统的“总控台”，它会根据用户 ID 初始化并管理所有不同类型的记忆模块，包括短期窗口记忆、摘要记忆、长期记忆和**用户画像记忆**。

**保存短期对话**

- 用户的原始问题（`que`）会立刻通过 `session_manager.save_window_memory` 方法被保存下来。这属于短期记忆，确保了对话的上下文连贯性。

**更新长期与画像记忆**

- 接着，程序会创建一个 `MemoryManager` 实例，并调用其 `update` 方法。
- 这个管理器会分析用户的问题，判断其中是否包含需要长期保存的信息。特别是，它会调用**用户画像智能体 (ProfileAgent)** 来专门检查问题中是否含有姓名、年龄、职业等个人信息。如果有，就自动提取并更新到用户画像记忆中。

**构建智能提示词**

- 这是最关键的一步。程序调用 `session_manager.builder_prompt` 方法。
- 这个方法会像一个“信息收集员”，从 `SessionManager` 管理的各个记忆模块中（短期窗口、摘要、长期记忆、**用户画像**）把所有相关信息都提取出来。
- 然后，它将这些信息拼装成一段结构化的文本（即 `memory_prompt`），作为背景知识注入到给 AI 的系统提示词中。这样，AI 在回答问题前，就已经“复习”了关于用户的所有已知信息。

**创建并调用智能体**

- 程序使用上一步生成的、包含了丰富记忆信息的完整提示词，来创建一个 LangChain 智能体 (`create_agent`)。
- 然后，将用户的问题提交给这个智能体 (`agent.invoke`)。智能体结合其自身能力和提示词中提供的“记忆”，生成一个个性化的、知情的回复。

**保存 AI 回复并输出**

- 获取到 AI 的回复内容后，程序会再次调用 `session_manager.save_window_memory`，将 AI 的回答也作为一轮对话保存到短期记忆中，以保持对话历史的完整性。
- 最后，将 AI 的回答打印出来，完成一次完整的交互。

```
if __name__ == '__main__':
    print("=== 开始测试用户画像记忆 ===\n")

    # --- 第一阶段：输入信息（写入记忆）---
    print(">>> 步骤1：告诉AI你的信息...")

    # 1. 输入姓名和年龄
    q1 = "我叫Roy，今年26岁"
    print(f"用户输入: {q1}")
    create_email_agent(q1)

    # 2. 输入职业和爱好
    q2 = "我是一名歌手，平时喜欢唱歌和滑雪"
    print(f"用户输入: {q2}")
    create_email_agent(q2)

    print("\n--- 记忆已更新，开始验证 ---\n")

    # --- 第二阶段：验证回忆（读取记忆）---
    print(">>> 步骤2：询问AI刚才的信息...")

    # 3. 验证姓名
    q3 = "我叫什么名字？"
    print(f"用户输入: {q3}")
    create_email_agent(q3)

    # 4. 验证职业
    q4 = "我的职业是什么？"
    print(f"用户输入: {q4}")
    create_email_agent(q4)

    # 5. 验证爱好
    q5 = "我平时喜欢做什么？"
    print(f"用户输入: {q5}")
    create_email_agent(q5)

    print("\n=== 测试结束 ===")
```

