from langGraph_demo.demo03.state.email_state03 import EmailState

# 定义query节点条件路由函数 -- 是否能查询到邮箱
def query_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- query_router")
    data = state['next_step']
    if data == "email":
        return "email"
    else:
        return "end"

# 是否发送邮件
def agent_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- agent_router")
    data = state['next_step']
    if data == "chat":
        return "chat"
    else:
        return "internet"

# 查不到就重新查
def query_for_router(state:EmailState):
    print("\n【测试】这里是condiyion_node03.py -- query_for_router")
    # 获取查询结果
    query = query_router(state)
    count = state['count']
    if query == "email":
        return "email"
    else:
        if count < 3:
            return "i"
        else:
            return "end"