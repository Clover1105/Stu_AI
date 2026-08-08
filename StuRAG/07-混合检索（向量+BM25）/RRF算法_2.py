# 向量检索结果和BM25检索结果不一定都是一样的
# 不一样的处理思路：分开处理

# 假设检索结果
# -- 向量
one = [{"id2": 0.95}, {"id9": 0.88}, {"id3": 0.65}, {"id5": 0.75}]
# -- BM25
two = [{"id5": 15.2}, {"id2": 12.1}, {"id9": 0.95}, {"id3": 8.5}]

# RRF算法融合计算top-2
l = []
for i,v_item in enumerate(one):
    for v_key in v_item.keys():
        l.append({
            v_key: (1/(60+i))
        })
for j,b_item in enumerate(two):
    for b_key in b_item.keys():
        f = 0
        for l_item in l:
            if b_key in l_item:
                l_item[b_key] += (1/(60+j))
                f = 1
                break
        if f == 0:
            l.append({
                b_key: (1/(60+j))
            })
print(l)

# for i in l:
#     print(list(i.values()))

# 排序
l.sort(key=lambda x: list(x.values())[0], reverse=True)
print(l)