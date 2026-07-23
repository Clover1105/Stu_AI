"""
- 一个.py文件就是一个模块
- 模块中可以定义变量、函数、类
"""

# 题目：创建并使用自定义模块

# 创建 mymath.py 文件

# 导入并使用
import mymath

print(f"pi：{mymath.pi}")
print(f"加法：{mymath.add(10, 20)}")

calc = mymath.Calculator()
print(f"乘法：{calc.multiply(5, 6)}")