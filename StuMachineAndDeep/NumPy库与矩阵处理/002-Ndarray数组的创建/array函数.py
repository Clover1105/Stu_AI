# 作用：创建Ndarray数组
"""
numpy.array(
    object, -- 可迭代对象
    dtype=None, -- 指定类型
    copy=True, -- 是否复制
    order='K',  -- 尽可能与输入数据的顺序一致
    subok=False, -- True，则返回的数组将是输入对象的子类；False，则返回的数组将始终是基类数组
    ndmin=0, -- 指定数组的最小维度
)
"""

import numpy as np

# 一维
print("-*"*10," 一维 ","-*"*10)
l = np.array([1, 2, 3])
print(type(l))
print(l)

# 二维
print("-*"*10," 二维 ","-*"*10)
l = np.array([[1,2,3,4],[4,5,6,7]])
print(type(l))
print(l)

# 三维
print("-*"*10," 三维 ","-*"*10)
l = np.array([[[1,2,3,4],[5,6,7,8]],[[10,11,12,13],[14,15,16,17]],[[44,55,66,77],[47,58,69,14]]])
print(type(l))
print(l)
