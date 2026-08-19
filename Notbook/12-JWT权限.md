# 一、权限

为什么需要使用：

当我们访问服务器内部的方法、访问客户端的页面的时候，应该做一个身份认证；以及有的服务器接口只能够某些角色可以访问

客户端：

- 使用导航守卫实现未登录拦截

服务器：

- 使用jwt认证来实现

- 所有的请求方法都需要改：
    - 今后的请求，必须携带token才能进入接口里面，如未携带或随便乱写一个token，那么就无法访问此方法，会被拒绝访问
    - JWT是无状态的，服务器端不需要做任何的存储处理，只需要在登陆的时候生成一个token，然后返回给客户端
    - 因此登陆的时候需要得到token，并用一个变量将token进行存储，在页面可以使用方法`sessionStorage`

# 二、客户端

`main.js`

添加导航守卫代码

判断页面是否需要登陆后才能访问

需要：查看登陆信息，是否能成功获取用户，能则放行，不能则拒绝访问

不需要：直接放行

```
router.beforeEach((to, from, next) => {
    if (to.meta.login){
        let username = sessionStorage.getItem('username')
        if (username){
            console.log('已登录，跳转到聊天页面')
            next()
        } else {
            console.log('未登录，跳转到登录页面')
            next('/')
        }
    } else {
        console.log('此为登陆页面，直接访问')
        next()
    }
})
```

`index.js`

为路由添加访问状态

```
// 定义路由配置对象 -- 数组
const routes = [
    {
        // 一个页面的访问路径就是一个 js 对象，至少包含 2 个属性：path、component
        path: '',   // 访问路径，和服务器的请求路访问规则一致
        meta:{
            login:false  // 该页面是否允许（或需要）登录态访问
        },
        component: () => import('../components/Login.vue')    // 访问组件
    },
    {
        // 一个页面的访问路径就是一个 js 对象，至少包含 2 个属性：path、component
        path: '/chat',   // 访问路径，和服务器的请求路访问规则一致
        meta:{
            login:true // 该页面是否允许（或需要）登录态访问
        },
        component: () => import('../components/Chat.vue')    // 访问组件
    }
]
```

# 三、服务器

我们使用JWT来实现

## （一）JWT（JSON Web Token）

- 是一种开放标准（RFC 7519），用于在各方之间安全地传输信息。它由三部分组成，以 `.` 分隔：`Header.Payload.Signature`
- 就是一个token认证，它可以把登录信息封装了一个字符串中，客户端请求就需要携带这个token内容来进行认证，认证通过允许访问，认证不通过不允许访问
- 认证通过和不通过：指的是请求进入接口的时候被拦截

密码加密处理：

对于开发者而言，直接通过数据库的方式是可以看到任何用户的账号和密码的，这样的方式是不安全的。我们把数据库中存储的密码信息进行加密处理，把明文转为密文，比如111 ==> asdfghjksdfghjkl

使用 redis，生成token后可保存30分钟，每一次进入页面都可以去redis里面验证token是否存在，存在则可以继续访问，不存在拒绝访问，还可以实现退出登陆后，token一并删除

## （二）安装依赖

```
# 全部包
pip install fastapi uvicorn[standard] python-jose[cryptography] passlib[bcrypt] python-multipart pydantic bcrypt==4.0.1 passlib==1.7.4
# JWT包（现在只需要安装一部分，上面的安装过）
pip install python-jose[cryptography] passlib[bcrypt] python-multipart bcrypt==4.0.1 passlib==1.7.4
```

## （三）生成安全密钥

密钥生成，提供给生成JWT的时候使用，生成后需要存储到环境变量（`.env`）中

```
# 生成 JWT 签名密钥（64 字节随机字符串的 base64 编码）
# 生成适用于管理帐户身份验证、令牌等秘密的加密强伪随机数。
import secrets

# 生成32位随机字符组成的字符串密钥
# 返回一个随机的URL安全文本字符串，采用Base64编码
mi_key = secrets.token_urlsafe(32)
print(mi_key)
```

