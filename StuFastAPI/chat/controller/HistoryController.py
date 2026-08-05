from fastapi import APIRouter

from chat.service import HistoryService

# 创建子路由对象
history_router = APIRouter()

@history_router.get(
    path="/queryHistoryMenu",
    summary="查询历史记录菜单栏",

)
def query_history_menu(username: str):
    return HistoryService.query_history_menu(username)

@history_router.get(
    path="/conversationLog",
    summary="查询某条历史记录详情",
)
def conversation_log(historyId: int):
    return HistoryService.conversation_log(historyId)
