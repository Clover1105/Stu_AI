from pydantic import BaseModel,Field
# 定义工具参数校验类
class EmailParams(BaseModel):
    # 收件人
    to:str = Field(...,description="收件人邮箱")
    # 邮件主题
    subject:str = Field(...,description="邮件主题")
    # 邮件内容
    content:str = Field(...,description="邮件内容")