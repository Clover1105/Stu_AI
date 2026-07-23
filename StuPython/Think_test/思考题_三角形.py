# 思考题
# 如果已知一个三角形的三个顶点（2，3）（2，8）（8，5），求每一个角是几度？
"""
a向量 = (x2-x1,y2-y1)
cos = (a向量*b向量)/(a向量的模*b向量的模)
"""
"""
边长：d = sqrt((x2-x1)**2+(y2-t1)**2)
余弦值：cosa = (b^2+c^2-a^2)/2bc
    cosb = (a^2+c^2-b^2)/2ac
    cosc = (a^2+b^2-c^2)/2ab
先将坐标明确定义出来，
"""
"""import math # 导入math库
# 定义三个顶点坐标
x1,y1 = 2,3
x2,y2 = 2,8
x3,y3 = 8,5
# 计算边长  math.sqrt(x)：返回数字x的平方根。
a = math.sqrt((x2-x1)**2+(y2-y1)**2)
b = math.sqrt((x3-x2)**2+(y3-y2)**2)
c = math.sqrt((x1-x3)**2+(y1-y3)**2)
# 计算余弦值
cos_a = (b**2+c**2-a**2)/(2*b*c)
cos_b = (a**2+c**2-b**2)/(2*a*c)
cos_c = (a**2+b**2-c**2)/(2*a*b)
print(cos_a,cos_b,cos_c)
# 计算角度  math.degrees(x)：将弧度转换为角度
j_a = math.degrees(math.acos(cos_a))
j_b = math.degrees(math.acos(cos_b))
j_c = math.degrees(math.acos(cos_c))
# 输出结果
print(f'三角形的角是：{j_a:.2f}\t{j_b:.2f}\t{j_c:.2f}')
print(f"内角和为：{j_a+j_b+j_c:.2f}度")"""


import math # 导入math库

# 定义三个顶点坐标
x1,y1 = 2,3
x2,y2 = 2,8
x3,y3 = 8,5

# a向量(a1,a2)
a1 = x2-x1
a2 = y2-y1
# b向量(b1,b2)
b1 = x3-x1
b2 = y3-y1
# cos(a,b)=
cos_theta = (a1*b1+a2*b2)/((a1**2+a2**2)**0.5 * (b1**2+b2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta1 = math.degrees(cos_theta) # 弧度转角度
print(theta1)

# c向量(a1,a2)
c1 = x3-x2
c2 = y3-y2
# d向量(d1,d2)
d1 = x1-x2
d2 = y1-y2
# cos(c,d)=
cos_theta = (c1*d1+c2*d2)/((c1**2+c2**2)**0.5 * (d1**2+d2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta2 = math.degrees(cos_theta) # 弧度转角度
print(theta2)

# e向量(b1,b2)
e1 = x1-x3
e2 = y1-y3
# f向量(f1,f2)
f1 = x2-x3
f2 = y2-y3
# cos(e,f)=
cos_theta = (e1*f1+e2*f2)/((e1**2+e2**2)**0.5 * (f1**2+f2**2)**0.5) # 夹角公式，求夹角余弦（弧度）
cos_theta = math.acos(cos_theta)    # 反余弦
theta3 = math.degrees(cos_theta) # 弧度转角度
print(theta3)

print(theta1+theta2+theta3)
