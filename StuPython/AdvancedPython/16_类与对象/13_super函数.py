"""
super函数基础
    - super是一个全局函数，调用时传入两个参数：类名和对象
    - 返回值是该对象，但访问属性或方法时找的是父类中的
    - 在类的代码中使用super()可省略参数，默认为当前类和self
"""

# 基本super用法
class A:
    x = 10
class B(A):
    x = 20
b1 = B()
print(f"b1.x = {b1.x}")  # 20
print(f"super(B, b1).x = {super(B, b1).x}")  # 10


# super调用父类方法
class A:
    x = 10
    def fn(self):
        print(f"第一个人写了一个工具，写了很多有用的代码，x={self.x}")
class B(A):
    y = 20
    def fn(self):
        super(B, self).fn()  # 方法一：调用父类方法
        # A.fn(self)         # 方法二：直接通过类名调用
        print(f"第二个人写了一个工具，写了很多有用的代码，y={self.y}")
b1 = B()
b1.fn()


"""
super调用父类构造函数
    - 子类可以通过super()调用父类的__init__方法
    - 确保父类的初始化代码得到执行
    - 可以传递参数给父类构造函数
"""

# 不使用super导致子类缺少属性
class A:
    def __init__(self):
        print("A--init")
        self.x = 10
class B(A):
    def __init__(self, x, y):
        print("B--init")
        self.y = y
b1 = B(100, 200)
# print(b1.x)  # 报错：b1没有x属性
print(f"b1.y = {b1.y}")


# 使用super调用父类构造函数
class A:
    x = 40
    def __init__(self):
        print("A--init")
        self.x = 10
class B(A):
    def __init__(self, x, y):
        print("B--init")
        super(B, self).__init__()  # 调用父类构造函数
        self.y = y
b1 = B(100, 200)
print(f"b1.x = {b1.x}")  # 10
print(f"b1.y = {b1.y}")


# 向父类传递参数
class A:
    x = 40
    def __init__(self, x):
        print("A--init")
        self.x = x
class B(A):
    def __init__(self, x, y):
        print("B--init")
        super(B, self).__init__(x)  # 传递参数给父类
        self.y = y
b1 = B(100, 200)
print(f"b1.x = {b1.x}")  # 100
print(f"b1.y = {b1.y}")


