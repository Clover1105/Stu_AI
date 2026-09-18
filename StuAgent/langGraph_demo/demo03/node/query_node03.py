from langGraph_demo.demo03.state.email_state03 import EmailState
from tool.query_employee_tool import QueryEmployeeTool
from langchain_core.messages import ToolMessage
"""
查询节点
"""

def query_node(state:EmailState):
    print("\n\n【测试】这里是query_node03.py")
    # 获取查询次数
    count = state['count']+1
    # 获取用户姓名
    name = state["name"]
    # 调用工具
    rs = QueryEmployeeTool.invoke({
        "sql":f"select email from employee where user_name = '{name}'"
    })
    print("\n【测试】这里是query_node03.py")
    # print(f"【测试】查询数据结果：{rs}")    # [{'email': '2920242909@qq.com'}]
    # print("【测试】查询数据结果数据类型：",type(rs))
    if rs == ():
        return {
            "messages":[ToolMessage(content="用户邮箱不存在",tool_call_id="query_node")],
            "result":"用户邮箱不存在",
            "next_step":"end",   # 标识结束了
            "count":count
        }
    # 获取邮箱
    email = rs[0]['email']
    print(f"【测试】获取到的邮箱结果：{email}")
    # 定义结果
    tool_msg = f"\n查询节点成功\n邮箱为：{email}"
    return {
        "messages": [ToolMessage(content=tool_msg, tool_call_id="query_node")],
        "result": "\n用户邮箱查询成功\n",
        "email":email,
        "next_step":"email",     # 标识下一步走邮箱节点
        "count":count
    }


