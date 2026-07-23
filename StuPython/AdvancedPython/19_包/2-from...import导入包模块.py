"""
from...import导入包模块
    - from 包名 import 模块名
    - from 包名.模块名 import 标识符
"""

# 目录结构：
# shapes/
#   __init__.py
#   circle.py
#   rectangle.py

# 方式1：导入模块
from shapes import circle
print(f"圆面积：{circle.area(5)}")

# 方式2：直接导入函数
from shapes.rectangle import area
print(f"矩形面积：{area(4, 6)}")