from  fastapi import FastAPI
from contextlib import asynccontextmanager
from demo.email_agent import EmailAgent
import uvicorn

@asynccontextmanager
async def test(app:FastAPI):
    app.state.email_agent = EmailAgent()
    print("邮件智能体实例化成功！！！")
    yield
    app.state.email_agent = None
    print("销毁邮件智能体实例化！！！")


# 创建一个FastAPI应用 -- 异步上下文管理器
app = FastAPI(lifespan=test)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host="localhost",
        port=8000,
        reload=False    # 关闭自动重载
    )