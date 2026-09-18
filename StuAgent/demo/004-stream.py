from langchain_core.messages import HumanMessage

from model import MyModel
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool

"""创建智能体步骤"""
def create_email_agent(que):
    # 1. 创建一个大模型
    model = MyModel.MyModel.get_model()
    # 2. 创建一个工具
    tools = [SendEmailTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
    """
    # 4. 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        # debug=True  # 可选，一般用于调试，生成环境必须设置为false
    )
    # 5. 提问
    # 定义一个人类消息类型格式（第一种）
    # human_msg = {"messages":[{"role":"user","content":que}]}
    # 定义一个人类消息类型格式（第二种）
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    # result = agent.invoke(human_msg)    # 非流式输出
    # stream_mode="messages"：大模型返回的消息流
    for c,m in agent.stream(human_msg,stream_mode="messages"):
        if c.content:
            print(c.content,end="")


if __name__ == '__main__':
    # 1967532979@qq.com、3131355723@qq.com、2018561771@qq.com、3010207312@qq.com
    que = "请发送一封邮件给2920242909@qq.com，内容为一段心灵鸡汤"
    create_email_agent(que)