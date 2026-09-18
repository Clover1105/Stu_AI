from langchain.agents import create_agent
from langchain_core.messages import AIMessage,HumanMessage
from model import my_model

from langGraph_demo.demo03.state.email_state03 import EmailState
import json

# 创建大模型
model = my_model.MyModel.get_local_model()

# 创建提示词
prompt = """
-- 角色：
    你是一个专业的路由智能体，根据用户的输入，选择调用合适的节点，并且返回节点的名称和置信度
-- 任务：
    根据用户的输入，选择调用合适的节点，并且返回节点的名称和置信度
    只要用户提到‘发邮件’、‘通知’、‘写信’等和邮件相关的关键词，哪怕收件人写得不规范（比如只写了名字或数字），也必须强制分类为 internet 节点（或你的邮件查询节点），不要当成闲聊
-- 规则：
    节点名称必须是: chat_node, internet_node 其中一个
    执行度根据问题和智能体的匹配程度来判断，置信度必须是0.00-1.00（开区间）之间，保留2位小数
-- 输出格式:
    输出必须是 {"node":"节点名称","confidence":置信度}，不能输出其他任何解释或说明性文字
"""

# 创建工具
tools = []

# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    middleware=[]
)

def routeAgent_node(state:EmailState):
    print("\n【测试】这里是routeAgent_node03.py")
    # print(f"【测试】接收到的state：{state}")
    que_msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    result = agent.invoke(que_msg)
    # print(f"【测试】大模型回复结果：{result}")
    data = result["messages"][-1].content
    # print(f"【测试】大模型回复结果data：{data}")
    json_data = json.loads(data)
    print(f"【测试】将大模型回复结果转为字典类型：{json_data}")
    # 定义AI返回的内容
    ai_msg = f"\n路由智能体意图识别成功：\n - 选择节点：{json_data['node']}\n - 置信度：{json_data['confidence']}"
    if json_data["node"] == "chat_node":
        return {
            "messages": [AIMessage(content=ai_msg)],
            "result": "路由智能体意图识别成功",
            "next_step": "chat",
            "confidence": json_data["confidence"],
            "agent_name": json_data["node"]
        }
    else:
        return {
            "messages": [AIMessage(content=ai_msg)],
            "result": "路由智能体意图识别成功",
            "next_step": "internet",
            "confidence": json_data["confidence"],
            "agent_name": json_data["node"]
        }




# if __name__ == '__main__':
#     que = EmailState({'messages': [HumanMessage(content='给year发送一封邮件，通知开学了', additional_kwargs={}, response_metadata={})]})
#     print(routeAgent_node(que))
    # que = "我要给李四发一封邮件，通知他开会"
    # print(routeAgent_node(que))
    # que = "你好，变量是什么"
    # print(routeAgent_node(que))