```
# .env 文件

# 密钥
SECRET_KEY="your-generated-secret-key-here"
# 算法名称
ALGORITHM="HS256"
# token过期时间（分钟）
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## （四）密码哈希工具

将数据库中存储的密码变为密文样式

- schemes=[“bcrypt”] -- 使用的算法名称

```python
from passlib.context import CryptContext

# 创建密码加密上下文对象
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 对密码进行加密处理
def hash_password(psaaword: str) -> str:
    hash_pw = crypt_context.hash(psaaword)
    return hash_pw

# 验证
def ver_password(plain_pw: str, hash_pw: str) -> bool:
    result = crypt_context.verify(plain_pw, hash_pw)
    return result

if __name__ == '__main__':
    # hp = hash_password("123456")
    # print(hp)
    """
    $2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC
    $2b$12$H1m5peHJT2MtYHNKSUmRLeuw5RnwmrQnp8nRz/zQ9Zyt0KbK19ltm
    """
    # hp = hash_password("123")
    # print(hp)
    """
    $2b$12$10iejQKz70VhksVMy03G2eeWQmtQ4AABDxH1apMd3q0z9cy1ppk.e
    $2b$12$noE.x6Wx7VXd/UXWpNIkb.UZKeuDo5v.9bmdFNQS7DKsthOwUlst2
    """
    plain_pw = "123456"
    hash_pw = "$2b$12$hCgTBvG4z2IRPqDwCvvDJOD6kzInLwrtk12cItzp6axRQFNGvyrOC"
    vp = ver_password(plain_pw, hash_pw)
    print(vp)
```

## （五）jwt令牌工具

生成令牌：

发生在登陆阶段，登陆成功后就将令牌【令牌就是token】生成出来返回给客户端，客户端拿到令牌后通过`sessionStorage`对令牌进行存储

今后客户端请求服务器，就只需要将令牌从`sessionStorage`中取出来然后放在请求头中发送给服务器

验证令牌：

在服务器中请求某个具体的方法时就需要被拦截处理，判断是否被允许访问，因此需要在接口中添加对应操作，使得处理数据时使用认证方法

认证方法中需要调用**解码**操作，通过解码操作可以得到被封装的信息，主要信息在载荷`payload`中

```
from datetime import datetime,timezone,timedelta
from jose import JWTError,jwt

import os
from dotenv import load_dotenv
load_dotenv()
```

### 1. 生成令牌

将payload的数据内容复制一份，计算token到期时间（当前时间 + 保质期），更新data信息，调用`jwt.encode`方法生成token

 **jwt.encode()：生成 JWT Token**

它的作用是将包含用户信息的载荷（Payload）与加密密钥结合，通过指定算法进行加密签名，最终生成一个安全的、不可篡改的 Token 字符串。

核心参数：

- payload：字典类型，包含要传递的数据（如用户ID、角色、过期时间 `exp` 等）。
- key：加密签名使用的密钥（必须保密）。
- algorithm：定义加密算法，如 `HS256`（对称加密）、`RS256`（非对称加密）。

**注意：**在调用 `create_token` 时，只需要传入能够**唯一标识该用户**的信息即可

```python
# 生成token
def create_token(data:dict):
    # data：用户需要封装进入payload的数据内容，字典格式{k:v}
    copy_data = data.copy()
    # 到期时间 = 当前时间 + 保质期
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    # 将到期时间和token生成时间放入data中
    copy_data.update({"exp":expire, "iat":datetime.now(timezone.utc)})
    """
        本质上调这个方法的时候：
        token生成后入库 --- 退出登录的时候应该删除掉token
    """
    # 生成token
    token = jwt.encode(
        claims = copy_data,
        key = os.getenv("SECRET_KEY"),
        algorithm=os.getenv("ALGORITHM")
    )
    return token
