from typing_extensions import TypedDict, Annotated
from langchain.messages import AnyMessage
import operator

"""
邮件状态节点
"""
# 类的属性要求定义为字典类型
class EmailState(TypedDict):
    print("\n这里是email_state01.py")
    # 消息
    messages:Annotated[list[AnyMessage],operator.add]
    # 用户名
    name:str
    # 邮件
    email:str
    # 主题
    subject:str
    # 内容
    content:str
    # 结果回复，可选
    result:str