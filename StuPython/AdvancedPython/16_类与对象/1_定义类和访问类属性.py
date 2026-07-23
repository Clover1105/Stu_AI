"""
定义类和访问类属性
    - 使用class关键字定义类
    - 类中可以定义属性和方法
    - 类属性是直接定义在类中的变量
    - 通过类名.属性名访问类属性
"""
# 1.定义一个简单的类
class Student:
    life = 1
    school = "华清远见"
print(f"类对象：{Student}") # <class '__main__.Student'>
print(f"访问类属性life：{Student.life}")
print(f"访问类属性school：{Student.school}")


# 2.修改类属性
print(f"\n修改前school：{Student.school}")
Student.school = "三峡科技大学"
print(f"修改后school：{Student.school}")


# 3.定义带方法的类
class Cat:
    name = "汤圆"
    def bark(): # 静态方法
        print("喵喵叫！")
print(f"\n猫的名字：{Cat.name}")
Cat.bark()