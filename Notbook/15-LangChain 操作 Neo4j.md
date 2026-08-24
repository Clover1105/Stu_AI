# 一、环境准备

大语言模型擅长理解自然语言，但它本身并不直接保存业务系统中的实时结构化数据

将 LangChain 与 Neo4j 结合后，可以实现：

```
用户自然语言问题
    ↓
大模型理解问题
    ↓
生成 Cypher 查询语句
    ↓
查询 Neo4j 图数据库
    ↓
根据查询结果生成自然语言回答
```

## （一）版本

### 1. 导入

```
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain, Neo4jVector
```

### 2. 安装依赖

```
pip install langchain==1.1.0 -i https://repo.huaweicloud.com/repository/pypi/simple/
pip install langchain-neo4j -i https://repo.huaweicloud.com/repository/pypi/simple/
pip install neo4j -i https://repo.huaweicloud.com/repository/pypi/simple/
pip install langchain-openai -i https://repo.huaweicloud.com/repository/pypi/simple/
pip install python-dotenv -i https://repo.huaweicloud.com/repository/pypi/simple/
```

如果后续要做文本切分和向量存储，可以继续安装：

```
pip install langchain-text-splitters -i https://repo.huaweicloud.com/repository/pypi/simple/
```

### 3. Neo4j 启动要求

请确保 Neo4j 数据库已经启动，并确认以下信息：

可以先在 Neo4j Browser 中测试连接是否正常

| 配置项    | 示例                    |
| --------- | ----------------------- |
| Bolt 地址 | `bolt://127.0.0.1:7687` |
| 用户名    | `neo4j`                 |
| 密码      | `rootroot`              |
| 数据库名  | `neo4j`                 |

## （二）配置环境变量

在项目根目录创建 `.env` 文件或者在环境变量中配置：

```env
DASHSCOPE_API_KEY=你的阿里云百炼或 DashScope API Key
NEO4J_URL=bolt://127.0.0.1:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=rootroot
NEO4J_DATABASE=neo4j
```

- `DASHSCOPE_API_KEY` 用于调用通义千问模型

- `NEO4J_URL` 是 Neo4j 的 Bolt 连接地址

- `NEO4J_USERNAME` 和 `NEO4J_PASSWORD` 是数据库账号密码

- `NEO4J_DATABASE` 是数据库名称

## （三）连接 Neo4j 数据库

操作的库选择 neo4j，Neo4j 安装后自带的库

`Neo4jGraph` 是 `langchain-neo4j` 提供的图数据库连接类，主要作用是：

- 连接 Neo4j 数据库

- 执行 Cypher 查询语句

- 获取图数据库结构信息

- 为 `GraphCypherQAChain` 提供图数据库对象

### 1. 封装连接工具类

```python
from langchain_neo4j import Neo4jGraph

def get_neo4j_conn():
    return Neo4jGraph(
        url="bolt://127.0.0.1:7687",
        username="neo4j",
        password="12345678",
        database="test"
    )

if __name__ == '__main__':
    conn = get_neo4j_conn()
    print(f"连接成功：{conn}")
```

# 二、LangChain 执行 Cypher 增删改查

###  1. 清空数据库

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()
graph.query("MATCH (n) DETACH DELETE n")
print("数据库已清空")
```

### 2. 创建节点

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
CREATE (a:Person {name: $name1, age: $age1}),
       (b:Person {name: $name2, age: $age2}),
       (c:Person {name: $name3, age: $age3})
"""

params = {
    "name1": "Alice", "age1": 25,
    "name2": "Bob", "age2": 30,
    "name3": "Charlie", "age3": 35,
}

graph.query(cypher, params)
print("节点创建成功")
```

### 3. 查询节点

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
MATCH (n:Person)
RETURN n.name AS name, n.age AS age
"""

result = graph.query(cypher)
print(result)
```

### 4. 修改节点属性

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
MATCH (n:Person {name: $name})
SET n.age = $age
RETURN n.name AS name, n.age AS age
"""

