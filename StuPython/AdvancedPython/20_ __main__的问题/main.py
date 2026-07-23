"""
直接运行 student_manager.py：
    __name__ 值为 "__main__"
    执行测试代码，输出自测试信息

运行 main.py：
    student_manager.py 中的 __name__ 值为 "student_manager"
    测试代码不执行，只执行导入代码
    主程序的 __name__ 值为 "__main__"
"""



"""
主程序 - 导入并使用student_manager模块
"""

import student_manager

print("=" * 40)
print("主程序运行模式")
print(f"主程序的__name__值：{__name__}")
print("=" * 40)

# 使用导入的模块
manager = student_manager.StudentManager()
manager.add("小明", 98)
manager.add("小红", 88)
manager.add("小刚", 76)

print(f"\n班级平均分：{manager.average_score()}")

print("\n成绩排名：")
for i, student in enumerate(manager.get_top(), 1):
    print(f"  {i}. {student}")

print("\n提示：上面没有输出模块的测试代码，因为测试代码被if __name__ == '__main__'保护了")