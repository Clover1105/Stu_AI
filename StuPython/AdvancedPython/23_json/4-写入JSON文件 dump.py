"""
写入JSON文件 - json.dump()
    - 将Python数据类型写入JSON文件
    - 直接传入文件对象，无需先转换为字符串
    - 可以指定编码格式确保中文正常显示
"""

# 将Python数据写入JSON文件
import json

# 准备Python数据
python_list = [10, 20, 30, None, True, "中文测试"]

# 写入JSON文件
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(python_list, f)

print("数据已写入output.json文件")

# 验证写入结果
with open("output.json", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"文件内容：{content}")