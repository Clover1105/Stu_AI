# 这个文件里面的内容就是用来学习fastapi相关操作的

# 引入子路由类
from fastapi import APIRouter

# 创建子路由对象
users_router = APIRouter()

# 定义了一个函数
@users_router.get("/zero")
def zero():
    return {"msg":"this is one"}


"""
方式一：get请求+key = value数据
    直接用形参接收，形参的名字许哟啊和key相同，否则接收不到数据
"""
@users_router.get("/one")
def one(username: str,password:str):
    print(f"接收的数据：username={username}，password={password}")
    return{
        "code":200,
        "msg":"this is one",
        "data":{
            "u_n":username,
            "p_w":password
        }
    }



"""
方式二：get请求+参数直接在请求路径后面（没有key，只有value）
    需要现在接口的请求路径定义中，定义{变量}占位，然后在接口方法中定义和占位变量相同的名字的形参来接收，有顺序问题
    通常情况下，用于查询和删除操作
注意事项：
    接口函数的形参必须和请求路径中的占位符的名字一样，否则422报错
"""
@users_router.get("/two/{username}/{password}")
def teo(username: str, password: str):
    print(f"接收的数据：username={username}，password={password}")
    return{
        "code":200,
        "msg":"this is two",
        "data":{
            "u_n":username,
            "p_w":password
        }
    }


"""
方式三：post 请求 + json 格式数据【application/json】
    需要定义一个类来接收，类的属性的名字必须和json数据中key相同，比如：
        json --- {"username":"admin", "password":"111"}
        类 ---- username: str password: str
"""
from pydantic import BaseModel,Field
# 定义接收数据的类 -- 直接继承BaseModel即可
class tc(BaseModel):
    # 定义属性 -- Field(...,title="用户名") 关于这个属性的说明
    username: str = Field(..., title="用户名")
    password: str = Field(..., title="密码")
@users_router.post("/three")
def three(data: tc):
    print(f"接收的数据：username={data.username}，password={data.password}")
    print(data.username,data.password)
    return {
        "code":200,
        "msg":"this is three",
        "data":data
    }

"""
方式四：post 请求 + 文件 file
    file 类型的数据，必须用 post 请求
    通过接口形参来接收，形参用UploadFile类来接收
    file 以外的数据可以封装在From中，比如 username: str = Form(...) 就是接收变量username
"""
from fastapi import UploadFile,File,Form
import time
@users_router.post("/four")
def four(file: UploadFile = File(..., title="上传的文件"),username: str = Form(..., title="用户名")):
    print(f"接收的数据：username={username}，file={file.filename}")
    # 重定义文件名
    filename = str(int(time.time())) + file.filename.split(".")[-1]
    # 传入文件存储地址
    save_path= r"G:\GitHub\Stu_AI\StuFastAPI\static\upload"+filename
    # 读取并保存文件
    with open(save_path,"wb") as f:
        # 读取文件内容
        f.write(file.file.read())
    return {
        "code":200,
        "msg":"this is four",
        "data":{
            "file_name":filename
        }
    }

"""
流式输出：StreamingResponse
    在 fastapi中，通过设置接口方法的返回值就可以实现流式输出
    参数1：content：一个迭代器（生成器）对象，直接通过yield作为函数的返回值即可创建出来迭代器（生成器）对象
    参数2：media_type: xxxx
"""
from starlette.responses import StreamingResponse

"""
流式输出方案一：直接把结果当前返回值返回，不做任何处理
    优点：服务器代码简单
    缺点：客户端代码非常难写
"""
@users_router.get("/stream_one")
def stream_one():
    # 设置模型返回值
    result = "程序员去医院体检，医生说：“你有点缺钙。”程序员点点头：“难怪最近老报错，原来不是代码有问题，是我这个‘运行环境’该升级了。”"
    # 定义生成器
    def generator():
        for i in result:
            yield f"{i}"
            time.sleep(0.05)
    # 返回结果
    return StreamingResponse(
        content=generator(),    # 迭代器对象
        media_type="text/event-stream",
    )

"""
流式输出方案二：客户端使用SSE请求，服务器必须把数据包装成data：数据内容\n\n 字符串格式，否则报错
    服务器中通常把数据内容转为json格式返回，便于客户处理，并且需要告诉客户但数据输出什么时候结束【给一个标识符】
    缺点：
"""
import json
@users_router.get("/stream_sse")
def stream_sse():
    result = "程序员去医院体检，医生说：“你有点缺钙。”程序员点点头：“难怪最近老报错，原来不是代码有问题，是我这个‘运行环境’该升级了。”"
    def generator():
        for i in result:
            yield f"data:{json.dumps({"content": i})}\n\n"
            time.sleep(0.05)
        yield f"data:{json.dumps({"content": "end_end"})}\n\n"
    return StreamingResponse(
        content=generator(),
        media_type="text/event-stream",
    )




