import random

from fastapi import FastAPI
from fastapi import Depends
from dotenv import load_dotenv
from pydantic import BaseModel
from util.JWTDecode import get_current_user
from util.JWTUtil import create_token
from util.PolePermission import is_roles

load_dotenv()

app = FastAPI()

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(userLogin: UserLogin):
    # 判断用户角色
    if userLogin.username == "clover":
        user_id = 0
        username = "clover"
        role_name = "admin"
    else:
        user_id = random.randint(1,10)
        username = f"temporary_{user_id}"
        role_name = "user"

    token = create_token({"user_id":user_id, "username":username, "role_name":role_name})
    return {
        "code":200,
        "msg":"登录成功",
        "token":token
    }

class CurrentUser(BaseModel):
    user_id: int
    username: str
    role_name: str

@app.get("/currentUser")
def current_user(now_user: CurrentUser = Depends(get_current_user)):
    print(f"当前用户信息：{now_user}")
    return {
        "code":200,
        "msg":"获取当前用户信息成功",
        "data":now_user
    }

# 删除 -- 管理员
@app.delete("/deleteUser/{user_id}")
def delete_user(user_id:int,now_user: CurrentUser = Depends(is_roles(["admin"]))):
    print(f"删除用户：{user_id}")
    return {
        "code":200,
        "msg":"删除用户成功",
        "data":None
    }

# 查询 -- 管理员、用户
@app.get("/queryUser")
def get_user(now_user: CurrentUser = Depends(is_roles(["admin","user"]))):
    print(f"查询用户：{now_user}")
    return {
        "code":200,
        "msg":"查询用户成功",
        "data":None
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000,reload=False)




