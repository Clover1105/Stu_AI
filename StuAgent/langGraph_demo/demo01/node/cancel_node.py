from langGraph_demo.demo01.state.email_state01 import EmailState

def cancel_node(state: EmailState):
    print("邮件发送已取消")
    return {}