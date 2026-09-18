# 复习yield

def func():
    print("start")
    yield 1
    print("end")

if __name__ == '__main__':
    # # 普通迭代
    # rs = func()
    # x = next(rs)
    # print(x)
    # y = next(rs,'')
    # print(y)

    # 循环迭代
    for x in func():
        print(x)