result = graph.query(cypher, {"name": "Alice", "age": 30})
print(result)
```

### 5. 删除节点

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
MATCH (n:Person {name: $name})
DELETE n
"""

graph.query(cypher, {"name": "Alice"})
print("节点删除成功")
```

### 6. 批量创建节点

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
UNWIND $people AS person
CREATE (:Person {name: person.name, age: person.age, city: person.city})
"""

params = {
    "people": [
        {"name": "Alice", "age": 25, "city": "北京"},
        {"name": "Bob", "age": 30, "city": "上海"},
        {"name": "Charlie", "age": 35, "city": "深圳"},
    ]
}

graph.query(cypher, params)
print("批量创建成功")
```

### 7. 创建关系

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
MATCH (a:Person {name: $name1}), (b:Person {name: $name2})
CREATE (a)-[:KNOWS {since: $since}]->(b)
"""

params = {
    "name1": "Alice",
    "name2": "Bob",
    "since": 2020,
}

graph.query(cypher, params)
print("关系创建成功")
```

### 8. 查询关系

```
from Neo4jUtil import connect_to_neo4j

graph = connect_to_neo4j()

cypher = """
MATCH (a:Person)-[r:KNOWS]->(b:Person)
RETURN a.name AS start, type(r) AS relation, r.since AS since, b.name AS end
"""

result = graph.query(cypher)
print(result)
```

# 三、使用问答链

### 1. 创建连接图数据库工具类

```
from langchain_neo4j import Neo4jGraph

def get_neo4j_conn():
    return Neo4jGraph(
        url="bolt://127.0.0.1:7687",
        username="neo4j",
        password="12345678",
        database="neo4j"
    )

if __name__ == '__main__':
    conn = get_neo4j_conn()
    print(f"连接成功：{conn}")
```

### 2. 连接数据库

```
from Load import LangChainNeo4jUtil
conn = LangChainNeo4jUtil.get_neo4j_conn()
```

### 3. 创建问答大模型对象

```
import os
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )
```

## （一）无历史记录

### 4. 提示词

```
from langchain_core.prompts import PromptTemplate

