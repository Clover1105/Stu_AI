"""
- readable()判断是否可读
- writable()判断是否可写
- closed判断文件是否已关闭
- name获取文件名
- encoding获取编码（二进制模式无此属性）
"""

f = open("test.txt", "r", encoding="utf-8")

print(f"文件名：{f.name}")
print(f"是否可读：{f.readable()}")
print(f"是否可写：{f.writable()}")
print(f"是否已关闭：{f.closed}")
print(f"编码格式：{f.encoding}")

f.close()
print(f"\n关闭后是否已关闭：{f.closed}")

# 二进制模式没有encoding属性
f_b = open("test.txt", "rb")
print(f"\n二进制模式是否可读：{f_b.readable()}")
print(f"二进制模式是否有encoding属性：{hasattr(f_b, 'encoding')}")
f_b.close()