
# # concatenate：将多个数组拼接起来
# import numpy as np
#
# # 创建两个数组
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
#
# print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
# print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
#
# # 沿着第一个轴（垂直方向）连接数组
# c = np.concatenate((b, a), axis=0)
# print(f'数组c的形状为{c.shape}, 数组c为：\n', c)
#
# # 沿着第二个轴（水平方向）连接数组
# d = np.concatenate((a, b.T), axis=1)
# print(f'数组b的转置的形状为{b.T.shape}, 数组b的转置为：\n', b.T)
# print(f'数组d的形状为{d.shape}, 数组d为：\n', d)




# # stack:
# import numpy as np
#
# # 创建两个一维数组
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.array([7, 8, 9])
#
# print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
# print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
#
# # # 沿着新的轴堆叠数组
# # d = np.stack((a, c, b), axis=0)
# # print(f'数组d的形状为{d.shape}, 数组d为：\n', d)
#
# # 沿着第二个轴堆叠数组
# e = np.stack((a, b), axis=1)
# print(f'数组e的形状为{e.shape}, 数组e为：\n', e)



# # hstack:
# import numpy as np
#
# # 创建两个 2x2 的矩阵
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
#
# print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
# print(f'数组b的形状为{b.shape}, 数组b为：\n', b)
#
# # 使用 hstack 进行水平堆叠
# c = np.hstack((a, b))
#
# # 输出结果
# print(f'数组c的形状为{c.shape}, 数组c为：\n', c)



import numpy as np

# 创建两个二维数组
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8, 9]])

print(f'数组a的形状为{a.shape}, 数组a为：\n', a)
print(f'数组b的形状为{b.shape}, 数组b为：\n', b)


# 使用 vstack 进行垂直堆叠
c = np.vstack((a, b))

# 输出结果
print(f'数组c的形状为{c.shape}, 数组c为：\n', c)