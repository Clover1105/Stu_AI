# 数字的类型：整型、浮点型、复数、布尔
x = 10  # 整数
print(x,type(x))
y = 20.5    # 浮点型
print(y,type(y))
z = (2+3j)  # 复数
print(z,type(z))
a = True    # 布尔（True--1、False--0）
print(a,type(a))


# 不同进制的数字表示
a = 500     # 十进制
x = 0b1010  # 二进制
y = 0o123   # 八进制
z = 0x123   # 十六进制
print(f"十进制a={a}\t二进制x={x}\t八进制y={y}\t十六进制z={z}")


# 进制转换函数
print(int(13.14))	    # 浮点转整型
print(float(520))	    # 整型转浮点型
print(bin(7))	    # 整型转二进制
print(oct(25))	    # 整型转八进制
print(hex(85))	    # 整型转十六进制
print(complex(29))	    # 整型转复数
print(complex(10,3))	# 浮点型转复数
