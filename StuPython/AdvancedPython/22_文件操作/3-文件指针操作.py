"""
- tell()获取当前指针位置
- seek(offset, whence)移动指针
  whence: 0文件开头 1当前位置 2文件结尾
- 中文字符UTF-8占3个字节
"""

with open("seek_test.txt", "w", encoding="utf-8") as f:
    f.write("abc123中文")

f = open("seek_test.txt", "r", encoding="utf-8")

print(f"初始指针位置：{f.tell()}")

# 读取3个字符
res = f.read(3)
print(f"读取3个字符：{res}")
print(f"读取后指针位置：{f.tell()}")

# 移动指针到开头
f.seek(0, 0)
print(f"seek到开头后指针：{f.tell()}")

# 移动指针到第6个字节
f.seek(6, 0)
print(f"seek到第6字节后指针：{f.tell()}")
print(f"从第6字节开始读：{f.read()}")

f.close()