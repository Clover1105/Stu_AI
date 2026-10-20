# 该函数的作用与 Python 自带的 range() 类似
# 作用：只能返回一个一维数组（ndarray）
"""
numpy.arange(
    [start], -- 可选参数，表示数组的起始值。默认值为 0
    stop[, step,], -- stop必须参数，表示数组的结束值（不包含该值）;step可选参数，表示相邻两个值的差值。默认值为 1
    dtype=None, -- 可选参数，表示返回数组的数据类型。如果没有指定，则根据其他参数推断数据类型
)
"""

import numpy as np

l = np.arange(10)
print(l)

l = np.arange(4,15,3)
print(l)

l = np.arange(0,1,0.1)
print(l)

l = np.arange(10,dtype=np.float64)
print(l)