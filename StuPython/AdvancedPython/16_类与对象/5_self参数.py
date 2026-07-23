"""
self参数的使用
    - self代表调用该方法的对象本身
    - 通过self可以访问和修改对象的属性
    - self不是关键字，可以使用其他名字，但习惯用self
"""
# 1.self访问对象属性
class Student:
    life = 1
    school = "华清远见"

    def sleep(self):
        print(f"sleep方法被调用，self是：{self}")
s1 = Student()
s1.sleep()


# 2.self区分不同对象
class Cat:
    def introduce(self):
        print(f"我是猫：{self}")
cat1 = Cat()
cat2 = Cat()
cat1.introduce()
cat2.introduce()


# 3.通过self访问对象特有的属性
class Dog:
    def set_name(self, name):
        self.name = name
    def show_name(self):
        print(f"我的名字是：{self.name}")
d1 = Dog()
d2 = Dog()
d1.set_name("旺财")
d2.set_name("小黑")
d1.show_name()
d2.show_name()