from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.config import get_stream_writer

from app.ai.model.my_model import MyModel
from app.ai.agent.multi_agent.state.exam_state import ExamState
from app.ai.prompt.bulider_prompt import BuilderPromptYaml

"""
评价节点，对用户的答题内容进行评价
"""

# 读取外部提示词配置文件
prompt = BuilderPromptYaml.get_prompt("evaluate_node.yaml")

async def evaluate_node(state:ExamState):
    print("\n【测试】这里是 -- evaluate_node.py")

    # 获取问题列表
    question_list = state["questions"]
    # 获取用户答案列表
    user_answer_list = state["user_answer_list"]
    # 构建提问内容
    question = f"用户问题列表：{question_list}\n用户答案列表：{user_answer_list}"

    # 调用模型
    model = MyModel.get_model()

    # 提示词
    agent = create_agent(
        model = model,
        system_prompt=prompt,
    )

    # 提问
    user_msg = {"messages":[HumanMessage(content=question)]}

    # 异步流式
    result = []
    # 获取流式写入对象
    write = get_stream_writer()
    async for c,m in agent.astream(user_msg,stream_mode="messages"):
        if c.content:
            result.append(c.content)
            write(c.content)
    # result = await agent.invoke(user_msg)

    # ai_msg = f"\n开始评价{result['messages'][-1]}\n"
    ai_msg = ""
    return {
        "messages":[AIMessage(content=ai_msg)],
        "exam_step":"done"
    }