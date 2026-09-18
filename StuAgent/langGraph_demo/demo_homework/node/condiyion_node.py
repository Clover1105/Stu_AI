from langGraph_demo.demo_homework.state.email_state import EmailState

# 定义query节点条件路由函数
def query_router(state:EmailState):
    print("\n【测试】这里是condiyion_node.py -- query_router")
    data = state['next_step']
    if data == "email":
        return "email"
    else:
        return "end"

def agent_router(state:EmailState):
    print("\n【测试】这里是condiyion_node.py -- agent_router")
    data = state['next_step']
    if data == "chat":
        return "chat"
    else:
        return "internet"