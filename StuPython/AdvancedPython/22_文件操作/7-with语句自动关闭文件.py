"""
- with语句自动管理文件生命周期
- 代码块结束后自动调用close()
- 不需要手动写f.close()
- 更安全、更简洁
"""

# 写入文件
with open("auto_close.txt", "w", encoding="utf-8") as f:
    f.write("使用with语句写入的内容\n")
    f.write("不需要手动关闭")
# with块结束后文件自动关闭

# 读取文件
with open("auto_close.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("读取的内容：")
    print(content)
# 文件已自动关闭，无需close()

# 验证文件已关闭
with open("auto_close.txt", "r", encoding="utf-8") as f:
    pass
print(f"文件对象已自动释放")