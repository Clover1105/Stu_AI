from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool

from pydantic import BaseModel,Field

# 类型校验
class code_format_schema(BaseModel):
    data:str = Field(description="验证码")
    code:str = Field(description="状态码，200表示成功，500表示失败")
    msg:str = Field(description="提示信息")



# 1. 创建一个大模型
model = my_model.MyModel.get_local_model()
# 2. 创建一个工具
tools = [SendEmailTool]
# 3. 创建提示词 -- 系统提示词
prompt = """
    -- 角色：你是一个专业的邮件发送助手
    -- 任务：
        - 理解用户需求
        - 生成一个不规则的4位数的数字作为验证码
        - 根据用户需求发送邮件
    -- 规则：
        - 验证码必须是4位
        - 如果邮件发送成功，状态码是200，提示信息是"邮件发送成功"
        - 如果邮件发送失败，状态码是500，提示信息是"邮件发送失败"
    -- 输出：
        - 输出内容是：验证码、状态码、提示信息
    -- 示例
        - 输入：邮箱是123456@qq.com,发送邮件
        - 输出：验证码，状态码，提示信息
"""
# 4. 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    response_format=code_format_schema,
    debug=True  # 可选，一般用于调试，生成环境必须设置为false
)


def create_email_agent(que):
    # 5. 提问
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    result = agent.invoke(human_msg)    # 非流式输出
    print(f"原始的：{result}")
    # 获取验证码信息
    json = result["structured_response"].model_dump()
    print(f"json:{json}")
    print(type(json))
    return json

if __name__ == '__main__':
    que = "请发送一封邮件给2920242909@qq.com"
    create_email_agent(que)