# 生成CQL的提示词
CYPHER_GENERATION_TEMPLATE = """Task:Generate Cypher statement to query a graph database.
Instructions:
Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.
Schema:
{schema}

# 节点标签及含义
| 节点标签     | 含义             |
|--------------|------------------|
| Disease      | 疾病（核心节点） |
| Symptom      | 症状             |
| Check        | 检查项目         |
| Cureway      | 治疗方式         |
| Drug         | 药物             |
| Department   | 就诊科室         |
| Food         | 食物             |
| Dishes       | 菜肴             |
| Category     | 疾病分类         |

# 关系类型及含义
| 关系类型             | 含义              | 起始节点 | 目标节点    |
|----------------------|-------------------|----------|-------------|
| DISEASE_SYMPTOM      | 疾病症状          | Disease  | Symptom     |
| DISEASE_CHECK        | 相关检查项目      | Disease  | Check       |
| DISEASE_CUREWAY      | 治疗方式          | Disease  | Cureway     |
| DISEASE_DRUG         | 治疗或相关药物    | Disease  | Drug        |
| DISEASE_DEPARTMENT   | 就诊科室          | Disease  | Department  |
| DISEASE_DO_EAT       | 推荐进食的食物    | Disease  | Food        |
| DISEASE_NOT_EAT      | 不推荐进食的食物  | Disease  | Food        |
| DISEASE_DISHES       | 适合疾病的菜肴    | Disease  | Dishes      |
| DISEASE_ACOMPANY     | 并发症 / 伴随疾病 | Disease  | Disease     |
| DISEASE_CATEGORY     | 疾病所属类别      | Disease  | Category    |

# 查询示例
# 问：高血压有哪些症状？
MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_SYMPTOM]->(s:Symptom) RETURN s.name AS symptom

# 问：感冒吃什么药？
MATCH (d:Disease {{name:"感冒"}})-[:DISEASE_DRUG]->(dr:Drug) RETURN dr.name AS drug

# 问：糖尿病不宜吃什么？
MATCH (d:Disease {{name:"糖尿病"}})-[:DISEASE_NOT_EAT]->(f:Food) RETURN f.name AS food

# 问：肺炎需要做什么检查？
MATCH (d:Disease {{name:"肺炎"}})-[:DISEASE_CHECK]->(c:Check) RETURN c.name AS check_item

# 问：高血压挂什么科？
MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_DEPARTMENT]->(dep:Department) RETURN dep.name AS department

# 问：感冒的并发症有哪些？
MATCH (d:Disease {{name:"感冒"}})-[:DISEASE_ACOMPANY]->(a:Disease) RETURN a.name AS complication

# 问：糖尿病属于哪类疾病？
MATCH (d:Disease {{name:"糖尿病"}})-[:DISEASE_CATEGORY]->(c:Category) RETURN c.name AS category

# 问：高血压可以吃什么菜？
MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_DISHES]->(dishes:Dishes) RETURN dishes.name AS dishes

# 问：哪些疾病会有头痛症状？
MATCH (d:Disease)-[:DISEASE_SYMPTOM]->(s:Symptom {{name:"头痛"}}) RETURN d.name AS disease

Note: Do not include any explanations or apologies in your responses.
Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
Do not include any text except the generated Cypher statement.

The question is:
{question}"""
```

```
# 问答提示词
QA_TEMPLATE = """你是一名专业的医疗智能问答助手，基于 Neo4j 疾病知识图谱为用户提供准确的健康咨询。

# 第一步：意图识别
判断用户问题是否属于【医疗疾病类】，包括但不限于：
- 疾病症状、病因、并发症
- 检查项目、就诊科室
- 治疗方式、用药建议
- 饮食宜忌、推荐菜肴
- 疾病分类与归属

# 第二步：按类别处理

## 情形 1：属于医疗疾病类 → 基于以下图谱查询结果作答
- 严格基于查询结果作答，不得编造疾病、药物或诊疗方案
- 若查询结果为空，回复："知识库中未收录该疾病的相关信息，建议咨询专业医生"

## 情形 2：不属于医疗疾病类
- 忽略知识图谱查询结果
- 基于自身通用知识自然作答
- 回复中不得出现"知识库""图谱""上下文"等字样

# 输出要求
- 直接给出最终答案，不复述问题、不解释判断过程
- 涉及用药、治疗、剂量等敏感内容时，附加一句："具体方案请遵医嘱"
- 语言简洁、准确、通俗易懂

---
【图谱查询结果】
{context}

【用户问题】
{question}

【回答】
"""
```

```
# 提示词对象
cypher_generation = PromptTemplate(
    template=CYPHER_GENERATION_TEMPLATE,
    input_variables=["schema", "question"]
)
qa = PromptTemplate(
    template=QA_TEMPLATE,
    input_variables=["context", "question"]
)
```

### 5. 问答链 -- 无历史记录

```python
# 问题
question = "糖尿病的并发症？"

# 问答链
from langchain_neo4j import GraphCypherQAChain
chain = GraphCypherQAChain.from_llm(
    llm=llm,    # 问答大模型
    cypher_prompt=cypher_generation,    # 生成CQL的提示词
    qa_prompt=qa,  # 问答提示词
    graph=conn,  # 连接图数据库
    verbose=True,   # 是否显示详细信息 --- 执行过程内容打印出来，比如CQL的生成
    allow_dangerous_requests=True, # 是否允许危险请求
)

