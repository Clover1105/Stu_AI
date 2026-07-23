"""
多继承
    - 一个子类可以继承多个父类
    - 语法：class 子类(父类1, 父类2, ...)
    - 子类拥有所有父类的属性和方法
"""
# 基本多继承
class Flyable:
    def fly(self):
        print("可以飞行")
class Swimmable:
    def swim(self):
        print("可以游泳")
class Duck(Flyable, Swimmable):
    def quack(self):
        print("嘎嘎叫")
duck = Duck()
duck.fly()
duck.swim()
duck.quack()


# 多继承属性访问
class A:
    x = 1
class B:
    y = 20
class C(A, B):
    z = 30
obj = C()
print(f"来自A的x：{obj.x}")
print(f"来自B的y：{obj.y}")
print(f"自己的z：{obj.z}")


# 游戏角色多继承
class Fighter:
    power = 100
    def attack(self):
        print(f"攻击力：{self.power}")
class Mage:
    mana = 200
    def cast_spell(self):
        print(f"消耗法力：{self.mana}")
class BattleMage(Fighter, Mage):
    def __init__(self):
        self.health = 500
hero = BattleMage()
hero.attack()
hero.cast_spell()
print(f"生命值：{hero.health}")