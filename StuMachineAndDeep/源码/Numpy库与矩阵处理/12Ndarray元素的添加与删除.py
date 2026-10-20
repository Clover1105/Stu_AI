
# append
import numpy as np

# # 创建一个一维数组
# arr = np.array([[1, 2, 3], [4, 5, 6]])
#
# # 要追加的值
# values = np.array([[1, 2, 3]])
#
# # 使用 numpy.append 追加值
# result = np.append(arr, values, axis=0)
#
# # 输出结果
# print(result)

# # 创建一个二维数组
# arr_2d = np.array([[1, 2], [3, 4]])
#
# # 要追加的值
# values_2d = np.array([[5], [6]])
#
# # 使用 numpy.append 追加值，沿着列方向
# result_2d = np.append(arr_2d, values_2d, axis=1)
#
# # 输出结果
# print(result_2d)




# insert
# import numpy as np
#
# # 创建一个一维数组
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)


# 在索引 2 的位置插入值 10
# result = np.insert(arr, 2, 10)

# 输出结果
# print(result)


# # 在索引 [1, 3] 的位置插入值 [20, 30]
# result_2 = np.insert(arr, [1, 3], [20, 10, 20])
#
# # 输出结果
# print(result_2)


# # 在二维数组中插入值
# arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr_2d)
#
# values = np.array([[5], [6], [7]])
#
# # 在索引 0 的位置沿着列方向插入值 [10]
# result_2d = np.insert(arr_2d, [0], values, 1)
#
# # 输出结果
# print(result_2d)



# delete

import numpy as np
#
# # 创建一个一维数组
# arr = np.array([1, 2, 3, 4, 5])

# # 删除索引 2 的元素
# result = np.delete(arr, 2)

# # 输出结果
# print(result)


# # 删除索引 [1, 3] 的元素
# result_2 = np.delete(arr, [1, 3])
#
# # 输出结果
# print(result_2)


# 在二维数组中删除元素
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # 删除索引 1 的列
# result_2d = np.delete(arr_2d, 0, axis=0)
#
# # 输出结果
# print(result_2d)


# 删除索引 [0, 2] 的行
result_2d_row = np.delete(arr_2d, [0, 2], axis=0)

# 输出结果
print(result_2d_row)