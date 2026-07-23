"""
- tm_year：年
- tm_mon：月(1-12)
- tm_mday：日(1-31)
- tm_hour：时(0-23)
- tm_min：分(0-59)
- tm_sec：秒(0-61)
- tm_wday：星期(0-6，0是周一)
- tm_yday：一年中的第几天(1-366)
"""
import time

t = time.localtime()

print(f"年：{t.tm_year}")
print(f"月：{t.tm_mon}")
print(f"日：{t.tm_mday}")
print(f"时：{t.tm_hour}")
print(f"分：{t.tm_min}")
print(f"秒：{t.tm_sec}")
print(f"星期(0周一)：{t.tm_wday}")
print(f"一年中的第几天：{t.tm_yday}")
print(f"是否夏令时：{t.tm_isdst}")

# 综合输出
print(f"\n今天是{t.tm_year}年{t.tm_mon}月{t.tm_mday}日，是今年的第{t.tm_yday}天")