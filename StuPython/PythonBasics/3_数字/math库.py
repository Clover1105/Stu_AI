# math库：import math
import math
# 绝对值
print(f"abs(-25) = {abs(-25)}")
print(f"fabs(-25) = {math.fabs(-25)}")  # 以浮点数形式返回数字的绝对值
# 上取整 / 下取整
print(f"math.ceil(3.14) = {math.ceil(3.14)}")   # 向上取整
print(f"math.floor(3.99) = {math.floor(3.99)}") # 向下取整
# 四舍五入（四舍六入 5看齐 奇进偶不进）
print(f"round(3.5) = {round(3.5)}")   # 奇进偶不进
print(f"round(4.5) = {round(4.5)}")
print(f"round(3.55, 1) = {round(3.55, 1)}")
# 最大值 / 最小值
print(f"max(10, 55, 3, 88, 20) = {max(10, 55, 3, 88, 20)}")
print(f"min(10, 55, 3, 88, 20) = {min(10, 55, 3, 88, 20)}")
# 幂运算与平方根
print(f"math.pow(5, 3) = {math.pow(5, 3)}")  # 5的3次方
print(f"math.sqrt(64) = {math.sqrt(64)}")   # 平方根
# 对数运算
print(f"math.log(100, 10) = {math.log(100, 10)}")  # 以10为底
print(f"math.log(100) = {math.log(100)}")          # 自然对数
print(f"math.log10(1000) = {math.log10(1000)}")
# 数学常数
print(f"math.pi = {math.pi}")   # 圆周率
print(f"math.e = {math.e}")
# 拆分整数和小数部分
fenShu, zhenShu = math.modf(3.14159)
print(f"math.modf(3.14159) = 整数部分: {zhenShu}, 小数部分: {fenShu}")