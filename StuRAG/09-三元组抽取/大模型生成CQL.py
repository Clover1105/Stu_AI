import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

message = [
    {"role":"system","content":"请根据用户的问题内容，生成CQL查询语句。"},
    {"role":"user","content":"请根据一下内容生成对应的CQL语句："
                             "[{'竞赛名称': [{'text': '语言与智能技术竞赛', 'start': 6, 'end': 15, 'probability': 0.6310065965976648, "
                             "'relations': {'主办方': [{'text': '中国计算机学会', 'start': 25, 'end': 32, 'probability': 0.7511016583800938}, "
                             "{'text': '中国中文信息学会', 'start': 16, 'end': 24, 'probability': 0.8484645105804987}], "
                             "'承办方': [{'text': '百度公司', 'start': 37, 'end': 41, 'probability': 0.8332406110869108}, "
                             "{'text': '中国计算机学会自然语言处理专委会', 'start': 58, 'end': 74, 'probability': 0.6294969648882613}, "
                             "{'text': '中国中文信息学会评测工作委员会', 'start': 42, 'end': 57, 'probability': 0.7172121474980742}], "
                             "'时间': [{'text': '2022年', 'start': 0, 'end': 5, 'probability': 0.9482227255116413}]}}]}]"}
]

result = llm.invoke(message)
print(result.content)

