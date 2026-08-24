import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen3.7-max-preview",
        streaming=True,
    )

message = [
    {"role":"system","content":"你是一个专业的自然语言处理（NLP）知识图谱构建专家。你的任务是从给定的非结构化文本中，精准抽取实体及其关系，输出格式严格为标准的三元组（Subject, Predicate, Object）的列表形式输出。若句子中不存在有效三元组，则返回空列表[]。不要包含任何额外解释或无关内容。"},
    {"role":"user","content":'抽取的内容按照{竞赛名称：[主办方，承办方，时间]}这个格式，数据内容为：'
        '2022年的语言与智能技术竞赛由中国中文信息学会和中国计算机学会联合主办，'
        '百度公司、中国中文信息学会评测工作委员会和中国计算机学会自然语言处理专委会承办，'
        '已连续举办4届，成为全球最热门的中文NLP赛事之一。'},
    # {"role":"user","content":"1949年中国成立了吗？"}
]

result = llm.invoke(message)
print(result.content)
