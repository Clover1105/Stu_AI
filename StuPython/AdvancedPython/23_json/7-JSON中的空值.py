"""
- JSON中使用null表示空值
- Python解析JSON时null转换为None
- Python序列化时None转换为null
"""

# JSON空值与Python None的转换
import json

# JSON字符串中的null
json_str = '{"name": "张三", "age": null, "address": null, "score": null}'
print(f"JSON字符串：{json_str}")

# 反序列化：null -> None
python_data = json.loads(json_str)
print(f"\n反序列化后：{python_data}")
print(f"age的值：{python_data['age']}")
print(f"age的类型：{type(python_data['age'])}")

# 检查是否为None
if python_data['address'] is None:
    print("address字段的值为None")

# 序列化：None -> null
python_dict = {"name": "李四", "age": None, "email": None}
json_result = json.dumps(python_dict)
print(f"\n序列化Python数据：{python_dict}")
print(f"生成的JSON字符串：{json_result}")