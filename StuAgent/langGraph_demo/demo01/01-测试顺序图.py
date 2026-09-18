from langchain_core.messages import HumanMessage
from langGraph_demo.demo01.graph.email_agent01 import email_agent

import asyncio
async def test01():
    print(f"\n【测试】这里是01-测试顺序图.py")
    graph = email_agent()
    print(f"\n【测试】这里是01-测试顺序图.py")
    print(f"【测试】获取邮件智能体结果：{graph}")
    input = {"messages":[HumanMessage(content="给year发送一封邮件，通知开学了")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content



# 画流程图
def draw_graph():
    agent = email_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("顺序图.png","wb") as f:
        f.write(data)



if __name__ == '__main__':
    # draw_graph()
    async def test():
        print("*-*-"*40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())