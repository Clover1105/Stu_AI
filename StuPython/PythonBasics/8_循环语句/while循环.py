"""
while循环
    - 当条件为True时重复执行代码块
    - 需要手动改变条件避免死循环
    - 适用于不确定循环次数的场景
"""
# 计算存款年数
money = 1000
target = 2000  # target: 目标金额
year = 0
while money < target:
    money *= 1.05  # 每年增长5%
    year += 1
print(f"\n需要{year}年才能从1000增长到{target:.0f}")