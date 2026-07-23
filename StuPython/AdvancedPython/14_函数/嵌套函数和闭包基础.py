"""
嵌套函数和闭包基础
    - 函数内部定义函数
    - 内部函数可以访问外部函数的变量
    - 闭包：返回内部函数，保留外部变量的状态
"""
# 1.简单的嵌套函数
def outer_function():
    print("这是外部函数")
    def inner_function():
        print("这是内部函数")
    inner_function()  # 在外部函数内调用
outer_function()
# inner_function()  # 错误：外部无法调用内部函数


# 2.闭包 - 返回内部函数
def make_greeting(greeting):
    """创建一个问候函数"""
    def greet(name):
        print(f"{greeting}，{name}！")
    return greet
say_hello = make_greeting("你好")
say_hi = make_greeting("嗨")
say_hello("张三")
say_hi("李四")
"""
全局[
make_greeting ==> {}
say_hello ==> make_greeting("你好") ==> [greeting="你好" 
                                        greet ==> {}
                                        return greet ==> say_hello=geet
                                        name="张三"   打印"你好，张三！"
                                        ]
say_hi ==> make_greeting("嗨") ==> [greeting="嗨" 
                                    greet ==> {}
                                    return greet ==> say_hi=geet
                                    name="李四"   打印"嗨，李四！"]
say_hello("张三") ==> geet("张三")
say_hi("李四") ==> geet("李四")
]
"""


# 3.闭包保留状态
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3
another_counter = counter()
print(another_counter())  # 1（独立的状态）