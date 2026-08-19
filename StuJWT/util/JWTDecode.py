from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from util.JWTUtil import verify_token

# 定义 OAuth2 令牌获取端点
# FastAPI 会自动从请求头 Authorization: Bearer <token> 中提取令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 解码，获取用户信息
# Depends：在进入这个方法的时候，要依赖于oauth2_scheme这个方法，等价于拦截处理，获取token
def get_current_user(token:Annotated[str, Depends(oauth2_scheme)]):
    print("进入方法之前进行验证：")
    payload = verify_token(token)
    print(payload)

    # 定义认证异常
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭据",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if payload is None:
        raise credentials_exception

    return payload

if __name__ == '__main__':
    # data = {"user_id":1}
    # token = create_token(data)
    # print(token)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3ODY0MzE0NDIsImlhdCI6MTc4NjQzMTE0Mn0.y97uF_kQskzxIyriX0HvVz3WJaBKO5nVX4XjsP4Wqyg"
    print(token)
    print(verify_token(token))
    print(get_current_user(token))