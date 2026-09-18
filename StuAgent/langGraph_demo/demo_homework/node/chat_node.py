from langGraph_demo.demo_homework.state.email_state import EmailState
from langchain_core.messages import AIMessage,HumanMessage
from langchain.agents import create_agent
from model import my_model


def chat_node(state:EmailState):
    print("\n\n【测试】这里是chat_node.py\n")
    # print(f"【测试】接收到的state：{state}\n")
    prompt = """
        -- 角色：你是一个专业的聊天助手
    """
    model = my_model.MyModel.get_local_model()
    agent = create_agent(
        model = model,
        tools=[],
        system_prompt=prompt,
        middleware=[],
    )
    que_msg = {"messages": [{"role": "user", "content": state["messages"][0].content}]}
    result = agent.invoke(que_msg)
    result = result['messages'][1].content
    # print(f"【测试】大模型回复结果：{result}\n")
    return {
        "messages": [AIMessage(content=result)],
        "result": "聊天节点成功",
    }

if __name__ == '__main__':
    que = EmailState({'messages': [
        HumanMessage(content='你好呀！', additional_kwargs={}, response_metadata={})
    ]})
    print(chat_node(que))