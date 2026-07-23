"""
回调函数
    - 将函数作为参数传入另一个函数
    - 被传入的函数在适当的时候被调用
    - 实现代码的灵活性和扩展性
"""
# 1.简单回调函数
def process_data(data, callback):
    """处理数据并调用回调"""
    result = data * 2
    print(f"处理后的数据：{result}")
    callback(result)  # 调用回调函数
def print_result(x):
    print(f"回调函数收到：{x}")
process_data(10, print_result)


# 2.多个回调函数
def calculate(a, b, on_success, on_error):
    """计算并调用相应的回调"""
    try:
        result = a / b
        on_success(result)
    except ZeroDivisionError:
        on_error("除数不能为0")
def success_handler(result):
    print(f"计算成功：{result}")
def error_handler(msg):
    print(f"计算失败：{msg}")
calculate(10, 2, success_handler, error_handler)
calculate(10, 0, success_handler, error_handler)


# 3.排序中的key回调
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
# 使用lambda作为回调
sorted_by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("按成绩排序：")
for s in sorted_by_score:
    print(f"  {s['name']}: {s['score']}")


# 4.自定义排序规则
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]
def get_score_key(student):
    return student["score"]
def get_name_key(student):
    return student["name"]
print("按姓名排序：")
for s in sorted(students, key=get_name_key):
    print(f"  {s['name']}: {s['score']}")