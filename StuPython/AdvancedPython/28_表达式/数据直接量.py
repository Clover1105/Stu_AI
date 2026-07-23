"""
表达式：可以被求值的代码，运行后会产生一个结果（数据）
数据直接量：直接写出的具体数据值，是最简单的表达式
包含：数字、字符串、布尔、None、列表、元组、字典、集合等

注意事项：
表达式可以写在任何需要数据的地方（赋值、函数参数、容器元素等）
每个表达式都有类型，可以通过 type() 查看
"""

## 基本数据直接量

# 数字直接量
x = 10                    # 整数
y = 3.14                  # 浮点数
z = 1 + 2j                # 复数
print(f"数字: {x}, {y}, {z}")

# 字符串直接量
s1 = "hello"
s2 = 'world'
s3 = """多行
字符串"""
print(f"字符串: {s1}, {s2}")

# 布尔和None
b1 = True
b2 = False
n = None
print(f"布尔: {b1}, {b2}, None: {n}")

## 容器类型直接量

# 列表直接量
arr = [10, 20, 30, 40]
print(f"列表: {arr}, 类型: {type(arr)}")

# 元组直接量（注意单元素元组需要逗号）
t1 = (10, 20, 30)
t2 = (10,)      # 单元素元组必须有逗号
t3 = ()         # 空元组
print(f"元组: {t1}, {t2}, {t3}")

# 字典直接量（键值对）
d = {"name": "张三", "age": 25, "city": "北京"}
print(f"字典: {d}, 类型: {type(d)}")

# 集合直接量（无序、不重复）
s = {10, 20, 30, 30}    # 重复的30会被去重
print(f"集合: {s}, 类型: {type(s)}")

## 类创建对象的表达式

# 内置类型创建对象
num = int(10)           # 创建整数对象
text = str("hello")     # 创建字符串对象
lst = list([1, 2, 3])   # 创建列表对象
dct = dict(name="李四", age=30)  # 创建字典对象

print(f"int(): {num}, 类型: {type(num)}")
print(f"str(): {text}")
print(f"list(): {lst}")
print(f"dict(): {dct}")

# 自定义类创建对象
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student("王五", 20)    # 创建自定义对象
print(f"自定义类对象: {stu.name}, {stu.age}")