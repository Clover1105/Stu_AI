"""
生成器表达式
    - 语法：(表达式 for 变量 in 可迭代对象 if 条件)
    - 返回生成器对象，不立即生成所有数据
    - 节省内存，适合大数据量
"""
# 1.创建生成器对象
gen = (x**2 for x in range(1, 6))
print(f"生成器对象：{gen}")
print(f"生成器类型：{type(gen)}")

# 2.遍历生成器获取值
print("生成器中的值：", end="")
for value in gen:
    print(value, end=" ")
print()

# 3.使用next()逐个获取
gen2 = (x * 10 for x in range(1, 4))
print(f"第一个值：{next(gen2)}")
print(f"第二个值：{next(gen2)}")
print(f"第三个值：{next(gen2)}")

# 4.生成器表达式用于函数参数
total = sum(x**2 for x in range(1, 11))
print(f"1-10平方和：{total}")

# 5.找出1-100中的偶数
evens = (x for x in range(1, 101) if x % 2 == 0)
print(f"前5个偶数：", end="")
for i, e in enumerate(evens):
    if i < 5:
        print(e, end=" ")
    else:
        break
print()