"""
生成器应用-斐波那契数列
    - 使用生成器实现斐波那契数列
    - 斐波那契数列：1,1,2,3,5,8,13...
    - 每个数是前两个数之和
    - 生成器非常适合实现这种数列
"""
# 生成指定数量的斐波那契数
def fibonacci(n):
    """生成前n个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b
print("斐波那契数列前10项：")
fib_seq = fibonacci(10)
for num in fib_seq:
    print(num, end=" ")
print()

# 验证斐波那契数列
print("\n验证斐波那契数列：")
fib_seq2 = fibonacci(8)
result = list(fib_seq2)
print(f"前8项：{result}")
print("验证：1+1=2, 1+2=3, 2+3=5, 3+5=8...")

# 使用for循环遍历斐波那契生成器
print("\n使用for循环遍历：")
for num in fibonacci(6):
    print(f"斐波那契数：{num}")