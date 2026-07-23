"""
pass语句
    - 空语句，占位符
    - 保持代码结构完整性
    - 不执行任何操作
"""
# pass作为占位符
age = 18
if age >= 18:
    pass  # 含义：暂时不写具体逻辑，稍后补充
else:
    print("未成年")
# 循环中的pass
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        pass  # 含义：偶数暂时不做处理
    else:
        print(f"奇数：{num}")


# 函数中的pass
def f():
    pass  # 函数体稍后实现


print("\n代码可以正常运行")