# 复制文件 -- 021-智能体的封装.py

from tool.send_email_tool import SendEmailTool
from model.my_model import MyModel
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

class EmailAgent:
    def __init__(self):
        self.model = MyModel.get_model()
        self.tools = self.get_tools()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()

    def get_tools(self):
        self.tools = [SendEmailTool]
        return self.tools

    def get_prompt(self):
        self.prompt = """
            -- 角色：你是一个专业的聊天助手
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools = self.tools,
            system_prompt = self.prompt,
            debug = True,
            middleware = []
        )
        return self.agent

# 业务代码 -- 异步流式问答
async def get_astream(self,que:str,user_id:str):
    # 提问
    human_msg = {"messages": [HumanMessage(content=que)]}
    # 构建记忆配置
    config = {"configurable": {"thread_id": user_id}}
    # 回答
    async for event in self.agent.astream_events(human_msg, version="v2", config=config):
        # print(event)
        # 获取事件内容
        event_name = event['event']  # 事件名称
        if event_name == 'on_chain_start':
            yield f"邮件智能体开始运行。。。\n\n"
        elif event_name == 'on_chain_end':
            yield f"邮件智能体停止运行！！！\n\n"
        elif event_name == 'on_chat_model_start':
            yield f"大模型开始思考。。。\n\n"
        elif event_name == 'on_chat_model_end':
            yield f"大模型思考结束！！！\n\n"
        elif event_name == 'on_chain_stream':
            yield f"大模型开始生成答案。。。\n\n"
        elif event_name == 'on_tool_start':
            # 获取工具名称
            tool_name = event['name']
            if tool_name == "QueryEmployeeTool":
                yield f"开始查询员工信息。。。\n\n"
            if tool_name == "SendEmailTool":
                yield f"开始发送邮件。。。\n\n"
        elif event_name == 'on_tool_end':
            # 获取工具返回值
            tool_output = event['data']['output'].content
            yield f"邮件工具执行完毕，执行结果为{tool_output}\n\n"
        elif event_name == 'on_chat_model_stream':
            data = event['data']['chunk'].content
            if data:
                yield data

if __name__ == '__main__':
    agent = EmailAgent()
    