from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.config import get_stream_writer

from app.ai.model.my_model import MyModel
from app.ai.agent.multi_agent.state.exam_state import ExamState
from app.ai.prompt.bulider_prompt import BuilderPromptYaml
from langchain.agents.middleware import ModelCallLimitMiddleware
"""
面试对话记忆节点
"""

# 读取外部提示词配置文件
prompt = BuilderPromptYaml.get_prompt("chat_node.yaml")

async def chat_node(state:ExamState):
    print("\n【测试】这里是 -- chat_node.py")

    try:
        # 获取用户问题和记忆信息
        memory = state["messages"]

        # 调用模型
        model = MyModel.get_local_model()

        # 提示词 -- 降级处理 -- 1.限制模型思考次数 2.换模型 3.人工提示
        agent = create_agent(
            model = model,
            system_prompt=prompt,
            debug=True,
            middleware=[
                ModelCallLimitMiddleware(
                    thread_limit=3,
                    exit_behavior="end",
                )
            ],
        )

        # 提问
        user_msg = {"messages":memory}

        # 异步流式
        result = []
        # 获取流式写入对象
        write = get_stream_writer()
        async for c,m in agent.astream(user_msg,stream_mode="messages"):
            if c.content:
                result.append(c.content)
                write(c.content)

        ai_msg = ""
        return {
            "messages":[AIMessage(content=ai_msg)],
            "exam_step":"done"
        }
    except Exception as e:
        print("【测试】大模型兜底")
        print(f"【测试】报错信息：{e}")
        try:
            # 获取用户问题和记忆信息
            memory = state["messages"]

            # 调用模型
            model = MyModel.get_model()

            # 提示词 -- 降级处理 -- 1.限制模型思考次数 2.换模型 3.人工提示
            agent = create_agent(
                model=model,
                system_prompt=prompt,
                debug=True,
                middleware=[
                    ModelCallLimitMiddleware(
                        thread_limit=3,
                        exit_behavior="end",
                    )
                ],
            )

            # 提问
            user_msg = {"messages": memory}

            # 异步流式
            result = []
            # 获取流式写入对象
            write = get_stream_writer()
            async for c, m in agent.astream(user_msg, stream_mode="messages"):
                if c.content:
                    result.append(c.content)
                    write(c.content)

            ai_msg = ""
            return {
                "messages": [AIMessage(content=ai_msg)],
                "exam_step": "done",
            }
        except Exception as e:
            print("【测试】超时了")
            print(f"【测试】报错信息：{e}")
            return {
                "messages":[AIMessage(content="\n请求超时，请稍后重试\n")],
                "exam_step":"done"
            }