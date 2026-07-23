"""
- 使用pip install 模块名安装
- 安装后可以像内置模块一样导入使用
"""

# 题目：安装并使用numpy模块

# 安装命令：pip install numpy

import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(f"数组：{arr}")
print(f"平均值：{np.mean(arr)}")
print(f"数组形状：{arr.shape}")