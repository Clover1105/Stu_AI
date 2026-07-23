"""
类的私有属性
    - 使用双下划线__开头的属性是私有属性
    - 私有属性不能在类的外部直接访问
    - 可以在类内部通过self.__属性名访问
"""

# 定义私有属性
class BankAccount:
    __password = "123456"  # 私有属性
    money = 1000  # 公有属性
    def show_password(self):
        # 内部可以访问私有属性
        print(f"密码是：{self.__password}")
account = BankAccount()
# print(account.__password)  # 报错：外部无法访问私有属性
print(account.money)  # 公有属性可以访问
account.show_password()  # 通过内部方法访问


# 私有属性在不同对象间独立
class Person:
    __secret = "默认秘密"
    def set_secret(self, secret):
        self.__secret = secret
    def tell_secret(self):
        print(f"秘密是：{self.__secret}")
p1 = Person()
p2 = Person()
p1.set_secret("p1的秘密")
p2.set_secret("p2的秘密")
p1.tell_secret()
p2.tell_secret()

"""
类的私有方法
    - 使用双下划线__开头的方法是私有方法
    - 私有方法不能在类的外部直接调用
    - 可以在类内部通过self.__方法名()调用
"""

# 定义私有方法
class Calculator:
    def __add(self, a, b):
        """私有方法：内部计算逻辑"""
        return a + b
    def calculate(self, x, y):
        # 内部调用私有方法
        result = self.__add(x, y)
        print(f"{x} + {y} = {result}")
calc = Calculator()
# calc.__add(10, 20)  # 报错：外部无法调用私有方法
calc.calculate(10, 20)


# 私有方法用于内部验证
class User:
    def __check_password(self, pwd):
        """私有方法：验证密码"""
        return pwd == "admin123"
    def login(self, username, password):
        if self.__check_password(password):
            print(f"{username}登录成功")
        else:
            print("密码错误")
user = User()
user.login("张三", "123456")
user.login("张三", "admin123")

"""
私有属性和方法的访问限制
    - 私有成员只能在类内部访问
    - 子类也不能直接访问父类的私有成员
    - 这是封装特性的体现
"""

# 子类无法访问父类的私有属性
class Parent:
    __private_money = 1000
    public_money = 500
class Child(Parent):
    def show_money(self):
        # print(self.__private_money)  # 报错：子类也不能访问
        print(f"公有财产：{self.public_money}")
c = Child()
c.show_money()


# 私有方法也不能被继承调用
class Animal:
    def __private_breath(self):
        print("呼吸中...")
    def live(self):
        self.__private_breath()  # 内部可以调用
class Dog(Animal):
    def action(self):
        # self.__private_breath()  # 报错：无法调用父类私有方法
        print("汪汪叫")
dog = Dog()
dog.live()  # 通过公有方法间接调用私有方法
dog.action()


# 题目3：封装的意义
class SafeBox:
    def __init__(self):
        self.__password = "0000"
        self.__balance = 0
    def __verify(self, pwd):
        return pwd == self.__password
    def deposit(self, amount):
        self.__balance += amount
        print(f"存入{amount}元，余额{self.__balance}")
    def withdraw(self, pwd, amount):
        if self.__verify(pwd):
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"取出{amount}元，余额{self.__balance}")
            else:
                print("余额不足")
        else:
            print("密码错误")
box = SafeBox()
box.deposit(500)
box.withdraw("0000", 200)
box.withdraw("1234", 100)