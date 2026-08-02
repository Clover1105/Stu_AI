from fastapi import FastAPI
print("加载了main.py")
# 启动项目和关闭项目分别执行一些内容
from contextlib import asynccontextmanager
@asynccontextmanager
async def start_rnd_run(app):
    """
        app:FastAPI 对象
        yield之前的内容：启动项目执行
        yield 之后的内容：关闭项目执行
        如果想实现一些变量的初始化操作，可以把变量写入到 app.state 属性中，格式如下：
            app.state.变量名 = 初始值
        如果某个接口中需要使用，就用 request 对象取出来，格式如下：
            变量名2 = request.app.state.变量名
    """
    print("启动项目")
    yield
    print("关闭项目")
# 创建 FastAPI 对象
app = FastAPI(lifespan=start_rnd_run)
# app = FastAPI()

# 导入子路由对象
from users.controller.UsersController import users_router
# 注册子路由
app.include_router(
    router=users_router,    # 引入子路由对象
    prefix="/users", # 配置访问子路由接口的前缀，默认“”，推荐写为模块的包名作为区分
    tags=["text"]   # 配置swaggerUI中的模块名称
)

# 静态资源配置
from fastapi.staticfiles import StaticFiles
app.mount(
    "/static",	# 静态资源访问的前缀 -- 请求路径
    StaticFiles(directory="static"),	# 静态资源目录 -- 放行的文件夹
    name="static"	# 静态资源访问的模块名称
)

# 跨域配置
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],    # 允许的跨域访问的域名 -- 完整的客户端域名
    allow_credentials=True, # 允许携带cookie
    allow_methods=["*"],    # 允许的跨域访问请求的方法
    allow_headers=["*"],    # 允许的跨域访问请求的头部信息
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
        port=8000,  # 配置启动的服务器端口
        reload=False    # 配置是否自动重启
    )

