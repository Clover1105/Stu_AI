# 5.f-string：格式化字符串
"""
语法：f"文本{变量}"
可以设置小数位数：{变量:.nf}
可以在{}中写表达式
"""
import math
name = "pen"
danPrice = 13
sum_num = 5
print(f"{name}的价格是{danPrice:.2f}元，一共买了{sum_num}个")
pi = math.pi
print(f"圆周率保留两位小数是{pi:.2f}")
print(f"圆周率保留五位小数是{pi:.5f}")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")