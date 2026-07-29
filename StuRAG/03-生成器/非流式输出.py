from langchain_openai import ChatOpenAI
import os

chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.7-max",
)

contant = input("请输入内容：\n")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": contant}]
response = chatLLM.invoke(messages)
# print(response.model_dump_json())   # 返回的是json格式
print(response.content) # 只返回文本内容