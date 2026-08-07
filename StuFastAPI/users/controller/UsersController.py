from fastapi import APIRouter
print("加载了UsersController")
from users.service import UsersService
from users.entity.CheckCodeEntity import CheckCodeEntity

# 创建子路由对象
users_router = APIRouter()

@users_router.get(
    # 请求路径
    path="/sendEmail",
    # 接口简短摘要，显示在 Swagger UI 的接口列表中
    summary="发送邮件",
    # 接口详细描述，显示在 Swagger UI 的接口详情中
    description="""
        给用户输入的邮箱号发送验证码
        访问路径：http://localhost:8000/users/sendEmail
        请求参数：
            email：字符串类型，用户输入的邮箱号
        返回值：
            {
                "code": 状态码，成功200、失败500，int
                "msg": 提示信息，字符串
                "data": None，数据内容，Object
            }
    """,
)
def send_email(email: str):
    print("==========进入send_email==========")
    # 调用服务层方法 --- 服务层方法的返回值在这里就是直接返回给客户端请求
    print(f"接收到邮箱号：email={email}")
    return UsersService.send_email(email)

@users_router.post(
# 请求路径
    path="/checkCode",
    # 接口简短摘要，显示在 Swagger UI 的接口列表中
    summary="验证码的验证",
    # 接口详细描述，显示在 Swagger UI 的接口详情中
    description="""
        验证用户输入的验证码是否正确
        访问路径：http://localhost:8000/users/checkCode
        请求参数：
            CheckCodeModel：一个对象，两个属性
                email：邮箱号，用于去除redis中存入的值作为key
                code：用户输入的验证码，用于和redis中存入的值进行比较
        返回值：
            {
                "code": 状态码，成功200、失败500，int
                "msg": 提示信息，字符串
                "data": None，数据内容，Object
            }
    """,
)
def check_code(checkCodeEntity: CheckCodeEntity):
    print("==========进入check_code==========")
    print(f"接收到的对象：{checkCodeEntity}")
    return UsersService.check_code(checkCodeEntity)

# 通过EventSource创建出来的对象实现SSE，只支持get请求方式；
# 如果想要用POST请求，可以用原生的fetch请求或者找有没有第三方集成的库

@users_router.get(
# 请求路径
    path="/chat",
    # 接口简短摘要，显示在 Swagger UI 的接口列表中
    summary="去聊天页面",
    # 接口详细描述，显示在 Swagger UI 的接口详情中
    description="""
        聊天
        访问路径：http://localhost:8000/users/chat
        请求参数：
            question：用户问题
        返回值：
            流式输出：sse
    """,
)
def chat(question: str):
    print("==========进入chat==========")
    print(f"接收到问题：{question}")
    return UsersService.chat(question)