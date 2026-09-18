from fastapi import APIRouter,Request
from fastapi.responses import StreamingResponse
from app.ai.agent.vosk_agent import VoskAgent
import json
from fastapi import WebSocket

chat_router = APIRouter()

# 创建语音实例
vosk_agent = VoskAgent.get_vosk()

# 聊天接口
@chat_router.get("/chat")
async def chat(request:Request,question:str,user_id:str):
    print('\n【测试】这里是 -- chat_router.py')
    print(f"【测试】用户问题：{question}，用户ID：{user_id}")

    exam_agent = request.app.state.exam_agent
    print(f"【测试】考试智能体：{exam_agent}")

    # 定义一个异步迭代器
    async def generate(question, user_id, session_id):
        try:
            async for x in exam_agent.chat(question,user_id,"001"):
                # False 流式未结果
                data = {"data": x, "done": False}
                yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
            # 流式结束
            data = {"data": "", "done": True}
            yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"
        except Exception as e:
            print(f"【测试】Agent 内部报错了：{e}")
            # 流式结束
            data = {"data": "流式异常", "done": True}
            yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"

    # 返回结果是json，默认是ajax
    return StreamingResponse(
        generate(question,user_id,"001"),
        media_type="text/event-stream"
    )


# 语音输入接口
@chat_router.websocket("/vosk")
async def vosk(ws: WebSocket):
    # 当前方法没有返回值
    try:
        # 第一次握手，创建链接
        await ws.accept()
        print("【测试】第一次握手，创建链接")
        # 开启语音
        await vosk_agent.speak(ws)
        while True:
            # 接收客户端发送给的数据
            await ws.receive_text()
    except Exception as e:
        print(f"【测试】异常：{e}")