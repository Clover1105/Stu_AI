from Load import LangChainNeo4jUtil

conn = LangChainNeo4jUtil.get_neo4j_conn()

import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

message = [
    {"role":"system","content":"你是一个专业的图数据库查询专家。请根据用户的问题，基于给定的数据库模式生成对应的Cypher查询语句(CQL)。"
                               "数据库包含以下节点和关系：竞赛名称节点(属性:name, probability)、机构节点(属性:name, probability)、"
                               "时间节点(属性:name, probability)；关系包括:主办方、承办方、举办时间。只回复CQL语句，不要包含任何解释、"
                               "Markdown标记或多余文字。"},
    {"role":"user","content":"帮我生成查询语言与智能技术竞赛的所有相关内容的cql语句"}
]

result = llm.invoke(message)
print(result.content)
# MATCH (c:竞赛名称 {name: '语言与智能技术竞赛'})-[r]-(n) RETURN c, r, n