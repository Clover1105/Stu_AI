
# squeeze: 降维
import numpy as np

# # 创建一个具有单维度的数组
# arr = np.array([[[1], [2], [3]]])
# print(arr)
# print("原始数组形状:", arr.shape)
#
# # 使用squeeze函数去掉所有单维度的条目
# squeezed_arr = np.squeeze(arr, axis=(0, 2))
# print(squeezed_arr)
# print("压缩后的数组形状:", squeezed_arr.shape)



# expand_dims:升维
import numpy as np

# 创建一个一维数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("原始数组形状:", arr.shape)
print(arr)

# # 在位置0增加一个维度
# expanded_arr = np.expand_dims(arr, axis=2)
# print("增加维度后的数组形状:", expanded_arr.shape)
# print(expanded_arr)

# 在位置1增加一个维度
expanded_arr = np.expand_dims(arr, axis=(0, 1))
print("增加维度后的数组形状:", expanded_arr.shape)
print(expanded_arr)