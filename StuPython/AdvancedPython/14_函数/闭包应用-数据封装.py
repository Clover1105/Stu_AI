"""
闭包应用-数据封装
    - 使用闭包实现私有变量
    - 类似面向对象中的封装
    - 外部无法直接访问内部变量
"""
# 1.银行账户闭包
def create_account(initial_balance=0):
    """创建银行账户"""
    balance = initial_balance   # 100 --> 150 --> 120
    def deposit(amount):    # 50
        nonlocal balance    # 100
        if amount > 0:
            balance += amount   # 100+50=150
            print(f"存入{amount}元，余额：{balance}")
        else:
            print("存款金额必须大于0")
    def withdraw(amount):   # 30 --> 200
        nonlocal balance    # 150 --> 120
        if amount > balance:    # 200 > 120
            print(f"余额不足！当前余额：{balance}")
        elif amount <= 0:
            print("取款金额必须大于0")
        else:
            balance -= amount   # 150-30=120
            print(f"取出{amount}元，余额：{balance}")
    def get_balance():
        return balance
    return deposit, withdraw, get_balance
deposit, withdraw, get_balance = create_account(100)
deposit(50)
withdraw(30)
print(f"当前余额：{get_balance()}")
withdraw(200)  # 余额不足


# 2.闭包实现计数器带重置
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def reset():
        nonlocal count
        count = 0
        print("计数器已重置")
    def get():
        return count
    return increment, reset, get
inc, reset, get = create_counter()
print(inc(), inc(), inc())
reset()
print(inc(), inc())