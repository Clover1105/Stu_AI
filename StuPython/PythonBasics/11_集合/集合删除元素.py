"""
集合删除元素
    - remove()：删除指定元素，不存在时报错
    - discard()：删除指定元素，不存在时不报错
    - pop()：随机删除并返回一个元素
"""
# remove()删除
colors = {"红", "黄", "蓝", "绿"}
colors.remove("黄")
print(f"remove后：{colors}")
# colors.remove("紫")  # 取消注释会报错 KeyError（元素不存在）

# discard()删除（安全删除）
colors.discard("蓝")
colors.discard("紫")  # 不存在也不会报错
print(f"discard后：{colors}")

# pop()随机删除
random_item = colors.pop()
print(f"随机删除的元素：{random_item}")
print(f"pop后：{colors}")

# clear()清空
colors.clear()
print(f"clear后：{colors}")