"""
推导式综合应用
    - 结合多个知识点解决实际问题
    - 数据清洗和转换
    - 复杂数据结构处理
"""
# 1.数据清洗 - 过滤并转换
raw_data = ["12", "abc", "34", "56", "xyz", "78", ""]
# 筛选出数字字符串并转为整数
clean_numbers = [int(x) for x in raw_data if x.isdigit()]
print(f"清洗后的数字：{clean_numbers}")


# 2.学生成绩分析
students = [
    {"name": "张三", "chinese": 85, "math": 92, "english": 78},
    {"name": "李四", "chinese": 92, "math": 88, "english": 94},
    {"name": "王五", "chinese": 78, "math": 85, "english": 80}
]
# 计算每个学生的平均分
averages = {s["name"]: (s["chinese"] + s["math"] + s["english"]) / 3 for s in students}
print(f"学生平均分：{averages}")


# 3.找出总分超过250的学生
high_achievers = [
    s["name"] for s in students
    if s["chinese"] + s["math"] + s["english"] > 250
]
print(f"高分学生：{high_achievers}")


# 4.数据分组
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 将数字按奇偶分组
grouped = {"偶数": [x for x in numbers if x % 2 == 0],
           "奇数": [x for x in numbers if x % 2 == 1]}
print(f"分组结果：{grouped}")


# 5.矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# transpose = []
# for i in range(len(matrix[0])):
#     for row in matrix:
#         transpose.append(row[i])
print(f"原矩阵：{matrix}")
print(f"转置后：{transpose}")