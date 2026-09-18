from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from tool.send_email_tool import SendEmailTool
from tool.add_tool import AddTool

"""创建智能体步骤"""
def create_email_agent(que):
    # 1. 创建一个大模型
    model = my_model.MyModel.get_model()
    # 2. 创建一个工具
    tools = [SendEmailTool,AddTool]
    # 3. 创建提示词 -- 系统提示词
    prompt = """
        -- 角色：你是一个专业的邮件发送助手
    """
    # 4. 创建智能体
    agent = create_agent(
        model, tools,
        system_prompt=prompt,
        debug=True  # 可选，一般用于调试，生成环境必须设置为false
    )
    # 5. 提问
    # 定义一个人类消息类型格式（第一种）
    # human_msg = {"messages":[{"role":"user","content":que}]}
    # 定义一个人类消息类型格式（第二种）
    human_msg = {"messages":[HumanMessage(content=que)]}
    # 6. 回答
    result = agent.invoke(human_msg)    # 非流式输出
    print(result)

if __name__ == '__main__':
    # 1967532979@qq.com、3131355723@qq.com、2018561771@qq.com、3010207312@qq.com
    # 请发送一封邮件给1967532979@qq.com，恭喜她成功抢到了蒲熠星巡回演唱会《银河系旅行》成都站的门票，请她2026年9月26日准时参加，另天气炎热注意避暑！（内容丰富一些有热情）
    # 请以热情真挚的粉丝向口吻，给1967532979@qq.com写一封恭喜抢到蒲熠星《银河系旅行》成都站门票的邮件，融入专属情感与主题意象，内容丰富地提醒2026年9月26日准时参加及成都秋季防暑注意事项（发件人是蒲熠星，收件人是满天星）
    # que = "请发送一封邮件给3131355723@qq.com，内容为一段心灵鸡汤"
    que = "3+4的结果"
    create_email_agent(que)