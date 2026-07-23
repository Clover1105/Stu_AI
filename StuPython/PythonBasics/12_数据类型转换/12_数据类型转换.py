"""
数据类型转换
    - int()：转整数
    - str()：转字符串
    - list()：转列表
    - tuple()：转元组
    - set()：转集合
    - bool()：转布尔值
"""
# 字符串 --> 数字
num_str = "123"
num_int = int(num_str)  # 字符串全为数字时转换成功
print(f"字符串'{num_str}'转整数：{num_int}，类型：{type(num_int)}")

# 列表 --> 元组/集合
data_list = [1, 2, 2, 3, 4, 4, 5]
data_tuple = tuple(data_list)
data_set = set(data_list)
print(f"列表：{data_list}")
print(f"转元组：{data_tuple}")
print(f"转集合（自动去重）：{data_set}")

# 字符串 --> 列表/元组/集合
text = "hello"
print(f"字符串'{text}'转列表：{list(text)}")
print(f"字符串'{text}'转元组：{tuple(text)}")
print(f"字符串'{text}'转集合：{set(text)}")

# 列表去重：列表 --> 集合 --> 列表
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(f"\n原列表：{numbers}")
print(f"去重后：{unique_numbers}")

# 任意类型转字符串
print(f"数字转字符串：{str(100)}")
print(f"列表转字符串：{str([1, 2, 3])}")
print(f"字典转字符串：{str({'a': 1})}")
