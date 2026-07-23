import math
# 三角函数
jiaoDu = 30
huDu = math.radians(jiaoDu)  # 角度转弧度
print(f"角度 {jiaoDu}° 的三角函数：")
print(f"sin : {math.sin(huDu)}")    # 弧度的正弦
print(f"cos : {math.cos(huDu)}")    # 弧度的余弦
print(f"tan : {math.tan(huDu)}")    # 弧度的正切
# 反三角函数
val = 0.5
print(f"math.asin({val}) = {math.asin(val)} 弧度")    # 反正弦弧度值
print(f"math.acos({val}) = {math.acos(val)} 弧度")    # 反余弦弧度值
print(f"math.atan({val}) = {math.atan(val)} 弧度")    # 反正切弧度值
print(f"math.atan2(3, 2) = {math.atan2(3, 2)} 弧度")  # 给定的x及y坐标值的反正切值
print(f"math.degrees(math.asin({val})) = {math.degrees(math.asin(val))}°")  # 将弧度转换为角度
# 弧度角度互转
print(f"math.radians(180) = {math.radians(180)}")   # 将角度转换为弧度
print(f"math.degrees(math.pi) = {math.degrees(math.pi)}")   # 将弧度转换为角度