result = chain.invoke({'query':question})
print(result)
```

## （二）有历史记录

### 4. 提示词

```
# 问答提示词
QA_TEMPLATE = """你是一名专业的医疗智能问答助手，基于 Neo4j 疾病知识图谱为用户提供准确的健康咨询。

# 第一步：意图识别
判断用户问题是否属于【医疗疾病类】，包括但不限于：
- 疾病症状、病因、并发症
- 检查项目、就诊科室
- 治疗方式、用药建议
- 饮食宜忌、推荐菜肴
- 疾病分类与归属

# 第二步：按类别处理

## 情形 1：属于医疗疾病类 → 基于以下图谱查询结果作答
- 严格基于查询结果作答，不得编造疾病、药物或诊疗方案
- 若查询结果为空，回复："知识库中未收录该疾病的相关信息，建议咨询专业医生"

## 情形 2：不属于医疗疾病类
- 忽略知识图谱查询结果
- 基于自身通用知识自然作答
- 回复中不得出现"知识库""图谱""上下文"等字样

# 输出要求
- 直接给出最终答案，不复述问题、不解释判断过程
- 涉及用药、治疗、剂量等敏感内容时，附加一句："具体方案请遵医嘱"
- 语言简洁、准确、通俗易懂

---
【历史记录】
{history}

【图谱查询结果】
{context}

【用户问题】
{question}

【回答】
"""
```

```
qa = PromptTemplate(
    template=QA_TEMPLATE,
    input_variables=["history","context", "question"]
)
```

### 5. 历史记录

```
# 历史记录（原始消息列表）
history_messages = [
    {"role": "user", "content": "我叫cc"},
    {"role": "assistant", "content": "你好cc。"},
    {"role": "user", "content": "我今年29岁"},
    {"role": "assistant", "content": "好滴。"},
]

# 将历史记录格式化为可读的对话文本
def format_history(messages):
    role_map = {"user": "用户", "assistant": "助手"}
    lines = []
    for msg in messages:
        role = role_map.get(msg["role"], msg["role"])
        lines.append(f"{role}: {msg['content']}")
    return "\n".join(lines)

history = format_history(history_messages)
```

### 6. 预填充

```
# 预填充history，chain内部只需传context和question
qa = qa.partial(history=history)
```

### 7. 问答链 -- 有历史记录

```
from langchain_neo4j import GraphCypherQAChain
chain = GraphCypherQAChain.from_llm(
    llm=llm,    # 问答大模型
    cypher_prompt=cypher_generation,    # 生成CQL的提示词
    qa_prompt=qa,  # 问答提示词
    graph=conn,  # 连接图数据库
    verbose=True,   # 是否显示详细信息 --- 执行过程内容打印出来，比如CQL的生成
    allow_dangerous_requests=True, # 是否允许危险请求
)

result = chain.invoke({'query':question})
print(result)
```

# 四、 LLM绑定工具

目前模型有的事情不可以完成，因为它不能够去访问外部内容【比如联网查询、访问数据库等】

大模型 = 人的脑袋，不具备行动的能力 --- 如果说你需要他可以去采取行动，就需要给他一定的工具（手脚）

前提：大模型必须满足`function calling`能力

工具：本质上就是一个函数，函数的内容就是实现了某个业务的代码

落脚点：大模型不可以干的事情，我们让大模型去调用某个函数来干，得到结果 --- 生成回复

大模型调用工具流程：

​    1、识别用户问题中的意图，输出需要调用的工具列表

​    2、调用工具，获取结果

​    3、再把工具的返回结果+问题，作为输入，给大模型，让大模型生成最终的回复

大模型基于问题解析后的工具信息在输出的tool_calls中

工具的定义：

​    1、需要明确参数，比如工具的名称【给模型注册工具的时候使用的】、描述【告诉模型什么时候被调用】、参数列表【可选项】等

​    2、最初，我们可以直接使用@tool来定义：

​        参数：名称、描述、参数列表

### 1. 测试绑定工具

整个流程就是三步：
    模型判断：ollama.invoke(que) → 模型决定是否需要工具，返回 tool_calls（不执行工具）
    执行工具：遍历 tool_calls，调用对应工具获取真实结果，将结果追加到 messages
    生成回复：ollama.invoke(messages) → 把用户问题、模型的调用决策、工具返回的结果一起交给模型，由它组织成自然语言回复
这就是标准的 ReAct / Tool-Calling 循环：
    模型规划 → 工具执行 → 模型总结。代码中的 messages 列表正是用来累积这三轮对话历史的载体。

```python
# 初始化大模型
from langchain_ollama import ChatOllama
ollama = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://127.0.0.1:11434"
)

# 参数校验
from pydantic import BaseModel, Field
class getWeather(BaseModel):
    city:str = Field(..., description="城市名称")

