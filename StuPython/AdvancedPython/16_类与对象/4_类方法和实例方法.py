"""
类方法和实例方法
    - 实例方法：第一个参数通常是self，表示调用该方法的对象
    - 类调用实例方法时不会自动传参
    - 对象调用实例方法时会自动传入对象自身作为第一个参数
"""
# 1.定义带参数的方法
class Student:
    life = 1
    school = "华清远见"
    def sleep(x, y):
        print(f"x参数：{x}, y参数：{y}")
        print(f"x和y是否相等：{x == y}")
# 类调用方法：需要传入所有参数
Student.sleep(10, 20)


# 2.对象调用方法会自动传入对象
s1 = Student()
print(f"s1对象：{s1}")
# s1.sleep(s1, 30)  # 报错，因为对象调用实例方法时 会自动传入对象自身作为第一个参数，后面的30就溢出了
s1.sleep(30)    # 手动传入对象


# 3.对象调用方法的实际机制
class Person:
    def introduce(self):
        print(f"我是{self}")
p = Person()
print(f"p对象：{p}")
p.introduce()  # 等价于 Person.introduce(p)