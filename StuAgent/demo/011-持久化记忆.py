from langchain_core.messages import HumanMessage

from model import MyModel
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool

from dotenv import load_dotenv
load_dotenv()
import os

from langgraph.checkpoint.postgres import PostgresSaver




def create_email_agent(que,user_id):
    # 1. 创建一个大模型
    model = MyModel.MyModel.get_model()

    # 2. 创建一个工具
    tools = [SendEmailTool,AddTool]

    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
        -- 规则：如果不调用工具，直接输出结果即可，不用给提示
    """

    # 创建数据库连接
    url = os.getenv("POSTGRESQL_URL")
    with PostgresSaver.from_conn_string(url) as pg:
        # 安装数据库和表
        # 运行情况 -- 第一种：创建需要执行；第二种：数据库名修改；第三种：langgraph 版本更新
        # pg.setup()

        # 5. 创建智能体
        agent = create_agent(
            model, tools,
            system_prompt=prompt,
            checkpointer=pg,
            # debug=True  # 可选，一般用于调试，生成环境必须设置为false
        )

        # 6. 提问
        # 定义一个人类消息类型格式（第一种）
        # human_msg = {"messages":[{"role":"user","content":que}]}
        # 定义一个人类消息类型格式（第二种）
        human_msg = {"messages":[HumanMessage(content=que)]}

        # 7. 构建记忆配置
        config = {'configurable':{'thread_id':user_id}}

        # 8. 回答
        result = agent.invoke(human_msg,config=config)    # 非流式输出
        return result["messages"][-1].content

if __name__ == '__main__':
    que = [
        "我是clover",
        "我19号要去看演唱会",
        "我是谁，19号要干嘛？"
    ]
    for i in range(len(que)):
        print(f"第{i+1}次提问：{que[i]}")
        result = create_email_agent(que[i],"1")
        print(f"第{i+1}次回答：{result}")