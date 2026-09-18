"""
作业：完成基于langGraph的条件图：
要求：
        基于上一次作业，改造路由智能体成一个意图识别节点，定义一个基于本地大模型的聊天节点，完成以下功能
        通过用户不同问题，找到不同节点
      例如：
             问题一：给王五你发个邮件，说今晚开会
             AI：调用上课讲的基于langGraph的邮件智能体
             问题而 ：你好，什么是python
             AI：调用 基于本地大模型的聊天节点 完成对象

提交作业到邮箱里，提交内容是：graph 代码和 条件图
"""

from langchain_core.messages import HumanMessage
from langGraph_demo.demo_homework.graph.langGraph_agent import langGraph_agent

import asyncio
async def test():
    print(f"\n【测试】这里是 -- 测试条件图.py")
    graph = langGraph_agent()
    print(f"\n【测试】这里是 -- 测试条件图.py")
    # print(f"【测试】获取路由智能体结果：{graph}")
    # input = {"messages":[HumanMessage(content="你好，什么是python")]}
    input = {"messages": [HumanMessage(content="给year发送一首诗词")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content


# 画流程图
def draw_graph():
    agent = langGraph_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("条件图.png","wb") as f:
        f.write(data)



if __name__ == '__main__':
    # draw_graph()
    async def t():
        print("*-*-"*40)
        async for rs in test():
            print(rs,end="")
    asyncio.run(t())