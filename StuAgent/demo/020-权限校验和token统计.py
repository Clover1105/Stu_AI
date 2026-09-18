from langchain_core.messages import HumanMessage

from model import my_model
from langchain.agents import create_agent

from middleware.permission_limit_middleware import PermissionCheckMiddleware,CountTokenMiddleware,CountTokenMemoryMiddleware


# 创建一个大模型
model = my_model.MyModel.get_model()
# 创建一个工具
tools = []
# 创建提示词 -- 系统提示词
prompt = """
	-- 角色：你是一个专业的聊天助手
"""
# 创建智能体
agent = create_agent(
    model, tools,
    system_prompt=prompt,
    debug=True,  # 可选，一般用于调试，生成环境必须设置为false
    middleware=[PermissionCheckMiddleware,CountTokenMemoryMiddleware]
)

"""创建智能体步骤"""
def create_email_agent(que):
    try:
        # 5. 提问
        human_msg = {"messages":[HumanMessage(content=que)]}
        # 6. 回答
        config = {"configurable":{"thread_id":"4"}}
        result = agent.invoke(human_msg,config)    # 非流式输出
        data = result["messages"][-1].content
        print(data)
        return data
    except Exception as e:
        print(f"权限校验和统计token报错:{e}")
        return "权限校验和统计token报错"

if __name__ == '__main__':
    que = "讲个脑筋急转弯"
    create_email_agent(que)