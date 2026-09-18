from langgraph.graph import StateGraph, START, END
from langGraph_demo.demo01.state.email_state01 import EmailState
from langGraph_demo.demo01.node.email_node01 import email_node
from langGraph_demo.demo01.node.query_node01 import query_node
from langGraph_demo.demo01.node.internet_node01 import internet_node
from langGraph_demo.demo01.node.cancel_node import cancel_node

"""
创建一个大脑或智能体
"""

def email_agent(m):
    print("\n【测试】这里是email_agent01.py")
    # 获取图形结果
    graph = StateGraph(EmailState)
    # print(f"【测试】获取图形结果：{graph}")
    # 顺序图添加
    # print("【测试】意图识别节点")
    graph.add_node("internet",internet_node)
    # print("【测试】查询节点")
    graph.add_node("query",query_node)
    # print("【测试】邮件节点")
    graph.add_node("email",email_node)
    # print("【测试】取消节点")
    graph.add_node("cancel", cancel_node)
    # 画边
    # 新版入口
    # print("【测试】开始 --》意图识别")
    graph.add_edge(START,"internet")
    # 旧版入口
    # graph.set_entry_("internet")
    # print("【测试】意图识别 --》查询")
    graph.add_edge("internet", "query")
    # print("【测试】查询 --》邮件")
    graph.add_edge("query", "email")
    # print("【测试】邮件 --》结束")
    graph.add_edge("email", END)
    # print("【测试】取消 --》结束")
    graph.add_edge("cancel", END)
    # 编译 -- 在邮件节点前中断
    agent = graph.compile(
        interrupt_before=["email"],
        checkpointer=m  # 人工审核必须加入检查点
    )
    # print(f"【测试】编译结果：{agent}")
    return agent