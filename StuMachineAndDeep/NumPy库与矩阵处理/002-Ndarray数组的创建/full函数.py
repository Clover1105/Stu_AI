# 作用：创建指定形状、指定元素（都为同一个）的数组
"""
numpy.full(
    shape,
    fill_value, -- 用于填充数组的值
    dtype=None,
    order='C'
)
"""

import numpy as np

# 创建一个形状为 (2, 3) 的数组，所有元素初始化为 7
x = np.full((2, 3), 7)
print(x)

# 创建一个形状为 (2, 3) 的数组，所有元素初始化为 5.5，数据类型为 float
y = np.full((2, 3), 5.5, dtype=float)
print(y)