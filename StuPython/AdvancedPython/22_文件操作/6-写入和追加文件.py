"""
- "w"模式：覆盖写入，不存在则创建
- "a"模式：追加写入，末尾添加
- write()写入字符串
- writelines()写入字符串列表
"""

# 覆盖写
f = open("write_test.txt", "w", encoding="utf-8")
f.write("这是第一行\n")
f.write("这是第二行")
f.close()
# 验证写入结果
with open("write_test.txt", "r", encoding="utf-8") as f:
    print("覆盖写入后内容：")
    print(f.read())

# 追加写
f = open("write_test.txt", "a", encoding="utf-8")
f.write("\n这是追加的第三行")
f.close()
with open("write_test.txt", "r", encoding="utf-8") as f:
    print("\n追加写入后内容：")
    print(f.read())

# writelines写入列表
lines = ["苹果\n", "香蕉\n", "橘子"]
f = open("fruits.txt", "w", encoding="utf-8")
f.writelines(lines)
f.close()
with open("fruits.txt", "r", encoding="utf-8") as f:
    print("\nwritelines写入结果：")
    print(f.read())