# 定义工具函数 -- 查询天气
from langchain_core.tools import tool
@tool(
    name_or_callable="get_weather",
    description="""
        当用户需要查询某个城市的天气时，调用此工具
        参数：
            city：字符串类型，表示城市名称
    """
)
def get_weather(city:str):
    print(f"查询天气的城市：{city}")
    return f"{city}的天气是晴天"

# 模型绑定工具
ollama = ollama.bind_tools(tools=[get_weather])

# 问题
que = "你好，今天重庆的天气怎么样？"

# 模型意图识别与工具调用决策
# 让大模型进行意图识别和参数提取，生成工具调用指令，而不是直接执行工具函数。
"""
语义理解：分析用户输入 "你好，今天重庆的天气怎么样？"，判断是否需要使用已绑定的工具。
决策输出：如果判定需要调用工具，模型不会返回天气结果，而是返回一个包含 tool_calls 的响应对象，其中指明了要调用的工具名（如 get_weather）及提取出的参数（如 {"city": "重庆"}）。
不执行逻辑：此时 get_weather 函数并未被实际运行，print 语句不会触发，也不会返回“晴天”等真实数据。
"""
response = ollama.invoke(que)   # 里面包含了：工具调用指令
print("意图识别结果：\n", response)

# 保存信息
messages = []
messages.append(response)

# 解析response结果，获取工具的具体信息，然后调用工具获取结果
for tool_call in messages[0].tool_calls:
    tool_name = tool_call['name']
    city = tool_call['args']['city']
    print(f"工具名称：{tool_name}, 城市：{city}")
    tool_result = eval(tool_name).invoke(tool_call)
    print(f"工具调用结果：{tool_result}")
    # 保存工具调用结果
    messages.append(tool_result)

# 最后的回复
fin = ollama.invoke(messages)
print("最终的回复：\n", fin)
```

### 2. 天气查询实现

高德开放平台API-KEY：

```
be2c23df0824437362ed4948ecfb50d9
```

修改工具函数：

```python
# 定义工具函数 -- 查询天气
from langchain_core.tools import tool
import requests
@tool(
    name_or_callable="get_weather",
    description="""
        当用户需要查询某个城市的天气时，调用此工具
        参数：
            city：字符串类型，表示城市名称
    """
)
def get_weather(city:str):
    print(f"查询天气的城市：{city}")
    # 引入天气查询接口 --- 第三方api【高德、心知】
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": "be2c23df0824437362ed4948ecfb50d9",
        "city": city,
    }
    # 通过requests发送get请求
    result = requests.get(url=url, params=params)
    result = result.json()
    # 拼接天气数据
    live = result["lives"][0]
    return {
        "result": (
            f"{live['province']}{live['city']}当前天气{live['weather']}，"
            f"气温{live['temperature_float']}℃，湿度{live['humidity_float']}%，"
            f"{live['winddirection']}风{live['windpower']}级，"
            f"数据更新时间为{live['reporttime']}。"
        )
    }
```

### 3. Neo4j问答的工具操作

工具：天气查询+执行cql命令

```python
# 连接图数据库
from Load import LangChainNeo4jUtil
conn = LangChainNeo4jUtil.get_neo4j_conn()

# 加载大模型
from langchain_openai import ChatOpenAI
import os
llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

# 参数校验
from pydantic import BaseModel, Field
class CypherTool(BaseModel):
    cypher: str = Field(..., description="Cypher语句")
class WeatherTool(BaseModel):
    city: str = Field(..., description="城市名称")

