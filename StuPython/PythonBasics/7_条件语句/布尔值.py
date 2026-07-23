# 布尔值
# bool()：将数据转换为布尔值
# False值：None, 0, 空字符串, 空列表, 空字典等
# 其他值都为True
a = 10 > 20
b = 100 == 200
c = 10 is 10    # 比较内存地址是否相同（是否为同一个对象）
d = 10 is not 10    # 比较内存地址是否相同（是否为同一个对象）
e = 10 != 10
print(a,b,c,d,e)
# 测试各种数据的布尔值：空和0是False，其他是True
test = [None, 0, 1, -1, "", " ", "hello",
        [], [0], [1, 2], (), (1,)]
for i in test:
    print(f"{str(i)} --> {bool(i)}")