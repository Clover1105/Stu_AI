"""
lambda匿名函数
    - 单表达式函数
    - 语法：lambda 参数: 返回值
    - 适合简单的一次性使用场景
"""
# 1.基本lambda函数
# 普通函数
def square(x):
    return x ** 2
# lambda版本
square_lambda = lambda x: x ** 2
print(f"普通函数：{square(5)}")
print(f"lambda函数：{square_lambda(5)}")


# 2.多个参数的lambda
add = lambda a, b: a + b
multiply = lambda x, y, z: x * y * z
print(f"加法：{add(10, 20)}")
print(f"乘法：{multiply(2, 3, 4)}")


# 3.lambda作为参数使用
numbers = [1, 2, 3, 4, 5]
# 使用lambda作为排序key
sorted_desc = sorted(numbers, key=lambda x: -x)
print(f"降序排序：{sorted_desc}")
# 使用map和lambda
squared = list(map(lambda x: x ** 2, numbers))
print(f"平方：{squared}")
# 使用filter和lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数：{evens}")


# 4.条件lambda
max_func = lambda a, b: a if a > b else b
print(f"较大值：{max_func(10, 20)}")