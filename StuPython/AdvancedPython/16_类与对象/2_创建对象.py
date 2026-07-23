"""
创建对象
    - 类名后面跟小括号即可创建对象
    - 对象是类的实例
    - 每个对象独立存储数据
"""
# 1.创建多个对象
class Student:
    life = 1
    school = "华清远见"
# 创建两个对象
s1 = Student()
s2 = Student()
print(f"s1对象：{s1}") # <__main__.Student object at 0x0000020E76B9D550>
print(f"s2对象：{s2}") # <__main__.Student object at 0x0000020E784D5310>
print(f"s1的school：{s1.school}")
print(f"s2的school：{s2.school}")


# 2.修改类的属性会影响所有对象
print(f"\n修改前 - s1.school：{s1.school}")
print(f"修改前 - s2.school：{s2.school}")
Student.school = "新大学"
print(f"\n修改后 - s1.school：{s1.school}")
print(f"修改后 - s2.school：{s2.school}")


# 3.验证对象是独立的
obj1 = Student()
obj2 = Student()
print(f"\nobj1和obj2是同一个对象吗？{obj1 is obj2}")