# 作用：创建指定长度或者形状的全 0 数组
"""
numpy.zeros(
    shape, -- 一个整数或整数元组，用于指定输出数组的形状
    dtype=float, -- 可选参数，指定数组元素的数据类型。默认为 float
    order='C' -- 可选参数，指定数组数据在内存中的存储顺序。‘C’ 表示按行（C语言风格），‘F’ 表示按列（Fortran风格）
)
"""
import numpy as np

# 创建一维全 0 数组
arr1 = np.zeros(5)
print(arr1)

# 创建二维全 0 数组
arr1 = np.zeros((3, 2))
print(arr1)

# 创建三维全 0 数组
# 3个二维数组，每个二维数组有2行4列
arr1 = np.zeros((3, 2, 4))
print(arr1)