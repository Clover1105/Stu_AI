from app.ai.agent.multi_agent.scheam.intent_scheam import IntentSchema
from app.ai.agent.multi_agent.state.exam_state import ExamState
from app.ai.model.my_model import MyModel
from app.ai.prompt.bulider_prompt import BuilderPromptYaml
from langchain.agents import create_agent
from langchain_core.messages import AIMessage

# 意图识别节点

# 读取外部提示词配置文件
prompt = BuilderPromptYaml.get_prompt("intent_node.yaml")

# 创建意图识别智能体
def intent_node(state:ExamState):
    print('\n【测试】这里是 -- intent_node.py')
    print(f"【测试】状态：{state}")
    # 获取用户输入
    user_input = state["messages"][-1].content
    print(f"【测试】用户输入：{user_input}")
    # 获取本地模型
    model = MyModel.get_local_model()
    # 创建智能体
    agent = create_agent(
        model=model,
        system_prompt=prompt,
        response_format=IntentSchema,
    )
    # 提问
    user_msg = {"messages":{"role":"user","content":user_input}}
    rs = agent.invoke(user_msg)
    # 将输入结果转换为字典，json
    data = rs["structured_response"].model_dump()
    # 自定义AI消息
    ai_msg = f"\n意图识别成功：课程名称:{data["course"]},课程数量:{data["num"]}\n"
    # 更新状态
    return {
        "messages":[AIMessage(content=ai_msg)],
        "course":data["course"],
        "total":data["num"],
        "exam_step":"intent"
    }