# 创建执行cql命令的工具
from langchain_core.tools import tool
@tool(
    name_or_callable="execute_cypher",
    description="""
        Task:Generate Cypher statement to query a graph database.
        Instructions:
        Use only the provided relationship types and properties in the schema.
        Do not use any other relationship types or properties that are not provided.
        数据库的信息定义如下：
        # 节点标签及含义
        | 节点标签     | 含义             |
        |--------------|------------------|
        | Disease      | 疾病（核心节点） |
        | Symptom      | 症状             |
        | Check        | 检查项目         |
        | Cureway      | 治疗方式         |
        | Drug         | 药物             |
        | Department   | 就诊科室         |
        | Food         | 食物             |
        | Dishes       | 菜肴             |
        | Category     | 疾病分类         |
        
        # 关系类型及含义
        | 关系类型             | 含义              | 起始节点 | 目标节点    |
        |----------------------|-------------------|----------|-------------|
        | DISEASE_SYMPTOM      | 疾病症状          | Disease  | Symptom     |
        | DISEASE_CHECK        | 相关检查项目      | Disease  | Check       |
        | DISEASE_CUREWAY      | 治疗方式          | Disease  | Cureway     |
        | DISEASE_DRUG         | 治疗或相关药物    | Disease  | Drug        |
        | DISEASE_DEPARTMENT   | 就诊科室          | Disease  | Department  |
        | DISEASE_DO_EAT       | 推荐进食的食物    | Disease  | Food        |
        | DISEASE_NOT_EAT      | 不推荐进食的食物  | Disease  | Food        |
        | DISEASE_DISHES       | 适合疾病的菜肴    | Disease  | Dishes      |
        | DISEASE_ACOMPANY     | 并发症 / 伴随疾病 | Disease  | Disease     |
        | DISEASE_CATEGORY     | 疾病所属类别      | Disease  | Category    |
        
        # 查询示例
        # 问：高血压有哪些症状？
        MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_SYMPTOM]->(s:Symptom) RETURN s.name AS symptom
        
        # 问：感冒吃什么药？
        MATCH (d:Disease {{name:"感冒"}})-[:DISEASE_DRUG]->(dr:Drug) RETURN dr.name AS drug
        
        # 问：糖尿病不宜吃什么？
        MATCH (d:Disease {{name:"糖尿病"}})-[:DISEASE_NOT_EAT]->(f:Food) RETURN f.name AS food
        
        # 问：肺炎需要做什么检查？
        MATCH (d:Disease {{name:"肺炎"}})-[:DISEASE_CHECK]->(c:Check) RETURN c.name AS check_item
        
        # 问：高血压挂什么科？
        MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_DEPARTMENT]->(dep:Department) RETURN dep.name AS department
        
        # 问：感冒的并发症有哪些？
        MATCH (d:Disease {{name:"感冒"}})-[:DISEASE_ACOMPANY]->(a:Disease) RETURN a.name AS complication
        
        # 问：糖尿病属于哪类疾病？
        MATCH (d:Disease {{name:"糖尿病"}})-[:DISEASE_CATEGORY]->(c:Category) RETURN c.name AS category
        
        # 问：高血压可以吃什么菜？
        MATCH (d:Disease {{name:"高血压"}})-[:DISEASE_DISHES]->(dishes:Dishes) RETURN dishes.name AS dishes
        
        # 问：哪些疾病会有头痛症状？
        MATCH (d:Disease)-[:DISEASE_SYMPTOM]->(s:Symptom {{name:"头痛"}}) RETURN d.name AS disease
        
        Note: Do not include any explanations or apologies in your responses.
        Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
        Do not include any text except the generated Cypher statement.
        
        参数：
            cql: 查询命令
    """,
)
def execute_cypher(cql: str) -> dict:
    result = conn.query(cql)
    print(f"执行cql命令结果：\n{result}")
    return {"result": result}

# 创建查询天气的工具
import requests
@tool(
    name_or_callable="get_weather",
    description="""
        当用户需要查询某个城市的天气时，调用此工具
        参数：
            city：字符串类型，表示城市名称
    """
)
def get_weather(city:str):
    print(f"查询天气的城市：{city}")
    # 引入天气查询接口 --- 第三方api【高德、心知】
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "key": "be2c23df0824437362ed4948ecfb50d9",
        "city": city,
    }
    # 通过requests发送get请求
    result = requests.get(url=url, params=params)
    result = result.json()
    # 拼接天气数据
    live = result["lives"][0]
    return {
        "result": (
            f"{live['province']}{live['city']}当前天气{live['weather']}，"
            f"气温{live['temperature_float']}℃，湿度{live['humidity_float']}%，"
            f"{live['winddirection']}风{live['windpower']}级，"
            f"数据更新时间为{live['reporttime']}。"
        )
    }

