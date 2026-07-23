"""
推导式中的复杂条件
    - 多个if条件
    - if-else嵌套
    - 逻辑运算符组合
"""
# 1.多个if条件（同时满足）
numbers = list(range(1, 31))
# 找出既能被3整除又能被5整除的数
result = [x for x in numbers if x % 3 == 0 if x % 5 == 0]
print(f"既能被3又能被5整除的数：{result}")


# 2.使用and/or组合条件
# 找出10-30之间，是偶数或是3的倍数的数
nums = range(10, 31)
filtered = [x for x in nums if x % 2 == 0 or x % 3 == 0]
print(f"10-30中偶数或3的倍数：{filtered[:10]}...")  # 只显示前10个


# 3.复杂if-else嵌套
scores = [85, 45, 92, 58, 73, 39, 88]
grades = [
    "A" if s >= 90 else
    "B" if s >= 80 else
    "C" if s >= 70 else
    "D" if s >= 60 else
    "F"
    for s in scores
]
# grades = []
# for s in scores:
#     if s >= 90:
#         grades.append("A")
#     elif s >= 80:
#         grades.append("B")
#     elif s >= 70:
#         grades.append("C")
#     elif s >= 60:
#         grades.append("D")
#     else:
#         grades.append("F")
print(f"成绩：{scores}")
print(f"等级：{grades}")


# 4.根据多个条件转换数据
data = [5, -3, 0, 8, -2, 0, 4]
transformed = [
    "正数" if x > 0 else
    "负数" if x < 0 else
    "零"
    for x in data
]
# transformed = []
# for x in data:
#     if x > 0:
#         transformed.append("正数")
#     elif x < 0:
#         transformed.append("负数")
#     else:
#         transformed.append("零")
print(f"原数据：{data}")
print(f"分类：{transformed}")