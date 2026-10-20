# import numpy as np
#
# arr = np.array([1, 2, 3, 4, 5])
#
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print(arr)
# print(type(arr))
#
# # Numpy数组可以直接进行加1操作，它会令数组中的所有的元素都去进行加1
# arr = arr + 1
#
# print(arr)






# # 使用list完成两个列表元素的加法
# a = [1, 2, 3, 4, 5]
# b = [5, 4, 3, 2, 1]
#
# # # python中支持两个列表直接相加，但相加的结果是两个列表拼接的结果
# # # 不是我们想要的对应元素进行数值运算的结果
# # c = a + b
# # print(c)
#
# # 只能是通过遍历的形式去拿到每个元素再去进行算术运算
# c = []
# for i in range(len(a)):
#     c.append(a[i] + b[i])
# print(c)




import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

# Ndarray数组可以通过两个数组变量之间的运算直接对数组中的元素进行算术运算
c = a + b
print(c)






