from langgraph.checkpoint.memory import InMemorySaver  # 需要导入检查点
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_core.messages import HumanMessage
from langgraph.types import Command

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool

"""创建智能体步骤"""
def create_email_agent(que):
    # 1. 创建一个大模型
    model = my_model.MyModel.get_local_model()
    # 2. 创建一个工具
    tools = [SendEmailTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
    """

    # 人工审核
    try:
        # 定义人工审核中间件
        hum_middleware = HumanInTheLoopMiddleware(
            # 拦截点，拦截哪些工具
            interrupt_on={
                "send_email_tool":{
                    "allowed_decisions": ["approve", "reject", "edit"],  # 允许的操作：批准、拒绝、编辑
                    "description": "邮件发送需要人工审核，请确认邮件内容是否正确",  # 自定义提示
                }
            },
            description_prefix="【人工审核】"  # 公共提示前缀，可选
        )
        # 定义检查点
        memory = InMemorySaver()

        # 4. 创建智能体
        agent = create_agent(
            model, tools,
            system_prompt=prompt,
            middleware=[hum_middleware],
            checkpointer=memory,    # 记录智能体运行状态信息
            debug=True  # 可选，一般用于调试，生成环境必须设置为false
        )
    except Exception as e:
        print(f"人工审核:限制模型访问次数失败{e}")
        return "限制模型访问次数失败"
    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    config = {'configurable':{'thread_id':"1"}}
    result = agent.invoke(human_msg,config)    # 非流式输出
    print(f"原始的回答：{result}")
    # 模拟界面输入??????
    d = result["__interrupt__"]
    if d:
        print("请选择操作：")
        print("   1. approve - 批准发送")
        print("   2. edit - 编辑内容后发送")
        print("   3. reject - 拒绝发送")
        choice = input("请输入你的选择：")
        if choice == "1":
            print("批准发送邮件")
            data = agent.invoke(Command(
                resume={
                    "decisions": [
                        {"type": "approve"}
                    ]
                }
            ), config)
            print(data["messages"][-1].content)
        elif choice == "2":
            print("请输入编辑内容")
            to = input("请输入收件人邮箱：")
            subject = input("请输入标题")
            content = input("请输入内容")
            # 构建一个修改后的工具参数对象
            p = {
                "to": to,
                "subject": subject,
                "content": content
            }
            # 发送邮件
            data = agent.invoke(Command(
                resume={
                    "decisions": [
                        {"type": "edit", "edited_action": {
                            "name": "send_email_tool",
                            "args": p
                        }}
                    ]
                }
            ), config)
            print(data["messages"][-1].content)
        else:
            print("拒绝发送邮件")
            reason = input("请输入拒绝理由")
            data = agent.invoke(Command(
                resume={
                    "decisions": [
                        {"type": "reject", "reason": reason}
                    ]
                }
            ), config)
            print(data)
            print(data["messages"][-1].content)
    else:
        print("模型不支持")
        return "模型不支持"
    return data


if __name__ == '__main__':
    que = "请发送一封邮件给2920242909@qq.com，内容歌手王源的歌的4句歌词"
    r = create_email_agent(que)
    print(r)