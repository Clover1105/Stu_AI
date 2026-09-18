from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

"""
考试节点状态
"""

class ExamState(TypedDict):
    print("\n【测试】这里是 -- exam_state.py")
    # AI 消息列表
    messages:Annotated[list[AnyMessage],operator.add]

    # 意图识别节点
    # 课程
    course:str
    # 题目数量
    total:int   # 总计

    # 出题节点
    # 题库列表
    questions:list[dict[str, any]]
    # 当前题目
    current_question:str

    # 收集用户答案节点
    # 用户的答案列表
    user_answer_list:list[dict[str, any]]

    # 控制出题节奏
    # 当前已经答题数量
    current:int     # 当前

    # 评价结果节点
    # 评价结果
    evaluation:str

    # 考试状态
    exam_step:str

    # 当前题目编号
    question_id:int

    # 是否继续出题
    continue_question:bool

    # 判断是否为新一轮
    is_new_round:bool

