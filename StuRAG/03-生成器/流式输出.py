from langchain_openai import ChatOpenAI
import os

chatLLM = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3.7-max",
    # 流式输出
    streaming=True,
)

contant = input("请输入内容：\n")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": contant}]

# stream方法：调用LLM生成回复、流式输出结果
for chunk in chatLLM.stream(messages):
    print(chunk.content, end="", flush=True)
