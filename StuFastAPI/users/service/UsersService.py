from users.dao import UsersDao
# 随机数
import random
# api
# 创建信封
from email.mime.text import MIMEText
# 邮件发送服务
import smtplib
# 加载redis工具
from common import RedisUtil
# 加载大模型
from ai import LoadLLM
# 加载环境信息
import os
from dotenv import load_dotenv
load_dotenv()

# 发送邮件
def send_email(email):
    # 1. 验证邮箱是否输出注册过的用户
    flag = False

    # 取出当前邮箱号的用户名 -- 需要数据库
    result = UsersDao.check_email(email)
    username = result[0]["username"]
    print(f"取出的用户名为：{username}")

    # isinstance(a,b)：返回布尔，判断a是不是b类型（b的实例）
    if isinstance(result, list):
        flag = True

    # 2. 根据结果判断是否发送邮箱
    if not flag:    # 不发邮件
        return {
            "code":500,
            "msg":f"该邮箱号 {email} 不存在",
            "data":None
        }

    # 3.发邮件
    # 随机生成6位验证码
    code = ""
    for _ in range(6):
        code += str(random.randint(0, 9))

    # 配置发送信息：发件方、授权码（从.env文件读取）、主题、邮件内容
    sender = os.getenv("SENDER_EMAIL")
    senger_pwd = os.getenv("SENDER_EMAIL_PASSWORD")
    subject = "主题为：发送验证码"
    content = f"验证码为：{code},请在1分钟内使用"

    # 创建邮件对象 -- 将要发送的信息写在这个对象里面
    message = MIMEText(content, "plain", "utf-8")
    print(f"创建的邮件对象为：{message}")

    # 添加内容在 message对象中
    message["From"] = sender    # 发件人
    message["To"] = email   # 收件人
    message["Subject"] = subject    # 主题
    print(f"添加内容后的邮件对象为：{message}")

    try:
        # 创建邮件发送服务配置
        smtp = smtplib.SMTP(
            host=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT"))
        )

        # 开启邮件发送服务 TLS
        smtp.starttls()

        # 验证发送方和发送方的授权码是否能对上
        smtp.login(sender, senger_pwd)

        # 发送邮件 -- 方法：sendmail(发送方，接收方，邮件对象)
        smtp.sendmail(sender, email, message.as_string())

        # 发送成功后退出
        smtp.quit()

        # 将验证码存储到redis中
        # 获取连接
        r = RedisUtil.get_redis_conn()
        # redis存值通过key,value格式存入，取值通过key
        r.setex(email, 60 ,code)  # 60秒后过期，key为email，value为code
        # 关闭连接
        RedisUtil.close_redis_conn(r)

        # 返回成功信息
        return {
            "code": 200,
            "msg": f"邮件已发送成功，到 {email}",
            "data": username
        }

    except Exception as e:
        print(f"发送邮件失败：{e}")
        return {
            "code": 501,
            "msg": f"邮件发送到 {email} 失败",
            "data": None
        }

# 验证码的验证
def check_code(checkCodeEntity):
    # 取出用户传递过来的验证码和邮箱号
    email = checkCodeEntity.email
    code = checkCodeEntity.code

    # 通过用户输入的邮箱号，从redis中取出验证码
    r = RedisUtil.get_redis_conn()
    redis_code = r.get(email)
    RedisUtil.close_redis_conn(r)

    # 判断验证码是否过期
    if redis_code is None:  # 过期
        return {
            "code": 502,
            "msg": "验证码已过期",
            "data": None
        }

    # 没有过期，但验证码不一致
    if redis_code != code:
        return {
            "code": 503,
            "msg": "验证码错误",
            "data": None
        }

    # 没有过期，且验证码一致
    return {
        "code": 200,
        "msg": "验证码验证成功",
        "data": None
    }

# 聊天
def chat(question):
    # 加载模型
    llm = LoadLLM.create_model()
    # 聊天
    return {
        "code": 200,
        "msg": "成功",
        "data": llm.invoke([
            {"role": "user", "content": question}
        ]).content
    }

if __name__ == "__main__":
    print(send_email("c@qq.com"))


