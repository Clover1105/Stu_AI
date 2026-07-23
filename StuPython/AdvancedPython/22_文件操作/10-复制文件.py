"""
- shutil.copyfile()复制文件内容
- 源文件和目标文件路径
- 目标文件会被覆盖
"""

import shutil
import os

# 创建源文件
with open("source.txt", "w", encoding="utf-8") as f:
    f.write("这是源文件的内容\n复制测试")

print("源文件内容：")
with open("source.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 复制文件
shutil.copyfile("source.txt", "destination.txt")
print("\n复制成功！")

# 验证目标文件
print("目标文件内容：")
with open("destination.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 清理测试文件
os.remove("source.txt")
os.remove("destination.txt")
print("\n清理测试文件完成")