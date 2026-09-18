from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo_homework.state.email_state import EmailState
from langGraph_demo.demo_homework.node.email_node import email_node
from langGraph_demo.demo_homework.node.query_node import query_node
from langGraph_demo.demo_homework.node.routeAgent_node import routeAgent_node
from langGraph_demo.demo_homework.node.condiyion_node import query_router,agent_router
from langGraph_demo.demo_homework.node.chat_node import chat_node
from langGraph_demo.demo_homework.node.internet_node import internet_node

"""
创建一个大脑或智能体
"""

def langGraph_agent():
    print("\n【测试】这里是langGraph_agent.py")

    # 获取图形结果 -- 创建一个空的“流程图”骨架，并规定了这个流程图中所有节点必须遵守的“数据规范”
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")

    # 顺序图添加
    # print("【测试】路由智能体节点")
    graph.add_node("routeAgent",routeAgent_node)
    # print("【测试】聊天节点")
    graph.add_node("chat", chat_node)
    # print("【测试】意图识别节点")
    graph.add_node("internet", internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)

    # 画边
    # print("【测试】开始 --》路由智能体")
    graph.add_edge(START,"routeAgent")

    # 智能体判断普通聊天还是发邮件
    # print("【测试】routeAgent --》聊天/意图识别")
    graph.add_conditional_edges("routeAgent", agent_router, {"chat":"chat","internet":"internet"})

    # 普通聊天
    # print("【测试】聊天 --》结束")
    graph.add_edge("chat", END)

    # 发邮件 -- 查询邮箱
    # print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")
    # print("【测试】查询 --》结束/邮件")
    graph.add_conditional_edges("query",query_router,{"email":"email","end":END})

    # print("【测试】邮件 --》结束")
    graph.add_edge("email", END)

    # 编译
    agent = graph.compile()
    # print(f"【测试】编译结果：{agent}")
    return agent