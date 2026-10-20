# 一、MCP 服务应用

## （一）认识MCP

### 1. 定义

MCP 的全称是 **Model Context Protocol**，直译是“模型上下文协议”。

MCP（Model Context Protocol）是由 **Anthropic** 公司推出的一种开放协议。它的核心目标是让大型语言模型能够与外部工具、数据源和服务进行**安全、可控、标准化**的交互。

可以把它想象成 LLM 的“**应用商店**”或“**插件系统**”。在 MCP 出现之前，每个 AI 应用或平台（如 ChatGPT、[Claude.ai](https://claude.ai/)）都需要自己单独为每个工具或数据源开发集成，这非常低效且不统一。MCP 旨在解决这个问题。

### 2. 应用环境

- **企业内部知识问答系统**（知识库、私有化 RAG）开始使用 MCP 作为数据层接口；
- **LangChain 代理系统**（AgentExecutor、Tool Calling）逐步迁移到 MCP 统一协议；
- **FastMCP 框架** 在国内 GitHub、Gitee 上出现大量 Fork；
- **高校、培训课程** 开始讲授 MCP 体系（如「LangChain 智能体 + MCP 工程实战」）

### 3. 核心目标

**统一协议层，打通模型上下文与外部世界**

它的核心理念是：

> 让任何大模型（LLM）都能**安全、统一、标准化**地访问外部数据与工具。

### 4. 跨平台兼容（真正的通用标准）

MCP 目前被以下主流框架共同采用：

- OpenAI（GPT 系列）
- Anthropic（Claude）
- LangChain 
- LlamaIndex

这让它成为了**AI Agent 的通用底层协议**。

## （二）核心概念与工作原理

MCP 的架构主要包含三个核心组成部分：

### 1. MCP 客户端

- **角色**：**使用工具**的一方。通常是指大型语言模型本身或承载模型的应用程序（如 Claude 桌面端、Cursor IDE 等）。
- **功能**：向 MCP 服务器发送请求，例如“请查询一下北京的天气”或“请从我的数据库中获取用户列表”。
- **举例**：Claude 桌面应用程序就是一个 MCP 客户端。

### 2. MCP 服务器

- **角色**：**提供工具和数据**的一方。它是一个独立的进程，负责封装特定的功能或数据访问能力。
- **功能**：暴露一系列“工具”和“资源”给客户端调用。当客户端调用一个工具时，服务器负责执行具体的逻辑（如调用 API、查询数据库、执行计算）并返回结果。
- **举例**：一个提供天气查询 API 的服务器、一个连接到你公司数据库的服务器、一个能够执行代码的服务器。

### 3. 传输层

- **角色**：**连接客户端和服务器**的通信桥梁。
- **实现方式**：MCP 协议本身与传输方式无关。最常见的是 **Stdio**和 **SSE**。
    - **Stdio**：客户端直接启动服务器进程，通过**标准输入和标准输出**进行通信。简单、高效，适合本地工具。
    - **SSE ,http**：客户端通过 HTTP 连接到远程的服务器。适合需要远程访问或由第三方提供的服务

## （三）安装环境

```
pip install "mcp>=1.8.0" "langchain-mcp-adapters>=0.1.2" "fastmcp[server]" -i https://pypi.org/simple
```

## （四）FastMCP

创建 MCP（Model Context Protocol）服务主要有以下几种方式，从易到难、从快速到灵活，各有侧重。

### 1. 核心方式

| 方式                     | 核心工具                         | 优点                                         | 缺点                                 | 适合场景                                   |
| ------------------------ | -------------------------------- | -------------------------------------------- | ------------------------------------ | ------------------------------------------ |
| **1. 使用官方 SDK**      | `@modelcontextprotocol/sdk`      | **官方推荐、最稳定、最便捷**，封装了底层细节 | 灵活性相对较低                       | **绝大多数情况**，快速开发标准服务         |
| **2. 手动实现 STDIO**    | 任意语言 + 标准输入/输出         | **灵活性最高**，可用任何语言实现             | 需要手动处理协议、JSON RPC、生命周期 | 使用非 Node.js/Python 语言，或需要深度定制 |
| **3. 使用社区 SDK/模板** | 社区维护的 Python/Go/Rust 等 SDK | 比手动实现方便，比官方支持更多语言           |                                      |                                            |

**fastMCP 属于第一种方式：使用官方 SDK 的增强版和简化版**。

更准确地说，fastMCP 是**基于官方 @modelcontextprotocol/sdk 构建的高层封装和工具集**，属于 "官方 SDK 生态" 的一部分。

### 2. 定位

**底层依赖**：仍然使用官方的 `@modelcontextprotocol/sdk`

**设计目标**：简化开发流程，减少样板代码，提供更友好的 API

**额外功能**：内置了常用的工具、资源类型、服务器管理等开箱即用的功能

### 3. 优势

**开发效率**：用装饰器、依赖注入等模式大幅减少代码量

**内置功能**：提供了常用工具的快速实现（如 HTTP 客户端、文件操作等）

**配置简化**：简化了服务器配置和客户端连接

**生态整合**：更容易集成到现有的 Python/Node.js 项目中

# 二、基于 SSE 协议的MCP

## （一）服务端

基于 FastMCP 库构建了一个标准的 MCP 服务端，通过 SSE 协议对外暴露工具能力。它集成了邮件发送与数据库查询功能，并内置了敏感配置读取与安全校验机制，确保服务在本地端口稳定运行且数据安全

### 1. 导入库

引入 FastMCP 框架、邮件处理库（smtplib/MIMEText）、环境变量加载器（dotenv）、数据校验模型（Pydantic）以及自定义的数据库连接工具，为后续功能提供基础支持

```python
from fastmcp import FastMCP
from email.mime.text import MIMEText    # 写邮件
import smtplib  # 发送邮件
from dotenv import load_dotenv
import os

from pydantic import BaseModel,Field
from util.mysql_conn import GetMySQLConn
```

### 2. 引入环境，创建应用程序

加载 `.env` 配置文件以读取敏感信息，并初始化 `FastMCP` 实例作为应用入口，用于后续注册工具和启动服务

```python
load_dotenv()
# 创建应用程序
app = FastMCP()
```

### 3. 定义发送邮件工具

- **注册工具**：使用装饰器将函数注册为名为 `send_email_tool` 的 MCP 工具。
- **读取配置**：从环境变量中动态获取发件人邮箱、SMTP 主机、端口及密码，避免硬编码。
- **构建邮件**：使用 `MIMEText` 封装收件人、主题、内容及发件人信息。
    - `MIMEText` -- 
- **发送执行**：建立 SSL 加密连接并登录服务器，调用 `sendmail` 发送邮件。
- **异常处理**：捕获发送过程中的错误，返回明确的成功或失败状态字符串。

```python
@app.tool('send_email_tool')
def send_email_tool(to: str, subject: str, content: str)->str:
    """
    描述：发送邮件工具
    :param to: 收件人
    :param subject: 主题
    :param content: 邮件内容
    :return: 返回成功200或失败500
    """
    # 每个工具都要加异常处理
    try:
        # 读取配置文件信息
        email = os.getenv("SENDER_EMAIL")   # 发件人邮箱
        host = os.getenv("EMAIL_HOST")
        port = os.getenv("EMAIL_PORT")
        password = os.getenv("SENDER_EMAIL_PASSWORD")
        # 判断配置是否读取成功
        if not email or not host or not port or not password:
            raise Exception("配置文件信息读取失败")
        # 创建邮件对象
        msg = MIMEText(content)
        msg['To'] = to  # 收件人
        msg['Subject'] = subject    # 邮件主题
        msg['From'] = email  # 发件人
        # 创建一个链接邮件服务器地址
        with smtplib.SMTP_SSL(host,int(port)) as smtp:  # port读取出来为字符串，需要转换为int
            # 登录邮件服务器
            smtp.login(email,password)
            # 发送邮件
            smtp.sendmail(email,to,msg.as_string())
        return "发送邮件成功"
    except Exception as e:
        print(f"发送邮件失败:{e}")
        return f"发送邮件失败：{e}"
```

### 4. 参数校验

定义 `QueryEmployeeSchema` 类继承自 Pydantic 的 `BaseModel`，用于规范 SQL 查询工具的输入参数格式，确保传入的 SQL 语句符合预期结构

```python
class QueryEmployeeSchema(BaseModel):
    sql: str = Field(...,description="sql语句")
```

### 5. 执行SQL语句

- **安全拦截**：在执行前检查 SQL 内容，若包含删除、修改等高危关键词则直接拒绝，防止数据被篡改。
- **连接数据库**：调用自定义工具获取数据库连接和游标对象。
- **执行查询**：运行 SQL 语句并获取所有结果集。
- **资源释放**：使用 `finally` 块确保无论执行成功与否，游标和数据库连接都会被关闭。

```python
@app.tool(
    description="执行 sql 语句查询；数据库模型：表名：employee，字段：user_id 员工ID编号,user_name 员工名字,email 员工邮箱,department 员工所属部门；规则：禁止生成DELETE、UPDATE、INSERT语句"
)
def mysql_tool(sql: QueryEmployeeSchema)->str:
    """
    描述：MySQL工具
    :param sql: SQL语句
    :return: 返回成功200或失败500
    """
    print(f"生成的sql语句：{sql}")
    conn = None
    cur = None
    # 兜底操作
    sql = sql.sql
    if "DELETE" in sql.upper() or "UPDATE" in sql.upper() or "INSERT" in sql.upper() or "DROP" in sql.upper() or "CREATE" in sql.upper() or "ALTER" in sql.upper():
        return "禁止执行非法sql语句操作"
    try:
        conn = GetMySQLConn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return str(result)
    except Exception as e:
        print(f"执行sql语句失败：{e}")
        return "执行sql语句失败"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
```

### 6. 主程序

判断文件是否为主程序入口，若是则启动应用，监听本地 9000 端口，指定使用 SSE 传输协议

```python
if __name__ == '__main__':
    app.run(
        host = "localhost",
        port = 9000,
        transport = 'sse',
    )
```

## （二）客户端

实现了一个异步 MCP 客户端，用于连接上述 SSE 服务端。它演示了如何通过身份验证建立连接、发现可用工具列表，并按照特定格式调用远程工具以完成邮件发送和数据查询任务

### 1. 导入库

引入异步编程库 `asyncio` 以及 FastMCP 的客户端模块，用于发起异步网络请求

```python
import asyncio
from fastmcp import Client
```

### 2. 定义异步函数

- **建立连接**：使用上下文管理器连接服务端地址，并传入 `auth` 参数进行身份验证。
- **获取工具**：调用 `list_tools()` 方法获取服务端注册的所有可用工具信息。
- **调用邮件工具**：使用 `call_tool` 触发发送邮件功能，传入收件人、主题和内容参数。
- **处理结果**：打印返回对象的原始数据及结构化内容中的具体结果字段。
- **调用 SQL 工具**：触发数据库查询功能，注意参数需按照 Pydantic 模型的嵌套结构传递。

```python
async def test():
    # 定义客户端
    async with Client("http://localhost:9000/sse",auth="130806") as client:
        # 获取工具列表
        tools = await client.list_tools()
        print(tools)
        # 调用工具
        email_data = await client.call_tool("send_email_tool",{"to":"2920242909@qq.com","subject":"测试邮件","content":"测试邮件内容"})
        print(email_data)
        print(email_data.structured_content["result"])
        sql_data = await client.call_tool("mysql_tool",{"sql":{"sql":"select * from employee"}})
        print(sql_data)
        print(sql_data.structured_content["result"])
```

### 3. 主程序

判断是否为主程序入口，使用 `asyncio.run()` 启动定义的异步测试函数

```python
if __name__ == '__main__':
    asyncio.run(test())
```

# 三、基于stdio协议的MCP

## （一）服务端

构建了一个基于标准输入输出（stdio）协议的 MCP 服务端。与 SSE 协议不同，它不依赖网络端口，而是通过进程间的标准流进行通信。代码重点解决了 Windows 环境下的编码兼容性问题，并实现了邮件发送与安全 SQL 查询功能

### 1. 导入库

引入 FastMCP 框架、邮件处理库（smtplib/MIMEText）、环境变量加载器（dotenv）、数据校验模型（Pydantic）以及自定义的数据库连接工具，为后续功能提供基础支持

```python
from fastmcp import FastMCP
from email.mime.text import MIMEText    # 写邮件
import smtplib  # 发送邮件
from dotenv import load_dotenv
import os

from pydantic import BaseModel,Field
from util.mysql_conn import GetMySQLConn
```

### 2. 强制编码

使用 `io.TextIOWrapper` 强制将标准输出（stdout）和标准错误（stderr）的编码设置为 `utf-8`。这是为了防止在 Windows 等默认编码非 UTF-8 的系统上运行时，因中文输出导致 MCP 协议通信乱码或崩溃

```python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
```

### 3. 引入环境，创建应用程序

加载 `.env` 配置文件以读取敏感信息，并初始化 `FastMCP` 实例作为应用入口，用于后续注册工具和启动服务

```python
load_dotenv()
# 创建应用程序
app = FastMCP()
```

### 4. 定义发送邮件工具

- **注册工具**：使用装饰器将函数注册为名为 `send_email_tool` 的 MCP 工具。
- **读取配置**：从环境变量中动态获取发件人邮箱、SMTP 主机、端口及密码，避免硬编码。
- **构建邮件**：使用 `MIMEText` 封装收件人、主题、内容及发件人信息。
- **发送执行**：建立 SSL 加密连接并登录服务器，调用 `sendmail` 发送邮件。
- **异常处理**：捕获发送过程中的错误，返回明确的成功或失败状态字符串。

```python
@app.tool('send_email_tool')
def send_email_tool(to: str, subject: str, content: str)->str:
    """
    描述：发送邮件工具
    :param to: 收件人
    :param subject: 主题
    :param content: 邮件内容
    :return: 返回成功200或失败500
    """
    # 每个工具都要加异常处理
    try:
        # 读取配置文件信息
        email = os.getenv("SENDER_EMAIL")   # 发件人邮箱
        host = os.getenv("EMAIL_HOST")
        port = os.getenv("EMAIL_PORT")
        password = os.getenv("SENDER_EMAIL_PASSWORD")
        # 判断配置是否读取成功
        if not email or not host or not port or not password:
            raise Exception("配置文件信息读取失败")
        # 创建邮件对象
        msg = MIMEText(content)
        msg['To'] = to  # 收件人
        msg['Subject'] = subject    # 邮件主题
        msg['From'] = email  # 发件人
        # 创建一个链接邮件服务器地址
        with smtplib.SMTP_SSL(host,int(port)) as smtp:  # port读取出来为字符串，需要转换为int
            # 登录邮件服务器
            smtp.login(email,password)
            # 发送邮件
            smtp.sendmail(email,to,msg.as_string())
        return "发送邮件成功"
    except Exception as e:
        print(f"发送邮件失败:{e}")
        return f"发送邮件失败：{e}"
```

### 5. 参数校验

定义 `QueryEmployeeSchema` 类继承自 Pydantic 的 `BaseModel`，用于规范 SQL 查询工具的输入参数格式，确保传入的 SQL 语句符合预期结构

```python
class QueryEmployeeSchema(BaseModel):
    sql: str = Field(...,description="sql语句")
```

### 6. 执行SQL语句

- **调试输出**：将生成的 SQL 语句打印到 `sys.stderr`，避免干扰 stdout 上的 JSON-RPC 协议通信。
- **安全拦截**：在执行前检查 SQL 内容，若包含删除、修改等高危关键词则直接拒绝，防止数据被篡改。
- **连接数据库**：调用自定义工具获取数据库连接和游标对象。
- **执行查询**：运行 SQL 语句并获取所有结果集。
- **资源释放**：使用 `finally` 块确保无论执行成功与否，游标和数据库连接都会被关闭。

```python
@app.tool(
    description="执行 sql 语句查询；数据库模型：表名：employee，字段：user_id 员工ID编号,user_name 员工名字,email 员工邮箱,department 员工所属部门；规则：禁止生成DELETE、UPDATE、INSERT语句"
)
def mysql_tool(t: QueryEmployeeSchema)->str:
    """
    描述：MySQL工具
    :param sql: SQL语句
    :return: 返回成功200或失败500
    """
    print(f"生成的sql语句：{t}",file=sys.stderr)
    conn = None
    cur = None
    # 兜底操作
    sql = t.sql
    if "DELETE" in sql.upper() or "UPDATE" in sql.upper() or "INSERT" in sql.upper() or "DROP" in sql.upper() or "CREATE" in sql.upper() or "ALTER" in sql.upper():
        return "禁止执行非法sql语句操作"
    try:
        conn = GetMySQLConn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return str(result)
    except Exception as e:
        print(f"执行sql语句失败：{e}")
        return "执行sql语句失败"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
```

### 7. 主程序

判断文件是否为主程序入口，若是则启动应用，指定传输协议为 `stdio`，通过标准输入输出与客户端进行交互

```python
if __name__ == '__main__':
    app.run(
        transport = 'stdio',
    )
```

## （二）客户端

实现了一个基于 stdio 协议的异步客户端。它通过直接启动服务端进程的方式建立连接，演示了如何配置子进程参数、初始化会话以及调用远程工具。同样包含了针对 Windows 环境的编码修复逻辑

### 1. 导入库

引入异步编程库 `asyncio` 以及 MCP 官方的 stdio 客户端模块和会话管理模块，用于发起进程间通信

```python
import asyncio

from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
```

### 2. 强制编码

与服务端保持一致，强制将客户端的标准输出和标准错误流设置为 `utf-8` 编码，确保通信数据的完整性

```python
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
```

### 3. 构建启动服务器命令

- **定义路径**：指定服务端脚本所在的绝对路径目录。
- **定义脚本**：指定要运行的 Python 文件名。
- **构建参数**：使用 `StdioServerParameters` 组装启动命令，包含解释器（python）、工作目录（cwd）和启动参数（args），告诉客户端如何拉起服务端进程。

```python
# 定义客户端所在的目录
dir = r"G:\GitHub\Stu_AI\StuAgent\MCP服务应用程序开发"

# 定义客户端的启动程序
p = "002-基于stdio协议的MCP服务端.py"

# 构建命令
c = StdioServerParameters(
    command="python",   # 编译命令
    cwd = dir,  # 启动程序所在目录
    args=[p],   # 编译的启动程序文件（带后缀）
)
```

### 4. 定义异步函数

- **建立连接**：使用 `stdio_client` 根据构建好的命令启动子进程，并获得读写流。
- **初始化会话**：创建 `ClientSession` 并调用 `initialize()` 完成握手。
- **获取工具**：调用 `list_tools()` 获取服务端注册的所有可用工具信息。
- **调用工具**：通过 `call_tool` 触发远程功能（如 SQL 查询），注意参数需按照 Pydantic 模型的嵌套结构传递。
- **处理结果**：打印返回对象的原始数据及结构化内容中的具体结果字段。

```python
async def test():
    async with stdio_client(c) as (read,write):
        async with ClientSession(read,write) as session:
            # 初始化
            await session.initialize()
            # 获取工具列表
            tools = await session.list_tools()
            print(tools)
            # 调用工具
            # email_data = await session.call_tool("send_email_tool", {"to": "2920242909@qq.com", "subject": "测试邮件","content": "测试邮件内容"})
            # print(email_data)
            # print(email_data.structuredContent["result"])
            sql_data = await session.call_tool("mysql_tool", {"t": {"sql":"select * from employee"}})
            print(sql_data)
            print(sql_data.structuredContent["result"])
```

### 5. 主程序

判断是否为主程序入口，使用 `asyncio.run()` 启动定义的异步测试函数

```python
if __name__ == '__main__':
    asyncio.run(test())
```

# 四、基于SSE协议的langchain1.x版本调用

## （一）服务端

本部分作为调用逻辑的前置依赖，支持灵活切换底层通信协议。

开发者可根据部署环境选择启动基于标准输入输出（stdio）的本地进程服务，或基于服务器发送事件（SSE）的网络 HTTP 服务，为上层 LangChain 智能体提供统一的工具能力接口

运行（二选一）：

- 基于stdio协议的MCP的服务端
- 基于SSE 协议的MCP的服务端

- 

## （二）客户端

展示了如何在 LangChain 1.x 框架中集成 MCP 协议。通过 `MultiServerMCPClient` 适配器，将远程或本地的 MCP 工具转换为 LangChain 可用的标准工具对象。代码构建了包含大模型、工具和系统提示词的异步智能体（Agent），实现了从自然语言指令到具体工具调用的自动化流程

### 1. 导入库

引入 LangChain 核心消息类（HumanMessage）、自定义模型封装模块、智能体创建工厂函数，以及关键的 MCP 适配器客户端（MultiServerMCPClient）和异步支持库

```python
from langchain_core.messages import HumanMessage
from model import my_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
```

### 2. 基于SSE配置MCP客户端

- **实例化适配器**：创建 `MultiServerMCPClient` 对象，用于管理多服务器连接。
- **定义连接参数**：配置名为 `mytool` 的服务节点，指定传输协议为 `sse`。
- **设置网络地址**：填入服务端监听的 URL（`http://127.0.0.1:9000/sse`）。
- **配置鉴权头**：在 `headers` 中添加 `Authorization` 字段，携带 Bearer Token 以通过服务端的身份验证。

```python
client_sse = MultiServerMCPClient({
    "mytool":{
        "transport":"sse",
        "url":"http://127.0.0.1:9000/sse",
        "headers":{
            "Authorization": f"Bearer 130806"
        }
    }
})
```

### 3. 基于stdio协议配置MCP客户端

- **定义本地参数**：配置名为 `mytool` 的服务节点，指定传输协议为 `stdio`。
- **指定执行命令**：设置启动命令为 `python`，并指定工作目录（cwd）和具体的脚本文件名。
- **用途说明**：此配置用于在本地直接拉起子进程进行通信，通常用于开发调试或单机部署场景，无需网络端口。

```python
client_stdio = MultiServerMCPClient({
    "mytool":{
        "transport":"stdio",
        "command":"python",
        "cwd":r"G:\GitHub\Stu_AI\StuAgent\my_MCP",
        "args":["002-基于stdio协议的MCP服务端.py"],
    }
})
```

### 4. 创建异步智能体

- **初始化模型**：调用自定义模块获取配置好的大语言模型实例。
- **加载工具**：异步调用客户端的 `get_tools()` 方法，将 MCP 服务端的工具动态注册到当前环境。
- **设定人设**：定义系统提示词（System Prompt），赋予 AI “专业邮件助手” 的角色身份。
- **构建 Agent**：使用 `create_agent` 工厂函数，组合模型、工具列表和提示词，开启调试模式（debug=True）以便观察执行过程。
- **构造消息**：将用户的自然语言问题封装为 `HumanMessage` 对象，并放入标准的消息列表中。
- **执行推理**：调用 `agent.ainvoke()` 触发非流式推理，等待模型规划并执行工具调用。
- **提取结果**：从返回的消息历史中提取最后一条消息的内容作为最终答案并打印。

```python
async def create_email_agent(que):
    # 创建一个大模型
    model = my_model.MyModel.get_model()

    # 创建一个工具
    # tools = []
    tools = await client_sse.get_tools()
    print(tools)

    # 创建提示词 -- 系统提示词
    prompt = """
    	-- 角色：你是一个专业的邮件助手
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=True,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que)
    ]}

    # 回答
    result = await agent.ainvoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content

    print(data)
    return data
```

### 5. 主程序

- **定义任务**：设定具体的自然语言指令，例如“给指定邮箱发送一封测试邮件”。
- **启动执行**：使用 `asyncio.run()` 入口函数启动异步协程，开始智能体的工作流程。

```python
if __name__ == '__main__':
    que = "给2920242909@qq.com发送一封邮件，主题是测试邮件，内容是测试邮件内容"
    asyncio.run(create_email_agent(que))
```

# 五、阿里的MCP广场

## （一）应用

本部分演示了如何通过原生 MCP 客户端直接调用阿里云 DashScope 平台提供的远程工具服务。代码展示了基于 SSE 协议的连接建立、身份验证以及特定工具（如网页抓取）的调用流程，验证了云端 MCP 服务的可用性

```python
import asyncio
from fastmcp import Client
import os

api_key = os.getenv("DASHSCOPE_API_KEY")

#定义异步
async def test():
    #定义客户端
    async with Client("https://dashscope.aliyuncs.com/api/v1/mcps/WebFetch/mcp",auth=f"Bearer {api_key}") as client:
          #获取工具列表
          rs = await client.list_tools()
          print(rs)
          data = await  client.call_tool("web_fetch",{"url":"https://www.swpu.edu.cn/"})
          print(data)
          print(data.content[0].text)

if __name__ == '__main__':
    asyncio.run(test())
```

## （二）智能体演示

将阿里云的远程 MCP 工具集成到了 LangChain 智能体框架中。通过适配器模式，将云端的网页抓取能力转化为智能体可调用的本地工具对象，使大模型能够根据自然语言指令自动执行联网搜索或内容提取任务

### 1. 导入库

引入 LangChain 的消息类、自定义模型模块、智能体创建工厂、MCP 多服务器适配器客户端以及异步和环境变量支持库

```python
from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

import asyncio
import os
```

### 2. 获取密钥

从环境变量中读取 `DASHSCOPE_API_KEY`，用于配置 MCP 客户端的连接鉴权信息

```python
api_key = os.getenv("DASHSCOPE_API_KEY")
```

### 3. 基于SSE或者http协议配置MCP客户端

- **实例化适配器**：创建 `MultiServerMCPClient` 实例以管理远程连接。
- **配置节点**：定义名为 `mytool` 的服务节点，指定传输协议为 `http`（或 SSE）。
- **设置端点**：填入阿里云 DashScope 的 WebFetch 服务 URL。
- **配置鉴权**：在 headers 中添加 `Authorization` 字段，使用 Bearer Token 格式传递 API Key。

```python
client_http = MultiServerMCPClient({
    "mytool":{
        "transport":"http",
        "url":"https://dashscope.aliyuncs.com/api/v1/mcps/WebFetch/mcp",
        "headers":{
            "Authorization":f"Bearer {api_key}"
        }
    }
})
```

### 4. 创建异步智能体

- **初始化模型**：获取配置好的大语言模型实例作为智能体的大脑。
- **加载工具**：异步调用客户端的 `get_tools()` 方法，将云端工具注册到智能体。
- **设定人设**：定义系统提示词，赋予 AI “专业聊天助手” 的角色。
- **构建 Agent**：组合模型、工具和提示词创建智能体，开启调试模式以便观察执行链路。
- **构造消息**：将用户的自然语言问题封装为 `HumanMessage` 对象。
- **执行推理**：调用 `agent.ainvoke()` 触发非流式推理，等待模型规划并执行工具调用。
- **提取结果**：从返回的消息历史中提取最后一条消息的内容作为最终答案。

```python
async def create_email_agent(que):
    # 创建一个大模型
    model = my_model.MyModel.get_model()

    # 创建一个工具
    # tools = []
    tools = await client_http.get_tools()
    print(tools)

    # 创建提示词 -- 系统提示词
    prompt = """
    	-- 角色：你是一个专业的聊天助手
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=True,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que)
    ]}

    # 回答
    result = await agent.ainvoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content


    print(data)
    return data
```

### 5. 主程序

- **定义任务**：设定具体的自然语言指令，例如要求爬取西南石油大学官网的特定日期公告。
- **启动执行**：使用 `asyncio.run()` 启动异步协程，开始智能体的工作流程。

```python
if __name__ == '__main__':
    # que = "请爬取这个网址：https://www.swpu.edu.cn/，提取通知公告，6月16日的数据"
    que = "请爬取西南石油大学官网，提取通知公告，6月16日的数据"
    asyncio.run(create_email_agent(que))
```

# 六、魔搭社区的MCP

## （一）应用

演示了如何调用魔搭社区（ModelScope）提供的远程 MCP 服务。与阿里云类似，它展示了通过原生客户端连接到 ModelScope 推理 API 网关的过程，重点在于验证不同社区平台的 MCP 接口连通性

```python
import asyncio
from fastmcp import Client
import os

api_key = os.getenv("DASHSCOPE_API_KEY")

#定义异步
async def test():
    #定义客户端
    async with Client("https://mcp.api-inference.modelscope.net/5d216f91ea7142/mcp") as client:
          #获取工具列表
          rs = await client.list_tools()
          print(rs)
          # data = await  client.call_tool("web_fetch",{"url":"https://www.swpu.edu.cn/"})
          # print(data)
          # print(data.content[0].text)

if __name__ == '__main__':
    asyncio.run(test())
```

## （二）智能体演示

将魔搭社区的远程 MCP 工具集成到 LangChain 智能体中。通过配置 HTTP 流式传输协议，使智能体能够利用 ModelScope 上的模型能力来处理复杂任务，如查询火车票余票信息

### 1. 导入库

引入 LangChain 核心组件（消息、智能体工厂）、自定义模型模块、MCP 适配器客户端以及异步支持库

```python
from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

import asyncio
```

### 2. 基于SSE或者http协议配置MCP客户端

- **实例化适配器**：创建 `MultiServerMCPClient` 实例。
- **配置协议**：指定传输协议为 `streamable_http`，这是 ModelScope 推荐的流式 HTTP 传输方式。
- **设置端点**：填入魔搭社区特定的 MCP 推理服务 URL。

```python
client_http = MultiServerMCPClient({
    "mytool":{
        "transport":"streamable_http",
        "url":"https://mcp.api-inference.modelscope.net/5d216f91ea7142/mcp",
    }
})
```

### 3. 创建异步智能体

- **初始化模型**：获取大语言模型实例。
- **加载工具**：异步获取魔搭社区提供的工具集。
- **设定人设**：定义系统提示词，赋予 AI “专业邮件助手” 的角色（注：此处提示词可能需根据实际任务调整，如改为“出行助手”）。
- **构建 Agent**：组合模型、工具和提示词创建智能体，此处关闭了调试模式（`debug=False`）以适应生产或正式测试环境。
- **执行推理**：封装用户指令并调用 `ainvoke`，获取模型经过工具增强后的回答。

```python
async def create_email_agent(que):
    # 创建一个大模型
    model = my_model.MyModel.get_model()

    # 创建一个工具
    # tools = []
    tools = await client_http.get_tools()
    print(tools)

    # 创建提示词 -- 系统提示词
    prompt = """
    	-- 角色：你是一个专业的邮件助手
    """

    # 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=False,  # 可选，一般用于调试，生成环境必须设置为false
        middleware=[]
    )

    # 提问
    human_msg = {"messages":[
        HumanMessage(content=que)
    ]}

    # 回答
    result = await agent.ainvoke(human_msg)    # 非流式输出
    data = result["messages"][-1].content


    print(data)
    return data
```

### 4. 主程序

- **定义任务**：设定具体的查询指令，例如“查询 2026 年 9 月 12 日重庆到成都的火车票余票”。
- **启动执行**：使用 `asyncio.run()` 启动异步协程，执行智能体任务。

```python
if __name__ == '__main__':
    # que = "请爬取这个网址：https://www.swpu.edu.cn/，提取通知公告，6月16日的数据"
    # que = "请爬取西南石油大学官网，提取通知公告，6月16日的数据"
    que = "2026年9月12日重庆到成都的火车票的余票信息，下午三点以后"
    # 异步调用
    asyncio.run(create_email_agent(que))
```

# 七、密钥验证

## （一）密钥验证器

定义了一个自定义的 `KeyVerifier` 类，继承自 FastMCP 的 `TokenVerifier`。它实现了一个简易的硬编码鉴权逻辑，用于在 MCP 服务端拦截并校验客户端传入的 Token，确保只有持有特定凭证的请求才能访问服务。

- **继承基类**：`KeyVerifier` 继承 `TokenVerifier`，并重写 `verify_token` 异步方法。
- **硬编码校验**：在方法内部直接判断传入的 `token` 字符串是否等于 `"130806"`。
- 返回凭证：
    - 若匹配成功，返回一个 `AccessToken` 对象，其中包含 `token` 本身、客户端 ID（`client_id="1108"`）以及权限范围（`scopes=[]`，此处为空表示未限制具体权限或默认全权）。
    - 若匹配失败，返回 `None`，表示验证未通过。
- **调试输出**：打印接收到的 token 以便调试观察。

```python
from fastmcp.server.auth import TokenVerifier, AccessToken

class KeyVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        print("verify_token",token)
        # 允许访问
        if token == "130806":
            return AccessToken(
                token=token,
                client_id="1108",
                scopes=[],
                # scopes=["read", "write"],   # 允许访问的权限信息
            )
        else:
            return None
```

## （二）验证密钥是否生效

### 1. 导入库

引入 FastMCP 框架、邮件与数据库相关库、环境变量加载器，以及上一步定义的自定义验证器 `KeyVerifier`，为构建受保护的服务端做准备。

```python
from fastmcp import FastMCP
from email.mime.text import MIMEText    # 写邮件
import smtplib  # 发送邮件
from dotenv import load_dotenv
import os
from my_MCP.keyVerifier import KeyVerifier

from pydantic import BaseModel,Field
from util.mysql_conn import GetMySQLConn
```

### 2. 引入环境，创建应用程序

加载 `.env` 配置文件，并在初始化 `FastMCP` 实例时，通过 `auth=KeyVerifier()` 参数注入自定义的鉴权逻辑，使服务启动时即开启 Token 验证功能

```
load_dotenv()
# 创建应用程序
app = FastMCP(auth=KeyVerifier())
```

### 3. 定义发送邮件工具

- **注册工具**：使用装饰器注册 `send_email_tool`。
- **读取配置**：从环境变量获取 SMTP 服务器地址、端口、账号密码等敏感信息。
- **构建邮件**：封装 MIMEText 邮件对象，设置收件人、主题和发件人。
- **发送执行**：建立 SSL 连接，登录服务器并发送邮件。
- **异常处理**：捕获发送过程中的错误，返回明确的成功或失败状态字符串。

```python
@app.tool('send_email_tool')
def send_email_tool(to: str, subject: str, content: str)->str:
    """
    描述：发送邮件工具
    :param to: 收件人
    :param subject: 主题
    :param content: 邮件内容
    :return: 返回成功200或失败500
    """
    # 每个工具都要加异常处理
    try:
        # 读取配置文件信息
        email = os.getenv("SENDER_EMAIL")   # 发件人邮箱
        host = os.getenv("EMAIL_HOST")
        port = os.getenv("EMAIL_PORT")
        password = os.getenv("SENDER_EMAIL_PASSWORD")
        # 判断配置是否读取成功
        if not email or not host or not port or not password:
            raise Exception("配置文件信息读取失败")
        # 创建邮件对象
        msg = MIMEText(content)
        msg['To'] = to  # 收件人
        msg['Subject'] = subject    # 邮件主题
        msg['From'] = email  # 发件人
        # 创建一个链接邮件服务器地址
        with smtplib.SMTP_SSL(host,int(port)) as smtp:  # port读取出来为字符串，需要转换为int
            # 登录邮件服务器
            smtp.login(email,password)
            # 发送邮件
            smtp.sendmail(email,to,msg.as_string())
        return "发送邮件成功"
    except Exception as e:
        print(f"发送邮件失败:{e}")
        return f"发送邮件失败：{e}"
```

### 4. 参数校验

定义 `QueryEmployeeSchema` 类继承自 Pydantic 的 `BaseModel`，用于规范 SQL 查询工具的输入参数格式，确保传入的 SQL 语句符合预期结构。

```python
class QueryEmployeeSchema(BaseModel):
    sql: str = Field(...,description="sql语句")
```

### 5. 定义执行SQL语句工具

- **安全拦截**：在执行前检查 SQL 内容，若包含 DELETE、UPDATE 等高危关键词则直接拒绝，防止数据被篡改。
- **连接数据库**：调用自定义工具获取数据库连接和游标对象。
- **执行查询**：运行 SQL 语句并获取所有结果集。
- **资源释放**：使用 `finally` 块确保无论执行成功与否，游标和数据库连接都会被关闭。

```python
@app.tool(
    description="执行 sql 语句查询；数据库模型：表名：employee，字段：user_id 员工ID编号,user_name 员工名字,email 员工邮箱,department 员工所属部门；规则：禁止生成DELETE、UPDATE、INSERT语句"
)
def mysql_tool(sql: QueryEmployeeSchema)->str:
    """
    描述：MySQL工具
    :param sql: SQL语句
    :return: 返回成功200或失败500
    """
    print(f"生成的sql语句：{sql}")
    conn = None
    cur = None
    # 兜底操作
    sql = sql.sql
    if "DELETE" in sql.upper() or "UPDATE" in sql.upper() or "INSERT" in sql.upper() or "DROP" in sql.upper() or "CREATE" in sql.upper() or "ALTER" in sql.upper():
        return "禁止执行非法sql语句操作"
    try:
        conn = GetMySQLConn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return str(result)
    except Exception as e:
        print(f"执行sql语句失败：{e}")
        return "执行sql语句失败"
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
```

### 6. 主程序

判断文件是否为主程序入口，若是则启动应用，监听本地 9000 端口，指定使用 SSE 传输协议。此时服务端已具备鉴权能力，客户端连接时必须携带正确的 Token。

```python
if __name__ == '__main__':
    app.run(
        host = "localhost",
        port = 9000,
        transport = 'sse',
    )
```

