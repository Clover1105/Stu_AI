"""
从JSON文件加载 - json.load()
    - 读取JSON文件并转换为Python数据类型
    - 不需要先读取文件内容再使用loads
    - 直接传入文件对象即可
"""

# 从JSON文件中读取数据
import json

# 先创建一个JSON文件
test_data = {"name": "李四", "age": 20, "city": "上海"}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(test_data, f)

# 从JSON文件加载数据
with open("data.json", "r", encoding="utf-8") as f:
    python_data = json.load(f)

print(f"从文件加载的数据：{python_data}")
print(f"数据类型：{type(python_data)}")
print(f"姓名：{python_data['name']}")