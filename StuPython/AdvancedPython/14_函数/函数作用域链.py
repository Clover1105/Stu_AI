"""
函数作用域链
    - 变量查找顺序：当前函数 -> 外层函数 -> 全局
    - 函数定义的位置决定作用域链
    - 函数调用位置不影响作用域链
"""
# 1.作用域链查找
global_var = "全局变量"
def outer():
    outer_var = "outer变量"
    def inner():
        inner_var = "inner变量"
        # 查找顺序：inner -> outer -> 全局
        print(f"访问inner_var：{inner_var}")
        print(f"访问outer_var：{outer_var}")
        print(f"访问global_var：{global_var}")
    inner()
outer()


# 2.函数定义位置决定作用域
x = 100
def func1():
    print(f"func1中x={x}")
def func2():
    x = 200
    func1()  # func1的x是在定义时决定的，不是调用时
func2()


# 3.多层作用域查找
a = 1
def func_a():
    a = 2
    def func_b():
        a = 3
        def func_c():
            print(f"func_c中访问a：{a}")  # 找到func_b的a=3
        func_c()
    func_b()
func_a()