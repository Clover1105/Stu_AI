"""
序列化 - json.dumps()
    - 将Python数据类型转换为JSON格式字符串
    - Python的None转为JSON的null
    - Python的True/False转为JSON的true/false
"""

# 将Python字典转换为JSON字符串
import json

# Python数据
python_dict = {
    "title": "华清远见",
    "url": "https://www.hqyj.com",
    "price": None,
    "is_available": True,
    "scores": [10, 20, 30]
}

# 序列化：Python数据 -> JSON字符串
json_str = json.dumps(python_dict)

print(f"原始Python数据：{python_dict}")
print(f"类型：{type(python_dict)}")
print(f"\n转换后的JSON字符串：{json_str}")
print(f"类型：{type(json_str)}")



"""
反序列化 - json.loads()
    - 将JSON格式的字符串转换为Python数据类型
    - JSON中的null转为Python的None
    - JSON中的true/false转为Python的True/False
"""

# 将JSON字符串转换为Python字典
import json

# 包含多种数据类型的JSON字符串
json_str = '{"name": "alex", "age": 18, "score": null, "is_student": true, "hobbies": ["reading", "swimming"]}'

# 反序列化：JSON字符串 -> Python数据
python_data = json.loads(json_str)

print(f"转换后的Python数据类型：{type(python_data)}")
print(f"内容：{python_data}")
print(f"姓名：{python_data['name']}")
print(f"成绩(null转为None)：{python_data['score']}")
print(f"是否学生：{python_data['is_student']}")
print(f"爱好列表：{python_data['hobbies']}")