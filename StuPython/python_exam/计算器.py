"""
实现一个简单的计算器类 Calculator，支持： 
  加减乘除运算 
  历史记录功能（记录每次运算） 
  查看历史和清除历史的方法 
  使用 __call__ 方法支持 calc(a,op,b) 语法调用（对象当作函数调用时 自动调用）
"""
# class Calculator:
#     def __init__(self):
#         self.history_list = []
#     def __call__(self,a,op,b):
#         self.a = a
#         self.b = b
#         self.op = op
#         if self.op == "+":
#             self.result = self.add(self.a,self.b)
#         elif self.op == "-":
#             self.result = self.sub(self.a,self.b)
#         elif self.op == "*":
#             self.result = self.mul(self.a,self.b)
#         elif self.op == "/":
#             self.result = self.div(self.a,self.b)
#         else:
#             print("运算符错误")
#         return self.result
#     def add(self,a,b):  # 加法
#         self.history_list.append(f"{a} + {b} = {a + b}")
#         return print(f"{a} + {b} =", a + b)
#     def sub(self,a,b):  # 减法
#         self.history_list.append(f"{a} - {b} = {a - b}")
#         return print(f"{a} - {b} =", a - b)
#     def mul(self,a,b):  # 乘法
#         self.history_list.append(f"{a} * {b} = {a * b}")
#         return print(f"{a} * {b} =", a * b)
#     def div(self,a,b):  # 除法
#         self.history_list.append(f"{a} / {b} = {a / b}")
#         return print(f"{a} / {b} =", a / b)
#     def history(self):  # 查看历史记录
#         print("历史记录：")
#         for i in self.history_list:
#             print(i)
#     def clear_history(self):    # 清除历史记录
#         self.history_list.clear()
#         print("历史记录已清除",self.history_list)
#
# calc = Calculator()
# calc(100,"+",20)
# calc(100,"-",20)
# calc(100,"*",20)
# calc(100,"/",20)
# calc.history()
# calc.clear_history()


# 老师的代码
class Calculator:
    history=[]
    def calc(self,a, op, b):
        res=0
        if op=="+":
            res=a+b
        elif op=="-":
            res=a-b
        elif op=="*":
            res=a*b
        elif op=="/":
            res=a/b
        else:
            raise ValueError("不支持的运算符")
        self.history.append(f"{a}{op}{b}={res}")
        return  res
    def __call__(self, *args, **kwargs):
        return self.calc(*args, **kwargs)
    def get_history(self):
        return self.history
    def clear_history(self):
        self.history=[]
c=Calculator()
print(c(1, "+", 2))
print(c(1, "-", 2))
print(c(1, "*", 2))
print(c(1, "/", 2))
print(c.get_history())
c.clear_history()
print(c.get_history())