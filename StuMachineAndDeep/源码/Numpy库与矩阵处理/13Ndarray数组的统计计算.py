
# mean：求平均值
# import numpy as np

# # 创建一个一维数组
# arr = np.array([1, 2, 3, 4, 5])
#
# # 计算整个数组的平均值
# mean_arr = np.mean(arr)
#
# # 输出结果
# print(mean_arr)

# # 创建一个二维数组
# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr_2d)
#
# # 计算整个二维数组的平均值
# mean_arr_2d = np.mean(arr_2d)
#
# # 输出结果
# print(mean_arr_2d)
#
# # 计算二维数组沿着列的平均值
# mean_arr_2d_col = np.mean(arr_2d, axis=0)
#
# # 输出结果
# print(mean_arr_2d_col)
#
# # 计算二维数组沿着行的平均值
# mean_arr_2d_row = np.mean(arr_2d, axis=1)
#
# # 输出结果
# print(mean_arr_2d_row)
#
# # 使用 keepdims=True 保留维度
# mean_arr_2d_row_keepdims = np.mean(arr_2d, axis=1, keepdims=True)
#
# # 输出结果
# print(mean_arr_2d_row_keepdims)


#
# a = np.array([np.nan, 1, 2, 3])
# b = np.mean(a)
# print(b)



#
# # sum: 求和
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
# print(arr)
#
# # 计算整个数组的和
# total_sum = np.sum(arr)
# print(total_sum)
#
# # 计算每一列的和
# sum_col = np.sum(arr, axis=0, keepdims=True)
# print(sum_col)
#
# # 计算每一行的和
# sum_row = np.sum(arr, axis=1)
# print(sum_row)
#
# # 保留原始维度
# sum_row_keep = np.sum(arr, axis=1, keepdims=True)
# print(sum_row_keep)



#
# # max和min：求数组中的最大值和最小值
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
# print(arr)
#
# # 计算整个数组的最大值
# max_val = np.min(arr)
# print(max_val)
#
#
#
# # 计算每一列的最大值
# max_val_col = np.min(arr, axis=0)
# print(max_val_col)
#
#
# # 计算每一行的最大值
# max_val_row = np.min(arr, axis=1)
# print(max_val_row)
#



# # var:求方差
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
#
# # 计算整个数组的方差
# total_var = np.var(arr)
# print(total_var)
#
# # 计算每一列的方差
# var_col = np.var(arr, axis=0)
# print(var_col)
# # 计算每一行的方差
# var_row = np.var(arr, axis=1)
# print(var_row)
#




# # std:
# import numpy as np
#
# arr = np.array([[1, 2, 3]])
#
# total_var = np.var(arr)
# print(total_var)
# # 计算整个数组的标准差
# total_std = np.std(arr)
# print(total_std)
# # # 计算每一列的标准差
# # std_col = np.std(arr, axis=0)
# #
# # # 计算每一行的标准差
# # std_row = np.std(arr, axis=1)
# #
#
# # print(std_col)
# # print(std_row)




# # argmin和argmax：求最值元素的索引值
# import numpy as np
#
# arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
# print(arr)
#
# # 找出整个数组中的最大值和最小值的索引位置
# max_index = np.argmax(arr)
# min_index = np.argmin(arr)
#
# print(max_index)
# print(min_index)
#
# # 找出每一列中的最大值和最小值的索引位置
# max_index_col = np.argmax(arr, axis=0)
# min_index_col = np.argmin(arr, axis=0)
#
#
# print(max_index_col)
# print(min_index_col)
#
#
# # 找出每一行中的最大值和最小值的索引位置
# max_index_row = np.argmax(arr, axis=1)
# min_index_row = np.argmin(arr, axis=1)
#
# print(max_index_row)
# print(min_index_row)
#
#




# np.where:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
condition = arr > 5
print(arr)


result = np.where(condition)
print(result)