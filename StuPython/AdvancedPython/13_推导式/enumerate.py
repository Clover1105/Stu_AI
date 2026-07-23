"""
enumerate在推导式中的应用
    - enumerate()返回索引和元素
    - 常用于需要索引的推导式
    - 语法：enumerate(可迭代对象, start=0)
"""
# 1.创建索引-元素字典
colors = ["红", "黄", "蓝", "绿"]
color_dict = {idx: color for idx, color in enumerate(colors)}
print(f"索引-颜色字典：{color_dict}")

# 2.将列表中大于前一个元素的元素保留
nums = [10, 20, 15, 25, 30, 22, 35]
bao_liu = [num for i, num in enumerate(nums) if i == 0 or num > nums[i-1]]
print(f"原列表：{nums}")
print(f"递增序列：{bao_liu}")

# 3.添加索引信息到字符串列表
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
indexed = [f"{i+1}.{fruit}" for i, fruit in enumerate(fruits)]
print(f"带编号的水果：{indexed}")

# 4.提取奇数索引位置的元素
items = ["a", "b", "c", "d", "e", "f", "g"]
ji_index = [item for i, item in enumerate(items) if i % 2 == 1]
print(f"原列表：{items}")
print(f"奇数索引位置的元素：{ji_index}")