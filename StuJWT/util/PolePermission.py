from fastapi import Header, HTTPException
from util.JWTDecode import get_current_user


def is_roles(*allow_roles:list):
    print(f"被允许的角色：{allow_roles}")
    def user_permission(authorization:str = Header(None)):
        # 分词，获取token
        token = authorization.split(" ")[1]
        print(f"token:{token}")
        # 解析token，获取用户信息
        now_user = get_current_user(token)
        print(f"当前用户信息：{now_user}")
        # 判断用户是否被允许访问该接口
        if now_user['role_name'] in allow_roles[0]:
            return now_user
        else:
            raise HTTPException(status_code=403, detail="用户无权访问该接口")
    return user_permission
