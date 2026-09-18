

from langGraph_demo.demo01.state.email_state01 import EmailState
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import AIMessage

# 响应参数
class InternetResponse(BaseModel):
    name:str = Field(...,description="姓名")
    subject:str = Field(...,description="邮件主题")
    content:str = Field(...,description="邮件内容")

"""
意图识别节点，返回值必须为字典
"""

def internet_node(state:EmailState):
    print("\n【测试】这里是internet_node01.py")
    # print(f"【测试】接收到的state：{state}")
    model = MyModel.get_local_model()
    prompt = """
        -- 角色：你是一个意图识别助手
        -- 任务：
            - 理解用户需求
            - 根据用户问题，提取姓名，邮件主题，邮件内容
        -- 规则：
            - 姓名、邮件主题、邮件内容不能为空
        -- 输出：
            - 输出以下内容：{"name":"xx","subject":"xx","content":"xx"}
        -- 示例：
            - 用户问题：发送邮件给张三，主题是测试，内容是测试邮件内容
            - 输出：{"name":"张三","subject":"测试","content":"测试邮件内容"}
    """
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
        response_format=InternetResponse,
    )
    msg = {"messages":[{"role":"user","content":state["messages"][0].content}]}
    # 获取结果
    rs = agent.invoke(msg)
    # print(f"【测试】大模型回复结果：{rs}")
    # 把结果转换成字典
    json = rs["structured_response"].model_dump()
    print(f"【测试】将回结果转为字典类型：{json}")
    # 定义AI返回的内容
    ai_msg = f"\n意图节点识别成功：\n 姓名：{json['name']}\n 邮件主题：{json['subject']}\n 邮件内容：{json['content']}"
    # 只返回当前节点修改的状态信息
    return {
        "messages":[AIMessage(content=ai_msg)],
        "name":json["name"],
        "subject":json["subject"],
        "content":json["content"],
        "result":"意图识别成功"
    }