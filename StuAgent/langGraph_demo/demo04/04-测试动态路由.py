from langchain_core.messages import HumanMessage
from langGraph_demo.demo04.graph.langGraph_agent04 import langGraph_agent

import asyncio
async def test():
    print(f"\n【测试】这里是 -- 04-测试动态路由.py")
    graph = langGraph_agent()
    print(f"\n【测试】这里是 -- 04-测试动态路由.py")
    # print(f"【测试】获取路由智能体结果：{graph}")
    # input = {"messages":[HumanMessage(content="你好，什么是python")]}
    input = {"messages": [HumanMessage(content="给小明发送邮件，通知她放学了")]}
    async for chunk,metadate in graph.astream(input, stream_mode="messages"):
        yield chunk.content


# 画流程图
def draw_graph():
    agent = langGraph_agent()
    # 画图
    data = agent.get_graph().draw_mermaid_png()
    # 展示流程图
    with open("动态路由图.png","wb") as f:
        f.write(data)



if __name__ == '__main__':
    # draw_graph()
    async def t():
        print("*-*-"*40)
        async for rs in test():
            print(rs,end="")
    asyncio.run(t())