# 模型绑定工具
llm = llm.bind_tools(tools=[execute_cypher, get_weather])

# 问题
que = "抑郁症的症状有哪些？"

# 意图识别，选择工具
result = llm.invoke(que)
print(f"意图识别结果：\n{result}")

# 保存
messages = [result]

# 获取工具结果，执行工具
for tool_call in messages[0].tool_calls:
    tool_result = eval(tool_call['name']).invoke(tool_call)
    print(f"工具调用结果：\n{tool_result}")
    messages.append(tool_result)

# 调用大模型，返回最终回复
result = llm.invoke(messages)
print(f"最终回复：\n{result.content}")
```

# 五、智能体

### 1. 构建智能体

报错：

```
ImportError: cannot import name 'ExecutionInfo' from 'langgraph.runtime' (D:\anaconda3\envs\langchain_env\Lib\site-packages\langgraph\runtime.py)
```

解决：

```
pip install langgraph-prebuilt==1.0.8
```

普通智能体：

```python
from langchain.agents import create_agent

# 加载大模型
from langchain_openai import ChatOpenAI
import os
llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

# 创建智能体对象
agent = create_agent(
    model=llm,
    # 系统提示词
    system_prompt="你是一个有用的助手，可以帮助用户解决各种问题。",
    # 工具列表
    tools=[],
    # 打印信息
    debug=True,
)

# 调用智能体对象 -- 普通输出
# result = agent.invoke({"input":"你好，今天成都的天气怎么样？"})
# result = agent.invoke({"message": [{"role": "user", "content": "你好，今天成都的天气怎么样？"}]})
# print(result)

# 调用智能体对象 -- 流式输出
def agent_stream(que):
    for chunk in agent.stream({"messages": [{"role": "user", "content": que}]}, stream_mode="messages"):
        l = chunk[0].content
        yield l

for i in agent_stream("你好，介绍一下重庆？"):
    print(i,end="",flush=True)
```

### 3. agent注册工具

```python
# 调用工具
from Load.LoadTools import get_weather, execute_cypher

# 加载大模型
from langchain_openai import ChatOpenAI
import os
llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

# 创建智能体对象
from langchain.agents import create_agent
agent = create_agent(
    model=llm,
    # 系统提示词
    system_prompt="""你是一个智能助手，能够根据用户问题选择合适的处理方式。

    ## 工具使用规则
    1. **天气查询**：当用户询问天气相关信息（如"今天北京天气怎么样"、"明天会下雨吗"）时，必须调用 `get_weather` 工具获取实时数据，不要自行编造天气信息。
    2. **医疗信息查询**：当用户询问医疗、健康、疾病、药品、症状、医院等相关信息时，必须调用 `execute_cypher` 工具从知识库中检索，不要凭记忆回答医疗问题。
    3. **其他问题**：对于不属于上述两类的普通问题（如闲聊、常识、写作、翻译等），直接生成回复，不要调用任何工具。

    ## 注意事项
    - 每次只选择最匹配的一个工具，不要同时调用多个工具。
    - 如果用户的问题模糊，无法判断是否需要工具，优先直接回复并引导用户澄清。
    - 工具返回的结果需要你用自然语言整理后回复给用户，不要直接输出原始数据。""",
    # 工具列表
    tools=[get_weather, execute_cypher],
    # 打印信息
    debug=True,
)

# 调用智能体对象 -- 普通输出
# print(agent.invoke({"messages": [{"role": "user", "content": "重庆天气如何"}]}))
# print("-*-"*20)
# print(agent.invoke({"messages": [{"role": "user", "content": "抑郁症的介绍"}]}))
# print("-*-"*20)
# print(agent.invoke({"messages": [{"role": "user", "content": "你好，感觉今天如何"}]}))

# 提取回答
que = "重庆天气如何"
result = agent.invoke({"messages": [{"role": "user", "content": que}]})
msg = result["messages"]
data = []
for i in msg:
    data.append(i.content)
print(data)
print(data[-1])
```

