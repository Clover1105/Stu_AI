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



