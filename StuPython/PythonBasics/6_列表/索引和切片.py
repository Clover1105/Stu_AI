"""
列表索引和切片
    - 正索引：0开始
    - 负索引：-1开始
    - 切片：[start:end:step]
    - 切片返回新列表，且可以越界
"""
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]
# 索引
# 每个元素有了两个索引（正数和负数），索引越界会报错
print(f"第一个元素：{fruits[0]}")
print(f"最后一个元素：{fruits[-1]}")
print(f"第三个元素：{fruits[2]}")
# 切片
print(f"[1:4]：{fruits[1:4]}")
print(f"[:3]：{fruits[:3]}")
print(f"[2:]：{fruits[2:]}")
print(f"[::2]：{fruits[::2]}")
print(f"[-4:4:1]：{fruits[-4:4:1]}") # 如果左和右符号不一样，先换算成一样的符号
print(f"[-4:4:-1]：{fruits[-4:4:-1]}")   # 空列表
# 总结：步长为正数就是从start开始往右取 步长为负数就是从start开始往左取
print(f"反转列表：{fruits[::-1]}")