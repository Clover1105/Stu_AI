import asyncio
from langchain_core.messages import HumanMessage
from model import MyModel
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool

"""创建智能体步骤"""
async def create_email_agent(que):
    # 1. 创建一个大模型
    model = MyModel.MyModel.get_model()
    # 2. 创建一个工具
    tools = [SendEmailTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        1. 角色：你是一个专业的邮件发送助手
        2. 任务：
            （1）根据用户输入问题发送邮件
        3. 规则：
            （1）你只能根据用户输入问题发送邮件
            （2）如果不是发送邮件的问题，告知用户，只能发送邮件
            （3）如果邮件内容为空，告知用户，邮件为空
            （4）如果邮箱格式不正确，告知用户，邮箱格式不正确
        4. 输出：
            （1）只输出json格式，不能输出其他格式
            （2）json格式如下：{"output":"xxx"}
        5. 示例：
            输入：请解释一下python是什么
            输出：只能发送邮件
            输入：请发送一封邮件给2920242909@qq.com
            输出：邮件内容为空
    """
    # 4. 创建智能体
    agent = create_agent(
        model=model, tools=tools,
        system_prompt=prompt,
        debug=True  # 可选，一般用于调试，生成环境必须设置为false
    )
    # 5. 提问
    # 定义一个人类消息类型格式（第一种）
    # human_msg = {"messages":[{"role":"user","content":que}]}
    # 定义一个人类消息类型格式（第二种）
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    result = await agent.ainvoke(human_msg)    # 非流式输出
    print(f"*-*-*-{result}")
    print(result["messages"][-1].content)



if __name__ == '__main__':
    # 1967532979@qq.com、3131355723@qq.com、2018561771@qq.com、3010207312@qq.com
    # que = "请发送一封邮件给2920242909@qq.com，内容为一段心灵鸡汤"
    que = "今天天气如何"
    # que = "请发送一封邮件给2920242909@qq.com"
    # 异步调用
    asyncio.run(create_email_agent(que))