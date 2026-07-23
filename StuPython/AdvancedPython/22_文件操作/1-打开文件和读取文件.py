"""
- open()函数打开文件，返回文件对象
- encoding="utf-8"解决编码错误
- 路径：相对路径（同目录）或绝对路径
- read()读取整个文件内容
- read(n)指定读取n个字符
- close()关闭文件释放资源
"""

# 先创建测试文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python\n这是一个测试文件\n第三行内容")

# 打开并读取文件
f = open("test.txt", "r", encoding="utf-8")
res = f.read()
print("读取整个文件：")
print(res)
f.close()

# 指定读取字符数
f = open("test.txt", "r", encoding="utf-8")
res = f.read(5)
print(f"\n读取5个字符：{res}")
f.close()