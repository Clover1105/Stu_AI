# if条件语句
"""
if 表达式:
    条件为真时执行
    缩进逻辑运行代码
"""
price = 50
if price < 100: # 判断价格是否小于100
    print("价格很合适！") # 小于100执行
root = 123
if root:    # 判断root是否为空
    print(f"是管理员{root}")    # 不为空执行
s = 85
if s >= 90: # 判断分数是否大于等于90
    print("优秀") # 大于等于90执行
if s >= 80: # 判断分数是否大于等于80
    print("良好") # 大于等于80执行
if s >= 60: # 判断分数是否大于等于60
    print("及格") # 大于等于60执行

# if-else条件语句
"""
if-else条件语句
    二选一执行
    if条件True执行if块，否则执行else块
"""
# 奇偶数判断
num = 7
if num % 2 == 0:    # 判断num是否为偶数
    print(f"{num}是偶数")  # 为偶数执行
else:
    print(f"{num}是奇数")  # 为奇数执行
# 登录验证
password = "123456"
if password == "123456":    # 判断密码是否正确
    print("登录成功")   # 正确执行
else:
    print("密码错误")   # 错误执行

# if-elif-else条件语句
month = 7
if 3 <= month <= 5:         # 判断月份是否在3-5月之间
    print("春季")     # 在3-5月之间执行
elif 6 <= month <= 8:       # 判断月份是否在6-8月之间
    print("夏季")     # 在6-8月之间执行
elif 9 <= month <= 11:      # 判断月份是否在9-11月之间
    print("秋季")     # 在9-11月之间执行
elif month in [12, 1, 2]:   # 判断月份是否在12-2月之间
    print("冬季")     # 在12-2月之间执行
else:
    print("无效月份")   # 月份无效执行
