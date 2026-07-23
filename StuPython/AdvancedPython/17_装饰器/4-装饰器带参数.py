"""
装饰器带参数（修改参数）
    - 装饰器可以拦截并修改传入原始函数的参数
    - 在闭包函数中对参数进行处理后再传给原始函数
    - 原始函数接收的是处理后的数据
"""

# 将参数平方后传入
def tool(cb):
    def f(x, y):
        print("tool公共功能")
        cb(x**2, y**2)
    return f
@tool
def fn(x, y):
    print(f"fn函数的功能：{x}*{y}={x*y}")
fn(2, 3)  # 参数2,3被平方后传给fn: 4,9 -> 4*9=36
fn(3, 4)
fn(4, 5)


# 将参数相加后传入
def sum_decorator(cb):
    def f(x, y):
        cb(x + y)
    return f
@sum_decorator
def print_result(n):
    print(f"结果是：{n}")
print_result(2, 3)
print_result(3, 4)
print_result(4, 5)


# 参数过滤和转换
def filter_positive(cb):
    def f(*args):
        # 只保留正数
        positive_nums = [n for n in args if n > 0]
        cb(*positive_nums)
    return f
@filter_positive
def sum_all(*args):
    print(f"正数和：{sum(args)}")
sum_all(1, -2, 3, -4, 5)



"""
带参数的装饰器（装饰器工厂）
    - @tool 和 @tool() 的区别：
      @tool → 直接调用tool作为装饰器
      @tool() → 先调用tool()，返回值作为装饰器
    - 带参数的装饰器是三层嵌套函数
"""

# 基本带参数装饰器
def tool(n):
    print(f"外层接收参数：{n}")
    def g(cb):
        print("中间层接收原始函数")
        def f():
            print("内层执行装饰功能")
            cb()
        return f
    return g
@tool(10)   # 等价于 @g，g = tool(10)
def fn():
    print("fn函数的功能")
fn()


# 根据参数返回不同网址
def website(title):
    urls = {"百度": "baidu.com", "腾讯": "qq.com", "淘宝": "taobao.com"}
    def decorator(cb):
        def wrapper():
            print(f"{title}网址是：{urls.get(title, '未知')}")
            cb()
        return wrapper
    return decorator
@website("百度")
def baidu_func():
    print("访问百度")
@website("腾讯")
def tencent_func():
    print("访问腾讯")
@website("淘宝")
def taobao_func():
    print("访问淘宝")
baidu_func()
tencent_func()
taobao_func()