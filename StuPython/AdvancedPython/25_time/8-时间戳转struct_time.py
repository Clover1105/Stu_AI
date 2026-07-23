import time

# 使用当前时间戳
current = time.time()
local = time.localtime(current)
print(f"当前时间戳：{current}")
print(f"转换后：{local}")
print(f"日期：{local.tm_year}-{local.tm_mon}-{local.tm_mday}")

# 使用特定时间戳
timestamp = 1776952517
specific = time.localtime(timestamp)
print(f"\n时间戳{timestamp}转换：")
print(f"{specific.tm_year}年{specific.tm_mon}月{specific.tm_mday}日 {specific.tm_hour}:{specific.tm_min}:{specific.tm_sec}")
