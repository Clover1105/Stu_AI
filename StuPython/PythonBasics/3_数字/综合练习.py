# 题目：计算一元二次方程 x² - 5x + 6 = 0 的根
a, b, c = 1, -5, 6  # 定义变量，方程系数
derTa = b**2 - 4*a*c    # 获取二次方程的判别式
print(f"解方程：{a}x² + {b}x + {c} = 0")
if derTa >= 0:  # 判断，判别式 >= 0才有根
    root1 = (-b + math.sqrt(derTa)) / (2*a) # 计算根1
    root2 = (-b - math.sqrt(derTa)) / (2*a) # 计算根2
    print(f"两个实数根：x1 = {root1}, x2 = {root2}")
else:   # 判别式 < 0 没有根
    print("方程无实数根")

# 题目：判断闰年
year = 2026 # 定义年份
"""
闰年判断规则：
    1.能被4整除，但不能被100整除
    2.能被400整除
"""
is_rn = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)  # 逻辑运算判断
print(f"\n{year}年是闰年吗？{is_rn}")