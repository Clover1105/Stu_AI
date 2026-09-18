from app.ai.agent.multi_agent.state.exam_state import ExamState
from app.ai.tool.mysql_tool import mysql_tool
import ast
from langchain_core.messages import AIMessage

"""
出题节点，随机抽取一道未出过的题目
"""

def question_node(state:ExamState):
    print("\n【测试】这里是 -- question_node.py")
    # 课程名称
    course = state['course']
    # 题目数量
    num = state['total']
    # 查询题目列表
    question_list = state.get('questions',[])
    # 获取当前题目号
    current = state.get("current", 0) + 1
    # 判断题目列表是否有数据
    if len(question_list)>0:
        print("【测试】开始判断题目列表 -- 重组问题id")
        rs = ",".join([str(i["id"]) for i in question_list])
        print("【测试】开始判断题目列表 -- sql语句1")
        sql = f"select * from question_bank where question_subject='{course}' and question_id not in ({rs})  ORDER BY RAND() desc LIMIT 1"
    else:
        print("【测试】开始判断题目列表 -- sql语句2")
        sql = f"select * from question_bank where question_subject='{course}' ORDER BY RAND() desc LIMIT 1"
    # 调用MySQL工具
    rs = mysql_tool.invoke({"sql":sql})
    print(f"【测试】数据库查询结果：{rs}")
    print(f"【测试】数据库查询结果的类型：{type(rs)}")
    data = rs[0]
    # 添加到题库列表
    question_list.append({
        "id": data["question_id"],
        "question": data["question_title"],
        "answer": data["answer"]
    })
    # ai回复消息
    ai_msg = f"\n第{current}题：{data["question_title"]}\n"
    return {
        "messages": [AIMessage(content=ai_msg)],
        "questions": question_list,
        "current": current,
        "exam_step": "question",
        "question_id": data["question_id"],
        "total": num,
    }

if __name__ =="__main__":
    data =[
        {"id": 1, "question": "sdfsdfs"},
        {"id": 2, "question": "sdfsdfs"},
        {"id": 3, "question": "sdfsdfs"},
    ]
    rs =",".join([str(i["id"]) for i in data])
    print(rs)
