"""
元组常用方法
    - count()：统计元素出现次数
    - index()：查找元素索引
    - len()：获取长度
    - in：判断是否存在
"""
# count()统计次数
t = (1, 2, 2, 3, 2, 4, 5, 2)
print(f"元组：{t}")
print(f"2出现了{t.count(2)}次")  # 统计元素2出现的次数

# index()查找索引
colors = ("红", "黄", "蓝", "绿", "黄")
print(f"第一个'黄'的索引：{colors.index('黄')}")

# len()和in
print(f"元组长度：{len(colors)}")
print(f"'红'是否在元组中：{'红' in colors}")
print(f"'紫'是否在元组中：{'紫' in colors}")

# 遍历元组
print("\n遍历元组：")
for item in colors:
    print(f"{item}")