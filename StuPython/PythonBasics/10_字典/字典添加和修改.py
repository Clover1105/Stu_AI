"""
字典添加和修改
    - 通过键赋值：dict[key] = value
    - 键存在则修改，不存在则添加
    - 键不存在时取值会报错
"""
# 添加新键值对
scores = {}
scores["语文"] = 90
scores["数学"] = 85
print(f"添加后：{scores}")

# 修改已有键的值
scores["数学"] = 95
print(f"修改数学成绩后：{scores}")

# 键不存在时报错
# print(scores["英语"])  # 取消注释会报错 KeyError

# 安全访问方式
if "英语" in scores:
    print(scores["英语"])
else:
    print("英语成绩不存在")