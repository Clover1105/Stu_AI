"""
方式1：直接调用 → 返回协程对象（不执行）
方式2：await 调用 → 等待执行完成，只能在异步函数中使用
方式3：asyncio.run() → 创建事件循环并执行协程（入口函数用）
事件循环：管理和调度异步任务的机制

注意事项：
asyncio.run() 是程序的入口，一个程序通常只调用一次
异步函数中不要使用 time.sleep()，要用 await asyncio.sleep()
await 会挂起当前函数，让事件循环执行其他任务
"""

import asyncio
import time

# 三种调用方式对比
async def demo_task(name, seconds):
    """模拟异步任务"""
    print(f"任务 {name}: 开始执行，需要{seconds}秒")
    await asyncio.sleep(seconds)  # 异步等待，不阻塞
    print(f"任务 {name}: 执行完成")
    return f"{name}的结果"


# 方式1：直接调用（不执行）
print("方式1：直接调用")
coroutine = demo_task("A", 1)
print(f"返回类型: {type(coroutine)}，值: {coroutine}")
print("函数体没有执行！需要 await 或 run() 才能执行\n")

# 方式2：在异步函数中使用 await
print("方式2：await 调用")
async def use_await():
    result = await demo_task("B", 1)
    print(f"await 获取的结果: {result}")
    return result

# 注意：上面的 use_await 只是定义，需要执行才能看到效果
# 实际执行放在后面

# 方式3：asyncio.run() 调用
print("方式3：asyncio.run() 调用")
# result = asyncio.run(demo_task("C", 1))  # 不会打印，因为上面有未完成的循环
# print(f"run() 获取的结果: {result}")

print("\n" + "=" * 50 + "\n")




# 正确使用 await 和 run
async def business_logic():
    """业务逻辑：使用 await 调用异步函数"""
    print("业务逻辑开始...")
    # 使用 await 等待异步任务完成
    result1 = await demo_task("任务1", 2)
    print(f"得到结果1: {result1}")
    result2 = await demo_task("任务2", 1)
    print(f"得到结果2: {result2}")
    print("业务逻辑结束")
    return "全部完成"
# 程序入口：使用 asyncio.run() 启动
print("程序入口：asyncio.run(business_logic())")
print("注意：asyncio.run() 只能调用一次，作为整个程序的入口\n")
# asyncio.run(business_logic())  # 取消注释即可运行




# 正确的异步 sleep（不要用time.sleep）
print("\n=== 异步 vs 同步 sleep 的区别 ===")
async def async_sleep_demo():
    """使用 await asyncio.sleep() - 正确"""
    print("正确做法：await asyncio.sleep()")
    start = time.time()
    await asyncio.sleep(1)  # 让出控制权，其他任务可以运行
    print(f"  耗时: {time.time() - start:.2f}秒")
async def wrong_sleep_demo():
    """使用 time.sleep() - 错误，会阻塞整个事件循环"""
    print("错误做法：time.sleep()")
    start = time.time()
    time.sleep(1)  # 会阻塞事件循环，其他异步任务无法运行
    print(f"  耗时: {time.time() - start:.2f}秒")
    print("  注意：time.sleep() 会阻塞整个事件循环！")
# 演示多个异步任务并发
async def show_concurrency():
    """展示多个异步任务交替执行"""
    print("\n多个异步任务并发执行：")
    # 创建多个任务
    task1 = asyncio.create_task(demo_task("并发1", 2))
    task2 = asyncio.create_task(demo_task("并发2", 1))
    task3 = asyncio.create_task(demo_task("并发3", 3))
    # 等待所有任务完成
    results = await asyncio.gather(task1, task2, task3)
    print(f"所有任务结果: {results}")
# 最终程序入口（取消注释即可运行）
# async def main():
#     await business_logic()
#     await async_sleep_demo()
#     await show_concurrency()
#
# asyncio.run(main())