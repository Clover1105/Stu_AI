from memory.retrieval.SummaryAgent import SummaryAgent
from memory.manager.session_manager import SessionManager
from memory.retrieval.LongAgent import LongAgent
from memory.retrieval.ProfileAgent import ProfileAgent
"""

记忆管理器，管理记忆的更新
"""

class MemoryManager:
    def __init__(self,sessionManager:SessionManager):
        # 摘要智能体
        self.summary_agent = SummaryAgent(sessionManager.summary_memory)
        # 获取窗口记忆对象
        self.window_memory = sessionManager.window_memory
        # 创建长期记忆智能体
        self.long_agent = LongAgent(sessionManager.long_memory)
        # 创建用户画像智能体
        self.profile_agent = ProfileAgent(sessionManager.profile_memory)

    def update(self,user_id,question):
        # 查询，获取窗口记忆
        query_window = self.window_memory.query()
        # 更新长期记忆
        self.long_agent.update(user_id,question)
        # 更新用户画像记忆
        self.profile_agent.update(question)
        # 触发摘要
        if len(self.window_memory.query()) >= 2:
            # 更新摘要记忆
            self.summary_agent.update(query_window)