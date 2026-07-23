"""
生成器与next()配合
    - 生成器对象可以使用next()逐个获取值
    - 生成器也可以用在for循环中
    - 两种方式都可以遍历生成器的值
"""
# 1.使用next()手动获取生成器值
def three_colors():
    yield "红"
    yield "黄"
    yield "蓝"
colors = three_colors()
print("使用next()逐个获取：")
print(next(colors))
print(next(colors))
print(next(colors))


# 2.生成器耗尽后继续next会报错
def two_numbers():
    yield 10
    yield 20
nums = two_numbers()
print(f"\n第一次next：{next(nums)}")
print(f"第二次next：{next(nums)}")
try:
    print(next(nums))
except StopIteration:
    print("第三次next：迭代器已耗尽")


# 3.生成器同时支持for和next
def simple_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
gen = simple_range(3)
print("\n先用next取一个：", next(gen))
print("再用for遍历剩余：", end=" ")
for num in gen:
    print(num, end=" ")
print()