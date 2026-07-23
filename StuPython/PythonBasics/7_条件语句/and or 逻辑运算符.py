# and or 逻辑运算符
def test():
    print("函数被执行")
    day = "周六"
    if day == "周六" or day == "周日":
        print("今天是周末")
    return True
result = False and test()  # test不会执行
print(f"短路and结果：{result}")
result = True or test()  # test不会执行
print(f"短路or结果：{result}")