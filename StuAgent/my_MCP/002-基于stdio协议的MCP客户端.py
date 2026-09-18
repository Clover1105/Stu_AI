import asyncio

from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

import sys
import io

# 强制将 stdout 和 stderr 设置为 utf-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 你的其他 MCP 服务端代码...


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

# 定义异步函数
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

if __name__ == '__main__':
    asyncio.run(test())