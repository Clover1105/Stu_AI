# 在 TestController 包下实现用户输入问题 --> LLM 针对于问题生成回复 --> 流式输出给客户端展示

# 引入子路由类
from fastapi import APIRouter
# 创建子路由对象
work_router = APIRouter()

# 引入 LLM 模型
from ai.LoadLLM import create_model
# 流式输出
from starlette.responses import StreamingResponse
# 引入json包，time包
import json, time

@work_router.get("/stream")
def stream(question: str):
    # 创建模型对象
    llm = create_model()
    # 接收用户输入的问题
    print(f"接收的问题：question={question}")
    # 角色
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}]
    # 创建生成器
    def generator():
        for chunk in llm.stream(messages):
            if chunk.content:
                yield f"data: {json.dumps({'content': chunk.content})}\n\n"
        yield f"data: {json.dumps({'content': 'end_end'})}\n\n"
    # 流式输出
    return StreamingResponse(

        content=generator(),
        media_type="text/event-stream",
    )