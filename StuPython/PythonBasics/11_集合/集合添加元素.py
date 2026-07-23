"""
集合添加元素：
    - add()：添加单个元素
    - update()：添加多个元素（可迭代对象）
    - 重复元素不会添加
"""
# add()添加单个元素
fruits = {"苹果", "香蕉"}
fruits.add("橘子")
fruits.add("苹果")  # 重复不会添加
print(f"add后：{fruits}")

# update()添加多个元素
numbers = {1, 2, 3}
numbers.update([4, 5, 6])  # 添加列表
numbers.update((7, 8))  # 添加元组
numbers.update({9, 10})  # 添加集合
print(f"update后：{numbers}") # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 批量添加字符串
chars = set()
chars.update("abc")  # 字符串是可迭代对象，会拆分成字符
print(f"字符串拆分成字符：{chars}")