```

### 2. 验证令牌

调用`jwt.decode`方法验证解析token，返回验证结果

**jwt.decode()：验证并解析 JWT Token**

它用于解析客户端传来的 JWT 字符串，**同时验证其合法性**（包括签名是否正确、是否过期等），验证通过后返回原始的 Payload 数据。

核心参数：

- jwt：待解析的 JWT 字符串。
- key：验签密钥（必须与 `encode` 时使用的密钥一致）。
- algorithms：允许的加密算法列表（如 `["HS256"]`，2.x 版本强制要求填写以防攻击）。
    - **`algorithms: str | Container[str] | None = None`**
    - 接受一个字符串（`str`），或者一个容器（`Container[str]`，比如列表 `list` 或元组 `tuple`）
    - 虽然类型提示允许传入单个字符串，但在实际的安全验证中，PyJWT 强烈推荐使用列表（如 `["HS256"]`），这能有效防止“算法降级攻击”

```python
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
```

### 3. 包装为工具函数

```python
from datetime import datetime,timezone,timedelta

from fastapi import HTTPException,status
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
```

## （六）解码获取用户信息

### 1. OAuth2 密码流（Password Flow）认证

`OAuth2PasswordBearer` 是一个**安全依赖项（Security Dependency）**。它的主要作用是告诉 FastAPI：“我的系统使用 Bearer Token 进行身份验证，并且前端需要去指定的 URL 获取这个 Token。”

```
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
```

- 创建了一个 OAuth2 密码流的安全方案实例
- `tokenUrl="/users/login"` 是一个**相对路径**，它仅仅是一个**声明**，告诉客户端：“如果你需要获取令牌，请向 `/users/login` 这个端点发送请求。”
- 这行代码**本身并不会创建** `/users/login` 这个路由，你仍然需要自己编写 `@app.post("/users/login")` 来处理实际的登录逻辑

它作为依赖注入（Dependency Injection）使用时，会自动拦截请求并进行以下操作：

- **自动提取 Token**：它会去 HTTP 请求头（Header）中寻找 `Authorization` 字段。
- **校验格式**：检查该字段的值是否符合 `Bearer <token>` 的格式。
- **返回 Token 字符串**：如果找到且格式正确，它会把提取到的 `<token>` 字符串返回给你的路由函数。
- **自动拦截未授权请求**：如果请求头中没有 `Authorization`，或者格式不对，它会**直接返回 401 Unauthorized 错误**，你的路由函数根本不会被执行。

### 2. 依赖注入

```
def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict:
```

- **`str`**：告诉 FastAPI 和编辑器，这个参数最终的数据类型是一个字符串（即提取出来的 Token）。这保证了代码的自动补全和类型检查。
- **`Depends(oauth2_scheme)`**：告诉 FastAPI，这个参数的值不是由前端直接传过来的，而是**需要 FastAPI 自动去调用 `oauth2_scheme` 来获取**。

当有请求访问使用了这个函数的接口时，FastAPI 会在后台自动执行以下流程：

- **触发依赖**：FastAPI 看到 `Depends(oauth2_scheme)`，于是去调用你之前定义的 `oauth2_scheme`。
- **提取 Token**：`oauth2_scheme` 会自动去 HTTP 请求头（Header）中寻找 `Authorization: Bearer <token>`，并把它提取出来。
- **赋值给参数**：提取出的 Token 字符串会被自动赋值给 `token` 这个参数。
- **拦截无效请求**：如果请求头里没有 Token，或者格式不对，`oauth2_scheme` 会直接返回 `401 Unauthorized` 错误，你的 `get_current_user` 函数根本不会被执行。

### 3. 创建post和get接口

```python
from fastapi import FastAPI
from fastapi import Depends
from dotenv import load_dotenv
from pydantic import BaseModel
from util.JWTDecode import get_current_user
from util.JWTUtil import create_token

