from pydantic import BaseModel,Field

# 创建实体类
class ConversationResultEntity(BaseModel):
    question: str = Field(..., description="用户问题")
    username: str = Field(..., description="用户名")
    parentId: int = Field(..., description="对话历史记录ID")
    answer: str = Field(..., description="答案")