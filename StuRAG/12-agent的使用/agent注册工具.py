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
