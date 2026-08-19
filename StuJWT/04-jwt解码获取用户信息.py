from datetime import datetime,timezone,timedelta
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt

import os
from dotenv import load_dotenv
load_dotenv()

# 生成token
def create_token(data:dict):
    # data：用户需要封装进入payload的数据内容，字典格式{k:v}
    copy_data = data.copy()
    # 到期时间 = 当前时间 + 保质期
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    # 将到期时间和token生成时间放入data中
    copy_data.update({"exp":expire, "iat":datetime.now(timezone.utc)})
    # 生成token
    token = jwt.encode(
        claims = copy_data,
        key = os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )
    return token


# 验证token
def verify_token(token:str):
    try:
        result = jwt.decode(
            token = token,
            key = os.getenv("SECRET_KEY"),
            algorithms=[os.getenv("ALGORITHM")]
        )
        return result
    except JWTError:
        return {
            "code":401,
            "msg":"token错误或已过期，验证失败"
        }

# 定义 OAuth2 令牌获取端点
# FastAPI 会自动从请求头 Authorization: Bearer <token> 中提取令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 解码获取用户信息
# Depends：在进入这个方法的时候，要依赖于oauth2_scheme这个方法，等价于拦截处理，获取token
def get_current_user(token:Annotated[str, Depends(oauth2_scheme)]):
    payload = verify_token(token)
    if payload is None:
        return {
            "code":401,
            "msg":"token错误或已过期，验证失败"
        }
    user_id = payload.get("user_id")
    if user_id is None:
        return {
            "code": 401,
            "msg": "用户不存在"
        }
    payload.update({"username": "clover","role_name":"admin"})
    return payload


if __name__ == '__main__':
    # data = {"username":"admin", "password":"$2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC"}
    # token = create_token(data)
    # print(token)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIkMmIkMTIkaENnVEJ2RzR6MklSUHFEd0N2dkRKT0Q2a3pJbkx3cnRrMTJjSXR6cDZheFJRRk5HdnlyT0MiLCJleHAiOjE3ODY0MTcwOTQsImlhdCI6MTc4NjQxNjc5NH0.0U9ZKlkBU0KKmRnlNkDGcp7GnBhp0H-FGXPdTGLte-A"
    result = verify_token(token)
    print(result)


