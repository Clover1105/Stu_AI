"""
用面向对象的类语法,实现一个学生成绩管理系统 GradeManager ：
  使用字典存储学生信息
  实现添加学生、删除学生、查找学生、修改成绩功能
  统计全班平均分、最高分、最低分
  使用正则表达式验证学号格式（8位数字）
"""
# import re
# class GradeManager:
#     def __init__(self):
#         self.students = {}
#
#     def add_stu(self,id,name,*grade):
#         self.id = id
#         self.name = name
#         self.grade = grade
#         self.students[name] = {"id":self.id,"grade":self.grade}
#         print(f"学生{id}添加成功")
#
#     def del_stu(self):
#         if self.name:
#             self.students.pop(self.name)
#             print(f"学生{self.name}已删除")
#         else:
#             print(f"删除失败，学生{self.name}不存在")
#
#     def find_stu(self):
#         try:
#             stu = self.students[self.name]
#             print(f"学生{self.name}存在：",stu)
#         except KeyError:
#             print(f"学生{self.name}不存在")
#
#     def update_grade(self,*grade):
#         self.grade = grade
#         self.students[self.name]["grade"] = self.grade
#         print(f"学生{self.name}的成绩已更新")
#
#     def get_avg(self):
#         con = 0
#         l = len(self.grade)
#         for i in self.grade:
#              con += i
#         print(f"学生{self.name}的平均分是：{con/l:.2f}")
#
#     def get_max(self):
#         max_g = max(self.grade)
#         print(f"学生{self.name}的最高分是：{max_g}")
#
#     def get_min(self):
#         min_g = min(self.grade)
#         print(f"学生{self.name}的最低分是：{min_g}")
#
#     def stu_id(self):
#         if re.fullmatch(r"2026\d{4}$",str(self.id)):
#             print(f"学生{self.name}的学号是规范的")
#         else:
#             print(f"学生{self.name}的学号是不规范的")
#
# s1 = GradeManager()
# s2 = GradeManager()
# s3 = GradeManager()
# s4 = GradeManager()
# s1.add_stu("20261001", "A", 90,70,60)
# s2.add_stu("20261002", "b", 80,89,76)
# s3.add_stu("20261003", "C", 85,45,100)
# s4.add_stu("20261004", "D", 99,89,79)
# print()
#
# s1.del_stu()
#
# s1.find_stu()
# s3.find_stu()
#
# s2.find_stu()
# s2.stu_id()
# s2.update_grade(100,90,80)
# s2.find_stu()
#
# s3.get_avg()
# s4.get_max()
# s4.get_min()

# 老师的代码
import re
class GradeManager:
    def __init__(self):
        self.students={}
    def verify_id(self,id):
        res=re.findall("^\d{8}$",id)
        if len(res)==1:
            return True
        else:
            return False
    def add_student(self,id,name,scores=0):
        if self.verify_id(id):
            self.students[id]={"name":name,
                               "scores":scores}
            return "添加成功"
        else:
            return "学号格式不正确"
    def del_student(self,id):
        if id in self.students:
            del self.students[id]
            return "删除成功"
        else:
            return "学号不存在"
    def get_student(self,id):
        if not self.verify_id(id):
            return "学号格式不正确"
        if id in self.students:
            return self.students[id]
        else:
            return "学号不存在"
    def change_score(self,id,score):
        if id in self.students:
            self.students[id]["scores"]=score
            return "修改成功"
        else:
            return "学号不存在"
    def total(self):
        scores=[s["scores"] for s in self.students.values()]
        average=sum(scores)/len(scores)
        max_score=max(scores)
        min_score=min(scores)
        return {"平均分":average,
                "最高分":max_score,
                "最低分":min_score
                }

m1=GradeManager()
m1.add_student("20240429","小美",90)
m1.add_student("20240421","小张",89)
m1.del_student("20240421")
print(m1.get_student("20240429"))
m1.change_score("20240429",95)
print(m1.get_student("20240429"))
print(m1.total())
print(m1.get_student("按上20240429"))
print(m1.get_student("20240421"))
