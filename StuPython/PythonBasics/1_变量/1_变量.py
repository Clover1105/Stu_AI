# 1.python中的变量是一种代数思想，写代码的时候变量非常简洁，称之为标识符，变量表示的是一种数据
age = 22
id = 123456
print(age,id)

# 2.变量的取值和存值
# 总结：变量存值，有就更新，没有创建；变量取值，没有就报错，有就取出变量最近一次存的值
x = 100 # 变量不存在，创建变量
print(x)
x = 200 # 变量存在，更新变量
print(x)
# print(c)    # 变量不存在，报错
# print(456)  # python语言是一个脚本语言,前面报错了，这里面的代码不会运行

# 3.变量是一种不加引号的标识符、单词
# 变量名设计公约，见名知意
# 变量的名字规则：字母、数字、下划线的组合，数字不能打头
# 大小驼峰：agent_name、agentName、AgentName
Stu_name = "clover"
stuClass = "python1班"
_ = 123
print(Stu_name,stuClass,_)

# 4.变量保存的数据，有哪些类型的数据？
# 数字、布尔数据、字符串、None、列表、元组、字典、集合、函数、类、对象
# type(): 查看变量保存的数据类型
x = 10  # 数字，整型
print(type(x))
x = 10.1    # 数字，浮点型
print(type(x))
x = True    # 布尔型
print(type(x))
x = "hello" # 字符串
print(type(x))
x = None    # None
print(type(x))
x = [10,20,30]  # 列表
print(type(x))
x = (10,20,30)  # 元组
print(type(x))
x = {10,20,30}  # 集合
print(type(x))
x = {"name":"clover","age":22}  # 字典
print(type(x))



