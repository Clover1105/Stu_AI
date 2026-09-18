from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo02.state.email_state02 import EmailState
from langGraph_demo.demo02.node.email_node02 import email_node
from langGraph_demo.demo02.node.query_node02 import query_node
from langGraph_demo.demo02.node.internet_node02 import internet_node
from langGraph_demo.demo02.node.condiyion_node02 import query_router

"""
创建一个大脑或智能体
"""

def email_agent():
    print("\n【测试】这里是email_agent02.py")
    # 获取图形结果
    graph = StateGraph(EmailState)
    print(f"【测试】获取图形结果：{graph}")
    # 顺序图添加
    print("【测试】意图识别节点")
    graph.add_node("internet",internet_node)
    print("【测试】查询节点")
    graph.add_node("query",query_node)
    print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # 画边
    # 新版入口
    print("【测试】开始 --》意图识别")
    graph.add_edge(START,"internet")
    # 旧版入口
    # graph.set_entry_point("internet")
    print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")

    # 添加条件边
    print("【测试】查询 --》结束")
    graph.add_conditional_edges("query",query_router,{"a":"email","b":END})

    # print("【测试】查询 --》邮件")
    # graph.add_edge("query", "email")
    # print("【测试】邮件 --》结束")
    # graph.add_edge("email", END)
    # 编译
    agent = graph.compile(debug=True)
    print(f"【测试】编译结果：{agent}")
    return agent