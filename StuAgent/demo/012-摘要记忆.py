from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool


# 1. 创建一个大模型
model = my_model.MyModel.get_local_model()

# 2. 创建一个工具
tools = [SendEmailTool,AddTool]

# 3. 创建提示词 -- 系统提示词
prompt = """
    -- 角色：你是一个专业的聊天助手
"""

# 定义摘要提示词
summary_prompt = """
    1. 角色：你是一个摘要记忆助手
    2. 任务：
        - 请根据下面提供的历史对话生成摘要
        - 历史对话：{messages}
    3. 规则：
        - 只提取用户的姓名
"""

# 定义摘要中间件
summary = SummarizationMiddleware(
    model=model,
    trigger=[
        {"tokens":40,"messages":4},
        # {"tokens":3000,"messages":15}
    ],  # 当token达到10个触发摘要，生成环境建议3000
    keep=("messages",2),    # 保留最近1轮的对话，生成环境建议保留20以上
    summary_prompt=summary_prompt,  # 可选
    trim_tokens_to_summarize=4000,  # 可选，摘要总结的摘要信息限制在4000token
)

# 4. 创建内存记忆检查点
memory = InMemorySaver()

# 5. 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    checkpointer=memory,
    # debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[summary]    # 中间件配置
)

def print_memory(thread_id="1"):
    config = {"configurable": {"thread_id": thread_id}}
    state = agent.get_state(config)
    messages = state.values.get("messages", [])
    print("\n================ 当前记忆状态 ================")
    print("消息数量：", len(messages))
    for i, message in enumerate(messages):
        print(f"\n--- Message {i + 1} ---")
        print("类型：", type(message).__name__)
        # 只打印前500个字符，避免输出太长
        content = str(message.content)
        print("内容：")
        print(content[:500])
    print("==============================================\n")


def create_email_agent(que,user_id):
    # 6. 提问
    human_msg = {"messages":[HumanMessage(content=que)]}

    # 7. 构建记忆配置
    config = {'configurable':{'thread_id':user_id}}

    # 8. 回答
    result = agent.invoke(human_msg,config=config)    # 非流式输出
    return result["messages"][-1].content

if __name__ == '__main__':
    que = [
        "1+1等于多少？",
        "我的名字叫张三，我是一名Java程序员。",
        "我今年23岁，目前正在学习LangChain和LangGraph。",
        "10+20等于多少？",
        "我的第一个问题是什么？",  # 测试记忆保留
        "我是谁？多少岁了，目前在学习什么"
    ]
    for i in range(len(que)):
        print(f"第{i+1}次提问：{que[i]}")
        result = create_email_agent(que[i],1)
        print(f"第{i+1}次回答：{result}")
    print("=============打印当前记忆信息=====================")
    print_memory("1")