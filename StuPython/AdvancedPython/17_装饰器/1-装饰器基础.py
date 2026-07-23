"""
- 装饰器本质是闭包和回调函数的语法糖
- @装饰器名 是语法糖，等价于 函数 = 装饰器(函数)
- 装饰器会在函数定义时立即执行
"""

# 最简单的装饰器
def tool(cb):
    print("tool装饰器的功能,立即执行")
    def f():
        print("tool公共功能")
        cb()
    return f
@tool
def fn():
    print("fn函数的功能")
@tool
def fm():
    print("fm函数的功能")
fn()
fm()


# 理解装饰器的执行过程
def my_decorator(func):
    print("装饰器正在执行")
    def wrapper():
        print("装饰器添加的功能")
        func()
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
print("函数定义完成")
say_hello()