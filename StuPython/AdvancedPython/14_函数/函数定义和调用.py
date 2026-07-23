"""
函数定义和调用
    - def关键字定义函数
    - 函数需要调用才会执行
    - 函数可以重复调用
"""
# 1.定义最简单的函数
def say_hello():
    """打印问候语"""
    print("Hello, Python!")
# 调用函数
say_hello()
say_hello()  # 可以多次调用


# 2.带计算功能的函数
def sum():
    """计算两个数的和"""
    a = 15
    b = 25
    result = a + b
    print(f"{a} + {b} = {result}")
sum()


# 3.函数不调用不执行
def not_called():
    print("这行代码不会执行，因为函数没有被调用")
# 注释掉下面的调用，上面的print不会执行
# not_called()
print("函数定义完成，但没有调用")