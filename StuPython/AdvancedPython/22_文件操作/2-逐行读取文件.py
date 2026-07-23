"""
- for循环遍历文件对象逐行读取
- readline()读取一行
- readlines()读取所有行返回列表
"""

# 创建测试文件
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("第一行：苹果\n第二行：香蕉\n第三行：橘子")

# 方法1：for循环逐行读取
print("=== for循环逐行读取 ===")
f = open("data.txt", "r", encoding="utf-8")
for line in f:
    print(f"读取一行：{line.strip()}")
f.close()

# 方法2：readline逐行读取
print("\n=== readline逐行读取 ===")
f = open("data.txt", "r", encoding="utf-8")
print(f"第一行：{f.readline().strip()}")
print(f"第二行：{f.readline().strip()}")
print(f"第三行：{f.readline().strip()}")
f.close()

# 方法3：readlines读取所有行
print("\n=== readlines读取所有行 ===")
f = open("data.txt", "r", encoding="utf-8")
lines = f.readlines()
print(f"列表内容：{lines}")
for i, line in enumerate(lines, 1):
    print(f"第{i}行：{line.strip()}")
f.close()