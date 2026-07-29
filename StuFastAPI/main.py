from fastapi import FastAPI

# 创建 FastAPI 对象
app = FastAPI()


# 导入子路由对象
from users.controller.TestController import users_router
# 注册子路由
app.include_router(
    router=users_router,    # 引入子路由对象
    prefix="/users", # 配置访问子路由接口的前缀，默认“”，推荐写为模块的包名作为区分
    tags=["text"]   # 配置swaggerUI中的模块名称
)

# 导入子路由对象
from users.controller.WorkController import work_router
# 注册子路由
app.include_router(
    router=work_router,
    prefix="/users",
    tags=["work"]
)

# 启动服务
if __name__ == "__main__":
    # 导入 uvicorn 包来写命令启动 fastapi 服务器项目
    import uvicorn as uv
    # 配置启动
    uv.run(
        # 启动项目的文件，即FastAPI()对象所在的文件
        app="main:app", # 配置启动的项目文件 --- main.py中的αpp对象
        host="localhost",   # 配置启动的服务器地址
        port=9000,  # 配置启动的服务器端口
        reload=False    # 配置是否自动重启
    )

