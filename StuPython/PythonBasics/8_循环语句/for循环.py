"""
for循环
    - 用于遍历可迭代对象（列表、字符串、元组等）
    - 语法：for 变量 in 可迭代对象:
    - 每次循环将元素赋值给变量
"""
# 遍历列表元素
numbers = [11, 22, 33, 44, 55]
print("\n列表中的偶数：")
for num in numbers:  # 遍历列表元素num = 11,num = 22,num = 33...
    if num % 2 == 0:
        print(f"{num}是偶数")
# 遍历字符串
word = "Python"
print(f"\n遍历字符串'{word}'：")
for c in word:
    print(f"字符：{c}")

"""
嵌套for循环
    - 循环内部再写循环
    - 外层循环执行一次，内层循环执行完整一轮
"""
# 打印乘法表
print("\n九九乘法表：")
for i in range(1, 10):  # 外层循环控制行数
    for j in range(1, i + 1):  # 内层循环控制列数
        print(f"{j}×{i}={i * j}", end="\t")
    print()  # 换行
# 遍历嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\n遍历二维列表：")
for row in matrix:  # 遍历[1, 2, 3] --> [4, 5, 6] --> [7, 8, 9]
    for col in row:  # 遍历1 --> 2 --> 3
        print(col, end=" ")
    print()  # 换行

"""
for-else语句
    - for循环正常执行完毕后执行else块
    - 如果循环被break打断，则不执行else
"""
# 判断是否所有数都大于0
nums = [5, 8, -2, 10, 3]
print("\n检查是否所有数都大于0：")
for n in nums:  # 遍历nums列表中的所有元素
    if n <= 0:  # 判断当前元素是否小于等于0
        print(f"发现非正数：{n}")  # 小于等于0执行
        break  # 有一个非正数就停止循环
else:  # 循环 正常执行 完毕后执行else块
    print("所有数都大于0")