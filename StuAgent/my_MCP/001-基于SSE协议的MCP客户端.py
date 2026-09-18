import asyncio
from fastmcp import Client

# 定义异步
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

if __name__ == '__main__':
    asyncio.run(test())