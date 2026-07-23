"""
动态添加包搜索路径
    - 使用sys.path.append()添加自定义包路径
    - 解决包不在默认搜索路径中的问题
"""

# 目录结构：
# /custom_libs/
#   mypackage/
#       __init__.py
#       tools.py

# 假设mypackage包不在当前目录，而在D:/custom_libs/下

import sys

# 添加自定义包路径
sys.path.append("D:/custom_libs")

try:
    import mypackage.tools

    print("成功导入自定义路径下的包")

    # 查看添加后的路径
    print(f"当前搜索路径包含自定义路径：{any('custom_libs' in p for p in sys.path)}")

except ImportError:
    print("包导入失败，请确认路径正确")