import re
from langchain.agents.middleware import before_model, AgentState, after_model
from langchain_core.messages import AIMessage
from langgraph.runtime import Runtime

"""
过滤黄，赌，毒信息
"""
@before_model
def WordFilterMiddleware(state:AgentState,time:Runtime):
    print("验证是否在模型调用之前执行")
    print(state)
    # 用户问题
    que = state["messages"][0].content
    # 查询数据库或者查询外部文件
    word_list = ["赌博","嫖娼","吸毒"]
    for w in word_list:
        if w in que:
            raise ValueError(f"问题中内容包含敏感词{w}，不允许生成")
    return time

@after_model
def WordPingMiddleware(state:AgentState,time:Runtime):
    print("验证是否在模型调用之后执行")
    print(state)
    # AI回复内容
    ai_msg = state["messages"][1].content
    # 查询数据库或者查询外部文件
    word_list = ["赌博","嫖娼","吸毒"]
    change_msg = ai_msg
    for w in word_list:
        if w in change_msg:
            # 获取过滤内容
            change_msg = re.sub(w,"$$$",change_msg)
    if change_msg != ai_msg:
        return {
            "messages": [AIMessage(content=change_msg)]
        }
    # 没有任何修改
    return {}