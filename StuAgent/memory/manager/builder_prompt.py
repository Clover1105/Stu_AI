from memory.save.window_memory import WindowMemory
from memory.save.summary_memory import SummaryMemory
from memory.save.long_memory import LongMemory
from memory.save.profile_memory import ProfileMemory

class BuilderPrompt:
    def __init__(self,session_id,user_id):
        self.window_memory = WindowMemory(session_id)
        self.summary_memory = SummaryMemory(session_id)
        self.long_memory = LongMemory()
        self.profile_memory = ProfileMemory(user_id)

    # 构建提示词
    def builder_prompt(self,user_id,que):
        prompt = """
         -- 角色：你是一个记忆提取助手
         -- 任务：
            - 理解用户需求
            - 根据用户问题，提取相关记忆
        """
        # 查询窗口记忆 -- 提取记忆
        window_memory = self.window_memory.query()
        prompt += "短期记忆 -- 窗口记忆"
        for i in window_memory:
            if i['role'] == 'user':
                prompt += f"用户提问：{i['content']}"
            else:
                prompt += f"AI回复：{i['content']}"

        # 查询摘要记忆 -- 提取记忆
        summary_memory = self.summary_memory.query_summary()
        prompt += "短期记忆 -- 摘要记忆"
        prompt += summary_memory

        # 查询长期记忆 -- 提取记忆
        long_memory = self.long_memory.query_long(user_id,que)
        prompt += "长期记忆"
        for x in long_memory:
            prompt += x+'\n'

        # 查询用户画像 -- 提取记忆
        profile_memory = self.profile_memory.query_profile()
        prompt += f"用户画像：{profile_memory}"
        return prompt