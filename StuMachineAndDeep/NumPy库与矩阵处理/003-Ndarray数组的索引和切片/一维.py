import numpy as np

a = (1,2,3,4,5,6,7,8,9,10)
np = np.array(a)
print(np)

# 索引
print(np[0])
print(np[7])
print(np[-1])
print(np[-6])
np[5] = 50
print(np)



# 切片
np1 = np[4:7]
print('4-7：', np1)
np2 = np[1:6:2]
print('1-6-2：', np2)
# 将一个标量值赋值给一个切片时，该值会自动传播到整个选区。
np[4:7] = 6
print('4-7：', np)
# 也可以使用:代表全部元素
np[:] = 10
print('0--1：', np)