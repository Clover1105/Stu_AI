"""
生成器完整流程演示
    - 综合演示生成器的创建、取值、耗尽全过程
    - 理解生成器的执行顺序
    - 掌握生成器的使用场景
"""
# 完整演示生成器生命周期
def demo_generator():
    print("【1】生成器函数开始执行")
    yield "第一个值"
    print("【2】第一次yield后继续")
    yield "第二个值"
    print("【3】第二次yield后继续")
    yield "第三个值"
    print("【4】生成器函数执行完毕")

print("=== 创建生成器 ===")
gen = demo_generator()
print("生成器已创建，函数体未执行")

print("\n=== 开始获取值 ===")
print(f"获取到：{next(gen)}")
print(f"获取到：{next(gen)}")
print(f"获取到：{next(gen)}")

print("\n=== 尝试继续获取 ===")
try:
    next(gen)
except StopIteration:
    print("生成器已耗尽")

# for循环自动管理生成器
print("\n=== 使用for循环遍历生成器 ===")
def simple_gen():
    print("生成器启动")
    for i in range(3):
        print(f"准备生成{i}")
        yield i
    print("生成器结束")

for value in simple_gen():
    print(f"得到：{value}")

print("\n循环自动处理了StopIteration异常")