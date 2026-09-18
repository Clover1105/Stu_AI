import asyncio
from langchain_core.messages import HumanMessage
from model import my_model
from langchain.agents import create_agent
from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool
from prompt.builder_prompt_yaml import BuilderPromptYaml

"""创建智能体步骤"""
async def send_email_agent(que):
    # 1. 创建一个大模型
    model = my_model.MyModel.get_model()
    # 2. 创建一个工具
    tools = [SendEmailTool,AddTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = BuilderPromptYaml.get_prompt("send_email_agent.yaml")
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
    que = "1+2等于多少？"
    # que = "请发送一封邮件给2920242909@qq.com"
    # 异步调用
    asyncio.run(send_email_agent(que))