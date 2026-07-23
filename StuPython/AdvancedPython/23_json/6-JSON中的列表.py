"""
- JSON数组对应Python的列表
- 可以使用索引访问列表元素
- 可以使用列表方法操作（append、pop等）
"""

import json

# 包含列表的JSON数据
json_data = {
    "fruits": ["apple", "banana", "cherry"],
    "scores": [85, 92, 78, 90]
}

print("原始数据：")
print(f"水果列表：{json_data['fruits']}")
print(f"成绩列表：{json_data['scores']}")

# 访问列表元素
first_fruit = json_data["fruits"][0]
second_score = json_data["scores"][1]
print(f"\n第一个水果：{first_fruit}")
print(f"第二个成绩：{second_score}")

# 修改列表元素
json_data["fruits"][0] = "orange"
print(f"\n修改第一个水果后：{json_data['fruits']}")

# 添加新元素
json_data["fruits"].append("grape")
json_data["scores"].append(95)
print(f"添加后水果列表：{json_data['fruits']}")
print(f"添加后成绩列表：{json_data['scores']}")

# 转换为JSON字符串
json_str = json.dumps(json_data, ensure_ascii=False)
print(f"\nJSON字符串：{json_str}")