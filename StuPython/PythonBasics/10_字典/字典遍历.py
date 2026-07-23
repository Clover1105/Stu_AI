"""
遍历字典
    - keys()：遍历所有键
    - values()：遍历所有值
    - items()：遍历所有键值对
"""
# 遍历键
student = {"name": "王芳", "age": 19, "grade": "A"}
print("遍历键：")
for key in student.keys():
    print(f"键：{key}")

# 遍历值
print("\n遍历值：")
for value in student.values():
    print(f"值：{value}")

# 遍历键值对
print("\n遍历键值对：")
for key, value in student.items():
    print(f"{key}: {value}")

# 直接遍历字典（默认遍历键）
print("\n直接遍历字典：")
for key in student:
    print(f"{key} -> {student[key]}")