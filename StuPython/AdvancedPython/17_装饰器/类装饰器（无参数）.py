"""
- 类也可以作为装饰器使用
- @Tool 等价于 fn = Tool(fn)
- 类装饰器通过 __init__ 接收原始函数
- 通过 __call__ 实现调用时的功能
"""


# 基本类装饰器
class Tool:
    def __init__(self, n):
        print(f"__init__接收参数：{n}")
        self.n = n  # 保存原始函数
    def __call__(self):
        print("调用被装饰的函数时，其实是调用__call__方法")
        self.n()  # 调用原始函数
@Tool  # fn = Tool(fn)
def fn():
    print("fn函数的功能")
print("装饰完成")
fn()  # 对象被当作函数调用，触发__call__


# 统计调用次数的类装饰器
class CallCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"第{self.count}次调用 {self.func.__name__}")
        return self.func(*args, **kwargs)
@CallCounter
def greet(name):
    print(f"Hello, {name}!")
greet("张三")
greet("李四")
greet("王五")


# 缓存结果的类装饰器
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, n):
        if n in self.cache:
            print(f"从缓存获取 {n} 的结果")
            return self.cache[n]
        result = self.func(n)
        self.cache[n] = result
        print(f"计算并缓存 {n} 的结果")
        return result
@Cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(5))
print(fibonacci(5))  # 第二次从缓存获取