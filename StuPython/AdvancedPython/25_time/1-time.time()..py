"""
- 获取当前时间的时间戳
- 时间戳是从1970-01-01 08:00:00到现在的秒数
- 返回浮点数，精确到小数点后若干位
"""
import time

# 获取当前时间戳
timestamp = time.time()
print(f"当前时间戳：{timestamp}")
print(f"时间戳类型：{type(timestamp)}")