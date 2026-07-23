"""
- 将时间戳转换为易读的本地时间格式
- 格式：星期 月 日 时:分:秒 年
- 不传参数则使用当前时间戳
"""
import time

# 获取当前时间的ctime格式
current = time.ctime()
print(f"当前时间：{current}")

# 使用特定时间戳转换
timestamp = 1776952517
specific = time.ctime(timestamp)
print(f"时间戳{timestamp}对应时间：{specific}")
print(f"类型：{type(specific)}")