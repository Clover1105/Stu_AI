from langchain.agents import create_agent
from model.my_model import MyModel
from memory.save.summary_memory import SummaryMemory
from langchain_core.messages import HumanMessage

"""
摘要智能体
"""

class SummaryAgent:
    def __init__(self,summary_memory:SummaryMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.summary_memory = summary_memory

    def get_prompt(self):
        self.prompt = """
         -- 角色：你是一个摘要生成助手
         -- 任务：
            - 根据旧摘要和最新的聊天记录生成新的摘要
         -- 规则：
            - 保留重要信息
            - 去掉闲聊内容
            - 避免重复
            - 控制在200字以内
            - 使用第三人称描述
            - 只返回新的摘要
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=False,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[]
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,messages):
        # 查询旧摘要
        old_summary = self.summary_memory.query_summary()
        # 最新聊天记录
        prompt = ""
        for i in messages:
            if i['role'] == 'user':
                prompt += f"用户提问：{i['content']}"
            # else:
            #     prompt += f"AI回复：{i['content']}"
        # 问题
        que = f"请根据旧摘要：{old_summary}和最新聊天记录：{prompt}"
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=que)]})
        # 把新摘要存入到摘要记忆中
        self.summary_memory.save_summary(result['messages'][-1].content)



if __name__ == '__main__':
    summary_memory = SummaryMemory(1)
    s = SummaryAgent(summary_memory)
    # 最近聊天记录
    record = [{'role': 'user', 'content': '你好，我叫张胜男'}, {'role': 'ai', 'content': '你好，张胜男'},
              {'role': 'user', 'content': 'langchain是什么'}, {'role': 'ai', 'content': 'langchain是一个智能体框架'}]
    s.update(record)













