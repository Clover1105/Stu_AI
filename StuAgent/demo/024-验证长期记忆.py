from langchain_core.messages import HumanMessage, SystemMessage

from model import my_model
from langchain.agents import create_agent

from memory.manager.session_manager import SessionManager
from memory.manager.memory_manager import MemoryManager

# 创建一个大模型
model = my_model.MyModel.get_model()

# 创建一个工具
tools = []

"""创建智能体步骤"""
def create_email_agent(que):
    # 创建会话管理器
    session_manager = SessionManager("001")

    # 创建一个窗口记忆
    session_manager.save_window_memory("user", que)

    # 更新记忆
    memory_manager = MemoryManager(session_manager)
    memory_manager.update(1, que)

    # 构建记忆的提示词
    memory_prompt = session_manager.builder_prompt(1, que)

    # 创建提示词 -- 系统提示词
    prompt = f"""
    	-- 角色：你是一个专业的聊天助手
    	-- 任务：
    	    - 理解用户问题，回答用户问题
    	-- 规则：
    	    - 你只需要回答用户问题，回复内容不需要每次携带记忆内容
    	    - 请严格根据以下【用户记忆】来回答用户的问题，如果记忆中有答案，请直接回答：

        【用户记忆】：
        {memory_prompt['content']}
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=False,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que),
        SystemMessage(content=prompt),
    ]}

    # 回答
    result = agent.invoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    # 存储AI回复内容
    session_manager.save_window_memory("assistant", data)

    print(data)
    return data


if __name__ == '__main__':
    q1 = "我叫张三，今年23岁"
    q2 = "我擅长python"
    q3 = "我在学习langchain"
    q4 = "我在学习什么"
    q5 = "我擅长什么"
    # for q in [q1, q2, q3]:
    #     print("---------------------")
    #     create_email_agent(q)
    create_email_agent(q5)
