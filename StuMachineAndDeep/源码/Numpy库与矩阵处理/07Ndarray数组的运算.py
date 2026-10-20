#
# # 标量与数组的运算：
# # 加法运算
# import numpy as np
#
# # 生成一个2行3列的Ndarray数组
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# # 数组加上标量，会使数组的每一个元素都加上该标量得到一个新数组
# b = arr / 2
#
# print('original: \n', arr)
# print('new: \n', b)






# 数组和数组的运算：
# 加法运算
# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # 数组加上数组，会使对应位置的元素相加
# arr3 = arr1 + arr2
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)

# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # add会使arr1和arr2中的每个对应位置的元素相加
# arr3 = np.add(arr1, arr2)
#
# print(arr1)
# print(arr2)
# # print('运算的结果为：\n', arr3)
#
# condition = np.array([[True, True, True], [False, False, False]], dtype=np.bool_)
# arr4 = np.add(arr1, arr2, where=condition)
# print('运算的结果为：\n', arr4)




# # 减法运算
# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # 数组减去数组，会使对应位置的元素相减
# arr3 = arr1 - arr2
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)


# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # subtract会使arr1中的每个元素减去arr2中的对应位置的元素
# arr3 = np.subtract(arr2, arr1)
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)

# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # multiply会使arr1中的每个元素乘以arr2中的对应位置的元素
# arr3 = np.multiply(arr1, arr2)
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)

# # 点积：
# import numpy as np
#
# # 二维数组矩阵乘法
# A = np.array([[1, 2, 3], [3, 4, 5]])
# B = np.array([[2, 0], [1, 3]])
# print(A)
# print(B)
# matrix_product = np.dot(A, B)
# print(matrix_product)



# # 除法：
# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # 数组除以数组，会使对应位置的元素相除
# arr3 = arr1 / arr2
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)


# import numpy as np
#
# # 生成两个2行3列的数组
# arr1 = np.array([[11, 12, 13], [14, 15, 16]])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#
# # divide会使arr1中的每个元素除以arr2中的对应位置的元素
# arr3 = np.divide(arr2, arr1)
#
# print(arr1)
# print(arr2)
# print('运算的结果为：\n', arr3)




# # 开根号：
# import numpy as np
#
# # 生成一个2行3列的数组
# arr1 = np.array([[4, 9, 16], [25, 36, 49]])
#
# # 开根号操作就是让一个数组进行0.5次方的幂运算
# arr2 = arr1 ** 0.5
#
# print(arr1)
# print('运算的结果为：\n', arr2)


import numpy as np

# 生成两个2行3列的数组
arr1 = np.array([[11, 12, 13], [14, 15, 16]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# power会使arr1中的每个元素为底数，arr2中的对应位置的元素为指数进行运算
arr3 = np.power(arr1, arr2)

print(arr1)
print(arr2)
print('运算的结果为：\n', arr3)