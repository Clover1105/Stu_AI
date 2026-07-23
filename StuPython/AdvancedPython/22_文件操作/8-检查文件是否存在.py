"""
- os.path.exists()检查文件或目录是否存在
- 存在返回True，不存在返回False
- 操作文件前先检查避免异常
"""

import os

# 检查存在的文件
path1 = "test.txt"
if os.path.exists(path1):
    print(f"文件 {path1} 存在")
    with open(path1, "r", encoding="utf-8") as f:
        print(f"内容：{f.read()}")
else:
    print(f"文件 {path1} 不存在")

# 检查不存在的文件
path2 = "不存在的文件.txt"
if os.path.exists(path2):
    print(f"文件 {path2} 存在")
else:
    print(f"文件 {path2} 不存在，无法读取")

# 创建前检查避免覆盖
filename = "new_file.txt"
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("新创建的文件")
    print(f"已创建文件：{filename}")
else:
    print(f"文件已存在：{filename}")