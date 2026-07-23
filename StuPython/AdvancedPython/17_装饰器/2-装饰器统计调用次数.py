"""
- 使用nonlocal在闭包中保存状态
- 每次调用被装饰函数时计数器加1
- 可以统计函数被调用的次数
"""

# 统计单个函数的调用次数
def print_log(cb):
    n = 0
    def f():
        nonlocal n
        n += 1
        print(f"日志：调用了{n}次装饰器所装饰的函数")
        cb()
    return f
@print_log
def fn():
    print("fn函数的功能")
@print_log
def fm():
    print("fm函数的功能")
fn()
fn()
fn()
fm()
fm()
fm()


# 带返回值的计数器
def counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"第{count}次调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
@counter
def add(a, b):
    return a + b
print(add(1, 2))
print(add(3, 4))
print(add(5, 6))