"""
字典删除操作
    - del：删除指定键值对或整个字典
    - pop()：删除并返回指定键的值
    - clear()：清空字典
"""
# del删除键值对
person = {"name": "赵六", "age": 30, "city": "上海", "job": "工程师"}
print(f"原字典：{person}")
del person["job"]
print(f"删除job后：{person}")

# pop()删除并返回值
removed = person.pop("city")
print(f"删除的city值：{removed}")
print(f"pop后：{person}")

# clear()清空字典
person.clear()
print(f"clear后：{person}")

# del删除整个字典
data = {"a": 1, "b": 2}
del data
# print(data)  # 取消注释会报错：NameError
print("字典已被删除")