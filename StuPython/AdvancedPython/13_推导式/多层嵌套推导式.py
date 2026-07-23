"""
多层嵌套推导式
    - 处理三层或更多层的嵌套结构
    - 注意可读性，过于复杂应改用循环
    - 从外层到内层依次写for
"""
# 1.处理三层嵌套列表
three_level = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # three_level：三层
flatten = [num for level2 in three_level for level1 in level2 for num in level1]
# flatten = []
# for level2 in three_level:
#     for level1 in level2:
#         for num in level1:
#             flatten.append(num)
print(f"三层嵌套：{three_level}")
print(f"完全展平：{flatten}")

# 2.提取嵌套字典中的特定值
students = [
    {"name": "张三", "scores": {"语文": 85, "数学": 92}},
    {"name": "李四", "scores": {"语文": 78, "数学": 88}},
    {"name": "王五", "scores": {"语文": 95, "数学": 91}}
]
math_scores = [s["scores"]["数学"] for s in students]
# math_scores = []
# for s in students:
#     math_scores.append(s["scores"]["数学"])
print(f"所有学生的数学成绩：{math_scores}")

# 3.从复杂结构中提取数据
data = [
    {"id": 1, "tags": ["python", "编程"]},
    {"id": 2, "tags": ["java", "开发"]},
    {"id": 3, "tags": ["python", "数据分析"]}
]
python_items = [item["id"] for item in data if "python" in item["tags"]]
# python_items = []
# for item in data:
#     if "python" in item["tags"]:
#         python_items.append(item["id"])
print(f"包含python标签的ID：{python_items}")

# 4.三维坐标展平
coordinates = [[(1,2), (3,4)], [(5,6), (7,8)]]
all_nums = [num for row in coordinates for point in row for num in point]
# all_nums = []
# for row in coordinates:
#     for point in row:
#         for num in point:
#             all_nums.append(num)
print(f"所有数字：{all_nums}")