"""
集合推导式
    - 语法：{表达式 for 变量 in 可迭代对象 if 条件}
    - 自动去重
    - 无序
"""
# 1.从列表中创建唯一元素的集合
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unique_set = {x for x in numbers}
print(f"原列表：{numbers}")
print(f"集合（自动去重）：{unique_set}")

# 2.提取字符串中的唯一字符
text = "abracadabra"
unique_chars = {ch for ch in text}
print(f"字符串：{text}")
print(f"唯一字符：{unique_chars}")

# 3.筛选奇数的平方
squ_ji = {x**2 for x in range(1, 11) if x % 2 == 1}
print(f"奇数的平方（去重后）：{squ_ji}")

# 4.将字符串列表转为小写集合
words = ["Apple", "BANANA", "apple", "orange", "APPLE"]
lower_set = {word.lower() for word in words}
print(f"原列表：{words}")
print(f"小写集合（自动去重）：{lower_set}")