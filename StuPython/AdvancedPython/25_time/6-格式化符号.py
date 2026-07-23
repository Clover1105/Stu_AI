"""
- %Y：四位年份
- %y：两位年份
- %m：月份(01-12)
- %d：日期(01-31)
- %H：24小时制(00-23)
- %I：12小时制(01-12)
- %M：分钟(00-59)
- %S：秒(00-59)
- %A：完整星期名称
- %a：简化星期名称
- %B：完整月份名称
- %b：简化月份名称
"""
import time

print("=== 时间格式化符号演示 ===\n")

# 基础日期时间
print(f"四位年份 %Y：{time.strftime('%Y')}")
print(f"两位年份 %y：{time.strftime('%y')}")
print(f"月份 %m：{time.strftime('%m')}")
print(f"日期 %d：{time.strftime('%d')}")
print(f"24小时制 %H：{time.strftime('%H')}")
print(f"12小时制 %I：{time.strftime('%I')}")
print(f"分钟 %M：{time.strftime('%M')}")
print(f"秒 %S：{time.strftime('%S')}")

# 文本格式
print(f"\n完整星期 %A：{time.strftime('%A')}")
print(f"简写星期 %a：{time.strftime('%a')}")
print(f"完整月份 %B：{time.strftime('%B')}")
print(f"简写月份 %b：{time.strftime('%b')}")

# 完整组合
print(f"\n完整格式 %c：{time.strftime('%c')}")
print(f"本地日期 %x：{time.strftime('%x')}")
print(f"本地时间 %X：{time.strftime('%X')}")