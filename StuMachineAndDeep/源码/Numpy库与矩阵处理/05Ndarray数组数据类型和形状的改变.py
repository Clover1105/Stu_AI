# # 修改Ndarray数组的数据类型
# import numpy as np
#
# # 创建一个浮点数数组
# arr = np.array([1.1, 2.2, 3.3])
#
# # 使用 astype 方法将数组转换为整数类型
# new_arr = arr.astype(np.int32)
#
# print("Original array:", arr)
# print("old type:", arr.dtype)
# print("New array:", new_arr)
# print("new type:", new_arr.dtype)


# # 修改Ndarray数组的形状
# # reshape：
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print('shape--a', a.shape)
#
# b = a.reshape((3, 2))
# print(a)
# print(b)
# print('shape--b',b.shape)






# # resize:
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print('before:', a.shape)
#
# a.resize((3, 2))
#
# print('after:', a.shape)
# print(a)
#
# # a.resize((2, 2))
# # print(a)
#
# a.resize((5, 5))
# print(a)



#
# # flatten:
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(a)
# b = a.flatten()
# print(b)
# b[0] = 10
# print(a)
# print(b)


# ravel:
# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = a.ravel()
# print(b)


# import numpy as np
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = a.flatten()
# c = a.ravel()
# d = a.ravel(order='F')
#
# a[0][0] = 100
# a[1][0] = 50
# print('a', a)
# print('b', b)
# print('c', c)
# print('d', d)



# T:转置：
import numpy as np

# 创建一个二维数组
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])

# 获取转置
transposed_arr = arr_2d.T

print("Original array:")
print(arr_2d)
print("Transposed array:")
print(transposed_arr)