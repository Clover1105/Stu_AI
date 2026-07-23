"""
字典基础
    - 用花括号{}定义
    - 键值对存储：key: value
    - 键必须是不可变类型（字符串、数字、元组）
    - 值可以是任意类型
"""
# 创建字典
person = {"name": "张三", "age": 25, "city": "北京"}
print(f"字典：{person}")
print(f"姓名：{person['name']}")
print(f"年龄：{person['age']}")

# 使用变量作为键
key_name = "email"
person[key_name] = "zhangsan@qq.com"
print(f"添加后：{person}")

# 嵌套字典
school = {"name": "第一中学",
          "classes": {"一班": 45, "二班": 42}
          }
print(f"学校：{school['name']}")
print(f"一班人数：{school['classes']['一班']}")