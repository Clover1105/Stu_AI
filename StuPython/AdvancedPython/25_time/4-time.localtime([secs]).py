"""
- 将时间戳转换为本地时区的struct_time元组
- 不传参数则使用当前时间戳
- struct_time包含年、月、日、时、分、秒等信息
"""

import time

# 获取当前时间的struct_time元组
local_time = time.localtime()
print("当前时间struct_time：")
print(local_time)

# 使用特定时间戳转换
timestamp = time.time()
converted = time.localtime(timestamp)
print(f"\n时间戳{timestamp}转struct_time：")
print(converted)