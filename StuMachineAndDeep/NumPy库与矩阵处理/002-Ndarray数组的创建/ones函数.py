# 作用：创建指定长度或者形状的全 1 数组
"""
numpy.ones(shape, dtype=float, order='C')
"""

import numpy as np

# 创建一维全 1 数组
arr1 = np.ones(5)
print(arr1)

# 创建二维全 1 数组
arr1 = np.ones((3, 2))
print(arr1)

# 创建三维全 1 数组
arr1 = np.ones((3, 2, 4))
print(arr1)