# 作用：创建一个指定形状、数据类型且未初始化的数组
# 数组中的值是未定义的，可能包含任何值，因此创建数组后，应立即用有效值填充数组，以避免使用未定义的数据
"""
numpy.empty(shape, dtype=float, order='C')
"""

import numpy as np

# 创建一个形状为 (2, 3) 的空数组
x = np.empty((2, 3))
print(x)

# 创建一个形状为 (2, 3) 的空数组，数据类型为整型
y = np.empty((2, 3), dtype=int)
print(y)
