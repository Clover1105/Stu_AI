l = [1,2,3,4,5]

# 列表不能直接加常数
# l = l + 1   # 会报错

# 只能通过 for 循环
for i in range(len(l)):
    l[i] += 1
print("list：",l)

# ndarray数组可以直接加常数
import numpy as np
nd_l = np.array(l)
print("转换后类型：",type(nd_l))
print("转换后数据：",nd_l)
nd_l = nd_l + 3
print("ndarray：",nd_l)