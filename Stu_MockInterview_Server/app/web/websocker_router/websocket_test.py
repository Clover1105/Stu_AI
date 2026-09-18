from fastapi import WebSocket

# 前后端先建立连接，连接建立好后才能通信
# WebSocket天生异步，方法是固定的

from fastapi import APIRouter

ws_router = APIRouter()

@ws_router.websocket("/ws")
async def test(ws: WebSocket):
    # 当前方法没有返回值
    try:
        # 第一次握手，创建链接
        await ws.accept()
        print("【测试】第一次握手，创建链接")
        while True:
            # 获取客户端发送的数据（客户 --》 服务）
            data = await ws.receive_text()
            print(f"【测试】客户端发送的数据：{data}")
            # 服务端发送的数据（服务 --》 客户）
            msg = "你好，我是服务端"
            print(f"【测试】服务端发送的数据：{msg}")
            # 发送数据给客户端
            await ws.send_text(msg)
    except Exception as e:
        print(f"【测试】异常：{e}")

