"""
break语句
    - 立即终止当前循环
    - break后面的代码不执行
    - 只终止最内层的循环
"""
# break在嵌套循环中的效果
print("\n嵌套循环中的break：")
for i in range(3):
    for j in range(5):
        if j == 2:
            break  # 只终止内层循环
        print(f"i={i}, j={j}")
    print(f"内层循环结束，继续外层i={i}")

"""
continue语句
    - 跳过当前循环的剩余代码
    - 继续下一次循环迭代
    - 不终止整个循环
"""
# 跳过指定字符
text = "hello world"
print(f"\n跳过'o'字符：")
for char in text:
    if char == 'o':
        continue
    print(char, end="")