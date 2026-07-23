"""
- 带参数的类装饰器：@Tool(10)
- 先 Tool(10) 创建实例，调用 __init__
- 再 @实例，调用实例的 __call__ 方法接收原始函数
- 通常 __call__ 返回一个闭包函数
"""


# 基本带参数类装饰器
class Tool:
    def __init__(self, n):
        print(f"__init__接收参数：{n}")
        self.n = n
    def __call__(self, cb):
        print("__call__接收原始函数")
        def f():
            print(f"装饰器参数是：{self.n}")
            print("调用被装饰的函数时，其实是调用我")
            cb()
        return f
@Tool(10)  # 先 Tool(10) 创建实例，再 @实例
def fn():
    print("fn函数的功能")
fn()


# 带参数的权限验证装饰器
class Permission:
    def __init__(self, required_level):
        self.required_level = required_level
    def __call__(self, func):
        def wrapper(user):
            if user.get("level", 0) >= self.required_level:
                return func(user)
            else:
                print(f"权限不足！需要等级{self.required_level}，当前等级{user.get('level', 0)}")
        return wrapper
@Permission(3)
def admin_action(user):
    print(f"管理员{user['name']}执行了操作")
user1 = {"name": "张三", "level": 5}
user2 = {"name": "李四", "level": 1}
admin_action(user1)
admin_action(user2)