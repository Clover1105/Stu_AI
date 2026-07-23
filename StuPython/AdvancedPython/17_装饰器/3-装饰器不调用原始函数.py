"""
- 装饰器内部的闭包函数可以不调用原始函数
- 此时原始函数的代码不会执行
- 可以用来替换或屏蔽原始函数的功能
"""

# 装饰器不调用原始函数
def tool(cb):
    def f():
        print("tool公共功能")
        # cb()  # 注释掉，不调用原始函数
    return f
@tool
def fn():
    print("fn函数的功能")    # 此行代码不会执行
fn()  # 只输出 "tool公共功能"


# 条件性调用原始函数
def conditional_decorator(condition):
    def decorator(func):
        def wrapper():
            if condition:
                print("条件满足，执行原始函数")
                func()
            else:
                print("条件不满足，跳过原始函数")
        return wrapper
    return decorator
@conditional_decorator(True)
def say_yes():
    print("执行了原始函数")
@conditional_decorator(False)
def say_no():
    print("不会执行")

say_yes()
say_no()