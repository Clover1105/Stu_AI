# 输出（也是用于开发阶段）
"""
print()输出格式化
    - sep：分隔符，默认空格
    - end：结束符，默认换行
    - flush：立即刷新输出
"""
print("苹果", "香蕉", "橘子", sep="-")    # 用 - 分隔
print("姓名", "年龄", "城市", sep=" | ")  # 用 | 分隔
print("Hello", end=" ")     # 不换行，以空格连接
print("World", end="!!!")   # 不换行，以 !!! 连接
print()  # 换行
a, b, c = 10, 20, 30
print("数值：", a, b, c, sep=", ") #将数值用 , 连接
import time
for i in range(6):  # 遍历6次，输出进度
    # flush=True 刷新输出 ; flush=False 不刷新输出
    print(f"\r加载中...{i*20}%", end="", flush=True)
    time.sleep(0.5)
print("\n完成！")

# 输入（也是用于开发阶段）
"""
input()输入
    - 让程序暂停等待用户输入
    - 返回的是字符串类型
    - 需要类型转换时使用int()/float()
"""
name = input("请输入一个名字：")    # 会让程序暂停在这里，等待程序员在控制台输入
print(f"你好，我是{name}")
num1 = int(input("请输入第一个数字："))  # 输入数字，返回的是字符串类型，需要类型转换时使用int()/float()
num2 = int(input("请输入第二个数字："))
print(f"{num1} + {num2} = {num1 + num2}")
number = int(input("请输入一个整数："))
if number % 2 == 0: # 判断奇偶
    print("偶数")
else:
    print("奇数")







