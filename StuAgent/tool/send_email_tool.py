from langchain.tools import tool
from email.mime.text import MIMEText    # 写邮件
import smtplib  # 发送邮件
from tool.schema.send_email_schema import EmailParams
from dotenv import load_dotenv
import os
load_dotenv()


# 定义工具
@tool(
    "send_email_tool",  # 可选，默认用对应方法名作为工具名称
    description="发送邮件工具",
    args_schema=EmailParams,
)
def SendEmailTool(to:str,subject:str,content:str)->str:
    """
    用于发送邮件，发送通知，发送信息
    """
    # 每个工具都要加异常处理
    try:
        # 读取配置文件信息
        email = os.getenv("SENDER_EMAIL")   # 发件人邮箱
        host = os.getenv("EMAIL_HOST")
        port = os.getenv("EMAIL_PORT")
        password = os.getenv("SENDER_EMAIL_PASSWORD")
        # 判断配置是否读取成功
        if not email or not host or not port or not password:
            raise Exception("配置文件信息读取失败")
        # 创建邮件对象
        msg = MIMEText(content)
        msg['To'] = to  # 收件人
        msg['Subject'] = subject    # 邮件主题
        msg['From'] = email  # 发件人
        # 创建一个链接邮件服务器地址
        with smtplib.SMTP_SSL(host,int(port)) as smtp:  # port读取出来为字符串，需要转换为int
            # 登录邮件服务器
            smtp.login(email,password)
            # 发送邮件
            smtp.sendmail(email,to,msg.as_string())
        return "发送邮件成功\n"
    except Exception as e:
        print(f"发送邮件失败:{e}")
        return f"发送邮件失败:{e}"

if __name__ == '__main__':
    SendEmailTool.invoke({
        "to":"2920242909@qq.com",
        "subject":"测试邮件",
        "content":"测试邮件内容"
    })
