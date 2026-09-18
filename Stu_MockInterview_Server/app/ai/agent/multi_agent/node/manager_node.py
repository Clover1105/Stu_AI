from langchain_core.messages import HumanMessage
from app.ai.agent.multi_agent.state.exam_state import ExamState
from langgraph.types import Command
from langgraph.graph import END
from app.ai.agent.multi_agent.node.router_agent import router_agent

# 定义记忆关键字匹配
keyword = [
    "上一个问题","上一题"
]

# 定义一个函数，判断问题是否在记忆关键字匹配
def is_in_keyword(question):
    for k in keyword:
        if k in question:
            return True
    return False


"""
主管节点，中枢，复制调用其他节点
"""

def manager_node(state:ExamState):
    print('\n【测试】这里是 -- manager_node.py')
    print(f"【测试】状态：{state}")

    # 获取考试状态
    exam_state = state.get("exam_step","start")
    print(f"【测试】当前考试状态：{exam_state}")

    # 获取用户输入
    last_msg = state["messages"][-1]
    if isinstance(last_msg, HumanMessage):
        user_input = last_msg.content
        print("【测试】人类问题", user_input)
        if is_in_keyword(user_input):
            # 进入对话记忆节点
            print("【测试】关键字命中，进入关键字匹配......")
            return Command(goto="chat")
        print("【测试】意图识别，模型兜底")
        router = router_agent(user_input)
        print(f"【测试】路由结果：{router}")
        if router == "exam":
            return Command(goto="intent")
        if router == "answer":
            return Command(goto="answer")
        if router == "chat":
            return Command(goto="chat")
    else:
        user_input = ""
    print(f"【测试】用户输入：{user_input}")

    # 获取是否继续出题
    continue_question = state.get("continue_question",True)

    # 如果是第一次进入
    if exam_state == "start":
        # 调用意图识别节点
        return Command(goto="intent")
    elif exam_state == "intent":
        # 调用意图识别节点
        return Command(goto="question")
    elif exam_state == "question":
        if user_input == "":
            print("【测试】等待用户输入答案...")
            # 调用意图识别节点
            return Command(goto=END)
        else:
            # 进入答案节点
            return Command(goto="answer")
    elif exam_state == "answer":
        if continue_question:
            print("【测试】继续出题...")
            # 调用意图识别节点
            return Command(goto="question")
        else:
            print("【测试】答题结束，进入评价...")
            # 调用意图识别节点
            return Command(goto="evaluate")
    elif exam_state == "evaluate":
        # 调用意图识别节点
        return Command(goto="evaluate")
    elif exam_state == "done":  # 评价结束
        # 调用意图识别节点
        return Command(goto=END, update={
            "exam_step":"start",    # 从头开始
            "questions":[],
            "user_answer_list":[],
            "current":0,
        })
    else:
        return Command(goto=END)