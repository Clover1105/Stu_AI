from langchain_core.messages import HumanMessage
from langGraph_demo.demo01.graph.email_agent01 import email_agent
from langgraph.checkpoint.memory import InMemorySaver
import asyncio
from langgraph.types import Command

print(f"\n【测试】这里是01-测试顺序图.py")
memory = InMemorySaver()
graph = email_agent(memory)
# print(f"【测试】获取邮件智能体结果：{graph}")

# 添加记忆配置
config = {"configurable": {"thread_id": 1}}

async def test01():
    print(f"\n【测试】这里是01-测试顺序图.py")
    # print(f"【测试】获取邮件智能体结果：{graph}")
    input = {"messages":[HumanMessage(content="给year发送一封邮件，通知开学了")]}
    async for chunk,metadate in graph.astream(input, config, stream_mode="messages"):
        yield chunk.content

# 人工审核 -- 修改
def test_edit():
    async def test():
        print("修改：","*-*-" * 40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())
    #获取拦截的节点信息
    state = graph.get_state(config)
    print(state)
    info = input("请输入修改的邮件内容：\n")
    graph.update_state(config,{"content": info})
    #继续执行
    rs = graph.invoke(None, config)
    print(rs['messages'][-1].content)

# 人工审核-批准
def test_approve():
    async def test():
        print("批准：","*-*-" * 40)
        async for rs in test01():
            print(rs,end="")
    asyncio.run(test())
    #获取拦截的节点信息
    state = graph.get_state(config)
    print(state)
    info = input("请输入批准或者拒绝（y/n）：")
    if info =="y":
        # 继续执行
        rs = graph.invoke(None, config)
        print(rs['messages'][-1].content)
    else:
        #拒绝
        graph.invoke(Command(goto="cancel"),config)
        print("邮件发送取消")


if __name__ == '__main__':
    # test_edit()
    test_approve()