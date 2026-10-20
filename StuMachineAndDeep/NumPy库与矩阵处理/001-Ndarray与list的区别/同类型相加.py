l1 = [11,22,33,44]
l2 = [10,20,30,40]

# 列表直接相加是将两个列表拼接的结果
l = l1 + l2
print("list：",l)

# 依旧需要循环
l = []
for i in range(len(l2)):
    l.append(l1[i]+l2[i])
print("list：",l)

# ndarray 数组可以直接相加
import numpy as np
nd_l1 = np.array(l1)
nd_l2 = np.array(l2)
nd_l = nd_l1 + nd_l2
print("ndarray：",nd_l)