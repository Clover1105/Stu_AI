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
    session_manager = SessionManager("001",1)

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
    print("=== 开始测试用户画像记忆 ===\n")

    # --- 第一阶段：输入信息（写入记忆）---
    print(">>> 步骤1：告诉AI你的信息...")

    # 1. 输入姓名和年龄
    q1 = "我叫Roy，今年26岁"
    print(f"用户输入: {q1}")
    create_email_agent(q1)

    # 2. 输入职业和爱好
    q2 = "我是一名歌手，平时喜欢唱歌和滑雪"
    print(f"用户输入: {q2}")
    create_email_agent(q2)

    print("\n--- 记忆已更新，开始验证 ---\n")

    # --- 第二阶段：验证回忆（读取记忆）---
    print(">>> 步骤2：询问AI刚才的信息...")

    # 3. 验证姓名
    q3 = "我叫什么名字？"
    print(f"用户输入: {q3}")
    create_email_agent(q3)

    # 4. 验证职业
    q4 = "我的职业是什么？"
    print(f"用户输入: {q4}")
    create_email_agent(q4)

    # 5. 验证爱好
    q5 = "我平时喜欢做什么？"
    print(f"用户输入: {q5}")
    create_email_agent(q5)

    print("\n=== 测试结束 ===")
