from langchain_openai import ChatOpenAI
import os

chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.7-max",
)

# 输入问题
contant = input("请输入内容：\n")
# 模拟上下文
words = "重庆三峡学院正式更名为重庆三峡科技大学"
# 拼接
contant = "请根据上下文：\n" + words + "回答问题：\n" + contant

messages = [
    {"role": "system", "content": "你是一个专业的学校百科全书，什么都知道"},
    {"role": "user", "content": contant}]

response = chatLLM.invoke(messages)
# print(response.model_dump_json())   # 返回的是json格式
print(response.content) # 只返回文本内容