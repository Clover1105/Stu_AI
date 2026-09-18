from langGraph_demo.demo04.state.email_state04 import EmailState
from langgraph.graph import END
from langgraph.types import Command

"""
主管节点，处理任务分类
"""

def manager_node(state:EmailState):
    print("\n\n【测试】这里是manager_node04.py.py")

    # 主管觉得下一步做什么 -- 获取当前步骤信息
    step = state.get("step","start")

    if step == "start":
        next_node = "internet"
    elif step == "internet_node":
        next_node = "query"
    elif step == "query_node":
        next_node = "email"
    elif step == "email_node":
        next_node = END
    else:
        next_node = END
    # 动态跳转节点
    return Command(goto=next_node)

if __name__ == '__main__':
    data = {"name":"","age":23}
    # print(f"name={data["address"]}")
    print(f"name={data.get("address", "a")}")
