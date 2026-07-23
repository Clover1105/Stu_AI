"""
- os.remove()删除文件
- os.rename()重命名文件
- 操作前检查文件是否存在
"""

import os

# 创建测试文件
with open("old_name.txt", "w", encoding="utf-8") as f:
    f.write("这是要重命名的文件")

print("=== 重命名文件 ===")
print(f"原文件是否存在：{os.path.exists('old_name.txt')}")

os.rename("old_name.txt", "new_name.txt")
print(f"重命名后新文件是否存在：{os.path.exists('new_name.txt')}")

with open("new_name.txt", "r", encoding="utf-8") as f:
    print(f"文件内容：{f.read()}")

print("\n=== 删除文件 ===")
# 创建要删除的文件
with open("to_delete.txt", "w", encoding="utf-8") as f:
    f.write("这个文件即将被删除")

print(f"删除前文件是否存在：{os.path.exists('to_delete.txt')}")
os.remove("to_delete.txt")
print(f"删除后文件是否存在：{os.path.exists('to_delete.txt')}")

# 清理
os.remove("new_name.txt")