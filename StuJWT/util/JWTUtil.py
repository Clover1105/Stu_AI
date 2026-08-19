from datetime import datetime,timezone,timedelta

from fastapi import HTTPException,status
from jose import JWTError,jwt

import os
from dotenv import load_dotenv
load_dotenv()

# 生成token
def create_token(data:dict):
    print(f"create_token函数的形参data: {data}")
    # data：用户需要封装进入payload的数据内容，字典格式{k:v}
    copy_data = data.copy()
    # 到期时间 = 当前时间 + 保质期
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    # 将信息按需放入data中
    copy_data.update({
        "exp":expire,
        "iat":datetime.now(timezone.utc),
        "user_id":data.get("user_id"),
        "username":data.get("username"),
        "role_name":data.get("role_name")
    })
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
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token错误或已过期，验证失败"
        )

if __name__ == '__main__':
    # data = {"username":"admin", "password":"$2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC"}
    # token = create_token(data)
    # print(token)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIkMmIkMTIkaENnVEJ2RzR6MklSUHFEd0N2dkRKT0Q2a3pJbkx3cnRrMTJjSXR6cDZheFJRRk5HdnlyT0MiLCJleHAiOjE3ODY0MTcwOTQsImlhdCI6MTc4NjQxNjc5NH0.0U9ZKlkBU0KKmRnlNkDGcp7GnBhp0H-FGXPdTGLte-A"
    result = verify_token(token)
    print(result)
