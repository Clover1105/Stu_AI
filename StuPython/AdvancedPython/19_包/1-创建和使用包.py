"""
创建和使用包
    - 包是一个包含__init__.py文件的目录
    - 包用于组织和管理相关模块
    - 使用import 包名.模块名 导入
"""

# 目录结构：
# mypackage/
#   __init__.py
#   math_utils.py
#   string_utils.py

# 使用包
import mypackage.math_utils
import mypackage.string_utils

result1 = mypackage.math_utils.add(10, 20)
result2 = mypackage.string_utils.to_upper("hello")

print(f"加法结果：{result1}")
print(f"转大写：{result2}")