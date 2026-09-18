from langchain.agents import create_agent
from model.my_model import MyModel
from langchain_core.messages import HumanMessage
from memory.save.profile_memory import ProfileMemory
from pydantic import BaseModel,Field

class ProfileParams(BaseModel):
    name:str = Field(description="姓名")
    age:int = Field(description="年龄")
    job:str = Field(description="职业")
    address:str = Field(description="地址")
    hobby:str = Field(description="爱好")
    xueli:str = Field(description="学历")

"""
用户画像记忆智能体
"""

class ProfileAgent:
    def __init__(self,profile_memory:ProfileMemory):
        self.model = MyModel.get_model()
        self.prompt = self.get_prompt()
        self.agent = self.get_agent()
        # 获取摘要记录的保存对象
        self.profile_memory = profile_memory

    def get_prompt(self):
        self.prompt = """
        -- 角色：你是一个用户画像提取助手
        -- 任务：
            - 根据用户问题提取相关用户画像信息
        -- 规则：
            - 用户画像信息包含以下信息：姓名，年龄，爱好，职业，地址，学历
            - 去掉闲聊内容
            - 避免重复
            - 使用第三人称描述
            - 不要做总结，只记录重要信息即可
            - 如果没有用户画像信息，返回空
        -- 输出：
            - 只输出姓名，年龄，职业，地址，学历
        -- 示例：
            用户输入：我喜欢打游戏
            输出:{'name': '', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
             
            用户输入：我是张三
            输出:{'name': '张三', 'age': 0, 'job': '', 'address': '', 'xueli': ''}
        """
        return self.prompt

    def get_agent(self):
        self.agent = create_agent(
            model = self.model,
            tools=[],
            system_prompt=self.prompt,
            debug=True,  # 可选，一般用于调试，生成环境必须设置为false
            middleware=[],
            response_format=ProfileParams
        )
        return self.agent

    # 业务代码 -- 记忆更新 -- messages：窗口记忆的消息
    def update(self,question):
        # 获得回答
        result = self.agent.invoke({"messages":[HumanMessage(content=question)]})
        # 存储长期记忆
        data = result['structured_response'].model_dump()
        for key,value in data.items():
            if value:
                print("有用户画像")
                print(f"{key}:{value}")
                self.profile_memory.save_profile(key,value)
        return data







if __name__ == '__main__':
    profile_memory = ProfileMemory(1)
    agent = ProfileAgent(profile_memory)
    q1 = "roy喜欢蹦蹦跳跳的"
    q2 = "roy是个很内向的男孩"
    q3 = "roy很爱小汤圆"
    r = agent.update(q1)
    print(r)












