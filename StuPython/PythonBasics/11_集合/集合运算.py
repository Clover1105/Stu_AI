"""
集合运算
    - 交集(&)：两个集合都有的元素 --> intersection()
    - 并集(|)：两个集合的所有元素 --> union()
    - 差集(-)：在第一个但不在第二个的元素 --> difference()
    - 对称差集(^)：不同时存在于两个集合的元素 --> symmetric_difference()
"""
# 交集（&）
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"集合A：{set_a}")
print(f"集合B：{set_b}")
print(f"交集(&)：{set_a & set_b}")
print(f"intersection()：{set_a.intersection(set_b)}")

# 并集（|）
print(f"并集(|)：{set_a | set_b}")
print(f"union()：{set_a.union(set_b)}")

# 差集（-）
print(f"差集(A-B)：{set_a - set_b}")
print(f"difference()：{set_a.difference(set_b)}")

# 对称差集（^）
print(f"对称差集(^)：{set_a ^ set_b}")
print(f"symmetric_difference()：{set_a.symmetric_difference(set_b)}")