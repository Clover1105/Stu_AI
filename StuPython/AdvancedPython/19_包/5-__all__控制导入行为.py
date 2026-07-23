"""
知识点：__all__控制导入行为
- __all__定义from 包 import *时导出的模块
- 未在__all__中的模块不会被导入
"""

# 目录结构：
# utilities/
#   __init__.py
#   file_tools.py
#   net_tools.py
#   secret_tools.py


# 使用*导入（只能导入__all__中指定的）
from utilities import *

print(file_tools.read_file("test.txt"))
print(net_tools.download("http://example.com"))

# 以下代码会报错，因为secret_tools不在__all__中
try:
    print(secret_tools.encrypt("secret"))
except NameError:
    print("secret_tools未被导入")