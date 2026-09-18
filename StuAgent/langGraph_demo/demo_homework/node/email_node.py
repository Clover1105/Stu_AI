from langGraph_demo.demo_homework.state.email_state import EmailState
from tool.send_email_tool import SendEmailTool
from langchain_core.messages import AIMessage

def email_node(state:EmailState):
    print("\n\n【测试】这里是email_node.py")
    # 邮箱
    email = state["email"]
    # 标题
    subject = state["subject"]
    # 内容
    content = state["content"]
    # 调用邮件工具
    rs = SendEmailTool.invoke(
        {"to":email,"subject":subject,"content":content}
    )
    print(f"【测试】获得调用邮件工具结果：{rs}")
    if str(rs).strip() == "发送邮件成功":
        # 自定义最终答案，结果
        ai_msg = f"邮件发送成功\n"
        return {
            "messages":[AIMessage(content=ai_msg)],
            "return":"邮件发送成功"
        }
    else:
        # 自定义最终答案，结果
        ai_msg = f"邮件发送失败\n"
        return {
            "messages": [AIMessage(content=ai_msg)],
            "return": "邮件发送失败"
        }