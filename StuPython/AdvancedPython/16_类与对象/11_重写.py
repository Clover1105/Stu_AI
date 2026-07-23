"""
方法重写
    - 子类可以重新定义父类的方法
    - 调用时优先使用子类的方法
    - 可以通过super()调用父类的方法
"""

# 基本方法重写
class Animal:
    def speak(self):
        print("动物发出声音")
class Cat(Animal):
    def speak(self):  # 重写父类方法
        print("喵喵喵")
class Dog(Animal):
    def speak(self):  # 重写父类方法
        print("汪汪汪")
animals = [Animal(), Cat(), Dog()]
for a in animals:
    a.speak()


# 属性重写
class Parent:
    name = "父亲"
class Child(Parent):
    name = "儿子"  # 重写属性
print(f"Parent.name：{Parent.name}")
print(f"Child.name：{Child.name}")


# 使用super()调用父类方法
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        print(f"品牌：{self.brand}")
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # 调用父类初始化
        self.model = model
    def info(self):
        super().info()  # 调用父类方法
        print(f"型号：{self.model}")
car = Car("奔驰", "S级")
car.info()