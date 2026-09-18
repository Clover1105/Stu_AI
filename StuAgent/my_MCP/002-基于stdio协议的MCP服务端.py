from fastmcp import FastMCP
from email.mime.text import MIMEText    # 写邮件
import smtplib  # 发送邮件
from dotenv import load_dotenv
import os


import sys
import io

# 强制将 stdout 和 stderr 设置为 utf-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

load_dotenv()
# 创建应用程序
app = FastMCP()

# 定义mysql工具
@app.tool('send_email_tool')
def send_email_tool(to: str, subject: str, content: str)->str:
    """
    描述：发送邮件工具
    :param to: 收件人
    :param subject: 主题
    :param content: 邮件内容
    :return: 返回成功200或失败500
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
        return "发送邮件成功"
    except Exception as e:
        print(f"发送邮件失败:{e}")
        return f"发送邮件失败：{e}"


from pydantic import BaseModel,Field
from util.mysql_conn import GetMySQLConn

class QueryEmployeeSchema(BaseModel):
    sql: str = Field(...,description="sql语句")

# 定义MySQL
@app.tool(
    description="执行 sql 语句查询；数据库模型：表名：employee，字段：user_id 员工ID编号,user_name 员工名字,email 员工邮箱,department 员工所属部门；规则：禁止生成DELETE、UPDATE、INSERT语句"
)
def mysql_tool(t: QueryEmployeeSchema)->str:
    """
    描述：MySQL工具
    :param sql: SQL语句
    :return: 返回成功200或失败500
    """
    print(f"生成的sql语句：{t}",file=sys.stderr)
    conn = None
    cur = None
    # 兜底操作
    sql = t.sql
    if "DELETE" in sql.upper() or "UPDATE" in sql.upper() or "INSERT" in sql.upper() or "DROP" in sql.upper() or "CREATE" in sql.upper() or "ALTER" in sql.upper():
        return "禁止执行非法sql语句操作"
    try:
        conn = GetMySQLConn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return str(result)
    except Exception as e:
        print(f"执行sql语句失败：{e}")
        return "执行sql语句失败"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(
        transport = 'stdio',
    )


