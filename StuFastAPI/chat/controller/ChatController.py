import json

from fastapi import APIRouter

from chat.service import ChatService

# 导入流式输出模块
from starlette.responses import StreamingResponse

from chat.entity.ConversationResultEntity import ConversationResultEntity


# 创建子路由对象
chat_router = APIRouter()

# 创建聊天接口
@chat_router.get(
    path="/chat",
    summary="聊天",
    description="""
        聊天
        访问路径：http://localhost:8000/chat/chat
        请求参数：
            question：用户问题
        返回值：
            流式输出：sse
    """
)
def chat(question: str, historyId: int):
    # 流式输出处理
    def generator():
        for item in ChatService.chat(question,historyId):
            # print(item.content)
            yield f"data:{json.dumps({'content':item},ensure_ascii=False)}\n\n"
        yield f"data:{json.dumps({'content':'end_end'})}\n\n"
    return StreamingResponse(
        content=generator(),
        media_type="text/event-stream"
    )

# 创建接口，接收要保存的对话
@chat_router.post(
    path="/saveConversationResult",
    summary="保存对话结果",
    description="""
        保存对话结果
        访问路径：http://localhost:8000/chat/saveConversationResult
    """
)
def save_conversation_result(conversationResultEntity: ConversationResultEntity):
    return ChatService.save_conversation_result(conversationResultEntity)

if __name__ == "__main__":
    print(chat("你好",1))