from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

import asyncio

# 基于SSE或者http协议配置MCP客户端
client_http = MultiServerMCPClient({
    "mytool":{
        "transport":"streamable_http",
        "url":"https://mcp.api-inference.modelscope.net/5d216f91ea7142/mcp",
    }
})

"""创建智能体步骤"""
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


if __name__ == '__main__':
    # que = "请爬取这个网址：https://www.swpu.edu.cn/，提取通知公告，6月16日的数据"
    # que = "请爬取西南石油大学官网，提取通知公告，6月16日的数据"
    que = "2026年9月12日重庆到成都的火车票的余票信息，下午三点以后"
    # 异步调用
    asyncio.run(create_email_agent(que))
