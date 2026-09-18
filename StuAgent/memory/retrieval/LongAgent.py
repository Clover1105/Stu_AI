from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.long_memory import LongMemory

"""
长期记忆智能体
"""

class LongAgent:
    def __init__(self,long_memory:LongMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取长期记忆的保存对象
        self.long_memory = long_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个长期记忆助手
         -- 任务：
            - 根据用户问题提取相关的长期记忆信息
         -- 规则：
            - 如果用户输入是陈述句（例如：“我叫张三”，“我喜欢Python”），请从中提取关键事实（如姓名、爱好、技能等），并以简洁的第三人称形式输出，用于更新记忆。
            - 如果用户输入是疑问句（例如：“我叫什么？”，“我擅长什么？”），请直接输出“NO_UPDATE”，表示无需更新记忆。
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,user_id,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        self.long_memory.save_long(user_id,result['messages'][-1].content)
        print("长期记忆更新成功")







if __name__ == '__main__':
    long_memory = LongMemory()
    l = LongAgent(long_memory)
    q1 = "roy喜欢蹦蹦跳跳的"
    q2 = "roy是个很内向的男孩"
    q3 = "roy很爱小汤圆"
    l.update("1",q3)