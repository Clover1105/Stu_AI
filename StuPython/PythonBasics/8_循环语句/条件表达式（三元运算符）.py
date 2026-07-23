"""
条件表达式（三元运算符）
    - 语法：值1 if 条件 else 值2
    - 条件为True返回值1，否则返回值2
    - 简洁的单行if-else
"""
# 基本用法
age = 20
status = "成年" if age >= 18 else "未成年"
print(f"年龄{age}：{status}")
# 取最大值
a, b = 15, 28
max_val = a if a > b else b
print(f"{a}和{b}中较大的是：{max_val}")
# 嵌套条件表达式
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(f"分数{score}：等级{grade}")
