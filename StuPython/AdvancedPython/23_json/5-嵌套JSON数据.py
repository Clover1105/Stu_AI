"""
- JSON可以包含嵌套的对象和数组
- 通过多级键名访问嵌套值
- 可以递归地修改嵌套结构中的数据
"""

# 处理嵌套的JSON数据
import json

# 嵌套的JSON数据（Python字典形式）
json_data = {
    "name": "Alice",
    "info": {
        "age": 25,
        "location": "Paris",
        "contact": {
            "email": "alice@example.com",
            "phone": "123456789"
        }
    }
}

print("原始嵌套数据：")
print(f"姓名：{json_data['name']}")
print(f"年龄：{json_data['info']['age']}")
print(f"邮箱：{json_data['info']['contact']['email']}")

# 修改嵌套的值
json_data["info"]["location"] = "New York"
json_data["info"]["contact"]["phone"] = "987654321"

print("\n修改后：")
print(f"新位置：{json_data['info']['location']}")
print(f"新电话：{json_data['info']['contact']['phone']}")

# 转换为JSON字符串
new_json_str = json.dumps(json_data, ensure_ascii=False)
print(f"\n转换后的JSON字符串：{new_json_str}")