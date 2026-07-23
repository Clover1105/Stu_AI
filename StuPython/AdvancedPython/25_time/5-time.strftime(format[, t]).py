"""
- 将struct_time格式化为指定格式的字符串
- 不传t参数则使用当前本地时间
- 格式符号：%Y年、%m月、%d日、%H时、%M分、%S秒
"""
import time

# 格式化当前时间（年-月-日 时:分:秒）
time1 = time.strftime('%Y-%m-%d %H:%M:%S')
print(f"标准格式：{time1}")

# 自定义格式
time2 = time.strftime("%Y年%m月%d日 %H时%M分%S秒")
print(f"中文格式：{time2}")

# 紧凑格式
time3 = time.strftime("%Y%m%d_%H%M%S")
print(f"紧凑格式：{time3}")

# 使用指定时间戳格式化
timestamp = time.time()
custom = time.strftime("%Y/%m/%d", time.localtime(timestamp))
print(f"日期格式：{custom}")