# 2026年9月2日作业

import asyncio
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from tool.query_employee_tool import QueryEmployeeTool
from tool.send_email_tool import SendEmailTool
from model.my_model import MyModel
from prompt.builder_prompt_yaml import BuilderPromptYaml


# 创建大模型
model = MyModel.get_model()

# 创建工具 -- 查询员工信息、发送邮件
tool = [QueryEmployeeTool,SendEmailTool]

# 创建提示词
prompt = BuilderPromptYaml.get_prompt("send_email_agent.yaml")

# 创建摘要提示词
summary_prompt = """
    1. 角色：你是一个摘要记忆助手
    2. 任务：
        - 请根据下面提供的历史对话生成摘要
        - 务必保留对话中提到的所有关键实体信息，如ID、人名、邮箱、部门等。
        - 务必清晰记录已成功执行的操作及其结果。
        - 历史对话：{messages}        
"""

# 创建摘要中间件
summary = SummarizationMiddleware(
    model=model,
    trigger=[
        {"tokens":40,"messages":6},
        # {"tokens":3000,"messages":15}
    ],  # 当token达到10个触发摘要，生成环境建议3000
    keep=("messages",4),    # 保留最近6条对话（一问一答算两条），生成环境建议保留20以上
    summary_prompt=summary_prompt,  # 可选
    trim_tokens_to_summarize=4000,  # 可选，摘要总结的摘要信息限制在4000token
)

# 创建内存记忆检查点
memory = InMemorySaver()

# 创建智能体
agent = create_agent(
    model=model, tools=tool,
    system_prompt=prompt,
    # debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[summary],    # 中间件配置
    checkpointer=memory
)

async def SendEmailAgent(que):
    # 提问
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 构建记忆配置
    config = {"configurable": {"thread_id": "3"}}
    # 回答
    async for event in agent.astream_events(human_msg, version="v2",config=config):
        # print(event)
        # 获取事件内容
        event_name = event['event']  # 事件名称
        if event_name == 'on_chain_start':
            yield f"邮件智能体开始运行。。。\n\n"
        elif event_name == 'on_chain_end':
            yield f"邮件智能体停止运行！！！\n\n"
        elif event_name == 'on_chat_model_start':
            yield f"大模型开始思考。。。\n\n"
        elif event_name == 'on_chat_model_end':
            yield f"大模型思考结束！！！\n\n"
        elif event_name == 'on_chain_stream':
            yield f"大模型开始生成答案。。。\n\n"
        elif event_name == 'on_tool_start':
            # 获取工具名称
            tool_name = event['name']
            if tool_name == "QueryEmployeeTool":
                yield f"开始查询员工信息。。。\n\n"
            if tool_name == "SendEmailTool":
                yield f"开始发送邮件。。。\n\n"
        elif event_name == 'on_tool_end':
            # 获取工具返回值
            tool_output = event['data']['output'].content
            yield f"邮件工具执行完毕，执行结果为{tool_output}\n\n"
        elif event_name == 'on_chat_model_stream':
            data = event['data']['chunk'].content
            if data:
                yield data

# 创建迭代器
async def test(que):
    async for rs in SendEmailAgent(que):
        print(rs,end="")


async def main():
    # 所有对话都在同一个事件循环中进行
    for i in range(len(que)):
        print("*-" * 50)
        print(f"第{i + 1}次提问：{que[i]}")
        await test(que[i])  # 使用 await 而不是 asyncio.run
        print("\n" + "*-" * 50)

if __name__ == '__main__':
    # que = "通知4，明天上午来上课"
    # asyncio.run(test(que))
    que = [
        "通知yang，明天上午来上课",
        "你好，我是year",
        "帮我写一个100字的卖油翁课程的大纲",
        "请把课程大纲发送到我的邮箱里"
    ]
    asyncio.run(main())