load_dotenv()
app = FastAPI()

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(userLogin: UserLogin):
    token = create_token({"user_id":1})
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

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000,reload=False)
```

### 4. 解码获取用户信息

```python
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
    user_id = int(payload.get("user_id"))
    if user_id is None:
        raise credentials_exception
    payload.update({"username": "clover","role_name":"admin"})

    return payload

if __name__ == '__main__':
    # data = {"user_id":1}
    # token = create_token(data)
    # print(token)

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3ODY0MzE0NDIsImlhdCI6MTc4NjQzMTE0Mn0.y97uF_kQskzxIyriX0HvVz3WJaBKO5nVX4XjsP4Wqyg"
    print(token)
    print(verify_token(token))
    print(get_current_user(token))
```

`raise` 是一个用于**主动抛出异常**的关键字。它的核心作用是：**当程序运行到某个不符合预期的条件时，立即中断当前执行流程，并向调用者报告一个错误**。

### 5. 测试验证

![image-20260811160742344](12-JWT权限.assets/image-20260811160742344.png)

![image-20260811160944663](12-JWT权限.assets/image-20260811160944663.png)

## （七）删除操作

### 1. 创建删除接口

```python
@app.delete("/deleteUser/{user_id}")
def delete_user(user_id:int,now_user: CurrentUser = Depends(is_roles(["admin"]))):
    print(f"删除用户：{user_id}")
    return {
        "code":200,
        "msg":"删除用户成功",
        "data":None
    }
```

### 2. 判断是否允许访问接口

允许访问：返回用户信息

不允许访问：返回拒绝访问信息

```python
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

```

### 3. 优化：登陆接口判断用户角色

```python
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
```

### 4. 优化：封装用户信息

生成token的时候就需要将用户信息包装进去

```python
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
```

删除`JWTDecode.py`中的：

```
user_id = int(payload.get("user_id"))

if user_id is None:
	raise credentials_exception
	
payload.update({"username": "clover","role_name":"admin"})
```

### 5. 测试

![image-20260811193745318](12-JWT权限.assets/image-20260811193745318.png)

![image-20260811194131620](12-JWT权限.assets/image-20260811194131620.png)

## （八）查询操作

### 1. 创建查询接口

```
# 查询 -- 管理员、用户
@app.get("/queryUser")
def get_user(now_user: CurrentUser = Depends(is_roles(["admin","user"]))):
    print(f"查询用户：{now_user}")
    return {
        "code":200,
        "msg":"查询用户成功",
        "data":None
    }
```

### 2. 测试验证

![image-20260811195229099](12-JWT权限.assets/image-20260811195229099.png)

## （九）MD解析配置

### 1. 安装两个库

```bash
# 安装 marked（markdown 解析）
npm install marked

# 安装 dompurify（XSS 防护）
npm install dompurify
```

### 2. 全局配置：

```js
// Markdown 配置
import { marked } from 'marked'
import DOMPurify from 'dompurify'

//  Markdown 配置
marked.setOptions({
  breaks: true,    // 支持换行
  gfm: true,       // GitHub 风格
  smartLists: true,
  smartypants: false
})

// Markdown 正则处理
function normalizeMarkdown(text) {
  return text
    .replace(/(#{1,6} )/g, '\n$1')
    .replace(/- /g, '\n- ')
}

// 全局 markdown 渲染方法
function renderMarkdown(text) {
  if (!text) return ''
  const rawHtml = marked.parse(normalizeMarkdown(text))
  return DOMPurify.sanitize(rawHtml)
}
app.config.globalProperties.$renderMarkdown = renderMarkdown
```

### 3. 使用

```vue
<template>
    <div>
        <div v-html="renderMarkdown(content)"></div>
    </div>
</template>

<script setup>
import {ref, getCurrentInstance} from 'vue'

const proxy = getCurrentInstance().proxy

const content = ref('# Markdown 解析测试数据')

function renderMarkdown(content) {
  return proxy.$renderMarkdown(content)
}
</script>
```

