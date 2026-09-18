from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool

"""创建智能体步骤"""
def create_email_agent(que):
    # 1. 创建一个大模型
    model = my_model.MyModel.get_local_model()
    # 2. 创建一个工具
    tools = [SendEmailTool,AddTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
    """
    try:
        # 限制模型访问次数
        model_limit = ModelCallLimitMiddleware(
            thread_limit=1, # 限制次数
            exit_behavior="end",    # 达到限制次数后，结束对话
        )
        # 4. 创建智能体
        agent = create_agent(
            model, tools,
            system_prompt=prompt,
            middleware=[model_limit],
            debug=True  # 可选，一般用于调试，生成环境必须设置为false
        )
    except Exception as e:
        print(f"模型访问次数限制:{e}")
        return "模型访问次数限制"
    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content
    print(data)
    return data

if __name__ == '__main__':
    que = "请发送一封邮件给2920242909@qq.com，内容歌手王源的歌的4句歌词"
    r = create_email_agent(que)
    print(f"最终的:{r}")