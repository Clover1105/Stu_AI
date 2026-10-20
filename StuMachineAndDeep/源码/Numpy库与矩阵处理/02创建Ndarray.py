# 使用array函数创建Ndarray数组
# # 创建一维数组
# import numpy as np
#
#
# # 可以直接使用array函数进行创建
# arr1 = np.array([1, 2, 3, 4, 5])
# print(type(arr1))
# print(arr1)
# #
# # # 也可以将列表、元组等数据转化为Ndarray数组
# # ls1 = [1, 2, 3, 4, 5]
# # arr2 = np.array(ls1)
# # print(type(ls1))
# # print(type(arr2))
# # print(ls1)
# # print(arr2)
#
#
#
# # 创建二维数组
# import numpy as np
#
# # 可以直接使用array函数进行创建
# arr1 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
#
# print(type(arr1))
# print(arr1)
#
#
#
#
#
# # 创建三维数组
# import numpy as np
#
# # 可以直接使用array函数进行创建
# arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# print(type(arr1))
# print(arr1)




# # 使用arange函数创建Ndarray数组
# import numpy as np
#
# # 创建一个从0到9的数组
# arr1 = np.arange(10)
# print(arr1)
#
# # 创建一个从5到14的数组，步长为2
# arr2 = np.arange(5, 15, 2)
# print(arr2)
#
# # 创建一个从0到1的数组，包含10个值（步长为0.1）
# arr3 = np.arange(0, 1, 0.1)
# print(arr3)
#
# # 指定数据类型
# arr4 = np.arange(10, dtype=np.float32)
# print(arr4)


# # 创建全0数组：zeros
# # 创建一维全0数组
# import numpy as np
#
# arr1 = np.zeros(5)
#
# print(arr1)
#
#
# # 创建二维全0数组
# import numpy as np
#
# arr1 = np.zeros((3, 2))
#
# print(arr1)
#
#
#
#
# # 创建三维全0数组
# import numpy as np
#
# arr1 = np.ones((3, 2, 4))
#
# print(arr1)





# # empty: 创建空数组/创建未初始化的数组
# import numpy as np
#
# # 创建一个形状为 (2, 3) 的空数组
# x = np.empty((2, 3))
# print(x)
#
# # 创建一个形状为 (2, 3) 的空数组，数据类型为整型
# y = np.empty((2, 3), dtype=int)
# print(y)



# full: 创建指定形状、指定元素的数组
import numpy as np

# 创建一个形状为 (2, 3) 的数组，所有元素初始化为 7
x = np.full((2, 3), 7)
print(x)

# 创建一个形状为 (2, 3) 的数组，所有元素初始化为 5.5，数据类型为 float
y = np.full((2, 3), 5.5, dtype=int)
print(y)

