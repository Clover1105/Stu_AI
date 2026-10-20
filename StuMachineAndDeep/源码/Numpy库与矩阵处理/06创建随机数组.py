# # rand
# # 生成一个0~1之间的随机数
# import numpy as np
#
# # # 设置随机数种子
# # np.random.seed(10)
#
# arr1 = np.random.rand()
# print('arr1:', arr1)
#
# # 生成1个一行三列的随机数组
# import numpy as np
# arr2 = np.random.rand(3)
# print('arr2:', arr2)
#
# # 生成一个3行2列的随机数组
# import numpy as np
# arr3 = np.random.rand(3, 2, 1)
# print('arr3:', arr3)




# # random:
# import numpy as np
#
# # # 设置随机数种子
# # np.random.seed(10)
#
# # 生成一个一维数组，包含5个随机数
# array_1d = np.random.random(5)
# print(array_1d)
#
# # 生成一个二维数组，形状为 (2, 3)
# array_2d = np.random.random((2, 3))
# print(array_2d)


# randn:
# import numpy as np
#
#
# # # 设置随机数种子
# # np.random.seed(10)
#
# # 返回一个从标准正态分布中抽取的单个随机数
# print(np.random.randn())
#
# # 返回一个一维数组，包含5个从标准正态分布中抽取的随机数
# print(np.random.randn(5))
#
# # 返回一个二维数组，形状为2x3，元素从标准正态分布中抽取
# print(np.random.randn(2, 3))


# # normal:
# import numpy as np
#
# # # 设置随机数种子
# # np.random.seed(10)
#
# # 返回一个均值为0.0，标准差为1.0的正态分布中的单个随机数
# print(np.random.normal())
#
# # 返回一个均值为0.0，标准差为1.0的正态分布中的5个随机数
# print(np.random.normal(size=5))
#
# # 返回一个均值为5.0，标准差为2.0的正态分布中的5个随机数
# print(np.random.normal(loc=5, scale=2, size=5))
#
# # 返回一个2x3数组，其元素来自均值为10.0，标准差为3.0的正态分布
# print(np.random.normal(loc=10, scale=3, size=(2, 3)))
#



# # randint:
# import numpy as np
#
# # # 设置随机数种子
# # np.random.seed(10)
#
# # 从 0 到 10（不包含）之间随机生成一个整数
# print(np.random.randint(10))
#
# # 从 1 到 10（不包含）之间随机生成一个整数
# print(np.random.randint(1, 10))
#
# # 从 1 到 10（不包含）之间随机生成一个 3x3 的整数数组
# print(np.random.randint(1, 10, size=(3, 3)))
#
# # 从 1 到 10（不包含）之间随机生成一个 3x3 的整数数组，数据类型为 'int32'
# print(np.random.randint(1, 10, size=(3, 3), dtype=np.int64))


#
# # uniform:
# import numpy as np
#
# # 设置随机数种子
# np.random.seed(15)
#
# # 在 [0, 1) 范围内抽取一个浮点数
# print(np.random.uniform())
#
# # 在 [5, 10) 范围内抽取一个浮点数
# print(np.random.uniform(5, 10))
#
# # 在 [0, 1) 范围内抽取一个 3x3 的浮点数数组
# print(np.random.uniform(size=(3, 3)))
#
# # 在 [5, 10) 范围内抽取一个 2x3 的浮点数数组
# print(np.random.uniform(5, 10, size=(2, 3)))



# shuffle
import numpy as np

# 设置随机数种子
np.random.seed(10)

# 创建一个numpy数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 打乱数组
np.random.shuffle(arr)

print(arr)