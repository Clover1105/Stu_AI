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