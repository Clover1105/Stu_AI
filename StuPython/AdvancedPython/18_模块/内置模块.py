#  内置模块示例 - Python安装时自带的模块，直接import使用

# sys模块
import sys
print(f"Python版本：{sys.version}")
print(f"操作系统：{sys.platform}")

# os模块
import os
print(f"当前工作目录：{os.getcwd()}")
print(f"文件是否存在：{os.path.exists('main.py')}")

# time模块
import time
print(f"时间戳：{time.time()}")
print(f"格式化时间：{time.strftime('%Y-%m-%d %H:%M:%S')}")