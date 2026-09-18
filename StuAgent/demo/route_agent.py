from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from model import my_model

# 创建大模型
model = my_model.MyModel.get_local_model()

# 创建提示词
prompt = """
-- 角色：
    你是一个专业的路由智能体，根据用户的输入，返回一个智能体的名称和置信度
-- 规则：
    智能体名称必须是: email_agent ,chat_agent,exam_agent 这三个名称其中一个
    执行度根据问题和智能体的匹配程度来判断，置信度必须是0.00-1.00之间，保留2位小数
-- 输出格式:
    必须是 {"agent":"智能体名称","confidence ":置信度}，不能输出其他任何解释或说明性文字
"""

# 创建工具
tools = []

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    # debug=True,
    middleware=[]
)

def route_agent(que:str):
    human_msg = {"messages":[HumanMessage(content=que)]}
    result = agent.invoke(human_msg)
    data = result["messages"][-1].content
    return data

if __name__ == '__main__':
    que = "我要参加模拟考试"
    print(route_agent(que))
    que = "我要给李四发一封邮件，通知他开会"
    print(route_agent(que))
    que = "你好，变量是什么"
    print(route_agent(que))


