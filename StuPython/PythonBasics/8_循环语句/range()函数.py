"""
range()函数
    - 生成一个整数序列
    - range(stop)：0到stop-1
    - range(start, stop)：start到stop-1
    - range(start, stop, step)：指定步长
"""
# range基本用法
print("\nrange(5)：", end="")
for i in range(5):  # 0,1,2,3,4
    print(i, end=" ")
print("\nrange(2, 8)：", end="")
for i in range(2, 8):  # 2,3,4,5,6,7
    print(i, end=" ")
print("\nrange(1, 10, 2)：", end="")
for i in range(1, 10, 2):  # 1,3,5,7,9
    print(i, end=" ")
# 倒序输出
print("\n\n倒序输出：", end="")
for i in range(10, 0, -1):  # 10,9,8,7,6,5,4,3,2,1
    print(i, end=" ")
# 计算1到100的和
total = 0
for i in range(1, 101):  # 1,2,3,4,5,6,7,8,9,10...100
    total += i  # total = total + i
print(f"\n\n1到100的和：{total}")