from langGraph_demo.demo02.state.email_state02 import EmailState

# 定义query节点条件路由函数
def query_router(state:EmailState):
    print("\n【测试】这里是condiyion_node02.py")
    data = state['next_step']
    if data == "email":
        return "a"
    else:
        return "b"