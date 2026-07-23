"""
- 同步：代码按顺序执行，前一个任务完成才能执行下一个（会阻塞）
- 异步：任务可以交替执行，等待时可以去干别的事（不阻塞）
- async def：定义异步函数，返回协程对象而非直接执行
- await：等待异步任务完成，只能在异步函数中使用

注意事项：
- 异步函数直接调用返回协程对象，不会真正执行
- 协程对象需要通过 await 或 asyncio.run() 来执行
"""
import asyncio
import time

# 同步代码示例（阻塞）
def sync_task():
    print("开始同步任务...")
    for i in range(3):
        time.sleep(1)  # 模拟耗时操作，会阻塞
        print(f"  同步任务: 第{i+1}秒")
    print("同步任务完成")
    return i
# 同步执行：必须等同步任务完才能继续
result = sync_task()
print(f"同步任务结果: {result}")
print("后面的代码必须等待...\n")




# 异步函数基础
async def async_task():
    print("开始异步任务...")
    for i in range(3):
        time.sleep(1)  # 注意：time.sleep 不是异步的，这里仅作演示
        print(f"  异步任务: 第{i+1}秒")
    print("异步任务完成")
    return i
# 直接调用异步函数：返回协程对象，不会执行函数体
coroutine_obj = async_task()
print(f"直接调用异步函数返回: {coroutine_obj}")
print(f"类型: {type(coroutine_obj)}")
print("注意：协程对象不会自动执行，需要 await 或 asyncio.run()\n")




# 通过 asyncio.run() 执行异步函数
async def simple_async():
    print("异步函数执行中...")
    await asyncio.sleep(1)  # 异步版本的 sleep，不阻塞事件循环
    print("异步函数执行完毕")
    return "完成"
# asyncio.run() 会创建事件循环并执行协程
result = asyncio.run(simple_async())
print(f"执行结果: {result}")