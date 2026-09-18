from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool
from middleware.word_filter_middleware import WordFilterMiddleware, WordPingMiddleware


# 1. 创建一个大模型
model = my_model.MyModel.get_model()
# 2. 创建一个工具
tools = [SendEmailTool,AddTool]
# 3. 创建提示词 -- 系统提示词
prompt = """
    -- 角色：你是一个专业的聊天助手
"""
# 4. 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[WordPingMiddleware,WordFilterMiddleware]
)

"""创建智能体步骤"""
def create_email_agent(que):

    try:
        # 5. 提问
        human_msg = {"messages":[HumanMessage(content=que)]}
        # 6. 回答
        result = agent.invoke(human_msg)    # 非流式输出
        data = result["messages"][-1].content
        print(data)
        return data
    except Exception as e:
        print(f"敏感词过滤报错:{e}")
        return "敏感词过滤报错"

if __name__ == '__main__':
    que = "中国严令禁止的事情，5个"
    create_email_agent(que)