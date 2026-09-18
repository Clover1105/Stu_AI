from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo04.state.email_state04 import EmailState
from langGraph_demo.demo04.node.email_node04 import email_node
from langGraph_demo.demo04.node.query_node04 import query_node
from langGraph_demo.demo04.node.internet_node04 import internet_node
from langGraph_demo.demo04.node.manager_node04 import manager_node

"""
创建一个大脑或智能体
"""

def langGraph_agent():
    print("\n【测试】这里是langGraph_agent04.py")

    # 获取图形结果 -- 创建一个空的“流程图”骨架，并规定了这个流程图中所有节点必须遵守的“数据规范”
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")

    # 顺序图添加
    # print("【测试】意图识别节点")
    graph.add_node("internet", internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # print("【测试】主管节点")
    graph.add_node("manager", manager_node)

    # 画边
    # print("【测试】开始 --》主管")
    graph.add_edge(START, "manager")

    graph.add_edge("internet","manager")
    graph.add_edge("query", "manager")
    graph.add_edge("email", "manager")


    # 编译
    agent = graph.compile()
    # print(f"【测试】编译结果：{agent}")
    return agent