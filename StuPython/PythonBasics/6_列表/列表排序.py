"""
列表排序
    - sort()：原地排序
        - key参数：指定排序规则
        - reverse参数：降序
    - sorted()：对列表进行排序并返回一个新的列表
"""
# sort()：原地排序，默认升序，降序为reverse=True
num = [3, 1, 4, 1, 5, 9]
num.sort()  # 在原列表上进行排序
print(f"升序：{num}")
num.sort(reverse=True)
print(f"降序：{num}")

# 按绝对值排序
num = [-5, 3, -2, 8, -1]
num.sort(key=abs)
print(f"按绝对值排序：{num}")
num.sort(key=lambda x:abs(x-10))
print(f"减10后按绝对值排序：{num}")

# 按字符串长度排序
words = ["python", "java", "c", "javascript"]
words.sort(key=len)
print(f"按长度排序：{words}")

# sorted()：对列表进行排序并返回一个新的列表
l1 = [5, 2, 4, 1, 3]
l2 = sorted(l1) # 返回一个新列表，不改变原列表
print(f"排序后：{l2}")