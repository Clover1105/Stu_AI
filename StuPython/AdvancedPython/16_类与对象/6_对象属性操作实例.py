"""
对象属性操作实例
    - 综合演示对象属性的添加、修改和访问
    - 理解对象属性和类属性的区别
"""
# 1.赚钱案例
class Student:
    life = 1
    school = "华清远见"
    money = 100
    def make_money(self, money):
        """赚钱方法"""
        self.money = self.money + money
    def look_money(self):
        print(f"{self.name}的money是：{self.money}")
# 创建学生对象
s1 = Student()
s2 = Student()
# 给对象添加name属性
s1.name = "小王"
s2.name = "小里"
# 查看初始金额
s1.look_money() # 100
s2.look_money() # 100
# s1赚钱
s1.make_money(10)   # s1: 100 + 10 = 110
s1.look_money() # 110
s2.look_money() # 100
# s1继续赚钱
s1.make_money(10)   # s1: 110 + 10 = 120
s1.look_money() # 120
s2.look_money() # 100


# 2.理解self.money的含义
class Test:
    money = 100
    def add_money(self, amount):
        # self.money：对象的money属性
        # self.money + amount：计算新值
        # self.money = ...：赋值给对象的money属性
        self.money = self.money + amount
        print(f"添加{amount}后：{self.money}")
t = Test()
t.add_money(50)
print(f"类属性money仍然是：{Test.money}")