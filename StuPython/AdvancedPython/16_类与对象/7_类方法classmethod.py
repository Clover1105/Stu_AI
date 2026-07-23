"""
类方法classmethod
    - 使用@classmethod装饰器定义类方法
    - 第一个参数是cls，代表类本身
    - 类方法可以通过类或对象调用
    - 类方法中只能访问类属性，不能访问对象属性
"""
# 1.定义和使用类方法
class Student:
    life = 1
    school = "华清远见"
    def fm(self):
        print(f"实例方法，self：{self}")
    @classmethod
    def fn(cls, x):
        print(f"类方法，cls：{cls}")
        print(f"传入参数x：{x}")
        print(f"访问类属性life：{cls.life}")
# 类调用类方法
Student.fn(10)
# 对象调用类方法
s1 = Student()
s1.life = 100  # 创建对象属性
s1.fn(20)  # 类方法仍然访问类属性，不会用对象属性


# 题目2：类方法中修改类属性
class Tool:
    count = 0
    @classmethod
    def add_count(cls):
        cls.count += 1
        print(f"当前计数：{cls.count}")
Tool.add_count()
Tool.add_count()
Tool.add_count()