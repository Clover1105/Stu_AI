"""
返回值return基础
    - return结束函数并返回值
    - 没有return时返回None
    - return后面的代码不会执行
"""
# 1.函数返回计算结果
def add(a, b):
    """返回两个数的和"""
    result = a + b
    return result
sum1 = add(10, 20)
sum2 = add(5, 7)
print(f"10+20={sum1}")
print(f"5+7={sum2}")

# 2.没有return的函数返回None
def say_hello(name):
    print(f"你好，{name}")
result = say_hello("张三")
print(f"返回值：{result}")  # None

# 3.return提前结束函数
def check_age(age):
    if age < 0:
        return "年龄无效"  # 提前返回
    if age < 18:
        return "未成年"
    return "成年"
print(check_age(-5))
print(check_age(15))
print(check_age(20))



"""
返回多个值
    - 返回多个值实际是返回元组
    - 可以用多个变量接收
"""
# 1.返回多个计算结果
def calculate(a, b):
    """返回和、差、积、商"""
    sum_result = a + b
    diff = a - b
    product = a * b
    quotient = a / b
    return sum_result, diff, product, quotient
# 用一个变量接收（得到元组）
result = calculate(10, 5)
print(f"一个变量接收：{result}")
print(f"类型：{type(result)}")
# 用多个变量接收
s, d, p, q = calculate(10, 5)
print(f"和={s}, 差={d}, 积={p}, 商={q}")

# 2.返回圆的相关计算
import math
def circle_calc(radius):
    """返回圆的周长和面积"""
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return circumference, area
c, a = circle_calc(5)
print(f"半径5的圆：周长={c:.2f}, 面积={a:.2f}")

# 3.使用_忽略不需要的返回值
def get_user():
    return "张三", 18, "北京", "工程师"
name, age, _, job = get_user()  # 忽略城市
print(f"{name}，{age}岁，{job}")