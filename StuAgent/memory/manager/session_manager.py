from memory.save.window_memory import WindowMemory
from memory.manager.builder_prompt import BuilderPrompt
from memory.save.summary_memory import SummaryMemory
from memory.save.long_memory import LongMemory
from memory.save.profile_memory import ProfileMemory
"""
会话管理器：
    主要负责四层记忆的对象创建和提示词的生成
"""

class SessionManager:
    def __init__(self,session_id:str,user_id):
        self.window_memory = WindowMemory(session_id)
        self.session_id = session_id
        self.b_p = BuilderPrompt(self.session_id,user_id)
        self.summary_memory = SummaryMemory(self.session_id)
        self.long_memory = LongMemory()
        self.profile_memory = ProfileMemory(user_id)

    # 添加窗口记忆
    def save_window_memory(self,role:str,content:str):
        self.window_memory.save_memory(role,content)

    # 构建提示词
    def builder_prompt(self,user_id,question):
        prompt = self.b_p.builder_prompt(user_id,question)
        return {"role":"system","content":prompt}
