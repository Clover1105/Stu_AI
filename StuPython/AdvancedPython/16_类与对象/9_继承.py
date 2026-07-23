"""
单继承
    - 子类继承父类的属性和方法
    - 语法：class 子类(父类):
    - 子类可以添加新的属性和方法
"""

# 基本继承
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name}在吃东西")
class Dog(Animal):
    def bark(self):
        print(f"{self.name}在汪汪叫")
dog = Dog("旺财")
dog.eat()  # 继承自父类
dog.bark()  # 自己的方法


# 继承父类属性
class Person:
    species = "人类"
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def info(self):
        print(f"{self.name}，{self.age}岁，{self.species}，年级{self.grade}")
stu = Student("小明", 18, "高三")
stu.info()


# 继承关系判断
class A:
    pass
class B(A):
    pass
b = B()
print(f"b是B的实例：{isinstance(b, B)}")
print(f"b是A的实例：{isinstance(b, A)}")
print(f"B是A的子类：{issubclass(B, A)}")