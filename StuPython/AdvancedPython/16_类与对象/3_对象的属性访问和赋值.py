"""
对象的属性访问和赋值
    - 对象.属性：优先访问对象自己的属性
    - 如果对象没有该属性，则去类中查找
    - 对象.属性 = 值：会创建或修改对象自己的属性
"""
# 1.对象取值优先访问自己的属性
class Student:
    life = 1
    school = "华清远见"
s1 = Student()
print(f"初始时s1.school：{s1.school}")  # 从类中获取
# 给对象创建自己的school属性
s1.school = "重庆大学"
print(f"创建对象属性后s1.school：{s1.school}")  # 使用对象自己的属性
print(f"类的school属性不变：{Student.school}")


# 2.对象没有的属性会报错
s2 = Student()
# print(s2.age)  # 取消注释会报错：对象和类都没有age属性


# 3.给对象添加新属性
s2.age = 18
print(f"\ns2添加age属性后：{s2.age}")
# 另一个对象没有该属性
try:
    print(s1.age)
except AttributeError:
    print("s1没有age属性")