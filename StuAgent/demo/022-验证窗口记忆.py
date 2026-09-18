from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

# 创建提示词 -- 系统提示词
prompt = """
	-- 角色：你是一个专业的聊天助手
"""

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[]
)

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("1")
    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)
    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt()

    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que),memory_prompt]}
    # 6. 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)
    print(data)
    return data


if __name__ == '__main__':
    q1 = "我叫张三，今年23岁"
    q2 = "我喜欢打篮球"
    q3 = "我在学习langchain"
    q4 = "我在学习什么"
    q5 = "我是谁，今年多大了"
    create_email_agent(q2)