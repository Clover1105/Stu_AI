"""
表达式可以写在哪里：赋值右侧、函数参数、容器元素、索引/切片、字典键值等
表达式组成语句，语句是Python执行的基本单位
常见语句：赋值语句、条件语句、循环语句、函数调用语句、返回语句等

注意事项：
表达式一定产生一个值，语句不一定产生值（如if语句）
语句以换行或分号结束，代码块通过缩进组织
"""

## 表达式可以出现的位置

# 位置1：赋值语句的等号右侧
print("1. 赋值语句右侧")
x = 10 + 20                    # 算术表达式
y = max(5, 10, 3)              # 函数调用表达式
z = "hello" if True else "world"  # 条件表达式
print(f"  x={x}, y={y}, z={z}\n")

# 位置2：函数调用的参数
print("2. 函数参数位置")
def show(a, b, c):
    print(f"  参数值: a={a}, b={b}, c={c}")

show(10, 20 + 30, "ok" if 1 > 0 else "no")
print()

# 位置3：容器的元素
print("3. 容器元素位置")
arr = [10, 20 + 30, len("hello")]
tup = (5 * 2, max(1, 2, 3), "a" if False else "b")
dic = {"sum": 10 + 20, "product": 5 * 6}
print(f"  列表: {arr}")
print(f"  元组: {tup}")
print(f"  字典: {dic}\n")

# 位置4：索引和切片
print("4. 索引和切片位置")
arr = [10, 20, 30, 40, 50]
index = 2
print(f"  arr[{index}] = {arr[index]}")           # 索引位置
print(f"  arr[1:{index+2}] = {arr[1:index+2]}")   # 切片位置
print(f"  arr[::{len('step')}] = {arr[::len('step')]}\n")

# 位置5：字典的键
print("5. 字典键位置")
key_name = "name"
key_age = "age"
person = {key_name: "张三", key_age: 25}
print(f"  字典: {person}\n")

## 表达式嵌套（表达式内部还有表达式）

# 复杂表达式示例
result = (10 + 20) * (30 - 15) / (5 if 3 > 1 else 2)
print(f"复杂嵌套表达式结果: {result}")

# 嵌套函数调用
def square(x):
    return x * x

def double(x):
    return x * 2

result = square(double(5) + 3)  # double(5)=10, 10+3=13, square(13)=169
print(f"square(double(5) + 3) = {result}\n")

## 语句类型示例

# 赋值语句
print("1. 赋值语句")
a = 100
b, c = 10, 20
print(f"   a={a}, b={b}, c={c}")

# 表达式语句
print("2. 表达式语句（单独的表达式）")
print("   print('hello') 就是表达式语句")  # 函数调用作为表达式语句
len("test")  # 这也是一条表达式语句（虽然没实际作用）

# 条件语句
print("3. 条件语句")
score = 85
if score >= 60:
    print("   及格")
else:
    print("   不及格")

# 循环语句
print("4. 循环语句")
for i in range(3):
    print(f"   循环第{i+1}次")

# 函数定义语句
print("5. 函数定义语句")
def my_func():
    """这是一个函数定义语句"""
    return 100

# 返回语句
print("6. 返回语句（在函数内）")
def get_value():
    return 42  # 返回语句

# 导入语句
print("7. 导入语句")
import math
print(f"   math.pi = {math.pi}")

# 删除语句
print("8. 删除语句")
temp_var = 123
print(f"   删除前: {temp_var}")
del temp_var  # 删除变量
# print(temp_var)  # 取消注释会报错：NameError

## Python程序的层次结构
print("""
表达式 => 语句 => 代码块 => 模块/包 => 应用程序

举例：
  表达式: 10 + 20、x > 5
  语句: x = 10 + 20、if x > 5: print(x)
  代码块: if语句内部缩进的代码
  模块: 一个 .py 文件
  包: 包含 __init__.py 的文件夹
  应用程序: 多个模块/包组成的完整程序
""")