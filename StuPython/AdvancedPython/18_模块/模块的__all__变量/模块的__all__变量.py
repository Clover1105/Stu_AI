"""
知识点：模块的__all__变量
- __all__定义from module import *时导出的内容
- 未在__all__中的内容不会被导入
"""

# 题目：定义模块的公共接口

# 创建 mymodule.py 文件

# 使用from...import *导入
from mymodule import *

print(public_func())  # 可以访问

try:
    print(_private_func())
except NameError:
    print("私有函数无法访问")