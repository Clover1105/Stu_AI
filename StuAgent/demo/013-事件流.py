import asyncio

from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool

"""创建智能体步骤"""
async def create_email_agent(que):
    # 1. 创建一个大模型
    model = my_model.MyModel.get_model()
    # 2. 创建一个工具
    tools = [SendEmailTool,AddTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
        -- 约束：
            1. 当用户要求发送邮件时，只调用一次 send_email_tool。
            2. 工具返回成功后，直接告诉用户发送完成，不要再次调用工具。
            3. 严禁重复执行相同的操作。
    """
    # 4. 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        # debug=True  # 可选，一般用于调试，生成环境必须设置为false
    )
    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    async for event in agent.astream_events(human_msg,version="v2"):
        print(event)
        # 获取事件内容
        event_name = event['event'] # 事件名称
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
            if tool_name == "send_email_tool":
                yield f"开始发送邮件。。。\n\n"
        elif event_name == 'on_tool_end':
            # 获取工具返回值
            tool_output = event['data']['output'].content
            yield f"邮件工具执行完毕，执行结果为{tool_output}\n\n"
        elif event_name == 'on_chat_model_stream':
            data = event['data']['chunk'].content
            if data:
                yield data

# 创建一个迭代器
async def test(que):
    async for rs in create_email_agent(que):
        print(rs,end="")

if __name__ == '__main__':
    que = "请发送一封邮件给2920242909@qq.com，内容为一段心灵鸡汤"
    asyncio.run(test(que))