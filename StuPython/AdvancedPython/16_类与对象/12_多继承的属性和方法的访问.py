"""
多继承属性查找顺序
    - 多继承时，属性和方法按照继承顺序（继承链）依次查找
    - 先继承的父类优先级更高
    - 一个父类找完再找下一个
"""

# 多继承属性查找
class A:
    x = 10
class B(A):
    y = 20
class C1:
    w = 50
    y = 60  # 与B中的y同名
class C(C1):
    z = 30
class D(C, B):
    q = 40
d = D()
print(f"d.y = {d.y}")  # 按照D->C->C1的顺序，找到C1中的y=60


# 复杂查找示例
class A:
    x = 10
class B(A):
    y = 20
    def fn(self):
        print(self.y)
    def fm(self):
        print(self.x)
class C1:
    y = 60
    def fm(self):
        print(self.z)
class C(C1):
    z = 30
class D(C, B):
    q = 40
d = D()
d.fm()  # (1) D -> C -> C1中有fm ==> self.z = d.z
        # (2) d没有z属性 -> D没有 -> C中有z=30
d.fn()  # (1) D -> C -> C1 -> B中有fn ==> self.y = d.y
        # (2) d没有y属性 -> D没有 -> C没有 -> C1中有y=60