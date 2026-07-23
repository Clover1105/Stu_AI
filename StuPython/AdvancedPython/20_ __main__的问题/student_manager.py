"""
1. __name__变量：直接运行时为"__main__"，被导入时为模块名
2. if __name__ == "__main__"：区分主程序运行和模块导入
3. 模块自测试：开发阶段调试，导入时不执行
4. 双重用途：同一个文件可以既作为主程序运行，又作为模块导入
"""

"""
学生管理模块 - 可以被导入使用，也可以直接运行测试
"""

class Student:
    """学生类"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"{self.name}: {self.score}分"
class StudentManager:
    """学生管理类"""
    def __init__(self):
        self.students = []
    def add(self, name, score):
        """添加学生"""
        self.students.append(Student(name, score))
        print(f"添加成功：{name}")
    def get_top(self, n=3):
        """获取前n名"""
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)
        return sorted_students[:n]
    def average_score(self):
        """平均分"""
        if not self.students:
            return 0
        total = sum(s.score for s in self.students)
        return total / len(self.students)


# 测试代码 - 只有在直接运行此文件时才会执行
if __name__ == "__main__":
    print("=" * 40)
    print("学生管理系统 - 自测试模式")
    print(f"当前__name__变量值：{__name__}")
    print("=" * 40)

    # 创建管理器实例
    manager = StudentManager()

    # 添加测试数据
    manager.add("张三", 95)
    manager.add("李四", 87)
    manager.add("王五", 92)
    manager.add("赵六", 78)

    # 显示测试结果
    print(f"\n平均分：{manager.average_score()}")
    print("\n前三名：")
    for i, student in enumerate(manager.get_top(3), 1):
        print(f"  {i}. {student}")

    print("\n自测试完成")
else:
    # 被导入时执行的代码
    print(f"学生管理模块已导入，当前__name__={__name__}")