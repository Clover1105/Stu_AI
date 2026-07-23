"""
字典get()方法
    - dict.get(key, default)
    - 键存在返回值，不存在返回默认值
    - 不会因为键不存在而报错
"""
# get()基本用法
person = {"name": "李四", "age": 20}
print(f"name：{person.get('name')}")
print(f"gender：{person.get('gender')}")  # 不存在返回None
print(f"city：{person.get('city', '未知')}")  # 指定默认值

# get()和直接访问
# 直接访问不存在会报错
try:
    print(person["gender"])
except KeyError:
    print("直接访问不存在的键会报错")

# get()不存在不会报错
result = person.get("gender")
print(f"get()不存在：{result}")

# 实际应用
user_input = input("请输入查询的键：")
value = person.get(user_input, "该键不存在")
print(f"查询结果：{value}")