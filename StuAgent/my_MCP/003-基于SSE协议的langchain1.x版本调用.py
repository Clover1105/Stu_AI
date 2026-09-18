from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

import asyncio

# 基于SSE配置MCP客户端
client_sse = MultiServerMCPClient({
    "mytool":{
        "transport":"sse",
        "url":"http://127.0.0.1:9000/sse",
        "headers":{
            "Authorization": f"Bearer 130806"
        }
    }
})

# # 基于stdio协议配置
# client_stdio = MultiServerMCPClient({
#     "mytool":{
#         "transport":"stdio",
#         "command":"python",
#         "cwd":r"G:\GitHub\Stu_AI\StuAgent\my_MCP",
#         "args":["002-基于stdio协议的MCP服务端.py"],
#         # "args":["006-验证密钥是否生效.py"]
#     }
# })

"""创建智能体步骤"""
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


if __name__ == '__main__':
    que = "给2920242909@qq.com发送一封邮件，主题是测试邮件，内容是测试邮件内容"
    asyncio.run(create_email_agent(que))
