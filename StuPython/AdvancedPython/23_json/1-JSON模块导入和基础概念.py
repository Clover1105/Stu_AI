"""
- JSON是一种轻量级数据交换格式
- 本质是字符串，有特定格式
- Python内置json模块用于处理JSON数据
"""

# 导入json模块并查看JSON字符串格式
import json

# JSON字符串示例
json_str = '{"name": "张三", "age": 25, "city": "北京"}'
print(f"JSON字符串：{json_str}")
print(f"类型：{type(json_str)}")
print(f"JSON模块已导入：{json}")