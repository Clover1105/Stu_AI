"""
算术运算：+ - * / // % **
逻辑运算：and or not
比较运算：> < == != >= <=
成员运算：in / not in
身份运算：is / is not
函数调用：fn() / obj.method() 也是表达式
条件表达式：值1 if 条件 else 值2（三元运算符）

注意事项：
逻辑运算返回的是短路后的值，不一定是布尔值
条件表达式可以嵌套使用，但可读性会下降
"""

## 算术运算表达式

a, b = 10, 3
print(f"a={a}, b={b}")
print(f"加法: a + b = {a + b}")
print(f"减法: a - b = {a - b}")
print(f"乘法: a * b = {a * b}")
print(f"除法: a / b = {a / b}")        # 结果是浮点数
print(f"整除: a // b = {a // b}")      # 取整
print(f"取余: a % b = {a % b}")        # 取余数
print(f"幂运算: a ** b = {a ** b}")    # 10的3次方

# 复杂运算表达式
x = (a + b) * (a - b) / 2
print(f"复杂运算 (a+b)*(a-b)/2 = {x}")

## 逻辑运算表达式

# and：全真才真，短路求值
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"10 and 20 = {10 and 20}")      # 返回20（短路后的值）
print(f"0 and 20 = {0 and 20}")        # 返回0（短路）

# or：一真则真，短路求值
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")
print(f"10 or 20 = {10 or 20}")        # 返回10（短路）
print(f"0 or 20 = {0 or 20}")          # 返回20

# not：取反
print(f"not True = {not True}")
print(f"not 10 = {not 10}")            # 非0数值为True，取反得False

## 比较运算表达式

print(f"10 > 5: {10 > 5}")
print(f"10 < 5: {10 < 5}")
print(f"10 == 10: {10 == 10}")
print(f"10 != 5: {10 != 5}")
print(f"10 >= 10: {10 >= 10}")
print(f"10 <= 5: {10 <= 5}")

# 链式比较
print(f"1 < 5 < 10: {1 < 5 < 10}")     # 等同于 1<5 and 5<10

## 成员和身份运算

# 成员运算 in / not in
arr = [1, 2, 3, 4, 5]
print(f"3 in arr: {3 in arr}")
print(f"6 in arr: {6 in arr}")
print(f"6 not in arr: {6 not in arr}")

# 身份运算 is / is not（比较内存地址）
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is z: {x is z}")      # True，同一个对象
print(f"x is y: {x is y}")      # False，不同对象但值相同
print(f"x == y: {x == y}")      # True，值相等

## 函数调用表达式

def add(x, y):
    return x + y

def outer():
    def inner():
        return "内部函数"
    return inner

# 函数调用
result = add(10, 20)            # 函数调用表达式
print(f"add(10, 20) = {result}")

# 链式调用
fn_result = outer()()           # 先调用outer得到inner，再调用inner
print(f"outer()() = {fn_result}")

# 方法调用
text = "hello world"
print(f"'hello world'.upper() = {text.upper()}")

## 条件表达式（三元运算符）

age = 18
status = "成年" if age >= 18 else "未成年"
print(f"age={age}, status={status}")

# 嵌套条件表达式（不推荐过度使用）
score = 85
level = "优秀" if score >= 90 else ("良好" if score >= 75 else "及格" if score >= 60 else "不及格")
print(f"score={score}, level={level}")