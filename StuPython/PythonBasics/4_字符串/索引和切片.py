# 6.字符串索引和切片
"""
正索引：从左到右 0开始
负索引：从右到左 -1开始
切片：[start:end:step]
"""
s = "hello world hello python"
print(f"第一个字符：{s[0]}")
print(f"最后一个字符：{s[-1]}")
print(f"第三个字符：{s[2]}")
print(f"[0:5]：{s[0:5]}")
print(f"[:5]：{s[:5]}")
print(f"[5:]：{s[5:]}")
print(f"[::2]：{s[::2]}")  # 步长为2
print(f"[::-1]：{s[::-1]}")  # 反转字符串