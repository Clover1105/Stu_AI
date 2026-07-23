"""
- 一个函数可以被多个装饰器装饰
- 装饰阶段：从下往上执行（离函数近的先执行）
- 调用阶段：从上往下执行（离函数远的先执行）
- 最终函数指向最外层装饰器返回的函数
"""

# 两个装饰器链
def print_logs(cb):
    print("print_logs装饰器执行")
    def f():
        print("日志：调用了装饰器所装饰的函数")
        cb()
    return f
def net_tool(cb):
    print("net_tool装饰器执行")
    def f():
        print("联网的代码")
        cb()
    return f
@print_logs  # 外层装饰器（离函数远）
@net_tool    # 内层装饰器（离函数近）
def fn():
    print("fn函数的功能")
print("=== 装饰完成，开始调用 ===")
fn()
# 输出顺序：
# 日志：调用了装饰器所装饰的函数
# 联网的代码
# fn函数的功能


# 三个装饰器链
def decorator_a(func):
    print("A装饰器")
    def wrapper():
        print("A开始")
        func()
        print("A结束")
    return wrapper
def decorator_b(func):
    print("B装饰器")
    def wrapper():
        print("B开始")
        func()
        print("B结束")
    return wrapper
def decorator_c(func):
    print("C装饰器")
    def wrapper():
        print("C开始")
        func()
        print("C结束")
    return wrapper
@decorator_a
@decorator_b
@decorator_c
def original():
    print("原始函数")
print("\n=== 调用函数 ===")
original()
# 输出顺序：
# C装饰器
# B装饰器
# A装饰器
#
# === 调用函数 ===
# A开始
# B开始
# C开始
# 原始函数
# C结束
# B结束
# A结束


# 计时和日志装饰器链
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[计时] {func.__name__} 耗时 {end-start:.4f}秒")
        return result
    return wrapper
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[日志] 调用 {func.__name__}，参数: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
@timer
@logger
def calculate(x, y):
    time.sleep(0.5)
    return x * y
print(calculate(10, 20))